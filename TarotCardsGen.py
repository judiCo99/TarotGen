#by judi_Co
author = "judi_Co"
Version = "1.2"

import random

#==========================================
#dictionnaire des carte
#cards dictionary
Cards = {
    "1": ["1", 0.5], 
    "2": ["2", 0.5], 
    "3": ["3", 0.5],
    "4": ["4", 0.5], 
    "5": ["5", 0.5], 
    "6": ["6", 0.5], 
    "7": ["7", 0.5], 
    "8": ["8", 0.5], 
    "9": ["9", 0.5], 
    "10": ["10", 0.5], 
    "Valet": ["Valet", 2], 
    "Cavalier": ["Cavalier", 3],
    "Dame": ["Dame", 4], 
    "Roi": ["Roi", 5]
}
CardsExcuse = {"Excuse":["Excuse",5]}

CardsAtout = {
    "1":["1", 5],
    "2":["2", 0.5],
    "3":["3", 0.5],
    "4":["4", 0.5],
    "5":["5", 0.5],
    "6":["6", 0.5],
    "7":["7", 0.5],
    "8":["8", 0.5],
    "9":["9", 0.5],
    "10":["10", 0.5],
    "11":["11", 0.5],
    "12":["12", 0.5],
    "13":["13", 0.5],
    "14":["14", 0.5],
    "15":["15", 0.5],
    "16":["16", 0.5],
    "17":["17", 0.5],
    "18":["18", 0.5],
    "19":["19", 0.5],
    "20":["20", 0.5],
    "21":["21", 5]
}

#==========================================
#initialisation des liste de carte
#cards liste init
def piocheD(Cards=Cards):

    Piques = {}
    for cle, Valeur in Cards.items():
        Piques[f"{cle} de Piques"] = Valeur

    Carreaux = {}
    for cle, Valeur in Cards.items():
        Carreaux[f"{cle} de Carreaux"] = Valeur

    Coeurs = {}
    for cle, Valeur in Cards.items():
        Coeurs[f"{cle} de Coeurs"] = Valeur

    Tréfles = {}
    for cle, Valeur in Cards.items():
        Tréfles[f"{cle} de Tréfles"] = Valeur


    #==========================================
    #Pile de cartes
    #Stack of cards
    Pile = {}

    Pile.update(Piques)
    Pile.update(Carreaux)
    Pile.update(Coeurs)
    Pile.update(Tréfles)
    Pile.update(CardsAtout)
    Pile.update(CardsExcuse)

    #==========================================
    #mélanger la pile de carte
    #shuffle cards
    Keys = list(Pile.keys())
    random.shuffle(Keys)
    pioche = {}
    for key in Keys:
        pioche.update({key:Pile[key]})
    return pioche

#==========================================
#Liste des carte
#cards List
def piocheL(pioche=piocheD()):
    for cle in pioche.keys():
        Cles = list(pioche)
    return Cles

#===============================
def piocheLD(pioche=piocheD()):
    D = pioche
    for L in pioche.keys():
        L = list(pioche)

    return L, D

#==========================================
def Score(Paquet):
    Score = 0
    sup = []
    for cle, Value in Paquet.items():
        if Value[1] > 0.5:
            Score += Value[1]
            sup.append(cle)
    Nbsup=len(sup)
    for x in sup:
        del Paquet[x]
    sup = []
    for L in Paquet.keys():
        L = list(Paquet)
    for N in range(Nbsup):
        sup.append(L[N])
    for x in sup:
        del Paquet[x]
    S=len(Paquet)
    S = S/2
    Score += S   
    return Score

#==========================================
#ajouter True en variable dans les appelle de fonction pour ajouter les jocker
#add True as a variable in the function calls to add the wildcards

#stocker les cartes
#stock cards
#Liste = piocheL()
#dictionnaire = piocheD()
#List, dic = piocheLD()

#afficher les cartes sous forme de Liste
#display maps in List form
#print(piocheL())

#afficher les cartes sous forme de dictionnaire
#display maps in dictionary form
#print(piocheD())

#piocheLD() retourne à une liste et un dictionnaire identiques
#piocheLD() return to an identical list and dictionary
#print(piocheLD())        #no arg = list and dictionary
#print(piocheLD()[0])     #[0] = List
#print(piocheLD()[1])     #[1] = dictionary

#donner un paquet de carte a la fonction et il retourne le score de se paquet
#give a card deck to the function and it returns the score of that deck 
#Score(Paquet)
#print(Score(Paquet))
#==========================================
