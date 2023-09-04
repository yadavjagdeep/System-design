from abc import ABC, abstractmethod
from observer_pattern.cricket_scoreboard.confirmation2.processors.abstract_subscriber import Subscriber


class Publisher(ABC):

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber):
        raise NotImplementedError("subclass must implement publisher method !!! ")

    @abstractmethod
    def subscribe(self, subscriber: Subscriber):
        raise NotImplementedError("subclass must implement subscriber method !!! ")

    @abstractmethod
    def notify_all(self, runs: int, wickets: int, overs: float):
        raise NotImplementedError("subclass must implement notify_all method !!! ")

    @abstractmethod
    def get_runs(self):
        raise NotImplementedError("subclass must implement get_runs method !!! ")

    @abstractmethod
    def get_overs(self):
        raise NotImplementedError("subclass must implement get_overs method !!! ")

    @abstractmethod
    def get_wickets(self):
        raise NotImplementedError("subclass must implement get_wickets method !!! ")
