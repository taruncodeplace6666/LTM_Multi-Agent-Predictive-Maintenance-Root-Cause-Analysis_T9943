CSS = """
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
"""