from random import choices
from flask import redirect, render_template, request
from app import app
from models.game import *
from models.player import Player
from models.players import players, add_new_choice

@app.route('/')
def index():
    return render_template("index.html", title="Home", players=players)

@app.route('/player2', methods=["POST"])
def add_player2_choice():
    player_1_name = request.form["name"]
    player_1_choice = request.form["choice"]
    new_choice = Player(player_1_name, player_1_choice)
    add_new_choice(new_choice )
    return render_template ("player2.html", title="player2", players=players)


@app.route('/game', methods=["POST"])
def add_choices():
    player_2_name = request.form["name"]
    player_2_choice = request.form["choice"]
    new_choice = Player(player_2_name, player_2_choice)
    add_new_choice(new_choice )
    return render_template ("index_game.html", title="Game", players=players)

@app.route('/game', methods=["POST"])
def add_winner():
    player_1_choice = request.form["choice"]
    player_2_choice = request.form["choice"]
    return game(player_1_choice, player_2_choice)
    
