from observer_pattern.score_board.processors.abstract_football_scoreboard_publisher import FootballSubscriber
from observer_pattern.score_board.processors.abstract_football_scoreboard_publisher import FootballPublisher


class FootballBoardPublisher(FootballPublisher):
    def __init__(self, subscribers: list[FootballSubscriber]):
        self._goals = None
        self._game_time = None
        self.subscribers = subscribers

    def subscribe(self, subscriber: FootballSubscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: FootballSubscriber):
        self.subscribers.remove(subscriber)

    @property
    def get_goals(self):
        return self._goals

    @property
    def get_game_time(self):
        return self._game_time

    def notify_all(self, goals: int, game_time: str):
        self._goals = goals
        self._game_time = game_time

        for subscribers in self.subscribers:
            subscribers.update(self)
