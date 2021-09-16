from app.Models.inscription import Inscription
from fastapi import HTTPException
from services.fiuba import FiubaService
from app.Models.subject import Subject


class InscriptionController():

    def post(self, reposity, body):

        student_id = body.student_id
        subject_code = body.subject_code

        fiuba_service = FiubaService()

        if fiuba_service.validateStudentId(student_id) and Subject.exists(subject_code):
            inscription = Inscription(student_id, subject_code)

            reposity.append(inscription)

            return {'message': 'inscription created'}

        raise HTTPException(status_code=400, detail='inscription error')


    def get(self, repository):
        inscriptions = [inscription.toJson() for inscription in repository]
        return {'inscriptions': inscriptions}