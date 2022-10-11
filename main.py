carte = open("carte.txt")
liste_lemmings = []


class Lemmings :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        liste_lemmings.append(self)


class Case :
    def __init__(self,x,y,grotte,liste_lemmings):
        self.terrain = grotte[x][y]
        for i in liste_lemmings :
            if x == i.x and y == i.y :
                self.lemming = i
            else :
                self.lemming = None 
        



class Jeu :
    def __init__(self,grotte,lemmings):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]


print(grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()])