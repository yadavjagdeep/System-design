from abc import ABC


class Pizza(ABC):

    def __init__(self, name: str, cost: float):
        self._name = name
        self._cost = cost

    def get_name(self):
        return self._name

    def get_cost(self):
        return self._cost
