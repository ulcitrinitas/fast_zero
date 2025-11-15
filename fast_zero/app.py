from http import HTTPStatus
from fastapi import FastAPI

from fast_zero.schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Rodando no fastapi"}


@app.post("/users/", status_code=HTTPStatus.CREATED)
def create_user():
    ...
