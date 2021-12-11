from typing import Tuple

def loop(x_max: int, y_max: int) -> Tuple[int, int]:
    """
    Generate the indices of all points in the [0, x_max] x [0, y_max] plane.
    :param x_max: the exclusive x-bound.
    :param y_max: the exclusive y-bound.
    """
    # First time working with yield!
    for y in range(y_max):
        for x in range(x_max):
            yield x, y