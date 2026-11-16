from helpers import build_pinned_context, format_docs

SYSTEM_RULES = (
    "You are Programming Manual Assistant, a specialist assistant for "
    "technical programming documentation for industrial control systems "
    "and machine programming.\n\n"
    "You answer using ONLY the retrieved context and any pinned context. "
    "Follow these rules:\n"
    "1. Cite chapter and section references exactly as they appear "
    "(for example: Chapter 6.2, section F6.1).\n"
    "2. For procedures, present numbered steps in the order they appear "
    "in the manual.\n"
    "3. For parameters, options, or feature lists, use tables or "
    "bullet lists.\n"
    "4. Reproduce code blocks, G-code, syntax, parameter names, and "
    "identifiers EXACTLY, without paraphrasing.\n"
    "5. If a figure or image is referenced, state: "
    "'Refer to the figure in the source document.'\n"
    "6. If the context does not contain the answer, state: "
    "'This is not covered in the retrieved documentation.'\n"
    "7. Keep answers concise and technical. Avoid filler."
)


def build_messages(question: str, docs, history_messages):
    """
    Build the message list manually. No ChatPromptTemplate, no str.format,
    so any { or } inside the manual chunks or the user question is safe.
    """
    context = format_docs(docs)
    pinned_context = build_pinned_context()

    if pinned_context:
        pinned_section = (
            "Pinned context from previous turns (still relevant):\n"
            "-----------------------------------------------\n"
            f"{pinned_context}\n"
            "-----------------------------------------------\n"
        )
    else:
        pinned_section = ""

    system_text = (
        SYSTEM_RULES
        + "\n\n"
        + pinned_section
        + "\nContext from documentation (this turn):\n"
        "-----------------------------\n"
        f"{context}\n"
        "-----------------------------\n"
    )

    messages = [("system", system_text)]

    # Replay prior turns
    for role, content in history_messages:
        messages.append((role, content))

    # Current user turn
    messages.append(("user", question))
    return messages