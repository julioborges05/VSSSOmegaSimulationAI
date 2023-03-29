from bridge.actuator import Actuator

from bridge.referee import Referee
from bridge.bridgeReplacer import BridgeReplacer
from bridge.vision import Vision
from controllers.replacer import Replacer
from controllers.strategies import Strategies
from controllers.controls import controller

FREE_KICK = 0
PENALTY_KICK = 1
GOAL_KICK = 2
FREE_BALL = 3
KICKOFF = 4
STOP = 5
GAME_ON = 6
HALT = 7

if __name__ == "__main__":
    # Choose team (my robots are yellow)
    mray = False

    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = BridgeReplacer(mray, "224.5.23.2", 10004)
    vision = Vision(mray, "224.0.0.1", 10002)
    referee = Referee(mray, "224.5.23.2", 10003)
    replacer = Replacer(replacement)

    # Main infinite loop
    while True:
        referee.update()
        ref_data = referee.get_data()

        vision.update()
        field = vision.get_field_data()

        if ref_data["game_on"]:
            objectives = Strategies.main_strategy(field)
            speeds = controller(field, objectives)
            actuator.send_all(speeds)

        elif ref_data["foul"] == FREE_KICK:
            replacer.setDefaultPositions(ref_data, mray)
            actuator.stop()

        elif ref_data["foul"] == PENALTY_KICK:
            replacer.setDefaultPositions(ref_data, mray)
            actuator.stop()

        elif ref_data["foul"] == GOAL_KICK:
            replacer.setDefaultPositions(ref_data, mray)
            actuator.stop()

        elif ref_data["foul"] == FREE_BALL:
            replacer.setDefaultPositions(ref_data, mray)
            actuator.stop()

        elif ref_data["foul"] == KICKOFF:
            replacer.setDefaultPositions(ref_data, mray)
            actuator.stop()

        elif ref_data["foul"] == HALT:
            replacer.setDefaultPositions(ref_data, mray)
            actuator.stop()

        elif ref_data["foul"] == KICKOFF:
            replacer.setDefaultPositions(ref_data, mray)
            actuator.stop()

        else:
            actuator.stop()
