from observer_pattern.cricket_scoreboard.violation.processors.cricket_scoreboard_processor import CricketScoreBoardProcessor


class RunRateScoreBoardProcessor:

    def __init__(self, cricket_score_board: CricketScoreBoardProcessor):
        self._runs = None
        self._wickets = None
        self._overs = None
        self.cricket_score_board = cricket_score_board

    def update(self):
        while True:
            is_updated: bool = False
            updated_runs: int = self.cricket_score_board.get_runs
            if updated_runs != self._runs:
                self._runs = updated_runs
                is_updated = True

            updated_wickets: int = self.cricket_score_board.get_wickets
            if updated_wickets != self._wickets:
                self._wickets = updated_wickets
                is_updated = True

            updated_overs: float = self.cricket_score_board.get_overs
            if updated_overs != self._overs:
                self._overs = updated_overs
                is_updated = True

            if is_updated:
                # logic to persist data in db
                # algorithm to compute run rate
                # logic to update the board display
                pass
