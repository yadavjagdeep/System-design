from players import Player

class Bowler(Player):

    def __init__(self, player_id):
        super().__init__(player_id)

    def bowl(self):
        print(f"{self.player_id} -> Bowling as {self.__class__.__name__}")

    def bat(self):
        raise Exception("Bowler cannot bat")

    def field(self):
        print(f"{self.player_id} -> Fielding as {self.__class__.__name__}")

    def keep_wicket(self):
        raise Exception("Bowler cannot keep wicket")
