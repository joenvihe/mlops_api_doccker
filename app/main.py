from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler
import joblib 
import yaml
import numpy as np
import pandas as pd

app = FastAPI()

params_path = "params.yaml"

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_path = config["models"]
    model = joblib.load(model_path)
    list_predict = model.predict(data).tolist()
    prediction = list_predict[0]
    return prediction 

class FeatureIn(BaseModel):
    duration: int
    month: int
    date: int
    age: int
    balance: int
    pout: int
    job: int
    camp: int
    contact: int
    house: int


class TargetOut(FeatureIn):
    predict: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

@app.post("/predict", response_model=TargetOut, status_code=200)
def get_prediction(payload: FeatureIn):
    duration = payload.duration
    month = payload.month
    date = payload.date
    age = payload.age
    balance = payload.balance
    pout = payload.pout
    job = payload.job
    camp = payload.camp
    contact = payload.contact
    house = payload.house

    sc = StandardScaler() 
    balance = sc.fit_transform([[balance]])
    balance = balance[0][0]
    print(balance)

    df = {
	"duration(in minutes)":duration,	
    "ordinal_month":month,	
    "day":date,
    "age":age,
    "balance":balance,
    "ordinal_poutcome":pout,	
    "ordinal_job":job,
    "campaign":camp,
    "ordinal_contact":contact,	
    "housing":house
    }
    lst_df = []
    lst_df.append(df)

    inn = pd.DataFrame(lst_df)

    try:
        prediction_list = predict(inn)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Model not found.")

    result = ""
    if prediction_list == 1:
        result = 'deposit'
    else:
        result = 'not deposit'

    response_object = { 
        "duration":duration,
        "month":month,
        "date":date,
        "age":age,
        "balance":balance,
        "pout":pout,
        "job":job,
        "camp":camp,
        "contact":contact,
        "house":house,
        "predict": result
        }
    return response_object