from fastapi import FastAPI
from app.Controllers.inscription import InscriptionController
from app.Models.Requests.inscription import Inscription
from app.Models.Responses.inscriptions import Inscriptions
from app.Models.Responses.message import Message

app = FastAPI()
inscriptions_repository = []


@app.get("/inscriptions", response_model=Inscriptions)
def getInscriptions():
    return InscriptionController().get(inscriptions_repository)


@app.post("/inscriptions", status_code=201, response_model=Message)
def postInscriptions(body: Inscription):
    return InscriptionController().post(inscriptions_repository, body)


@app.get("/ping", response_model=Message)
def ping():
    return {"message": "ok"}


@app.post("/reset", response_model=Message)
def reset():
    # Rollback de la app
    inscriptions_repository.clear()
    return {"message": "ok"}
