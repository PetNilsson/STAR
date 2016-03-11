"""
The flask application package.
"""

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'host':"mongodb://mongo-timereport:K8._7fr92uQ_MDoh1SoQ1VUnu.quW2ELgfCv5eBRrA0-@ds062178.mlab.com:62178/mongo-timereport"
}

db = MongoEngine(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

import FlaskWebProject.views, FlaskWebProject.auth
