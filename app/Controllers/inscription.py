from app.Models.inscription import Inscription
from flask import request, jsonify
from services.fiuba import FiubaService
from app.Models.subject import Subject


class InscriptionController():

    def post(self, reposity):

        body = request.get_json()
        student_id = body['student_id']
        subject_code = body['subject_code']

        fiuba_service = FiubaService()

        if fiuba_service.validateStudentId(student_id) and Subject.exists(subject_code):
            inscription = Inscription(student_id, subject_code)

            reposity.append(inscription)

            return jsonify({'message': 'inscription created'}), 201

        return jsonify({'message': 'inscription error'}), 400


    def get(self, repository):
        inscriptions = [inscription.toJson() for inscription in repository]
        return jsonify({'inscriptions': inscriptions}), 200