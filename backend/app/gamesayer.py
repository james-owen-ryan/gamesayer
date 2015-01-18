import numpy


class Gamesayer(object):
    """A class specifying objects that each return the game most
    related to a group of user-chosen games.
    """

    def __init__(self, database, chosen_game_ids):
        """Initialize a Gamesayer object."""
        self.database = database
        self.most_related_game = self.get_most_related_game(chosen_game_ids=chosen_game_ids)

    def gamesay(self):
        """Return the most-related game."""
        return self.most_related_game

    def get_most_related_game(self, chosen_game_ids):
        """Get the most-related game to the user's chosen games.

        This is determined by taking each game in the database that is not one of the
        selected games and getting its average cosine similarity with each of the selected
        games -- the most related game is then the game with the highest such average.
        """
        chosen_game_ids = chosen_game_ids.split('+')
        chosen_game_ids = [int(game_id) for game_id in chosen_game_ids]
        chosen_games = [self.database[game_id] for game_id in chosen_game_ids]
        cumulative_scores_for_each_game_relative_to_the_chosen_games = {}
        for game in self.database:
            game_id = int(game.id)
            if game_id not in chosen_game_ids:
                scores = []
                for chosen_game in chosen_games:
                    scores.append(self.lsa_score(game, chosen_game))
                cumulative_score = sum(scores)/len(scores)
                cumulative_scores_for_each_game_relative_to_the_chosen_games[game_id] = cumulative_score
        id_of_most_related_game = (
            max(cumulative_scores_for_each_game_relative_to_the_chosen_games, 
                key=lambda g: cumulative_scores_for_each_game_relative_to_the_chosen_games[g])
        )
        most_related_game = self.database[id_of_most_related_game]
        return most_related_game

    @staticmethod
    def lsa_score(game1, game2):
        """Return a cosine similarity score for a pair of games."""
        cosine_between_the_games_lsa_vectors = (
            numpy.dot(game1.lsa_vector, game2.lsa_vector) /
            numpy.linalg.norm(game1.lsa_vector) /
            numpy.linalg.norm(game2.lsa_vector)
        )
        return cosine_between_the_games_lsa_vectors
