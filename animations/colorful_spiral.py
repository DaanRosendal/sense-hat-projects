from sense_hat import SenseHat
import time
import numpy as np
import time
import shapes
from random import randint
import sys

sense = SenseHat()

# colors
w = [150, 150, 150]
b = [0, 0, 255]
e = [0, 0, 0]


# create empty screen
image = np.array([
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
])

# colorful squares
for x in range(50):
    shapes.square(image, [0,0], [7,0], [7,7],[0,7],[randint(0,255),randint(0,255),randint(0,255)],.01)
    shapes.square(image, [1,1], [6,1], [6,6],[1,6],[randint(0,255),randint(0,255),randint(0,255)],.01)
    shapes.square(image, [2,2], [5,2], [5,5],[2,5],[randint(0,255),randint(0,255),randint(0,255)],.01)
    shapes.square(image, [3,3], [4,3], [4,4],[3,4],[randint(0,255),randint(0,255),randint(0,255)],.01)
