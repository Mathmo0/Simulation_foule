import numpy as np
from Code.Modele.CPersonne import CPersonne
from Code.Modele.COperation import COperation
from Code.Modele.CForce import CForce
from sympy.solvers import solve
from sympy import Symbol, sqrt, linsolve, diff
from sympy.vector import CoordSys3D

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
t = Symbol('t')
oui = solve([sqrt((3-x)**2 + (7.5-y)**2)+sqrt((x-7)**2 +(y-15)**2)-8.5,sqrt((x-1)**2 + (y-10)**2)+sqrt((5-x)**2 +(10-y)**2)-4],[x,y])
print(oui)

coord = np.array([5,4])
R = CoordSys3D('R')
v = coord[0]*R.x + coord[1]*R.y

print(diff(v,R.x))


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
#force = CForce()
#resultat =force.UAlphaObstacle(4)

#print(round(resultat * (10 ** (8)), 2))
#personne = CPersonne(np.array([0, 0]))
