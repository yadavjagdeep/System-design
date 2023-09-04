from abc import ABC, abstractmethod
from observer_pattern.score_board.processors.abstract_cricket_scoreboard_publisher import CricketPublisher


class CricketSubscriber(ABC):

    @abstractmethod
    def update(self, publisher: CricketPublisher):
        raise NotImplementedError(f"subclass must implement the update method !!!")
