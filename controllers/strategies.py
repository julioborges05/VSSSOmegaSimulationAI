from bridge.entity import Entity
from bridge.bridge import NUM_BOTS
from controllers.robots.goalKeeper import GoalKeeper


class Strategies:
    def __init__(self, matchParameters):
        self.matchParameters = matchParameters

    def main_strategy(self):
        """Sets all objetives to ball coordinates."""
        ball = self.matchParameters.ballValues
        objectives = [Entity(index=i) for i in range(NUM_BOTS)]
        objectives[0] = GoalKeeper(self.matchParameters).setGoalKeeperCoordinates()

        objectives[1] = Entity()
        objectives[2] = Entity()
        objectives[1].x = ball.x
        objectives[1].y = ball.y
        objectives[2].x = ball.x
        objectives[2].y = ball.y

        return objectives
