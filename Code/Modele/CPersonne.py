import numpy as np

from Code.Modele import COperation,CFRepulsion,CFAcceleration
from Code.Modele.CForce import Phi

class CPersonne:

    def __init__(self, vitesse = 0, pression = 0, rayon = 1, chpsVision = Phi):
        self.fPERVitesse = vitesse
        self.fPERPression = pression
        self.lPERDirection = np.array()
        self.lPERCoordonees = np.array()
        self.lPERlistPersonneProximite = []
        self.vPERForceRepulsion = np.array([0,0])
        self.vPERForceAttraction = np.array([0,0])
        self.vPERForceAcceleration = CFAcceleration()
        self.fPERRayon = rayon
        self.fPERChampsDeVision = chpsVision

#------------------------Getter------------------------

    def getVitesse(self):
        return self.fPERVitesse

    def getPression(self):
        return self.fPERPression

    def getListDirection(self):
        return self.lDirection

    def getListCoordonnees(self):
        return self.lPERCoordonees

    def getRayon(self):
        return self.fPERRayon

    def getChampsDeVision(self):
        return self.fPERChampsDeVision

#------------------------Setter------------------------

    def setVitesse(self, vitesse):
        self.fPERVitesse = vitesse

    def setPression(self, pression):
        self.fPERPression = pression

    def setListDirection(self, direction):
        self.lPERDirection = direction

    def setListCoordonnees(self, coordonnees):
        self.lPERCoordonees = coordonnees

    def setRayon(self, rayon):
        self.fPERRayon = rayon

    def setChampsDeVision(self, chpsVision):
        self.fPERChampsDeVision = chpsVision

#------------------------Methodes------------------------

    def ajouterCoordonnees(self, coordonnees):
        self.lPERCoordonees.append(coordonnees)

    def ajouterPersonne(self,Personne):
        self.lPERlistPersonneProximite.append(Personne)

    def ajouterDirection(self, direction):
        self.lPERDirection.append(direction)

    def marcher(self):
        self.canvas.delete(self.image)
        self.image = COperation.create_circle(self.x, self.y, self.rayon, self.canvas, self.color)

    def CalculerForceRepulsion(self):
        return 0

    def CalculerForceAcceleration(self):
        return 0

    def CalculerNouvellePosition(self):
        return 0
