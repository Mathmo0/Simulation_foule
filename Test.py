import numpy as np
from Code.Modele.COperation import COperation
from Code.Modele.CForce import CForce
list1 = [10, 15]
list2 = [1, 5]

a = np.array(list1)
b = np.array(list2)

dt = 0
vitesse = 0

def calculvitesse(a, b):
    if(dt == 0):
        return 0
    else :
        return np.linalg.norm((a - b), ord=1)/dt

def vitesse(a, b):
    if(dt == 0):
        return 0
    else :
        return (a - b)/dt

def nouvellepos(x, y):
    return 2*(x - y)

for i in range(0, 10):
    #print(a)
    v = vitesse(a, b)
    #print(v)
    ealpha = (b - a)/np.linalg.norm((a - b), ord=1)
    #print(ealpha)
    a = a + nouvellepos(ealpha*1.34, v)
    dt += 2

Position = np.array([1, 3])
PositionDeltaT = np.array([4, 9])
PositionB = np.array([5, 5])
#resultat = COperation.Nabla(Position, PositionDeltaT, PositionB)
force = CForce()
resultat =force.UAlphaObstacle(4)

print(round(resultat * (10 ** (8)), 2))
