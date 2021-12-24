import time
from Code.Modele.CPersonne import CPersonne
from Code.Vue.CPersonneVue import CPersonneVue
from tkinter import *
from Code.Modele.CFichier import CFichier
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CForce import DeltaT
import csv
import numpy as np
"""
-----------------------  Creation de la fenetre ------------------------------
"""
window = Tk()

WIDTH = 1000
HEIGHT = 1000

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='snow')
canvas.pack()

"""
------------------------- Recuperation des coordonees -------------------------
"""
monFichier = CFichier("../../FichierSimulation/FichierPositions")
listPositions = monFichier.LireFichierPosition()

#On obtient le nombre de personnes grace aux colonnes du fichier csv
nbPersonnes = len(listPositions[0])/2
print(listPositions)
personnes = []

#Creation des personnes et initialisation de leurs positions
index = 0
for i in range(0, int(nbPersonnes)):
    personne = CPersonneVue(canvas, listPositions[0][i + index], listPositions[0][i + index + 1], 10, 'red')
    personnes.append(personne)
    index += 1

#Mouvement
for i in range(0, len(listPositions)):
    window.update()
    index = 0
    for j in range(0, len(personnes)):
        personnes[j].setX(listPositions[i][j + index])
        personnes[j].setY(listPositions[i][j + index + 1])
        personnes[j].bouger()
        index += 1
    time.sleep(0.01)


#Lancement
window.mainloop()