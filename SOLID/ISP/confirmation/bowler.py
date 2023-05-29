from fielder_interface import Fielder
from bowler_interface import Bowler

class PureBowler(Fielder, Bowler):

    def __init__(self, player_id):
        super().__init__(player_id)

    def bowl(self):
        print(f"{self.player_id} => Bowling as {self.__class__.__name__}")

    def field(self):
        print(f"{self.player_id} => Fielding as {self.__class__.__name__}")
