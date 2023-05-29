from wicket_keeper_interface import WicketKeeper
from batter_interface import Batter

class Keeper(WicketKeeper, Batter):

    def __init__(self, player_id):
        super().__init__(player_id)

    def bat(self):
        print(f"{self.player_id} => Batting as {self.__class__.__name__}")

    def keep_wicket(self):
        print(f"{self.player_id} => Keeping wicket as {self.__class__.__name__}")
