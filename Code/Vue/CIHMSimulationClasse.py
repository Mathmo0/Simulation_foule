import time
import os

from Code.Modele.COperation import COperation
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

        # ___ Attributs de fenetre ___
        """
        -----------------------  Choix Fichier  ------------------------------
        """
        self.__lSIMListeEnvironnement = os.listdir('../../environnements/')
        self.__lSIMListeEnvironnement.append('Vide')
        self.__sSIMEnvironnement = ''
        self.__SIMFichierEnvironnement = CFichier()
        self.__SIMChoixMenu = OptionMenu(self.__IHMWindow, self.__sSIMEnvironnement, *self.__lSIMListeEnvironnement)
        self.SIMCreation_Choix_Fichier()

        """
        -----------------------  Zones de saisies  ------------------------------
        """
        self.labelForceAttract = Label()
        self.labelForceRepuls = Label()
        self.labelForceAcc = Label()
        self.SIMCreation_Zone_Saisies()

        self.IHMCreation_Zone_Simulation()
        print(self.__sSIMEnvironnement.get())

        """
        -----------------------  Lancement et navigation dans la simulation  ------------------------------
        """
        self.__bouton_back = Button()
        self.__bouton_front = Button()
        self.__bouton_lancement = Button()

        self.labelVitesse = Label()
        self.lListeVitesse = [0.25, 0.5, 1, 1.5, 2]
        self.fVitesse = 1
        self.menuVitesse = OptionMenu(self.__IHMWindow, self.__sSIMEnvironnement, *self.lListeVitesse)

        self.SIMCreation_Lancement_Simulation()

        """
        -----------------------  Bilan de la simulation  ------------------------------
        """
        self.Bilan:CIHMBilan = CIHMBilan
        self.__bouton_bilan = Button()
        self.SIMCreation_Bilan()

        self.__IHMWindow.mainloop()

    def SIMCreation_Choix_Fichier(self):
        self.__sSIMEnvironnement = StringVar(self.__IHMWindow)
        self.__sSIMEnvironnement.set(self.__lSIMListeEnvironnement[len(self.__lSIMListeEnvironnement) - 1])
        self.__SIMChoixMenu = OptionMenu(self.__IHMWindow, self.__sSIMEnvironnement, *self.__lSIMListeEnvironnement, command=self.SIMChoix_Environnement)
        self.__SIMChoixMenu.grid(column=0, row=2, sticky='E')

    #TODO RENDRE FONCTIONNEL LA SAISIS
    def SIMCreation_Zone_Saisies(self):
        # Force attraction
        self.__IHMWindow.columnconfigure(0, minsize=0, weight=0)
        self.labelForceAttract = Label(self.__IHMWindow, text="Force d'attraction (en %):", bg=self.__sIHMbackgroundColor)
        self.labelForceAttract.grid(column=1, row=2, sticky='E')
        self.__IHMWindow.columnconfigure(1, minsize=0, weight=0)
        self.__fSIMForceAttraction = Entry(self.__IHMWindow, width=3)
        self.__fSIMForceAttraction.grid(column=2, row=2, sticky='W')

        # Force répulsion
        self.__IHMWindow.columnconfigure(2, minsize=0, weight=1)
        self.labelForceRepuls = Label(self.__IHMWindow, text="Force de répulsion (en %):", bg=self.__sIHMbackgroundColor)
        self.labelForceRepuls.grid(column=3, row=2, sticky='E')
        self.__IHMWindow.columnconfigure(3, minsize=0, weight=1)
        self.__fSIMForceRepulsion = Entry(self.__IHMWindow, width=3)
        self.__fSIMForceRepulsion.grid(column=4, row=2, sticky='W')

        # Force accélération
        self.__IHMWindow.columnconfigure(4, minsize=0, weight=1)
        self.labelForceAcc = Label(self.__IHMWindow, text="Force d'accélération (en %):", bg=self.__sIHMbackgroundColor)
        self.labelForceAcc.grid(column=5, row=2, sticky='E')
        self.__IHMWindow.columnconfigure(5, minsize=0, weight=1)
        self.__fSIMForceAcceleration = Entry(self.__IHMWindow, width=3)
        self.__fSIMForceAcceleration.grid(column=6, row=2, sticky='W')

    def SIMCreation_Lancement_Simulation(self):
        # Reculer
        self.__IHMWindow.columnconfigure(3, minsize=0, weight=0)
        self.__bouton_back = Button(self.__IHMWindow, text='<<<')
        self.__bouton_back.grid(column=3, row=6, sticky='W')
        self.__bouton_back.bind('<ButtonPress-1>', self.SIMiterate_back)
        self.__bouton_back.bind('<ButtonRelease-1>', self.SIMstop_iterate_back)

        # Avancer
        self.__bouton_front = Button(self.__IHMWindow, text='>>>')
        self.__bouton_front.grid(column=3, row=6, sticky='E')
        self.__bouton_front.bind('<ButtonPress-1>', self.SIMiterate_front)
        self.__bouton_front.bind('<ButtonRelease-1>', self.SIMstop_iterate_front)

        # Lancement simulation
        self.__bouton_lancement = Button(self.__IHMWindow, text='LANCER')
        self.__bouton_lancement.grid(column=3, row=6, sticky='NS')
        self.__bouton_lancement.bind('<ButtonPress>', self.SIMlancerSimulation)

        # Force vitesse
        self.labelVitesse = Label(self.__IHMWindow, text="Vitesse de lecture : ", bg='light grey')
        self.labelVitesse.grid(column=3, row=5, sticky='E', pady=10)
        self.__IHMWindow.columnconfigure(5, minsize=0, weight=1)

        self.fVitesse = StringVar(self.__IHMWindow)
        self.fVitesse.set(self.lListeVitesse[2])
        self.menuVitesse = OptionMenu(self.__IHMWindow, self.fVitesse, *self.lListeVitesse)
        self.menuVitesse.grid(column=4, row=5, sticky='W')

    def SIMCreation_Bilan(self):
        self.__bouton_bilan.config(state=DISABLED, text="Bilan", command=self.SIMAffichageBilan)
        self.__bouton_bilan.grid(column=5, row=6, sticky='W')

    def SIMAffichageBilan(self):
        self.Bilan = CIHMBilan(self.__lSIMListePositions)

    def SIMmouvement(self):
        """
        Fonction permettant d'actualiser la position des personnes.

        @param : multiplicateur qui permet de moduler la vitesse de la simulation
        @return : rien
        """
        index = 0
        for j in range(0, len(self.__lSIMListePersonnesVue)):
            self.__lSIMListePersonnesVue[j].setX(self.__lSIMListePositions[self.__iSIMCurrent][j + index])
            self.__lSIMListePersonnesVue[j].setY(self.__lSIMListePositions[self.__iSIMCurrent][j + index + 1])
            self.__lSIMListePersonnesVue[j].setPression(self.__lSIMListePositions[self.__iSIMCurrent][j + index + 2])
            self.__lSIMListePersonnesVue[j].move()
            index += 2
        time.sleep(0.05 / float(self.fVitesse.get()))

    def SIMlancerSimulation(self, event):
        """
        Fonction permettant de lancer la simulation.

        @return : rien
        """
        for personne in self.__lSIMListePersonnesVue:
            personne.disparaitre()

        self.__lSIMListePersonnesVue.clear()

        """
        ------------------------- Recuperation des coordonees -------------------------
        """
        monFichier = CFichier("../../FichierSimulation/FichierPositions.csv")
        self.__lSIMListePositions = monFichier.LireFichierPosition()

        # On obtient le nombre de personnes grace aux colonnes du fichier csv

        if not (self.__bouton_lancement['state'] == DISABLED):
            self.__bouton_lancement.config(state=DISABLED)
            self.__bouton_front.config(state=DISABLED)
            #for personne in self.lListePersonnes:
                #personne.disparaitre()
            self.__lSIMListePersonnes.clear()
            self.__IHMWindow.update()
            self.__iSIMCurrent = 0
            # Creation des personnes et initialisation de leurs positions
            index = 0
            for self.__iSIMCurrent in range(0, int(self.__ENVEnvironnement.getNbPersonnes())):
                personne = CPersonneVue(self.__IHMCanvasSimulation, self.__lSIMListePositions[0][self.__iSIMCurrent + index], self.__lSIMListePositions[0][self.__iSIMCurrent + index + 1], 5)
                self.__lSIMListePersonnesVue.append(personne)
                index += 2

            # Mouvement
            self.__iSIMCurrent = 0
            for self.__iSIMCurrent in range(0, len(self.__lSIMListePositions)):
                self.__IHMWindow.update()
                self.SIMmouvement()
            self.__bouton_lancement.config(state=NORMAL)
            self.__bouton_back.config(state=NORMAL)
            self.__bouton_front.config(state=NORMAL)

    def SIMiterate_back(self, event):
        """
        Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "reculer"

        @return : rien
        """
        self.__bSIMBackward = True
        while (self.__iSIMCurrent - 1 >= 0 and (self.__bSIMBackward == True)):
            self.__IHMWindow.update()
            self.__iSIMCurrent -= 1
            self.SIMmouvement()

    def SIMiterate_front(self, event):
        """
        Fonction permettant d'avancer dans la simulation tant qu'on appuie sur le bouton "avancer"

        @return : rien
        """
        self.__bSIMForward = True
        while (self.__iSIMCurrent + 1 < len(self.__lSIMListePositions) and (self.__bSIMForward == True)):
            self.__IHMWindow.update()
            self.__iSIMCurrent += 1
            self.SIMmouvement()

    def SIMstop_iterate_back(self, event):
        self.__bSIMBackward = False

    def SIMstop_iterate_front(self, event):
        self.__bSIMForward = False

    def SIMRefresh_ListeEnvironnement(self):
        self.__lSIMListeEnvironnement = os.listdir('../../environnements/')
        self.__lSIMListeEnvironnement.append('Vide')

    #TODO rendre fonctionnel le choix de lenvironnement avec une methode
    def SIMChoix_Environnement(self, sEnvironnement):
        print(sEnvironnement)
        self.SIMClear()
        self.__bouton_lancement.config(state=DISABLED)
        self.__bouton_front.config(state=DISABLED)
        self.__bouton_back.config(state=DISABLED)
        self.__bouton_bilan.config(state=DISABLED)
        if(sEnvironnement != 'Vide'):
            self.LabelChargement = Label(self.__IHMWindow, text="Chargement... ", bg='light grey')
            self.LabelChargement.grid(column=0, row=5, ipadx=5, pady=5, columnspan=2)

            self.__SIMFichierEnvironnement = CFichier("../../environnements/" + sEnvironnement)
            self.__ENVEnvironnement.CEnvironnementFichier(self.__SIMFichierEnvironnement)
            for personnes in self.__ENVEnvironnement.getListePersonnes():
                personnes.ajouterDirection(self.__ENVEnvironnement.getSorties())

            self.__lSIMListePersonnesSorties = [True for i in range(self.__ENVEnvironnement.getNbPersonnes())]
            bfini = False

            self.__lSIMListePersonnes = self.__ENVEnvironnement.getListePersonnes()

            #Affichage de la position initiale
            for personnes in self.__lSIMListePersonnes:
                personne = CPersonneVue(self.__IHMCanvasSimulation, personnes.getListCoordonnees()[0][0], personnes.getListCoordonnees()[0][1], 5)
                self.__lSIMListePersonnesVue.append(personne)
                self.__IHMWindow.update()

            #Affichage des obstacles
            for obstacles in self.__ENVEnvironnement.getListeObstacles():
                obstacle = CObstacleQuadrilatereVue(self.__IHMCanvasSimulation, obstacles)
                self.__lSIMListeObstaclesVue.append(obstacle)
                self.__IHMWindow.update()

            for sortie in self.__ENVEnvironnement.getSorties():
                sortie = CSortiesVue(self.__IHMCanvasSimulation, sortie)
                self.__lSIMListeSortiesVue.append(sortie)
                self.__IHMWindow.update()

            header = len(self.__lSIMListePersonnes) * ["x", "y", "pression"]

            with  open("../../FichierSimulation/FichierPositions.csv", "w") as csv_file:
                writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
                writer.writerow(header)
                while bfini == False:
                    if self.__lSIMListePersonnes == []:
                        bfini = True

                    # ecriture des coordonnees
                    for personne in self.__lSIMListePersonnes:
                        self.__lSIMListePositions.append(personne.RecupererDerniereCoordonne()[0])
                        self.__lSIMListePositions.append(personne.RecupererDerniereCoordonne()[1])
                        self.__lSIMListePositions.append(personne.getPression())

                    writer.writerow(self.__lSIMListePositions)
                    self.__lSIMListePositions.clear()

                    # calcul des nouvelles coordonnees
                    for personne in self.__lSIMListePersonnes:
                        if self.__lSIMListePersonnesSorties[self.__lSIMListePersonnes.index(personne)] == True:

                            # Force D'acceleration :

                            personne.CalculerForceAcceleration()

                            # Force de Repulsion entre personne :

                            personne.ClearPersonneProximite()

                            # ajout des personnes proche de personne
                            for personneProx in self.__lSIMListePersonnes:

                                # pour pas qu'on ajoute elle-même dans la liste et les personnes sorti

                                if self.__lSIMListePersonnes.index(personne) != self.__lSIMListePersonnes.index(personneProx) and (
                                        self.__lSIMListePersonnesSorties[self.__lSIMListePersonnes.index(personneProx)] == True):
                                    coordper = personne.RecupererDerniereCoordonne()
                                    coordperprox = personneProx.RecupererDerniereCoordonne()
                                    if (COperation.DetectionCercle(coordper[0], coordper[1], coordperprox[0], coordperprox[1], 20) == True):
                                        personne.ajouterPersonne(personneProx)
                            print('__________Position : ', personne.RecupererDerniereCoordonne())
                            personne.CalculerForceRepulsion()
                            print("____REP : ", personne.getForceRepulsionPersonne().gettertForceRepulsion())
                            personne.CalculForceAttraction(self.__iSIMTempsDeSimulation)
                            print("____REPAttraction : ", personne.getForceAttraction().getValeurForceAttraction())

                            print('\n-------------autre------------\n')

                            # Force de Repulsion par un obstacle :
                            for obstacle in self.__ENVEnvironnement.getListeObstacles():
                                coordPieton = personne.RecupererDerniereCoordonne()
                                sommet = personne.getForceRepulsionObstacle().FREDeterminerSommetObstacleQuadrilatere(coordPieton,
                                                                                                                      obstacle)
                                #print("sommet = ", sommet)
                                if (COperation.DetectionCercle(sommet[0], sommet[1], coordPieton[0], coordPieton[1], 10) == True):
                                    personne.ajouterObstacle(obstacle)

                            personne.CalculerForceRepulsionObstacle()
                            print("____REPOBSTACLE : ", personne.getForceRepulsionObstacle().gettertForceRepulsion())
                            # Nouvelle Position:

                            personne.CalculerNouvellePosition(self.__iSIMTempsDeSimulation)

                            # On verifie si la personne est sortie ou non.
                            if personne.sorti() == True:
                                self.__lSIMListePersonnesSorties[self.__lSIMListePersonnes.index(personne)] = False
                                if not any(self.__lSIMListePersonnesSorties):
                                    bfini = True

                    self.__iSIMTempsDeSimulation += DeltaT


            self.__bouton_lancement.config(state=NORMAL)
            self.__bouton_front.config(state=NORMAL)
            self.__bouton_back.config(state=NORMAL)
            self.LabelChargement.config(text='')

            self.__bouton_bilan.config(state=NORMAL)

    def SIMClear(self):
        # ___ Attributs de navigation ___
        self.__iSIMCurrent = 0
        self.__bSIMBackward = False
        self.__bSIMForward = False

        self.__lSIMListePositions.clear()
        self.__lSIMListePersonnes.clear()
        self.__lSIMListePersonnesVue.clear()
        self.__lSIMListeObstaclesVue.clear()
        self.__lSIMListePersonnesSorties.clear()

        self.IHMCreation_Zone_Simulation()

test = CIHMSimulationClasse()
