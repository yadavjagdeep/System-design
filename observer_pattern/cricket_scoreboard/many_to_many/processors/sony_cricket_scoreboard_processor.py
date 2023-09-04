from observer_pattern.cricket_scoreboard.many_to_many.processors.abstract_publisher import Publisher
from observer_pattern.cricket_scoreboard.many_to_many.processors.abstract_subscriber import Subscriber


class SonyCricketScoreBoardProcessor(Publisher):

    def __init__(self, subscribers: list[Subscriber]):
        self._runs = None
        self._wickets = None
        self._overs = None
        self.subscribers = subscribers

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
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
