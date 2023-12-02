import io
import os
from google.cloud import vision

client = vision.ImageAnnotatorClient()

def text_detection():
    file_name = os.path.abspath('resources/IMG_2665.jpg')  # 画像ファイルのパス

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    return response.full_text_annotation.text
