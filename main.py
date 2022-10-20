from map_generator import *

class Lemmings :
    def __init__(self,jeu):
        self.l = 0
        self.c = 1
        self.d = 1
        self.jeu = jeu
        self.carte = self.jeu.grotte
    def __str__(self):
        """valeur par défaut de print(Lemmings)"""
        if self.d == 1:
            return ">"
        if self.d == -1:
            return "<"
    def action(self):
        """fait bouger le lemming"""
        if self.carte[self.l][self.c].sortie():
            return -1
        self.carte[self.l][self.c].depart()

        
        if self.carte[self.l+1][self.c].libre() :
            self.l += 1
        elif self.carte[self.l][self.c + self.d].libre() :
            self.c += self.d
        else :
            self.d *=-1
        
        self.carte[self.l][self.c].arrivee(self)
        
        def sort(self):
            """sort le lemming du jeu"""
            if self.terrain == "sortie":
                return True
        
class Case :
    def __init__(self, caractere:str):
        self.caractere = caractere
        self.Lemming = None
        if caractere == "#" :
            self.terrain = "mur"
        elif caractere == " " :
            self.terrain = "vide"
        elif caractere == "O" :
            self.terrain = "sortie"

    def __str__(self):
        """valeur par défaut pour print(Case)"""
        if self.Lemming !=None :
            return str(self.Lemming.__str__())
        else : 
            return self.caractere

    def libre(self)->bool:
        """vérifie si la case est libre"""
        if self.Lemming!=None:
            return False
        if self.terrain == "vide" or self.terrain=="sortie":
            return True 
        else :
            return False

    def arrivee(self, lem:Lemmings) -> None :
        """place le lemming sur las case"""
        self.Lemming = lem
    
    def sortie(self):
        """enleve le lemming si la case est une sortie"""
        if self.terrain == "sortie" :
            self.Lemming =None
            return True
        
    def depart(self) :
        """enleve le lemming de la case"""
        self.Lemming = None
        
class Jeu:
    def __init__(self) :   
        """cree un objet jeu"""  
        carte = int(input("Sur quelle carte voulez-vous jouer ?\ncarte 1 : 1\ncarte aléatoire : 2\n"))
        if carte == 1 :
            carte = open("carte.txt")
        if carte == 2 :
            tkt(randint(6,20), randint(6,15))
            carte = open("carte2.txt")
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]
        self.lemmings = []
    def affiche(self):
        """affiche l'etat actuel de la partie"""
        for case_l in self.grotte: #on prend la ligne
            ligne_temp = ""
            for case_l_c in case_l : #puis case par case
                    ligne_temp += case_l_c.__str__()
            print(ligne_temp)
        
    def tour(self):
        """joue un tour"""
        n=0
        for i in self.lemmings :
            i.action()


        self.affiche()

    def demarre(self):
        """lance le jeu"""
        commande = ""
        n_tour = 0
        self.affiche()
        while commande != "q" :
            n_tour += 1
            print(f"Tour n°{n_tour}")
            print(f"Que voulez-vous faire :\nl: ajouter un lemming et jouer (nb de lemmings:{len(self.lemmings)})\nq : quitter\nEntree pour jouer")
            commande = input()
            if commande == "q" :
                break
            if commande == "l":
                new_lemmings = Lemmings(self)
                self.lemmings.append(new_lemmings)
  
                self.tour()
            else :
                self.tour()

Jeu().demarre()