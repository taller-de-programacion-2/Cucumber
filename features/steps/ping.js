const {  When, Then } = require('cucumber');
const assert = require('assert');
const app = require('../../server');
const supertest = require('supertest');

When('i enter /ping', async function () {
    response = await supertest(app).get('/ping');
});

Then('i have a ok message', async function () {
    assert.equal(response.status,200);
    assert.equal(response.body["message"],"OK");
});
