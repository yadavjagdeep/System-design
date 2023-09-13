from observer_pattern.cricket_scoreboard.confirmation2.processors.cricket_scoreboard_processor import CricketScoreBoardProcessor
from observer_pattern.cricket_scoreboard.confirmation2.processors.projected_scoreboard_processor import ProjectedScoreBoardProcessor
from observer_pattern.cricket_scoreboard.confirmation2.processors.run_rate_scoreboard_processor import RunRateScoreBoardProcessor
from observer_pattern.cricket_scoreboard.confirmation2.processors.top_discussion_board_processor import TopDiscussionBoardProcessor
from observer_pattern.cricket_scoreboard.confirmation2.processors.abstract_publisher import Publisher
from observer_pattern.cricket_scoreboard.confirmation2.processors.abstract_subscriber import Subscriber


class Tester:

    @classmethod
    def __connect(cls, publisher: Publisher, subscribers: list[Subscriber]):
        for subscriber in subscribers:
            publisher.subscribe(subscriber)

    def start(self):
        cricket_score_board_publisher: CricketScoreBoardProcessor = CricketScoreBoardProcessor()
        top_discussion_subscriber: TopDiscussionBoardProcessor = TopDiscussionBoardProcessor(cricket_score_board_publisher)
        run_rate_subscriber: RunRateScoreBoardProcessor = RunRateScoreBoardProcessor(cricket_score_board_publisher)
        projected_score_board_subscriber: ProjectedScoreBoardProcessor = ProjectedScoreBoardProcessor(cricket_score_board_publisher)

        subscribers = [top_discussion_subscriber, run_rate_subscriber, projected_score_board_subscriber]

        self.__connect(cricket_score_board_publisher, subscribers)
