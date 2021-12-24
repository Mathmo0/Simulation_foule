from Code.Modele.CPersonne import CPersonne
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CForce import DeltaT
import csv
import numpy as np
import matplotlib.pyplot as plt

Mathis = CPersonne(np.array([10, 79]))
Maxime = CPersonne(np.array([8, 26]))
Hicham = CPersonne(np.array([78, 45]))

listPersonnes = []


listPersonnes.append(Mathis)
listPersonnes.append(Maxime)
listPersonnes.append(Hicham)

environnement1 = CEnvironnement("Bureau", 100, 100, np.array([10,50]), listPersonnes)

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