from bridge.actuator import Actuator

from bridge.referee import Referee
from bridge.bridgeReplacer import BridgeReplacer
from bridge.vision import Vision
from controllers.match.matchParameters import MatchParameters
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
    myRobotsAreYellow = False

    # Initialize all clients
    actuator = Actuator(myRobotsAreYellow, "127.0.0.1", 20011)
    replacement = BridgeReplacer(myRobotsAreYellow, "224.5.23.2", 10004)
    vision = Vision(myRobotsAreYellow, "224.0.0.1", 10002)
    referee = Referee(myRobotsAreYellow, "224.5.23.2", 10003)
    replacer = Replacer(replacement)

    # Main infinite loop
    while True:
        # Update the data received from the referee
        referee.update()
        ref_data = referee.get_data()

        if ref_data["game_on"]:
            # Update vision and data received from the simulator
            vision.update()
            fieldData = vision.get_field_data()

            # Define points to our bots
            matchParameters = MatchParameters(fieldData)
            strategies = Strategies(matchParameters)

            # Define speeds to send it to our bots
            speeds = controller(fieldData, strategies.main_strategy())
            actuator.send_all(speeds)

        elif ref_data["foul"] == FREE_KICK:
            replacer.setDefaultPositions(ref_data, myRobotsAreYellow)
            actuator.stop()

        elif ref_data["foul"] == PENALTY_KICK:
            replacer.setDefaultPositions(ref_data, myRobotsAreYellow)
            actuator.stop()

        elif ref_data["foul"] == GOAL_KICK:
            replacer.setDefaultPositions(ref_data, myRobotsAreYellow)
            actuator.stop()

        elif ref_data["foul"] == FREE_BALL:
            replacer.setDefaultPositions(ref_data, myRobotsAreYellow)
            actuator.stop()

        elif ref_data["foul"] == KICKOFF:
            replacer.setDefaultPositions(ref_data, myRobotsAreYellow)
            actuator.stop()

        elif ref_data["foul"] == HALT:
            actuator.stop()

        elif ref_data["foul"] == KICKOFF:
            replacer.setDefaultPositions(ref_data, myRobotsAreYellow)
            actuator.stop()

        else:
            actuator.stop()
