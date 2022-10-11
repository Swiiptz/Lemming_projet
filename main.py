carte = open("carte.txt")
liste_lemmings = []


class Lemmings :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        liste_lemmings.append(self)
    def 

class Case :
    def __init__(self,caractere):
        self.type = caractere
    def libre(self):
        if self.type == " " :
            return True 
        else :
            return False
    def arrivee(self, lem):
        self.caractere = lem.str()
    def depart(self) :
        self.caractere = self.type()

    



class Jeu :
    def __init__(self,grotte,lemmings):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]



print([[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()])

