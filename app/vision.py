import io
import os
import requests
from google.cloud import vision

client = vision.ImageAnnotatorClient()

def text_detection(image_url):
    # 画像データをHTTP経由で取得
    response = requests.get(image_url)
    content = response.content

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    return response.full_text_annotation.text
