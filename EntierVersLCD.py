#+-----------------------------------------------------------+
#+    Code Python decomposant un entier en liste de chiffres +
#+       et impression de ces chiffres en format LCD         +
#+                   fait le 28-01-2021                      +
#+                 par : Ahmed Islam KIMOUR                  +
#+-----------------------------------------------------------+
import sys
# fonction decomposant un entier en liste de chiffres  
def decomposerEntier(): 
    """
    ex: 
       n = 43365644
       res = [4, 3, 3, 6, 5, 6, 4, 4]
           
    """
    
    print("\n")

    # verifier si l'entrée est un entier
    cpt = 1 # compteur de nombres de tentives fausses d'entrée 
    num = input("introduire un entier: ") 

    while not num.isdigit() and cpt < 3:
       num = input("introduire un entier: ") 
       cpt += 1

    if cpt < 3: #num est un entier
     
       listChfr =  [int(d) for d in num]
       print("l'entier: "+num+" est composé des chiffres suivants: ")
       print(listChfr)
       return listChfr 

    # apres 3 tentatives d'entrée de autres qu'entier
    print("désolé, on veut un entier")
    sys.exit()

#+-----------------------------------------------------------+
# fonction imprimant un chiffre en LCD


def traiterChfr(listChfr): 
     #il y a 7 lignes par chiffres
     for i in range(7): # i indique la ligne
          print(" ")
          lignAimprimer = []  
          for chfr in listChfr:# prendre un chiffre
            ligneChfr = dictChfrs[chfr] # tirer son code du dictionnaire
            ligne = ligneChfr[i] # on prend ligne numero i 
            for point in ligne :
                if point == 0:
                   lignAimprimer.append(" ")
                    
                elif point == 1:
                   lignAimprimer.append("-")
                   
                elif point == 2:
                   lignAimprimer.append("|")

            lignAimprimer.append(" ")#  separateur
          #imprime la ligne contenant symboles de tous les chiffres de l'entier entrée        
          for car in lignAimprimer:
            print(car,end=" ")  
#+-----------------------------------------------------------+

#+----------------- programme principal -----------+
global dictChfrs
 
dictChfrs = {0:[[0,1,1,0],[2,0,0,2],[2,0,0,2],[2,0,0,23],[2,0,0,2],[2,0,0,2],
               [0,1,1,0]],
            1:[[0,0,0,0],[0,2,0,0],[0,2,0,0],[0,2,0,0],[0,2,0,0],[0,2,0,0],
               [0,0,0,0]],
            2:[[0,1,1,0],[0,0,0,2],[0,0,0,2],[0,1,1,0],[2,0,0,0],[2,0,0,0],
               [0,1,1,0]],
            3:[[0,1,1,0],[0,0,0,2],[0,0,0,2],[0,1,1,0],[0,0,0,2],[0,0,0,2],
               [0,1,1,0]],
            4:[[0,0,0,0],[2,0,0,2],[2,0,0,2],[0,1,1,0],[0,0,0,2],[0,0,0,2],
               [0,0,0,0]],
            5:[[0,1,1,0],[2,0,0,0],[2,0,0,0],[0,1,1,0],[0,0,0,2],[0,0,0,2],
               [0,1,1,0]],
            6:[[0,1,1,0],[2,0,0,0],[2,0,0,0],[0,1,1,0],[2,0,0,2],[2,0,0,2],
               [0,1,1,0]],
            7:[[0,1,1,0],[0,0,0,2],[0,0,0,2],[0,1,1,0],[0,0,0,2],[0,0,0,2],
               [0,0,0,0]],
            8:[[0,1,1,0],[2,0,0,2],[2,0,0,2],[0,1,1,0],[2,0,0,2],[2,0,0,2],
               [0,1,1,0]],
            9:[[0,1,1,0],[2,0,0,2],[2,0,0,2],[0,1,1,0],[0,0,0,2],[0,0,0,2],
               [0,1,1,0]] }

choix = " "

while choix not in "qQ": 
    #lecture d'un entier et sa décomposition en une liste de chiffres
    Lch = decomposerEntier() #Lch: liste de chiffres
    traiterChfr(Lch)
    # si on veut introduire un autre entier 
    choix = input("presser q pour quitter, autre caractere pour un autre entier ")




   




