from __future__ import unicode_literals
from yt_dlp import YoutubeDL, DownloadError


class YouTubeAudioDownloaderLogger:
    """
    logger for the downloader, providing progress logging
    """
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    @staticmethod
    def error(msg):
        print(msg)


def progress_hooks(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


class YouTubeAudioDownloader(YoutubeDL):
    """
    class which inherits YoutubeDL - this takes a URL for a corresponding YouTube video
    and produces an .mp3 file
    """
    def __init__(self, config, sub_folder):
        """
        :param config: full config file in main/resources/config.ini
        :param sub_folder: this is the sub-folder where the .mp3 will be saved
        """
        self.config = config
        self.youtube_audio_downloader_config = config["youtube-audio-downloader"]
        self.download_path = self.youtube_audio_downloader_config["download_folder"] + "/" + sub_folder + "/" + self.youtube_audio_downloader_config['download_name']

        ydl_opts = {
            'format': self.youtube_audio_downloader_config["format"],
            'outtmpl': self.download_path,
            'postprocessors': [{
                'key': self.youtube_audio_downloader_config["postprocessors_key"],
                'preferredcodec': self.youtube_audio_downloader_config["postprocessors_preferredcodec"],
                'preferredquality': self.youtube_audio_downloader_config["postprocessors_preferredquality"]
            }],
            'logger': YouTubeAudioDownloaderLogger(),
            'progress_hooks': [progress_hooks]
        }
        super().__init__(ydl_opts)

    def download_mp3(self, url):
        """
        :param url: URL to a YouTube video
        :return: msg with the result of the download
        """
        try:
            self.download([url])
            message_status_response = {"msg": "Download complete to " + self.download_path}, 200
        except DownloadError as e:
            message_status_response = {"msg": str(e)}, 400
        return message_status_response
