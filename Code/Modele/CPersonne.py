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
        assert vitesse >= 0, " La vitesse doit etre positive"
        assert pression >= 0, "La pression doit etre positive"
        assert rayon > 0, "La rayon doit etre strictement positive "
        assert chpsVision > 0, "Le champ de vision doit être strictement positif"

        self.__vPERVecteurVitesse = np.array([0, 0])
        self.__fPERVitesse = vitesse
        self.__fPERPression = pression
        self.__lPERDirection: List[np.array()] = []
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
        self.__fPERRayon = 10# rayon
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
        return self.__vPERVecteurVitesse

    def getPression(self):
        """
        getter pour l'attribut __fPERPression
        @return: __fPERPression
        """
        return self.__fPERPression

    def getListDirection(self) :
        """
        getter pour l'attribut .__lPERDirection
        @return: __lDirection
        """
        return self.__lPERDirection

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
        assert vitesse >= 0," La vitesse doit etre positive"

        self.__fPERVitesse = vitesse

    def setPression(self, pression):
        """
        setter pour l'attribut __fPERPression
        @param pression: nouvelle pression subit par le pieton
        @return: rien
        """
        assert pression >= 0, "La pression doit etre positive"

        self.__fPERPression = pression

    def setListDirection(self, direction):
        """
        setter pour l'attribut __lPERDirection
        @param direction: nouvelle direction pour le pieton
        @return: rien
        """
        self.__lPERDirection = direction

    def setListCoordonnees(self, listcoordonnees):
        """
        setter pour l'attribut __lPERCoordonees
        @param coordonnees: nouvelles corrdonées du pieton
        @return: rien
        """
        #TODO : exeption si taille de la liste > 2

        self.__lPERCoordonees = listcoordonnees

    def setRayon(self, rayon):
        """
        setter pour l'attribut __fPERRayon
        @param rayon: nouveau rayon
        @return:  rien
        """
        assert rayon > 0 , "La rayon doit etre strictement positive "

        self.__fPERRayon = rayon

    def setChampsDeVision(self, chpsVision):
        """
        setter pour l'attribut __fPERChampsDeVision
        @param chpsVision: nouveau champde vision de la personne
        @return: rien
        """
        assert chpsVision > 0,"Le champ de vision doit être strictement positif"

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
        self.__vPERVecteurVitesse = force.VecteurVitesse(self.__lPERCoordonees[0], self.RecupererDerniereCoordonne(), t)
        self.CalculVitesse()

    def CalculVitesse(self):
        """
        Permet de calculer la vitesse du pieton à partir du Vecteur Vitesse
        @return: rien
        """
        force = CForce()
        self.__fPERVitesse = np.linalg.norm(self.__vPERVecteurVitesse)
        Vmax = force.VitesseAlphaMax(1.34)
        if self.__fPERVitesse > Vmax :
            self.__vPERVecteurVitesse = Vmax

    def CalculerForceRepulsion(self):
        """
        Permet de calculer la force de repulsion totale excercé par toute les personne qui sont dans __lPERlistPersonneProximite

        @return: rien
        """
        valeurTotaleForceRepulsion = np.array([0.0,0.0])

        #calcul de nouvelle force de repulsion
        for personne in self.__lPERlistPersonneProximite :
            #TODO : Exception aucune direction
            try :
                valeurTotaleForceRepulsion += self.__vPERForceRepulsionPersonne.FREForceRepulsionPersonne(self.__lPERDirection[0], self.RecupererDerniereCoordonne(), self.__lPERCoordonees[0], personne.RecupererDerniereCoordonne(), personne.RecupererDirectionActuelle(), personne.getVitesse())# self.__fPERRayon
            except :
                print("Le pieton n'a aucun direction, on ne peut donc pas calculer la force de repulsion")

        self.__vPERForceRepulsionPersonne.settertForceRepulsion(valeurTotaleForceRepulsion)


    def CalculerForceRepulsionObstacle(self):
        """
        Permet de calculer la force de repulsion applique sur le pieton par tous les obstacles qui sont dans la liste __lPERlistObstacleProximite

        @return: rien
        """
        sommet = np.array([0.0,0.0])
        valeurTotaleForceRepulsionObstacle = np.array([0.0,0.0])

        for obstacle in self.__lPERlistObstacleProximite :
                sommet = self.__vPERForceRepulsionObstacle.FREDeterminerSommetObstacleQuadrilatere(self.RecupererDerniereCoordonne(), obstacle)
                valeurTotaleForceRepulsionObstacle += self.__vPERForceRepulsionObstacle.FREForceDeRepulsionObstacle(self.RecupererDerniereCoordonne(), self.__lPERCoordonees[0], sommet)
        self.__vPERForceRepulsionObstacle.settertForceRepulsion(valeurTotaleForceRepulsionObstacle)

    def CalculerForceAcceleration(self):
        """
        Permet de calculer la force d'acceleration

        @return: rien
        """
        eALpha = self.__lPERDirection[0]
        RAlpha = self.RecupererDerniereCoordonne()
        self.__vPERForceAcceleration.FACForceDacceleration(self.__vPERVecteurVitesse, 1.34, eALpha, RAlpha)

    def CalculForceAttraction(self,t):

        valeurTotaleForceAttraction = np.array([0.0, 0.0])

        ealphaAttrac = self.__vPERForceAttraction.eAlpha(self.RecupererDirectionActuelle(),self.RecupererDerniereCoordonne())

        # calcul de nouvelle force de repulsion

        for personne in self.__lPERlistPersonneProximite:
            try:
                valeurTotaleForceAttraction += self.__vPERForceAttraction.FRAForceAttraction(ealphaAttrac,self.RecupererDerniereCoordonne(),personne.RecupererDerniereCoordonne(),t)
            except:
                print("Le pieton a un problème, on ne peut donc pas calculer la force d'attraction")

        self.__vPERForceRepulsionPersonne.settertForceRepulsion(valeurTotaleForceAttraction)

    def CalculerNouvellePosition(self,t):
        """
        Permet calculer la nouvelle position du pieton une fois toute les forces calcule et l'ajoute a la liste de coordonnees __lPERCoordonees

        @return: rien
        """
        Force = self.__vPERForceAcceleration.FACgetForceAcceleration() + self.__vPERForceRepulsionPersonne.gettertForceRepulsion() + self.__vPERForceRepulsionObstacle.gettertForceRepulsion() #+self.__vPERForceAttraction.get() # pas encore fait
        self.__fPERPression = np.linalg.norm(Force)
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
        IsGone = COperation.DetectionCercle(coordonneeSortie[0], coordonneeSortie[1], coordonneePieton[0], coordonneePieton[1], 4)

        #Si oui, on retire les coordonnees de la sortie de sa memoire.
        if IsGone:
            return True
        else:
            return False


    def PlusCourtChemin(self):
        distance = 9999999999999999999
        coord = []
        for i in range(0, len(self.__lPERDirection)):
            distanceBIS = np.linalg.norm(self.__lPERCoordonees[0] - self.__lPERDirection[i])
            if distance > distanceBIS:
                distance = distanceBIS
                coord = self.__lPERDirection[i]
        self.__lPERDirection = coord
