import Code.Modele.CEnvironnement as CEnvironnement
import Code.Modele.CPersonne as CPersonne
import Code.Modele.CObstacleQuadrilatere as CObstacleQuadrilatere
import tkinter

class CEnvironnementController:

    @staticmethod
    def ControleInCanvas(coordX, coordY, hauteur, largeur):
        if coordX > largeur:
            coordX = largeur
        elif coordX < 0:
            coordX = 0

        if coordY > hauteur:
            coordX = hauteur
        elif coordY < 0:
            coordX = 0

    @staticmethod
    def ControlePersonnesInCanvas(coordX, coordY, hauteur, largeur):
        CEnvironnementController.ControleInCanvas(coordX, coordY, hauteur, largeur)

    @staticmethod
    def ControleSortieInCanvas(coordX, coordY, hauteur, largeur):
        CEnvironnementController.ControleInCanvas(coordX, coordY, hauteur, largeur)

    @staticmethod
    def ControleObstaclesInCanvas(coordX, coordY, hauteur, largeur):
        if coordX > largeur:
            return 0

        if coordY < 0:
            return 0

        return 1
