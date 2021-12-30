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
backgroundColor = "#7fb3d5"

#multiplicateur = float(input("Entrez un multiplicateur"))

window = Tk()
window['background']='light gray'
#window.wm_attributes("-transparentcolor", 'grey')
window.title("Simulation de foule à échelle microscopique")
#window.resizable(0, 0)
window.geometry("1080x1080")
window.minsize(1080, 1080)
window.iconbitmap("../../Images/logo_polytech.ico")
window.config()


"""
-----------------------  Titre  ------------------------------
"""
labelTitle = Label(window, text="Simulation de l'évacuation d'une foule", font=("Arial", 40), bg='light grey')
labelSubTitle = Label(window, text="Simulation à l'échelle microscopique basées sur le modèle des forces sociales de D.Helbing", font=("Arial", 15), bg='light grey')
labelTitle.grid(column=0, row=0, ipadx=5, pady=5, columnspan=8, sticky='NS')
labelSubTitle.grid(column=0, row=1, ipadx=5, pady=5, columnspan=8, sticky='NS')

background = Label(window, width=window.winfo_width(), bg=backgroundColor)
background.grid(column=0, row=2, columnspan=7)
"""
-----------------------  Boutons  ------------------------------
"""
#Button : Fichier
window.columnconfigure(0, minsize=0, weight=1)
buttonFichier = Button(window, text="Fichier", font=("Arial", 10), bg='White', fg='Black')
buttonFichier.grid(column=0, row=2, sticky='W')

#Button : ?
window.columnconfigure(1, minsize=0, weight=1)
buttonInfos = Button(window, text="?", font=("Arial", 10), bg='White', fg='Black')
buttonInfos.grid(column=0, row=2, sticky='E')


"""
-----------------------  Zones de saisies  ------------------------------
"""
#Force attraction
window.columnconfigure(2, minsize=0, weight=1)
labelForceAtract = Label(window, text="Force d'attraction (en %):", bg=backgroundColor)
labelForceAtract.grid(column=1, row=2, sticky='E')
window.columnconfigure(3, minsize=0, weight=1)
ForceAtract = Entry(window, width=3)
ForceAtract.grid(column=2, row=2, sticky='W')

#Force répulsion
window.columnconfigure(4, minsize=0, weight=1)
labelForceRepuls = Label(window, text="Force de répulsion (en %):", bg=backgroundColor)
labelForceRepuls.grid(column=3, row=2, sticky='E')
window.columnconfigure(5, minsize=0, weight=1)
ForceRepuls = Entry(window, width=3)
ForceRepuls.grid(column=4, row=2, sticky='W')

#Force accélération
window.columnconfigure(6, minsize=0, weight=1)
labelForceAcc = Label(window, text="Force d'accélération (en %):", bg=backgroundColor)
labelForceAcc.grid(column=5, row=2, sticky='E')
window.columnconfigure(7, minsize=0, weight=1)
ForceAcc = Entry(window, width=3)
ForceAcc.grid(column=6, row=2, sticky='W')


"""
-----------------------  Zone de simulation  ------------------------------
"""
WIDTH = 800
HEIGHT = 800

main_frame= Frame(window)
#main_frame.pack(fill=BOTH, expand=1)
main_frame.grid(column=1, row=3, columnspan=5)

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='snow', bd=1, relief=RIDGE)
#canvas.pack(expand=YES)
canvas.grid(column=1, row=3, columnspan=5)


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


"""
-----------------------  Lancement et navigation dans la simulation  ------------------------------
"""
bouton_back = Button(window, text='<<<')
bouton_back.grid(column=3, row=5, sticky='W')
bouton_back.bind('<ButtonPress-1>', iterate_back)
bouton_back.bind('<ButtonRelease-1>', stop_iterate_back)

bouton_front = Button(window, text='>>>')
bouton_front.grid(column=3, row=5, sticky='E')
bouton_front.bind('<ButtonPress-1>', iterate_front)
bouton_front.bind('<ButtonRelease-1>', stop_iterate_front)

bouton_lancement = Button(window, text='LANCER')
bouton_lancement.grid(column=3, row=5, sticky='NS')
bouton_lancement.bind('<ButtonPress-1>', lancerSimulation)



#Lancement
window.mainloop()
