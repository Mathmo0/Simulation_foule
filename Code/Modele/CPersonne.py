from typing import List

import numpy as np

from Code.Modele.COperation import COperation
from Code.Modele.CFRepulsion import CFRepulsion
from Code.Modele.CFAcceleration import CFAcceleration
from Code.Modele.CFAttraction import CFAttraction
from Code.Modele.CForce import CForce,Phi
from Code.Modele.CObstacle import CObstacle

class CPersonne:

    #-------------------Constructeur-------------------:
    def __init__(self,recursif = False,coordonnees = np.array([0,0]),vitesse = 1.34, pression = 0, rayon = 1, chpsVision = Phi,ForceRepulsion =CFRepulsion(), ForceObstacle = CFRepulsion() ,ForceAttraction = CFAttraction(),ForceAccelaration = CFAcceleration()):
        assert vitesse >= 0, " La vitesse doit etre positive"
        assert pression >= 0, "La pression doit etre positive"
        assert rayon > 0, "La rayon doit etre strictement positive "
        assert chpsVision > 0, "Le champ de vision doit être strictement positif"

        self.__vPERVecteurVitesse = np.array([0, 0])
        self.__fPERVitesse = vitesse
        self.__fPERPression = pression
        self.__lPERDirection: List[np.array()] = []
        self.__lPERCoordonees = [coordonnees] #cette litse contient 2 coordonnees , en indice 0 la coordonnees à l'instant t-Deltat et en indice 1 la coordonnees à l'instant t
        if recursif == False :
            self.__lPERlistPersonneProximite = [CPersonne(True)]
        else :
            self.__lPERlistPersonneProximite = []

        self.__lPERlistObstacleProximite: List[CObstacle] = []
        self.__vPERForceRepulsionPersonne = ForceRepulsion
        self.__vPERForceRepulsionObstacle = ForceObstacle
        self.__vPERForceAttraction = ForceAttraction
        self.__vPERForceAcceleration = ForceAccelaration
        self.__fPERRayon = 10 # rayon
        self.__fPERChampsDeVision = chpsVision

    #------------------------Getter------------------------

    def PERgetVitesse(self):
        """
        getter pour l'attribut __fPERVitesse

        @return: __fPERVitesse
        """
        return self.__fPERVitesse

    def PERgetVecteurVitesse(self):
        """
        getter pour l'attribut __vPERVitesse

        @return: __vPERVitesse
        """
        return self.__vPERVecteurVitesse

    def PERgetPression(self):
        """
        getter pour l'attribut __fPERPression

        @return: __fPERPression
        """
        return self.__fPERPression

    def PERgetListDirection(self) :
        """
        getter pour l'attribut .__lPERDirection

        @return: __lDirection
        """
        return self.__lPERDirection

    def PERgetListCoordonnees(self):
        """
        getter pour l'attribut __lPERCoordonees

        @return: __lPERCoordonees
        """
        return self.__lPERCoordonees

    def PERgetListPersonneProx(self):
        """
        getter pour l'attribut __lPERlistPersonneProximite

        @return: __lPERlistPersonneProximite
        """
        return self.__lPERlistPersonneProximite

    def PERgetlistObstacle(self):
        """
        getter pour l'attribut __lPERlistObstacleProximite

        @return: __lPERlistObstacleProximite
        """
        return self.__lPERlistObstacleProximite

    def PERgetForceRepulsionPersonne(self):
        """
        getter pour l'attribut __vPERForceRepulsionPersonne

        @return: __vPERForceRepulsionPersonne
        """
        return self.__vPERForceRepulsionPersonne

    def PERgetForceRepulsionObstacle(self):
        """
        getter pour l'attribut __vPERForceRepulsionObstacle

        @return: __vPERForceRepulsionObstacle
        """
        return self.__vPERForceRepulsionObstacle

    def PERgetForceAttraction(self):
        """
        getter pour l'attribut __vPERForceAttraction

        @return: __vPERForceAttraction
        """
        return self.__vPERForceAttraction

    def PERgetForceAcceleration(self):
        """
        getter pour l'attribut __vPERForceAcceleration

        @return: __vPERForceAcceleration
        """
        return self.__vPERForceAcceleration

    def PERgetRayon(self):
        """
        getter pour l'attribut __fPERRayon

        @return: __fPERRayon
        """
        return self.__fPERRayon

    def PERgetChampsDeVision(self):
        """
        getter pour l'attribut __fPERChampsDeVision

        @return: __fPERChampsDeVision
        """
        return self.__fPERChampsDeVision

    #------------------------Setter------------------------

    def PERsetVitesse(self, vitesse):
        """
        setter pour l'attribut __fPERVitesse

        @param vitesse: nouvelle vitesse qu'on veut affecter au pieton

        @return: void
        """
        assert vitesse >= 0," La vitesse doit etre positive"

        self.__fPERVitesse = vitesse

    def PERsetPression(self, pression):
        """
        setter pour l'attribut __fPERPression

        @param pression: nouvelle pression subit par le pieton

        @return: void
        """
        assert pression >= 0, "La pression doit etre positive"

        self.__fPERPression = pression

    def PERsetListDirection(self, direction):
        """
        setter pour l'attribut __lPERDirection

        @param direction: nouvelle direction pour le pieton

        @return: void
        """
        self.__lPERDirection = direction

    def PERsetListCoordonnees(self, listcoordonnees):
        """
        setter pour l'attribut __lPERCoordonees

        @param coordonnees: nouvelles corrdonees du pieton

        @return: void
        """
        self.__lPERCoordonees = listcoordonnees

    def PERsetRayon(self, rayon):
        """
        setter pour l'attribut __fPERRayon

        @param rayon: nouveau rayon

        @return:  void
        """
        assert rayon > 0 , "La rayon doit etre strictement positive "

        self.__fPERRayon = rayon

    def PERsetChampsDeVision(self, chpsVision):
        """
        setter pour l'attribut __fPERChampsDeVision

        @param chpsVision: nouveau champ de vision de la personne

        @return: void
        """
        assert chpsVision > 0,"Le champ de vision doit être strictement positif"

        self.__fPERChampsDeVision = chpsVision

