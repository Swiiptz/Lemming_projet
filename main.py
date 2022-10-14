carte = open("carte.txt")

class Jeu:
    def __init__(self,terrain):
        self.grotte = [[Case(caractere) for caractere in ligne if caractere !='\n'] for ligne in terrain.readlines()]
        self.lemmings = []

    def affiche(self):
        """affiche la carte actuelle ainsi que les lemmings qui sont dessus"""
        copie_carte = self.grotte
        
        assert len(self.lemmings)>0, "Il n'y a pas de lemming existant"
        for lemming in self.lemmings : #on remplace les cases par les lemmings aux bonnes cos
            copie_carte[lemming.l][lemming.d] = lemming

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
    def __init__(self, caractere):
        self.caractere = caractere
        self.Lemming = False
        if caractere == "#" :
            self.terrain = "mur"
        elif caractere == " " :
            self.terrain = "vide"
        elif caractere == "O" :
            self.terrain = "sortie"

    def __str__(self):
        return self.caractere

    def libre(self):
        if self.Lemming  :
            return False
        elif self.terrain == ("vide" or "sortie"):
            return True 
        else :
            return False

    def arrivee(self, lem:Lemmings):
        self.Lemming = True
        if self.terrain == "sortie" :
            lem.sort()
            self.Lemming = False
        

    def depart(self) :
        self.Lemming = False







test = Jeu(carte).affiche()
