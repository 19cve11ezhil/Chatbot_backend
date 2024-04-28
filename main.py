from fastapi import FastAPI
from pydantic import BaseModel
from bot_model import start_model
from fastapi.middleware.cors import CORSMiddleware


class Message(BaseModel):
    message : str
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get('/hello')
def helloworld():

    return{"message":"server started"}


@app.post('/get/response/from_bot')
def get_bot_response(paylod:Message):

    request_mess = paylod.message

    res = start_model(request_mess)

    return res

