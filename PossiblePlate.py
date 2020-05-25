# PossiblePlate.py

import cv2
import numpy as np


class PossiblePlate:

    def __init__(self):# By using the self keyword, one can easily access all 
    # the instances defined within a class, including its methods and attributes.
    #  __init__ is one of the reserved methods in Python. In object oriented programming,
    #  it is known as a constructor.
        self.imgPlate = None
        self.imgGrayscale = None
        self.imgThresh = None

        self.rrLocationOfPlateInScene = None

        self.strChars = ""




