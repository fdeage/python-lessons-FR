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
#  Chap. 4      #  Nombres, opérateurs et arithmétique                         #
#               #                                                              #
################################################################################
#
#  - Les ints
#  - Les floats
#  - La fonction intégrée type()
#  - Arithmétique avec ints et floats
#  - La division entière
#
###########################################

# Les ints
###########

"""
En Python, les nombres sont, par défaut, des entiers représentés en base 10.
Python les appelle des "ints".
"""
print(3)   # => 3

# Ces ints peuvent être négatifs
print(-7)  # => -7

# Ils peuvent être TRÈS grands
print(999999999999999999999999)  # => 999999999999999999999999
# (Il n'y a plus la limite de 2^64 -1 comme dans Python2 : les ints peuvent être
# "arbitrairement grands")

# On peut utiliser le underscore (_) pour séparer les milliers, millions,
# et les puissances de 1000 en général
print(12_345)      # => 12345
print(12_345_678)  # => 12345678

# Les floats
#############

# Les nombres décimaux ("floats") sont représentés avec un point : 'x.y'
print(3.0)    # => 3.0
print(-4.35)  # => -4.35

# Python accepte également une notation scientifique avec "..e..", qui
# retournera un float
print(1e13)      # 10000000000000.0
print(-2.3e-04)  # -0.00023


"""
Complément sur les floats

On appelle aussi les décimaux des "nombres à virgule flottante" ("floating-point
numbers").

En raison de leur usage dans la simulation et les sciences, les calculs sur les
floats servent de référence pour comparer les performances d'ordinateurs
entre eux. On parle alors de "floating point operations per second" (flop/s ou
FLOPS).

Ainsi, l'Apollo Guidance Computer (AGC) embarqué sur Apollo 11 en 1969 avait
une puissance de 14,2 kiloFLOPS (1,42 × 10^4 FLOPS).

La PS5 de Sony (2020) est presque un milliard de fois plus puissante (!), avec
une capacité de 10,3 teraFLOPS (1,03 × 10^13 FLOPS).

Mais c'est 40.000 fois moins que Fugaku, l'ordinateur le plus rapide du monde
(au 01/04/21), qui est capable de 415 petaFLOPS (4,15 × 10^17 FLOPS)…

Au sujet de la représentation interne des floats, on pourra voir la norme
IEEE 754, qui est très intéressante pour comprendre les erreurs sur les floats.
"""

# TODO: erreur sur les floats 3 + 0.00000000000000001

# La fonction intégrée type()
##############################

# On peut utiliser la fonction intégrée type() pour déterminer le type d'une
# valeur
print(type(3))    # => <class 'int'>
print(type(3.0))  # => <class 'float'>
print(type("3"))  # => <class 'str'> (cf. les chaînes de caractères plus loin)

# 3 et 3.0 expriment différemment le même nombre
print(3 == 3.0)     # => True
print(3 == 3.0001)  # => False

"""
IMPT : ce signe "==" sert à tester une égalité. La ligne entière s'appelle une
"expression booléenne" : c'est un type particulier de calcul que Python va
transformer (évaluer) en "Oui" ou "Non", "Vrai" ou "Faux".

Pour tester si une variable est d'un certain type, on peut faire :
type(variable) == <le type testé>

Les types testables sont :
bool, int, float, str, tuple, list, dict
"""
print(type("3") == str)    # => True
print(type(3) == str)      # => False
print(type(True) == bool)  # => False


# Arithmétique avec ints et floats
###################################

# L'arithmétique de base avec des entiers est sans surprise : les calculs avec
# des ints retournent en général un int…
print(12 + 1)  # => 13
print(38 - 1)  # => 37
print(10 * 2)  # => 20

# …seule la division d'ints retournera un float
print(35 / 5)  # => 7.0

# Les calculs avec des floats recèlent quelques surprises…
print(0.1 + 0.2)  # => 0.30000000000000004

"""
Explication : les floats ne peuvent en fait stocker que des valeurs approchées
de nombres décimaux. Cela peut entraîner d'étranges problèmes d'arrondis (c'est
un problème bien connu de la norme IEEE-754…).
"""

# Quand on utilise un float dans un calcul, le résultat sera aussi un float
print(3 + 2.0)  # => 5.0
print(3 * 2.0)  # => 6.0

# Pour obtenir le reste d'une division euclidienne, on utilise l'opérateur
# modulo "%"
print(7 % 3)    # => 1 (en effet 7 = 3 * 2 + 1)

# L'exponentiation s'écrit x ** y ("x élevé à la puissance y")
print(2 ** 5)   # => 32

# Note : on peut aussi utiliser la fonction intégrée pow() (pour "power")
pow(2, 5)       # => 32 aussi

# Attention : l'opérateur ^ n'a rien à voir avec l'exponentation !
print(2 ^ 5)    # => 7 (cf. le chapitre sur les opérateurs de bits)

# On obtient la valeur absolue d'un nombre avec abs()
print(abs(-5))  # => 5
print(abs(3))   # => 3

# La division entière
###########################

# Pour une division entière (qui retournera un int), on utilisera //
# (opérateur appelé "floor division")
print(35 // 5)  # => 7

# Les résultats de divisions entières sont tronqués à l'entier.
print(5 // 3)  # => 1

# Attention avec les négatifs : l'opérateur arrondit toujours "vers le bas" !
print(-5 // 3)  # => -2
print(-5.0 // 3.0)  # => -2.0

# Diviser par un float retournera un float… tout en troquant quand même le
# quotient à l'entier (c'est rarement ce que l'on cherche)
print(5.0 // 3.0)  # => 1.0
