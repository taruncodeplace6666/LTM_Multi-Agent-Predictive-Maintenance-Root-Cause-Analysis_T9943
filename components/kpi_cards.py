import streamlit as st


def display_kpi_cards(values):

    col1, col2, col3 = st.columns(3)

    # ========================================================
    # X
    # ========================================================

    with col1:

        value = values.get("X")

        if value is None:

            st.metric(
                "Vibration X",
                "No data"
            )

        else:

            st.metric(
                "Vibration X",
                f"{value:,.3f}"
            )

    # ========================================================
    # Y
    # ========================================================

    with col2:

        value = values.get("Y")

        if value is None:

            st.metric(
                "Vibration Y",
                "No data"
            )

        else:

            st.metric(
                "Vibration Y",
                f"{value:,.3f}"
            )

    # ========================================================
    # Z
    # ========================================================

    with col3:

        value = values.get("Z")

        if value is None:

            st.metric(
                "Vibration Z",
                "No data"
            )

        else:

            st.metric(
                "Vibration Z",
                f"{value:,.3f}"
            )