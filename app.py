from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/example/{parameter}")
def example(parameter: str):
    return {
        "parameter": parameter,
        "datetime": datetime.datetime.now().time()
    }

@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }