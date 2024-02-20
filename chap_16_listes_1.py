################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2024                    #
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
#  - `.append()`, `.pop()`, `del` et `+`
#  - En bref
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
    - les strings (chap. 7),
    - les listes (chap. 16),
    - les tuples (chap. 17),
    - les dictionnaires (chap. 18),
    - les ensembles (chap. 25)

Les strings ressemblent à un type simple, mais supportent des opérateurs de
types construits. Elles sont en fait très similaires à des listes de caractères.
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
    0. une `string` : "pouet"
    1. un `int` : 3
    2. un `float` : 4.5
    3. un `bool` True
    4. une `list` (vide)
    5. encore une `string`
    6. et enfin une autre `list` : [1, 2, 3]
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


# `len()`, `.append()`, `.pop()`, `del` et `+`
###############################################

#   1. On ajoute des objets à la fin d'une liste avec la méthode `.append()`

# On vérifie que `li` est vide au départ
print(li)  # []

li.append(1)  # `li` vaut maintenant `[1]`
li.append(2)  # `li` vaut maintenant `[1, 2]`
li.append(4)  # `li` vaut maintenant `[1, 2, 4]`
li.append(3)  # `li` vaut maintenant `[1, 2, 4, 3]`


#   2. On enlève le dernier élément d'une liste avec la méthode `.pop()`
dernier = li.pop()  # => `dernier` vaut 3, `li` vaut maintenant `[1, 2, 4]`

# On peut ensuite le remettre en place
li.append(dernier)  # `li` vaut de nouveau `[1, 2, 4, 3]`


"""
    3. Pour supprimer un élément à un rang arbitraire, on utilise `del`. C'est
       utile car `.pop()` ne peut enlever que le dernier élément (càd le plus à
       droite de la liste)
"""
del li[2]  # On enlève l'élément de rang 2, `li` vaut maintenant `[1, 2, 3]`

"""
Attention, `del` ne retourne rien ! On ne peut donc pas écrire :

valeur = del li[2]  # Soulève une erreur
"""

"""
    4. On peut additionner des listes ensemble avec l'opérateur `+`, comme pour
     les strings
"""
print(li + liste_pre_remplie)  # => [1, 2, 3, 4, 5, 6]

# Note: les valeurs de `li` et `liste_pre_remplie` ne sont pas modifiées
print(li)                      # => [1, 2, 3]
print(liste_pre_remplie)       # => [4, 5, 6]


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

#   - Python calcule la longueur de la liste avec l'instruction `len(liste)`
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
         1. la méthode `.append()` :
"""
liste.append(2)
print(liste) # => [2]

#        2. la fusion de deux listes :

liste = liste + [4]
print(liste) # => [2, 4]
# (on peut donc ajouter "par la gauche" des éléments à une liste avec cette
# technique)

#        3. l'extension par une autre liste avec `.extend()` :
liste.extend([6, 8])  # => [2, 4, 6, 8]
