from http import HTTPStatus
from fastapi import FastAPI

from fast_zero.schemas import Message
from fast_zero.schemas import UserSchema, UserPublic, UserDB

app = FastAPI()

database = list()

@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Rodando no fastapi"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    
    user_with_id = UserDB(**user.model_dump(), id=(len(database) + 1))
    
    database.append(user_with_id)
    
    print(database)
    
    return user_with_id
