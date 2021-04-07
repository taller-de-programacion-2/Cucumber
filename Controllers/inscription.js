'use strict'
const Inscription = require('../Models/inscription');
const FiubaService = require('../Services/fiuba');
var inscription_repository = []

class InscriptionController {
    async createInscription(req, res){

        const student_id = req.body.student_id;
        const subject_code = req.body.subject_code;
        
        const valid_student_id = await FiubaService.validateStudentId(student_id);
        
        if(Inscription.exists(subject_code) && valid_student_id){
            const inscription = new Inscription(student_id, subject_code);
            inscription_repository.push(inscription);

            res.status(201).json({message: 'inscription created'});
        }else{
            res.status(400).json({message: 'inscription error'});
        }
        
    }

    async getInscriptions(req, res){
        res.status(200).json({inscriptions: inscription_repository});
    }
    
    async reset(req, res){
        inscription_repository = []
        res.status(200).json({messsage: "ok"});
    }
}

module.exports = InscriptionController;