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
#  Chap. 23     #  Types construits I : les listes (II)                        #
#               #                                                              #
################################################################################
#
#  - Fonctions intégrées
#  - Autres façons de créer une liste
#  - Parcourir une liste : TODO
#  - Matrices
#  - Tri de listes
#  - TODO : D'autres méthodes sur les listes
#  - TODO : Bonus sur les listes
#
###########################################

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
