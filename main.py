carte = open("carte.txt")

class Jeu:
    def __init__(self,terrain):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in terrain.readlines()]
        self.lemmings = []
        self.demarre()

    def affiche(self):
        """affiche la carte actuelle ainsi que les lemmings qui sont dessus"""
        copie_carte = self.grotte
        
        for i in copie_carte : #on transforme les cases en str
            for z in i :
                if type(z) != str :
                    z = z.caractere

        for i in self.lemmings : #on imprime les lemmings en str sur la carte
            if i.d == 1 :
                dir = ">"
            else :
                dir = "<"
            print(i.l,i.c)
            copie_carte[i.l][i.c] = dir

        #on affiche la carte :
        for case_l in copie_carte: #on prend la ligne
            ligne_temp = ""
            for case_l_c in case_l : #puis case par case
                ligne_temp += str(case_l_c)
            print(ligne_temp)


    def tour(self):
        """joue un tour"""
        for i in self.lemmings :
            i.action()
        self.affiche()
            

    def demarre(self):
        """lance le jeu"""
        commande = ""
        while commande != "q" :
            print(f"Que voulez-vous faire :\nl: ajouter un lemming et jouer (nb de lemmings:{len(self.lemmings)})\nq : quitter\nEntrée pour jouer")
            commande = input()
            if commande == "q" :
                break
            if commande == "l":
                self.lemmings.append(Lemmings(self.grotte))
                self.tour()
            else :
                self.tour()


class Lemmings :
    def __init__(self, grotte):
        self.l = 0
        self.c = 1
        self.d = 1
        self.carte = grotte
    def __str__(self):
        if self.d == 1:
            return ">"
        if self.d == -1:
            return "<"
    def action(self):
        if self.carte[self.l+1][self.c].libre():
            self.l +=1
        #elif self.carte[self.l][self.c+1].libre() and :
        #    self.d *=-1
        elif self.carte[self.l][self.c+1].libre():
            self.c += self.d
    def sort(self):
        del self     

class Case :
    def __init__(self,caractere:str):
        self.type = caractere
        self.caractere = self.type

    def __str__(self):
        return str(self.caractere)

    def libre(self):
        if self.type == (" " or "O"):
            return True 
        else :
            return False

    def arrivee(self, lem:Lemmings):
        self.caractere = str(lem)

    def depart(self) :
        self.caractere = self.type


test = Jeu(carte)
