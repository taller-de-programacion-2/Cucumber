from typing import List, Any

from flask import Flask, jsonify
from app.Controllers.inscription import InscriptionController

app = Flask(__name__)
inscriptions_repository = []

@app.route("/inscriptions", methods=["GET"])
def getInscriptions():
    return InscriptionController().get(inscriptions_repository)

@app.route("/inscriptions", methods=["POST"])
def postInscriptions():
    return InscriptionController().post(inscriptions_repository)

@app.route("/ping")
def ping():
    return jsonify({"message":"ok"}), 200

@app.route("/reset", methods=["POST"])
def reset():
    #Rollback de la app
    inscriptions_repository.clear()
    return jsonify({"message":"ok"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)