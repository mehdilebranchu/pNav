import numpy as np

class operationSurLesFacettesEtLesNormales():
    def __init__(self, listeNormales, listeFacettes, masseBateau):

        self.__listeN = listeNormales
        self.__listeF = listeFacettes
        self.__masseBateau = masseBateau
        self.__forcePoids = self.__masseBateau * 9.8
        self.__forceArchimede = 0

        self.__coodDeG = []
        self.__forcesPression = []
        self.__niveauEau = 0.5
        self.__tirantEau = 0
        self.__hauteurMax = 0
        self.__hEau = 0

    def getForcePoids(self):
        return self.__forcePoids
    def getForceArchimede(self):
        return self.__forceArchimede
    def getMassBateau(self):
        return self.__masseBateau
    def getNiveauEau(self):
        return self.__niveauEau
    def getTirantEau(self):
        return self.__tirantEau
    def getHauteurMax(self):
        return self.__hauteurMax

    def setMasse(self, masse):
        self.__forcePoids = masse * 9.8
    def setNiveauEau(self, niveau):
        self.__niveauEau = niveau

    def calculForcePression(self, N, F):
        rot = 1025
        g = 9.8
        AB = np.array([F[1][0]-F[0][0], F[1][1]-F[0][1], F[1][2]-F[0][2]])
        AC = np.array([F[2][0]-F[0][0], F[2][1]-F[0][1], F[2][2]-F[0][2]])
        normale = np.array([N[0], N[1], N[2]])
        produitVectoriel = np.cross(AB, AC)
        dS = np.linalg.norm(produitVectoriel) / 2
        zG = [(F[0][0] + F[1][0] + F[2][0]) / 3, (F[0][1] + F[1][1] + F[2][1]) / 3, (F[0][2] + F[1][2] + F[2][2]) / 3 ]
        FPression = -rot*g*dS*normale*abs(zG[2])
        return FPression

    def pousseeArchimede(self):
        PA = [0,0,0]
        for i in range(0, len(self.__listeF)):
            coordG = [(self.__listeF[i][0][0] + self.__listeF[i][1][0] + self.__listeF[i][2][0]) / 3, (self.__listeF[i][0][1] + self.__listeF[i][1][1] + self.__listeF[i][2][1]) / 3, (self.__listeF[i][0][2] + self.__listeF[i][1][2] + self.__listeF[i][2][2]) / 3 ]
            if coordG[2] < self.__hEau:
                PA[0] = PA[0] + self.calculForcePression(self.__listeN[i], self.__listeF[i])[0]
                #print("PA0 = ",PA[0])
                PA[1] = PA[1] + self.calculForcePression(self.__listeN[i], self.__listeF[i])[1]
                #print("PA1 = ",PA[1])
                PA[2] = PA[2] + self.calculForcePression(self.__listeN[i], self.__listeF[i])[2]
                #print("PA2 = ",PA[2])
        print("Force d'Archimede : ", PA)
        PA = np.vdot(PA, PA)**(1/2)
        return PA

    def calculDesCoordonneesDesG(self):
        x = len(self.__listeF)
        for elt in range(0, x) :
            g = []
            X = (self.__listeF[elt][0][0] + self.__listeF[elt][1][0] + self.__listeF[elt][2][0]) / 3
            Y = (self.__listeF[elt][0][1] + self.__listeF[elt][1][1] + self.__listeF[elt][2][1]) / 3
            Z = (self.__listeF[elt][0][2] + self.__listeF[elt][1][2] + self.__listeF[elt][2][2]) / 3
            g.append(X)
            g.append(Y)
            g.append(Z)
            self.__coodDeG.append(g)
        return self.__coodDeG

    def translationDesFacette(self, valeurDeTranslation):
        x = valeurDeTranslation
        for elt in range(0, len(self.__listeF)):
            for elt2 in range(0, 3):
                self.__listeF[elt][elt2][-1] = self.__listeF[elt][elt2][-1] + x
        self.__tirantEau -= x
        return self.__listeF

    def tirantEau(self):
        lst = []
        for i in range(0, len(self.__listeF)):
            for elt in range(0, 3):
                lst.append(self.__listeF[i][elt][2])
        pointLePlusBas = min(lst)
        return self.__niveauEau - pointLePlusBas

    def calculHauteurMaximal(self):
        lst = []
        for i in range(0, len(self.__listeF)):
            for elt in range(0, 3):
                lst.append(self.__listeF[i][elt][2])
        return max(lst)

    def Eq(self):
        #self.translationDesFacette(-x)
        eq = self.pousseeArchimede() - self.__forcePoids
        print("eq =",eq)
        return eq

    def dichotomie(self,hauteurInitial,hauteurMaximal,precision):
            debut = hauteurInitial
            fin = hauteurMaximal
            ecart = np.sqrt((hauteurMaximal-hauteurInitial)**2)
            n = 0
            lst1=[]
            while ecart > precision:
                m = (debut+fin)/2
                print(">> iteration num ",n)
                print("a,m,b",debut,m,fin)
                self.translationDesFacette(-debut)
                archiDebut = self.pousseeArchimede() - self.__forcePoids
                print(self.Eq())
                self.translationDesFacette(debut)
                self.translationDesFacette(-m)
                print(self.Eq())
                archiM = self.pousseeArchimede() - self.__forcePoids
                self.translationDesFacette(m)
                if archiM * archiDebut < 0:
                    fin = m
                else:
                    debut = m
                    ecart = fin-debut
                lst1.append(m)
                n+=1
            lst = [lst1,m,n]
            return lst
