from models.players import *
class Game:
    def __init__(self, players):
        self.players = players
    

def game():
    for player in players:
        if player.choice == "rock" and player.choice == "paper":
            return "Paper wins"
        if player.choice == "rock" and player.choice == "paper":
            return "Paper wins"
        elif player.choice  == "paper" and player.choice == "scissors":
            return "Scissors win"
        elif player.choice  == "scissors" and player.choice== "rock":
            return "Rock wins"
        elif player.choice == player.choice:
            return f"Both players selected {player.choice}. It's a tie!"