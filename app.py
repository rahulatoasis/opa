import config

from os import urandom
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

if __name__ == '__main__':
  from core.views import *
  app.run(debug = config.WEB_DEBUG,
          host  = config.WEB_HOST,
          port  = config.WEB_PORT,
          threaded=True,
          use_evalex=False)
