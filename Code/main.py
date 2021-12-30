from Code.Modele.CPersonne import CPersonne
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.COperation import COperation
from Code.Modele.CForce import DeltaT
import csv
import numpy as np
import matplotlib.pyplot as plt

t = 0
Mathis = CPersonne(False,np.array([100, 500]))
Maxime = CPersonne(False,np.array([500, 100]))
#Hicham = CPersonne(False,np.array([78, 45]))
Maxime.ajouterDirection(np.array([100,500]))
Mathis.ajouterDirection(np.array([500,100]))

listPersonnes = []


listPersonnes.append(Mathis)
listPersonnes.append(Maxime)
#listPersonnes.append(Hicham)


#Maxime.ajouterDirection(np.array([10,50]))

environnement1 = CEnvironnement("Bureau", 100, 100, np.array([50,50]), listPersonnes)

listPersonnes2 = environnement1.getListePersonnes()
listObstacle = environnement1.getListeObstacles()
#for personne in listPersonnes2 :
#    personne.ajouterDirection(environnement1.getSorties())

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

                    if listPersonnes2.index(personne) != listPersonnes2.index(personneProx) and (listPersonnesSorties[listPersonnes2.index(personneProx)] == True) :
                        coordper = personne.RecupererDerniereCoordonne()
                        coordperprox = personneProx.RecupererDerniereCoordonne()
                        #print(personne.__fPERVitesse)
                        if (COperation.DetectionCercle(coordper[0],coordper[1],coordperprox[0],coordperprox[1],1.34) == True) :
                            personne.ajouterPersonne(personneProx)
                #print('__________ooooo : ', len(personne.__lPERlistPersonneProximite))
                print('__________iiiii : ', personne.RecupererDerniereCoordonne())
                personne.CalculerForceRepulsion()
                #print("____ : ", personne.__vPERForceRepulsionPersonne.tForceRepulsion)
                print('\n-------------autre------------\n')

                #Force de Repulsion par un obstacle :

                for obstacle in listObstacle :
                   coordPieton = personne.RecupererDerniereCoordonne()
                   sommet = personne.getForceRepulsionObstacle().FREDeterminerSommetObstacle(coordPieton,obstacle)

                   if(COperation.DetectionCercle(sommet[0],sommet[1],coordPieton[0],coordPieton[1],1) == True) :
                       personne.ajouterObstacle(obstacle)

                personne.CalculerForceRepulsionObstacle()
                #Nouvelle Position:

                personne.CalculerNouvellePosition(t)

                #On verifie si la personne est sortie ou non.
                if personne.sorti() == True:
                    listPersonnesSorties[listPersonnes2.index(personne)] = False
                    if not any(listPersonnesSorties):
                        Fini = True

        t+=DeltaT







"""Environnements.e1.ENVToString()
Environnements.e2.ENVToString()
Environnements.e3.ENVToString()
Environnements.e4.ENVToString()
Environnements.Environnement(1).ENVToString()"""