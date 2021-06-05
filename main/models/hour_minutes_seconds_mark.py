import datetime


class HourMinutesSecondsMark:
    """
    class to manage time marks
    """

    def __init__(self, seconds):
        """
        :param seconds: seconds mark from start in video audio
        """
        time_elements = [int(i) for i in str(datetime.timedelta(seconds=seconds)).split(":")]
        self.hour = time_elements[0]
        self.minutes = time_elements[1]
        self.seconds = time_elements[2]

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
        :return: string in YouTube time mark format
        """
        if self.hour == 0:
            time_mark_string = str(self.minutes) + ":" + str(self.seconds).zfill(2)
        else:
            time_mark_string = str(self.hour) + ":" + str(self.minutes).zfill(
                2) + ":" + str(self.seconds).zfill(2)
        return time_mark_string
