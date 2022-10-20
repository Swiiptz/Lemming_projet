from random import randint

def tkt(longueur:int, hauteur:int):
    tab = []
    tab.append(["#"," ","#"*(longueur-2)])
    longueur-=2
    tab_l = []

    for i in range(longueur) :
        if i%2 == 0: #alors nb impaire
            tab_l = ["#"," "*longueur,"#"]
        else :
            gauche = longueur
            gauche -= randint(1,longueur-1)
            droite = longueur-1 - gauche
            tab_l = ["#",gauche*"#"," ",droite*"#","#"]
        tab.append(tab_l)
    
    tab.append(["O"*(longueur+2)])
    affiche = ""
    for i in tab :
        for z in i :
            affiche += z
        affiche += "\n"
    return affiche
        
print(tkt(15,10))
