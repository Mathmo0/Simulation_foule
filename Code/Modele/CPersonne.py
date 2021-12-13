import numpy as np

from Modele import COperation,CFRepulsion,CFAcceleration
from Modele.CForce import Phi

class CPersonne:

    def __init__(self, vitesse = 0, pression = 0, rayon = 1, chpsVision = Phi):
        self.fPERVitesse = vitesse
        self.fPERPression = pression
        self.lPERDirection = np.array([(0,0)])
        self.lPERCoordonees = np.array([(0,0)])
        self.lPERlistPersonneProximite = []
        self.vPERForceRepulsion = np.array([0,0])
        self.vPERForceAttraction = np.array([0,0])
        """self.vPERForceAcceleration = CFAcceleration()
        self.fPERRayon = rayon"""
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

        @return: rien
        """
        #recupere la valuer actuelle de la force la force de repulsion
        valeurTotaleForceRepulsion = self.vPERForceRepulsionPersonne.gettertForceRepulsion()

        #calcul de nouvelle force de repulsion
        for personne in self.lPERlistPersonneProximite :

            valeurTotaleForceRepulsion += personne.FREForceRepulsionPersonne()

        self.vPERForceRepulsionPersonne.settertForceRepulsion(valeurTotaleForceRepulsion)


    def CalculerForceRepulsionObstacle(self):
        """
        Permet de calculer la force de repulsion applique sur le pieton par tous les obstacles qui sont dans la liste lPERlistObstacleProximite

        @return: rien
        """
        valeurTotaleForceRepulsionObstacle = self.vPERForceRepulsionObstacle.gettertForceRepulsion()

        for obstacle in self.lPERlistObstacleProximite :
            valeurTotaleForceRepulsionObstacle+= CFRepulsion.FREForceDeRepulsionObstacle(self.RecupererDerniereCoordonne(),self.lPERCoordonees[0],)

    def CalculerForceAcceleration(self):
        return 0

    def CalculerNouvellePosition(self):
        return 0
