from all_rounder import AllRounder
from batter import Batter
from bowler import Bowler
from wicket_keeper import WicketKeeper


if __name__ == "__main__":
    players = [Batter("BT1"), Batter("BT2"), Batter("BT3"), Batter("BT4"), WicketKeeper("WT"), AllRounder("ALL1"),
               AllRounder("ALL2"), Bowler("B1"), Bowler("B2"), Bowler("B3"), Bowler("B4")]

    for player in players:
        if isinstance(player, (Batter, AllRounder, WicketKeeper)):
            player.bat()
        if isinstance(player, (Bowler, AllRounder)):
            player.bowl()
        if not isinstance(player, WicketKeeper):
            player.field()
        if isinstance(player, WicketKeeper):
            player.keep_wicket()

"""
- We had to add these isinstance conditions which is not good
- If we remove these remove these conditions
- Now when we run this will get exception "Exception: Batter cannot bowl"
"""
