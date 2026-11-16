import streamlit as st

SUGGESTIONS = [
    "What options are available in the Feature List?",
    "Show the features described in section F6.1.",
    "What does section 6.1 Introduction cover?",
    "Which options require special programming considerations?",
]


def render_header():
    st.markdown(
        """
        <div class="app-header">
            <h1>Programming Manual Assistant</h1>
            <p>Ask about options, features, parameters, and procedures from the programming documentation</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_suggestions():
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