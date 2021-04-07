class Subject:

    SUBJECT_LIST = {
            "AM1":"Analisis Matematico I",
            "AM2": "Analisis Matematico II",
            "F1": "Fisica I",
            "ALGO1": "Algoritmos y programacion I"
        }

    @staticmethod
    def list():
        return Subject.SUBJECT_LIST

    @staticmethod
    def exists(subject_code):
        return subject_code in Subject.SUBJECT_LIST