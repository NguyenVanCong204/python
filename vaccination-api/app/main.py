from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import os

app = FastAPI()
CSV_FILE = "app/data.csv"

# Đảm bảo file CSV có header nếu chưa có
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["cccd", "name", "phone"])

class User(BaseModel):
    cccd: str
    name: str
    phone: str

@app.post("/add_user")
def add_user(user: User):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.cccd, user.name, user.phone])
    return {"message": "User added successfully."}

@app.get("/get_user/{name}")
def get_user(name: str):
    results = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"].lower() == name.lower():
                results.append(row)
    if not results:
        raise HTTPException(status_code=404, detail="User not found")
    return results
