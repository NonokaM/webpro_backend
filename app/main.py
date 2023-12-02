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
def generate():
    image_url = "https://firebasestorage.googleapis.com/v0/b/webpro-10732.appspot.com/o/%E6%B3%A3%E3%81%84%E3%81%A1%E3%82%83%E3%81%A3%E3%81%9F.jpg?alt=media&token=f549db6f-cd5e-47eb-a534-263cceb481e9"

    detection_result=text_detection(image_url)
    response=get_destination(detection_result)
    return {"openai": response}

@app.get("/vision")
def vision_test():
    image_url = "https://firebasestorage.googleapis.com/v0/b/webpro-10732.appspot.com/o/%E6%B3%A3%E3%81%84%E3%81%A1%E3%82%83%E3%81%A3%E3%81%9F.jpg?alt=media&token=f549db6f-cd5e-47eb-a534-263cceb481e9"

    detection_result = text_detection(image_url)
    return {"vision": "test", "detection_result": detection_result}


# @app.get("/generate")
# def generate():
#     response = get_destination()
#     return {"openai": response}
