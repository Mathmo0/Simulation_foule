from tkinter import *

class CIHM:

    # -----------------Constructeur-----------------
    def __init__(self, titre = "", height = 400, width = 400):
        # ___ Attributs de fenetre ___
        """
        -----------------------  Creation de la fenetre ------------------------------
        """
        self.__IHMWindow = Tk()
        self.__sIHMbackgroundColor = "#7fb3d5"
        self.__IHMmainMenu = Menu()
        self.IHMCreation_Fenetre()

        """
        -----------------------  Titre  ------------------------------
        """
        self.__IHMlabelTitle = Label()
        self.__IHMlabelSubTitle = Label()
        self.IHMCreation_Titres(titre)

        """
        -----------------------  Menu  ------------------------------
        """
        self.__IHMaPropos = Label()
        self.__IHMLabelAPropos = Label()
        self.IHMCreation_Menu()
        self.__IHMLabelChargement = Label()

        """
        -----------------------  Zone de simulation  ------------------------------
        """
        self.__iIHMWidth = width
        self.__iIHMHeight = height
        self.__IHMFrameSimulation = Frame(self.__IHMWindow)
        self.__IHMCanvasSimulation = Canvas(self.__IHMWindow)

        #self.Window.mainloop()

    def IHMgetWindow(self):
        return self.__IHMWindow

    def IHMCreation_Fenetre(self):
        self.__IHMWindow['background'] = 'light gray'
        # self.window.wm_attributes("-transparentcolor", 'grey')
        self.__IHMWindow.title("Simulation de foule à échelle microscopique")
        # self.window.resizable(0, 0)
        self.__IHMWindow.geometry("1080x720")
        self.__IHMWindow.minsize(1080, 720)
        self.__IHMWindow.iconbitmap("../../Images/logo_polytech.ico")
        self.__IHMWindow.columnconfigure(0, minsize=0, weight=0)
        self.__IHMWindow.columnconfigure(2, minsize=0, weight=1)
        self.__IHMWindow.columnconfigure(4, minsize=0, weight=1)

    def IHMCreation_Menu(self):
        # TODO afficher les infos correspondantes aux boutons
        self.__IHMmainMenu = Menu(self.__IHMWindow)
        #fileMenuFichier = Menu(self.mainMenu)
        self.__IHMmainMenu.add_cascade(label="à propos", command=self.IHMA_Propos)
        self.__IHMmainMenu.add_cascade(label="?")
        self.__IHMWindow.config(menu=self.__IHMmainMenu)

    def IHMCreation_Titres(self, titre):
        self.__IHMlabelTitle = Label(self.__IHMWindow,
                                     text=titre,
                                     font=("Arial", 40),
                                     bg='light grey')
        self.__IHMlabelSubTitle = Label(self.__IHMWindow,
                                        text="Simulation à l'échelle microscopique basée sur le modèle des forces sociales de D.Helbing",
                                        font=("Arial", 15),
                                        bg='light grey')
        self.__IHMlabelTitle.grid(column=0, row=0, ipadx=5, pady=5, columnspan=6, sticky='NS')
        self.__IHMlabelSubTitle.grid(column=0, row=1, ipadx=5, pady=5, columnspan=6, sticky='NS')

        self.background = Label(self.__IHMWindow, width=self.__IHMWindow.winfo_width(), bg=self.__sIHMbackgroundColor)
        self.background.grid(column=0, row=2, columnspan=7)

    def IHMA_Propos(self):
        self.__IHMaPropos = Toplevel(self.__IHMWindow)
        self.__IHMaPropos.resizable(0, 0)
        self.__IHMLabelAPropos = Label(self.__IHMaPropos,
                                       text="Ce projet de simulation de foule à été réalisé par Maxime EDELINE, Hicham MOUSTAQIM et Mathis MOYSE\n pendant leur quatrième année d'étude à Polytech Tours en informatique.",
                                       font=("Arial", 20),
                                       bg='light grey')

        self.__IHMLabelAPropos.grid(column=0, row=0)

    def IHMCreation_Zone_Simulation(self):
        self.__IHMFrameSimulation = Frame(self.__IHMWindow)
        self.__IHMFrameSimulation.grid(column=0, row=3, columnspan=6, pady=10, padx=20, sticky='NS')
        self.__IHMCanvasSimulation = Canvas(self.__IHMWindow, width=self.__iIHMWidth, height=self.__iIHMHeight, bg='snow', bd=1, relief=RIDGE)
        self.__IHMCanvasSimulation.grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')

