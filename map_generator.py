from random import *

def tkt(longueur:int, hauteur:int):
    tab = []
    tab.append(["#"," ","#"*(longueur-2)])
    longueur-=2
    tab_l = []
    i = longueur
    while i != 0 :
        liste_structures = ['normal']*5+ ['trou']
        structure = liste_structures[randint(0,len(liste_structures)-1)]
        if i%2 != 0: #alors nb paire
            tab_l = ["#"]+[" "]*longueur+["#"]
            tab.append(tab_l)
            temp = randint(0, longueur)
            tab_l = ["#"]+[" "]*longueur+["#"]
            tab_l[temp] = "^"
            i-=2
            tab.append(tab_l)
            
        elif i >=3 and structure == 'trou' :
            #setup des variables
            gauche = longueur
            gauche -= randint(1,longueur-1)
            droite = longueur-1 - gauche
            temp = [randint(1,gauche),randint(droite,longueur-1)]
            passage = choice(temp)

            #construction de la structure
            tab_l = ["#"]+gauche*["#"]+[" "]+droite*["#"]+["#"]
            tab_l[passage] = " "
            tab.append(tab_l)
            tab_l = ["#"]+(gauche-1)*[" "]+["# #"]+(droite-1)*[" "]+["#"]
            tab.append(tab_l)
            tab_l = ["#"]+(gauche-1)*[" "]+["###"]+(droite-1)*[" "]+["#"]
            tab.append(tab_l)
            i-=3
            
        else :
            gauche = longueur
            gauche -= randint(1,longueur-1)
            droite = longueur-1 - gauche
            tab_l = ["#",gauche*"#"," ",droite*"#","#"]
            i-=1
            tab.append(tab_l)
        
    
    tab.append(["O"*(longueur+2)])
    affiche = ""
    for i in tab :
        for z in i :
            affiche += z
        affiche += "\n"
    file = open("carte2.txt",'w')
    file.write(affiche)
    return affiche
        
print(tkt(15,10))
