from abc import ABC, abstractmethod
from observer_pattern.score_board.processors.abstract_football_scoreboard_subscriber import FootballSubscriber


class FootballPublisher(ABC):

    @abstractmethod
    def unsubscribe(self, subscriber: FootballSubscriber):
        raise NotImplementedError("subclass must implement publisher method !!! ")

    @abstractmethod
    def subscribe(self, subscriber: FootballSubscriber):
        raise NotImplementedError("subclass must implement subscriber method !!! ")

    @abstractmethod
    def notify_all(self, goals: int, game_time: str):
        raise NotImplementedError("subclass must implement notify_all method !!! ")

    @abstractmethod
    def get_goals(self):
        raise NotImplementedError("subclass must implement get_goals method !!! ")

    @abstractmethod
    def get_game_time(self):
        raise NotImplementedError("subclass must implement get_game_time method !!! ")
