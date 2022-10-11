carte = open("carte.txt")
liste_lemmings = []


class Lemmings :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        liste_lemmings.append(self)


class Case :
<<<<<<< HEAD
    def __init__(self,caractere:str):
=======
<<<<<<< HEAD
    def __init__(self,x,y,grotte,liste_lemmings):
        self.terrain = grotte[x][y]
        for i in liste_lemmings :
            if x == i.x and y == i.y :
                self.lemming = i
            else :
                self.lemming = None 
>>>>>>> 330cba59b5707f313a098d4aa6d5ab34a6d7130f
        
=======
    def __init__(self,caractere):
        self.type = caractere
    
>>>>>>> dev_S


class Jeu :
    def __init__(self,grotte,lemmings):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]

<<<<<<< HEAD

print(grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()])
=======
print([[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()])
>>>>>>> dev_S
