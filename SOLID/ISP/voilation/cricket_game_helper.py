from batter import Batter
from bowler import Bowler
from all_rounder import AllRounder
from wicket_keeper import WicketKeeper
class CricketGameHelper:

    def bat(self, player: object):
        if not isinstance(player, Bowler):
            player.bat()

    def bowl(self, player: object):
        if not isinstance(player, (Batter, WicketKeeper)):
            player.bowl()

    def field(self, player: object):
        if not isinstance(player, WicketKeeper):
            player.field()

    def keep_wicket(self, player: object):
        if not isinstance(player, (Batter, Bowler, AllRounder)):
            player.keep_wicket()

"""
- We have these if checks to ensure if by mistake client invokes an operation that player does not support then we can skip that call
as he can make the call practically as all the concrete class inherits and implements player abstract class
"""