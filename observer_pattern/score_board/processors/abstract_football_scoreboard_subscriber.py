from abc import ABC, abstractmethod
from observer_pattern.score_board.processors.abstract_football_scoreboard_publisher import FootballPublisher


class FootballSubscriber(ABC):

    @abstractmethod
    def update(self, publisher: FootballPublisher):
        raise NotImplementedError(f"subclass must implement the update method !!!")
