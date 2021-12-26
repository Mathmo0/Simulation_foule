import time
from Code.Modele.CPersonne import CPersonne
from Code.Vue.CPersonneVue import CPersonneVue
from tkinter import *
from Code.Modele.CFichier import CFichier
from threading import Thread
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CForce import DeltaT
import csv
import numpy as np
"""
-----------------------  Creation de la fenetre ------------------------------
"""

current = 0
backward = False
forward = False

multiplicateur = float(input("Entrez un multiplicateur"))

window = Tk()

WIDTH = 500
HEIGHT = 500

main_frame= Frame(window)
main_frame.pack(fill=BOTH, expand=1)

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

def lancerSimulation(event):
    global current
    global multiplicateur
    for personne in personnes:
        personne.disparaitre()
    personnes.clear()
    window.update()
    current = 0
    #Creation des personnes et initialisation de leurs positions
    index = 0
    for current in range(0, int(nbPersonnes)):
        personne = CPersonneVue(canvas, listPositions[0][current + index], listPositions[0][current + index + 1], 10, 'red')
        personnes.append(personne)
        index += 1

    #Mouvement
    current = 0
    for current in range(0, len(listPositions)):
        window.update()
        index = 0
        for j in range(0, len(personnes)):
            personnes[j].setX(listPositions[current][j + index])
            personnes[j].setY(listPositions[current][j + index + 1])
            personnes[j].bouger()
            index += 1
        time.sleep(0.05/multiplicateur)

def iterate_back(event):
    global backward
    backward = True
    global current
    window.update()
    if (current - 1 >= 0):
        current -= 1
        index = 0
        for j in range(0, len(personnes)):
            personnes[j].setX(listPositions[current][j + index])
            personnes[j].setY(listPositions[current][j + index + 1])
            personnes[j].bouger()
            index += 1
        time.sleep(0.01)



def iterate_front(event):
    global forward
    forward = True
    global current
    window.update()
    if (current + 1 < len(listPositions)):
        current += 1
        index = 0
        for j in range(0, len(personnes)):
            personnes[j].setX(listPositions[current][j + index])
            personnes[j].setY(listPositions[current][j + index + 1])
            personnes[j].bouger()
            index += 1
        time.sleep(0.01)

def stop_iterate_back(event):
    global backward
    backward = False

def stop_iterate_front(event):
    global forward
    forward = False





bouton_back = Button(window, text='GO BACK')
bouton_back.pack(side=BOTTOM)
bouton_back.bind('<ButtonPress-1>', iterate_back)
bouton_back.bind('<ButtonRelease-1>', stop_iterate_back)

bouton_front = Button(window, text='GO FORWARD')
bouton_front.pack(side=RIGHT)
bouton_front.bind('<ButtonPress-1>', iterate_front)
bouton_front.bind('<ButtonRelease-1>', stop_iterate_front)

bouton_lancement = Button(window, text='LANCER')
bouton_lancement.pack(side=RIGHT)
bouton_lancement.bind('<ButtonPress-1>', lancerSimulation)



#Lancement
window.mainloop()