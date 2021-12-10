import numpy as np
from Code.Modele.COperation import COperation
from Code.Modele.CForce import CForce
import queue # pas fou
from collections import deque

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

'''
Position = np.array([1, 3])
PositionDeltaT = np.array([4, 9])
PositionB = np.array([5, 5])
#resultat = COperation.Nabla(Position, PositionDeltaT, PositionB)
force = CForce()
resultat =force.UAlphaObstacle(4)

print(round(resultat * (10 ** (8)), 2))

'''

#test FIFO avec queu : conclu pas ouf car get supprime en même tps l'objet
'''
q1 = queue.Queue(2)
q1.put(1)
q1.put(2)
#q1.put(3)
print("size = ", q1.qsize())
print("object = ",q1.get())
print("size = ", q1.qsize())
print(q1.empty())

q1.put(2)
q1.get(0)

print("--------------")
print(q1.get(0))
print(q1.get(1))
q1.get
q1.put(3)
print("--------------")
print(q1.get(0))
print(q1.get(1))
'''

##test FIFO avec Deque : conclusion ==> pas ouf
'''
q = deque()
q.append(1)
q.append(2)
print(q)
q.pop(0)
print(q)
'''

#test FIFO juste avec [] : ==> NICKEL
q = []
q.append(1)
q.append(2)
print(q)
q.pop(0)
print(q)