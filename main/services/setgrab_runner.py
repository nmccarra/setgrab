from main.services.acr_cloud_client import ACRCloudClient
from main.services.acr_results_parser import ACRResultsParser
from main.services.parsed_results_formatter import ParsedResultsFormatter
from main.services.youtube_audio_downloader import YouTubeAudioDownloader


class SetgrabRunner:
    """
    a runner class for all the stages in setgrab i.e.
    downloading audio, segment-building, sending requests to ACR API, parsing and formatting
    """

    def __init__(self, config, acr_cloud_config, sub_folder):
        """
        :param config: full config file in main/resources/config.ini
        :param acr_cloud_config: configuration for the ACR Cloud API i.e. credentials
        """
        self.config = config
        self.downloader = YouTubeAudioDownloader(config=config, sub_folder=sub_folder)
        # TODO : Create setlist_segment_builder class and add here as a property
        self.acr_cloud_client = ACRCloudClient(config, acr_cloud_config)
        self.acr_results_parser = ACRResultsParser(config)
        self.parsed_results_formatter = ParsedResultsFormatter(config)

    @staticmethod
    def recognize_setlist(url):
        """
        run content recognition on the audio of the video at URL provided
        :param url: URL to set on YouTube
        :return: a timestamped setlist of the songs recognised from the audio with timestamp keys and artist, song values
        """
        # TODO : Implement member once all stage classes are created
        return None

    @staticmethod
    def recognize_setlist_as_text(url):
        """
        run content recognition on the audio of the video at URL provided
        :param url: URL to set on YouTube
        :return: a timestamped setlist of the songs recognised from the audio (text)
        """
        # TODO : Implement member once all stage classes are created
        return None
