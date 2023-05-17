from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = '26d1bd3fcee5a4df129522e7'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from app import routes