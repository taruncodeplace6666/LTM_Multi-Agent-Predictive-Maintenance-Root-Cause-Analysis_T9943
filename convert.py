
import os

from huggingface_hub import snapshot_download

from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    RapidOcrOptions,
)

from docling.document_converter import (
    ConversionResult,
    DocumentConverter,
    InputFormat,
    PdfFormatOption,
)


# --------------------------------------------------
# Paths
# --------------------------------------------------

INPUT_DIRECTORY = r"C:\Users\T9943\project-1\input"
OUTPUT_DIRECTORY = r"C:\Users\T9943\project-1\output"


def main():

    # --------------------------------------------------
    # Create output directory
    # --------------------------------------------------

    os.makedirs(
        OUTPUT_DIRECTORY,
        exist_ok=True
    )

    # --------------------------------------------------
    # Find all PDF files
    # --------------------------------------------------

    pdf_files = [
        os.path.join(
            INPUT_DIRECTORY,
            filename
        )
        for filename in os.listdir(INPUT_DIRECTORY)
        if filename.lower().endswith(".pdf")
    ]

    pdf_files.sort()

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in: {INPUT_DIRECTORY}"
        )

    print("=" * 70)
    print(f"Found {len(pdf_files)} PDF files")
    print("=" * 70)

    for pdf in pdf_files:
        print(os.path.basename(pdf))

    # --------------------------------------------------
    # Download RapidOCR models
    # --------------------------------------------------

    print("\nDownloading RapidOCR models...")

    download_path = snapshot_download(
        repo_id="SWHL/RapidOCR"
    )

    print("RapidOCR models downloaded.\n")

    # --------------------------------------------------
    # RapidOCR model paths
    # --------------------------------------------------

    det_model_path = os.path.join(
        download_path,
        "PP-OCRv4",
        "en_PP-OCRv3_det_infer.onnx"
    )

    rec_model_path = os.path.join(
        download_path,
        "PP-OCRv4",
        "ch_PP-OCRv4_rec_server_infer.onnx"
    )

    cls_model_path = os.path.join(
        download_path,
        "PP-OCRv3",
        "ch_ppocr_mobile_v2.0_cls_train.onnx"
    )

    # --------------------------------------------------
    # Setup RapidOCR
    # --------------------------------------------------

    ocr_options = RapidOcrOptions(
        det_model_path=det_model_path,
        rec_model_path=rec_model_path,
        cls_model_path=cls_model_path,
    )

    pipeline_options = PdfPipelineOptions(
        ocr_options=ocr_options
    )

    # --------------------------------------------------
    # Create Docling converter
    # --------------------------------------------------

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options,
            ),
        },
    )

    # --------------------------------------------------
    # Convert all PDFs
    # --------------------------------------------------

    print("=" * 70)
    print("STARTING PDF → MARKDOWN CONVERSION")
    print("=" * 70)

    for index, source in enumerate(
        pdf_files,
        start=1
    ):

        input_filename = os.path.basename(source)

        input_filename_without_extension = (
            os.path.splitext(input_filename)[0]
        )

        output_filename = (
            f"{input_filename_without_extension}.md"
        )

        output_path = os.path.join(
            OUTPUT_DIRECTORY,
            output_filename
        )

        print("\n")
        print("-" * 70)
        print(
            f"[{index}/{len(pdf_files)}] "
            f"{input_filename}"
        )
        print("-" * 70)

        try:

            # Convert PDF
            conversion_result: ConversionResult = (
                converter.convert(
                    source=source
                )
            )

            # Get document
            doc = conversion_result.document

            # Export to Markdown
            md = doc.export_to_markdown()

            # Save Markdown
            with open(
                output_path,
                "w",
                encoding="utf-8"
            ) as outfile:

                outfile.write(md)

            print(
                f"SUCCESS"
            )

            print(
                f"Markdown written to:"
            )

            print(
                output_path
            )

        except Exception as e:

            print(
                f"FAILED: {input_filename}"
            )

            print(
                f"Error: {e}"
            )

    # --------------------------------------------------
    # Finished
    # --------------------------------------------------

    print("\n")
    print("=" * 70)
    print("CONVERSION COMPLETE")
    print("=" * 70)

    print(
        f"Output directory:\n"
        f"{OUTPUT_DIRECTORY}"
    )


if __name__ == "__main__":
    main()

