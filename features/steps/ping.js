const {  When, Then } = require('@cucumber/cucumber');
const assert = require('assert');
const app = require('../../src/server');
const supertest = require('supertest');

Then('i have a ok message', async function () {
    assert.equal(response.status,200);
    assert.equal(response.body["message"],"OK");
});
When(/^i enter \/ping$/, async function () {
    response = await supertest(app).get('/ping');
});
