from typing import Union

from fastapi import FastAPI, Query, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from enum import Enum


app = FastAPI()
templates = Jinja2Templates(directory="templates")

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

test_var = 10

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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






def main():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()

















# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


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