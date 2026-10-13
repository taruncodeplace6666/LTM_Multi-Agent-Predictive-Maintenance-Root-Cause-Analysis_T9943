import math

import config


# ============================================================
# MAX VIBRATION
# ============================================================

def get_max_vibration(values):

    valid_values = []

    for value in values.values():

        if value is None:
            continue

        value = float(value)

        if math.isfinite(value):

            valid_values.append(
                abs(value)
            )

    if not valid_values:

        return None

    return max(valid_values)


# ============================================================
# MACHINE STATUS
# ============================================================

def get_machine_status(values):

    max_vibration = get_max_vibration(
        values
    )

    if max_vibration is None:

        return "NO DATA"

    if max_vibration >= config.VIBRATION_CRITICAL:

        return "CRITICAL"

    if max_vibration >= config.VIBRATION_WARNING:

        return "WARNING"

    return "NORMAL"


# ============================================================
# DESCRIPTION
# ============================================================

def get_status_description(values):

    status = get_machine_status(
        values
    )

    if status == "CRITICAL":

        return "Critical vibration detected."

    if status == "WARNING":

        return "High vibration detected."

    if status == "NORMAL":

        return "Machine operating normally."

    return "Waiting for vibration data."


# ============================================================
# AXIS STATUS
# ============================================================

def get_axis_status(value):

    if value is None:

        return "NO DATA"

    value = abs(float(value))

    if value >= config.VIBRATION_CRITICAL:

        return "CRITICAL"

    if value >= config.VIBRATION_WARNING:

        return "WARNING"

    return "NORMAL"