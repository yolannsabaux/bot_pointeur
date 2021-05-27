from typing import Union
from enum import Enum
from dataclasses import dataclass
import requests

# Sources: https://github.com/becodeorg/graph/blob/develop/src/schema/models/attendances/types/attendance-time-period.js
class Periods(Enum):

    MORNING = "09h00"
    LUNCH = "12h30"
    NOON = "13h30"
    EVENING = "17h00"


class Locations(Enum):

    HOME = ("Home", True)  # at_home = True
    BECODE = ("Becode", False)  # at_home = False

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



token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoib3duZXIiLCJ1aWQiOiI5NmMxYTk1NS1lZWVhLTQzYTctYTQ3ZC05MGM2ZGEwMjVhYzciLCJrZXkiOiI2Yzc4YTE3IiwiaWF0IjoxNjIyMTE5MDcyfQ.L7TymzHR4AY7KIVv0cG_AHw-S5IzLlNJ7H7HA5uYvok"
location = Locations.HOME

# Init and send the request
attendance = Periods.EVENING
request = AttendanceRequest(attendance, location, token)

request.run()
# request.join()

if request.get_status():

    print(f"[!] Attendance was correctly sent.")

else:
    print(f"[!] Attendance was NOT correctly sent.")