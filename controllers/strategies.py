from bridge.entity import Entity
from bridge.bridge import NUM_BOTS


class Strategies:
    def main_strategy(field):
        """Sets all objetives to ball coordinates."""
        ball = field["ball"]
        objectives = [Entity(index=i) for i in range(NUM_BOTS)]
        for obj in objectives:
            obj.x = ball.x
            obj.y = ball.y

        return objectives