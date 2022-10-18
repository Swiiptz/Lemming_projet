import os
class Lemmings :
    def __init__(self,jeu):
        self.l = 0
        self.c = 1
        self.d = 1
        self.jeu = jeu
        self.carte = self.jeu.grotte
    def __str__(self):
        if self.d == 1:
            return ">"
        if self.d == -1:
            return "<"
    def action(self):
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
            if self.terrain == "sortie":
                return True
        
class Case :
    def __init__(self, caractere):
        self.caractere = caractere
        self.Lemming = None
        if caractere == "#" :
            self.terrain = "mur"
        elif caractere == " " :
            self.terrain = "vide"
        elif caractere == "O" :
            self.terrain = "sortie"

    def __str__(self):
        if self.Lemming !=None :
            return str(self.Lemming.__str__())
        else : 
            return self.caractere

    def libre(self):
        if self.Lemming!=None:
            return False
        if self.terrain == "vide" or self.terrain=="sortie":
            return True 
        else :
            return False

    def arrivee(self, lem):
        self.Lemming = lem
    
    def sortie(self):
        if self.terrain == "sortie" :
            self.Lemming =None
            return True
        
    def depart(self) :
        self.Lemming = None
class Jeu:
    def __init__(self):     
        carte = open("carte.txt")
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in carte.readlines()]
        self.lemmings = []
    def affiche(self):
        #for i in self.lemmings:
        #    self.grotte[i.l][i.c]=i.__str__()
        
        for case_l in self.grotte: #on prend la ligne
            ligne_temp = ""
            for case_l_c in case_l : #puis case par case
                    ligne_temp += case_l_c.__str__()
            print(ligne_temp)
        
    def tour(self):
        """joue un tour"""
        #print(self.lemmings)
        self.affiche()
        n=0
        for i in self.lemmings :
            
            if i.action()==-1:
                self.lemmings.pop(n)
            n+=1
            i.action()
            
    def demarre(self):
        """lance le jeu"""
        commande = ""
        print(f"Que voulez-vous faire :\nl: ajouter un lemming et jouer (nb de lemmings:{len(self.lemmings)})\nq : quitter\nEntree pour jouer")
        while commande != "q" :
            commande = input()
            os.system('cls')
            if commande == "q" :
                break
            if commande == "l":
                new_lemmings = Lemmings(self)
                self.lemmings.append(new_lemmings)
  
                self.tour()
            else :
                self.tour()


Jeu().demarre()