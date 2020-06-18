import numpy
from Programme_Mere import *

def calculForcePression(N, F):
    rot = 1025
    g = 9.8
    AB = numpy.array([F[1][0]-F[0][0], F[1][1]-F[0][1], F[1][2]-F[0][2]])
    AC = numpy.array([F[2][0]-F[0][0], F[2][1]-F[0][1], F[2][2]-F[0][2]])
    normale = numpy.array([N[0], N[1], N[2]])
    produitVectoriel = numpy.cross(AB, AC)
    dS = numpy.linalg.norm(produitVectoriel) / 2
    zG = [(F[0][0] + F[1][0] + F[2][0]) / 3, (F[0][1] + F[1][1] + F[2][1]) / 3, (F[0][2] + F[1][2] + F[2][2]) / 3 ]
    FPression = -rot*g*dS*normale*zG[2]
    return FPression

def pousseeArchimede(lstN, lstF):
    PA = [0,0,0]
    for i in range(0, len(lstF)):
        coordG = [(lstF[i][0][0] + lstF[i][1][0] + lstF[i][2][0]) / 3, (lstF[i][0][1] + lstF[i][1][1] + lstF[i][2][1]) / 3, (lstF[i][0][2] + lstF[i][1][2] + lstF[i][2][2]) / 3 ]
        if coordG[2] < 1.5:
            PA[0] = PA[0] + calculForcePression(lstN[i], lstF[i])[0]
            #print("PA0 = ",PA[0])
            PA[1] = PA[1] + calculForcePression(lstN[i], lstF[i])[1]
            #print("PA1 = ",PA[1])
            PA[2] = PA[2] + calculForcePression(lstN[i], lstF[i])[2]
            #print("PA2 = ",PA[2])
    print("Force d'Archimede : ", PA)
    return PA

#boat1 = extractionSTL("Rectangular_HULL.stl")
#boat1 = extractionSTL("V_HULL.stl")
boat1 = extractionSTL("Cylindrical_HULL.stl")
listN, listF = boat1.extractionDesListes()
#print(listN)
#print(listF)
pousseeArchimede(listN, listF)


"""
NTriangle = [-0, 0.70710678118654746, -0.70710678118654746]
FTriangle = [[4, 0, 0], [0, 1, 1], [4, 1, 1]]
NRectangle = [0, -1, -0]
FRectangle = [[0, -1, 0], [2, -1, 0], [2, -1, 1]]
NRectangle2 = [0, 0, 1]
FRectangle2 = [[2.0, -1.0, 1.0], [4.0, 0.0, 1.0], [2.0, 1.0, 1.0]]
"""
NRectangle3 = [0,0,-1]
FRectangle3 = [[2.0, -1.0, 0.0], [0.0, 0.0, 0.0], [2.0, 1.0, 0.0]]

#print(calculForcePression(NTriangle,FTriangle))
print(calculForcePression(NRectangle3,FRectangle3))
