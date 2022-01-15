import Code.Modele.CEnvironnement as CEnvironnement
import tkinter

class CEnvironnementController:

    def __init__(self):
        return 0

    def ControleInCanvas(self, environnement:CEnvironnement, canvas:tkinter.Canvas):
        for personne in environnement.getListePersonnes:
            if personne.getListeCoordonnees[0][0] > canvas.winfo_width():
                personne.getListeCoordonnees[0][0] = canvas.winfo_width()
            if personne.getListeCoordonnees[0][1] > canvas.winfo_height():
                personne.getListeCoordonnees[0][1] = canvas.winfo_height()

