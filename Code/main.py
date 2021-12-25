from Code.Modele.CPersonne import CPersonne
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.COperation import COperation
from Code.Modele.CForce import DeltaT
import csv
import numpy as np
import matplotlib.pyplot as plt

Mathis = CPersonne(False,np.array([10, 79]))
Maxime = CPersonne(False,np.array([8, 26]))
Hicham = CPersonne(False,np.array([78, 45]))
Bernard = CPersonne(False,np.array([120, 79]))
Louis = CPersonne(False,np.array([46, 26]))
moi = CPersonne(False,np.array([29, 45]))
lui = CPersonne(False,np.array([2, 79]))
il = CPersonne(False,np.array([89, 26]))
elle = CPersonne(False,np.array([160, 45]))
on = CPersonne(False,np.array([10, 5]))
nous = CPersonne(False,np.array([700, 800]))
vous = CPersonne(False,np.array([1000, 1000]))

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

                #Force D'acceleration :

                personne.CalculerForceAcceleration()

                #Force de Repulsion entre personne :

                personne.ClearPersonneProximite()

                    #ajout des personnes proche de personne
                for personneProx in listPersonnes2 :

                    #pour pas qu'on ajoute elle-même dans la liste et les personnes sorti

                    if listPersonnes2.index(personne) != listPersonnes2.index(personneProx) :
                        coordper = personne.RecupererDerniereCoordonne()
                        coordperprox = personneProx.RecupererDerniereCoordonne()
                        if (COperation.DetectionCercle(coordper[0],coordper[1],coordperprox[0],coordperprox[1],5) == True) and (listPersonnesSorties[listPersonnes2.index(personneProx)] == True) :
                            personne.ajouterPersonne(personneProx)

                personne.CalculerForceRepulsion()

                #Force de Repulsion par un obstacle :

                #Nouvelle Position:

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