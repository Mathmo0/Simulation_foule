import numpy as np
from Modele.CPersonne import CPersonne
from Modele.CObstacleQuadrilatere import CObstacleQuadrilatere

class CEnvironnement:
    """
    Classe de l'environnement
    """

    # -------------------Constructeur-------------------#
    def __init__(self, nom="", hauteur=1, largeur=1, sorties= np.array([(0, 0)]), listePersonnes = np.array([CPersonne()]), listeObstacles = np.array([CObstacleQuadrilatere()])):
        self.sNom = nom

        self.iHauteur = hauteur
        self.iLargeur = largeur

        self.fSuperficie = hauteur * largeur

        self.lListePersonnes = listePersonnes
        self.lListeObstacles = listeObstacles

        self.iNbPersonnes = len(listePersonnes)
        self.iNbObstacles = len(listePersonnes)

        self.tSorties = sorties

    """def __init__(self, fichier):
        self.sNom, self.iHauteur, self.iLargeur, self.tSorties, self.lListePersonnes, self.lListeObstacles = fichier.LireFichierEnvironnement()

        self.fSuperficie = self.hauteur * self.largeur

        self.iNbPersonnes = len(self.listePersonnes)
        self.iNbObstacles = len(self.listePersonnes)"""



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

    def getListePersonnes(self):
        return self.lListePersonnes

    def getListeObstacles(self):
        return self.lListeObstacles


    # ---------------------Setters---------------------#
    def setNom(self, nom):
        self.sNom = nom

    def setHauteur(self, hauteur):
        self.iHauteur = hauteur
        self.superficie = self.iHauteur * self.iLargeur


    def setLargeur(self, largeur):
        self.iLargeur = largeur
        self.superficie = self.iHauteur * self.iLargeur

    def setSorties(self, list_sorties):
        self.tSorties = list_sorties

    def setListePersonnes(self, listePersonnes):
        self.lListePersonnes = listePersonnes
        self.iNbPersonnes = len(self.lListePersonnes)

    def setListeObstacles(self, listeObstacles):
        self.lListeObstacles = listeObstacles
        self.iNbObstacles = len(self.lListeObstacles)


    # -------------------Methodes-------------------#
    def ENVToString(self):
        print(
            "\nSalle : {}\n" 
            "Superficie : {} m2\n" 
            "Hauteur : {} m\n" 
            "Largeur : {} m\n" 
            "Nombre de personnes : {}\n" 
            "Nombre d'obstacles : {}\n" 
            "Liste de sorties : {}\n"
                .format(self.getNom(), self.getSuperficie(), self.getHauteur(), self.getLargeur(), self.getNbPersonnes(), self.getNbObstacles(), self.getSorties()))



print("Lancement de la classe")

"""list_sorties = np.array([(3, 4), (2, 4)])

e1 = CEnvironnement("Bureau", 34, 20, 3, 1, list_sorties)
#e1 = CEnvironnement()

e1.ENVToString()
e1.tSorties[0][1] = 2
e1.ENVToString()"""

