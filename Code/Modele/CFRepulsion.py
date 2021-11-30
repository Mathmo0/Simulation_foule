from Code.Modele.CForce import CForce,tau
from Code.Modele.COperation import COpetation

from numpy import linalg as la

class CFRepulsion(CForce) :

    def __init__(self, tForceRepulsion):
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
        nablarAlphaB = COpetation.Nabla(Ralpha, RalphaDeltaT, Rbeta)
        bEffet = self.b(Ralpha, Rbeta, vitesseBeta, vRkBeta)
        V = self.VAlphaBeta(bEffet)

        return nablarAlphaB * V

    def FREForceDeRepulsionObstacle(self,Ralpha, RalphaDeltaT, RObstacle):
        """
        Cette fonction permet de calculer La force de replsion exercer sur un pieton par un obstacle

        @param Ralpha: position du piéton alpha à l'instant t
        @param RalphaDeltaT: position du piéton à l'instant t-DeltaT
        @param RObstacle: pposition de l'obstacle
        @return: valeur de la force de repulsion exercer par l'obstacle sur le pieton Alpha

        """
        NablaFRO = COpetation.Nabla(Ralpha, RalphaDeltaT, RObstacle)
        NormeVecteurRAlphaObstacle = la.norm(Ralpha - RObstacle)
        UFRO = COpetation.UAlphaObstacle(NormeVecteurRAlphaObstacle)

        return NablaFRO * UFRO

    def FREForceRepulsionPersonne(self,vRkAlpha, Ralpha, RalphaDeltaT, Rbeta, vRkBeta, vitesseBeta):
        """
        Cette fonction permet de calculer la force de repulsion d'un pieton Beta sur un pieton Alpha

        @param vRkAlpha : destination du pieton alpha
        @param Ralpha : position du piéton alpha à l'instant t
        @param RalphaDeltaT : position du piéton à l'instant t-DeltaT
        @param Rbeta : position du piéotn beta à l'instant t
        @param vRkBeta : destination du piéton Beta
        @param vitesseBeta : vitesse du piéton beta
        @return: valeur de la force de repulsion applique par le pieton Beta sur le pieton Alpha

        """
        eAlphaFRP = self.eAlpha(vRkAlpha, Ralpha)
        EffetrepulsionRFP = self.FREEffetDeRepulsion(Ralpha, RalphaDeltaT, Rbeta, vRkBeta, vitesseBeta)

        self.tForceRepulsion = self.w(eAlphaFRP, -EffetrepulsionRFP) * EffetrepulsionRFP

        return self.tForceRepulsion
