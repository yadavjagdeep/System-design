from abc import ABC, abstractmethod
from observer_pattern.cricket_scoreboard.confirmation2.processors.abstract_subscriber import Subscriber


class Publisher(ABC):

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber):
        raise NotImplementedError("subclass must implement publisher method !!! ")

    @abstractmethod
    def subscribe(self, subscriber: Subscriber):
        raise NotImplementedError("subclass must implement subscriber method !!! ")

    def notify_all(self, runs: int, wickets: int, overs: float):
        raise NotImplementedError("subclass must implement notify_all method !!! ")
