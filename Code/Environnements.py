from Modele.CEnvironnement import CEnvironnement
import numpy as np

list_sorties = np.array([(3, 4), (2, 4)])
list_sorties2 = np.array([(3, 4), (2, 4)])
list_sorties3 = np.array([(3, 4), (2, 4)])
list_sorties4 = np.array([(3, 4), (2, 4)])



e1 = CEnvironnement("Bureau", 34, 20, 3, 1, list_sorties)
e2 = CEnvironnement("Chambre", 34, 20, 3, 1, list_sorties)
e3 = CEnvironnement("Hall", 34, 20, 3, 1, list_sorties)
e4 = CEnvironnement("Bureau2", 34, 20, 3, 1, list_sorties)
