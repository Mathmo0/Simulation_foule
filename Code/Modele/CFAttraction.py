import numpy as np
from Code.Modele.CForce import CForce

class CFAttraction(CForce) :

    def __init__(self,ValeurForceAttraction = np.array([0.0,0.0])) :
        self.ValeurForceAttraction = ValeurForceAttraction


