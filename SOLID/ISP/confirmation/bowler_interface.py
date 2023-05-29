from abc import ABC, abstractmethod

class Bowler(ABC):

    def __init__(self, player_id):
        self.player_id = player_id

    @abstractmethod
    def bowl(self):
        raise NotImplementedError("Implement in subclass")
