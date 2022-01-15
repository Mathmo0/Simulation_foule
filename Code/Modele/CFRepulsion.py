import numpy as np

from Code.Modele.CForce import CForce,tau
from Code.Modele.COperation import COperation
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere

from numpy import linalg as la
import numpy as np

class CFRepulsion(CForce) :

    def __init__(self, tForceRepulsion = np.array([0.0,0.0])):
        self.tForceRepulsion = tForceRepulsion

    def gettertForceRepulsion(self):
        """
        getter pour l'attribut tForceRepulsion

        @return: tForceRepulsion
        """
        return self.tForceRepulsion

    def settertForceRepulsion(self,newForceRepulsion):
        """
        setter pour l'attribut tForceRepulsion

        @param newForceRepulsion:  nouvelle valeur de tForceRepulsion
        @return: rien

        """
        self.tForceRepulsion = newForceRepulsion

    def FREEffetDeRepulsion(self,Ralpha, RalphaDeltaT, Rbeta, vRkBeta, vitesseBeta):
        """
        cette fonction permet de calculer l'effet de repulsion entre 2 piétons Alpha et Beta

        @param Ralpha : position du piéton alpha à l'instant t
        @param RalphaDeltaT : position du piéton à l'instant t-DeltaT
        @param Rbeta : position du piéotn beta à l'instant t
        @param vRkBeta : destination du piéton Beta
        @param vitesseBeta : vitesse du piéton beta
        @return: valeur de l'effet de repulsion

        """
        nablarAlphaB = COperation.Nabla(Ralpha, Rbeta, Rbeta)
        bEffet = self.b(Ralpha, Rbeta, vitesseBeta, vRkBeta)
        V = self.VAlphaBeta(bEffet)

        return nablarAlphaB * V

    def FREForceDeRepulsionObstacle(self,Ralpha, RalphaDeltaT, RObstacle):
        """
        Cette fonction permet de calculer La force de repulsion exercer sur un pieton par un obstacle

        @param Ralpha: position du piéton alpha à l'instant t
        @param RalphaDeltaT: position du piéton à l'instant t-DeltaT
        @param RObstacle: position de l'obstacle
        @return: valeur de la force de repulsion exercer par l'obstacle sur le pieton Alpha

        """
        NablaFRO = COperation.Nabla(Ralpha, RObstacle, RObstacle)
        NormeVecteurRAlphaObstacle = la.norm(Ralpha - RObstacle)
        UFRO = self.UAlphaObstacle(NormeVecteurRAlphaObstacle)

        return NablaFRO * UFRO

    def FREForceRepulsionPersonne(self,vRkAlpha, Ralpha, RalphaDeltaT, Rbeta, vRkBeta, vitesseBeta):
        """
        Cette fonction permet de calculer la force de repulsion d'un pieton Beta sur un pieton Alpha

        @param vRkAlpha : destination du pieton alpha
        @param Ralpha : position du piéton alpha à l'instant t
        @param RalphaDeltaT : position du piéton à l'instant t-DeltaT
        @param Rbeta : position du piéton beta à l'instant t
        @param vRkBeta : destination du piéton Beta
        @param vitesseBeta : vitesse du piéton beta
        @return: valeur de la force de repulsion applique par le pieton Beta sur le pieton Alpha

        """
        eAlphaFRP = self.eAlpha(vRkAlpha, Ralpha)
        EffetrepulsionRFP = self.FREEffetDeRepulsion(Ralpha, RalphaDeltaT, Rbeta, vRkBeta, vitesseBeta)

        self.tForceRepulsion = self.w(eAlphaFRP, -EffetrepulsionRFP) * EffetrepulsionRFP

        return self.tForceRepulsion

    def FREDeterminerSommetObstacleQuadrilatere(self, coordPieton, obstacle:CObstacleQuadrilatere):
        """
        Cette fontion permet de lequel des sommets d'un obstacle est utilise pour calculer la force de repulsion entre un personne et un obstacle
        @param coordPieton: coordonnes du pieton sur lequel est applique la force de repulsion Personne-Obstacle
        @param obstacle: obstacle qui va appliquer la force de repulsion Personne-Obstacle
        @return: coordonnees du sommet qui va etre utilisée pour appliquer la force de repulsion Personne-Obstacle

        """
        listsommet = obstacle.getCoordonneesSommet()
        sommetRetenu = np.array([0,0])
        distance = 99999999999

        #determination du centre de l'obstacle: [topLeft, topRight, bottomLeft, bottomRight]

        centreX = listsommet[0][0] + obstacle.getLargeur()/2
        centreY = listsommet[0][1] + obstacle.getHauteur()/2
        centre = np.array([centreX, centreY])

        #determination position pieton par rapport a l'obstacle:

        if  coordPieton[1] <= listsommet[2][1] and  coordPieton[1] >= listsommet[0][1] and coordPieton[0] <= listsommet[0][0]:



        for sommet in listsommet :

            distancePO = la.norm(coordPieton-sommet)
            if(distancePO < distance) :
                sommetRetenu = sommet
                distance = distancePO
        return sommetRetenu


