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


data_update = InputQuantum()

@app.post("/quantum")
async def save(request: Request):
    data = await request.json()
    data = data_update.update_quantum(data)
    return str(list(data)).replace(' ', '')