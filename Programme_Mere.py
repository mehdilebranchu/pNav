from OperationSurFichierSTL import *

class extractionSTL():
    def __init__(self, chemin):
        self.__cheminSTL = chemin
        self.__listeFacette = []
        self.__listeNormales = []

    def extractionDesListes(self):
        fileHandle = open(self.__cheminSTL,"r")
        chaine = fileHandle.read()
        lst = chaine.split("\n")
        lst.remove(lst[0])
        lst.remove(lst[-1])
        x = len(lst)
        while x > 1 :
            self.lectureBlocDeSeptLignes(lst[:7])
            x = x-7
            lst = lst[-x:]
        print("Data has been successfully extracted\n\n")
        return self.__listeNormales, self.__listeFacette

    def lectureBlocDeSeptLignes(self, lst):
        lst.remove(lst[-1])
        lst.remove(lst[-1])
        lst.remove(lst[1])
        for elt in range(0, 4):
            lst[elt] = lst[elt].split(" ")
        self.__listeNormales.append([float(lst[0][-3]), float(lst[0][-2]), float(lst[0][-1])])
        lst.remove(lst[0])
        Vertex3 = []
        for elt2 in range(0, 3) :
            liste = [float(lst[elt2][-3]), float(lst[elt2][-2]), float(lst[elt2][-1])]
            Vertex3.append(liste)
        self.__listeFacette.append(Vertex3)
        return

def initialisation():

    print("Select : 1 for Rectangular / 2 for V boat / 3 for Mini650 / 4 for Cylindrical")
    number = int(input("Enter your choice : "))
    while number > 4 or number < 1:
        number = int(input("error\nEnter your choice : "))
    number -= 1
    lstChoice = ["Rectangular_HULL.stl","V_HULL.stl", "Mini650_HULL.STL","Cylindrical_HULL.stl"]
    masseBoat = int(input("Enter mass in kilograms : "))
    print("The path chosen is : ", lstChoice[number])

    chemin = lstChoice[number]
    masseBoat = masseBoat
    return chemin, masseBoat

def start():
    chemin, masseboat = initialisation()
    print("Start extraction stl file...")
    stl = extractionSTL(chemin)
    listN, listF = stl.extractionDesListes()
    return chemin, masseboat, listN, listF
