from players import Player

class AllRounder(Player):

    def __init__(self, player_id):
        super().__init__(player_id)

    def bat(self):
        print(f"{self.player_id} -> All-Rounder is Batting as {self.__class__.__name__}")

    def bowl(self):
        print(f"{self.player_id} -> All-Rounder is Bowling as {self.__class__.__name__}")

    def field(self):
        print(f"{self.player_id} -> All-Rounder is Fielding as {self.__class__.__name__}")

    def keep_wicket(self):
        raise Exception("All-Rounder cannot keep-wicket")
