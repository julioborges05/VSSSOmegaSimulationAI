from bridge.actuator import Actuator

from bridge.referee import Referee
from bridge.replacer import Replacer
from bridge.vision import Vision
from controllers.strategies import Strategies
from controllers.controls import controller

if __name__ == "__main__":
    # Choose team (my robots are yellow)
    mray = False

    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = Replacer(mray, "224.5.23.2", 10004)
    vision = Vision(mray, "224.0.0.1", 10002)
    referee = Referee(mray, "224.5.23.2", 10003)

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

        elif ref_data["foul"] != 7:
            # foul behaviour
            actuator.stop()

        else:
            # halt behavior
            actuator.stop()
