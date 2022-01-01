from typing import List

import numpy as np

from Code.Modele.COperation import COperation
from Code.Modele.CFRepulsion import CFRepulsion
from Code.Modele.CFAcceleration import CFAcceleration
from Code.Modele.CFAttraction import CFAttraction
from Code.Modele.CForce import CForce,Phi
from Code.Modele.CObstacle import CObstacle

class CPersonne:

    def __init__(self,recursif = False,coordonnees = np.array([0,0]),vitesse = 1.34, pression = 0, rayon = 1, chpsVision = Phi,ForceRepulsion =CFRepulsion(), ForceObstacle = CFRepulsion() ,ForceAttraction = CFAttraction(),ForceAccelaration = CFAcceleration()):
        #TODO : je sais pas si c'ets possible mais rajouter les exception necessaire mis dans les setter

        self.__vPERVitesse = np.array([0, 0])
        self.__fPERVitesse = vitesse
        self.__fPERPression = pression
        self.__lPERDirection = []
        self.__lPERCoordonees = [coordonnees] #cette litse contient 2 coordonnées , en indice 0 la coordonnès à l'instant t-Deltat et en indice 1 la coordonnées à l'instant t
        if recursif == False :
            self.__lPERlistPersonneProximite = [CPersonne(True)]
        else :
            self.__lPERlistPersonneProximite = []

        self.__lPERlistObstacleProximite: List[CObstacle] = []
        self.__vPERForceRepulsionPersonne = ForceRepulsion
        self.__vPERForceRepulsionObstacle = ForceObstacle
        self.__vPERForceAttraction = ForceAttraction
        self.__vPERForceAcceleration = ForceAccelaration
        self.__fPERRayon = rayon
        self.__fPERChampsDeVision = chpsVision

#------------------------Getter------------------------

    def getVitesse(self):
        """
        getter pour l'attribut __fPERVitesse

        @return: __fPERVitesse
        """
        return self.__fPERVitesse

    def getVecteurVitesse(self):
        """
        getter pour l'attribut __vPERVitesse
        @return:
        """
        return self.__vPERVitesse

    def getPression(self):
        """
        getter pour l'attribut __fPERPression
        @return: __fPERPression
        """
        return self.__fPERPression

    def getListDirection(self) :
        """
        getter pour l'attribut .__lDirection
        @return: __lDirection
        """
        return self.__lDirection

    def getListCoordonnees(self):
        """
        getter pour l'attribut __lPERCoordonees
        @return: __lPERCoordonees
        """
        return self.__lPERCoordonees

    def getListPersonneProx(self):
        """
        getter pour l'attribut __lPERlistPersonneProximite

        @return: __lPERlistPersonneProximite
        """
        return self.__lPERlistPersonneProximite

    def getlistObstacle(self):
        """
        getter pour l'attribut __lPERlistObstacleProximite

        @return: __lPERlistObstacleProximite
        """
        return self.__lPERlistObstacleProximite

    def getForceRepulsionPersonne(self):
        """
        getter pour l'attribut __vPERForceRepulsionPersonne
        @return: __vPERForceRepulsionPersonne
        """
        return self.__vPERForceRepulsionPersonne

    def getForceRepulsionObstacle(self):
        """
        getter pour l'attribut __vPERForceRepulsionObstacle
        @return: __vPERForceRepulsionObstacle
        """
        return self.__vPERForceRepulsionObstacle

    def getForceAttraction(self):
        """
        getter pour l'attribut __vPERForceAttraction
        @return: __vPERForceAttraction
        """
        return self.__vPERForceAttraction

    def getForceAcceleration(self):
        """
        getter pour l'attribut __vPERForceAcceleration
        @return: __vPERForceAcceleration
        """
        return self.__vPERForceAcceleration

    def getRayon(self):
        """
        getter pour l'attribut __fPERRayon
        @return: __fPERRayon
        """
        return self.__fPERRayon

    def getChampsDeVision(self):
        """
        getter pour l'attribut __fPERChampsDeVision
        @return: __fPERChampsDeVision
        """
        return self.__fPERChampsDeVision

