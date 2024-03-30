import joblib

from io import BytesIO

import numpy as np
import tensorflow as tf
import requests

from fastapi import FastAPI
from PIL import Image
from pydantic import BaseModel

model = joblib.load(r'models\iris_model.joblib')

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


app = FastAPI()

@app.get("/")
def read_root():
    return {"result": "Hello World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/predict")
def predict_iris_species(features: IrisFeatures):
    # Extract features into a list in the correct order
    feature_array = [[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]]
    
    # Predict the class
    prediction = model.predict(feature_array)
    
    # Translate prediction into species name
    species = ["setosa", "versicolor", "virginica"]
    predicted_species = species[prediction[0]]
    
    return {"predicted_species": predicted_species}

@app.get("/classify")
def classify_image(url: str):
    # Download the image from the URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Resize image to match model input shape
    img = img.resize((224, 224))  # Adjust size according to your model's input size

    # Convert image to numpy array and normalize pixel values
    img_array = np.array(img) / 255.0

    # Expand dimensions to match model input shape
    img_array = np.expand_dims(img_array, axis=0)

    # Predict class probabilities
    # predictions = model.predict(img_array)

    # Get the predicted class index (0 for cat, 1 for dog, assuming 2 classes)
    predicted_class = np.random.randint(0,2)

    # Return the result
    if predicted_class == 0:
        return {"prediction": "cat"}
    else:
        return {"prediction": "dog"}
