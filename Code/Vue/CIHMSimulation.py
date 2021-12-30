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

#multiplicateur = float(input("Entrez un multiplicateur"))

window = Tk()
window['background']='light gray'
#window.wm_attributes("-transparentcolor", 'grey')
window.title("Simulation de foule à échelle microscopique")
window.resizable(0, 0)
window.geometry("1080x1080")
window.iconbitmap("../../Images/logo_polytech.ico")
window.config()

"""
-----------------------  Titre  ------------------------------
"""
labelTitle = Label(window, text="Simulation de l'évacuation d'une foule", font=("Arial", 40), bg='light grey')
labelSubTitle = Label(window, text="Simulation à l'échelle microscopique basées sur le modèle des forces sociales de D.Helbing", font=("Arial", 15), bg='light grey')
labelTitle.grid(column=0, row=0, ipadx=5, pady=5, columnspan=3, sticky='S')
labelSubTitle.grid(column=0, row=1, ipadx=5, pady=5, columnspan=3, sticky='S')

"""
-----------------------  Boutons  ------------------------------
"""
#frame = Frame(window, bg='white')
buttonFichier = Button(window, text="Fichier", font=("Arial", 10), bg='White', fg='Black')
#buttonFichier
buttonFichier.grid(column=0, row=2, ipadx=5, pady=5, sticky='E')
#frame.pack()
#frame.grid(column=0, row=0, ipadx=5, pady=5, sticky='W' + 'N')

buttonInfos = Button(window, text="?", font=("Arial", 10), bg='White', fg='Black')
buttonInfos.grid(column=1, row=2, ipadx=5, pady=5, sticky='W')

"""
-----------------------  Zones de saisies  ------------------------------
"""
labelForceAtract = Label(window, text="Force d'attraction (en %):")
labelForceAtract.grid(column=2, row=2, ipadx=5, pady=5, sticky='w')
ForceAtract = Entry(window, width=3)
ForceAtract.grid(column=3, row=2, ipadx=5, pady=5, sticky='E')

WIDTH = 500
HEIGHT = 500

main_frame= Frame(window)
#main_frame.pack(fill=BOTH, expand=1)
main_frame.grid(column=0, row=3, ipadx=5, columnspan=3, pady=5)

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='snow', bd=1, relief=RIDGE)
#canvas.pack(expand=YES)
canvas.grid(column=0, row=3, ipadx=5, columnspan=3, pady=5)

"""
------------------------- Recuperation des coordonees -------------------------
"""
monFichier = CFichier("../../FichierSimulation/FichierPositions")
listPositions = monFichier.LireFichierPosition()

#On obtient le nombre de personnes grace aux colonnes du fichier csv
nbPersonnes = len(listPositions[0])/2
print(listPositions)
personnes = []

"""
Fonction permettant d'actualiser la position des personnes.
"""
def mouvement(multi):
    index = 0
    for j in range(0, len(personnes)):
        personnes[j].setX(listPositions[current][j + index])
        personnes[j].setY(listPositions[current][j + index + 1])
        personnes[j].move()
        index += 1
    time.sleep(0.05 / multiplicateur)

"""
Fonction permettant de lancer la simulation.
"""
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
        mouvement(multiplicateur)

"""
Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "reculer"
"""
def iterate_back(event):
    global backward
    backward = True
    global current
    while(current - 1 >= 0 and (backward == True)):
        window.update()
        current -= 1
        mouvement(10)

"""
Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "avancer"
"""
def iterate_front(event):
    global forward
    forward = True
    global current
    while(current + 1 < len(listPositions) and (forward == True)):
        window.update()
        current += 1
        mouvement(10)

def stop_iterate_back(event):
    global backward
    backward = False


def stop_iterate_front(event):
    global forward
    forward = False



bouton_back = Button(window, text='<<<')
#bouton_back.pack(side=BOTTOM)
bouton_back.grid(column=0, row=5, ipadx=5, pady=5, sticky='E')
bouton_back.bind('<ButtonPress-1>', iterate_back)
bouton_back.bind('<ButtonRelease-1>', stop_iterate_back)

bouton_front = Button(window, text='>>>')
#bouton_front.pack(side=RIGHT)
bouton_front.grid(column=2, row=5, ipadx=5, pady=5, sticky='W')
bouton_front.bind('<ButtonPress-1>', iterate_front)
bouton_front.bind('<ButtonRelease-1>', stop_iterate_front)

bouton_lancement = Button(window, text='LANCER')
#bouton_lancement.pack(side=RIGHT)
bouton_lancement.grid(column=1, row=5, ipadx=5, pady=5)
bouton_lancement.bind('<ButtonPress-1>', lancerSimulation)



#Lancement
window.mainloop()