#------------------------Setter------------------------

    def setVitesse(self, vitesse):
        """
        setter pour l'attribut __fPERVitesse
        @param vitesse: nouvelle vitesse qu'on veut affecter au pieton
        @return: rien
        """
        #TODO : exception si vitesse négatif ??
        self.__fPERVitesse = vitesse

    def setPression(self, pression):
        """
        setter pour l'attribut __fPERPression
        @param pression: nouvelle pression subit par le pieton
        @return: rien
        """
        #TODO : exception si pression négative ??
        self.__fPERPression = pression

    def setListDirection(self, direction):
        """
        setter pour l'attribut __lPERDirection
        @param direction: nouvelle direction pour le pieton
        @return: rien
        """
        self.__lPERDirection = direction

    def setListCoordonnees(self, coordonnees):
        """
        setter pour l'attribut __lPERCoordonees
        @param coordonnees: nouvelles corrdonées du pieton
        @return: rien
        """
        #TODO : exeption si taille de la liste > 2

        self.__lPERCoordonees = coordonnees

    def setRayon(self, rayon):
        """
        setter pour l'attribut __fPERRayon
        @param rayon: nouveau rayon
        @return:  rien
        """
        #TODO : exception si rayon < 0
        self.__fPERRayon = rayon

    def setChampsDeVision(self, chpsVision):
        """
        setter pour l'attribut __fPERChampsDeVision
        @param chpsVision: nouveau champde vision de la personne
        @return: rien
        """
        #TODO : exception si champ de vision négatif
        self.__fPERChampsDeVision = chpsVision

