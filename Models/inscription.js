'use strict'

class Inscription {
    static SUBJECT_LIST = {
        "AM1":"Analisis Matematico I",
        "AM2": "Analisis Matematico II",
        "F1": "Fisica I",
        "ALGO1": "Algoritmos y programacion I"
    }

    constructor(student_id, subject_code){
        this.student_id = student_id;
        this.subject_code = subject_code;
    }

    static exists(subject_code){
        return subject_code in this.SUBJECT_LIST; 
    }
}

module.exports = Inscription;