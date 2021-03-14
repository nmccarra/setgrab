from main.services.acr_cloud_client import ACRCloudClient
from main.services.acr_results_parser import ACRResultsParser


class SetgrabRunner:
    """
    a runner class for all the stages in setgrab i.e.
    downloading audio, segment-building, sending requests to ACR API, parsing and formatting
    """

    def __init__(self, config, acr_cloud_config):
        """
        :param config: full config file in main/resources/config.ini
        :param acr_cloud_config: configuration for the ACR Cloud API i.e. credentials
        """
        self.config = config
        # TODO : Create setlist_downloader class and add here as a property
        # TODO : Create setlist_segment_builder class and add here as a property
        self.acr_cloud_client = ACRCloudClient(config, acr_cloud_config)
        self.acr_results_parser = ACRResultsParser(config)
        # TODO : Create setlist_formatter class and add here as a property

    def recognize_setlist(self, url):
        """
        run content recognition on the audio of the video at URL provided
        :param url: URL to set on YouTube
        :return: a timestamped setlist of the songs recognised from the audio with timestamp keys and artist, song values
        """
        # TODO : Implement member once all stage classes are created
        return None

    def recognize_setlist_as_text(self, url):
        """
        run content recognition on the audio of the video at URL provided
        :param url: URL to set on YouTube
        :return: a timestamped setlist of the songs recognised from the audio (text)
        """
        # TODO : Implement member once all stage classes are created
        return None
