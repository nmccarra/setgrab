import unittest
from main.services.acr_results_parser import ACRResultsParser
from configparser import ConfigParser
import os
import json
from types import SimpleNamespace


class TestACRResultsParser(unittest.TestCase):
    def setUp(self):
        self.config = ConfigParser()
        self.config.read("./test/resources/config.ini")
        self.parser = ACRResultsParser(self.config)

    def test_should_return_list_of_artist_song_entry(self):
        with open(os.getcwd() + "/resources/beul_un_latha.json", "r") as json_file:
            data = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))

        result = self.parser.parse_to_artist_song_entry(data)
        self.assertEqual("Above & Beyond Group Therapy, Anjunabeats", result[0].artist_name)
        self.assertEqual("Beul Un Latha (ABGT401)", result[0].song_title)

        self.assertEqual("Trance Wax", result[1].artist_name)
        self.assertEqual("Buel Un Latha", result[1].song_title)

        self.assertEqual("Trance Wax", result[2].artist_name)
        self.assertEqual("Beul Un Latha", result[2].song_title)

    def test_should_be_none_for_may_be_mute_status(self):
        with open(os.getcwd() + "/resources/may_be_mute.json", "r") as json_file:
            data = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))

        result = self.parser.parse_to_artist_song_entry(data)
        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
