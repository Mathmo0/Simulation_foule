from Code.Modele.CPersonne import CPersonne
from tkinter import *
from Code.Modele.CFichier import CFichier
from Code.Modele.CEnvironnement import CEnvironnement
from Code.Modele.CForce import DeltaT
import csv
import numpy as np

monFichier = CFichier("../FichierSimulation/FichierPositions")

listPositions = monFichier.LireFichierPositions()
