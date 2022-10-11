carte = open("carte.txt")


class Jeu:
    def __init__(self):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]
        
            
    def affiche(self):
        for n_lemming in self.grotte:
            if n_lemming == Lemmings:
                print("x")
                continue
            print(n_lemming)
class Lemmings :
    def __init__(self,direction):
        self.l = 0
        self.c = 1
        self.d = direction
        self.jeu = Jeu
    def __str__(self):
        if self.d == 1:
            return ">"
        if self.d == -1:
            return "<"
    def action(self):
        if self.jeu[self.l,self]:

            self.l +=self.d
    def sort(self):
        pass


        

class Case :
    def __init__(self,caractere):
        self.type = caractere
    



print([[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()])
