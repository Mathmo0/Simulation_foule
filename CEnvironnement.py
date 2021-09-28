class CEnvironnement:
    """
    Classe de l'environnement
    """
    def __init__(self, nom, superficie, nbPersonnes, nbObstacles, sorties):
        self.sNom = nom
        self.fSuperficie = superficie
        self.iNbPersonnes = nbPersonnes
        self.iNbObstacles = nbObstacles
        self.tSorties = sorties

#-------------------Getters-------------------#

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

#---------------------Setters---------------------#

    def setNom(self, nom):
        self.sNom = nom

    def setSuperficie(self, superficie):
        self.fSuperficie = superficie

    def setNbPersonnes(self, nbPersonnes):
        self.iNbPersonnes = nbPersonnes

    def setNbObstacles(self, nbObstacles):
        self.iNbObstacles = nbObstacles

    def setSorties(self, list_sorties):
        self.tSorties = list_sorties

print("Lancement de la classe")

list_sorties = [(3, 4), (2, 4)]

e1 = CEnvironnement("Bureau", 34, 2, 3, list_sorties)
print("Salle : {}\nsuperficie : {} m2\nnombre de personnes : {}\nnombre d'obstacles : {}\nliste de sorties : {}".format(e1.sNom, e1.fSuperficie, e1.iNbPersonnes, e1.iNbObstacles, e1.tSorties))
e1.tSorties[0][1] = 2
print("Salle : {}\nsuperficie : {} m2\nnombre de personnes : {}\nnombre d'obstacles : {}\nliste de sorties : {}".format(e1.sNom, e1.fSuperficie, e1.iNbPersonnes, e1.iNbObstacles, e1.tSorties))
