"""
This module was created to interact with the FIRAClient 
located on https://github.com/yapiraUFPR/FIRAClient

This interaction is made with the file libfira.cpp,
witch generates the shared object libfira.so used here.

The classes located here use the lib subspace to store
their respective client data.
"""

__author__ = "Artur Coelho - github.com/arturtcoelho"

import ctypes
from ctypes import (c_double)
from math import pi

# Loads the compiled shared library based on libfira.cpp
# See README.md to compile and usage

# The lib object will contain the C++ local clients
# witch save their respective data
try:
    lib = ctypes.cdll.LoadLibrary('./libfira.so')
except Exception as e:
    try:
        lib = ctypes.cdll.LoadLibrary('./FIRAClient/libfira.so')
    except Exception as e:
        try:
            lib = ctypes.cdll.LoadLibrary('../FIRAClient/libfira.so')
        except Exception as e:
            print("Could not open lib in any directory")
            exit()

# set the return types for the lib functions (to double)
lib.vision_get_ball_x.restype = c_double
lib.vision_get_ball_y.restype = c_double
lib.vision_get_ball_vx.restype = c_double
lib.vision_get_ball_vy.restype = c_double
lib.vision_robot_x.restype = c_double
lib.vision_robot_y.restype = c_double
lib.vision_robot_angle.restype = c_double
lib.vision_robot_vx.restype = c_double
lib.vision_robot_vy.restype = c_double
lib.vision_robot_vangle.restype = c_double

NUM_BOTS = 3


# you can remove or modify these functions as you wish,
# these are used here mainly to run the example main 
def convert_width(w) -> float:
    """
    Converts width from the simulator data to centimetres
    with origin point on bottom left corner of field
    """
    try:
        return w * 100
    except TypeError:
        return 0


def inverse_width(w) -> float:
    try:
        return (w / 100)
    except TypeError:
        return 0


def convert_length(d) -> float:
    """
    Converts width from the simulator data to centimetres
    with origin point on bottom left corner of field
    """
    try:
        return d * 100
    except TypeError:
        return 0


def inverse_length(d) -> float:
    try:
        return (d / 100)
    except TypeError:
        return 0


def convert_angle(a) -> float:
    """
    Converts the angle from full radians to 
    -Pi to Pi radians range
    """
    try:
        if a > 0:
            if a > pi:
                return a - 2 * pi
        else:
            if a < -pi:
                return a + 2 * pi
        return a

    except TypeError:
        return 0
