import streamlit as st
from datetime import datetime
from aws import model
from helpers import extract_sources, update_pinned_sources
from prompts import build_messages
from retrieval import retrieve_docs


def handle_chat_input():
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