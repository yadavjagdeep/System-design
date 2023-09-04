from observer_pattern.cricket_scoreboard.many_to_many.processors.abstract_subscriber import Subscriber
from observer_pattern.cricket_scoreboard.many_to_many.processors.abstract_publisher import Publisher


class RunRateScoreBoardProcessor(Subscriber):

    def __init__(self, publishers: list[Publisher]):
        self._runs = None
        self._wickets = None
        self._overs = None
        self.publishers = publishers

    def update(self, publisher: Publisher):
        runs: int = publisher.get_runs()
        overs: float = publisher.get_overs()

        is_updated: bool = False
        if self._runs != runs:
            self._runs = runs
            is_updated = True

        if self._overs != overs:
            self._overs = overs
            is_updated = True

        if is_updated:
            # logic to persist data in db
            # algorithm to compute run rate score
            # logic to update the board display
            pass
