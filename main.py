from random import choice
from zipfile import PyZipFile
carte = open("carte.txt")

    
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
        pass #en chantier       

class Case :
    def __init__(self,caractere:str):
        self.type = caractere
        self.caractere = self.type
    def __str__(self):
        return str(self.caractere)
    def libre(self):
        if self.type == " " :
            return True 
        else :
            return False
    def arrivee(self, lem:Lemmings):
        self.caractere = str(lem)
    def depart(self) :
        self.caractere = self.type

class Jeu:
    def __init__(self):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]
        self.lemmings = []
    def affiche(self):
        for n_lemming in self.grotte:
            if n_lemming == Lemmings:
                print("x")
                continue
            print(n_lemming)
    def tour(self):
        tkt = self.lemmings
        for i in tkt :
            pass #en chantier
            


    def demarre(self):
        commande = ""
        while commande != "q" :
            print("Que voulez-vous faire :\nl: ajouter un lemming\nq : quitter\nEntrée pour jouer")
            commande = input()
            if commande == "q" :
                break
            if commande == "l":
                self.lemmings.append(Lemmings(choice([1,-1])))
            else :
                self.tour()








