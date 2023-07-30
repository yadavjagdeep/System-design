from abc import ABC, abstractmethod

class Batter(ABC):

    def __init__(self, player_id):
        self.player_id = player_id

    @abstractmethod
    def bat(self):
        raise NotImplementedError("Implement in subclass")

