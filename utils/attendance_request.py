from dataclasses import dataclass
import requests
from utils.periods import Periods
from utils.periods import Locations

@dataclass
class AttendanceJson:
    """Create and return the JSON structure to post."""

    period: Periods
    at_home: Locations

    def get_json(self):

        return {
            "operationName": "record_attendance_time",
            "variables": {
                "period": self.period.name,
                "atHome": self.at_home.value[1]
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "553ae433516c13a97e348d4a48dd0114d1949f791ab21d97bed27030a65e85a8"
                }
            }
        }

URL = "https://graph.becode.org/"

class AttendanceRequest():

    def __init__(self, period: Periods, at_home: Locations, token: str):

        self.data = AttendanceJson(period=period, at_home=at_home).get_json()
        self.header = {"Authorization": f"Bearer {token}"}

        self.response = None

    def __send(self):
        self.response = requests.post(url=URL, json=self.data, headers=self.header)

    def run(self):
        self.__send()

    def get_status(self):
        """Return the request status."""

        if self.response.status_code == 200:
            status = self.response.json()

            try:
                if status['data']['recordAttendanceTime']:
                    return True

            except KeyError:
                return False

        return False