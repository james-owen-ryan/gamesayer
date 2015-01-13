from flask import Flask, render_template, jsonify
from gamesayer import Gamesayer


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chosenGames=<chosen_game_ids>')
def gamesay(chosen_game_ids):
    gamesayer = Gamesayer(chosen_game_ids=chosen_game_ids)
    most_related_game = gamesayer.gamesay()
    game_id, title, year = most_related_game
    return jsonify(game_id=game_id, title=title, year=year)

if __name__ == '__main__':
    app.run(debug=False)
