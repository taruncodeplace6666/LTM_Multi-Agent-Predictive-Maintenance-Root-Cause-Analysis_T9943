import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import streamlit as st

# 1. Page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Programming Manual Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
)

import logging
logging.basicConfig(level=logging.CRITICAL)

# 2. Local modules (aws.py triggers boto3 + model + retriever init at import time)
from styles import CSS
from state import init_state
from sidebar import render_sidebar
from chat_ui import render_header, render_suggestions
from chat_view import render_chat_history
from chat_handler import handle_chat_input

# 3. Inject CSS
st.markdown(CSS, unsafe_allow_html=True)

# 4. Session state
init_state()

# 5. Render (order matches original flow)
render_sidebar()
render_header()
render_suggestions()
render_chat_history()
handle_chat_input()