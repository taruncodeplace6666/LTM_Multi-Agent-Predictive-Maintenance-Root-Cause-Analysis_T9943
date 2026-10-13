import os

from dotenv import load_dotenv


load_dotenv()


# ============================================================
# INFLUXDB
# ============================================================

INFLUX_URL = os.getenv(
    "INFLUX_URL",
    "http://localhost:8086"
)

INFLUX_TOKEN = os.getenv(
    "INFLUX_TOKEN",
    ""
)

INFLUX_ORG = os.getenv(
    "INFLUX_ORG",
    "LTM"
)

INFLUX_BUCKET = os.getenv(
    "INFLUX_BUCKET",
    "CNC-1"
)


# ============================================================
# MACHINE
# ============================================================

MACHINE_ID = os.getenv(
    "MACHINE_ID",
    "001"
)


# ============================================================
# REFRESH
# ============================================================

REFRESH_SECONDS = int(
    os.getenv(
        "REFRESH_SECONDS",
        "5"
    )
)


# ============================================================
# VIBRATION THRESHOLDS
# ============================================================

VIBRATION_WARNING = float(
    os.getenv(
        "VIBRATION_WARNING",
        "1500"
    )
)

VIBRATION_CRITICAL = float(
    os.getenv(
        "VIBRATION_CRITICAL",
        "2000"
    )
)