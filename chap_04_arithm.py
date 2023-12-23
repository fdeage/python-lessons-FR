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
#  - Précédence des opérateurs
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
Bonus : un complément sur les floats

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
IEEE 754, qui est très intéressante pour comprendre certaines erreurs sur les
floats.
"""


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

Les principaux types sont :
-  types simples : bool, int, float
-  types construits : str, tuple, list, dict

(Nous les verrons plus en détail au chap. 10)
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

# …mais la division d'ints retournera un float
print(35 / 5)  # => 7.0
# (Si on souhaite une division entière, on utilisera un opérateur spécifique,
# cf. plus bas)

# Les calculs avec des floats recèlent quelques surprises…
print(0.1 + 0.2)  # => 0.30000000000000004

"""
Explication : les floats ne peuvent en fait stocker que des valeurs approchées
de nombres décimaux, en raison de la représentation binaire utilisée. Cela peut
entraîner d'étranges problèmes d'arrondis (c'est un problème bien connu de la
norme IEEE-754 qui n'est pas propre à Python).
"""

# Quand on utilise un float dans un calcul, le résultat sera aussi un float
print(3 + 2.0)    # => 5.0
print(3 * 2.0)    # => 6.0

# Pour obtenir le reste d'une division euclidienne, on utilise l'opérateur
# modulo "%"
print(7 % 3)      # => 1 (en effet 7 = 3 * 2 + 1)

# L'exponentiation s'écrit x ** y ("x élevé à la puissance y")
print(2 ** 5)     # => 32

# Note : on peut aussi utiliser la fonction intégrée pow() (pour "power")
print(pow(2, 5))  # => 32 aussi

# Attention : l'opérateur ^ n'a rien à voir avec l'exponentiation !
print(2 ^ 5)      # => 7 (c'est l'opérateur XOR, cf. chap. 9)

# On obtient la valeur absolue d'un nombre avec abs()
print(abs(-5))    # => 5
print(abs(3))     # => 3


# La division entière
###########################

# Pour une division entière (= qui retourne un int), on utilisera un opérateur
# spécifique "//" (appelé "floor division" en anglais).
print(35 // 5)  # => 7

# Les résultats de divisions entières sont tronqués à l'entier inférieur...
print(5 // 3)  # => 1

# ...y compris pour les nombres négatifs !
print(-5 // 3)  # => -2

# Diviser par un float retournera toujours un float… tout en tronquant quand même le
# quotient à l'entier (c'est rarement ce que l'on cherche !)
print(5.0 // 3.0)  # => 1.0
print(-5.0 // 3.0)  # => -2.0


# Précédence des opérateurs
############################

"""
Une expression est une combinaison de calculs qui peut être évaluée pour
retourner une valeur.
"""
print(2 + 3)  # => l'expression "2 + 3" est évaluée et retourne 5

"""
Dans une expression, l'ordre dans lequel les opérations sont évaluées par
Python (on appelle cela la "précédence") suit grosso modo celui des opérateurs
mathématiques :
"""
print(2 + 3 * 6)    # => 2 + 18 => 20
print((2 + 3) * 6)  # => 5 * 6  => 30

"""
Voici l'ordre décroissant d'évaluation des opérations :
    1. exponentiation (puissance)
    2. les opérateurs *, /, //, and %, de gauche à droite
    3. les opérateurs + et -, de gauche à droite
    4. les opérateurs de comparaison, inégalité et inégalité (==, !=, <, >)
    5. l'opérateur d'assignation (a = 3)
    6. in, not in
    7. and, or, not (cf. chap. 9)

On peut, bien sûr, utiliser des parenthèses pour changer cette précédence :
"""
print((5 - 1) * ((7 + 1) / (3 - 1)))  # => 16.0

"""
L'ordre n'est pas à connaître, il faut juste savoir qu'il y en a un. En cas
de doute, utilisez des parenthèses !

Par défaut, les opérations au sein du même niveau de précédence sont
évaluées de gauche à droite.
"""
