import math
import random

from pygame import Vector2


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy


def limit(n, min_n, max_n):
    if min_n <= n <= max_n:
        return n
    elif min_n > n:
        return min_n
    else:
        return max_n

def linear(x, in_start=0, in_end=1, out_start=0, out_end=1):
    """
    Linearly map (scale) a number from one range to another range.
    Can also be used for linear interpolation. And you can invert
    the ranges by making start greater than end. Values outside
    both ranges are also possible.
    """
    return (x - in_start) / (in_end - in_start) * (out_end - out_start) + out_start

def linear_with_ranges(x, in_range=(0, 1), out_range=(0, 1)):
    """
    Linearly map (scale) a number from one range to another range.
    Can also be used for linear interpolation. And you can invert
    the ranges by making start greater than end. Values outside
    both ranges are also possible.
    """
    return linear(x, in_range[0], in_range[1], out_range[0], out_range[1])

def random_vector():
    angle = random.uniform(0, 360)
    return Vector2(1, 0).rotate(angle)

