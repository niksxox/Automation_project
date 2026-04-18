import requests
import pandas as pd
import sqlite3
from datetime import datetime

def run_pipeline():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Task Started: {timestamp}")

    api_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(api_url)
    
    if response.status_code != 200:
        return

    data = response.json()
    df = pd.DataFrame(data)

    df['city'] = df['address'].apply(lambda x: x['city'])
    processed_df = df[['id', 'name', 'email', 'city']].copy()

    processed_df['email'] = processed_df['email'].str.lower()
    processed_df['name'] = processed_df['name'].str.replace('Mrs. ', '', regex=False)
    processed_df['name'] = processed_df['name'].str.replace('Mr. ', '', regex=False)

    db_connection = sqlite3.connect('warehouse.db')
    processed_df.to_sql('user_records', db_connection, if_exists='replace', index=False)
    db_connection.close()

    print(f"Task Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    run_pipeline()