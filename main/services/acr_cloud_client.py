from acrcloud.recognizer import ACRCloudRecognizer


class ACRCloudClient(ACRCloudRecognizer):
    def __init__(self, config):
        super().__init__(config=config)
