from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class Task(BaseModel):
    title: str = "Add title"
    description: str = None
    is_done: bool = False

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

task_1 = Task()

tasks = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/tasks/{task_id}")
def get_task(task_id: int, task: Task = Task()):
    # return {"task_id": task_id, "title": task_1.title, "description": task_1.description, "is_done": task_1.is_done}
    return {"task_id": task_id, "title": task.title, "description": task.description, "is_done": task.is_done}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item = None):
    return {"test"}
    return {"item_name": item.name, "item_id": item_id}



@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}