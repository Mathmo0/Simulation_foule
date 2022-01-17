from tkinter import *
import Code.Modele.CEnvironnement as CEnvironnement
from Code.Modele.COperation import COperation
import numpy as np

class CSortiesVue:
    def __init__(self, canvas, listeCoord:np.array, rayon = 10):
        self.canvas = canvas
        self.rayon = rayon
        if len(listeCoord) == 2 :
            self.__coordx = listeCoord[0]
            self.__coordy = listeCoord[1]
            self.__image = COperation.create_circle(self.__coordx, self.__coordy, self.rayon, self.canvas, "green")
