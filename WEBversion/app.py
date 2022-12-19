from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request

from api.utils import InputQuantum

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
import sys

# matrix = []
# probability = []
# draw = []

def restartClass():
    return InputQuantum()

data_update = restartClass()

@app.post("/quantum")
async def save(request: Request):
    data= await request.json()

    if(data['llave']):
        print('servidor reiniciado')
        data_up = restartClass()
        matrix,probability,draw = data_up.update_quantum(data['eventKey'])
    else:
        matrix,probability,draw = data_update.update_quantum(data['eventKey'])
    
    return {
        'matrix': str(list(matrix)).replace(' ', ''),
        'probability': str(list(probability)).replace(' ', ''),
        'draw': str(list(draw)).replace(' ', '')
    }