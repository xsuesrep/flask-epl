from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.sqlite'
app.secret_key = b'qegqgqq3hq3hq'

db = SQLAlchemy(app)
Migrate = Migrate(app, db) 

from epl import models , routes