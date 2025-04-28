import pandas as pd
from fastapi import FastAPI
app = FastAPI()
df = pd.read_csv('fruit.csv')

@app.get("/lookup_price/")
def lookup_price_function(name: str):
  idx_item = df[df['fruit'] == name]
  price = idx_item['price'].values[-1]

  return {'name': name, 'price': str(price)}
    