#------------------------Methodes------------------------

    def PERRecupererDirectionActuelle(self):
        """
        permet de récupérer la direction actuelle du pieton

        @return: Un np.array qui contient les coordonnées de la direction
        """
        return self.__lPERDirection[0]

    def PERRecupererDerniereCoordonne(self):
        """
        Permet de recuperer la coordonnee actuelle du pieton

        @return: coordonnee actuelle du pieton
        """
        if (len(self.__lPERCoordonees) == 2):
            return self.__lPERCoordonees[1]
        else :
            return self.__lPERCoordonees[0]

    def PERajouterCoordonnees(self, coordonnees):
        """
        Permet d'ajouter une coordonnee dans la liste __lPERCoordonees

        @param coordonnees: coordonnee du pieton qu'on veut ajouter

        @return: void
        """

        if(len(self.__lPERCoordonees) == 2) :
            self.__lPERCoordonees.pop(0)
            self.__lPERCoordonees.append(coordonnees)
        else :
            self.__lPERCoordonees.append(coordonnees)

    def PERajouterPersonne(self, Personne):
        """
        Permet d'ajouter une personne proche du pieton dans la liste __lPERlistPersonneProximite

        @param Personne: personne proche du pieton

        @return: void
        """
        self.__lPERlistPersonneProximite.append(Personne)

    def PERajouterDirection(self, direction):
        """
        Permet d'ajouter une nouvelle direction pour le pieton dans la liste __lPERDirection

        @param direction: nouvelle direction que le pieton suivra

        @return: void
        """
        self.__lPERDirection.append(direction)

    def PERajouterObstacle(self, obstacle):
        """
        Permet d'ajouter un obstacle dans la liste des obstacles a proximite de la personne

        @param obstacle: permet d'ajouter un obstacle proche au pieton dans la liste __lPERlistObstacleProximite

        @return: void
        """
        self.__lPERlistObstacleProximite.append(obstacle)

    def PERClearPersonneProximite(self):
        """
        Vide la liste __lPERlistPersonneProximite

        @return: void
        """
        self.__lPERlistPersonneProximite.clear()

    def PERClearlistObstacleProx(self):
        """
        Vide la liste __lPERlistObstacleProximite

        @return: void
        """
        self.__lPERlistObstacleProximite.clear()

    def PERCalculVecteurVitesse(self, t):
        """
        Permet de Calculer le vecteur vitesse du pieotn à l'instant t

        @param t: instant t pour lequel on calcule le vecteur vitesse

        @return:  void
        """
        force = CForce()
        self.__vPERVecteurVitesse = force.FORVecteurVitesse(self.__lPERCoordonees[0], self.PERRecupererDerniereCoordonne(), t)
        self.PERCalculVitesse()

    def PERCalculVitesse(self):
        """
        Permet de calculer la vitesse du pieton à partir du Vecteur Vitesse

        @return: void
        """
        force = CForce()
        self.__fPERVitesse = np.linalg.norm(self.__vPERVecteurVitesse)
        Vmax = force.FORVitesseAlphaMax(1.34)
        if self.__fPERVitesse > Vmax :
            self.__vPERVecteurVitesse = Vmax

    def PERCalculerForceRepulsion(self):
        """
        Permet de calculer la force de repulsion totale excerce par toute les personne qui sont dans __lPERlistPersonneProximite

        @return: void
        """
        valeurTotaleForceRepulsion = np.array([0.0,0.0])

        #calcul de nouvelle force de repulsion
        for personne in self.__lPERlistPersonneProximite :
            try :
                valeurTotaleForceRepulsion += self.__vPERForceRepulsionPersonne.FREForceRepulsionPersonne(self.__lPERDirection[0], self.PERRecupererDerniereCoordonne(), self.__lPERCoordonees[0], personne.PERRecupererDerniereCoordonne(), personne.PERRecupererDirectionActuelle(), personne.PERgetVitesse())# self.__fPERRayon
            except :
                print("Le pieton n'a aucun direction, on ne peut donc pas calculer la force de repulsion")

        self.__vPERForceRepulsionPersonne.FREsettertForceRepulsion(valeurTotaleForceRepulsion)


    def PERCalculerForceRepulsionObstacle(self):
        """
        Permet de calculer la force de repulsion applique sur le pieton par tous les obstacles qui sont dans la liste __lPERlistObstacleProximite

        @return: void
        """
        sommet = np.array([0.0,0.0])
        valeurTotaleForceRepulsionObstacle = np.array([0.0,0.0])

        for obstacle in self.__lPERlistObstacleProximite :
                sommet = self.__vPERForceRepulsionObstacle.FREDeterminerSommetObstacleQuadrilatere(self.PERRecupererDerniereCoordonne(), obstacle)
                valeurTotaleForceRepulsionObstacle += self.__vPERForceRepulsionObstacle.FREForceDeRepulsionObstacle(self.PERRecupererDerniereCoordonne(), self.__lPERCoordonees[0], sommet)
        self.__vPERForceRepulsionObstacle.FREsettertForceRepulsion(valeurTotaleForceRepulsionObstacle)

    def PERCalculerForceAcceleration(self):
        """
        Permet de calculer la force d'acceleration

        @return: void
        """
        eALpha = self.__lPERDirection[0]
        RAlpha = self.PERRecupererDerniereCoordonne()
        self.__vPERForceAcceleration.FACForceDacceleration(self.__vPERVecteurVitesse, 1.34, eALpha, RAlpha)

    def PERCalculForceAttraction(self, t):

        valeurTotaleForceAttraction = np.array([0.0, 0.0])

        ealphaAttrac = self.__vPERForceAttraction.FOReAlpha(self.PERRecupererDirectionActuelle(), self.PERRecupererDerniereCoordonne())

        # calcul de nouvelle force de repulsion

        for personne in self.__lPERlistPersonneProximite:
            try:
                valeurTotaleForceAttraction += self.__vPERForceAttraction.FATForceAttraction(ealphaAttrac, self.PERRecupererDerniereCoordonne(), personne.PERRecupererDerniereCoordonne(), t)
            except:
                print("Le pieton a un problème, on ne peut donc pas calculer la force d'attraction")

        self.__vPERForceRepulsionPersonne.FREsettertForceRepulsion(valeurTotaleForceAttraction)

    def PERCalculerNouvellePosition(self, t):
        """
        Permet calculer la nouvelle position du pieton une fois toutes les forces calculees et l'ajoute a la liste de coordonnees __lPERCoordonees

        @return: void
        """
        Force = self.__vPERForceAcceleration.FACgetForceAcceleration() + self.__vPERForceRepulsionPersonne.FREgettertForceRepulsion() + self.__vPERForceRepulsionObstacle.FREgettertForceRepulsion() #+self.__vPERForceAttraction.get() # pas encore fait
        self.__fPERPression = np.linalg.norm(Force)
        nouvellecoord = self.PERRecupererDerniereCoordonne() + Force
        self.PERajouterCoordonnees(nouvellecoord)
        self.PERCalculVecteurVitesse(t)

    def PERsorti(self):
        """
        Permet de savoir si la personne est sortie ou non

        @return: booleen
        """
        coordonneeSortie = self.__lPERDirection[0]
        coordonneePieton = self.PERRecupererDerniereCoordonne()

        #On verifie si le pieton est aux alentours de la sortie.
        IsGone = COperation.OPEDetectionCercle(coordonneeSortie[0], coordonneeSortie[1], coordonneePieton[0], coordonneePieton[1], 4)

        #Si oui, on retire les coordonnees de la sortie de sa memoire.
        if IsGone:
            return True
        else:
            return False


    def PERPlusCourtChemin(self):
        """
        Permet de determiner la direction que le pieton doit emprunter

        @return: void
        """
        distance = 9999999999999999999
        coord = []
        for i in range(0, len(self.__lPERDirection)):
            distanceBIS = np.linalg.norm(self.__lPERCoordonees[0] - self.__lPERDirection[i])
            if distance > distanceBIS:
                distance = distanceBIS
                coord = self.__lPERDirection[i]
        self.__lPERDirection = coord
