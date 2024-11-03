from pydub import AudioSegment
from main.models.hour_minutes_seconds_mark import HourMinutesSecondsMark
import os


class SegmentGenerator(AudioSegment):
    """
    A class which should produce a sub-folder 'segments' in the hash folder
    containing the .mp3 files to send to ACR Cloud for recognition
    """

    def __init__(self, config, hash_folder_name):
        youtube_audio_downloader_config = config["youtube-audio-downloader"]
        segment_generator_config = config["segment-generator"]
        acr_cloud_request_config = config["acr-cloud-request"]

        self.config = config
        self.hash_folder_name = hash_folder_name
        self.download_path = youtube_audio_downloader_config["download_folder"] + "/" + hash_folder_name + "/" + youtube_audio_downloader_config["download_name"] + ".mp3"
        self.segments_path = youtube_audio_downloader_config["download_folder"] + "/" + hash_folder_name + "/" + segment_generator_config["segments_folder"]
        self.segment_length = int(acr_cloud_request_config["start_seconds"]) + int(acr_cloud_request_config["rec_length"])

    def segment(self, start_time_seconds, duration_seconds):
        """
        creates approx. equal segments of the .mp3 by length given in the config file
        :return: dict with starting time of segment as key and path to segment file as value
        """
        os.mkdir(self.segments_path)
        download = AudioSegment.from_file(
            file=self.download_path,
            start_second=start_time_seconds,
            duration=duration_seconds
        )
        download_length = int(download.duration_seconds)
        segment_count = download_length//self.segment_length
        output = {}
        for segment_index in range(1, segment_count+1):
            start_time = (segment_index-1)*self.segment_length * 1000
            end_time = max((segment_index*self.segment_length) * 1000, download_length * 1000) if segment_index == segment_count else (segment_index*self.segment_length) * 1000
            segment = download[start_time:end_time]
            segment_i_path = self.segments_path + "/" + "segment" + str(segment_index) + ".mp3"
            out_ = segment.export(segment_i_path, format="mp3")
            out_.close()
            output[HourMinutesSecondsMark(start_time_seconds + segment_index*self.segment_length)] = segment_i_path
        return output
