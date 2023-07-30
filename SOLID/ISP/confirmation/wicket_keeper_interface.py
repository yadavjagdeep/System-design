from abc import ABC, abstractmethod

class WicketKeeper(ABC):

    def __init__(self, player_id):
        self.player_id = player_id

    @abstractmethod
    def keep_wicket(self):
        raise NotImplementedError("Implement in subclass")
