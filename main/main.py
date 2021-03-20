from configparser import ConfigParser
from flask import Flask
from flask import request
from flask_restplus import Resource, Api, fields
from services.acr_cloud_client import ACRCloudClient
from services.youtube_audio_downloader import YouTubeAudioDownloader
import os
from uuid import uuid4

config = ConfigParser()
config.read(os.getcwd() + "/main/resources/config.ini")

default_config = config["default"]
acr_cloud_request_config = config["acr-cloud-request"]

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = False
api = Api(app, version=default_config["version"], title="SETGRAB",
          default='All', default_label='Recognise set lists')

# request body models
acr_cloud_config = api.model("acr_cloud_config", {
    "host": fields.String(required=True, description=""),
    "access_key": fields.String(required=True, description=""),
    "access_secret": fields.String(required=True, description=""),
    "timeout": fields.Integer(required=False, description="")
})

acr_cloud_song = api.model("acr_cloud_song", {
    'acr_cloud_config': fields.Nested(acr_cloud_config),
    'file_path': fields.String(required=True, description='')
})

acr_cloud_multiple = api.model("acr_cloud_multiple", {
    "acr_cloud_config": fields.Nested(acr_cloud_config),
    "folder_path": fields.String(required=True, description='')
})

youtube_download_mp3 = api.model("youtube_download_mp3", {
    "url": fields.String(required=True, description='')
})

setgrab_download_recognize = api.model("youtube_download_recognize", {
    "acr_cloud_config": fields.Nested(acr_cloud_config),
    "url": fields.String(required=True, description='')
})


# exception handlers
@api.errorhandler(KeyError)
def handle_key_error(error):
    return {'message': "failed to provide required keys in request"}, 400


@api.route("/home")
class Home(Resource):
    def get(self):
        return {"title": "WELCOME TO THE SETGRAB API v0.1"}


@api.route("/acr-cloud/recognize/song")
class ACRCloudRecognizeSong(Resource):
    @api.expect(acr_cloud_song, validate=True)
    def post(self):
        request_body = request.get_json()
        acr_cloud_client = ACRCloudClient(config=config, acr_cloud_config=dict(request_body["acr_cloud_config"]))
        return acr_cloud_client.recognize_song(request_body["file_path"])


@api.route("/acr-cloud/recognize/multiple")
class ACRCloudRecognizeMultiple(Resource):
    @api.expect(acr_cloud_multiple, validate=True)
    def post(self):
        request_body = request.get_json()
        acr_cloud_client = ACRCloudClient(config=config, acr_cloud_config=dict(request_body["acr_cloud_config"]))
        return acr_cloud_client.recognize_multiple(request_body["folder_path"])


@api.route("/youtube-download/mp3")
class YouTubeDownloadMp3(Resource):
    @api.expect(youtube_download_mp3, validate=True)
    def post(self):
        request_body = request.get_json()
        sub_folder = uuid4().hex
        downloader = YouTubeAudioDownloader(config=config, sub_folder=sub_folder)
        response = downloader.download_mp3(request_body["url"])
        return response


@api.route("/setgrab/download-recognize/song")
class SetgrabDownloadRecognizeSong(Resource):
    @api.expect(setgrab_download_recognize, validate=True)
    def post(self):
        request_body = request.get_json()
        sub_folder = uuid4().hex
        downloader = YouTubeAudioDownloader(config=config, sub_folder=sub_folder)
        response = downloader.download_mp3(request_body["url"])
        print(response)
        acr_cloud_client = ACRCloudClient(config=config, acr_cloud_config=dict(request_body["acr_cloud_config"]))
        return acr_cloud_client.recognize_song(downloader.download_path)


if __name__ == '__main__':
    app.run(debug=True, port=default_config["port"])
