from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cronjobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def init_db():
    db.create_all()
