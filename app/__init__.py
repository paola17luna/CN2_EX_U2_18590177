import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.models import Contacto
from app.routes.contacto import contacto_bp

with app.app_context():
    db.create_all()

app.register_blueprint(contacto_bp, url_prefix='/contactos')

@app.route('/')
def index():
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos)