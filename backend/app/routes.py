import csv
from flask import Flask, render_template, jsonify
from gamesayer import Gamesayer


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chosenGames=<chosen_game_ids>')
def gamesay(chosen_game_ids):
    gamesayer = Gamesayer(database=app.database, chosen_game_ids=chosen_game_ids)
    most_related_game = gamesayer.gamesay()
    game_id, title, year = most_related_game
    return jsonify(game_id=game_id, title=title, year=year)

def load_database():
    """Load the database of game representations from a TSV file."""
    database = []
    with open('static/game_lsa_vectors.tsv', 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            game_id, title, year, vector = row
            vector = [float(i) for i in vector.split(',')[1:]]  # Exclude first dimension
            database.append((game_id, title, year, vector))
    return database

if __name__ == '__main__':
    app.database = load_database()
    app.run(debug=False)
