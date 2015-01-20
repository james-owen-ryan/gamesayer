class Game(object):
    """A game representation for the purposes of Gamesayer."""

    def __init__(self, game_id, title, lsa_vector_str):
        """Initialize a Game object."""
        self.id = game_id
        self.title = title.decode('utf-8')
        self.lsa_vector = self.parse_lsa_vector_str(lsa_vector_str)
        self.gamenet_link = self.get_link_to_gamenet_entry(game_id, title)

    @staticmethod
    def parse_lsa_vector_str(lsa_vector_str):
        lsa_vector = [float(i) for i in lsa_vector_str.split(',')[1:]]  # Exclude first dimension
        return lsa_vector

    @staticmethod
    def get_link_to_gamenet_entry(game_id, title):
        """Return a link to this game's Gamenet entry."""
        url = "http://gamecip-projects.soe.ucsc.edu/gamenet/games/"
        url += game_id
        link = "<a href={} target=_blank>".format(url) + title + "</a>"
        return link
