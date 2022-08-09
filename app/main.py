from typing import Union
import os

import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static");


class Order(BaseModel):
    name: str
    phone: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/ls")
def read_item():
    return os.listdir()


@app.post("/server.php")
async def ordir(order:Order):
    return {"name": order.name, "phone": order.phone}


@app.post("/server.php")
async def serv(name: str = Form(None), phone: str = Form(None)):
    return {"name": name, "phone": phone}


@app.post('/server.php')
def some_post():
    print(1)
    return('')


@app.get("/favicon.ico")
async def read_file():
    return FileResponse('files/icons/favicon.ico')


@app.get("/{file_path:path}")
async def read_file(file_path: str):
    return FileResponse('files/' + file_path)


if __name__ == "__main__":
    uvicorn.run("main:app", port=5050)
