const { After, AfterAll, BeforeAll, AfterStep} = require('@cucumber/cucumber');
const app = require('../../src/server');
const supertest = require('supertest');
var {setDefaultTimeout} = require('@cucumber/cucumber');

setDefaultTimeout(60 * 1000);


//Rollback hooks, tambien se pueden setear variables de entorno y obtener informacion sobre el escenario
BeforeAll(async function(){
  await supertest(app).post('/reset').set('Accept', 'application/json');
})

AfterAll(async function(){
  await supertest(app).post('/reset').set('Accept', 'application/json');
});

After(async (scenario) => {
  await supertest(app).post('/reset').set('Accept', 'application/json');
});
