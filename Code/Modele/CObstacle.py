import numpy as np

class CObstacle :
    """
    Classe des obstacles
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nom = "", coordonneesSommet = np.array([(0, 0)])):
        self.sNom = nom
        self.iSuperficie = 0
        self.tCoordonneesSommet = coordonneesSommet


    # -------------------Getters-------------------#
    def getNom(self):
        return self.sNom

    def getSuperficie(self):
        return self.iSuperficie

    def getCoordoneesSommet(self):
        return self.tCoordonneesSommet


    # ---------------------Setters---------------------#
    def setNom(self, nom):
        self.sNom = nom

    def setCoordonneesSommet(self, coordonneesSommets):
        self.tCoordonneesSommet = coordonneesSommets


    # -------------------Methodes-------------------#
    def OBSToString(self):
        print("\nNom : {}\n"
              "Coordonnees : {}\n"
              "Superficie : {}"
              .format(self.getNom(), self.getCoordoneesSommet(), self.getSuperficie()))
