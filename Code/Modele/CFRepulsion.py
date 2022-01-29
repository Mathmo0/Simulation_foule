import numpy as np

from Code.Modele.CForce import CForce,tau
from Code.Modele.COperation import COperation
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere

from numpy import linalg as la
import numpy as np

class CFRepulsion(CForce) :

    def __init__(self, tForceRepulsion = np.array([0.0,0.0])):
        self.__tFREForceRepulsion = tForceRepulsion

    def FREgettertForceRepulsion(self):
        """
        getter pour l'attribut __tFREForceRepulsion

        @return: __tFREForceRepulsion
        """
        return self.__tFREForceRepulsion

    def FREsettertForceRepulsion(self, newForceRepulsion):
        """
        setter pour l'attribut __tFREForceRepulsion

        @param newForceRepulsion:  nouvelle valeur de __tFREForceRepulsion
        @return: rien

        """
        self.__tFREForceRepulsion = newForceRepulsion

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
        nablarAlphaB = COperation.OPENabla(Ralpha, Rbeta, Rbeta)
        bEffet = self.FORb(Ralpha, Rbeta, vitesseBeta, vRkBeta)
        V = self.FORVAlphaBeta(bEffet)

        return -nablarAlphaB * V

    def FREForceDeRepulsionObstacle(self,Ralpha, RalphaDeltaT, RObstacle):
        """
        Cette fonction permet de calculer La force de repulsion exercer sur un pieton par un obstacle

        @param Ralpha: position du piéton alpha à l'instant t
        @param RalphaDeltaT: position du piéton à l'instant t-DeltaT
        @param RObstacle: position de l'obstacle
        @return: valeur de la force de repulsion exercer par l'obstacle sur le pieton Alpha

        """
        NablaFRO = COperation.OPENabla(Ralpha, RObstacle, RObstacle)
        NormeVecteurRAlphaObstacle = la.norm(Ralpha - RObstacle)
        UFRO = self.FORUAlphaObstacle(NormeVecteurRAlphaObstacle)

        return -NablaFRO * UFRO

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
        eAlphaFRP = self.FOReAlpha(vRkAlpha, Ralpha)
        EffetrepulsionRFP = self.FREEffetDeRepulsion(Ralpha, RalphaDeltaT, Rbeta, vRkBeta, vitesseBeta)

        self.__tFREForceRepulsion = self.FORw(eAlphaFRP, -EffetrepulsionRFP) * EffetrepulsionRFP

        return self.__tFREForceRepulsion

    def FREDeterminerSommetObstacleQuadrilatere(self, coordPieton, obstacle:CObstacleQuadrilatere):
        """
        Cette fontion permet de lequel des sommets d'un obstacle est utilise pour calculer la force de repulsion entre un personne et un obstacle

        @param coordPieton: coordonnes du pieton sur lequel est applique la force de repulsion Personne-Obstacle
        @param obstacle: obstacle qui va appliquer la force de repulsion Personne-Obstacle
        @return: coordonnees du sommet qui va etre utilisée pour appliquer la force de repulsion Personne-Obstacle

        """
        listsommet = obstacle.OBSgetCoordonneesSommet()
        sommetRetenu = np.array([0.0,0.0])


        #determination du centre de l'obstacle: [topLeft, topRight, bottomLeft, bottomRight]

        centreX = listsommet[0][0] + obstacle.OBQgetLargeur() / 2
        centreY = listsommet[0][1] + obstacle.OBQgetHauteur() / 2
        centre = np.array([centreX, centreY])
        coef = COperation.OPEFonctionTrajectoirePieton(centre, coordPieton)

        #determination position pieton par rapport a l'obstacle:

        # cote gauche de l'obstacle:
        if  coordPieton[1] <= listsommet[2][1] and  coordPieton[1] >= listsommet[0][1] and coordPieton[0] <= listsommet[0][0]:
                x = listsommet[0][0]
                y = coef[0]*x + coef[1]
                sommetRetenu = np.array([x,y])

        # coin top left:
        elif coordPieton[1] >= listsommet[0][1] and coordPieton[0] <= listsommet[0][0]:
            sommetRetenu = listsommet[0]

        # en haut de l'obstacle:
        elif coordPieton[1] >= listsommet[0][1] and listsommet[0][0] <= coordPieton[0] <= listsommet[1][0]:

            y = listsommet[0][1]
            x =  (y- coef[1])/coef[0]
            sommetRetenu = np.array([x, y])

        # coin topRight
        elif coordPieton[1] >= listsommet[0][1] and coordPieton[0] >= listsommet[1][0]:
            sommetRetenu = listsommet[1]

        # a droite de l'obstacle:
        elif listsommet[3][1] <= coordPieton[1] <= listsommet[0][1] and coordPieton[0] >= listsommet[3][0]:

            x = listsommet[1][0]
            y = coef[0] * x + coef[1]
            sommetRetenu = np.array([x, y])

        # coin bottom Right:
        elif coordPieton[1] <= listsommet[3][1] and coordPieton[0] >= listsommet[3][0]:
            sommetRetenu = listsommet[3]

        # en bas :
        elif listsommet[2][0] <= coordPieton[0] <= listsommet[3][0] and coordPieton[1] <= listsommet[3][1]:
            y = listsommet[2][1]
            x = (y - coef[1]) / coef[0]
            sommetRetenu = np.array([x, y])

        # coin bottomLeft:
        elif coordPieton[1] <= listsommet[2][1] and coordPieton[0] <= listsommet[2][0]:
            sommetRetenu = listsommet[2]
        return sommetRetenu


