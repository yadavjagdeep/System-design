from observer_pattern.cricket_scoreboard.confirmation2.processors.abstract_publisher import Publisher
from observer_pattern.cricket_scoreboard.confirmation2.processors.abstract_subscriber import Subscriber


class CricketScoreBoardProcessor(Publisher):

    def __init__(self, subscribers: list[Subscriber]):
        self._runs = None
        self._wickets = None
        self._overs = None
        self.subscribers = subscribers

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def notify_all(self, runs: int, wickets: int, overs: float):
        self._runs = runs
        self._wickets = wickets
        self._overs = overs

        for subscribers in self.subscribers:
            subscribers.update(runs=self._runs, wickets=self._wickets, overs=self._overs)
