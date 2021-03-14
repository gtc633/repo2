from flask import Flask
from myapp.admin import admin
import config

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(admin)

from . import views