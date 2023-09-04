class TopDiscussionBoardProcessor:
    def __init__(self):
        self._runs = None
        self._wickets = None
        self._overs = None

    def update(self, runs: int, wickets: int, overs: float):
        is_updated: bool = False
        updated_runs: int = runs
        if updated_runs != self._runs:
            self._runs = updated_runs
            is_updated = True

        updated_wicket: int = wickets
        if updated_wicket != self._wickets:
            self._wickets = updated_wicket
            is_updated = True

        updated_overs: float = overs
        if updated_overs != self._overs:
            self._overs = updated_overs
            is_updated = True

        if is_updated:
            # logic to persist data in db
            # algorithm for top discussion
            # logic to update the board display
            pass
