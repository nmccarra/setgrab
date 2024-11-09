import unittest
from main.services.acr_results_parser import ACRResultsParser
from configparser import ConfigParser
import os
import json
from types import SimpleNamespace
from main.models.hour_minutes_seconds_mark import HourMinutesSecondsMark
from main.models.artist_song_entry import ArtistSongTitleEntry


class TestACRResultsParser(unittest.TestCase):
    def setUp(self):
        if os.getcwd().endswith("test"):
            self.dir = os.getcwd().removesuffix("test")
        else:
            self.dir = os.getcwd()

        self.config = ConfigParser()
        self.config.read("{}/resources/test/config.ini".format(self.dir))
        self.parser = ACRResultsParser(self.config)

    def create_dummy_acr_client_output(self):
        files = ['beul_un_latha.json', 'beul_un_latha.json', 'may_be_mute.json', 'walk_on_wire.json']
        dummy_acr_client_output = {}
        for index_file_pair in enumerate(files):
            with open(self.dir + "/resources/test/" + index_file_pair[1], "r") as json_file:
                key = HourMinutesSecondsMark(index_file_pair[0]*60*60)
                dummy_acr_client_output[key] = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))
        return dummy_acr_client_output

    def test_should_return_list_of_artist_song_entry(self):
        with open(self.dir + "/resources/test/beul_un_latha.json", "r") as json_file:
            data = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))

        result = self.parser.parse_to_artist_song_entry(data)
        self.assertEqual("Above & Beyond Group Therapy, Anjunabeats", result[0].artist_name)
        self.assertEqual("Beul Un Latha (ABGT401)", result[0].song_title)

        self.assertEqual("Trance Wax", result[1].artist_name)
        self.assertEqual("Beul Un Latha", result[1].song_title)

        self.assertEqual("Trance Wax", result[2].artist_name)
        self.assertEqual("Beul Un Latha", result[2].song_title)

    def test_should_be_none_for_may_be_mute_status(self):
        with open(self.dir + "/resources/test/may_be_mute.json", "r") as json_file:
            data = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))

        result = self.parser.parse_to_artist_song_entry(data)
        self.assertEqual(None, result)

    def test_should_prune_results_correctly(self):
        with open(self.dir + "/resources/test/prune_test_case.json", "r") as json_file:
            test_case_dict = json.load(json_file)

        pruned_results = self.parser.prune_results(test_case_dict, list(test_case_dict.keys()))

        self.assertListEqual(['seg_1', 'seg_3', 'seg_4', 'seg_5'], list(pruned_results.keys()))

    def test_should_parse_results_correctly(self):
        dummy_acr_client_output = self.create_dummy_acr_client_output()
        parsed_dict = self.parser.parse(dummy_acr_client_output)
        self.assertEqual(ArtistSongTitleEntry("Trance Wax", "Beul Un Latha"), parsed_dict[HourMinutesSecondsMark(0)])
        self.assertEqual(ArtistSongTitleEntry("Pablo Bozzi", "Last Vision"), parsed_dict[HourMinutesSecondsMark(10800)])
        self.assertEqual(2, len(parsed_dict))


if __name__ == '__main__':
    unittest.main()
