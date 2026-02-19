import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()  

def get_recent_matches(player_id=None):

    if player_id is None:
        player_id = os.getenv("PLAYER_ID")

    url= f"https://api.opendota.com/api/players/{player_id}/recentMatches"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)