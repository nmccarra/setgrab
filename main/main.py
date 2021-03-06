from configparser import ConfigParser
from flask import Flask
from flask import request
from flask_restplus import Resource, Api, fields
from services.acr_cloud_client import ACRCloudClient
import json

config = ConfigParser()
config.read("./main/resources/config.ini")

app_config = config["app"]
acr_cloud_request_config = config["acr-cloud-request"]

app = Flask(__name__)
api = Api(app, version=app_config["version"], title="SETGRAB",
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


@api.route("/home")
class Home(Resource):
    def get(self):
        return {"title": "WELCOME TO THE SETGRAB API v0.1"}


@api.route("/acr-cloud/recognise/song")
class ACRCloudRecognizeSong(Resource):
    @api.expect(acr_cloud_song, validate=True)
    def post(self):
        start_seconds = int(acr_cloud_request_config["start_seconds"])
        rec_length = int(acr_cloud_request_config["rec_length"])
        request_body = request.get_json()
        acr_cloud_client = ACRCloudClient(config=dict(request_body["acr_cloud_config"]))
        return json.loads(
            acr_cloud_client.recognize_by_file(request_body["file_path"], start_seconds, rec_length, None, 4)
        )


if __name__ == '__main__':
    app.run(debug=True, port=app_config["port"])
