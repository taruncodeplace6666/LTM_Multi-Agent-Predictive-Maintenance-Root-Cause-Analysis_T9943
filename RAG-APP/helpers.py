import os
import streamlit as st
from config import PINNED_CONTEXT_TURNS


def format_docs(docs):
    if not docs:
        return "No relevant context found."
    parts = []
    for doc in docs:
        if hasattr(doc, "page_content"):
            parts.append(doc.page_content)
        elif isinstance(doc, dict):
            parts.append(doc.get("page_content", str(doc)))
        else:
            parts.append(str(doc))
    return "\n\n".join(parts)


def extract_sources(docs):
    """Return list of (filename, raw_chunk) tuples."""
    results = []
    for doc in docs:
        meta = None
        content = ""
        if hasattr(doc, "metadata"):
            meta = doc.metadata
            content = getattr(doc, "page_content", "")
        elif isinstance(doc, dict):
            meta = doc.get("metadata", {})
            content = doc.get("page_content", "")
        if not meta:
            continue
        src = (
            meta.get("source")
            or meta.get("location")
            or meta.get("uri")
            or meta.get("x-amz-bedrock-kb-source-uri")
            or meta.get("title")
        )
        if src:
            src = str(src)
            if "/" in src or "\\" in src:
                src = os.path.basename(src.replace("\\", "/"))
            results.append((src, content))
    return results


def update_pinned_sources(new_sources):
    seen = set(st.session_state.pinned_sources)
    for name, chunk in new_sources:
        if name in seen:
            continue
        st.session_state.pinned_sources.append(name)
        st.session_state.pinned_chunks.append(chunk)
        seen.add(name)

    if len(st.session_state.pinned_sources) > PINNED_CONTEXT_TURNS:
        drop = len(st.session_state.pinned_sources) - PINNED_CONTEXT_TURNS
        st.session_state.pinned_sources = st.session_state.pinned_sources[drop:]
        st.session_state.pinned_chunks = st.session_state.pinned_chunks[drop:]


def build_pinned_context():
    if not st.session_state.pinned_chunks:
        return ""
    parts = []
    for name, chunk in zip(
        st.session_state.pinned_sources, st.session_state.pinned_chunks
    ):
        parts.append(f"[Pinned from {name}]\n{chunk}")
    return "\n\n".join(parts)


def clear_pins():
    st.session_state.pinned_sources = []
    st.session_state.pinned_chunks = []