import os
from uuid import uuid4

from main.services.acr_cloud_client import ACRCloudClient
from main.services.acr_results_parser import ACRResultsParser
from main.services.parsed_results_formatter import ParsedResultsFormatter
from main.services.segment_generator import SegmentGenerator
from main.services.youtube_audio_downloader import YouTubeAudioDownloader
import json


class Setgrabber:
    """
    class for all the stages in setgrab i.e.
    downloading audio, segment-building, sending requests to ACR API, parsing and formatting
    """

    def __init__(self, config, acr_cloud_config, sub_folder_name=uuid4().hex):
        """
        :param config: full config file in main/resources/config.ini
        :param acr_cloud_config: configuration for the ACR Cloud API i.e. credentials
        """
        self.config = config
        self.downloader = YouTubeAudioDownloader(config=config, sub_folder=sub_folder_name)
        self.segment_generator = SegmentGenerator(config=config, hash_folder_name=sub_folder_name)
        self.acr_cloud_client = ACRCloudClient(config, acr_cloud_config)
        self.acr_results_parser = ACRResultsParser(config)
        self.parsed_results_formatter = ParsedResultsFormatter(config)

        # directory and file paths
        self.download_folder_path = self.config["youtube-audio-downloader"]["download_folder"]
        self.sub_folder_name = sub_folder_name
        self.sub_folder_path = "{}/{}".format(self.download_folder_path, sub_folder_name)
        self.formatted_file_path = "{}/{}".format(self.sub_folder_path, "setgrab_results.json")

    def recognize_setlist(self, url):
        """
        run content recognition on the audio of the video at URL provided
        :param url: URL to set on YouTube
        :return: a timestamped setlist of the songs recognised from the audio with timestamp keys and artist, song values
        """
        if not os.path.exists(self.download_folder_path):
            os.mkdir(self.download_folder_path)
        os.mkdir(self.sub_folder_path)
        print("Processing request {}".format(self.sub_folder_name))
        print("(1/5) Downloading..")
        self.downloader.download_mp3(url)
        print("(2/5) Segmenting..")
        segments_dict = self.segment_generator.segment()
        print("Produced {} segments".format(len(segments_dict.keys())))
        print("(3/5) Recognising..")
        acr_results_dict = {k: self.acr_cloud_client.recognize_song_as_object(v) for (k, v) in segments_dict.items()}
        print("(4/5) Parsing..")
        parsed_dict = self.acr_results_parser.parse(acr_results_dict)
        print("(5/5) Formatting..")
        formatted_result = self.parsed_results_formatter.format(parsed_dict)
        with open(self.formatted_file_path, 'w', encoding='utf-8') as f:
            json.dump(formatted_result, f, ensure_ascii=False, indent=4)
        print(formatted_result)
        return 0

    def recognize_setlist_as_text(self, url):
        """
        run content recognition on the audio of the video at URL provided
        :param url: URL to set on YouTube
        :return: a timestamped setlist of the songs recognised from the audio (text)
        """
        print("(1/5) Downloading..")
        self.downloader.download_mp3(url)
        print("(2/5) Segmenting..")
        segments_dict = self.segment_generator.segment()
        print("(3/5) Recognising..")
        acr_results_dict = {k: self.acr_cloud_client.recognize_song_as_object(v) for (k, v) in segments_dict.items()}
        print("(4/5) Parsing..")
        parsed_dict = self.acr_results_parser.parse(acr_results_dict)
        print("(5/5) Formatting..")
        print("---------------------------------------------")
        print(self.parsed_results_formatter.format_as_text(parsed_dict))
        print("---------------------------------------------")
        return 0
