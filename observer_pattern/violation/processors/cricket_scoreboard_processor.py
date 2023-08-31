class CricketScoreBoardProcessor:

    def __init__(self):
        self._runs = None
        self._wickets = None
        self._overs = None

    def update_score(self, runs: int, wickets: int, overs: float):
        self._runs = runs
        self._wickets = wickets
        self._overs = overs

    @property
    def get_runs(self):
        return self._runs

    @property
    def get_wickets(self):
        return self._wickets

    @property
    def get_overs(self):
        return self._overs
