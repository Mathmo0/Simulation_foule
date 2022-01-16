import numpy as np

from Code.Modele.CFichier import CFichier
from Code.Modele.CPersonne import CPersonne
from Code.Modele.COperation import COperation
from Code.Modele.CForce import CForce
from sympy.solvers import solve
from sympy import Symbol, sqrt, linsolve, diff
from sympy.vector import CoordSys3D
import matplotlib.pyplot as plt


x = Symbol('x')
y = Symbol('y')
a = Symbol('a',constant=True)
b = Symbol('b',constant=True)
c = Symbol('c',constant=True)
d = Symbol('d',constant=True)
s1x = Symbol('s1x',constant=True)
s1y = Symbol('s1y',constant=True)
s2x = Symbol('s2x',constant=True)
s2y = Symbol('s1y',constant=True)

#oui = solve([sqrt((3-x)**2 + (7.5-y)**2)+sqrt((x-7)**2 +(y-15)**2)-8.5,sqrt((x-1)**2 + (y-10)**2)+sqrt((5-x)**2 +(10-y)**2)-4],[x,y])
#oui = solve([sqrt((c-x)**2 + (d-y)**2)+sqrt((x-a)**2 +(y-b)**2)-sqrt((a-x)**2+(b-d)**2),sqrt((x-s1x)**2 + (y-s1y)**2)+sqrt((s2x-x)**2 +(s2y-y)**2)- sqrt((s2x-s1x)**2+(s2y-s1y)**2)],[x,y,a,b,c,d,s1x,s2x,s1y,s2y])
#print(oui)

coord = np.array([5,4])
R = CoordSys3D('R')
v = coord[0]*R.x + coord[1]*R.y

print(diff(v,R.x))


list1 = [10, 15]
list2 = [1, 5]

a = np.array(list1)
b = np.array(list2)

Position = np.array([1, 3])
PositionDeltaT = np.array([4, 9])
PositionB = np.array([5, 5])
#resultat = COperation.Nabla(Position, PositionDeltaT, PositionB)
#force = CForce()
#resultat =force.UAlphaObstacle(4)

#print(round(resultat * (10 ** (8)), 2))
#personne = CPersonne(np.array([0, 0]))

def heatmap2d(arr: np.ndarray):
    plt.imshow(arr, cmap='viridis')
    plt.colorbar()
    plt.show()


'''monFichier = CFichier("FichierSimulation/FichierPositions.csv")
listPositions = monFichier.LireFichierPosition()

listCarteChaleur = np.zeros((400,400))
print(listCarteChaleur)
for uiBoucle1 in range(len(listPositions)) :

    px1 = (listPositions[uiBoucle1][0]*400)/500 # ici 400 = widh et 500 largeur de l'environnement
    px2 = (listPositions[uiBoucle1][1]*400)/500 # ici 400 = Height et 500 longueur de l'environnement
    listCarteChaleur[round(px1)][round(px2)] +=1



test_array = listCarteChaleur # np.arange(100 * 100).reshape(100, 100)
heatmap2d(test_array)
'''

position2 = np.array([3,7.5])
position = np.array([7,15])
a = COperation.FonctionTrajectoirePieton(position,position2)
print("a = ",a)