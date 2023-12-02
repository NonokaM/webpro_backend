from typing import Optional
from fastapi import FastAPI
from vision import text_detection
from gpt import get_destination

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/generate")
def generate(image_url: str):
    detection_result=text_detection(image_url)
    response=get_destination(detection_result)
    return {"openai": response}


# @app.get("/vision")
# def vision_test(image_url: str):
#     detection_result = text_detection(image_url)
#     return {"vision": "test", "detection_result": detection_result}
