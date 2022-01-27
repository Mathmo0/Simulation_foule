import time
import os

import numpy as np

from Code.Modele.COperation import COperation
from Code.Modele.CPersonne import CPersonne
from Code.Vue.CIHM import CIHM
from Code.Vue.CIHMBilan import CIHMBilan
from Code.Vue.CPersonneVue import CPersonneVue
from tkinter import *
from Code.Vue.CObstacleQuadrilatereVue import CObstacleQuadrilatereVue
from Code.Modele.CFichier import CFichier
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CForce import DeltaT
import csv

from Code.Vue.CSortiesVue import CSortiesVue


class CIHMSimulationClasse(CIHM):
    # -----------------Constructeur-----------------
    def __init__(self, height = 400, width = 400):

        super().__init__("Simulation de l'évacuation d'une foule")

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
        self.lListePositions = []
        self.lListePersonnes = []
        self.lListePersonnesVue = []
        self.lListePersonnesSorties = [] #Liste des personnes sortie
        self.lListeSortiesVue = []
        self.lListeObstaclesVue = []
        self.listeTest = []

        # ___ Attributs de fenetre ___
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
        self.labelForceAttract = Label()
        self.labelForceRepuls = Label()
        self.labelForceAcc = Label()
        self.Creation_Zone_Saisies()

        self.Creation_Zone_Simulation()
        print(self.sEnvironnement.get())

        """
        -----------------------  Lancement et navigation dans la simulation  ------------------------------
        """
        self.__bouton_back = Button()
        self.__bouton_front = Button()
        self.__bouton_lancement = Button()

        self.labelVitesse = Label()
        self.lListeVitesse = [0.25, 0.5, 1, 1.5, 2]
        self.fVitesse = 1
        self.menuVitesse = OptionMenu(self.Window, self.sEnvironnement, *self.lListeVitesse)

        self.Creation_Lancement_Simulation()

        """
        -----------------------  Bilan de la simulation  ------------------------------
        """
        self.Bilan:CIHMBilan = CIHMBilan
        self.__bouton_bilan = Button()
        self.Creation_Bilan()

        self.Window.mainloop()

    def Creation_Choix_Fichier(self):
        self.sEnvironnement = StringVar(self.Window)
        self.sEnvironnement.set(self.lListeEnvironnement[len(self.lListeEnvironnement) - 1])
        self.ChoixMenu = OptionMenu(self.Window, self.sEnvironnement, *self.lListeEnvironnement, command=self.Choix_Environnement)
        self.ChoixMenu.grid(column=0, row=2, sticky='E')

    #TODO RENDRE FONCTIONNEL LA SAISIS
    def Creation_Zone_Saisies(self):
        # Force attraction
        self.Window.columnconfigure(0, minsize=0, weight=0)
        self.labelForceAttract = Label(self.Window, text="Force d'attraction (en %):", bg=self.backgroundColor)
        self.labelForceAttract.grid(column=1, row=2, sticky='E')
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

    def Creation_Lancement_Simulation(self):
        # Reculer
        self.Window.columnconfigure(3, minsize=0, weight=0)
        self.__bouton_back = Button(self.Window, text='<<<')
        self.__bouton_back.grid(column=3, row=6, sticky='W')
        self.__bouton_back.bind('<ButtonPress-1>', self.iterate_back)
        self.__bouton_back.bind('<ButtonRelease-1>', self.stop_iterate_back)

        # Avancer
        self.__bouton_front = Button(self.Window, text='>>>')
        self.__bouton_front.grid(column=3, row=6, sticky='E')
        self.__bouton_front.bind('<ButtonPress-1>', self.iterate_front)
        self.__bouton_front.bind('<ButtonRelease-1>', self.stop_iterate_front)

        # Lancement simulation
        self.__bouton_lancement = Button(self.Window, text='LANCER')
        self.__bouton_lancement.grid(column=3, row=6, sticky='NS')
        self.__bouton_lancement.bind('<ButtonPress>', self.lancerSimulation)

        # Force vitesse
        self.labelVitesse = Label(self.Window, text="Vitesse de lecture : ", bg='light grey')
        self.labelVitesse.grid(column=3, row=5, sticky='E', pady=10)
        self.Window.columnconfigure(5, minsize=0, weight=1)

        self.fVitesse = StringVar(self.Window)
        self.fVitesse.set(self.lListeVitesse[2])
        self.menuVitesse = OptionMenu(self.Window, self.fVitesse, *self.lListeVitesse)
        self.menuVitesse.grid(column=4, row=5, sticky='W')

    def Creation_Bilan(self):
        self.__bouton_bilan.config(state=DISABLED, text="Bilan", command=self.AffichageBilan)
        self.__bouton_bilan.grid(column=5, row=6, sticky='W')

    def AffichageBilan(self):
        self.Bilan = CIHMBilan(self.listeTest)

    def mouvement(self):
        """
        Fonction permettant d'actualiser la position des personnes.

        @param : multiplicateur qui permet de moduler la vitesse de la simulation
        @return : rien
        """
        index = 0
        for j in range(0, len(self.lListePersonnesVue)):
            self.personne = CPersonne(False, np.array([self.lListePositions[self.iCurrent][j + index], self.lListePositions[self.iCurrent][j + index + 1]]))
            self.personne.ajouterDirection(self.CEnvironnement.getSorties()[0])
            if self.personne.sorti() == False :
                self.lListePersonnesVue[j].setX(self.lListePositions[self.iCurrent][j + index])
                self.lListePersonnesVue[j].setY(self.lListePositions[self.iCurrent][j + index + 1])
                self.lListePersonnesVue[j].setPression(self.lListePositions[self.iCurrent][j + index + 2])
                self.lListePersonnesVue[j].move()
            else:
                self.lListePersonnesVue[j].setColor("")
                self.lListePersonnesVue[j].move()
            index += 2
        time.sleep(0.05 / float(self.fVitesse.get()))

    def lancerSimulation(self, event):
        """
        Fonction permettant de lancer la simulation.

        @return : rien
        """
        for personne in self.lListePersonnesVue:
            personne.disparaitre()

        self.lListePersonnesVue.clear()

        """
        ------------------------- Recuperation des coordonees -------------------------
        """
        monFichier = CFichier("../../FichierSimulation/FichierPositions.csv")
        self.lListePositions = monFichier.LireFichierPosition()
        self.listeTest = self.lListePositions

        # On obtient le nombre de personnes grace aux colonnes du fichier csv

        if not (self.__bouton_lancement['state'] == DISABLED):
            self.__bouton_lancement.config(state=DISABLED)
            self.__bouton_bilan.config(state=DISABLED)
            self.__bouton_back.config(state=DISABLED)
            self.__bouton_front.config(state=DISABLED)
            #for personne in self.lListePersonnes:
                #personne.disparaitre()
            self.lListePersonnes.clear()
            self.Window.update()
            self.iCurrent = 0
            # Creation des personnes et initialisation de leurs positions
            index = 0
            for self.iCurrent in range(0, int(self.CEnvironnement.getNbPersonnes())):
                personne = CPersonneVue(self.CanvasSimulation, self.lListePositions[0][self.iCurrent + index], self.lListePositions[0][self.iCurrent + index + 1], 5)
                self.lListePersonnesVue.append(personne)
                index += 2

            # Mouvement
            self.iCurrent = 0
            for self.iCurrent in range(0, len(self.lListePositions)):
                self.Window.update()
                self.mouvement()
            self.__bouton_lancement.config(state=NORMAL)
            self.__bouton_bilan.config(state=NORMAL)
            self.__bouton_back.config(state=NORMAL)
            self.__bouton_front.config(state=NORMAL)

    def iterate_back(self, event):
        """
        Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "reculer"

        @return : rien
        """
        self.bBackward = True
        while (self.iCurrent - 1 >= 0 and (self.bBackward == True)):
            self.Window.update()
            self.iCurrent -= 1
            self.mouvement()

    def iterate_front(self, event):
        """
        Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "avancer"

        @return : rien
        """
        self.bForward = True
        while (self.iCurrent + 1 < len(self.lListePositions) and (self.bForward == True)):
            self.Window.update()
            self.iCurrent += 1
            self.mouvement()

    def stop_iterate_back(self, event):
        self.bBackward = False

    def stop_iterate_front(self, event):
        self.bForward = False

    def Refresh_ListeEnvironnement(self):
        self.lListeEnvironnement = os.listdir('../../environnements/')
        self.lListeEnvironnement.append('Vide')

    #TODO rendre fonctionnel le choix de lenvironnement avec une methode
    def Choix_Environnement(self, sEnvironnement):
        print(sEnvironnement)
        self.Clear()
        self.__bouton_lancement.config(state=DISABLED)
        self.__bouton_front.config(state=DISABLED)
        self.__bouton_back.config(state=DISABLED)
        self.__bouton_bilan.config(state=DISABLED)
        if(sEnvironnement != 'Vide'):
            self.LabelChargement = Label(self.Window, text="Chargement... ", bg='light grey')
            self.LabelChargement.grid(column=0, row=5, ipadx=5, pady=5, columnspan=2)

            self.FichierEnvironnement = CFichier("../../environnements/" + sEnvironnement)
            self.CEnvironnement.CEnvironnementFichier(self.FichierEnvironnement)
            for personnes in self.CEnvironnement.getListePersonnes():
                personnes.ajouterDirection(self.CEnvironnement.getSorties())

            self.lListePersonnesSorties = [True for i in range(self.CEnvironnement.getNbPersonnes())]
            bfini = False

            self.lListePersonnes = self.CEnvironnement.getListePersonnes()

            #Affichage de la position initiale
            for personnes in self.lListePersonnes:
                personne = CPersonneVue(self.CanvasSimulation, personnes.getListCoordonnees()[0][0], personnes.getListCoordonnees()[0][1], 5)
                self.lListePersonnesVue.append(personne)
                self.Window.update()

            #Affichage des obstacles
            for obstacles in self.CEnvironnement.getListeObstacles():
                obstacle = CObstacleQuadrilatereVue(self.CanvasSimulation, obstacles)
                self.lListeObstaclesVue.append(obstacle)
                self.Window.update()

            for sortie in self.CEnvironnement.getSorties():
                sortie = CSortiesVue(self.CanvasSimulation, sortie)
                self.lListeSortiesVue.append(sortie)
                self.Window.update()

            header = len(self.lListePersonnes) * ["x", "y", "pression"]

            with  open("../../FichierSimulation/FichierPositions.csv", "w") as csv_file:
                writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
                writer.writerow(header)
                while bfini == False and self.iTempsDeSimulation <= 5000:
                    print(self.iTempsDeSimulation)
                    if self.lListePersonnes == []:
                        bfini = True

                    # ecriture des coordonnees
                    for personne in self.lListePersonnes:
                        self.lListePositions.append(personne.RecupererDerniereCoordonne()[0])
                        self.lListePositions.append(personne.RecupererDerniereCoordonne()[1])
                        self.lListePositions.append(personne.getPression())

                    writer.writerow(self.lListePositions)
                    self.lListePositions.clear()

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
                            #print('__________Position : ', personne.RecupererDerniereCoordonne())
                            personne.CalculerForceRepulsion()
                            #print("____REP : ", personne.getForceRepulsionPersonne().gettertForceRepulsion())
                            #personne.CalculForceAttraction(self.iTempsDeSimulation)
                            #print("____REPAttraction : ", personne.getForceAttraction().getValeurForceAttraction())

                            #print('\n-------------autre------------\n')

                            # Force de Repulsion par un obstacle :
                            for obstacle in self.CEnvironnement.getListeObstacles():
                                coordPieton = personne.RecupererDerniereCoordonne()
                                sommet = personne.getForceRepulsionObstacle().FREDeterminerSommetObstacleQuadrilatere(coordPieton,
                                                                                                                      obstacle)
                                #print("sommet = ", sommet)
                                if (COperation.DetectionCercle(sommet[0], sommet[1], coordPieton[0], coordPieton[1], 10) == True):
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


            self.__bouton_lancement.config(state=NORMAL)
            self.__bouton_front.config(state=NORMAL)
            self.__bouton_back.config(state=NORMAL)
            self.LabelChargement.config(text='')

            self.__bouton_bilan.config(state=NORMAL)

    def Clear(self):
        # ___ Attributs de navigation ___
        self.iCurrent = 0
        self.bBackward = False
        self.bForward = False
        self.iTempsDeSimulation = 0

        self.lListePositions.clear()
        self.lListePersonnes.clear()
        self.lListePersonnesVue.clear()
        self.lListeObstaclesVue.clear()
        self.lListePersonnesSorties.clear()

        self.Creation_Zone_Simulation()

test = CIHMSimulationClasse()
