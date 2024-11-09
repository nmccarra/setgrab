
![setgrab logo](docs/assets/setgrab_banner.png)
# setgrab
![Python](https://img.shields.io/badge/python-3.8-blue)

Give setgrab a URL to a DJ set on YouTube and it will try to recognise the songs played.

### Getting Started

Follow the [Development Environment Setup](docs/developemental_env_setup.md) page so that you can run the application locally.

Create a recognition job using:
```commandline
curl --location --request POST 'localhost:8000/setgrab' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url" : "<url>",
    "start_time" : "00:00"
}'
```
Retrieve the recognition results using:
```commandline
curl --location --request GET 'localhost:8000/setgrab/<job-id>'
```

The API can be inspected by running the application locally and going to `http://localhost:8000` where there is a Swagger doc available.

### Resources

- [Development Environment Setup](docs/developemental_env_setup.md)
