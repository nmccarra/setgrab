import unittest
from configparser import ConfigParser
from main.services.parsed_results_formatter import ParsedResultsFormatter
from main.models.artist_song_entry import ArtistSongTitleEntry
from main.models.hour_minutes_seconds_mark import HourMinutesSecondsMark


class TestParsedResultsFormatter(unittest.TestCase):
    def setUp(self):
        self.config = ConfigParser()
        self.config.read("./test/resources/config.ini")
        self.formatter = ParsedResultsFormatter(self.config)

        self.parsed_results_dict_test_case_1 = {
            HourMinutesSecondsMark(60): ArtistSongTitleEntry("Bicep", "Just"),
            HourMinutesSecondsMark(210): ArtistSongTitleEntry("Ansome", "Smuggler's Den"),
            HourMinutesSecondsMark(300): ArtistSongTitleEntry("Blawan", "993"),
            HourMinutesSecondsMark(4890): ArtistSongTitleEntry("Karenn", "Salz"),
            HourMinutesSecondsMark(10980): ArtistSongTitleEntry("Djedjotronic, Miss Kittin", "Pleasure & Pain")
        }

    def test_should_return_formatted_dict(self):
        formatted_result = self.formatter.format(self.parsed_results_dict_test_case_1)
        self.assertEqual("Bicep - Just", formatted_result["1:00"])
        self.assertEqual("Ansome - Smuggler's Den", formatted_result["3:30"])
        self.assertEqual("Blawan - 993", formatted_result["5:00"])
        self.assertEqual("Karenn - Salz", formatted_result["1:21:30"])
        self.assertEqual("Djedjotronic, Miss Kittin - Pleasure & Pain", formatted_result["3:03:00"])

    def test_should_return_formatted_text(self):
        formatted_result = self.formatter.format_as_text(self.parsed_results_dict_test_case_1).replace(" ", "").replace(
            "\n", "")
        self.assertEqual("""
        1:00 ~ Bicep - Just
        3:30 ~ Ansome - Smuggler's Den
        5:00 ~ Blawan - 993
        1:21:30 ~ Karenn - Salz
        3:03:00 ~ Djedjotronic, Miss Kittin - Pleasure & Pain
        """.replace(" ", "").replace("\n", ""), formatted_result)
