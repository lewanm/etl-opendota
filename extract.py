import requests
import pandas as pd
from transform import transform_matches
from load import create_table, load_matches

PLAYER_ID = 86745912

def get_recent_matches(player_id):
    url= f"https://api.opendota.com/api/players/{player_id}/recentMatches"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = get_recent_matches(PLAYER_ID)
    clean_df = transform_matches(df)
    
    create_table()
    load_matches(clean_df)
