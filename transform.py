import pandas as pd

def transform_matches(df):
    df["duration_minutes"] = df["duration"] / 60
    df["kda"] = (df["kills"] + df["assists"]) / df["deaths"].replace(0, 1)

    df = df[[
        "match_id",
        "hero_id",
        "kills",
        "deaths",
        "assists",
        "kda",
        "duration_minutes"
    ]]

    return df
