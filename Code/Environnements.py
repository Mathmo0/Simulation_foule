from Modele.CEnvironnement import CEnvironnement
from Modele.CPersonne import CPersonne
from Modele.CObstacleQuadrilatere import CObstacleQuadrilatere
import numpy as np
import csv
import re

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

"""def Environnement(choix):
    return {
        1 : CEnvironnement("Bureau", 34, 20, list_sorties, list_personnes, list_objets),
        2 : CEnvironnement("Chambre", 34, 20, list_sorties, list_personnes, list_objets),
        3 : CEnvironnement("Hall", 34, 20, list_sorties, list_personnes, list_objets),
        4 : CEnvironnement("Bureau2", 34, 20, list_sorties, list_personnes, list_objets)
    }"""

#TODO rendre cette partie de code robuste
#TODO faire la recuperation de la liste de personnes et la liste des obstacles
with open('E:\Projets\projets7_simulation\Environnements\Environnement_0.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for rew in reader:

        #recuperer le nom
        if(rew[0] == 'Nom'):
            nom = rew[1]

        #recuperer la hauteur
        elif(rew[0] == 'Hauteur'):
            hauteur = int(rew[1])

        #recuperer la largeur
        elif(rew[0] == 'Largeur'):
            largeur = int(rew[1])

        #recuperer la liste des sorties
        elif(rew[0] == 'Sortie(s)'):
            str = ""
            sorties = np.array([(0, 0) for i in range(1, len(rew))])
            for i in range(1, len(rew)):
                str = str.join(re.split("[(,)]", rew[i]))

                listeoe = [0 for i in range(2)]
                listeoe[0], listeoe[1] = str.split(" ", 1)

                listeoe[0] = int(listeoe[0])
                listeoe[1] = int(listeoe[1])

                tuplePLZ = (int(listeoe[0]), int(listeoe[1]))

                sorties[i - 1] = tuplePLZ
                str = ""

        #recuperer la liste des personnes


        #recuperer la liste des obstacles

    test = CEnvironnement(nom, hauteur, largeur, sorties, list_personnes, list_objets)
    test.ENVToString()
    test2 = CEnvironnement("Chambre", 34, 20, list_sorties, list_personnes, list_objets)
    test2.ENVToString()




