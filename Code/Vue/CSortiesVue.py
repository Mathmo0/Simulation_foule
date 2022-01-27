from tkinter import *
import Code.Modele.CEnvironnement as CEnvironnement
from Code.Modele.COperation import COperation
import numpy as np

class CSortiesVue:
    def __init__(self, canvas, listeCoord:np.array, rayon = 10):
        self.__SORcanvas = canvas
        self.__SORrayon = rayon
        if len(listeCoord) == 2 :
            self.__SORcoordx = listeCoord[0]
            self.__SORcoordy = listeCoord[1]
            self.__SORimage = COperation.create_circle(self.__SORcoordx, self.__SORcoordy, self.__SORrayon, self.__SORcanvas, "green")
