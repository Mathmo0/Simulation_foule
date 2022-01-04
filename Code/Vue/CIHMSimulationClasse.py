import time
import os

from tkinter import ttk
from Code.Modele.CPersonne import CPersonne
from Code.Modele.COperation import COperation
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


class CIHMSimulationClasse:

    # -----------------Constructeur-----------------
    def __init__(self):
        # ___ Attributs de navigation ___
        self.iCurrent = 0
        self.bBackward = False
        self.bForward = False

        # ___ Attributs pour la simulation ___
        self.iForceAttraction = 0
        self.iForceRepulsion = 0
        self.iForceAcceleration = 0
        self.iTempsDeSimulation = 0

        self.CEnvironnement = CEnvironnement()

        self.FichierPosition = CFichier("../../FichierSimulation/FichierPositions")
        self.lListePosition = []
        self.lListePersonnes = []
        self.lListePersonnesSorties = [] #Liste des personnes sortie

        # ___ Attributs de fenetre ___
        """
        -----------------------  Creation de la fenetre ------------------------------
        """
        self.Window = Tk()
        self.backgroundColor = "#7fb3d5"
        self.mainMenu = Menu()
        self.Creation_Fenetre()

        """
        -----------------------  Titre  ------------------------------
        """
        self.labelTitle = Label()
        self.labelSubTitle = Label()
        self.Creation_Titres()

        """
        -----------------------  Menu  ------------------------------
        """
        self.aPropos = Label()
        self.LabelAPropos = Label()
        self.Creation_Menu()

        """
        -----------------------  Choix Fichier  ------------------------------
        """
        self.lListeEnvironnement = os.listdir('../../environnements/')
        self.lListeEnvironnement.append('Vide')
        self.sEnvironnement = ''
        self.FichierEnvironnement = CFichier()
        self.ChoixMenu = OptionMenu(self.Window, self.sEnvironnement, *self.lListeEnvironnement)
        self.Creation_Choix_Fichier()

        """
        -----------------------  Zones de saisies  ------------------------------
        """
        self.labelForceAtract = Label()
        self.labelForceRepuls = Label()
        self.labelForceAcc = Label()
        self.Creation_Zone_Saisies()

        """
        -----------------------  Zone de simulation  ------------------------------
        """
        self.iWidth = 600
        self.iHeight = 600
        self.FrameSimulation = Frame(self.Window)
        self.CanvasSimulation = Canvas(self.Window)
        self.Creation_Zone_Simulation()
        print(self.sEnvironnement.get())
        self.Window.mainloop()


    def Creation_Fenetre(self):
        self.Window['background'] = 'light gray'
        # self.window.wm_attributes("-transparentcolor", 'grey')
        self.Window.title("Simulation de foule à échelle microscopique")
        # self.window.resizable(0, 0)
        self.Window.geometry("1080x1080")
        self.Window.minsize(1080, 1080)
        self.Window.iconbitmap("../../Images/logo_polytech.ico")
        # self.window.config()

    def Creation_Menu(self):
        # TODO afficher les infos correspondantes aux boutons
        self.mainMenu = Menu(self.Window)
        #fileMenuFichier = Menu(self.mainMenu)
        self.mainMenu.add_cascade(label="à propos", command=self.A_Propos)
        self.mainMenu.add_cascade(label="?")
        self.Window.config(menu=self.mainMenu)

    def Creation_Titres(self):
        self.labelTitle = Label(self.Window,
                                text="Simulation de l'évacuation d'une foule",
                                font=("Arial", 40),
                                bg='light grey')
        self.labelSubTitle = Label(self.Window,
                                   text="Simulation à l'échelle microscopique basées sur le modèle des forces sociales de D.Helbing",
                                   font=("Arial", 15),
                                   bg='light grey')
        self.labelTitle.grid(column=0, row=0, ipadx=5, pady=5, columnspan=6, sticky='NS')
        self.labelSubTitle.grid(column=0, row=1, ipadx=5, pady=5, columnspan=6, sticky='NS')

        self.background = Label(self.Window, width=self.Window.winfo_width(), bg=self.backgroundColor)
        self.background.grid(column=0, row=2, columnspan=7)

    def Creation_Choix_Fichier(self):
        self.sEnvironnement = StringVar(self.Window)
        self.sEnvironnement.set(self.lListeEnvironnement[len(self.lListeEnvironnement) - 1])
        self.ChoixMenu = OptionMenu(self.Window, self.sEnvironnement, *self.lListeEnvironnement, command=self.Choix_Environnement)
        self.ChoixMenu.grid(column=0, row=2, sticky='E')

    def Creation_Zone_Saisies(self):
        # Force attraction
        self.Window.columnconfigure(0, minsize=0, weight=0)
        self.labelForceAtract = Label(self.Window, text="Force d'attraction (en %):", bg=self.backgroundColor)
        self.labelForceAtract.grid(column=1, row=2, sticky='E')
        self.Window.columnconfigure(1, minsize=0, weight=0)
        self.iForceAttraction = Entry(self.Window, width=3)
        self.iForceAttraction.grid(column=2, row=2, sticky='W')

        # Force répulsion
        self.Window.columnconfigure(2, minsize=0, weight=1)
        self.labelForceRepuls = Label(self.Window, text="Force de répulsion (en %):", bg=self.backgroundColor)
        self.labelForceRepuls.grid(column=3, row=2, sticky='E')
        self.Window.columnconfigure(3, minsize=0, weight=1)
        self.iForceRepulsion = Entry(self.Window, width=3)
        self.iForceRepulsion.grid(column=4, row=2, sticky='W')

        # Force accélération
        self.Window.columnconfigure(4, minsize=0, weight=1)
        self.labelForceAcc = Label(self.Window, text="Force d'accélération (en %):", bg=self.backgroundColor)
        self.labelForceAcc.grid(column=5, row=2, sticky='E')
        self.Window.columnconfigure(5, minsize=0, weight=1)
        self.iForceAcceleration = Entry(self.Window, width=3)
        self.iForceAcceleration.grid(column=6, row=2, sticky='W')

    def Creation_Zone_Simulation(self):
        self.FrameSimulation = Frame(self.Window)
        self.FrameSimulation.grid(column=0, row=3, columnspan=6, pady=10, padx=20, sticky='NS')
        self.CanvasSimulation = Canvas(self.Window, width=self.iWidth, height=self.iHeight, bg='snow', bd=1, relief=RIDGE)
        self.CanvasSimulation.grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')

        for obstacles in self.CEnvironnement.getListeObstacles():
            obstacles.calculerCoordonnees()
            CObstacleQuadrilatereVue(self.CanvasSimulation, obstacles)

        for personnes in self.CEnvironnement.getListePersonnes():
            CPersonneVue(self.CanvasSimulation, personnes.getListCoordonnees()[0][0], personnes.getListCoordonnees()[0][1], 10, 'red')


    def A_Propos(self):
        self.aPropos = Toplevel(self.Window)
        self.aPropos.resizable(0, 0)
        self.LabelAPropos = Label(self.aPropos,
                                  text="Ce projet de simulation de foule à été réalisé par Maxime EDELINE, Hicham MOUSTAQIM et Mathis MOYSE\n pendant leur quatrième année d'étude à Polytech Tours en informatique.",
                                  font=("Arial", 20),
                                  bg='light grey')

        self.LabelAPropos.grid(column=0, row=0)

    def Refresh_ListeEnvironnement(self):
        self.lListeEnvironnement = os.listdir('../../environnements/')
        self.lListeEnvironnement.append('Vide')

    #TODO rendre fonctionnel le choix de lenvironnement avec une methode
    def Choix_Environnement(self, sEnvironnement):
        print(sEnvironnement)
        if(sEnvironnement != 'Vide'):
            self.FichierEnvironnement = CFichier("../../environnements/" + sEnvironnement)
            self.CEnvironnement.CEnvironnementFichier(self.FichierEnvironnement)
            for personnes in self.CEnvironnement.getListePersonnes():
                personnes.ajouterDirection(self.CEnvironnement.getSorties())

            self.lListePersonnesSorties = [True for i in range(self.CEnvironnement.getNbPersonnes())]
            bfini = False

            self.lListePersonnes = self.CEnvironnement.getListePersonnes()
            header = len(self.lListePersonnes) * ["x", "y"]
            with  open("../../FichierSimulation/FichierPositions.csv", "w") as csv_file:
                writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
                writer.writerow(header)
                while bfini == False:
                    # ecriture des coordonnees
                    for personne in self.lListePersonnes:
                        self.lListePosition.append(personne.RecupererDerniereCoordonne()[0])
                        self.lListePosition.append(personne.RecupererDerniereCoordonne()[1])

                    writer.writerow(self.lListePosition)
                    self.lListePosition.clear()

                    # calcul des nouvelles coordonnees
                    for personne in self.lListePersonnes:
                        if self.lListePersonnesSorties[self.lListePersonnes.index(personne)] == True:

                            # Force D'acceleration :

                            personne.CalculerForceAcceleration()

                            # Force de Repulsion entre personne :

                            personne.ClearPersonneProximite()

                            # ajout des personnes proche de personne
                            for personneProx in self.lListePersonnes:

                                # pour pas qu'on ajoute elle-même dans la liste et les personnes sorti

                                if self.lListePersonnes.index(personne) != self.lListePersonnes.index(personneProx) and (
                                        self.lListePersonnesSorties[self.lListePersonnes.index(personneProx)] == True):
                                    coordper = personne.RecupererDerniereCoordonne()
                                    coordperprox = personneProx.RecupererDerniereCoordonne()
                                    if (COperation.DetectionCercle(coordper[0], coordper[1], coordperprox[0], coordperprox[1], 20) == True):
                                        personne.ajouterPersonne(personneProx)
                            print('__________iiiii : ', personne.RecupererDerniereCoordonne())
                            personne.CalculerForceRepulsion()
                            print("____REP : ", personne.getForceRepulsionPersonne().gettertForceRepulsion())
                            print('\n-------------autre------------\n')

                            # Force de Repulsion par un obstacle :
                            for obstacle in self.CEnvironnement.getListeObstacles():
                                coordPieton = personne.RecupererDerniereCoordonne()
                                sommet = personne.getForceRepulsionObstacle().FREDeterminerSommetObstacle(coordPieton,
                                                                                                          obstacle)
                                print("sommet = ", sommet)
                                if (COperation.DetectionCercle(sommet[0], sommet[1], coordPieton[0], coordPieton[1], 100) == True):
                                    personne.ajouterObstacle(obstacle)

                            personne.CalculerForceRepulsionObstacle()
                            print("____REPOBSTACLE : ", personne.getForceRepulsionObstacle().gettertForceRepulsion())
                            # Nouvelle Position:

                            personne.CalculerNouvellePosition(self.iTempsDeSimulation)

                            # On verifie si la personne est sortie ou non.
                            if personne.sorti() == True:
                                self.lListePersonnesSorties[self.lListePersonnes.index(personne)] = False
                                if not any(self.lListePersonnesSorties):
                                    bfini = True

                    self.iTempsDeSimulation += DeltaT

            #TODO AFFICHER POSITION INITIALES
            for personnes in self.lListePersonnes:
                PersonnesVUE = CPersonneVue(self.CanvasSimulation, personnes.getListCoordonnees()[0][0], personnes.getListCoordonnees()[0][1], 10, 'red')
                self.Window.update()

test = CIHMSimulationClasse()

#test.Creation_Zone_Simulation()
