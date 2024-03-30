import logging
from io import BytesIO

import torch
import requests

from fastapi import FastAPI
from PIL import Image
from transformers import AutoImageProcessor, ResNetForImageClassification

# Set Logging Level
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

# Initialize model and image processor
processor = AutoImageProcessor.from_pretrained("microsoft/resnet-18")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-18")

app = FastAPI()

@app.get("/")
def read_root():
    return {"result": "Hello World!"}

@app.get("/classify_image")
def classify_image(url: str):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)) 
    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    result = model.config.id2label[predicted_label].split(',')
    logging.info(result)    
    return {"result":result}
