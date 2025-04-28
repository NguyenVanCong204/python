import requests 
import  pandas as pd
from pandas import json_normalize

response = requests.get('https://data-api.coindesk.com/index/cc/v1/historical/days',
    params={"market":"cadli","instrument":"BTC-USD","limit":30,"aggregate":1,"fill":"true","apply_mapping":"true","response_format":"JSON"},
    headers={"Content-type":"application/json; charset=UTF-8"}
)


dic = response.json()['Data']
df = json_normalize(dic)
df.to_csv('detections.csv', index=False, sep="\t")