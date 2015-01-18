import csv
from flask import Flask, render_template, jsonify
from gamesayer import Gamesayer
from game import Game


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chosenGames=<chosen_game_ids>')
def gamesay(chosen_game_ids):
    gamesayer = Gamesayer(database=app.database, chosen_game_ids=chosen_game_ids)
    most_related_game = gamesayer.gamesay()
    return jsonify(gamenet_link=most_related_game.gamenet_link)

def load_database():
    """Load the database of game representations from a TSV file."""
    database = []
    with open('static/game_lsa_vectors.tsv', 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            game_id, title, year, lsa_vector_str = row
            game_object = Game(game_id, title, lsa_vector_str)
            database.append(game_object)
    return database

if __name__ == '__main__':
    app.database = load_database()
    app.run(debug=False)