#------------------------Methodes------------------------

    def RecupererDirectionActuelle(self):
        """
        permet de récupérer la direction actuelle du pieton
        @return: Un np.array qui contient les coordonnées de la direction
        """
        return self.__lPERDirection[0]

    def RecupererDerniereCoordonne(self):
        """
        Permet de recuperer la coordonnee actuelle du pieton

        @return: coordonnee actuelle du pieton
        """
        if (len(self.__lPERCoordonees) == 2):
            return self.__lPERCoordonees[1]
        else :
            return self.__lPERCoordonees[0]

    def ajouterCoordonnees(self, coordonnees):
        """
        Permet d'ajouter une coordonnee dans la liste __lPERCoordonees

        @param coordonnees: coordonnee du pieton qu'on veut ajouter
        @return: rien
        """

        if(len(self.__lPERCoordonees) == 2) :
            self.__lPERCoordonees.pop(0)
            self.__lPERCoordonees.append(coordonnees)
        else :
            self.__lPERCoordonees.append(coordonnees)

    def ajouterPersonne(self,Personne):
        """
        Permet d'ajouter une personne proche du pieton dans la liste __lPERlistPersonneProximite
        @param Personne: personne proche du pieton
        @return: rien
        """
        self.__lPERlistPersonneProximite.append(Personne)

    def ajouterDirection(self, direction):
        """
        Permet d'ajouter une nouvelle direction pour le pieton dans la liste __lPERDirection
        @param direction: nouvelle direction que le pieton suivra
        @return: rien
        """
        self.__lPERDirection.append(direction)

    def ajouterObstacle(self,obstacle):
        """
        @param obstacle: permet d'ajouter un obstacle proche au pieton dans la liste __lPERlistObstacleProximite
        @return: rien
        """
        self.__lPERlistObstacleProximite.append(obstacle)

    def ClearPersonneProximite(self):
        """
        Vide la liste __lPERlistPersonneProximite
        @return: rien
        """
        self.__lPERlistPersonneProximite.clear()

    def ClearlistObstacleProx(self):
        """
        Vide la liste __lPERlistObstacleProximite
        @return: rien
        """
        self.__lPERlistObstacleProximite.clear()

    def CalculVecteurVitesse(self,t):
        """
        Permet de Calculer le vecteur vitesse du pieotn à l'instant t
        @param t: instant t pour lequel on calcul le vecteur vitesse
        @return:  rien
        """
        force = CForce()
        self.__vPERVitesse = force.VecteurVitesse(self.__lPERCoordonees[0], self.RecupererDerniereCoordonne(), t, )
        self.CalculVitesse()

    def CalculVitesse(self):
        """
        Permet de calculer la vitesse du pieton à partir du Vecteur Vitesse
        @return: rien
        """
        force = CForce()
        self.__fPERVitesse = np.linalg.norm(self.__vPERVitesse)
        Vmax = force.VitesseAlphaMax(1.34)
        if self.__fPERVitesse > Vmax :
            self.__vPERVitesse = Vmax

    def marcher(self):
        self.canvas.delete(self.image)
        self.image = COperation.create_circle(self.x, self.y, self.rayon, self.canvas, self.color)

    def CalculerForceRepulsion(self):
        """
        Permet de calculer la force de repulsion totale excercé par toute les personne qui sont dans __lPERlistPersonneProximite

        @return: rien
        """

        #recupere la valuer actuelle de la force la force de repulsion
        valeurTotaleForceRepulsion = np.array([0.0,0.0])#self.__vPERForceRepulsionPersonne.gettertForceRepulsion() ne pas decommenter provoque bug de la peste

        #calcul de nouvelle force de repulsion
        for personne in self.__lPERlistPersonneProximite :
            #TODO : Exception aucune direction
            valeurTotaleForceRepulsion += self.__vPERForceRepulsionPersonne.FREForceRepulsionPersonne(self.__lPERDirection[0], self.RecupererDerniereCoordonne(), self.__lPERCoordonees[0], personne.RecupererDerniereCoordonne(), personne.RecupererDirectionActuelle(), personne.getVitesse())

        self.__vPERForceRepulsionPersonne.settertForceRepulsion(valeurTotaleForceRepulsion)


    def CalculerForceRepulsionObstacle(self):
        """
        Permet de calculer la force de repulsion applique sur le pieton par tous les obstacles qui sont dans la liste __lPERlistObstacleProximite

        @return: rien
        """
        #sommet = np.array([0,0])
        valeurTotaleForceRepulsionObstacle = np.array([0.0,0.0]) #self.__vPERForceRepulsionObstacle.gettertForceRepulsion()

        for obstacle in self.__lPERlistObstacleProximite :
            if(len(self.__lPERlistObstacleProximite) != 0) :
                sommet = self.__vPERForceRepulsionObstacle.FREDeterminerSommetObstacle(self.RecupererDerniereCoordonne(), obstacle)
                valeurTotaleForceRepulsionObstacle += self.__vPERForceRepulsionObstacle.FREForceDeRepulsionObstacle(self.RecupererDerniereCoordonne(), self.__lPERCoordonees[0], sommet)

        self.__vPERForceRepulsionObstacle.settertForceRepulsion(valeurTotaleForceRepulsionObstacle)

    def CalculerForceAcceleration(self):
        """
        Permet de calculer la force d'acceleration

        @return: rien
        """
        eALpha = self.__lPERDirection[0]
        RAlpha = self.RecupererDerniereCoordonne()
        self.__vPERForceAcceleration.FACForceDacceleration(self.__vPERVitesse, 1.34, eALpha, RAlpha)

    def CalculerNouvellePosition(self,t):
        """
        Permet calculer la nouvelle position du pieton une fois toute les forces calcule et l'ajoute a la liste de coordonnees __lPERCoordonees

        @return: rien
        """
        Force = self.__vPERForceAcceleration.FACgetForceAcceleration() + self.__vPERForceRepulsionPersonne.gettertForceRepulsion() + self.__vPERForceRepulsionObstacle.gettertForceRepulsion() #+self.__vPERForceAttraction.get() # pas encore fait
        nouvellecoord = self.RecupererDerniereCoordonne()+Force
        self.ajouterCoordonnees(nouvellecoord)
        self.CalculVecteurVitesse(t)


    def sorti(self):
        """
        Permet de savoir si la personne est sortie ou non

        @return: booleen
        """
        coordonneeSortie = self.__lPERDirection[0]
        coordonneePieton = self.RecupererDerniereCoordonne()

        #On verifie si le pieton est aux alentours de la sortie.
        IsGone = COperation.DetectionCercle(coordonneeSortie[0], coordonneeSortie[1], coordonneePieton[0], coordonneePieton[1], 3)

        #Si oui, on retire les coordonnees de la sortie de sa memoire.
        if IsGone:
            return True
        else:
            return False


