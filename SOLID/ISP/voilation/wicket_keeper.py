from players import Player

class WicketKeeper(Player):

    def __init__(self, player_id):
        super().__init__(player_id)

    def bat(self):
        print(f"{self.player_id} -> Batting in {self.__class__.__name__}")

    def keep_wicket(self):
        print(f"{self.player_id} -> Keeping wicket in {self.__class__.__name__}")

    def bowl(self):
        raise Exception("Wicket keeper cannot bowl")

    def field(self):
        raise Exception("Wicket keeper cannot field")

