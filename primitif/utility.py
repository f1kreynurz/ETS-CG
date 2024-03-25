## optimated

import math

from primitif.size import Sizes

def convert_to_cartesian(xa, ya, width = Sizes.width, height = Sizes.height):
    axis = int(math.ceil(width//2))
    ordinat = int(math.ceil(height//2))

    return [int(axis+xa), int(ordinat-ya)]