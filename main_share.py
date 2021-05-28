from utils.periods import Periods
from utils.periods import Locations
from utils.send_email_share import send_email
from utils.attendance_request import AttendanceRequest
import datetime

def main_func():
    now = datetime.datetime.now()

    if now.hour < 9:
        attendance = Periods.MORNING
    elif now.hour < 13:
        attendance = Periods.LUNCH
    elif now.hour < 14:
        attendance = Periods.NOON
    else:
        attendance = Periods.EVENING
    

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoib3duZXIiLCJ1aWQiOiI5NmMxYTk1NS1lZWVhLTQzYTctYTQ3ZC05MGM2ZGEwMjVhYzciLCJrZXkiOiI2Yzc4YTE3IiwiaWF0IjoxNjIyMTE5MDcyfQ.L7TymzHR4AY7KIVv0cG_AHw-S5IzLlNJ7H7HA5uYvok"
    location = Locations.HOME
    
    request = AttendanceRequest(attendance, location, token)

    request.run()
    # request.join()

    if request.get_status():
        response = "[!] Attendance was correctly sent."
        send_email(response)
    else:
        response = "[!] Attendance was NOT correctly sent."
        send_email(response)


if __name__ == "__main__":
    main_func()