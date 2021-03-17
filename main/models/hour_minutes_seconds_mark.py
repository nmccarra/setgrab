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

    def as_youtube_time_mark(self):
        """
        function to convert HourMinutesSecondsMark to a string of its representation
        in YouTube time mark format
        :param hour_minutes_seconds: instance of HourMinutesSecondsMark
        :return: string in YouTube time mark format
        """
        if self.hour == 0:
            time_mark_string = str(self.minutes) + ":" + str(self.seconds).zfill(2)
        else:
            time_mark_string = str(self.hour) + ":" + str(self.minutes).zfill(
                2) + ":" + str(self.seconds).zfill(2)
        return time_mark_string
