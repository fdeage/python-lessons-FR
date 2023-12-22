################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2023                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 16     #  Types construits I : les listes (I)                         #
#               #                                                              #
################################################################################
#
#  - Définition et intérêt
#  - Déclarer une liste
#  - Accéder à une valeur de la liste
#  - Autres façons de créer une liste
#  - .append(), .pop(), del et +
#  - Fonctions intégrées
#  - Parcourir une liste : TODO
#  - En bref
#  - Matrices
#  - Tri de listes
#  - TODO : D'autres méthodes sur les listes
#  - TODO : Bonus sur les listes
#
###########################################

"""
Introduction : les types construits

Nous allons nous intéresser maintenant à ce qu'on appelle les "types
construits" (par opposition aux "types simples" que sont les booléens, ints et
floats).

Les types construits permettent de stocker non pas une seule valeur, mais
plusieurs valeurs en même temps.

Les principaux types construits de Python sont :
    - les listes (chap. 16),
    - les tuples (chap. 17),
    - les dictionnaires (chap. 18),
    - les ensembles (chap. 22)

Note : les strings sont un cas particulier, de type ni vraiment simple ni
vraiment construit.
"""

# Définition et intérêt
########################

"""
Les listes (similaires aux tableaux en Python) sont des variables qui
permettent de stocker des séquences d'éléments, de toute nature : strings,
ints… ou même d'autres listes !

On peut y ranger simultanément des valeurs de nature différente.
"""

# Les listes sont utiles quand on commence à avoir plusieurs variables de même
# nature. Par exemple :
voiture_1 = "bleue"
voiture_2 = "rouge"
voiture_3 = "jaune"
voiture_4 = "verte"
# …

"""
Si l'on souhaite conserver plus de voitures, il faudra créer une nouvelle
variable à chaque fois, avec le bon numéro à la fin, ce qui pose plusieurs
problèmes :
    - comment ajouter ou supprimer facilement une voiture ?
    - comment s'assurer que l'on ne se trompe pas dans la numérotation ?

Heureusement Python, comme la plupart des langages, nous propose un type pour
"ranger" différentes valeurs dans une seule : la liste.
"""

# On la déclare avec la syntaxe "[…]"
voitures = [voiture_1, voiture_2, voiture_3]
# ou directement :
voitures = ["bleue", "rouge", "jaune"]

"""
On voit déjà ses intérêts :
    - on centralise dans la même variable de valeurs qui "vont ensemble"
    - on évite toute confusion sur la numérotation des valeurs, qui est gérée
      par la liste (on le verra plus loin)
"""


# Déclarer une liste
#####################

# Cette syntaxe crée une liste vide, que l'on pourra remplir plus tard
li = []

# Pour pré-remplir une liste, on énumère les valeurs en les séparant par ","
liste_pre_remplie = [4, 5, 6]

# On peut mélanger les types dans une même liste, et même les imbriquer
liste_variee = ["pouet", 3, 4.5, True, [], "Hop", [1, 2, 3]]

"""
liste_variee contient 7 valeurs, dans l'ordre :
    0. une string : "pouet"
    1. un entier : 3
    2. un float : 4.5
    3. un booléen True
    4. une liste (vide)
    5. encore une string
    6. et enfin une autre liste : [1, 2, 3]
"""


# Accéder à une valeur de la liste
###################################

"""
Une fois ces valeurs stockées dans la liste, on peut y accéder en partant de
leur "ordre" dans la liste.

IMPT: cet ordre commence toujours à 0.
"""
liste_variee[0]  # => "pouet"
liste_variee[3]  # => True
liste_variee[6]  # => [1, 2, 3]

# L'accès au dernier élément peut aussi se faire "par la fin" avec "-n"
liste_variee[-1]  # => [1, 2, 3]

# Accéder à un élément en dehors des limites soulève une IndexError
try:
    liste_variee[7]  # => Lève une IndexError
