from Code.Modele.CPersonne import CPersonne
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CForce import DeltaT
import csv
import numpy as np
import matplotlib.pyplot as plt

Mathis = CPersonne(np.array([10, 79]))
Maxime = CPersonne(np.array([8, 26]))
Hicham = CPersonne(np.array([78, 45]))
Bernard = CPersonne(np.array([120, 79]))
Louis = CPersonne(np.array([46, 26]))
moi = CPersonne(np.array([29, 45]))
lui = CPersonne(np.array([2, 79]))
il = CPersonne(np.array([89, 26]))
elle = CPersonne(np.array([160, 45]))
on = CPersonne(np.array([10, 5]))
nous = CPersonne(np.array([700, 800]))
vous = CPersonne(np.array([1000, 1000]))

listPersonnes = []


listPersonnes.append(Mathis)
listPersonnes.append(Maxime)
listPersonnes.append(Hicham)
listPersonnes.append(Bernard)
listPersonnes.append(Louis)
listPersonnes.append(lui)
listPersonnes.append(il)
listPersonnes.append(elle)
listPersonnes.append(on)
listPersonnes.append(nous)
listPersonnes.append(vous)

environnement1 = CEnvironnement("Bureau", 100, 100, np.array([600,600]), listPersonnes)

listPersonnes2 = environnement1.getListePersonnes()

for personne in listPersonnes2 :
    personne.ajouterDirection(environnement1.getSorties())

listPersonnesSorties = [True for i in range (len(listPersonnes2))]
Fini = False

listPositions = []
header = len(listPersonnes2)*["x", "y"]
with  open("../FichierSimulation/FichierPositions.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
    writer.writerow(header)
    while Fini == False:
        #ecriture des coordonnees
        for personne in listPersonnes2:
                listPositions.append(personne.RecupererDerniereCoordonne()[0])
                listPositions.append(personne.RecupererDerniereCoordonne()[1])

        writer.writerow(listPositions)
        listPositions.clear()

        #calcul des nouvelles coordonnees
        for personne in listPersonnes2:
            if listPersonnesSorties[listPersonnes2.index(personne)] == True :
                personne.CalculerForceAcceleration()
                personne.CalculerNouvellePosition()
                #On verifie si la personne est sortie ou non.
                if personne.sorti() == True:
                    listPersonnesSorties[listPersonnes2.index(personne)] = False
                    if not any(listPersonnesSorties):
                        Fini = True







"""Environnements.e1.ENVToString()
Environnements.e2.ENVToString()
Environnements.e3.ENVToString()
Environnements.e4.ENVToString()
Environnements.Environnement(1).ENVToString()"""