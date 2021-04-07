from behave import *
import json
import requests_mock
from services.fiuba import FiubaService


@given("que me quiero anotar a la materia Algoritmos y Programacion I")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


# Ejemplo de mock de api call
@when('me inscribo indicando mi id de estudiante "{}" y el codigo de la materia "{}"')
def step_impl(context, student_id, subject_code):
    """
    :param subject_code: String
    :param student_id: String
    :type context: behave.runner.Context
    """
    body = {
        "student_id": student_id,
        "subject_code": subject_code
    }

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "/inscriptions"

    with requests_mock.Mocker() as m:
        service = FiubaService()

        mock_url = service.getStudentEnpointURL(student_id)
        mock_body = {'message': 'valid student'}
        m.get(mock_url, json=mock_body, headers=headers, status_code=200)

        context.response = context.client.post(url, headers=headers, data=json.dumps(body))


@then("me indica que mi inscripcion fue exitosa")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@given("que no hay alumnos inscriptos en ninguna materia")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("pido las inscripciones")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = context.client.get("/inscriptions")


@then("no me devuelve ninguna inscripcion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
    assert len(context.response.json['inscriptions']) == 0


@given('hay {:d} alumnos inscriptos en ninguna materia')
def step_impl(context, inscriptions_amount):
    """
    :param inscriptions_amount: String
    :type context: behave.runner.Context
    """
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    url = "/inscriptions"

    amount_to_create = inscriptions_amount
    for i in range(amount_to_create):
        body = {
            "student_id": str(i),
            "subject_code": "ALGO1"
        }

        with requests_mock.Mocker() as m:
            service = FiubaService()

            mock_url = service.getStudentEnpointURL(str(i))
            mock_body = {'message': 'valid student'}
            m.get(mock_url, json=mock_body, headers=headers, status_code=200)

            response = context.client.post(url, headers=headers, data=json.dumps(body))
            assert response.status_code == 201

@then('me devuelve {:d} inscripciones')
def step_impl(context, inscriptions_amount):
    """
    :param inscriptions_amount: Integer
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
    assert len(context.response.json['inscriptions']) == inscriptions_amount
