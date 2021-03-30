# SETGRAB

An API to recognise a set list from given audio

*Developed with Python 3 (Flask framework)*

### Development Environment Setup

This project requires [ffmpeg](https://ffmpeg.org/download.html)

To run the application, ensure that you have created a new virtual environment:

```buildoutcfg
python -m venv setgrab_env
```

##### Activation / Deactivation
To activate this environment:

Windows
```buildoutcfg
setgrab_env/Scripts/activate.bat
```

Unix/MacOs
```buildoutcfg
source setgrab/bin/activate
```

To deactivate:
```buildoutcfg
deactivate
```

#### Install Relevant Packages

Ensure *pip* is up-to-date by running the following in environment:
```buildoutcfg
/path/to/setgrab/setgrab_env/bin/python -m pip install --upgrade pip
```

In this environment, install the relevant packages:

```buildoutcfg
pip install -r requirements.txt
```

### Running the Application

With a fully set-up development environment, can run application using:
```buildoutcfg
python main/main.py
```
There is a Swagger UI at the root address of the API for documentation and for testing the endpoints.

#### Docker
The application can also be run inside a Docker container (must have Docker engine installed). 

Run the following at the root of the project:
```buildoutcfg
docker build --tag setgrab .
docker run --publish 3000:8000 setgrab
```

The application will listen on port 8000, however if using the Docker commands above, requests should be directed to port 3000 as this is the external port to which the container is bound.

##### Other Useful Docker Commands
List all running containers:
```buildoutcfg
docker ps
```
Stop all running containers:
```buildoutcfg
docker kill $(docker ps -q)
```
Delete all stopped containers:
```buildoutcfg
docker rm $(docker ps -a -q)
```
Exec into container and start a Bash session:
```buildoutcfg
docker exec -it <container name> /bin/bash
```