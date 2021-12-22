import numpy as np

from Code.Modele.COperation import COperation
from Code.Modele.CFRepulsion import CFRepulsion
from Code.Modele.CFAcceleration import CFAcceleration
from Code.Modele.CFAttraction import CFAttraction
from Code.Modele.CForce import CForce,Phi
from Code.Modele.CObstacle import CObstacle

class CPersonne:

    def __init__(self,coordonnees = np.array([0,0]), direction = [], vitesse = 1.34, pression = 0, rayon = 1, chpsVision = Phi,ForceRepulsion =CFRepulsion(), ForceObstacle = CFRepulsion() ,ForceAttraction = CFAttraction(),ForceAccelaration = CFAcceleration()):
        #TODO : je sais pas si c'ets possible mais rajouter les exception necessaire mis dans les setter

        self.vPERVitesse = np.array([0,0])
        self.fPERVitesse = vitesse
        self.fPERPression = pression
        self.lPERDirection = direction
        self.lPERCoordonees = [coordonnees] #cette litse contient 2 coordonnées , en indice 0 la coordonnès à l'instant t-Deltat et en indice 1 la coordonnées à l'instant t
        self.lPERlistPersonneProximite = [CPersonne]
        self.lPERlistObstacleProximite = [CObstacle]
        self.vPERForceRepulsionPersonne = ForceRepulsion
        self.vPERForceRepulsionObstacle = ForceObstacle
        self.vPERForceAttraction = ForceAttraction
        self.vPERForceAcceleration = ForceAccelaration
        self.fPERRayon = rayon
        self.fPERChampsDeVision = chpsVision

#------------------------Getter------------------------

    def getVitesse(self):
        """
        getter pour l'attribut fPERVitesse

        @return: fPERVitesse
        """
        return self.fPERVitesse

    def getPression(self):
        """
        getter pour l'attribut fPERPression
        @return: fPERPression
        """
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

    def RecupererDirectionActuelle(self):
        return self.lPERDirection[0]

    def RecupererDerniereCoordonne(self):
        """
        Permet de recuperer la coordonnee actuelle du pieton

        @return: coordonnee actuelle du pieton
        """
        if (len(self.lPERCoordonees) == 2):
            return self.lPERCoordonees[1]
        else :
            return self.lPERCoordonees[0]

    def ajouterCoordonnees(self, coordonnees):
        """
        Permet d'ajouter une coordonnee dans la liste lPERCoordonees

        @param coordonnees: coordonnee du pieton qu'on veut ajouter
        @return: rien
        """

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

    def CalculerForceRepulsion(self):
        """
        Permet de calculer la force de repulsion totale excercé par toute les personne qui sont dans lPERlistPersonneProximite

        @return: rien
        """

        #recupere la valuer actuelle de la force la force de repulsion
        valeurTotaleForceRepulsion = self.vPERForceRepulsionPersonne.gettertForceRepulsion()

        #calcul de nouvelle force de repulsion
        for personne in self.lPERlistPersonneProximite :
            valeurTotaleForceRepulsion += self.vPERForceRepulsionPersonne.FREForceRepulsionPersonne(self.lPERDirection[0],self.RecupererDerniereCoordonne(),self.lPERCoordonees[0],personne.RecupererDerniereCoordonne(),personne.RecupererDirectionActuelle(),personne.getVitesse())

        self.vPERForceRepulsionPersonne.settertForceRepulsion(valeurTotaleForceRepulsion)


    def CalculerForceRepulsionObstacle(self):
        """
        Permet de calculer la force de repulsion applique sur le pieton par tous les obstacles qui sont dans la liste lPERlistObstacleProximite

        @return: rien
        """
        valeurTotaleForceRepulsionObstacle = self.vPERForceRepulsionObstacle.gettertForceRepulsion()

        for obstacle in self.lPERlistObstacleProximite :
            valeurTotaleForceRepulsionObstacle+= self.vPERForceRepulsionObstacle.FREForceDeRepulsionObstacle(self.RecupererDerniereCoordonne(),self.lPERCoordonees[0],o)

        self.vPERForceRepulsionObstacle.settertForceRepulsion(valeurTotaleForceRepulsionObstacle)

    def CalculerForceAcceleration(self):
        """
        Permet de calculer la force d'acceleration

        @return: rien
        """
        self.vPERForceAcceleration.FACForceDacceleration(self.vPERVitesse,1.34,self.lPERDirection[0],self.RecupererDerniereCoordonne())

    def CalculerNouvellePosition(self):
        """
        Permet calculer la nouvelle position du pieton une fois toute les forces calcule et l'ajoute a la liste de coordonnees lPERCoordonees

        @return: rien
        """

        Force = self.vPERForceAcceleration.FACgetForceAcceleration() +self.vPERForceRepulsionPersonne.gettertForceRepulsion()+self.vPERForceRepulsionObstacle.gettertForceRepulsion() #+self.vPERForceAttraction.get() # pas encore fait
        nouvellecoord = self.RecupererDerniereCoordonne()+Force
        self.ajouterCoordonnees(nouvellecoord)

    def sorti(self):
        """
        Permet de savoir si la personne est sortie ou non

        @return: booleen
        """
        coordonneeSortie = self.lPERDirection[0]
        coordonneePieton = self.RecupererDerniereCoordonne()

        #On verifie si le pieton est aux alentours de la sortie.
        IsGone = COperation.DetectionCercle(coordonneeSortie[0], coordonneeSortie[1], coordonneePieton[0], coordonneePieton[1], 0.5)

        #Si oui, on retire les coordonnees de la sortie de sa memoire.
        if IsGone:
            self.lPERDirection.pop(0)

        if len(self.lPERDirection) == 0:
            return True
        else:
            return False


