import numpy as np

from Code.Modele.COperation import COperation
from Code.Modele.CFRepulsion import CFRepulsion
from Code.Modele.CFAcceleration import CFAcceleration
from Code.Modele.CFAttraction import CFAttraction
from Code.Modele.CForce import CForce,Phi

class CPersonne:

    def __init__(self,coordonne,vitesse = 1.34, pression = 0, rayon = 1, chpsVision = Phi,ForceRepulsion =CFRepulsion(), ForceObstacle = CFRepulsion() ,ForceAttraction = CFAttraction(),ForceAccelaration = CFAcceleration()):
        #TODO : je sais pas si c'ets possible mais rajouter les exception necessaire mis dans les setter
        self.vPERVitesse = np.array([0,0])
        self.fPERVitesse = vitesse
        self.fPERPression = pression
        self.lPERDirection = []
        self.lPERCoordonees = [coordonne] #cette litse contient 2 coordonnées , en indice 0 la coordonnès à l'instant t-Deltat et en indice 1 la coordonnées à l'instant t
        self.lPERlistPersonneProximite = []
        self.vPERForceRepulsionPersonne = ForceRepulsion
        self.vPERForceRepulsionObstacle = ForceObstacle
        self.vPERForceAttraction = ForceAttraction
        self.vPERForceAcceleration = ForceAccelaration
        self.fPERRayon = rayon
        self.fPERChampsDeVision = chpsVision

#------------------------Getter------------------------

    def getVitesse(self):
        return self.fPERVitesse

    def getPression(self):
        return self.fPERPression

    def getListDirection(self) :
        return self.lDirection

    def getListCoordonnees(self):
        return self.lPERCoordonees

    def getRayon(self):
        return self.fPERRayon

    def getChampsDeVision(self):
        return self.fPERChampsDeVision

#------------------------Setter------------------------

    def setVitesse(self, vitesse):
        #TODO : exception si vitesse négatif ??
        self.fPERVitesse = vitesse

    def setPression(self, pression):
        #TODO : exception si pression négative ??
        self.fPERPression = pression

    def setListDirection(self, direction):
        self.lPERDirection = direction

    def setListCoordonnees(self, coordonnees):
        #TODO : exeption si taille de la liste > 2

        self.lPERCoordonees = coordonnees

    def setRayon(self, rayon):
        #TODO : exception si rayon < 0
        self.fPERRayon = rayon

    def setChampsDeVision(self, chpsVision):
        #TODO : exception si champ de vision négatif
        self.fPERChampsDeVision = chpsVision

#------------------------Methodes------------------------

    def ajouterCoordonnees(self, coordonnees):

        if(len(self.lPERCoordonees) == 2) :
            self.lPERCoordonees.pop(0)
            self.lPERCoordonees.append(coordonnees)
        else :
            self.lPERCoordonees.append(coordonnees)

    def ajouterPersonne(self,Personne):
        self.lPERlistPersonneProximite.append(Personne)

    def ajouterDirection(self, direction):
        self.lPERDirection.append(direction)

    def marcher(self):
        self.canvas.delete(self.image)
        self.image = COperation.create_circle(self.x, self.y, self.rayon, self.canvas, self.color)

    def CalculerForceRepulsionPersonne(self):

        valeurTotaleForceRepulsion = np.array([0,0])

        for personne in self.lPERlistPersonneProximite :

            self.vPERForceRepulsionPersonne.FREForceRepulsionPersonne()


    def CalculerForceRepulsionObstacle(self):
        return 0

    def CalculerForceAcceleration(self):
        """
        Permet de calculer la force d'acceleration

        @return: rien
        """
        self.vPERForceAcceleration.FACForceDacceleration(self.vPERVitesse,1.34,self.lPERDirection[0],self.lPERCoordonees[1])

    def CalculerNouvellePosition(self):
        """
        Permet calculer la nouvelle position du pieton une fois toute les forces calcule et l'ajoute a la liste de coordonnees lPERCoordonees

        @return: rien
        """
        return 0
        #nouvellecoord =
        #self.lPERCoordonees.append(nouvellecoord)

