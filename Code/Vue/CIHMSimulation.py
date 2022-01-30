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


class CIHMSimulation(CIHM):
    # -----------------Constructeur-----------------
    def __init__(self, height = 400, width = 400):

        super().__init__("Simulation de l'évacuation d'une foule")

        # ___ Attributs de navigation ___
        self.__iSIMCurrent = 0
        self.__bSIMBackward = False
        self.__bSIMForward = False

        # ___ Attributs pour la simulation ___
        self.__fSIMForceAttraction = 0
        self.__fSIMForceRepulsion = 0
        self.__fSIMForceAcceleration = 0
        self.__iSIMTempsDeSimulation = 0

        self.__ENVEnvironnement = CEnvironnement()

        self.__SIMFichierPosition = CFichier("../../FichierSimulation/FichierPositions")
        self.__lSIMListePositions = []
        self.__lSIMListePersonnes = []
        self.__lSIMListePersonnesVue = []
        self.__lSIMListePersonnesSorties = [] #Liste des personnes sortie
        self.__lSIMListeSortiesVue = []
        self.__lSIMListeObstaclesVue = []
        self.__lSIMlisteTest = []

        # ___ Attributs de fenetre ___
        """
        -----------------------  Choix Fichier  ------------------------------
        """
        self.__lSIMListeEnvironnement = os.listdir('../../environnements/')
        self.__lSIMListeEnvironnement.append('Vide')
        self.__sSIMEnvironnement = ''
        self.__SIMFichierEnvironnement = CFichier()
        self.__SIMChoixMenu = OptionMenu(self._IHMWindow, self.__sSIMEnvironnement, *self.__lSIMListeEnvironnement)
        self.SIMCreation_Choix_Fichier()

        """
        -----------------------  Zones de saisies  ------------------------------
        """
        self.__SIMlabelForceAttract = Label()
        self.__SIMlabelForceRepuls = Label()
        self.__SIMlabelForceAcc = Label()
        self.SIMCreation_Zone_Saisies()

        self.IHMCreation_Zone_Simulation()
        print(self.__sSIMEnvironnement.get())

        """
        -----------------------  Lancement et navigation dans la simulation  ------------------------------
        """
        self.__SIMbouton_back = Button()
        self.__SIMbouton_front = Button()
        self.__SIMbouton_lancement = Button()

        self.__SIMlabelVitesse = Label()
        self.__lSIMListeVitesse = [0.25, 0.5, 1, 1.5, 2]
        self.__fSIMVitesse = 1
        self.__SIMmenuVitesse = OptionMenu(self._IHMWindow, self.__sSIMEnvironnement, *self.__lSIMListeVitesse)

        self.SIMCreation_Lancement_Simulation()

        """
        -----------------------  Bilan de la simulation  ------------------------------
        """
        self.__SIMBilan:CIHMBilan = CIHMBilan
        self.__SIMbouton_bilan = Button()
        self.SIMcreation_Bilan()

        self._IHMWindow.mainloop()

    def SIMCreation_Choix_Fichier(self):
        """
        Fonction permettant d'afficher le menu de choix des environnements.

        @return : void
        """
        self.__sSIMEnvironnement = StringVar(self._IHMWindow)
        self.__sSIMEnvironnement.set(self.__lSIMListeEnvironnement[len(self.__lSIMListeEnvironnement) - 1])
        self.__SIMChoixMenu = OptionMenu(self._IHMWindow, self.__sSIMEnvironnement, *self.__lSIMListeEnvironnement, command=self.SIMchoix_Environnement)
        self.__SIMChoixMenu.grid(column=0, row=2, sticky='E')

    #TODO RENDRE FONCTIONNEL LA SAISIS
    def SIMCreation_Zone_Saisies(self):
        """
        Fonction permettant d'afficher les zones de saisies pour les pourcentages des forces.

        @return : void
        """
        # Force attraction
        self._IHMWindow.columnconfigure(0, minsize=0, weight=0)
        self.__SIMlabelForceAttract = Label(self._IHMWindow, text="Force d'attraction (en %):", bg=self._sIHMbackgroundColor)
        self.__SIMlabelForceAttract.grid(column=1, row=2, sticky='E')
        self._IHMWindow.columnconfigure(1, minsize=0, weight=0)
        self.__fSIMForceAttraction = Entry(self._IHMWindow, width=3)
        self.__fSIMForceAttraction.grid(column=2, row=2, sticky='W')

        # Force répulsion
        self._IHMWindow.columnconfigure(2, minsize=0, weight=1)
        self.__SIMlabelForceRepuls = Label(self._IHMWindow, text="Force de répulsion (en %):", bg=self._sIHMbackgroundColor)
        self.__SIMlabelForceRepuls.grid(column=3, row=2, sticky='E')
        self._IHMWindow.columnconfigure(3, minsize=0, weight=1)
        self.__fSIMForceRepulsion = Entry(self._IHMWindow, width=3)
        self.__fSIMForceRepulsion.grid(column=4, row=2, sticky='W')

        # Force accélération
        self._IHMWindow.columnconfigure(4, minsize=0, weight=1)
        self.__SIMlabelForceAcc = Label(self._IHMWindow, text="Force d'accélération (en %):", bg=self._sIHMbackgroundColor)
        self.__SIMlabelForceAcc.grid(column=5, row=2, sticky='E')
        self._IHMWindow.columnconfigure(5, minsize=0, weight=1)
        self.__fSIMForceAcceleration = Entry(self._IHMWindow, width=3)
        self.__fSIMForceAcceleration.grid(column=6, row=2, sticky='W')

    def SIMCreation_Lancement_Simulation(self):
        """
        Fonction permettant de créer tous les boutons en lien avec le lancement et la navigation de la simulation.

        @return : void
        """
        # Reculer
        self._IHMWindow.columnconfigure(3, minsize=0, weight=0)
        self.__SIMbouton_back = Button(self._IHMWindow, text='<<<')
        self.__SIMbouton_back.grid(column=3, row=6, sticky='W')
        self.__SIMbouton_back.bind('<ButtonPress-1>', self.SIMiterate_Back)
        self.__SIMbouton_back.bind('<ButtonRelease-1>', self.SIMstop_Iterate_Back)

        # Avancer
        self.__SIMbouton_front = Button(self._IHMWindow, text='>>>')
        self.__SIMbouton_front.grid(column=3, row=6, sticky='E')
        self.__SIMbouton_front.bind('<ButtonPress-1>', self.SIMiterate_Front)
        self.__SIMbouton_front.bind('<ButtonRelease-1>', self.SIMstop_Iterate_Front)

        # Lancement simulation
        self.__SIMbouton_lancement = Button(self._IHMWindow, text='LANCER')
        self.__SIMbouton_lancement.grid(column=3, row=6, sticky='NS')
        self.__SIMbouton_lancement.bind('<ButtonPress>', self.SIMlancer_Simulation)

        # Force vitesse
        self.__SIMlabelVitesse = Label(self._IHMWindow, text="Vitesse de lecture : ", bg='light grey')
        self.__SIMlabelVitesse.grid(column=3, row=5, sticky='E', pady=10)
        self._IHMWindow.columnconfigure(5, minsize=0, weight=1)

        self.__fSIMVitesse = StringVar(self._IHMWindow)
        self.__fSIMVitesse.set(self.__lSIMListeVitesse[2])
        self.__SIMmenuVitesse = OptionMenu(self._IHMWindow, self.__fSIMVitesse, *self.__lSIMListeVitesse)
        self.__SIMmenuVitesse.grid(column=4, row=5, sticky='W')

    def SIMcreation_Bilan(self):
        """
        Fonction permettant d'afficher le bouton "bilan".

        @return : void
        """
        self.__SIMbouton_bilan.config(state=DISABLED, text="Bilan", command=self.SIMaffichageBilan)
        self.__SIMbouton_bilan.grid(column=5, row=6, sticky='W')

    def SIMaffichageBilan(self):
        self.__SIMBilan = CIHMBilan(self.__lSIMlisteTest)

    def SIMmouvement(self):
        """
        Fonction permettant d'actualiser la position des personnes.

        @param : multiplicateur qui permet de moduler la vitesse de la simulation
        @return : void
        """
        index = 0
        for j in range(0, len(self.__lSIMListePersonnesVue)):
            self.personne = CPersonne(False, np.array([self.__lSIMListePositions[self.__iSIMCurrent][j + index], self.__lSIMListePositions[self.__iSIMCurrent][j + index + 1]]))
            self.personne.PERajouterDirection(self.__ENVEnvironnement.getSorties()[0])
            if self.personne.PERsorti() == False :
                self.__lSIMListePersonnesVue[j].setX(self.__lSIMListePositions[self.__iSIMCurrent][j + index])
                self.__lSIMListePersonnesVue[j].setY(self.__lSIMListePositions[self.__iSIMCurrent][j + index + 1])
                self.__lSIMListePersonnesVue[j].PERsetPression(self.__lSIMListePositions[self.__iSIMCurrent][j + index + 2])
                self.__lSIMListePersonnesVue[j].move()
            else:
                self.__lSIMListePersonnesVue[j].setColor("")
                self.__lSIMListePersonnesVue[j].move()
            index += 2
        time.sleep(0.05 / float(self.__fSIMVitesse.get()))

    def SIMlancer_Simulation(self, event):
        """
        Fonction permettant de lancer la simulation.

        @return : void
        """
        for personne in self.__lSIMListePersonnesVue:
            personne.disparaitre()

        self.__lSIMListePersonnesVue.clear()

        """
        ------------------------- Recuperation des coordonees -------------------------
        """
        monFichier = CFichier("../../FichierSimulation/FichierPositions.csv")
        self.__lSIMListePositions = monFichier.FICLireFichierPosition()
        self.__lSIMlisteTest = self.__lSIMListePositions

        # On obtient le nombre de personnes grace aux colonnes du fichier csv

        if not (self.__SIMbouton_lancement['state'] == DISABLED):
            self.__SIMbouton_lancement.config(state=DISABLED)
            self.__SIMbouton_bilan.config(state=DISABLED)
            self.__SIMbouton_back.config(state=DISABLED)
            self.__SIMbouton_front.config(state=DISABLED)
            #for personne in self.lListePersonnes:
                #personne.disparaitre()
            self.__lSIMListePersonnes.clear()
            self._IHMWindow.update()
            self.__iSIMCurrent = 0
            # Creation des personnes et initialisation de leurs positions
            index = 0
            for self.__iSIMCurrent in range(0, int(self.__ENVEnvironnement.getNbPersonnes())):
                personne = CPersonneVue(self._IHMCanvasSimulation, self.__lSIMListePositions[0][self.__iSIMCurrent + index], self.__lSIMListePositions[0][self.__iSIMCurrent + index + 1], 5)
                self.__lSIMListePersonnesVue.append(personne)
                index += 2

            # Mouvement
            self.__iSIMCurrent = 0
            for self.__iSIMCurrent in range(0, len(self.__lSIMListePositions)):
                self._IHMWindow.update()
                self.SIMmouvement()
            self.__SIMbouton_lancement.config(state=NORMAL)
            self.__SIMbouton_bilan.config(state=NORMAL)
            self.__SIMbouton_back.config(state=NORMAL)
            self.__SIMbouton_front.config(state=NORMAL)

    def SIMiterate_Back(self, event):
        """
        Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "reculer"

        @return : void
        """
        self.__bSIMBackward = True
        while (self.__iSIMCurrent - 1 >= 0 and (self.__bSIMBackward == True)):
            self._IHMWindow.update()
            self.__iSIMCurrent -= 1
            self.SIMmouvement()

    def SIMiterate_Front(self, event):
        """
        Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "avancer"

        @return : void
        """
        self.__bSIMForward = True
        while (self.__iSIMCurrent + 1 < len(self.__lSIMListePositions) and (self.__bSIMForward == True)):
            self._IHMWindow.update()
            self.__iSIMCurrent += 1
            self.SIMmouvement()

    def SIMstop_Iterate_Back(self, event):
        """
        Fonction permettant d'arreter d'aller en arriere.

        @return : void
        """
        self.__bSIMBackward = False

    def SIMstop_Iterate_Front(self, event):
        """
        Fonction permettant d'arreter d'avancer dans la simulation.

        @return : void
        """
        self.__bSIMForward = False

    def SIMrefresh_ListeEnvironnement(self):
        self.__lSIMListeEnvironnement = os.listdir('../../environnements/')
        self.__lSIMListeEnvironnement.append('Vide')

    #TODO rendre fonctionnel le choix de lenvironnement avec une methode
    def SIMchoix_Environnement(self, sEnvironnement):
        """
        Fonction permettant de réaliser les calculs des forces et calculer les positions des personnes lors d'une evacuation.

        @return : void
        """
        print(sEnvironnement)
        self.SIMclear()
        self.__SIMbouton_lancement.config(state=DISABLED)
        self.__SIMbouton_front.config(state=DISABLED)
        self.__SIMbouton_back.config(state=DISABLED)
        self.__SIMbouton_bilan.config(state=DISABLED)
        if(sEnvironnement != 'Vide'):
            self.LabelChargement = Label(self._IHMWindow, text="Chargement... ", bg='light grey')
            self.LabelChargement.grid(column=0, row=5, ipadx=5, pady=5, columnspan=2)

            self.__SIMFichierEnvironnement = CFichier("../../environnements/" + sEnvironnement)
            self.__ENVEnvironnement.CEnvironnementFichier(self.__SIMFichierEnvironnement)
            for personnes in self.__ENVEnvironnement.getListePersonnes():
                personnes.PERajouterDirection(self.__ENVEnvironnement.getSorties())

            self.__lSIMListePersonnesSorties = [True for i in range(self.__ENVEnvironnement.getNbPersonnes())]
            bfini = False

            self.__lSIMListePersonnes = self.__ENVEnvironnement.getListePersonnes()

            #Affichage de la position initiale
            for personnes in self.__lSIMListePersonnes:
                personne = CPersonneVue(self._IHMCanvasSimulation, personnes.PERgetListCoordonnees()[0][0], personnes.PERgetListCoordonnees()[0][1], 5)
                self.__lSIMListePersonnesVue.append(personne)
                self._IHMWindow.update()

            #Affichage des obstacles
            for obstacles in self.__ENVEnvironnement.getListeObstacles():
                obstacle = CObstacleQuadrilatereVue(self._IHMCanvasSimulation, obstacles)
                self.__lSIMListeObstaclesVue.append(obstacle)
                self._IHMWindow.update()

            for sortie in self.__ENVEnvironnement.getSorties():
                sortie = CSortiesVue(self._IHMCanvasSimulation, sortie)
                self.__lSIMListeSortiesVue.append(sortie)
                self._IHMWindow.update()

            header = len(self.__lSIMListePersonnes) * ["x", "y", "pression"]

            with  open("../../FichierSimulation/FichierPositions.csv", "w") as csv_file:
                writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
                writer.writerow(header)
                while bfini == False and self.__iSIMTempsDeSimulation <= 5000:
                    print(self.__iSIMTempsDeSimulation)
                    if self.__lSIMListePersonnes == []:
                        bfini = True

                    # ecriture des coordonnees
                    for personne in self.__lSIMListePersonnes:
                        self.__lSIMListePositions.append(personne.PERRecupererDerniereCoordonne()[0])
                        self.__lSIMListePositions.append(personne.PERRecupererDerniereCoordonne()[1])
                        self.__lSIMListePositions.append(personne.PERgetPression())

                    writer.writerow(self.__lSIMListePositions)
                    self.__lSIMListePositions.clear()

                    # calcul des nouvelles coordonnees
                    for personne in self.__lSIMListePersonnes:
                        if self.__lSIMListePersonnesSorties[self.__lSIMListePersonnes.index(personne)] == True:

                            # Force D'acceleration :

                            personne.PERCalculerForceAcceleration()

                            # Force de Repulsion entre personne :

                            personne.PERClearPersonneProximite()

                            # ajout des personnes proche de personne
                            for personneProx in self.__lSIMListePersonnes:

                                # pour pas qu'on ajoute elle-même dans la liste et les personnes sorti

                                if self.__lSIMListePersonnes.index(personne) != self.__lSIMListePersonnes.index(personneProx) and (
                                        self.__lSIMListePersonnesSorties[self.__lSIMListePersonnes.index(personneProx)] == True):
                                    coordper = personne.PERRecupererDerniereCoordonne()
                                    coordperprox = personneProx.PERRecupererDerniereCoordonne()
                                    if (COperation.OPEDetectionCercle(coordper[0], coordper[1], coordperprox[0], coordperprox[1], 20) == True):
                                        personne.PERajouterPersonne(personneProx)
                            #print('__________Position : ', personne.RecupererDerniereCoordonne())
                            personne.PERCalculerForceRepulsion()
                            #print("____REP : ", personne.getForceRepulsionPersonne().gettertForceRepulsion())
                            #personne.CalculForceAttraction(self.iTempsDeSimulation)
                            #print("____REPAttraction : ", personne.getForceAttraction().getValeurForceAttraction())

                            #print('\n-------------autre------------\n')

                            # Force de Repulsion par un obstacle :
                            for obstacle in self.__ENVEnvironnement.getListeObstacles():
                                coordPieton = personne.PERRecupererDerniereCoordonne()
                                sommet = personne.PERgetForceRepulsionObstacle().FREDeterminerSommetObstacleQuadrilatere(coordPieton,
                                                                                                                         obstacle)
                                #print("sommet = ", sommet)
                                if (COperation.OPEDetectionCercle(sommet[0], sommet[1], coordPieton[0], coordPieton[1], 10) == True):
                                    personne.PERajouterObstacle(obstacle)

                            personne.PERCalculerForceRepulsionObstacle()
                            print("____REPOBSTACLE : ", personne.PERgetForceRepulsionObstacle().FREgettertForceRepulsion())
                            # Nouvelle Position:

                            personne.PERCalculerNouvellePosition(self.__iSIMTempsDeSimulation)

                            # On verifie si la personne est sortie ou non.
                            if personne.PERsorti() == True:
                                self.__lSIMListePersonnesSorties[self.__lSIMListePersonnes.index(personne)] = False
                                if not any(self.__lSIMListePersonnesSorties):
                                    bfini = True

                    self.__iSIMTempsDeSimulation += DeltaT


            self.__SIMbouton_lancement.config(state=NORMAL)
            self.__SIMbouton_front.config(state=NORMAL)
            self.__SIMbouton_back.config(state=NORMAL)
            self.LabelChargement.config(text='')

            self.__SIMbouton_bilan.config(state=NORMAL)

    def SIMclear(self):
        """
        Fonction permettant de reinitialiser la fenetre.

        @return : void
        """
        # ___ Attributs de navigation ___
        self.__iSIMCurrent = 0
        self.__bSIMBackward = False
        self.__bSIMForward = False
        self.__iSIMTempsDeSimulation = 0

        self.__lSIMListePositions.clear()
        self.__lSIMListePersonnes.clear()
        self.__lSIMListePersonnesVue.clear()
        self.__lSIMListeObstaclesVue.clear()
        self.__lSIMListePersonnesSorties.clear()

        self.IHMCreation_Zone_Simulation()

test = CIHMSimulation()
