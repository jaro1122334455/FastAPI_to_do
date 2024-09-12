from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class Task(BaseModel):
    title: str
    description: str | None = None
    is_done: bool = False


fake_tasks_db = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    try:
        return {"task_id": task_id, "title": fake_tasks_db[task_id].title, "description": fake_tasks_db[task_id].description, "is_done": fake_tasks_db[task_id].is_done}
    except:
        return {"msg": "task doesn't exist yet"}


@app.post("/tasks/")
async def create_task(task: Task):
    fake_tasks_db.append(task)
    return{"msg": "task added succesfully"}


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    try:
        fake_tasks_db[task_id] = task
        return{"msg": "task updated succesfully"}
    except:
        return{"msg": "fail"}























@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item = None):
#     return {"test"}
#     return {"item_name": item.name, "item_id": item_id}



# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}