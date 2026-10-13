import streamlit as st

import config

from src.metrics import (
    get_axis_status
)


def display_alerts(values):

    st.subheader(
        "Vibration Alerts"
    )

    alerts_found = False

    for axis in [
        "X",
        "Y",
        "Z"
    ]:

        value = values.get(axis)

        status = get_axis_status(
            value
        )

        if status == "CRITICAL":

            alerts_found = True

            st.error(
                f"🔴 {axis}-Axis Critical | "
                f"Value: {value:,.3f} | "
                f"Limit: {config.VIBRATION_CRITICAL:,.0f}"
            )

        elif status == "WARNING":

            alerts_found = True

            st.warning(
                f"🟡 {axis}-Axis Warning | "
                f"Value: {value:,.3f} | "
                f"Limit: {config.VIBRATION_WARNING:,.0f}"
            )

    if not alerts_found:

        st.success(
            "No active vibration alerts."
        )