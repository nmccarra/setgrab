# SETGRAB

An API to recognise a set list from given audio


![setgrab-api-layers](https://user-images.githubusercontent.com/26139776/111034222-786fd100-840c-11eb-8909-ca608f8aef96.png)


*Developed with Python 3 (Flask framework)*

### Run

#### Virtual Environment Setup
To run the application, first ensure that you have created a new virtual environment:

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

#### Running the Application

In the environment:
```buildoutcfg
python main/main.py
```
This will start up the application on port *8080*.

There is a Swagger UI at the root address of the API for documentation and for testing the endpoints.
