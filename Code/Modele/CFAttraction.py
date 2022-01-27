import numpy as np
from Code.Modele.CForce import CForce
from Code.Modele.COperation import COperation

class CFAttraction(CForce) :

    def __init__(self,ValeurForceAttraction = np.array([0.0,0.0])) :
        self.__tFATValeurForceAttraction = ValeurForceAttraction

    def getValeurForceAttraction(self):
        """
        getter pour l'attribut __tFATValeurForceAttraction

        @return: __tFATValeurForceAttraction
        """
        return self.__tFATValeurForceAttraction

    def setValeurForceAttraction(self,ValeurForceAttraction):

        """
         setter pour l'attribut __tFATValeurForceAttraction
        @param ValeurForceAttraction: nouvelle valeur pour la force d'attraction

        @return: rien
        """
        self.__tFATValeurForceAttraction = ValeurForceAttraction

    def FRAeffetAttraction(self,Ralpha,Ri,t) :
        """
        Cette fonction permet de calculer l'effet d'attraction

        @param Ralpha: Position du pieton alpha à l'instant t
        @param Ri: Position du pieton i à l'instant t
        @param t: temps actuelle dans la simulation

        @return: la valeur de l'effet de repulsion
        """
        Nabla = COperation.Nabla(Ralpha,Ri,Ri)
        normeRalphaI = np.linalg.norm(Ralpha-Ri)

        Wattraction = self.W(self,normeRalphaI,t)

        return -Nabla*Wattraction

    def FRAForceAttraction(self,eApha,RAlpha,Ri,t) :
        """
        Cette fcontion permet de calculer l'effet d'attraction

        @param eApha: vecteur direction du pieton alpha
        @param Ralpha: Position du pieton alpha à l'instant t
        @param Ri: Position du pieton i à l'instant t
        @param t: temps actuelle dans la simulation

        @return: valeur de la force d'attraction

        """
        effetAttraction = self.FRAeffetAttraction(RAlpha,Ri,t)
        self.__tFATValeurForceAttraction = self.w(eApha,effetAttraction)*effetAttraction

        return self.__tFATValeurForceAttraction
