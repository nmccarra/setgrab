class HourMinutesSecondsMark:
    """
    class to manage time marks
    """
    def __init__(self, hour, minutes, seconds):
        """
        :param hour: hour mark from start in video audio
        :param minutes: minutes mark from start in video audio
        :param seconds: seconds mark from start in video audio
        """
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return "HourMinutesSecondsMark({hour_str}, {minutes_str}, {seconds_str})" \
            .format(hour_str=self.hour, minutes_str=self.minutes, seconds_str=self.seconds)

    def __hash__(self):
        return hash((self.hour, self.minutes, self.seconds))

    def __eq__(self, other):
        return (self.hour, self.minutes, self.seconds) == (other.hour, other.minutes, other.seconds)
