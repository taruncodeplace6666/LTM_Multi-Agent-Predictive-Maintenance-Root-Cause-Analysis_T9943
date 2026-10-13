import streamlit as st

from streamlit_autorefresh import st_autorefresh

import config

from src.influxdb_client import (
    get_vibration_data
)

from src.data_processing import (
    prepare_vibration_data,
    get_latest_values
)

from components.kpi_cards import (
    display_kpi_cards
)

from components.charts import (
    display_x_chart,
    display_y_chart,
    display_z_chart
)

from components.machine_status import (
    display_machine_status
)

from components.alerts import (
    display_alerts
)

from components.machine_3d import (
    display_machine_3d
)


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="CNC Machine Monitoring",
    page_icon="⚙️",
    layout="wide"
)


# ============================================================
# AUTO REFRESH
# ============================================================

st_autorefresh(
    interval=config.REFRESH_SECONDS * 1000,
    key="cnc_refresh"
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "⚙️ CNC Machine Monitoring"
)

st.caption(
    "Real-time CNC vibration monitoring "
    "using InfluxDB and Streamlit"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "Dashboard Settings"
)


time_range = st.sidebar.selectbox(
    "Time Range",
    [
        "Last 5 minutes",
        "Last 15 minutes",
        "Last 30 minutes",
        "Last 1 hour",
        "Last 6 hours",
        "Last 24 hours"
    ],
    index=2
)


range_map = {

    "Last 5 minutes": "-5m",

    "Last 15 minutes": "-15m",

    "Last 30 minutes": "-30m",

    "Last 1 hour": "-1h",

    "Last 6 hours": "-6h",

    "Last 24 hours": "-24h"
}


selected_range = range_map[
    time_range
]


st.sidebar.divider()


st.sidebar.write(
    f"**Machine ID:** {config.MACHINE_ID}"
)

st.sidebar.write(
    f"**Organization:** {config.INFLUX_ORG}"
)

st.sidebar.write(
    f"**Bucket:** {config.INFLUX_BUCKET}"
)

st.sidebar.write(
    "**Measurement:** cnc"
)

st.sidebar.write(
    f"**Refresh:** {config.REFRESH_SECONDS}s"
)


# ============================================================
# LOAD DATA
# ============================================================

try:

    records = get_vibration_data(
        start=selected_range
    )

    df = prepare_vibration_data(
        records
    )

except Exception as e:

    st.error(
        "Unable to connect to InfluxDB."
    )

    st.error(
        str(e)
    )

    st.info(
        "Check your InfluxDB URL, token, "
        "organization and bucket."
    )

    st.stop()



# ============================================================
# LATEST VALUES
# ============================================================

latest_values = get_latest_values(df)

# Temporary debugging: display the actual data
st.write("DEBUG latest_values:", latest_values)


# ============================================================
# MACHINE STATUS
# ============================================================

display_machine_status(
    latest_values
)


st.divider()


# ============================================================
# KPI
# ============================================================

st.subheader(
    "Current Vibration"
)


display_kpi_cards(
    latest_values
)


st.divider()


# ============================================================
# SEPARATE X / Y / Z GRAPHS
# ============================================================

st.subheader(
    "Vibration Analysis"
)


# ------------------------------------------------------------
# X AXIS
# ------------------------------------------------------------

st.markdown(
    "### Vibration X"
)

display_x_chart(
    df
)


# ------------------------------------------------------------
# Y AXIS
# ------------------------------------------------------------

st.markdown(
    "### Vibration Y"
)

display_y_chart(
    df
)


# ------------------------------------------------------------
# Z AXIS
# ------------------------------------------------------------

st.markdown(
    "### Vibration Z"
)

display_z_chart(
    df
)


st.divider()


# ============================================================
# ALERTS + 3D
# ============================================================

left, right = st.columns(
    [1, 1]
)


with left:

    display_alerts(
        latest_values
    )


with right:

    display_machine_3d(latest_values)


st.divider()


# ============================================================
# DATA TABLE
# ============================================================

st.subheader(
    "Vibration Data"
)


if df.empty:

    st.info(
        "No vibration data available."
    )

else:

    table_df = df[
        [
            "time",
            "axis",
            "value"
        ]
    ].copy()


    table_df.columns = [
        "Time",
        "Axis",
        "Vibration"
    ]


    st.dataframe(
        table_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.caption(
    f"CNC Machine {config.MACHINE_ID} | "
    f"InfluxDB: {config.INFLUX_URL} | "
    f"Bucket: {config.INFLUX_BUCKET} | "
    f"Auto-refresh: {config.REFRESH_SECONDS} seconds"
)