except IndexError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# La liste vide ne contient, par définition, aucune valeur. Même l'indice 0
# n'existe pas !
liste_vide = []
try:
    liste_vide[0]  # => Lève aussi une IndexError
except IndexError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Pour tester si une valeur est dans une liste, on peut utiliser "… in …" et
son complément "… not in …"
"""
print(1 in liste_pre_remplie)      # => False
print(1 not in liste_pre_remplie)  # => True


# Autres façons de créer une liste
###################################

# Pour déclarer une liste d'éléments identiques, on utilise l'opérateur "*"
["a"] * 4  # => ['a', 'a', 'a', 'a']

# On peut appliquer la fonction intégrée list() sur une séquence :
#   - avec un argument range() pour déclarer une liste d'entiers croissants
liste_entiers_croissants = list(range(5))  # => [0, 1, 2, 3, 4]

#   - avec un argument de type string
liste_caracteres = list("une string")
# ['u', 'n', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']


# .append(), .pop(), del et +
##############################

#   1. On ajoute des objets à la fin d'une liste avec la méthode .append()

# (On rappelle que li est vide)
print(li)  # []

li.append(1)  # li vaut maintenant [1]
li.append(2)  # li vaut maintenant [1, 2]
li.append(4)  # li vaut maintenant [1, 2, 4]
li.append(3)  # li vaut maintenant [1, 2, 4, 3]


#   2. On enlève le dernier élément d'une liste avec la méthode .pop()
dernier = li.pop()  # => dernier vaut 3, li vaut maintenant [1, 2, 4]

# On peut ensuite le remettre en place
li.append(dernier)  # li vaut de nouveau [1, 2, 4, 3]


#   3. Pour supprimer un élément à un rang arbitraire, on utilise "del". C'est
#      utile car .pop() ne peut enlever que le dernier élément (càd le plus à
#      droite de la liste)
del li[2]  # On enlève l'élément de rang 2, li vaut maintenant [1, 2, 3]

"""
Attention, del ne retourne rien ! On ne peut donc pas écrire :

valeur = del li[2]  # Soulève une erreur
"""

"""
    4. On peut additionner des listes ensemble avec l'opérateur "+", comme pour
     les strings
"""
print(li + liste_pre_remplie)  # => [1, 2, 3, 4, 5, 6]

# Note: les valeurs de li et liste_pre_remplie ne sont pas modifiées
print(li)                      # => [1, 2, 3]
print(liste_pre_remplie)       # => [4, 5, 6]


# Fonctions intégrées
######################

"""
IMPT : Python propose des fonctions intégrées pour des listes numériques(càd
constituées d'ints ou de floats uniquement) :
    - len() retourne le nombre d'éléments de la liste
    - max() et min() retournent la plus haute et la plus basse valeur
    - sum() retourne la somme de toutes les valeurs de la liste
"""
# Rappel
print(liste_entiers_croissants)      # => [0, 1, 2, 3, 4]

print(len(liste_entiers_croissants)) # => 5
print(max(liste_entiers_croissants)) # => 4
print(min(liste_entiers_croissants)) # => 0
print(sum(liste_entiers_croissants)) # => 10

# Ainsi, pour calculer la moyenne des notes suivantes…
notes = [17, 12, 14, 9, 19, 11, 14, 14]
# …il suffira de faire :
moyenne = sum(notes) / len(notes)
print(f"Ma moyenne est de {moyenne}")  # => 'Ma moyenne est de 13.75'

# La liste vide a une longueur de 0
len([])  # => 0

"""
IMPT : la fonction intégrée enumerate()

Si l'on souhaite itérer sur les valeurs d'une liste tout en conservant leur
rang, on doit normalement utiliser "range(len(l))" :

Exemple :
"""
l = ["a", "b", "c"]

for i in range(len(l)):    # moche
    print(f"{i} : {l[i]}")

# Avec enumerate(), tout se fait en une ligne :
for i, j in enumerate(l):  # beau
    print(f"{i} : {j}")

"""
Les deux boucles for ci-dessus imprimeront :

0 : a
1 : b
2 : c
"""


# En bref
##########

"""
    - Une liste Python est une collection d'objets numérotés.
    - On accède à un élément de la collection à l'aide de son index (ou
      indice), compté à partir de 0. Ainsi :
