import numpy as np

list1 = [10, 15]
list2 = [1, 5]

a = np.array(list1)
b = np.array(list2)

<<<<<<< HEAD


=======
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
    print(a)
    v = vitesse(a, b)
    print(v)
    ealpha = (b - a)/np.linalg.norm((a - b), ord=1)
    print(ealpha)
    a = a + nouvellepos(ealpha*1.34, v)
    dt += 2
>>>>>>> 400a72c9547d6615064e7306fe558174b369c4a0
