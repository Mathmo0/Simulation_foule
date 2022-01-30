import Code.Modele.CEnvironnement as CEnvironnement
import Code.Modele.CPersonne as CPersonne
import Code.Modele.CObstacleQuadrilatere as CObstacleQuadrilatere
import tkinter

class CEnvironnementController:

    @staticmethod
    def ENCControleInCanvas(coordX, coordY, hauteur, largeur):
        """

        @param coordX:
        @param coordY:
        @param hauteur:
        @param largeur:
        @return:
        """

        if coordX > largeur:
            coordX = largeur
        elif coordX < 0:
            coordX = 0

        if coordY > hauteur:
            coordY = hauteur
        elif coordY < 0:
            coordY = 0

        return coordX, coordY

    @staticmethod
    def ENCControlePersonnesInCanvas(coordX, coordY, hauteur, largeur):
        """

        @param coordX:
        @param coordY:
        @param hauteur:
        @param largeur:
        @return:
        """
        CEnvironnementController.ENCControleInCanvas(coordX, coordY, hauteur, largeur)

    @staticmethod
    def ENCControleSortieInCanvas(coordX, coordY, hauteur, largeur):
        """

        @param coordX:
        @param coordY:
        @param hauteur:
        @param largeur:
        @return:
        """
        CEnvironnementController.ENCControleInCanvas(coordX, coordY, hauteur, largeur)

    @staticmethod
    def ENCControleObstaclesInCanvas(coordX, coordY, hauteur, largeur):
        """

        @param coordX:
        @param coordY:
        @param hauteur:
        @param largeur:
        @return:

        """
        if coordX > largeur:
            return 0

        if coordY < 0:
            return 0

        return 1
