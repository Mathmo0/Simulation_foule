from tkinter import *
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere


class CObstacleQuadrilatereVue:
    def __init__(self, canvas, obstacle = CObstacleQuadrilatere()):
        self.canvas = canvas
        self.topLeftx = obstacle.getCoordonneesSommet()[0]
        self.topLefty = obstacle.getCoordonneesSommet()[0]
        self.bottomRightx = self.topLeftx + obstacle.getLargeur()
        self.bottomRighty = self.topLefty + obstacle.getHauteur()
        self.image = canvas.create_rectangle(self.topLeftx, self.topLefty, self.bottomRightx, self.bottomRighty)


