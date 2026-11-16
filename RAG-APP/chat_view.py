import streamlit as st
from datetime import datetime


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


def render_chat_history():
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