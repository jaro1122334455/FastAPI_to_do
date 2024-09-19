from typing import Union

from fastapi import FastAPI, Query, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from enum import Enum

fake_tasks_db = []

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Montujemy folder 'static', aby serwować pliki statyczne
app.mount("/static", StaticFiles(directory="static"), name="static")

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class Task(BaseModel):
    title: str
    description: str | None = None
    is_done: bool = False




test_var = 10

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": fake_tasks_db})


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    try:
        return {"task_id": task_id, "title": fake_tasks_db[task_id].title, "description": fake_tasks_db[task_id].description, "is_done": fake_tasks_db[task_id].is_done}
    except:
        return {"msg": "task doesn't exist yet"}


@app.post("/tasks/")
async def create_task(task: Task):
    fake_tasks_db.append(task)
    return RedirectResponse(url="/", status_code=303) 


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


