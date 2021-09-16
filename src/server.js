'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const inscription_routes = require('./Routes/inscription');


// App
const app = express();
app.get('/ping', (req, res) => {
  res.status(200).json({"message":"OK"});
});

app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

//configuration headers http
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Authorization, X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Request-Method');
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
    res.header('Allow', 'GET, POST, OPTIONS, PUT, DELETE');
    next();
});


app.use('', inscription_routes);






module.exports = app;
