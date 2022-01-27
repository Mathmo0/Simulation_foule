from Code.Modele.CObstacle import CObstacle

import numpy as np

class CObstacleQuadrilatere(CObstacle):
    """
    Classe des obstacles de type quadrilatere
    """

    # -------------------Constructeur-------------------#
    def __init__(self, hauteur = 0, largeur = 0, coordonneesSommets = np.array([0, 0])):
        super().__init__(coordonneesSommets)
        self.iSuperficie = hauteur * largeur
        self.iHauteur = hauteur
        self.iLargeur = largeur


    # -------------------Getters-------------------#
    def getHauteur(self):
        return self.iHauteur

    def getLargeur(self):
        return self.iLargeur


    # ---------------------Setters---------------------#
    def setHauteur(self, hauteur):
        self.iHauteur = hauteur
        self.iSuperficie = self.iHauteur * self.iLargeur

    def setLargeur(self, largeur):
        self.iLargeur = largeur
        self.iSuperficie = self.iHauteur * self.iLargeur


    # -------------------Methodes-------------------#
    def OBSToString(self):
        print("\nCoordonnees : {}\n"
              "Superficie : {}\n"
              "Hauteur : {}\n"
              "Largeur : {}\n"
              .format(self.getCoordonneesSommet(), self.getSuperficie(), self.getHauteur(), self.getLargeur()))

    def calculerCoordonnees(self):
        coinTopRight = np.array([self.tCoordonneesSommet[0][0] + self.iLargeur, self.tCoordonneesSommet[0][1]])
        coinBottomLeft = np.array([self.tCoordonneesSommet[0][0], self.tCoordonneesSommet[0][1] - self.iHauteur])
        coinBottomRight = np.array([self.tCoordonneesSommet[0][0] + self.iLargeur, self.tCoordonneesSommet[0][1] - self.iHauteur])
        self.tCoordonneesSommet.append(coinTopRight)
        self.tCoordonneesSommet.append(coinBottomLeft)
        self.tCoordonneesSommet.append(coinBottomRight)


"""list_sorties = np.array([(3, 4), (2, 4)])
carreONE = CObstacleQuadrilatere(12, 12, list_sorties)
carreONE.OBSToString()"""
