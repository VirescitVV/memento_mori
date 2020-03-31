import datetime as dt

#retrieves system dtg for record management
def get_dtg():
    date = dt.datetime.now().date().isoformat()
    time = dt.datetime.now(dt.timezone.utc).time().isoformat(timespec='minutes')
    day = dt.datetime.now().date().weekday()

    if day == 0:
        dow = 'Monday'
    elif day == 1:
        dow = 'Tuesday'
    elif day == 2:
        dow = 'Wednesday'
    elif day == 3:
        dow = 'Thursday'
    elif day == 4:
        dow = 'Friday'
    elif day == 5:
        dow = 'Saturday'
    else:
        dow = 'Sunday'

    return date, dow, time
