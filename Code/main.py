from Code.Modele.CFichier import *
import numpy as np
import matplotlib.pyplot as plt

chemin = "C:/Users/Hicham/Desktop/"

monFichier = CFichier(chemin+"oui")

list = []

list = monFichier.LireFichierPositions()

print(list)
