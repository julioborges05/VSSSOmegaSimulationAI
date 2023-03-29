from ctypes import c_uint16, c_char_p

from bridge.bridge import lib


class Referee:
    """
    Referee client class,
    Use one instance at a time to minimize network errors.
    """

    def __init__(self, mray, addr="224.5.23.2", port=10003):
        """
        Initialize client on addr and port

        default adress: "224.5.23.2"
        default port: 10003
        Fetches the first data.
        """

        self.mray = mray

        # we need to convert the string type
        c_string = addr.encode('utf-8')
        lib.referee_init.argtypes = [c_char_p, c_uint16]

        lib.referee_init(c_string, c_uint16(port))
        self.update()

    def update(self):
        """Fetches new referee data."""
        lib.referee_update()

    def get_data(self):
        """
        Returns a dict with the new data from referee
        or default values (game stoped).
        """
        data = dict()

        try:
            data["foul"] = self.interrupt_type()
            data["yellow"] = self.color() == 1
            data["quad"] = self.get_quadrant()

            data["game_on"] = data["foul"] == 6
            data["our"] = data["yellow"] == self.mray
            data["is_game_halt"] = data["foul"] == 7
        except TypeError:
            return None

        return data

    def interrupt_type(self):
        """
        returns the type of interrupt
        being it a foul, game_on or halt
        From libfira.cpp:
            FREE_KICK = 0
            PENALTY_KICK = 1
            GOAL_KICK = 2
            FREE_BALL = 3
            KICKOFF = 4
            STOP = 5
            GAME_ON = 6
            HALT = 7
        """
        return lib.referee_get_interrupt_type()

    def color(self):
        """
        Returns interrupt color data from libira:
            BLUE = 0,
            YELLOW = 1,
            NONE = 2,
        """
        return lib.referee_interrupt_color()

    def get_quadrant(self):
        """
        returns quadrant on witch foul happened from:
            NO_QUADRANT = 0,
            QUADRANT_1 = 1,
            QUADRANT_2 = 2,
            QUADRANT_3 = 3,
            QUADRANT_4 = 4,
        """
        return lib.referee_get_interrupt_quadrant()

    def __del__(self):
        """Closes network conection."""
        lib.referee_term()
