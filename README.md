
![setgrab logo](docs/assets/setgrab_banner.png)
# setgrab
![Python](https://img.shields.io/badge/python-3.8-blue)

Give setgrab a URL to a DJ set on YouTube and it will try to recognise the songs played.

### Getting Started

Follow the [Development Environment Setup](docs/developemental_env_setup.md) page so that you can run the application locally.

Create a recognition job using:
```commandline
POST /setgrab
```
Retrieve the recognition results using:
```commandline
GET /setgrab/{job_Id}
```

The API can be inspected by running the application locally and going to `http://localhost:8000` where there is a Swagger doc available.

### Resources

- [Development Environment Setup](docs/developemental_env_setup.md)
