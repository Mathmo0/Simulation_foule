from Code.Modele import CEnvironnement as CEnvironnement

import numpy as np

class CEnvironnementController:
    """
    Classe de CEnvironnement
    """

    # -------------------Constructeur-------------------#
    """def __init__(self, nom="", hauteur=1, largeur=1, nbPersonnes=0, nbObstacles=0, sorties= np.array([(0, 0)])):
        CENV.__init__(nom, hauteur, largeur, nbPersonnes, nbObstacles, sorties)"""

    # -------------------Methodes-------------------#

print("\nLancement de la classe 2 :")

list_sorties = np.array([(3, 4), (2, 4)])

e1 = CEnvironnement.CEnvironnement("Bureau", 34, 20, 3, 1, list_sorties)
#e1 = CEnvironnement()

e1.ENVToString()
e1.tSorties[0][1] = 2
e1.ENVToString()
