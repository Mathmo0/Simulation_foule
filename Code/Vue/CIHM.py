from tkinter import *

class CIHM:

    # -----------------Constructeur-----------------
    def __init__(self, titre = "", height = 400, width = 400):
        # ___ Attributs de fenetre ___
        """
        -----------------------  Creation de la fenetre ------------------------------
        """
        self._IHMWindow = Tk()
        self._sIHMbackgroundColor = "#7fb3d5"
        self._IHMmainMenu = Menu()
        self.IHMCreation_Fenetre()

        """
        -----------------------  Titre  ------------------------------
        """
        self._IHMlabelTitle = Label()
        self._IHMlabelSubTitle = Label()
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
        self._iIHMWidth = width
        self._iIHMHeight = height
        self._IHMFrameSimulation = Frame(self._IHMWindow)
        self._IHMCanvasSimulation = Canvas(self._IHMWindow)

        #self.Window.mainloop()

    def IHMgetWindow(self):
        return self._IHMWindow

    def IHMCreation_Fenetre(self):
        self._IHMWindow['background'] = 'light gray'
        # self.window.wm_attributes("-transparentcolor", 'grey')
        self._IHMWindow.title("Simulation de foule à échelle microscopique")
        # self.window.resizable(0, 0)
        self._IHMWindow.geometry("1080x720")
        self._IHMWindow.minsize(1080, 720)
        self._IHMWindow.iconbitmap("../../Images/logo_polytech.ico")
        self._IHMWindow.columnconfigure(0, minsize=0, weight=0)
        self._IHMWindow.columnconfigure(2, minsize=0, weight=1)
        self._IHMWindow.columnconfigure(4, minsize=0, weight=1)

    def IHMCreation_Menu(self):
        # TODO afficher les infos correspondantes aux boutons
        self._IHMmainMenu = Menu(self._IHMWindow)
        #fileMenuFichier = Menu(self.mainMenu)
        self._IHMmainMenu.add_cascade(label="à propos", command=self.IHMA_Propos)
        self._IHMmainMenu.add_cascade(label="?")
        self._IHMWindow.config(menu=self._IHMmainMenu)

    def IHMCreation_Titres(self, titre):
        self._IHMlabelTitle = Label(self._IHMWindow,
                                    text=titre,
                                    font=("Arial", 40),
                                    bg='light grey')
        self._IHMlabelSubTitle = Label(self._IHMWindow,
                                       text="Simulation à l'échelle microscopique basée sur le modèle des forces sociales de D.Helbing",
                                       font=("Arial", 15),
                                       bg='light grey')
        self._IHMlabelTitle.grid(column=0, row=0, ipadx=5, pady=5, columnspan=6, sticky='NS')
        self._IHMlabelSubTitle.grid(column=0, row=1, ipadx=5, pady=5, columnspan=6, sticky='NS')

        self.background = Label(self._IHMWindow, width=self._IHMWindow.winfo_width(), bg=self._sIHMbackgroundColor)
        self.background.grid(column=0, row=2, columnspan=7)

    def IHMA_Propos(self):
        self.__IHMaPropos = Toplevel(self._IHMWindow)
        self.__IHMaPropos.resizable(0, 0)
        self.__IHMLabelAPropos = Label(self.__IHMaPropos,
                                       text="Ce projet de simulation de foule à été réalisé par Maxime EDELINE, Hicham MOUSTAQIM et Mathis MOYSE\n pendant leur quatrième année d'étude à Polytech Tours en informatique.",
                                       font=("Arial", 20),
                                       bg='light grey')

        self.__IHMLabelAPropos.grid(column=0, row=0)

    def IHMCreation_Zone_Simulation(self):
        self._IHMFrameSimulation = Frame(self._IHMWindow)
        self._IHMFrameSimulation.grid(column=0, row=3, columnspan=6, pady=10, padx=20, sticky='NS')
        self._IHMCanvasSimulation = Canvas(self._IHMWindow, width=self._iIHMWidth, height=self._iIHMHeight, bg='snow', bd=1, relief=RIDGE)
        self._IHMCanvasSimulation.grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')

