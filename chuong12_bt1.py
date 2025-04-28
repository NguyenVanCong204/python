from fastapi import FastAPI
app = FastAPI()
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b
@app.get("/example/")
def hello():
    return {"Hello": "World"}
@app.get("/algebra/plus")
def plus_endpoint(number_1: int, number_2: int):
    return {"result": plus(number_1, number_2)}

@app.get("/algebra/minus")
def minus_endpoint(number_1: int, number_2: int):
    return {"result": minus(6, 5)}



# uvicorn chuong12_bt1:app --reload --port 8009

