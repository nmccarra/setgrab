from configparser import ConfigParser
from flask import Flask
from flask import request
from flask_restplus import Resource, Api, fields
import os
import threading

from main.services.cache_manager import CacheManager
from main.services.setgrabber import Setgrabber

config = ConfigParser()
config.read(os.getcwd() + "/resources/main/config.ini")

default_config = config["default"]

cache_manager = CacheManager()

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = False
api = Api(app, version=default_config["version"], title="setgrab",
          default='All', default_label="Use these resources to start a recognition job and retrieve results")

# request models

create_setlist_recognition_job_request = api.model("create_setlist_recognition_job_request", {
    "url": fields.String(required=True, description='YouTube URL'),
    "start_time": fields.String(required=True, description="where to start recognition in setlist in format mm:ss")
})

# response models
create_setlist_recognition_job_response = api.model("create_setlist_recognition_job_response", {
    "job_id": fields.String(description="Setgrab job id for retrieving recognition results")
})

get_setlist_recognition_job_response_item = api.model("get_setlist_recognition_job_response_item", {
    "time": fields.String(description="Time when track was recognised in set"),
    "artist" : fields.String(description="Artists of track recognised"),
    "track": fields.String(description="Name of track recognised")
})

get_setlist_recognition_job_response = api.model("get_setlist_recognition_job_response", {
    "request_params": fields.Nested(model=create_setlist_recognition_job_request),
    "status": fields.String(description="Job status"),
    "items": fields.List(cls_or_instance=fields.Nested(get_setlist_recognition_job_response_item))
})


# exception handlers
@api.errorhandler(KeyError)
def handle_key_error(error):
    return {'message': "failed to provide required keys in request"}, 400


@api.route("/home")
class Home(Resource):
    def get(self):
        return {"title": "welcome to setgrab!"}


@api.route("/setgrab/<job_id>", doc={'params': {'job_id': 'recognition job id'}})
@api.response(200, 'Success', get_setlist_recognition_job_response)
@api.doc(description="retrieve recognition job results by id")
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
@api.doc(body=create_setlist_recognition_job_request, description="create a recognition job")
@api.response(200, 'Success', create_setlist_recognition_job_response)
class CreateSetlistRecognitionJob(Resource):
    """
    Create recognition job
    """

    @api.expect(create_setlist_recognition_job_request, validate=True)
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

        return {"job_id": setgrabber.sub_folder_name}


if __name__ == '__main__':
    app.run(debug=True, port=default_config["port"], host='0.0.0.0')
