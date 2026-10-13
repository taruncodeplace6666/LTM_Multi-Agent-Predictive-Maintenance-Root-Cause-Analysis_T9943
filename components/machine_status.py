import streamlit as st

from src.metrics import (
    get_machine_status,
    get_status_description
)


def display_machine_status(values):

    status = get_machine_status(
        values
    )

    description = get_status_description(
        values
    )

    if status == "NORMAL":

        st.success(
            f"🟢 MACHINE STATUS: {status}\n\n"
            f"{description}"
        )

    elif status == "WARNING":

        st.warning(
            f"🟡 MACHINE STATUS: {status}\n\n"
            f"{description}"
        )

    elif status == "CRITICAL":

        st.error(
            f"🔴 MACHINE STATUS: {status}\n\n"
            f"{description}"
        )

    else:

        st.info(
            f"⚪ MACHINE STATUS: {status}\n\n"
            f"{description}"
        )