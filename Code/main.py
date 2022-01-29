from Code.Modele.CFichier import CFichier
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere
from Code.Modele.CPersonne import CPersonne
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.COperation import COperation
from Code.Modele.CForce import DeltaT
import csv
import numpy as np
import matplotlib.pyplot as plt

t = 0
Mathis = CPersonne(False,np.array([200, 175]))
Maxime = CPersonne(False,np.array([40, 40]))
Hicham = CPersonne(False,np.array([400, 0]))
Killian = CPersonne(False,np.array([250,280]))
Bernard = CPersonne(False,np.array([120, 79]))
Louis = CPersonne(False,np.array([46, 26]))
moi = CPersonne(False,np.array([29, 45]))
lui = CPersonne(False,np.array([2, 79]))
il = CPersonne(False,np.array([89, 26]))
elle = CPersonne(False,np.array([160, 45]))
on = CPersonne(False,np.array([10, 5]))

'''
Maxime.ajouterDirection(np.array([0,0]))
Mathis.ajouterDirection(np.array([200,250]))
Hicham.ajouterDirection(np.array([0,400]))
Killian.ajouterDirection(np.array([400,400]))
'''

listPersonnes = []

listPersonnes.append(Bernard)
listPersonnes.append(Louis)
listPersonnes.append(lui)
listPersonnes.append(il)
listPersonnes.append(elle)
listPersonnes.append(on)
listPersonnes.append(Mathis)
listPersonnes.append(Maxime)
listPersonnes.append(Hicham)
listPersonnes.append(Killian)

'''
Bernard.ajouterDirection(np.array([400,400]))
Louis.ajouterDirection(np.array([400,400]))
lui.ajouterDirection(np.array([400,400]))
il.ajouterDirection(np.array([400,400]))
elle.ajouterDirection(np.array([400,400]))
on.ajouterDirection(np.array([400,400]))
Mathis.ajouterDirection(np.array([400,400]))
Maxime.ajouterDirection(np.array([400,400]))
Hicham.ajouterDirection(np.array([400,400]))
Killian.ajouterDirection(np.array([400,400]))
'''


table = CObstacleQuadrilatere(10, 400, np.array([300,300]))
table.OBQcalculerCoordonnees()

table2 = CObstacleQuadrilatere(100, 100, np.array([150,150]))
table2.OBQcalculerCoordonnees()

listObstacles = [] #[table, table2]

#Maxime.ajouterDirection(np.array([10,50]))

environnement1 = CEnvironnement("Bureau", 100, 100, np.array([400,400]), listPersonnes, listObstacles)
#fichier = CFichier("../environnements/Environnement_0")

#environnement1 = CEnvironnement()
#environnement1.CEnvironnementFichier(fichier)

listPersonnes2 = environnement1.getListePersonnes()
listObstacle = environnement1.getListeObstacles()
print(listObstacle)
#for personne in listPersonnes2 :
#   personne.ajouterDirection(environnement1.getSorties())

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
                listPositions.append(personne.PERRecupererDerniereCoordonne()[0])
                listPositions.append(personne.PERRecupererDerniereCoordonne()[1])

        writer.writerow(listPositions)
        listPositions.clear()

        #calcul des nouvelles coordonnees
        for personne in listPersonnes2:
            if listPersonnesSorties[listPersonnes2.index(personne)] == True :

                #Force D'acceleration :

                personne.PERCalculerForceAcceleration()

                #Force de Repulsion entre personne :

                personne.PERClearPersonneProximite()

                    #ajout des personnes proche de personne
                for personneProx in listPersonnes2 :

                    #pour pas qu'on ajoute elle-même dans la liste et les personnes sorti

                    if listPersonnes2.index(personne) != listPersonnes2.index(personneProx) and (listPersonnesSorties[listPersonnes2.index(personneProx)] == True) :
                        coordper = personne.PERRecupererDerniereCoordonne()
                        coordperprox = personneProx.PERRecupererDerniereCoordonne()
                        if (COperation.OPEDetectionCercle(coordper[0], coordper[1], coordperprox[0], coordperprox[1], 20) == True) :
                            personne.PERajouterPersonne(personneProx)
                print('__________iiiii : ', personne.PERRecupererDerniereCoordonne())
                personne.PERCalculerForceRepulsion()
                print("____REP : ", personne.PERgetForceRepulsionPersonne().FREgettertForceRepulsion())
                print('\n-------------autre------------\n')

                #Force de Repulsion par un obstacle :

                personne.PERClearlistObstacleProx()

                for obstacle in listObstacle :
                   coordPieton = personne.PERRecupererDerniereCoordonne()
                   sommet = personne.PERgetForceRepulsionObstacle().FREDeterminerSommetObstacleQuadrilatere(coordPieton, obstacle)
                   print("sommet = ",sommet)
                   if(COperation.OPEDetectionCercle(sommet[0], sommet[1], coordPieton[0], coordPieton[1], 10) == True) :
                       personne.PERajouterObstacle(obstacle)

                personne.PERCalculerForceRepulsionObstacle()
                print("____REPOBSTACLE : ", personne.PERgetForceRepulsionObstacle().FREgettertForceRepulsion())
                #Nouvelle Position:

                personne.PERCalculerNouvellePosition(t)

                #On verifie si la personne est sortie ou non.
                if personne.PERsorti() == True:
                    listPersonnesSorties[listPersonnes2.index(personne)] = False
                    if not any(listPersonnesSorties):
                        Fini = True

        t+=DeltaT







"""Environnements.e1.ENVToString()
Environnements.e2.ENVToString()
Environnements.e3.ENVToString()
Environnements.e4.ENVToString()
Environnements.Environnement(1).ENVToString()"""
