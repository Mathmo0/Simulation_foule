from Modele.CEnvironnement import CEnvironnement
from Modele.CPersonne import CPersonne
from Modele.CObstacleQuadrilatere import CObstacleQuadrilatere
import numpy as np

list_sorties = np.array([(3, 4), (2, 4)])
list_sorties2 = np.array([(3, 4), (2, 4)])
list_sorties3 = np.array([(3, 4), (2, 4)])
list_sorties4 = np.array([(3, 4), (2, 4)])

list_personnes = np.array([CPersonne() for i in range(10)])
list_objets = np.array([CObstacleQuadrilatere() for i in range(4)])

"""e1 = CEnvironnement("Bureau", 34, 20, list_sorties, list_personnes, list_objets)
e2 = CEnvironnement("Chambre", 34, 20, list_sorties, list_personnes, list_objets)
e3 = CEnvironnement("Hall", 34, 20, list_sorties, list_personnes, list_objets)
e4 = CEnvironnement("Bureau2", 34, 20, list_sorties, list_personnes, list_objets)"""

def Environnement(choix):
    return {
        1 : CEnvironnement("Bureau", 34, 20, list_sorties, list_personnes, list_objets),
        2 : CEnvironnement("Chambre", 34, 20, list_sorties, list_personnes, list_objets),
        3 : CEnvironnement("Hall", 34, 20, list_sorties, list_personnes, list_objets),
        4 : CEnvironnement("Bureau2", 34, 20, list_sorties, list_personnes, list_objets)
    }
