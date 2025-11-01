import streamlit as st
import redis
import json
import time
import pandas as pd

st.title("Redis Latest Message Table")

REDIS_HOST = "localhost"
REDIS_PORT = 6379
CHANNEL = "test_channel"

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
pubsub = r.pubsub()
pubsub.subscribe(CHANNEL)

table_area = st.empty()

while True:
    message = pubsub.get_message()
    if message and message['type'] == 'message':
        try:
            data = json.loads(message['data'])
            df = pd.DataFrame(list(data.items()), columns=["Key", "Value"])
            df["Value"] = df["Value"].astype(str)  # force all values to strings
            table_area.write(df)
        except Exception as e:
            table_area.text(f"Invalid data: {message['data']}")
    time.sleep(0.1)
