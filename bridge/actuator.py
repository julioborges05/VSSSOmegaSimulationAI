from ctypes import c_int32, c_double, c_char_p, c_uint16, c_bool

from bridge.bridge import NUM_BOTS, lib


class Actuator:
    """
    Actuator client class,
    Use one instance at a time to minimize network errors.
    """

    def __init__(self, my_robots_are_yellow, addr="224.0.0.1", port=10002):
        """
        Initialize client on addr and port

        default address: "224.0.0.1",
        default port: 10002
        requires bool team_color to indicate later commands.
        """

        # we need to convert the string type
        c_string = addr.encode('utf-8')
        lib.actuator_init.argtypes = [c_char_p, c_uint16, c_bool]

        lib.actuator_init(c_string, c_uint16(port), c_bool(my_robots_are_yellow))

    def send(self, index, left, right):
        """
        sends motor speeds for one robot indicated by
        index on team initialized.
        """
        lib.actuator_send_command(c_int32(index), c_double(left), c_double(right))

    def send_all(self, speeds):
        """sends a list of speed commands based on the passed list of dicts"""
        for s in speeds:
            try:
                self.send(s["index"], s["left"], s["right"])
            except Exception as e:
                print("speed exception:", e)

    def stop(self):
        """Sets all speeds to zero"""
        for i in range(NUM_BOTS):
            self.send(i, 0, 0)

    def __del__(self):
        """Closes network connection."""
        lib.actuator_term()
