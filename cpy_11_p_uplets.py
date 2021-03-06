################################################################################
#                                                                              #
#  NNNN    NNN    SSSSSS.   IIIII   (inspiré de https://learnxinyminutes.com)  #
#  NNNNN   NNN  SSSS  SSSS   III                                               #
#  NNNNNN  NNN  SSSS         III    Licence : CC BY-SA 4.0 FR                  #
#  NNNNNNN NNN   SSSSSS      III    Félix Déage - MMXXI                        #
#  NNN NNNNNNN      SSSSS    III                                               #
#  NNN  NNNNNN        SSSS   III    Cours Python - 1ère - v.3.4                #
#  NNN   NNNNN  SSSS  SSSS   III                                               #
#  NNN    NNNN   SSSSSSSS   IIIII                                              #
#                                                                              #
################################################################################
#               #                                                              #
#  Part. XI     #  types construits II : p-uplets                              #
#               #                                                              #
################################################################################

###############################
# 17. P-uplets (ou tuples)    #
###############################
#
#  - Définition et création
#  - Intérêt des tuples
#  - Opérations de base
#  - Modifier un tuple
#
###############################

# Définition et création
#########################

"""
Les p-uplets (ou tuples en Python) sont des séquences d'éléments,
comme des listes, mais persistants (immutable en anglais) : on ne peut pas
les modifier une fois créées.

À l'inverses des listes, dont la taille peut varier à l'infini, les p-uplets
sont utilisées quand on souhaite manipuler des ensembles de taille fixe de
valeurs : un vecteur, une ligne de base de données, etc.

Les p-uplets fonctionnent exactement comme des listes. Ils sont moins utilisés
qu'elles, mais il faut les connaître.
"""

# On les déclare avec des parenthèses autour d'une séquence de valeurs…
tuple_vide = ()
tup = (1, 2, 3, 4)
tup  # => (1, 2, 3, 4)

type(tup)  # => <class 'tuple'>

# …mais il est fréquent de rencontrer aussi cette écriture sans parenthèses
tup_alternatif = 4, 5, 6
tup_alternatif  # => 4, 5, 6

# Pour un tuple à une seule valeur, il faut ajouter une virgule finale (pour
# éviter la confusion avec un entier entre parenthèses)
(1)  # le nombre 1 entre parenthèses…
(1,)  # …un tuple à une seule valeur

type((1))  # => <class 'int'>
type((1,))  # => <class 'tuple'>


# Intérêt des tuples
#####################

"""
Question : quel intérêt de ne pas pouvoir faire autant de choses qu'avec une
liste normale ?

Réponse : les tuples offrent simplement la garantie qu'on ne va pas
modifier une valeur dans un programme. Ils permettent ainsi de simuler
l'exécution du programme plus facilement.

Les tuples n'ont aucune autre particularité par rapport aux listes.
"""

# Comme pour les listes, on peut affecter plusieurs variables avec un seul
# tuple
a, b, c = (1, 2, 3)  # a vaut 1, b vaut 2 et c vaut 3
type(a)  # => <class 'int'>
type(b)  # => <class 'int'>
type(c)  # => <class 'int'>

# On les utilise souvent si on veut une fonction qui retourne plusieurs valeurs
def retours_multiples(parametre):
    valeur1 = parametre * 2
    valeur2 = parametre + 8
    valeur3 = parametre / 3
    return valeur1, valeur2, valeur3

l = retours_multiples(2)
type(l)  # => <class 'tuple'>


# Opérations de base
#####################

# Comme dans une liste, on peut ranger n'importe quoi dans un tuple, et en
# autant d'exemplaires qu'on veut
pouet = (3.5, ("autre", "tuple!"), False, [2, 5, True], 42)

# À part les parenthèses, la syntaxe est la même pour accéder à un
# élément de la liste
tup[0]  # => 1, comme une liste

try:
    tup[6]  # => IndexError: tuple index out of range (cf. liste)
except IndexError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# On peut utiliser la plupart des opérations des listes sur des tuples
len(tup)  # => 4
tup[:2]  # => (1, 2)
2 in tup  # => True
tup.index(4)  # => 3 (indice de la première apparition de 4)
tup.count(4)  # => 1 (nombre d'apparitions de 4 dans le tuple)

# IMPT : on peut intervertir le contenu de deux variables avec la
# syntaxe a, b = b, a
x = 2
y = 3
y, x = x, y  # y vaut maintenant 2 et y vaut 3


# Modifier un tuple
####################

# Si on essaie de modifier le tuple, les méthodes courantes échoueront :
try:
    tup[0] = 1  # => TypeError: 'tuple' object does not support item assignment
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    tup.append(4)  # => AttributeError: 'tuple' object has no attribute 'append'
except AttributeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# Cependant, certaines modifications sont quand même possibles :

# 1. On peut toujours modifier le CONTENU d'un élément dans un tuple
pouet  # => (3.5, ("autre", "tuple!"), False, [2, 5, True], 42)

pouet[3]  # => [2, 5, True]
pouet[3][0] = 15  # => le tuple contient toujours la même liste, c'est le
# CONTENU de cette dernière qui change
pouet[3]  # => [15, 5, True]

# 2. On peut réaffecter le nom d'un tuple à une autre valeur
pouet = "pouet"  # => Pas d'erreur, car le tuple auquel la variable pouet
# faisait référence ne change pas

# 3. On peut enfin remplacer un tuple par un tuple plus grand
tup = tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
# (En fait, il s'agit aussi d'une réaffectation)
