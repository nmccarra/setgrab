import os

from main.services.acr_cloud_client import ACRCloudClient
from main.services.acr_results_parser import ACRResultsParser
from main.services.parsed_results_formatter import ParsedResultsFormatter
from main.services.segment_generator import SegmentGenerator
from main.services.youtube_audio_downloader import YouTubeAudioDownloader


class Setgrabber:
    """
    class for all the stages in setgrab i.e.
    downloading audio, segment-building, sending requests to ACR API, parsing and formatting
    """

    def __init__(self, config, acr_cloud_config, sub_folder):
        """
        :param config: full config file in main/resources/config.ini
        :param acr_cloud_config: configuration for the ACR Cloud API i.e. credentials
        """
        self.config = config
        self.sub_folder = sub_folder
        self.downloader = YouTubeAudioDownloader(config=config, sub_folder=sub_folder)
        self.segment_generator = SegmentGenerator(config=config, hash_folder_name=sub_folder)
        self.acr_cloud_client = ACRCloudClient(config, acr_cloud_config)
        self.acr_results_parser = ACRResultsParser(config)
        self.parsed_results_formatter = ParsedResultsFormatter(config)

    def recognize_setlist(self, url):
        """
        run content recognition on the audio of the video at URL provided
        :param url: URL to set on YouTube
        :return: a timestamped setlist of the songs recognised from the audio with timestamp keys and artist, song values
        """
        download_folder = self.config["youtube-audio-downloader"]["download_folder"]
        if not os.path.exists(download_folder):
            os.mkdir(self.config["youtube-audio-downloader"]["download_folder"])
        os.mkdir(self.config["youtube-audio-downloader"]["download_folder"] + "/" + self.sub_folder)
        print("(1/5) Downloading..")
        self.downloader.download_mp3(url)
        print("(2/5) Segmenting..")
        segments_dict = self.segment_generator.segment()
        print("(3/5) Recognising..")
        acr_results_dict = {k: self.acr_cloud_client.recognize_song_as_object(v) for (k, v) in segments_dict.items()}
        print("(4/5) Parsing..")
        parsed_dict = self.acr_results_parser.parse(acr_results_dict)
        print("(5/5) Formatting..")
        print(self.parsed_results_formatter.format(parsed_dict))
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
