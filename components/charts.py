import plotly.express as px
import streamlit as st


# ============================================================
# X-AXIS CHART
# ============================================================

def display_x_chart(df):

    axis_df = df[df["axis"] == "X"]

    if axis_df.empty:
        st.info("No X-axis vibration data available.")
        return

    fig = px.line(
        axis_df,
        x="time",
        y="value",
        labels={
            "time": "Time",
            "value": "Vibration X"
        },
        title="Vibration X"
    )

    fig.update_layout(
        height=350,
        hovermode="x unified",
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    fig.update_traces(
        line=dict(width=2)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# Y-AXIS CHART
# ============================================================

def display_y_chart(df):

    axis_df = df[df["axis"] == "Y"]

    if axis_df.empty:
        st.info("No Y-axis vibration data available.")
        return

    fig = px.line(
        axis_df,
        x="time",
        y="value",
        labels={
            "time": "Time",
            "value": "Vibration Y"
        },
        title="Vibration Y"
    )

    fig.update_layout(
        height=350,
        hovermode="x unified",
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    fig.update_traces(
        line=dict(width=2)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# Z-AXIS CHART
# ============================================================

def display_z_chart(df):

    axis_df = df[df["axis"] == "Z"]

    if axis_df.empty:
        st.info("No Z-axis vibration data available.")
        return

    fig = px.line(
        axis_df,
        x="time",
        y="value",
        labels={
            "time": "Time",
            "value": "Vibration Z"
        },
        title="Vibration Z"
    )

    fig.update_layout(
        height=350,
        hovermode="x unified",
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    fig.update_traces(
        line=dict(width=2)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )