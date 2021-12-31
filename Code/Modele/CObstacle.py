import numpy as np

class CObstacle :
    """
    Classe des obstacles
    """

    # -------------------Constructeur-------------------#
    def __init__(self, coordonneesSommet = np.array([0,0])):
        self.iSuperficie = 0
        self.tCoordonneesSommet = coordonneesSommet


    # -------------------Getters-------------------#
    def getSuperficie(self):
        return self.iSuperficie

    def getCoordonneesSommet(self):
        return self.tCoordonneesSommet


    # ---------------------Setters---------------------#
    def setCoordonneesSommet(self, coordonneesSommets):
        self.tCoordonneesSommet = coordonneesSommets


    # -------------------Methodes-------------------#
    def OBSToString(self):
        print("Coordonnees : {}\n"
              "Superficie : {}\n"
              .format(self.getCoordoneesSommet(), self.getSuperficie()))
