class Inscription:
    def __init__(self, student_id, subject_code):
        self.student_id = student_id
        self.subject_code = subject_code

    def toJson(self):
        return {
            "student_id": self.student_id,
            "subject_code": self.subject_code
        }