from players import Player

class Batter(Player):

    def __init__(self, player_id):
        super().__init__(player_id)

    def bat(self):
        print(f"{self.player_id} -> Batting as {self.__class__.__name__}")

    def field(self):
        print(f"{self.player_id} -> Fielding as {self.__class__.__name__}")

    def bowl(self):
        raise Exception("Batter cannot bowl")

    def keep_wicket(self):
        raise Exception("Batter cannot keep wicket")
