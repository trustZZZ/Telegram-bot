"""hour()
   minute()
   day()
   week()
   mounth()"""


def hour(hours: int):
    time_frame = (hours, 'H')
    return time_frame


def minute(minutes: int):
    time_frame = (minutes, 'm')
    return time_frame


def day(days: int):
    time_frame = (days, 'Dutc')
    return time_frame


def week(weeks: int):
    time_frame = (weeks, 'Wutc')
    return time_frame


def month(months: int):
    time_frame = (months, 'Mutc')
    return time_frame
