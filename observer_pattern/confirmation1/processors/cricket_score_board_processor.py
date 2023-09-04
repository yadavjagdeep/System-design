from observer_pattern.confirmation1.processors.projected_score_board_processor import ProjectedScoreBoardProcessor
from observer_pattern.confirmation1.processors.top_discussion_board_processor import TopDiscussionBoardProcessor
from observer_pattern.confirmation1.processors.run_rate_scoreboard_processor import RunRateScoreBoardProcessor


class CricketScoreBoardProcessor:
    """
    While creating the object of Scoreboard processor, all the subscribers are injected when the update
    method is called every time with data the same data is injected to all the subscribers
    """
    def __init__(self, projected_scoreboard: ProjectedScoreBoardProcessor,
                 run_rate_scoreboard: RunRateScoreBoardProcessor,
                 top_discussion_board: TopDiscussionBoardProcessor):
        self._runs = None
        self._wickets = None
        self._overs = None
        self.projected_scoreboard = projected_scoreboard
        self.run_rate_scoreboard = run_rate_scoreboard
        self.top_discussion_board = top_discussion_board

    def update(self, runs: int, wickets: int, overs: float):
        self._runs = runs
        self._wickets = wickets
        self._overs = overs

        self.projected_scoreboard.update(runs=runs, wickets=wickets, overs=overs)
        self.run_rate_scoreboard.update(runs=runs, wickets=wickets, overs=overs)
        self.top_discussion_board.update(runs=runs, wickets=wickets, overs=overs)


"""
Although the solution looks good but it have some design flaws:
1. Violation of dependency inversion principle(DIP), here the top level module 'CricketScoreBoardProcessor' depends on
low level entity like 'ProjectedScoreBoardProcessor' and 'RunRateScoreBoardProcessor'

2. There is no way here such that a subscriber class can unsubscribes from the publisher at runtime
"""