import numpy as np

class CEnvironnement:
    """
    Classe de l'environnement
    """

    # -------------------Constructeur-------------------#

    def __init__(self, nom="", hauteur=1, largeur=1, nbPersonnes=0, nbObstacles=0, sorties= np.array([(0, 0)])):
        self.sNom = nom
        self.iHauteur = hauteur
        self.iLargeur = largeur
        self.fSuperficie = hauteur * largeur
        self.iNbPersonnes = nbPersonnes
        self.iNbObstacles = nbObstacles
        self.tSorties = sorties

    # -------------------Getters-------------------#

    def getNom(self):
        return self.sNom

    def getSuperficie(self):
        return self.fSuperficie

    def getNbPersonnes(self):
        return self.iNbPersonnes

    def getNbObstacles(self):
        return self.iNbObstacles

    def getSorties(self):
        return self.tSorties

    def getHauteur(self):
        return self.iHauteur

    def getLargeur(self):
        return self.iLargeur
    # ---------------------Setters---------------------#


    def setNom(self, nom):
        self.sNom = nom


    def setHauteur(self, hauteur):
        self.iHauteur = hauteur
        self.superficie = self.iHauteur * self.iLargeur


    def setLargeur(self, largeur):
        self.iLargeur = largeur
        self.superficie = self.iHauteur * self.iLargeur

    def setNbPersonnes(self, nbPersonnes):
        self.iNbPersonnes = nbPersonnes


    def setNbObstacles(self, nbObstacles):
        self.iNbObstacles = nbObstacles


    def setSorties(self, list_sorties):
        self.tSorties = list_sorties


    # -------------------Methodes-------------------#

    def ENVToString(self):
        print(
            "Salle : {}\n" 
            "Superficie : {} m2\n" 
            "Hauteur : {} m\n" 
            "Largeur : {} m\n" 
            "Nombre de personnes : {}\n" 
            "Nombre d'obstacles : {}\n" 
            "Liste de sorties : {}"
                .format(self.getNom(), self.getSuperficie(), self.getHauteur(), self.getLargeur(), self.getNbPersonnes(), self.getNbObstacles(), self.getSorties()))


print("Lancement de la classe")

list_sorties = np.array([(3, 4), (2, 4)])

e1 = CEnvironnement("Bureau", 34, 20, 3, 1, list_sorties)
#e1 = CEnvironnement()
#print("Salle : {}\nsuperficie : {} m2\nnombre de personnes : {}\nnombre d'obstacles : {}\nliste de sorties : {}".format(
#    e1.sNom, e1.fSuperficie, e1.iNbPersonnes, e1.iNbObstacles, e1.tSorties))
e1.ENVToString()
e1.tSorties[0][1] = 2
e1.ENVToString()

#print("Salle : {}\nsuperficie : {} m2\nnombre de personnes : {}\nnombre d'obstacles : {}\nliste de sorties : {}".format(
#    e1.sNom, e1.fSuperficie, e1.iNbPersonnes, e1.iNbObstacles, e1.tSorties))
