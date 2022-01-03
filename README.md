# Plagiarism Checker

This app is built using Python 3.9+, Flask 2.0+.

## Running the app locally

Begin by cloning this git repo and navigating to the project directory.

Next, create a virtual environment and activate it:

```
python -m venv venv
venv/bin/activate //or venv/Script/activate according to venv version.
```

Install dependencies by running:

```
python -m pip install -r requirements.txt
```

Finally, to run the app on your machine, simply run this command from the terminal:

```
flask run
```
or:
```
venv/Scripts/python app.py
```


Or, to run the app in debug mode, add the `FLASK_ENV=development` environment variable before the command:

```
FLASK_ENV=development flask run
```

The app should now be running on http://127.0.0.1:5000 in your browser.

## Resources

Python, pyenv, and pip
- https://realpython.com/intro-to-pyenv/
- https://github.com/pyenv/pyenv
- https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-shell
- https://pip.pypa.io/en/latest/user_guide/#requirements-files
- https://www.twilio.com/blog/environment-variables-python

Flask
- https://flask.palletsprojects.com/en/2.0.x/installation/
- https://flask.palletsprojects.com/en/2.0.x/quickstart/
- https://flask.palletsprojects.com/en/2.0.x/tutorial/
- https://github.com/pallets/flask/tree/main/examples/tutorial
- https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request
