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

@app.post("/quantum")
async def save(request: Request):
    data = await request.json()
    data_update = InputQuantum()
    matrix,probability,draw = data_update.update_quantum(data['keyList'])

    return {
        'matrix': str(list(matrix)).replace(' ', ''),
        'probability': str(probability),
        'draw': str(list(draw)).replace(' ', '')
    }