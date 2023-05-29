from batter_interface import Batter
from fielder_interface import Fielder

class PureBatter(Batter, Fielder):

    def __init__(self, player_id):
        super().__init__(player_id)

    def bat(self):
        print(f"{self.player_id} => Batting as {self.__class__.__name__}")

    def field(self):
        print(f"{self.player_id} => Fielding as {self.__class__.__name__}")
