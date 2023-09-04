from observer_pattern.score_board.processors.abstract_football_scoreboard_subscriber import FootballSubscriber
from observer_pattern.score_board.processors.abstract_cricket_scoreboard_subscriber import CricketSubscriber
from observer_pattern.score_board.processors.abstract_cricket_scoreboard_publisher import CricketPublisher
from observer_pattern.score_board.processors.football_publisher import FootballPublisher
from typing import overload, Tuple, Optional


class PredictedScoreBoardSubscriber(CricketSubscriber, FootballSubscriber):

    def __init__(self, cricket_publishers: list[CricketPublisher], football_publishers: list[FootballPublisher]):
        self._runs = None
        self._wickets = None
        self._overs = None
        self._goals = None
        self._game_time = None
        self.cricket_publishers = cricket_publishers
        self.football_publishers = football_publishers

    @overload
    def update(self, publisher: CricketPublisher):
        pass

    @overload
    def update(self, publisher: FootballPublisher):
        pass

    def update(self, publisher: Tuple[Optional[CricketPublisher], Optional[FootballPublisher]]):
        if isinstance(publisher, CricketPublisher):
            self._runs = publisher.get_runs()
            self._wickets = publisher.get_wickets()
            self._overs = publisher.get_overs()
            # implement the logic here for cricket scoreboard prediction
        elif isinstance(publisher, FootballPublisher):
            self._goals = publisher.get_goals()
            self._game_time = publisher.get_game_time()
            # implement the logic here for cricket scoreboard prediction
        else:
            raise RuntimeError("Unknown publisher name !!! ")


"""
Since python does not support 'method-overloading' we have archived it using using typing lib
But this for static checking only it does not retracts on runtime
"""

