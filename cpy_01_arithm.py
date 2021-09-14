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
#  Part. I      #  arithmétique - précédence - bases                           #
#               #                                                              #
################################################################################

########################################################
#                                                      #
# 4. Nombres, opérateurs et arithmétique               #
# 5. Ordre des opérations, whitespace                  #
# 6. Conversions : binaire, décimal et hexadécimal     #
#                                                      #
########################################################

########################################################
# 4. Nombres, opérateurs et arithmétique               #
########################################################
#
#  - Les ints
#  - Les floats
#  - La fonction intégrée type()
#  - Arithmétique avec ints et floats
#  - HP : la division entière
#
########################################################

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

# HP : on peut utiliser le underscore (_) pour séparer les milliers, millions,
# et les puissances de 1000 en général
print(12_345)      # => 12345
print(12_345_678)  # => 12345678

# Les floats
#############

# Les nombres décimaux ("floats") sont représentés avec un point : 'x.y'
print(3.0)    # => 3.0
print(-4.35)  # => -4.35

# HP : Python accepte également une notation scientifique avec "..e..", qui
# retournera un float
print(1e13)      # 10000000000000.0
print(-2.3e-04)  # -0.00023


"""
HP : complément sur les floats

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
IEEE 754, qui est très intéressante mais est tout à fait hors-programme de NSI.
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
Explication : ceci est tout à fait HP, mais les floats ne peuvent
en fait stocker que des valeurs approchées de nombres décimaux. Cela peut
entraîner d'étranges problèmes d'arrondis (c'est un problème bien connu de la
norme IEEE-754…).
"""

# Quand on utilise un float dans un calcul, le résultat sera aussi un float
print(3 + 2.0)  # => 5.0
print(3 * 2.0)  # => 6.0

# Pour obtenir le reste d'une division euclidienne, on utilise l'opérateur
# modulo "%"
print(7 % 3)    # => 1 (en effet 7 = 3 * 2 + 1)

# L'exponentiation s'écrit x ** y ("x élevé à la puissance y")
print(2 ** 5)   # => 32

# HP : on peut aussi utiliser la fonction intégrée pow() (pour "power")
pow(2, 5)       # => 32 aussi

# Attention : l'opérateur ^ n'a rien à voir avec l'exponentation !
print(2 ^ 5)    # => 7 (cf. le chapitre sur les opérateurs de bits)

# On obtient la valeur absolue d'un nombre avec abs()
print(abs(-5))  # => 5
print(abs(3))   # => 3

# HP : la division entière
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


########################################################
# 5. Ordre des opérations (précédence), whitespace     #
########################################################
#
#  - Précédence
#  - Whitespace
#  - Espaces ou tabulations ?
#
########################################################

# Précédence
#############

"""
Une expression est une combinaison de calculs qui peut être évaluée pour
retourner une valeur.
"""
print(2 + 3)  # => l'expression "2 + 3" est évaluée et retourne 5

"""
Dans une expression, l'ordre dans lequel les opérations sont évaluées par
Python (on appelle cela la "précédence") suit celui des opérateurs mathématiques
"""
print(2 + 3 * 6)    # => 2 + 18 => 20
print((2 + 3) * 6)  # => 5 * 6  => 30

"""
IMPT : voici l'ordre décroissant d'évaluation des opérations :
    1. exponentiation (puissance)
    2. les opérateurs *, /, //, and %, de gauche à droite
    3. les opérateurs + et -, de gauche à droite
    4. les opérateurs de comparaison, inégalité et inégalité
    5. opérateur d'assignation (a = 3)
    6. in, not in
    7. and, or, not
"""

# On peut, bien sûr, utiliser des parenthèses pour changer cette précédence
print((5 - 1) * ((7 + 1) / (3 - 1)))  # => 16.0

# Whitespace
#############

"""
Le whitespace ("espace vide") désigne tous les caractères qui servent à
espacer les mots ou les lignes les uns des autres : espaces, tabulations,
sauts de ligne, etc.

À la différence de beaucoup de langages, le whitespace en Python peut changer
le sens du programme : on dit qu'il est "sémantique" (il porte une
signification).
"""
# Exemple :
a = 2
if a + 1 == 3:
    print("a = 2")
print("pouet")
"""
Dans le programme ci-dessus, ce sont les espaces en début de ligne qui
indiquent que le premier print() est "dans" le "if". On verra que le
whitespace en DÉBUT de ligne est particulièrement important en Python.
"""

# Les espaces et tabulations ("whitespace") en milieu de ligne n'importent pas
4 - 3  # C'est la présentation recommandée mais…
4- 3   # … fonctionne aussi
4 -3   # … fonctionne aussi
4            -   3  # … aussi !

# Débat : espaces ou tabulations ?
###################################

"""
Il y a parfois confusion entre tabulations et espaces multiples en début de
ligne. Il est fortement conseillé de ne jamais mélanger les deux et de s'en
tenir à 4 espaces pour les tabulations.

La plupart des bons éditeurs de texte proposent d'afficher le whitespace pour
repérer d'un coup d'oeil celui qui est utilisé (sur Sublime Text, c'est la
ligne :
"draw_white_space": "all"
dans votre fichier de configuration).

La plupart des bons éditeurs de texte proposent aussi des plugins pour
bien formater automatiquement votre code. Vous les découvrirez par vous-même !
"""


########################################################
# 6. Conversions : binaire, décimal et hexadécimal     #
########################################################
#
#  - Conversions vers le décimal
#  - Conversions depuis le décimal
#
########################################################

# Conversions vers le décimal
##############################

# Python s'exprime nativement en décimal (base 10), comme vous et moi
# (et comme presque tous les langages de programmation existants)
print(10)  # => 10. Ce 10 est décimal, comme vos 10 doigts

# On peut écrire un nombre en binaire avec le préfixe "0b"…
print(0b1011)  # => 11
# …et Python fera automatiquement la conversion en base 10
print(0b01001101)  # => 77

# De même, on peut écrire de l'hexadécimal avec le préfixe "0x"
print(0xA0)  # => 160 (base 10)
print(0xDF40E)  # => 914446
print(0xDF40E)  # => 914446 (les majuscules n'ont pas d'importance)

# Conversions depuis le décimal
################################

# En sens inverse, on peut convertir du décimal en binaire avec la
# fonction intégrée bin()
print(bin(14))  # => '0b1110'.

# Notez les guillemets : Python retourne une string ! On le confirme en
# utilisant type()
print(type(bin(3)))  # => <class 'str'>

# On peut convertir directement de l'hexa vers du binaire
print(bin(0xA4F2))  # => '0b1010010011110010'

# Pour convertir en hexadécimal, on utilise hex()
print(hex(35))  # = '0x23'
# hex() retourne aussi une string :
print(type(hex(3)))  # => <class 'str'>

# Ces fonctions évitent de faire à la main des conversions entre bases.

# HP : attention, on ne peut pas combiner ces deux fonctions, car hex() et bin()
# n'acceptent que des int en paramètre
try:
    print(hex(bin(5)))  # => TypeError: 'str' object cannot be interpreted as an
    integer
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# HP : pour convertir en base 10 une string représentant un nombre depuis une
# base arbitraire, on utilise int(string, base)
print(int("22", 3))  # 8 en base 10
print(int("221021", 5))  # 7636 en base 10
print(int("776", 8))  # 510 en base 10
print(int("7234", 10))  # 7234, on retrouve le nombre de départ
