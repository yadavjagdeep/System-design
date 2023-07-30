from batter import Batter
from bowler import Bowler
from wicket_keeper import WicketKeeper
from all_rounder import AllRounder
from cricket_game_helper import CricketGameHelper

class Test:

    def __init__(self, pure_batter: list, pure_bowler: list, all_rounder: list, keeper: list):
        self.pure_batter = pure_batter
        self.pure_bowler = pure_bowler
        self.all_rounder = all_rounder
        self.keeper = keeper

    def simulate(self):
        self.start_batting()
        self.start_keeping()
        self.start_bowling()
        self.start_fielding()
    def start_batting(self):
        for batter in self.pure_batter:
            CricketGameHelper().bat(batter)

        for keeper in self.keeper:
            CricketGameHelper().bat(keeper)

        for all_rounder in self.all_rounder:
            CricketGameHelper().bat(all_rounder)


    def start_bowling(self):
        for bowler in self.pure_bowler:
            CricketGameHelper().bowl(bowler)

        for all_rounder in self.all_rounder:
            CricketGameHelper().bowl(all_rounder)


    def start_keeping(self):
        for keeper in self.keeper:
            CricketGameHelper().keep_wicket(keeper)

    def start_fielding(self):
        for batter in self.pure_batter:
            CricketGameHelper().field(batter)

        for all_rounder in self.all_rounder:
            CricketGameHelper().field(all_rounder)

        for bowler in self.pure_bowler:
            CricketGameHelper().field(bowler)


if __name__ == "__main__":
    _pure_batter = [Batter("BT1"), Batter("BT2"), Batter("BT3"), Batter("BT4")]
    _pure_bowler = [Bowler("B1"), Bowler("B2"), Bowler("B3"), Bowler("B4")]
    _all_rounder = [AllRounder("ALL1"), AllRounder("ALL2")]
    _keeper = [WicketKeeper("WT")]

    Test(_pure_batter, _pure_bowler, _all_rounder, _keeper).simulate()