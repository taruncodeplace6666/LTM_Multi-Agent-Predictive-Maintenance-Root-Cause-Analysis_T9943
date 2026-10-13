import os
import boto3
import logging
import warnings
import streamlit as st
from datetime import datetime
from langchain_aws import ChatBedrockConverse, AmazonKnowledgeBasesRetriever
from botocore.config import Config

# Silence langchain-community deprecation noise if any leaks through
warnings.filterwarnings("ignore", category=DeprecationWarning)

# =============================================================================
# 1. PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="Programming Manual Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# 2. CUSTOM CSS
# =============================================================================
st.markdown("""
<style>
    .stApp { background: #f7f8fa; }

    .app-header {
        background: #0f172a;
        padding: 1.5rem 2rem;
        border-radius: 10px;
        margin-bottom: 1.4rem;
        border-left: 5px solid #2563eb;
    }
    .app-header h1 {
        margin: 0; font-size: 1.5rem; font-weight: 600;
        letter-spacing: -0.3px; color: #ffffff;
    }
    .app-header p {
        margin: 0.35rem 0 0 0; font-size: 0.88rem; color: #cbd5e1;
    }

    .section-label {
        font-size: 0.72rem; font-weight: 700; letter-spacing: 1.2px;
        text-transform: uppercase; color: #64748b;
        margin: 0.5rem 0 0.6rem 0;
    }

    [data-testid="stChatMessage"] {
        background: #ffffff; border-radius: 10px;
        padding: 1rem 1.2rem; border: 1px solid #e2e8f0;
        margin-bottom: 0.6rem;
    }

    [data-testid="stChatMessage"] code {
        background: #0f172a; color: #e2e8f0;
        padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.85rem;
    }
    [data-testid="stChatMessage"] pre {
        background: #0f172a; border-radius: 8px; border: 1px solid #1e293b;
    }
    [data-testid="stChatMessage"] pre code {
        background: transparent; color: #e2e8f0;
    }

    [data-testid="stSidebar"] {
        background: #ffffff; border-right: 1px solid #e2e8f0;
    }
    [data-testid="stSidebar"] h3 {
        font-size: 0.95rem; font-weight: 700; color: #0f172a;
    }

    .info-row {
        display: flex; justify-content: space-between;
        padding: 0.4rem 0; border-bottom: 1px solid #f1f5f9;
        font-size: 0.85rem;
    }
    .info-row .k { color: #64748b; }
    .info-row .v { color: #0f172a; font-weight: 600; }

    .dot {
        display: inline-block; width: 8px; height: 8px;
        border-radius: 50%; background: #16a34a;
        margin-right: 6px; vertical-align: middle;
    }

    .stButton > button {
        width: 100%; border-radius: 8px; font-weight: 500;
        font-size: 0.85rem; border: 1px solid #cbd5e1;
        background: #ffffff; color: #0f172a;
        transition: all 0.15s ease; text-align: left;
        padding: 0.55rem 0.85rem;
    }
    .stButton > button:hover {
        border-color: #2563eb; color: #2563eb; background: #f8fafc;
    }

    [data-testid="stChatInput"] {
        border-radius: 8px; border: 1px solid #cbd5e1;
    }
    [data-testid="stChatInput"]:focus-within {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
    }

    .welcome-panel {
        background: #ffffff; border: 1px solid #e2e8f0;
        border-radius: 10px; padding: 1.5rem 1.8rem;
        margin-bottom: 1rem;
    }
    .welcome-panel h2 {
        margin: 0 0 0.4rem 0; font-size: 1.1rem;
        color: #0f172a; font-weight: 600;
    }
    .welcome-panel p {
        margin: 0; color: #475569; font-size: 0.9rem; line-height: 1.55;
    }

    .sources-block {
        background: #f8fafc; border-left: 3px solid #2563eb;
        border-radius: 6px; padding: 0.7rem 0.9rem;
        margin-top: 0.6rem; font-size: 0.82rem; color: #334155;
    }
    .sources-block.pinned {
        border-left-color: #64748b; background: #f1f5f9;
    }
    .sources-block .title {
        font-weight: 700; color: #0f172a; font-size: 0.7rem;
        letter-spacing: 1px; text-transform: uppercase;
        margin-bottom: 0.4rem;
    }
    .sources-block .src {
        padding: 0.15rem 0; color: #475569;
        font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
        font-size: 0.8rem;
    }

    .feedback-pill {
        display: inline-block; padding: 0.15rem 0.55rem;
        border-radius: 999px; font-size: 0.72rem; font-weight: 600;
        letter-spacing: 0.4px; text-transform: uppercase;
        margin-left: 0.6rem; vertical-align: middle;
    }
    .feedback-pill.helpful { background: #dcfce7; color: #166534; }
    .feedback-pill.not-helpful { background: #fee2e2; color: #991b1b; }

    div[data-testid="column"] .stButton > button { text-align: center; }

    hr { margin: 0.9rem 0; border-color: #e2e8f0; }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# 3. CONFIGURATION
# =============================================================================
KNOWLEDGE_BASE_ID = "84R9EDOLXD"  # Replace with your actual KB ID
REGION_NAME = "ap-south-1"
PINNED_CONTEXT_TURNS = 3

@st.cache_resource(show_spinner=False)
def get_session():
    return boto3.Session(profile_name="Bedrock-admin", region_name=REGION_NAME)

session = get_session()
logging.basicConfig(level=logging.CRITICAL)

# =============================================================================
# 4. MODEL
# =============================================================================
@st.cache_resource(show_spinner=False)
def get_model():
    return ChatBedrockConverse(
        model="apac.amazon.nova-lite-v1:0",
        max_tokens=2048,
        temperature=0.0,
        top_p=1,
        region_name=REGION_NAME,
        client=session.client("bedrock-runtime"),
        config=Config(
            connect_timeout=3600,
            read_timeout=3600,
            retries={"max_attempts": 1},
        ),
    )

model = get_model()

# =============================================================================
# 5. RETRIEVER
# =============================================================================
@st.cache_resource(show_spinner=False)
def get_retriever():
    return AmazonKnowledgeBasesRetriever(
        knowledge_base_id=KNOWLEDGE_BASE_ID,
        region_name=REGION_NAME,
        client=session.client("bedrock-agent-runtime"),
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 10}},
    )

retriever = get_retriever()

# =============================================================================
# 6. SESSION STATE
# =============================================================================
# chat_history is a plain list of ("user" | "assistant", text) tuples.
# We manage it ourselves; no langchain-community classes needed.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "messages" not in st.session_state:
    st.session_state.messages = []
if "query_count" not in st.session_state:
    st.session_state.query_count = 0
if "pinned_sources" not in st.session_state:
    st.session_state.pinned_sources = []
if "pinned_chunks" not in st.session_state:
    st.session_state.pinned_chunks = []
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

# =============================================================================
# 7. HELPERS
# =============================================================================
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


# =============================================================================
# 8. MESSAGE BUILDER (no templates, no brace issues)
# =============================================================================
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


# =============================================================================
# 9. RETRIEVAL
# =============================================================================
def retrieve_docs(question):
    return retriever.invoke(question)


# =============================================================================
# 10. SIDEBAR
# =============================================================================
with st.sidebar:
    st.markdown("### Programming Manual Assistant")
    st.caption("Documentation lookup for machine programming")
    st.divider()

    st.markdown('<div class="section-label">System</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="info-row"><span class="k">Status</span>'
        f'<span class="v"><span class="dot"></span>Online</span></div>'
        f'<div class="info-row"><span class="k">Model</span>'
        f'<span class="v">Nova Lite</span></div>'
        f'<div class="info-row"><span class="k">Region</span>'
        f'<span class="v">{REGION_NAME}</span></div>'
        f'<div class="info-row"><span class="k">Queries</span>'
        f'<span class="v">{st.session_state.query_count}</span></div>',
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown('<div class="section-label">Pinned context</div>', unsafe_allow_html=True)
    if st.session_state.pinned_sources:
        for name in st.session_state.pinned_sources:
            st.markdown(
                f'<div class="info-row"><span class="k" '
                f'style="font-family:ui-monospace,monospace;font-size:0.78rem;">'
                f'{name}</span></div>',
                unsafe_allow_html=True,
            )
        if st.button("Unpin all sources", use_container_width=True):
            clear_pins()
            st.rerun()
    else:
        st.caption(
            "No pinned sources yet. Sources from recent answers are "
            "pinned automatically."
        )

    st.divider()
    st.markdown('<div class="section-label">Actions</div>', unsafe_allow_html=True)

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.messages = []
        st.session_state.query_count = 0
        clear_pins()
        st.rerun()

    if st.session_state.messages:
        transcript = "\n\n".join(
            f"[{m['role'].upper()}]\n{m['content']}"
            for m in st.session_state.messages
        )
        st.download_button(
            "Download transcript",
            data=transcript,
            file_name=f"manual_assistant_{datetime.now():%Y%m%d_%H%M%S}.txt",
            mime="text/plain",
            use_container_width=True,
        )

    st.divider()
    with st.expander("About"):
        st.markdown(
            "Answers are grounded in the ingested programming manual "
            "chapters. Sources from recent turns are pinned and reused "
            "for follow-up questions."
        )

# =============================================================================
# 11. HEADER
# =============================================================================
st.markdown(
    """
    <div class="app-header">
        <h1>Programming Manual Assistant</h1>
        <p>Ask about options, features, parameters, and procedures from the programming documentation</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =============================================================================
# 12. SUGGESTIONS
# =============================================================================
SUGGESTIONS = [
    "What options are available in the Feature List?",
    "Show the features described in section F6.1.",
    "What does section 6.1 Introduction cover?",
    "Which options require special programming considerations?",
]

if not st.session_state.messages:
    st.markdown(
        """
        <div class="welcome-panel">
            <h2>Start a documentation query</h2>
            <p>
                Ask about programming options, features, parameters, or procedures.
                The assistant retrieves the relevant manual sections and answers with
                exact chapter references and unmodified code or identifiers.
                Recent sources stay pinned across follow-up questions.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="section-label">Suggested questions</div>',
        unsafe_allow_html=True,
    )
    for i, suggestion in enumerate(SUGGESTIONS):
        if st.button(suggestion, key=f"sugg_{i}", use_container_width=True):
            st.session_state.pending_prompt = suggestion
            st.rerun()

# =============================================================================
# 13. RENDER CHAT HISTORY
# =============================================================================
def render_feedback_pill(rating):
    if rating == "up":
        return '<span class="feedback-pill helpful">Helpful</span>'
    if rating == "down":
        return '<span class="feedback-pill not-helpful">Not helpful</span>'
    return ""


def log_feedback(idx, value):
    st.session_state.messages[idx]["feedback"] = value
    question_text = ""
    if idx > 0 and st.session_state.messages[idx - 1]["role"] == "user":
        question_text = st.session_state.messages[idx - 1]["content"][:200]
    answer_text = st.session_state.messages[idx]["content"][:200]
    line = (
        f"{datetime.now().isoformat()}\t"
        f"idx={idx}\t"
        f"rating={value}\t"
        f"q={question_text!r}\t"
        f"a={answer_text!r}\n"
    )
    try:
        with open("feedback.log", "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass
    st.rerun()


for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        if msg.get("sources"):
            st.markdown(
                '<div class="sources-block">'
                '<div class="title">Sources</div>'
                + "".join(f'<div class="src">{s}</div>' for s in msg["sources"])
                + "</div>",
                unsafe_allow_html=True,
            )

        if msg.get("pinned_used"):
            st.markdown(
                '<div class="sources-block pinned">'
                '<div class="title">Pinned context used</div>'
                + "".join(
                    f'<div class="src">{s}</div>' for s in msg["pinned_used"]
                )
                + "</div>",
                unsafe_allow_html=True,
            )

        if msg["role"] == "assistant" and not msg.get("streaming"):
            fb = msg.get("feedback")
            col1, col2, col3 = st.columns([1, 1, 6])
            with col1:
                if st.button(
                    "Helpful",
                    key=f"fb_up_{i}",
                    use_container_width=True,
                    disabled=(fb == "up"),
                ):
                    log_feedback(i, "up")
            with col2:
                if st.button(
                    "Not helpful",
                    key=f"fb_down_{i}",
                    use_container_width=True,
                    disabled=(fb == "down"),
                ):
                    log_feedback(i, "down")
            with col3:
                if fb:
                    st.markdown(render_feedback_pill(fb), unsafe_allow_html=True)

        if msg.get("timestamp"):
            st.caption(msg["timestamp"])

# =============================================================================
# 14. CHAT INPUT + STREAMING
# =============================================================================
prompt = st.chat_input("Ask about programming options, features, or procedures...")

if st.session_state.pending_prompt:
    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

if prompt:
    timestamp = datetime.now().strftime("%H:%M:%S")

    # --- User message ---
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
            "timestamp": timestamp,
            "sources": [],
            "pinned_used": [],
            "feedback": None,
        }
    )
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(timestamp)

    # --- Assistant message (streaming) ---
    with st.chat_message("assistant"):
        placeholder = st.empty()
        status = st.empty()
        status.caption("Searching documentation...")

        try:
            # 1) Retrieve
            docs = retrieve_docs(prompt)
            src_pairs = extract_sources(docs)
            src_names = [name for name, _ in src_pairs]

            # 2) Snapshot pins BEFORE updating
            pinned_used = list(st.session_state.pinned_sources)

            # 3) Update pins
            update_pinned_sources(src_pairs)

            # 4) Build messages (no template, no brace risk)
            prompt_messages = build_messages(
                prompt, docs, st.session_state.chat_history
            )

            # 5) Stream
            status.caption("Generating answer...")
            accumulated = ""
            for chunk in model.stream(prompt_messages):
                piece = getattr(chunk, "content", "")
                if isinstance(piece, list):
                    piece = "".join(
                        b.get("text", "") if isinstance(b, dict) else str(b)
                        for b in piece
                    )
                if piece:
                    accumulated += piece
                    placeholder.markdown(accumulated + " |")

            placeholder.markdown(accumulated)
            status.empty()

            # 6) Update our own history (plain list of tuples)
            st.session_state.chat_history.append(("user", prompt))
            st.session_state.chat_history.append(("assistant", accumulated))

            # 7) Persist assistant message
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": accumulated,
                    "sources": src_names,
                    "pinned_used": pinned_used,
                    "feedback": None,
                    "timestamp": datetime.now().strftime("%H:%M:%S"),
                }
            )
            st.session_state.query_count += 1

            # 8) Rerun so sources + feedback render cleanly
            st.rerun()

        except Exception as e:
            status.empty()
            error_msg = f"**Error:** {str(e)}"
            placeholder.error(error_msg)
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_msg,
                    "sources": [],
                    "pinned_used": [],
                    "feedback": None,
                    "timestamp": datetime.now().strftime("%H:%M:%S"),
                }
            )