"""
liste = [10, 20, 30]
print(liste[0]) # => 10
print(liste[2]) # => 30

#   - Python calcule la longueur de la liste avec l'instruction len(liste)
len(liste) # => 3

#   - Une liste Python est un objet modifiable (ou "mutable") :
liste[1] = 0
print(liste) # => [10, 0, 30]

"""
    - La création d'une liste Python se fait souvent par accumulation : on peut
      partir d'une liste vide…
"""
liste = []
"""
      …et lui ajouter des éléments, le plus souvent "par la droite" (ou
      "par la fin"). Il y a plusieurs possibilités pour cela :
         1. la méthode .append()
"""
liste.append(2)
print(liste) # => [2]

#        2. la fusion de deux listes :

liste = liste + [4]
print(liste) # => [2, 4]
# (on peut donc ajouter "par la gauche" des éléments à une liste avec cette
# technique)

#        3. l'extension par une autre liste avec .extend() :
liste.extend([6, 8])  # => [2, 4, 6, 8]


# Itération sur les listes
##########################

"""
    Il y a deux approches pour réaliser un parcours de liste Python :

    1. itération sur les indices : on commence par énumérer l'ensemble des
       indices (càd les positions des éléments) :
"""
print(liste)  # => [2, 4, 6, 8]

for i in range(len(liste)):
    print(i)
"""
Ceci imprimera les indices des valeurs :
0
1
2
3

    2. itération sur les valeurs : on parcout directement l'ensemble des
       éléments de la liste :
"""
for valeur in liste:
    print(valeur)
"""
Ceci imprimera les valeurs elles-mêmes:
2
4
6
8
"""

# Les deux boucles suivantes font la même chose :
for i in range(len(liste)):
    print(i)


# TODO: dans quel cas utiliser 1 ou 2 ?


# Matrices
###########

# On peut déclarer un tableau à deux dimensions(ou matrices) avec des
# listes dans une liste
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrice[0]  # => [1, 2, 3]
matrice[1][2]  # => 6
matrice[2][0]  # => 7

# Pour avoir les dimensions de la matrice, on va utiliser len()
len(matrice)     # donne la "hauteur" de la matrice (=> son nombre de lignes)
len(matrice[0])  # donne la "largeur" de la première ligne (=> le nombre de
# colonnes).

"""
On supposera que la largeur de la première ligne sera identique aux largeurs
des autres lignes.
"""

"""
Note : il n'y a pas de limites au niveau d'imbrication que l'on peut atteindre !
Voici par exemple une très belle matrice 3D…
"""
liste_3d = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
# …mais en pratique on ira rarement au-delà de 2.


# Tri de listes
################

"""
On a deux options ici :
    1. trier la liste "en place" avec la méthode .sort()
    2. retourner une nouvelle valeur qui contient la liste triée avec sorted()
"""

#   1. On utilise .sort() pour trier une liste "sur place", sans rien retourner…
desordre = [2, 3, 7, 1, 9, 4]
s = desordre.sort()
print(s)  # => None. .sort() ne retourne rien !
desordre  # => [1, 2, 3, 4, 7, 9], la liste de départ est modifiée

#   2. … et on utilise sorted() pour retourner une liste triée sans changer
# l'original
desordre2 = [2, 3, 7, 1, 9, 4]
sorted(desordre2)  # => [1, 2, 3, 4, 7, 9]
desordre  # => [2, 3, 7, 1, 9, 4], la liste de départ n'est pas modifiée

# Note : on inverse une liste sur place avec .reverse()
desordre.reverse()
desordre  # => [9, 7, 4, 3, 2, 1]
