from tkinter import *
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere


class CObstacleQuadrilatereVue:
    def __init__(self, canvas, obstacle = CObstacleQuadrilatere()):
        self.__canvas = canvas
        self.__topLeftx = obstacle.getCoordonneesSommet()[0][0]
        self.__topLefty = obstacle.getCoordonneesSommet()[0][1]
        self.__bottomRightx = obstacle.getCoordonneesSommet()[3][0]
        self.__bottomRighty = obstacle.getCoordonneesSommet()[3][1]
        self.__image = canvas.create_rectangle(self.__topLeftx, self.__topLefty, self.__bottomRightx, self.__bottomRighty)


