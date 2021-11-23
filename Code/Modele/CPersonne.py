from COperation import *

class CPersonne:

    def __init__(self, poids, vitesse, pression, rayon, chpsVision):
        self.iPERPoids = poids
        self.fPERVitesse = vitesse
        self.fPERPression = pression
        self.lPERDirection = []
        self.lPERCoordonees = []
        self.fPERRayon = rayon
        self.fPERChampsDeVision = chpsVision

#------------------------Getter------------------------

    def getPoids(self):
        return self.iPERPoids

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

    def setPoids(self, poids):
        self.iPERPoids = poids

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

    def ajouterDirection(self, direction):
        self.lPERDirection.append(direction)

    def marcher(self):
        self.canvas.delete(self.image)
        self.image = create_circle(self.x, self.y, self.rayon, self.canvas, self.color)