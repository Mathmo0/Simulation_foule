import time
import os

from tkinter import ttk
from Code.Modele.CPersonne import CPersonne
from Code.Vue.CPersonneVue import CPersonneVue
from tkinter import *
from Code.Modele.CObstacleQuadrilatere import CObstacleQuadrilatere
from Code.Vue.CObstacleQuadrilatereVue import CObstacleQuadrilatereVue
from Code.Modele.CFichier import CFichier
from threading import Thread
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CForce import DeltaT
import csv
import numpy as np

"""
------------------------- Recuperation des coordonees -------------------------
"""
monFichier = CFichier("../../FichierSimulation/FichierPositions.csv")
listPositions = monFichier.LireFichierPosition()

#On obtient le nombre de personnes grace aux colonnes du fichier csv
nbPersonnes = len(listPositions[0])/2
print("list position = ",listPositions)
personnes = []


"""
---------------Carte de Chaleur -------------------------
"""
listCarteChaleur = [400][400]
for uiBoucle1 in range(399) :
    for uiBoucle2 in range(399) :
        listCarteChaleur[uiBoucle1][uiBoucle2] = 0




#----------------------------------------- Fonctions --------------------------------------------------------------------
def A_Propos():
    aPropos = Toplevel(window)
    aPropos.resizable(0, 0)
    LabelAPropos = Label(aPropos, text="Ce projet de simulation de foule à été réalisé par Maxime EDELINE, Hicham MOUSTAQIM et Mathis MOYSE\n pendant leur quatrième année d'étude à Polytech Tours en informatique.", font=("Arial", 20), bg='light grey')
    LabelAPropos.grid(column=0, row=0)

def Choix_Environnement(variable):
    print(variable)



def mouvement(multi):
    """
    Fonction permettant d'actualiser la position des personnes.

    @param : multiplicateur qui permet de moduler la vitesse de la simulation
    @return : rien
    """
    index = 0
    for j in range(0, len(personnes)):
        personnes[j].setX(listPositions[current][j + index])
        personnes[j].setY(listPositions[current][j + index + 1])
        personnes[j].move()
        index += 1
    time.sleep(0.5/multi)


def lancerSimulation(event):
    """
    Fonction permettant de lancer la simulation.

    @return : rien
    """
    if not (bouton_lancement['state'] == DISABLED):
        bouton_lancement.config(state=DISABLED)
        bouton_front.config(state=DISABLED)
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
            mouvement(10)
        bouton_lancement.config(state=NORMAL)
        bouton_back.config(state=NORMAL)
        bouton_front.config(state=NORMAL)

def iterate_back(event):
    """
    Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "reculer"

    @return : rien
    """
    global multiplicateur
    global backward
    backward = True
    global current
    while(current - 1 >= 0 and (backward == True)):
        window.update()
        current -= 1
        mouvement(10)

def iterate_front(event):
    """
    Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "avancer"

    @return : rien
    """
    global multiplicateur
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

def menu_fichier(event):
    listeEnvironnement = os.listdir('../../environnements/')
#-----------------------------------------------------------------------------------------------------------------------

"""
-----------------------  Creation de la fenetre ------------------------------
"""
current = 0
backward = False
forward = False
backgroundColor = "#7fb3d5"
multiplicateur = 1


window = Tk()
window['background']='light gray'
#window.wm_attributes("-transparentcolor", 'grey')
window.title("Simulation de foule à échelle microscopique")
#window.resizable(0, 0)
window.geometry("800x800")
window.minsize(800, 800)
window.iconbitmap("../../Images/logo_polytech.ico")
#window.config()


"""
-----------------------  Titre  ------------------------------
"""
labelTitle = Label(window, text="Simulation de l'évacuation d'une foule", font=("Arial", 40), bg='light grey')
labelSubTitle = Label(window, text="Simulation à l'échelle microscopique basées sur le modèle des forces sociales de D.Helbing", font=("Arial", 15), bg='light grey')
labelTitle.grid(column=0, row=0, ipadx=5, pady=5, columnspan=6, sticky='NS')
labelSubTitle.grid(column=0, row=1, ipadx=5, pady=5, columnspan=6, sticky='NS')

