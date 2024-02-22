from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from model_utils import load_model, prediction


app = FastAPI()

class LanguageInput(BaseModel):
    language: str

class FeaturesInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionOutput(BaseModel):
    category: int

model = load_model()

@app.post("/predict")
def prediction_root(feature_input: FeaturesInput):
    # feats has to be a 2D-NumPy array
    feats = [list(feature_input.model_dump().values())]
    preds = prediction(model, feats)[0]
    return PredictionOutput(category=preds)

@app.post("/predict2")
def prediction_root2(feature_input: FeaturesInput):
    print(type(feature_input))
    print(feature_input)
    return 1976
          
@app.post("/language")
def language_root(language_input: LanguageInput):
    if language_input.language.lower() == "french":
        return {"message": "Bonjour"}
    elif language_input.language.lower() == "english":
        return {"message": "Hello"}
    else:
        return {"message": "La langue n'est pas prise en charge"}

@app.post("/language2")
def language2_root(language_input: str):
    if language_input.lower() == "french":
        return {"message": "Bonjour"}
    elif language_input.lower() == "english":
        return {"message": "Hello"}
    else:
        return {"message": "La langue n'est pas prise en charge"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
