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
#  Chap. 4      #  Nombres, opérateurs et arithmétique                         #
#               #                                                              #
################################################################################
#
#  - Les ints
#  - Les floats
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

# On peut utiliser le underscore (`_`) pour séparer les milliers, millions,
# et les puissances de 1000 en général
print(12_345)      # => 12345
print(12_345_678)  # => 12345678


# Les floats
#############

# Les nombres décimaux ("floats") sont représentés avec un point : `x.y`
print(3.0)    # => 3.0
print(-4.35)  # => -4.35

# Python accepte également une notation scientifique avec `..e..`, qui
# retournera un float
print(1e13)      # 10000000000000.0
print(-2.3e-04)  # -0.00023


# Arithmétique avec ints et floats
###################################

# L'arithmétique de base avec des entiers est sans surprise : les calculs avec
# des ints retournent en général un int…
print(12 + 1)  # => 13
print(38 - 1)  # => 37
print(10 * 2)  # => 20

# …mais la division d'ints retournera un float
print(35 / 5)  # => 7.0
# (Si on souhaite une division entière, on utilisera un opérateur spécifique,
# cf. plus bas)

# Les calculs avec des floats recèlent quelques surprises…
print(0.1 + 0.2)  # => 0.30000000000000004

"""
Explication : les floats ne peuvent en fait stocker que des valeurs approchées
de nombres décimaux, en raison de la représentation binaire utilisée (IEEE 754).
Cela peut entraîner d'étranges problèmes d'arrondis (c'est un problème bien
connu de la norme IEEE 754, qui n'est pas propre à Python).
"""

# Quand on utilise un float dans un calcul, le résultat sera aussi un float
print(3 + 2.0)    # => 5.0
print(3 * 2.0)    # => 6.0

# Pour obtenir le reste d'une division euclidienne, on utilise l'opérateur
# modulo `%`
print(7 % 3)      # => 1 (en effet 7 = 3 * 2 + 1)

# Cet opérateur est très intéressant notamment pour les tests de parité (savoir
# si un nombre est pair ou impair) : si le reste est 0, le nombre est pair
print(7 % 2 == 0) # => False (7 est impair, donc le rste)

# L'exponentiation s'écrit x ** y ("x élevé à la puissance y")
print(2 ** 5)     # => 32

# Note : on peut aussi utiliser la fonction intégrée `pow()` (pour "power")
print(pow(2, 5))  # => 32 aussi

# Attention : l'opérateur `^` n'a rien à voir avec l'exponentiation !
print(2 ^ 5)      # => 7 (c'est l'opérateur XOR, cf. chap. 21)

# On obtient la valeur absolue d'un nombre avec `abs()`
print(abs(-5))    # => 5
print(abs(3))     # => 3


# La division entière
######################

# Pour une division entière (-> qui retourne un int), on utilisera un opérateur
# spécifique `//` (appelé "floor division" en anglais).
print(35 // 5)        # => 7
print(type(35 // 5))  # => <class 'int'>

# Les résultats de divisions entières sont tronqués à l'entier inférieur…
print(5 // 3)  # => 1

# …y compris pour les nombres négatifs !
print(-5 // 3)  # => -2

# Diviser par un float retournera toujours un float… tout en tronquant
# quand même le quotient à l'entier (c'est rarement ce que l'on cherche !)
print(5.0 // 3.0)  # => 1.0
print(-5.0 // 3.0)  # => -2.0
