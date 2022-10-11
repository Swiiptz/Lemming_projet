from random import choice
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
        del self     

class Case :
    def __init__(self,caractere:str):
        self.type = caractere
        self.caractere = self.type

    def __str__(self):
        return str(self.caractere)

    def libre(self):
        if self.type == " " or "O":
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
        self.demarre()

    def affiche(self):
        for case_l in self.grotte:
            for case_l_c in case_l :
                if case_l_c == Lemmings:
                    if case_l_c.direction == 1 :
                        print(">")
                    else :
                        print("<")
                    print("\n")
                    continue
                
                #bloc de test
                print(type(case_l_c))
                print(case_l_c,"\n")
                assert case_l_c == Case, "pas type Case"
                

    def tour(self):
        grotte = self.grotte
        for i in self.lemmings :
            l = i.l # on get les coos du lemming
            c = i.c
            if grotte[l-1][c].libre() == True : #check si la case du dessous est libre, si oui descendre
                i.l -= 1
            elif grotte[l][c+1].libre() == True and i.direction == 1 : #si libre à droite et direction droite, aller à droite
                i.c += 1
            elif grotte[l][c-1].libre() == True and i.direction == -1 : #pareil mais à gauche
                i.c -= 1
            else :
                i.direction *= -1 #sinon change de direction
            if grotte[i.l][i.c].type == "O" : #si le lemming est arrivé à la sortie, on le dégage
                i.sort()
        self.affiche()
            


    def demarre(self):
        commande = ""
        while commande != "q" :
            print(f"Que voulez-vous faire :\nl: ajouter un lemming et jouer (nb de lemmings:{len(self.lemmings)})\nq : quitter\nEntrée pour jouer")
            commande = input()
            if commande == "q" :
                break
            if commande == "l":
                self.lemmings.append(Lemmings(choice([1,-1])))
                self.tour()
            else :
                self.tour()






test = Jeu()

