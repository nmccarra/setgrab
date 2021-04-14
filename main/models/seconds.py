from datetime import timedelta
from main.models.hour_minutes_seconds_mark import HourMinutesSecondsMark


class Seconds:
    """
    A class which represents seconds of time
    used mainly as a helper for the hours_minutes_seconds_mark class
    """

    def __init__(self, seconds):
        self.seconds = seconds

    def as_hours_minutes_seconds_mark(self):
        time_elements = str(timedelta(seconds=self.seconds)).split(":")
        return HourMinutesSecondsMark(int(time_elements[0]), int(time_elements[1]), int(time_elements[2]))
