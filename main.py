from utils.periods import Periods
from utils.periods import Locations
from utils.send_email import send_email
from utils.attendance_request import AttendanceRequest
import datetime
from utils import variables
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
    
    
    token = variables.token
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