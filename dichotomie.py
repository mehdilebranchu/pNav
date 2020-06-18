from calculArchimede import *
import numpy as np

def Eq(self, hauteur):
    poids = 9.81 * 4000
    self.pousseArchimede() - poids
def dichotomie(self,hauteurInitial,hauteurMaximal,precision):
        debut = hauteurInitial
        fin = hauteurMaximal
        ecart = np.sqrt((hauteurMaximal-hauteurInitial)**2)
        n = 0
        lst1=[]
        while ecart> precision:
            m = (debut+fin)/2
            if self.Eq(m)*self.Eq(hauteurInitial) < 0:
                fin = m
            else:
                debut = m
                ecart = fin-debut
            lst1.append(m)
        n+=1
        lst = [lst1,m,n]
        return lst
