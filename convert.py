import os
import time
import json
import logging

import yaml
import mlflow

from huggingface_hub import snapshot_download
from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions
from docling.document_converter import (
    DocumentConverter,
    InputFormat,
    PdfFormatOption,
)
from docling.datamodel.base_models import ConversionStatus

logging.getLogger("docling").setLevel(logging.ERROR)
logging.getLogger("docling_core").setLevel(logging.ERROR)
logging.getLogger("MatchingPostProcessor").setLevel(logging.ERROR)


def load_params(path="params.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def main():
    params = load_params()

    source = params["source_pdf"]
    page_ranges = [tuple(r) for r in params["page_ranges"]]
    ocr_repo = params["ocr_repo"]

    if not os.path.exists(source):
        raise FileNotFoundError(f"Can't find file at: {source}")

    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment("pdf_conversion")

    with mlflow.start_run(run_name=os.path.basename(source)):
        mlflow.log_param("source_file", os.path.basename(source))
        mlflow.log_param("ocr_repo", ocr_repo)
        mlflow.log_param("page_ranges", str(page_ranges))

        print("Downloading RapidOCR models")
        download_path = snapshot_download(repo_id=ocr_repo)

        det_model_path = os.path.join(download_path, "PP-OCRv4", "en_PP-OCRv3_det_infer.onnx")
        rec_model_path = os.path.join(download_path, "PP-OCRv4", "ch_PP-OCRv4_rec_server_infer.onnx")
        cls_model_path = os.path.join(download_path, "PP-OCRv3", "ch_ppocr_mobile_v2.0_cls_train.onnx")

        ocr_options = RapidOcrOptions(
            det_model_path=det_model_path,
            rec_model_path=rec_model_path,
            cls_model_path=cls_model_path,
        )
        pipeline_options = PdfPipelineOptions(ocr_options=ocr_options)

        converter = DocumentConverter(
            format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)},
        )

        input_filename_without_extension = os.path.splitext(os.path.basename(source))[0]
        output_directory = "output"
        os.makedirs(output_directory, exist_ok=True)

        overall_start = time.time()
        range_results = []
        failed_ranges = []
        total_pages_converted = 0

        for start_page, end_page in page_ranges:
            print(f"\nConverting pages {start_page}-{end_page} ...")
            t0 = time.time()

            result = converter.convert(source=source, page_range=(start_page, end_page))
            elapsed = time.time() - t0
            pages = end_page - start_page + 1

            if result.status not in (ConversionStatus.SUCCESS, ConversionStatus.PARTIAL_SUCCESS):
                print(f"  FAILED (status={result.status}) — skipping this range")
                failed_ranges.append([start_page, end_page])
                range_results.append({
                    "start_page": start_page, "end_page": end_page,
                    "status": "failed", "elapsed_seconds": elapsed,
                })
                continue

            md = result.document.export_to_markdown()
            output_filename = f"{input_filename_without_extension}_p{start_page}-{end_page}.md"
            output_path = os.path.join(output_directory, output_filename)

            with open(output_path, "w", encoding="utf-8") as outfile:
                outfile.write(md)

            total_pages_converted += pages
            print(f"  Done in {elapsed:.1f}s ({elapsed/pages:.1f}s/page) -> {output_path}")

            range_results.append({
                "start_page": start_page, "end_page": end_page,
                "status": "success", "elapsed_seconds": elapsed,
                "pages": pages, "output_file": output_path,
                "char_count": len(md),
            })
            mlflow.log_artifact(output_path)

        total_elapsed = time.time() - overall_start

        mlflow.log_metric("total_time_seconds", total_elapsed)
        mlflow.log_metric("pages_converted", total_pages_converted)
        mlflow.log_metric("failed_range_count", len(failed_ranges))
        if total_pages_converted:
            mlflow.log_metric("seconds_per_page", total_elapsed / total_pages_converted)

        metrics = {
            "total_time_seconds": round(total_elapsed, 2),
            "pages_converted": total_pages_converted,
            "failed_range_count": len(failed_ranges),
            "failed_ranges": failed_ranges,
            "range_results": range_results,
        }
        with open("metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)
        mlflow.log_artifact("metrics.json")

        print(f"\nAll ranges complete. Total time: {total_elapsed/60:.1f} minutes")
        print("Metrics written to metrics.json")


if __name__ == "__main__":
    main()
