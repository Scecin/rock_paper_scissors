from flask import render_template, template_rendered
from app import app
from models.player import Player

@app.route('/')
def index():
    return render_template("index.html", title="Home")