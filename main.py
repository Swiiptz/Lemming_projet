carte = open("carte.txt")



class Lemmings :
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Case :
    def __init__(self,x,y):
        



class Jeu :
    def __init__(self,grotte,lemmings):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]


print(grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()])