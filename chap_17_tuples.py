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
#  Chap. 17     #  Types construits II : les tuples                            #
#               #                                                              #
################################################################################
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
Les tuples sont des séquences d'éléments, comme des listes : la seule différente
est qu'elle sont persistantes ("immutable" en anglais) : on ne peut pas les
modifier une fois créées.

À l'inverses des listes, dont la taille peut varier à l'infini, les tuples
sont utilisées quand on souhaite manipuler des ensembles de taille fixe de
valeurs : un vecteur, une ligne de base de données, etc. On a ensuite la
garantie que le nombre de valeurs et leur emplacement dans le tuple ne changera
jamais.

À part ça, les tuples fonctionnent exactement comme des listes. En français, on
les appelle parfois "p-uplets".
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

Réponse : les tuples offrent simplement la garantie qu'on ne va pas modifier
une valeur dans un programme. Ils permettent ainsi de simuler l'exécution du
programme plus facilement.

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
print(type(l))  # => <class 'tuple'>

# On peut aussi directement affecter plusieurs valeurs :
a, b, c = retours_multiples(3)
print(type(a))  # => <class 'int'>

# Attention, il faut avoir le même nombre de paramètres :
try:
    a, b, c, d = retours_multiples(4)
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Opérations de base
#####################

"""
Comme dans une liste, on peut ranger n'importe quoi dans un tuple, et en
autant d'exemplaires qu'on veut :
"""
pouet = (3.5, ("autre", "tuple!"), False, [2, 5, True], 42, 42)

# À part les parenthèses, la syntaxe est la même pour accéder à un
# élément de la liste
print(pouet[0])  # => 3.5, comme une liste

try:
    pouet[6]  # => IndexError: tuple index out of range (cf. liste)
except IndexError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# On peut utiliser la plupart des opérations des listes sur des tuples
print(len(pouet))  # => 6
print(pouet[:2])  # => (3.5, ('autre', 'tuple!'))
print(pouet[-1])  # => 42
print(42 in pouet)  # => True
print(pouet.index(False))  # => 2 (indice de la première apparition de False)
print(pouet.count(42))  # => 2 (nombre d'apparitions de 4 dans le tuple)

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
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    tup.append(4)  # => AttributeError: 'tuple' object has no attribute 'append'
except AttributeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# Cependant, certaines modifications sont quand même possibles :

# 1. On peut toujours modifier le CONTENU d'un type construit dans un tuple
print(pouet)  # => (3.5, ('autre', 'tuple!'), False, [2, 5, True], 42, 42)
print(pouet[3])  # => [2, 5, True]

pouet[3][0] = 15  # => le tuple contient toujours la même liste, c'est le
# CONTENU de cette dernière qui change
print(pouet[3])  # => [15, 5, True]

# 2. On peut réaffecter le nom d'un tuple à une autre valeur
pouet = "pouet"  # => Pas d'erreur, car le tuple auquel la variable pouet
# faisait référence ne change pas

# 3. On peut enfin remplacer un tuple par un tuple plus grand
tup = tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
# (En fait, il s'agit aussi d'une réaffectation)
