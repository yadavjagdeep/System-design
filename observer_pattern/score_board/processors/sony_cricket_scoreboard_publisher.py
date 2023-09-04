from observer_pattern.score_board.processors.abstract_cricket_scoreboard_publisher import CricketPublisher
from observer_pattern.score_board.processors.abstract_cricket_scoreboard_subscriber import CricketSubscriber


class SonyCricketScoreBoardPublisher(CricketPublisher):

    def __init__(self, subscribers: list[CricketSubscriber]):
        self._runs = None
        self._wickets = None
        self._overs = None
        self.subscribers = subscribers

    def subscribe(self, subscriber: CricketSubscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: CricketSubscriber):
        self.subscribers.remove(subscriber)

    @property
    def get_runs(self):
        return self._runs

    @property
    def get_wickets(self):
        return self._wickets

    @property
    def get_overs(self):
        return self._overs

    def notify_all(self, runs: int, wickets: int, overs: float):
        self._runs = runs
        self._wickets = wickets
        self._overs = overs

        for subscribers in self.subscribers:
            subscribers.update(self)
