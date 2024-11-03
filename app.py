from configparser import ConfigParser
from flask import Flask
from flask import request
from flask_restplus import Resource, Api, fields
import os
import threading

from main.services.cache_manager import CacheManager
from main.services.setgrabber import Setgrabber

config = ConfigParser()
config.read(os.getcwd() + "/main/resources/config.ini")

default_config = config["default"]

cache_manager = CacheManager()

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = False
api = Api(app, version=default_config["version"], title="setgrab",
          default='All', default_label='Recognise set lists')

# request body models
acr_cloud_config = api.model("acr_cloud_config", {
    "host": fields.String(required=True, description=""),
    "access_key": fields.String(required=True, description=""),
    "access_secret": fields.String(required=True, description=""),
    "timeout": fields.Integer(required=False, description="")
})

create_setlist_recognition_job = api.model("create_setlist_recognition_job", {
    "url": fields.String(required=True, description=''),
    "start_time": fields.String(required=True, description="where to start recognition in setlist in format mm:ss")
})


# exception handlers
@api.errorhandler(KeyError)
def handle_key_error(error):
    return {'message': "failed to provide required keys in request"}, 400


@api.route("/home")
class Home(Resource):
    def get(self):
        return {"title": "welcome to setgrab!"}


@api.route("/setgrab/<job_id>", doc={'params': {'job_id': 'id of create setlist recognition job'}})
class GetSetlistRecognitionJob(Resource):
    """
    Retrieve recognition results by job ID
    """

    def get(self, job_id):
        try:
            return cache_manager.get_by_job_id(job_id)
        except KeyError:
            return {"status": "not-found"}


@api.route("/setgrab")
class CreateSetlistRecognitionJob(Resource):
    """
    Create recognition job
    """

    @api.expect(create_setlist_recognition_job, validate=True)
    def post(self):
        request_body = request.get_json()
        setgrabber = Setgrabber(
            url=request_body["url"],
            config=config,
            start_time=request_body["start_time"],
            cache_manager=cache_manager
        )

        # kick off job
        thread = threading.Thread(target=setgrabber.recognize_setlist)
        thread.start()

        return setgrabber.sub_folder_name


if __name__ == '__main__':
    app.run(debug=True, port=default_config["port"], host='0.0.0.0')
