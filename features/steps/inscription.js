const {Given, When, Then, And} = require("cucumber");
const assert = require('assert');
const app = require('../../server');
const supertest = require('supertest');
const fetchMock = require('fetch-mock');
const FiubaService = require('../../Services/fiuba');


Given('que me quiero anotar a la materia Algoritmos y Programacion I', function () {});

When('me inscribo indicando mi id de estudiante {string} y el codigo de la materia {string}', async function (student_id, subject_code) {
  fetchMock.mock(FiubaService.getStudentEndpointURL(student_id), 200); // ejemplo de mock
  
  let body = {
    "student_id": student_id,
    "subject_code": subject_code
  }
  this.response = await supertest(app).post('/inscriptions').set('Accept', 'application/json').send(body); // ejemplo de como pegarle a la API

});

Then('me indica que mi inscripcion fue exitosa', function () {
  assert.equal(this.response.status, 201);
});

Given('que no hay alumnos inscriptos en ninguna materia', function () {});

When('pido las inscripciones', async function () {
  this.response = await supertest(app).get('/inscriptions').set('Accept', 'application/json');
});

Then('no me devuelve ninguna inscripcion', function () {
  assert.equal(this.response.status, 200);
  assert.equal(this.response.body.inscriptions.length, 0);
});

Given('hay {int} alumnos inscriptos en ninguna materia', async function (inscriptions_amount) {
  for (let index = 0; index < inscriptions_amount; index++) {
    let student_id = index.toString();
    let body = {
      "student_id": student_id,
      "subject_code": "ALGO1"
    }
    fetchMock.mock(FiubaService.getStudentEndpointURL(student_id), 200);
    let response = await supertest(app).post('/inscriptions').set('Accept', 'application/json').send(body);
    assert.equal(response.status, 201)
  }
});
  
Then('me devuelve {int} inscripciones', function (inscriptions_amount) {
  assert.equal(this.response.status, 200);
  assert.equal(this.response.body.inscriptions.length, inscriptions_amount);
  });