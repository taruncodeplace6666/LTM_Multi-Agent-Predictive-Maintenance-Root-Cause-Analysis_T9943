import streamlit as st


def init_state():
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