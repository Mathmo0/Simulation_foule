import numpy as np
from Code.Modele.CForce import CForce
from Code.Modele.COperation import COperation

class CFAttraction(CForce) :

    def __init__(self,ValeurForceAttraction = np.array([0.0,0.0])) :
        self.ValeurForceAttraction = ValeurForceAttraction

    def getValeurForceAttraction(self):
        return self.ValeurForceAttraction

    def setValeurForceAttraction(self,ValeurForceAttraction):
        self.ValeurForceAttraction = ValeurForceAttraction

    def FRAeffetAttraction(self,Ralpha,Ri,t) :

        Nabla = COperation.Nabla(Ralpha,Ri,Ri)
        normeRalphaI = np.linalg.norm(Ralpha-Ri)

        Wattraction = self.W(self,normeRalphaI,t)

        return -Nabla*Wattraction

    def FRAForceAttraction(self,eApha,RAlpha,Ri,t) :

        effetAttraction = self.FRAeffetAttraction(RAlpha,Ri,t)
        valeurForce = self.w(eApha,effetAttraction)*effetAttraction

        return valeurForce
