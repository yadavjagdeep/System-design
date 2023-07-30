from abc import ABC, abstractmethod

class Fielder(ABC):

    def __init__(self, player_id):
        self.player_id = player_id

    @abstractmethod
    def field(self):
        raise NotImplementedError("Implement in subclass")
