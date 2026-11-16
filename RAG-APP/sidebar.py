import streamlit as st
from datetime import datetime
from config import REGION_NAME
from helpers import clear_pins


def render_sidebar():
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