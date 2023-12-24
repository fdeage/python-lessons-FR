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
#  Chap. 21     #  Booléens II                                                 #
#               #                                                              #
################################################################################
#
#  - Tables de vérité
#  - Calculs avec les booléens et conversions
#  - all() et any()
#  - Les opérateurs bit à bit
#
###############################################################

# Tables de vérité
###################

"""
On peut résumer le fonctionnement de "not", "and" et "or" avec des tables, qu'on
appelle des tables de vérité.

Chaque cellule de la table sera une combinaison booléenne :
    - de la valeur sur la même ligne à gauche (T ou F)
    - de la valeur sur la même colonne en haut (T ou F)

Table de vérité de l'opérateur "and" :
     |   T   |   F   |
 --- | ----- | ----- |
 T   | True  | False |
 F   | False | False |

Table de vérité de l'opérateur "or" :
     |   T  |   F   |
 --- | ---- | ----- |
 T   | True | True  |
 F   | True | False |

Table de vérité de l'opérateur "not" (ne prend qu'un paramètre) :
 --- | ----- |
 T   | False |
 F   | True  |
"""


# Calculs avec les booléens et conversions
###########################################

"""
Attention : si vous utilisez True ou False dans un calcul arithmétique (avec
"+", "-", "*"…), ils seront automatiquement convertis ("castés") en entiers.

True et False valent en fait 1 et 0.
"""
True + True    # => 2
False + False  # => 0
True + False   # => 1
True * 8       # => 8
False - 5      # => -5

# Les opérateurs de comparaison vont convertir True et False en ints (1 et 0)
0 == False     # => True
1 == True      # => True
2 == True      # => False
-5 != False    # => True

# Cela donnera parfois d'étranges calculs :
(2 + 2 == 4) + (2 + 2 == 3) + (1 == 1)  # => 2

"""
Explication : ici l'opérateur "+" va entraîner une conversion de
True et False en leur équivalent numérique (1 et 0).

Conclusion : n'utilisez pas de booléens avec des opérateurs arithmétiques :
utilisez… les opérateurs booléens vus plus haut !
"""


# all() et any()
######################

"""
Ces deux fonctions opèrent sur des listes de booléens (chap. 16).

Elles permettent de faire des "and" ou des "or" sur une liste d'éléments
contenant autant de valeurs que l'on veut :
    - all(liste) retournera True si tous les éléments de la liste passée en
      paramètre valent True, et False sinon
    - any(liste) retournera True si au moins un élément de la liste vaut True
"""
li = [True, False, 2 == 2]
print(all(li))  # => False, car il y a au moins un False
print(any(li))  # => True, car il y a au moins un True


# Les opérateurs bit à bit
###########################

"""
Il arrive qu'on ait besoin de manipuler directement les bits constituant les
nombres, par exemple dans la programmation bas niveau, la cryptographie, la conception de protocoles réseau…

On utilise alors les opérateurs bit à bit (ou bitwise), pour effectuer des opérations comme le décalage de bits, l'ET, l'OU, le OU exclusif, etc.
"""

# Ex :
a = 0b0101  # (5 en décimal)
b = 0b0011  # (3 en décimal)

"""
    1. Le ET bitwise (&) retourne un nombre dont chaque bit est le résultat de
    l'opération ET entre les bits correspondants de deux nombres (= "les deux
    bits sont activés en même temps")
"""
print(a & b)  # => 1 (0001 en binaire)


"""
    2. Le OU Bitwise (|) fait la même chose avec l'opération OU (= "l'un ou
    l'autre est activé")
"""
print(a | b)  # => 7 (0111 en binaire)


"""
    3. Le OU exclusif Bitwise (^) fait la même chose avec l'opération OU
    exclusif (= "l'un ou l'autre est activé mais pas les deux")
"""
print(a ^ b)  # => 6 (0110 en binaire)


"""
    4. Le décalage à gauche (<<) ou à droite (>>) déplace les bits d'un nombre
    vers la gauche ou la droite, remplissant les positions libres avec des zéros.
"""
print(a << 1)  # => 10 (binaire: 1010)
print(a >> 1)  # => 2 (binaire: 0010)


"""
Quelques usages :

    1. On peut utiliser l'opérateur & pour masquer ou extraire des portions
       spécifiques de bits dans un nombre.

Ainsi pour extraire les 4 bits de droite d'un nombre, on fera :
"""
nomb = 0b11101
mask = 0b01111
print(nomb & mask)  # => 13 (binaire: 01101), seuls les 4 bits à droite sont gardés


"""
    2. On peut aussi vérifier facilement la parité d'un nombre avec & :
"""
def is_even(n):
    return n & 1 == 0

print(is_even(10))  # => True
print(is_even(7))   # => False

"""
    3. Enfin, l'opérateur XOR peut être utilisé pour échanger les valeurs de
       deux variables sans utiliser de variable temporaire.
"""
a = 10
b = 7

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)  # => 7, 10

# En pratique, Python propose une syntaxe avec des tuples qui est encore
# plus simple (cf. chap. 17) :
a, b = b, a
print(a, b)  # => 10, 7

