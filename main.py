from random import choice
carte = open("carte.txt")
liste_lemmings = []


class Lemmings :
    pass

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
        self.caractere = lem.str
    def depart(self) :
        self.caractere = self.type

    



class Jeu :
    def __init__(self,grotte,lemmings):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]
        self.lemmings = []
    def tour(self):
        pass
    def affiche(self):
        pass
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
                tour(self)








