class CacheManager:
    """
    class for managing cache holding setlist recognition jobs
    """

    def __init__(self):
        self.cache = {}

    def add(self, request_params, job_id):
        self.cache[job_id] = {
            "request_params": {
                "url": request_params["url"],
                "start_time": request_params["start_time"],
            },
            "status": "in-progress"
        }

    def get_by_job_id(self, job_id):
        return self.cache[job_id]

    def get_by_request_params(self, request_params):
        for key, value in self.cache.items():
            if (value["request_params"]["url"] == request_params["url"]) and (
                    value["request_params"]["start_time"] == request_params["start_time"]):
                return value
            else:
                return None

    def update(self, job_id, update_dict, status):
        self.cache[job_id] = {**self.cache[job_id], **update_dict}
        self.cache[job_id]["status"] = status
        return self.cache[job_id]
