import unittest
from main.models.seconds import Seconds
from main.models.hour_minutes_seconds_mark import HourMinutesSecondsMark


class TestSeconds(unittest.TestCase):

    def test_should_convert_to_hour_minutes_seconds_mark(self):
        test_case_100 = Seconds(100)
        test_case_1000 = Seconds(10000)

        self.assertEqual(HourMinutesSecondsMark(0, 1, 40), test_case_100.as_hours_minutes_seconds_mark())
        self.assertEqual(HourMinutesSecondsMark(2, 46, 40), test_case_1000.as_hours_minutes_seconds_mark())
