import pandas as pd


# ============================================================
# PREPARE DATA
# ============================================================

def prepare_vibration_data(records):

    if not records:

        return pd.DataFrame(
            columns=[
                "time",
                "field",
                "value",
                "axis"
            ]
        )

    df = pd.DataFrame(records)

    # Time
    df["time"] = pd.to_datetime(
        df["time"],
        errors="coerce"
    )

    # Numeric conversion
    df["value"] = pd.to_numeric(
        df["value"],
        errors="coerce"
    )

    # Remove invalid values
    df = df.dropna(
        subset=[
            "time",
            "value"
        ]
    )

    # Convert field to axis
    df["axis"] = df["field"].map(
        {
            "vibration_x": "X",
            "vibration_y": "Y",
            "vibration_z": "Z"
        }
    )

    # Remove unknown fields
    df = df.dropna(
        subset=["axis"]
    )

    # Sort by time
    df = df.sort_values(
        "time"
    )

    return df.reset_index(
        drop=True
    )


# ============================================================
# LATEST X Y Z
# ============================================================

def get_latest_values(df):

    values = {
        "X": None,
        "Y": None,
        "Z": None
    }

    if df.empty:

        return values

    for axis in [
        "X",
        "Y",
        "Z"
    ]:

        axis_data = df[
            df["axis"] == axis
        ]

        if not axis_data.empty:

            values[axis] = float(
                axis_data.iloc[-1]["value"]
            )

    return values