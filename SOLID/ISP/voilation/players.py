"""
- ISP(Interface segregation principle)
- Idea: if we do not have strict 'is-a' relationship b/w parent and child class, we should avoid inheritance
- Instead we can create multiple interfaces and use them a basis use case
"""
" => let's understand basis an example of designing a class to create cricket players object basis role"

"""
 => consider these as rules of the game
 
 :Batter -> bat and field
 :Wicketkeeper -> bat and keep-wicket
 :All-Rounder -> bat, bowl, field
 :Bowler -> bowl anf field
"""
from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, player_id):
        self.player_id = player_id

    @abstractmethod
    def bat(self):
        raise NotImplementedError("Implement in subclass")

    @abstractmethod
    def bowl(self):
        raise NotImplementedError("Implement in subclass")

    @abstractmethod
    def field(self):
        raise NotImplementedError("Implement in subclass")

    @abstractmethod
    def keep_wicket(self):
        raise NotImplementedError("Implement in subclass")


"""
- Problem with this abstract class is all the concreate classes implementing it will have to implement all methods, where as
  the relation-ship b/w the class is not strict 'is-a'
- Hence, violates (LSP)

- We can resolve this with (ISP) interface segregation principle, where will have diff interfaces with diff game attributes

"""