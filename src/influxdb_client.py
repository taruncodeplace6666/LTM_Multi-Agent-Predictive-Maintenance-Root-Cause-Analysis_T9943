from influxdb_client import InfluxDBClient

import config


# ============================================================
# CREATE CLIENT
# ============================================================

def get_client():

    return InfluxDBClient(
        url=config.INFLUX_URL,
        token=config.INFLUX_TOKEN,
        org=config.INFLUX_ORG
    )


# ============================================================
# GET VIBRATION DATA
# ============================================================

def get_vibration_data(start="-30m"):

    client = get_client()

    query_api = client.query_api()

    query = f'''
from(bucket: "{config.INFLUX_BUCKET}")
  |> range(start: {start})
  |> filter(fn: (r) => r["_measurement"] == "cnc")
  |> filter(fn: (r) =>
      r["_field"] == "vibration_x" or
      r["_field"] == "vibration_y" or
      r["_field"] == "vibration_z"
  )
'''

    try:

        tables = query_api.query(
            query=query,
            org=config.INFLUX_ORG
        )

        records = []

        for table in tables:

            for record in table.records:

                records.append(
                    {
                        "time": record.get_time(),
                        "field": record.get_field(),
                        "value": record.get_value()
                    }
                )

        return records

    finally:

        client.close()


# ============================================================
# TEST CONNECTION
# ============================================================

def test_connection():

    client = get_client()

    try:

        health = client.health()

        return health.status == "pass"

    except Exception:

        return False

    finally:

        client.close()