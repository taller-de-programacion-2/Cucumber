import requests
import os


class FiubaService:

    URL = os.environ.get("API_FIUBA_URL", "http://www.fi.uba.ar/api/")
    STUDENT_ENDPOINT = "students/"

    def validateStudentId(self, student_id):
        url_endpoint = self.getStudentEnpointURL(student_id)
        response = requests.get(url_endpoint)

        return response.status_code == 200

    def getStudentEnpointURL(self, student_id):
        return self.URL + self.STUDENT_ENDPOINT + student_id