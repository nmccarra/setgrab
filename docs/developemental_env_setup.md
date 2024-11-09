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

### Creating ACR Cloud Account

This application requires use of [ACR Cloud](https://www.acrcloud.com/).

Set up an account and obtain values for `host`, `access_key` and `access_secret`.

Insert these values into section `acr` in  `resource/main/config.ini`.

### Running the Application

With a fully set-up development environment, can run application using:
```buildoutcfg
python app.py
```

### Testing
```buildoutcfg
python -m unittest
```


### Docker
The application can also be run inside a Docker container (must have Docker engine installed). 

Run the following at the root of the project:
```buildoutcfg
docker build --tag setgrab .
docker run --publish 3000:8000 setgrab
```
