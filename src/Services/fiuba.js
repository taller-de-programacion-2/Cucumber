"use strict"
const config = require('../Configuration/config');
const fetch = require("node-fetch");


class FiubaService{

    static async validateStudentId(student_id){
        let url_endpoint = this.getStudentEndpointURL(student_id);
        let response = await fetch(url_endpoint);
        return response.ok;
    }

    static getStudentEndpointURL(student_id){
        return config.FIUBA_URL + "students/" + student_id
    }
}

module.exports = FiubaService;
