from observer_pattern.cricket_scoreboard.confirmation2.processors.abstract_subscriber import Subscriber
from observer_pattern.cricket_scoreboard.confirmation2.processors.abstract_publisher import Publisher


class TopDiscussionBoardProcessor(Subscriber):

    def __init__(self, publisher: Publisher):
        self._runs = None
        self._wickets = None
        self._overs = None
        self.publisher = publisher

    def update(self, runs: int, wickets: int, overs: float):
        is_updated: bool = False
        if self._runs != runs:
            self._runs = runs
            is_updated = True

        if self._wickets != wickets:
            self._wickets = wickets
            is_updated = True

        if self._overs != overs:
            self._overs = overs
            is_updated = True

        if is_updated:
            # logic to persist data in db
            # algorithm for top discussion
            # logic to update the board display
            pass
