'use strict'

var express = require('express');
const InscriptionController = require('../Controllers/inscription');

var api = express.Router();


api.post('/inscriptions', (req, res) => { new InscriptionController().createInscription(req, res)});
api.get('/inscriptions', (req, res) => { new InscriptionController().getInscriptions(req, res)});
api.post('/reset', (req, res) => { new InscriptionController().reset(req, res)});

module.exports = api;