from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere


class CObstacleQuadrilatereVue:
    #----------------- Constructeur-----------------:
    def __init__(self, canvas, obstacle = CObstacleQuadrilatere()):
        self.__QVUcanvas = canvas
        self.__fQVUtopLeftx = obstacle.OBSgetCoordonneesSommet()[0][0]
        self.__fQVUtopLefty = obstacle.OBSgetCoordonneesSommet()[0][1]
        self.__fQVUbottomRightx = obstacle.OBSgetCoordonneesSommet()[3][0]
        self.__fQVUbottomRighty = obstacle.OBSgetCoordonneesSommet()[3][1]
        self.__QVUimage = canvas.create_rectangle(self.__fQVUtopLeftx, self.__fQVUtopLefty, self.__fQVUbottomRightx, self.__fQVUbottomRighty)


