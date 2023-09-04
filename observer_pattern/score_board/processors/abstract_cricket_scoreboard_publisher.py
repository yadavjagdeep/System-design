from abc import ABC, abstractmethod
from observer_pattern.score_board.processors.abstract_cricket_scoreboard_subscriber import CricketSubscriber


class  CricketPublisher(ABC):

    @abstractmethod
    def unsubscribe(self, subscriber: CricketSubscriber):
        raise NotImplementedError("subclass must implement publisher method !!! ")

    @abstractmethod
    def subscribe(self, subscriber: CricketSubscriber):
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
