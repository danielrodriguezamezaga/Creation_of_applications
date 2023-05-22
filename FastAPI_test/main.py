# Exercise FastApi of: Daniel Rodríguez Amézaga
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from sklearn import datasets


from models import Iris

import pandas as pd
import json
import csv


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

MEDIA_ROOT = "iris.csv"


@app.get("/sklearn_target/", response_class=HTMLResponse)
async def read_item(request: Request):
    df = pd.read_csv('iris.csv')
    iris = datasets.load_iris()
    return templates.TemplateResponse("sklearn_target.html", {"request": request, 
                                                    "iris":iris.target})

@app.get("/home/")
async def test_1():
    return "Bienvenido a FastApi, estas en el Home"

@app.get("/iris/")
async def iris():
    df = pd.read_csv(MEDIA_ROOT)
    data = df.to_json(orient="index")
    data = json.loads(data)
    return data

@app.post("/insertData/", status_code=201)
async def insertData(item: Iris):
    with open(MEDIA_ROOT, "a", newline="") as csvfile:
        fieldnames = ['sepal_width','sepal_length',
                      'petal_width','petal_length',
                      'species']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'item_id':item.id,
                         'sepal_width':item.sepal_width,
                          'sepal_length':item.sepal_length,
                          'petal_width':item.petal_width,
                          'petal_length':item.petal_length,
                          'species':item.species})
        return item

@app.put("/updateData{item_id}")
async def updateData(item_id: int, item: Iris):
    df = pd.read_csv(MEDIA_ROOT)
    df.loc[df.index[-1], "sepal_width"] = item.sepal_width
    df.loc[df.index[-1], "sepal_length"] = item.sepal_length
    df.loc[df.index[-1], "petal_width"] = item.petal_width
    df.loc[df.index[-1], "petal_length"] = item.petal_length
    df.loc[df.index[-1], "species"] = item.species
    df.to_csv(MEDIA_ROOT, index=False)
    return {"item_id": item_id, **item.dict()}

@app.delete("/deleteData{item_id}")
async def deleteData(item_id: int):
    df = pd.read_csv(MEDIA_ROOT)
    df.drop(df.index[-1], inplace=True)
    df.to_csv(MEDIA_ROOT, index="False")
    return {"item_id": item_id, "msg": "Eliminado"}