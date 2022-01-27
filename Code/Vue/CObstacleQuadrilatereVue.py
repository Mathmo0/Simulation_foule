from tkinter import *
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere


class CObstacleQuadrilatereVue:
    def __init__(self, canvas, obstacle = CObstacleQuadrilatere()):
        self.__QVUcanvas = canvas
        self.__fQVUtopLeftx = obstacle.getCoordonneesSommet()[0][0]
        self.__fQVUtopLefty = obstacle.getCoordonneesSommet()[0][1]
        self.__fQVUbottomRightx = obstacle.getCoordonneesSommet()[3][0]
        self.__fQVUbottomRighty = obstacle.getCoordonneesSommet()[3][1]
        self.__QVUimage = canvas.create_rectangle(self.__fQVUtopLeftx, self.__fQVUtopLefty, self.__fQVUbottomRightx, self.__fQVUbottomRighty)


