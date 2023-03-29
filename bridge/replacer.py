from ctypes import c_int32, c_double, c_char_p, c_uint16, c_bool
from math import degrees

from bridge.bridge import lib, inverse_length, inverse_width


class Replacer:
    """
    Actuator client class,
    Use one instance at a time to minimize network errors.
    """

    def __init__(self, my_robots_are_yellow, addr="224.5.23.2", port=10004):
        """
        Initialize client on addr and port

        default address: "224.5.23.2"
        default port: 10004
        requires bool team_color to later commands.
        """
        c_string = addr.encode('utf-8')
        lib.actuator_init.argtypes = [c_char_p, c_uint16, c_bool]

        lib.replacer_init(c_string, c_uint16(port), c_bool(my_robots_are_yellow))

    def place(self, index, x, y, angle):
        """
            Sends an index indicated bot to x, y and angle.
            *Needs to use self.send() to actually send, or use place_all
        """
        lib.replacer_place_robot(c_int32(index), c_double(inverse_length(x)), c_double(inverse_width(y)), c_double(angle))

    def place_all(self, placement):
        """Sends a list of Entities locations"""
        for p in placement:
            try:
                self.place(p.index, p.x, p.y, degrees(p.a))
            except Exception as e:
                print("placement exception:", e)

        lib.replacer_send_frame()

    def send(self):
        """Actually sends the frame"""
        lib.replacer_send_frame()

    def __del__(self):
        """Closes network connection."""
        lib.replacer_term()
