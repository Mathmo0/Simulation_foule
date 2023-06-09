from Code.Modele.CObstacle import CObstacle

import numpy as np

class CObstacleQuadrilatere(CObstacle):
    """
    Classe des obstacles de type quadrilatere
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nom = "", hauteur = 0, largeur = 0, coordonneesSommets = np.array([(0, 0)])):
        super().__init__(nom, coordonneesSommets)
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
        print("\nNom : {}\n"
              "Coordonnees : {}\n"
              "Superficie : {}"
              "Hauteur : {}\n"
              "Largeur : {}\n"
              .format(self.getNom(), self.getCoordoneesSommet(), self.getSuperficie(), self.getHauteur(), self.getLargeur()))


list_sorties = np.array([(3, 4), (2, 4)])
carreONE = CObstacleQuadrilatere("carreone", 12, 12, list_sorties)
carreONE.OBSToString()
