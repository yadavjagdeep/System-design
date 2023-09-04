from observer_pattern.score_board.processors.abstract_cricket_scoreboard_subscriber import CricketSubscriber
from observer_pattern.score_board.processors.abstract_cricket_scoreboard_publisher import CricketPublisher


class RunRateScoreBoard(CricketSubscriber):

    def __init__(self, cricket_publishers: list[CricketPublisher]):
        self._run = None
        self._overs = None
        self.cricket_publishers = cricket_publishers

    def update(self, publisher: CricketPublisher):
        runs: int = publisher.get_runs()
        overs: float = publisher.get_overs()

        is_updated: bool = False
        if self._run != runs:
            self._run = runs
            is_updated = True

        if self._overs != overs:
            self._overs = overs
            is_updated = True

        if is_updated:
            # logic to persist data in db
            # algorithm to compute run rate score
            # logic to update the board display
            pass