background = Label(window, width=window.winfo_width(), bg=backgroundColor)
background.grid(column=0, row=2, columnspan=7)
"""
-----------------------  Menu  ------------------------------
"""
#TODO afficher les infos correspondantes aux boutons
mainMenu = Menu(window)
fileMenuFichier = Menu(mainMenu)
mainMenu.add_cascade(label="?")
mainMenu.add_cascade(label="à propos", command=A_Propos)

"""
-----------------------  Choix Fichier  ------------------------------
"""
#TODO rendre fonctionnel le choix de lenvironnement avec une methode
listeEnvironnement = os.listdir('../../environnements/')
listeEnvironnement.append('Vide')
variable = StringVar(window)
variable.set(listeEnvironnement[len(listeEnvironnement) - 1])
var = str(variable.get())
opt = OptionMenu(window, variable, *listeEnvironnement, command=Choix_Environnement)
opt.grid(column=0, row=2, sticky='E')
#print(variable.get())
"""
-----------------------  Zones de saisies  ------------------------------
"""
#TODO récupérer les valeurs dans des variables et en faire qqchose
#Force attraction
window.columnconfigure(0, minsize=0, weight=0)
labelForceAtract = Label(window, text="Force d'attraction (en %):", bg=backgroundColor)
labelForceAtract.grid(column=1, row=2, sticky='E')
window.columnconfigure(1, minsize=0, weight=0)
ForceAtract = Entry(window, width=3)
ForceAtract.grid(column=2, row=2, sticky='W')

#Force répulsion
window.columnconfigure(2, minsize=0, weight=1)
labelForceRepuls = Label(window, text="Force de répulsion (en %):", bg=backgroundColor)
labelForceRepuls.grid(column=3, row=2, sticky='E')
window.columnconfigure(3, minsize=0, weight=1)
ForceRepuls = Entry(window, width=3)
ForceRepuls.grid(column=4, row=2, sticky='W')

#Force accélération
window.columnconfigure(4, minsize=0, weight=1)
labelForceAcc = Label(window, text="Force d'accélération (en %):", bg=backgroundColor)
labelForceAcc.grid(column=5, row=2, sticky='E')
window.columnconfigure(5, minsize=0, weight=1)
ForceAcc = Entry(window, width=3)
ForceAcc.grid(column=6, row=2, sticky='W')

"""
-----------------------  Zone de simulation  ------------------------------
"""
WIDTH = 400
HEIGHT = 400

main_frame= Frame(window)
#main_frame.pack(fill=BOTH, expand=1)
main_frame.grid(column=0, row=3, columnspan=6, pady=10, padx=20, sticky='NS')

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='snow', bd=1, relief=RIDGE)
#canvas.pack(expand=YES)
canvas.grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')

table = CObstacleQuadrilatere(10, 400, np.array([300,300]))
table.calculerCoordonnees()
vueTable = CObstacleQuadrilatereVue(canvas, table)

table2 = CObstacleQuadrilatere(100, 100, np.array([250,250]))
table2.calculerCoordonnees()
vueTable2 = CObstacleQuadrilatereVue(canvas, table2)

"""
-----------------------  Lancement et navigation dans la simulation  ------------------------------
"""
window.columnconfigure(3, minsize=0, weight=0)
bouton_back = Button(window, text='<<<')
bouton_back.grid(column=3, row=6, sticky='W')
bouton_back.bind('<ButtonPress-1>', iterate_back)
bouton_back.bind('<ButtonRelease-1>', stop_iterate_back)

bouton_front = Button(window, text='>>>')
bouton_front.grid(column=3, row=6, sticky='E')
bouton_front.bind('<ButtonPress-1>', iterate_front)
bouton_front.bind('<ButtonRelease-1>', stop_iterate_front)

bouton_lancement = Button(window, text='LANCER')
bouton_lancement.grid(column=3, row=6, sticky='NS')
bouton_lancement.bind('<ButtonPress>', lancerSimulation)
window.bind('<space>',lancerSimulation)

#Force vitesse
labelmultiplicateur = Label(window, text="Vitesse de lecture : ", bg='light grey')
labelmultiplicateur.grid(column=3, row=5, sticky='E', pady=10)
window.columnconfigure(5, minsize=0, weight=1)
listeVitesse = [0.25, 0.5, 1, 1.5, 2]
variable = StringVar(window)
variable.set(listeVitesse[2])
opt = OptionMenu(window, variable, *listeVitesse)
opt.grid(column=4, row=5, sticky='W')


#Lancement
window.config(menu=mainMenu)
window.mainloop()
