import urllib.request,json

# Getting api key
SECRET_KEY = None

def configure_request(app):
    global SECRET_KEY
    SECRET_KEY = app.config['SECRET_KEY']