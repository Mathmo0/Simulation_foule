
# constante :

c = 0.5
tau = 0.5  # s
SqrtTeta = 0.26  # m/s
Sigma = 0.3  # m
R = 0.2  # m
DeltaT = 2  # s
Phi = 100  # °
VAlphaBeta0 = 2.1  # m**2
UAlphaObstacle0 = 10  # (m/s)**2

class CForce :
    #attribut :

    #constructeur :

    #methode :

    def DetectionCercle(CentreCercle0, CentreCercle1, Point0, Point1, rayon):

        DIstance = (Point0 - CentreCercle0) ** 2 + (Point1 - CentreCercle1 ** 2)
        r2 = (rayon ** 2)
        print("DIstance = ", DIstance)
        if (DIstance <= r2):
            # if((Point[0]-CentreCercle[0])**2 + (Point[1]-CentreCercle[1])**2 <= rayon**2 ) :
            return True
        else:
            return False

            # permet de calculer la vitesse max que peut attindre un piéton

    def VitesseAlphaMax(vAlpha0):
        return 1.3 * vAlpha0

    # Position : Position du pieton à l'intant t
    # PositionDeltaT : Position du pieton à l'intant t+DeltaT
    def VecteurVitesse(Position, PositionDeltaT, t):
        if (t == 0):
            return (0, 0)
        else:
            if (np.linalg.norm((Position - PositionDeltaT) / t) > 1.742):
                return [1.23, 1.23]
            else:
                return (Position - PositionDeltaT) / t

    # Position : Position du pieton à l'intant t
    # PositionDeltaT : Position du pieton à l'intant t- DeltaT
    def FonctionTrajectoirePieton(Position, PositionDeltaT):
        a = (Position[1] - PositionDeltaT[1]) / (Position[1] - PositionDeltaT[1])  # coef directeur
        b = Position[1] - Position[0] * a  # ordonne à l'origine
        coef = np.array([a, b])
        return coef

    # mm

    # Position : Position du pieton à l'intant t
    # PositionDeltaT : Position du pieton à l'intant t-DeltaT
    # PositionB = Position de l'obstacle ou d'un autre piéton
    def Nabla(Position, PositionDeltaT, PositionB):
        coef = np.array([0, 0])
        rAlphaBeta = rAlphaObstacle = (Position - PositionB)
        coef = FonctionTrajectoirePieton(Position, PositionDeltaT)

        return np.array([-rAlphaBeta[1] + coef[0] + coef[1], coef[0] * rAlphaBeta[0] - 1 + coef[1]])

    # vRkAlpha : destination du pieton alpha
    # vRalpha : position du piéton alpha
    def eAlpha(vRkAlpha, vRalpha):

        vdistance = vRkAlpha - vRalpha

        return vdistance / la.norm(vdistance)

    # Ralpha : position du piéton alpha
    # Rbeta : position du piéotn beta
    # vitesseBeta : vitesse du piéton beta
    # vRkBeta : destination du piéton Beta
    def b(Ralpha, Rbeta, vitesseBeta, vRkBeta):

        RalphaBeta = Ralpha - Rbeta
        NormeRalphaBeta = la.norm(RalphaBeta)
        eBeta = eAlpha(vRkBeta, Rbeta)

        calcul = (NormeRalphaBeta + la.norm(RalphaBeta - vitesseBeta * DeltaT * eBeta)) ** 2 - (
                    la.norm(vitesseBeta) * DeltaT) ** 2
        print(calcul)
        Deuxb = math.sqrt(calcul)
        return Deuxb / 2

    def VAlphaBeta(b):
        return VAlphaBeta0 * np.exp(-b / Sigma)

    def UAlphaObstacle(NormeVecteurRAlphaObstacle):
        return UAlphaObstacle0 * np.exp(-NormeVecteurRAlphaObstacle / R)

