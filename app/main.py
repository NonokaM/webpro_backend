from typing import Optional
from test import text_detection
from fastapi import FastAPI
from opneai_api import generate_test

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/vision")
def vision_test():
    detection_result = text_detection()
    return {"vision": "test", "detection_result": detection_result}

@app.get("/generate")
def generate():
    text=text_detection()
