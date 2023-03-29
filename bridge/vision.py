from ctypes import (c_char_p, c_uint16, c_int32, c_bool)

from bridge.bridge import lib, NUM_BOTS, convert_length, convert_width, convert_angle
from bridge.entity import Entity


class Vision:
    """
    Class for the vision client,
    Use one instance at a time to minimize network errors.
    """

    def __init__(self, mray, addr="224.0.0.1", port=10002):
        """
        Constructor initialized with adress and port

        default address: "224.0.0.1"
        default port: 10002
        Fetches the first field.
        """

        self.mray = mray

        # we need to convert the string type
        c_string = addr.encode('utf-8')
        lib.actuator_init.argtypes = [c_char_p, c_uint16, c_bool]

        lib.vision_init(c_string, c_uint16(port))
        # already update once
        self.update()

    def update(self):
        """Fetches client data."""
        return lib.vision_update_field()

    def get_field_data(self):
        """
            Returns a dict with the field info, 2 lists of entities
            one for each team robots and a ball entity
        """

        field = dict()
        field["mray"] = self.mray
        try:
            field["yellow"] = [self.get_robot(i, True) for i in range(NUM_BOTS)]
            field["blue"] = [self.get_robot(i, False) for i in range(NUM_BOTS)]
            if self.mray:
                field["our_bots"] = field["yellow"]
                field["their_bots"] = field["blue"]
            else:
                field["our_bots"] = field["blue"]
                field["their_bots"] = field["yellow"]

            field["ball"] = self.get_ball()
        except TypeError:
            return None

        return field

    def get_ball(self):
        """
        Returns an Entity with the ball data
        Use after the update method.
        """

        try:
            # fills and return the new object
            ball = Entity()
            # positions
            ball.x = convert_length(lib.vision_get_ball_x())
            ball.y = convert_width(lib.vision_get_ball_y())
            # speds
            ball.vx = lib.vision_get_ball_vx()
            ball.vy = lib.vision_get_ball_vy()
        except TypeError:
            return None

        return ball

    def get_robot(self, index, yellow):
        """
        Returns a Entity with the bot data
        bot is given by index and get_yellow parameters
        Use after the update method.
        """

        try:
            # fills and return bot object
            # get position
            bot = Entity()
            bot.x = convert_length(
                lib.vision_robot_x(c_int32(index), c_bool(yellow)))
            bot.y = convert_width(
                lib.vision_robot_y(c_int32(index), c_bool(yellow)))
            bot.a = convert_angle(
                lib.vision_robot_angle(c_int32(index), c_bool(yellow)))
            # get speeds
            bot.vx = lib.vision_robot_vx(c_int32(index), c_bool(yellow))
            bot.vy = lib.vision_robot_vy(c_int32(index), c_bool(yellow))
            bot.va = lib.vision_robot_vangle(c_int32(index), c_bool(yellow))
            bot.index = index

        except TypeError:
            return None
        return bot

    def __del__(self):
        """Closes network connection"""
        lib.vision_term()
