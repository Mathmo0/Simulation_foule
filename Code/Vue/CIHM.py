from tkinter import *

class CIHM:

    # -----------------Constructeur-----------------
    def __init__(self, titre = "", height = 400, width = 400):
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
        self.Creation_Titres(titre)

        """
        -----------------------  Menu  ------------------------------
        """
        self.aPropos = Label()
        self.LabelAPropos = Label()
        self.Creation_Menu()
        self.LabelChargement = Label()

        """
        -----------------------  Zone de simulation  ------------------------------
        """
        self.iWidth = width
        self.iHeight = height
        self.FrameSimulation = Frame(self.Window)
        self.CanvasSimulation = Canvas(self.Window)

        #self.Window.mainloop()

    def getWindow(self):
        return self.Window

    def Creation_Fenetre(self):
        self.Window['background'] = 'light gray'
        # self.window.wm_attributes("-transparentcolor", 'grey')
        self.Window.title("Simulation de foule à échelle microscopique")
        # self.window.resizable(0, 0)
        self.Window.geometry("1080x720")
        self.Window.minsize(1080, 720)
        self.Window.iconbitmap("../../Images/logo_polytech.ico")
        self.Window.columnconfigure(0, minsize=0, weight=0)
        self.Window.columnconfigure(2, minsize=0, weight=1)
        self.Window.columnconfigure(4, minsize=0, weight=1)

    def Creation_Menu(self):
        # TODO afficher les infos correspondantes aux boutons
        self.mainMenu = Menu(self.Window)
        #fileMenuFichier = Menu(self.mainMenu)
        self.mainMenu.add_cascade(label="à propos", command=self.A_Propos)
        self.mainMenu.add_cascade(label="?")
        self.Window.config(menu=self.mainMenu)

    def Creation_Titres(self, titre):
        self.labelTitle = Label(self.Window,
                                text=titre,
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

    def A_Propos(self):
        self.aPropos = Toplevel(self.Window)
        self.aPropos.resizable(0, 0)
        self.LabelAPropos = Label(self.aPropos,
                                  text="Ce projet de simulation de foule à été réalisé par Maxime EDELINE, Hicham MOUSTAQIM et Mathis MOYSE\n pendant leur quatrième année d'étude à Polytech Tours en informatique.",
                                  font=("Arial", 20),
                                  bg='light grey')

        self.LabelAPropos.grid(column=0, row=0)

    def Creation_Zone_Simulation(self):
        self.FrameSimulation = Frame(self.Window)
        self.FrameSimulation.grid(column=0, row=3, columnspan=6, pady=10, padx=20, sticky='NS')
        self.CanvasSimulation = Canvas(self.Window, width=self.iWidth, height=self.iHeight, bg='snow', bd=1, relief=RIDGE)
        self.CanvasSimulation.grid(column=0, row=3, columnspan=6, pady=20, padx=20, sticky='NS')

