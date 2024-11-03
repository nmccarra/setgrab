from acrcloud.recognizer import ACRCloudRecognizer
from os import listdir
from os.path import isfile, join
import json
from types import SimpleNamespace


class ACRCloudClient(ACRCloudRecognizer):
    """
    A class which extends the ACRCloudRecognizer by allowing for multiple file
    recognition
    """
    def __init__(self, config):
        """
        :param config: full config file in main/resources/config.ini
        """
        self.config = config
        self.acr_cloud_request_config = self.config["acr-cloud-request"]
        self.start_seconds = int(self.acr_cloud_request_config["start_seconds"])
        self.rec_length = int(self.acr_cloud_request_config["rec_length"])
        self.acr_cloud_config = config["acr"]
        super().__init__(config=self.acr_cloud_config)

    def recognize_song(self, file_path):
        """
        recognize a single song by file
        :param file_path: path to audio file
        :return: a dict of the song attributes
        """
        return json.loads(self.recognize_by_file(file_path, self.start_seconds, self.rec_length, None))

    def recognize_song_as_object(self, file_path):
        """
        recognize a single song by file and return dict as an object
        :param file_path: path to audio file
        :return: an object with the song attributes as properties
        """
        return json.loads(self.recognize_by_file(file_path, self.start_seconds, self.rec_length, None),
                          object_hook=lambda d: SimpleNamespace(**d))

    def recognize_multiple(self, folder_path):
        """
        recognize the songs in a given folder
        :param folder_path: folder containing audio files
        :return: dict object of filename to song attributes
        """
        onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        return {f.rsplit('.', 1)[0]: self.recognize_song(folder_path + "/" + f) for f in onlyfiles}
