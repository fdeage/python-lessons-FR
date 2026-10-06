################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Félix Déage - 2026                    #
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
#  - La division entière et le modulo
#  - La division par zéro
#  - Arrondis
#  - Autres fonctions utiles : min() et max()
#  - En bref
#
###########################################

# Les ints
###########

"""
En Python, les nombres sont, par défaut, des entiers représentés en base 10.
Python les appelle des "ints" (pour "integers", "entiers" en anglais).
"""
print(3)   # => 3

# Ces ints peuvent être négatifs
print(-7)  # => -7

# Ils peuvent être TRÈS grands
print(999999999999999999999999)  # => 999999999999999999999999
print(2 ** 100)  # => 1267650600228229401496703205376
# (Dans beaucoup de langages, comme C ou Java, les entiers sont limités à 64
# bits, soit au maximum 2^63 - 1 = 9223372036854775807. En Python, les ints
# sont "arbitrairement grands" : la seule limite est la mémoire de votre
# ordinateur.)

# On peut utiliser le underscore (`_`) pour séparer les milliers, millions,
# et les puissances de 1000 en général. Python l'ignore : il ne sert qu'à
# rendre le nombre plus lisible pour un humain (Python 3.6+).
print(12_345)      # => 12345
print(12_345_678)  # => 12345678

# Attention : on ne peut PAS utiliser d'espace ou de virgule pour séparer les
# milliers. Une virgule a un autre sens en Python, comme on le verra plus bas.

# Note : on peut aussi écrire des entiers en binaire, en octal ou en
# hexadécimal (cf. chap. 6).


# Les floats
#############

# Les nombres décimaux ("floats", pour "floating point numbers", nombres "à
# virgule flottante") sont représentés avec un POINT, et non une virgule
# comme en français : `x.y`
print(3.0)    # => 3.0
print(-4.35)  # => -4.35

# On peut omettre le 0 avant ou après le point (c'est moins lisible) :
print(.5)  # => 0.5
print(5.)  # => 5.0

# IMPT : 3 et 3.0 représentent le même nombre, mais pas le même TYPE de
# valeur : le premier est un int, le second un float. On verra au chap. 6
# comment connaître le type d'une valeur avec type().

# Python accepte également une notation scientifique avec `..e..`, qui
# retournera un float : `XeY` signifie "X multiplié par 10 puissance Y"
print(1e13)      # => 10000000000000.0
print(-2.3e-04)  # => -0.00023
print(3e0)       # => 3.0 (3 × 10^0 = 3 × 1)

# Les floats ne sont pas arbitrairement grands, contrairement aux ints : au-delà
# d'environ 1.8e308, Python utilise une valeur spéciale, "inf" (infini)
print(1e308 * 10)  # => inf


# Arithmétique avec ints et floats
###################################

# L'arithmétique de base avec des entiers est sans surprise : les calculs avec
# des ints retournent en général un int…
print(12 + 1)  # => 13
print(38 - 1)  # => 37
print(10 * 2)  # => 20

# …mais la division d'ints retournera un float, même si le résultat "tombe
# juste"
print(35 / 5)  # => 7.0
print(10 / 3)  # => 3.3333333333333335
# (Si on souhaite une division entière, on utilisera un opérateur spécifique,
# cf. plus bas)

# Les calculs avec des floats recèlent quelques surprises…
print(0.1 + 0.2)  # => 0.30000000000000004

"""
Explication : les floats ne peuvent en fait stocker que des valeurs approchées
de nombres décimaux, en raison de la représentation binaire utilisée (IEEE 754).
Cela peut entraîner d'étranges problèmes d'arrondis (c'est un problème bien
connu de la norme IEEE 754, qui n'est pas propre à Python).

De la même façon qu'on ne peut pas écrire 1/3 exactement en décimal
(0.33333…), on ne peut pas écrire 0.1 exactement en binaire : l'ordinateur
stocke donc la valeur la plus proche possible.

Conséquence pratique (IMPT) : ne jamais tester l'égalité exacte de deux floats
issus de calculs ! (L'opérateur d'égalité `==` sera vu au chap. 9.)
"""
print(0.1 + 0.2 == 0.3)  # => False (!)
# On compare plutôt des valeurs arrondies (cf. plus bas, round()) :
print(round(0.1 + 0.2, 2) == 0.3)  # => True

# Quand on utilise un float dans un calcul, le résultat sera aussi un float
print(3 + 2.0)    # => 5.0
print(3 * 2.0)    # => 6.0

# L'exponentiation s'écrit x ** y ("x élevé à la puissance y")
print(2 ** 5)     # => 32
print(2 ** -1)    # => 0.5 (une puissance négative donne un float : 1/2)
print(9 ** 0.5)   # => 3.0 (puissance 1/2 : c'est la racine carrée !)

# Note : on peut aussi utiliser la fonction intégrée `pow()` (pour "power")
print(pow(2, 5))  # => 32 aussi

# Attention : l'opérateur `^` n'a rien à voir avec l'exponentiation !
print(2 ^ 5)      # => 7 (c'est l'opérateur XOR, cf. chap. 21)

# On obtient la valeur absolue d'un nombre avec `abs()`
print(abs(-5))    # => 5
print(abs(3))     # => 3
print(abs(-2.5))  # => 2.5

# Le signe `-` devant un nombre (ou une expression) en change le signe : on
# l'appelle "moins unaire"
print(-(3 - 5))   # => 2

# Lorsqu'une expression contient plusieurs opérateurs, Python suit un ordre de
# priorité proche de celui des mathématiques (cf. chap. 5)
print(2 + 3 * 4)  # => 14


# La division entière et le modulo
###################################

# Pour une division entière (-> qui retourne un int), on utilisera un opérateur
# spécifique `//` (appelé "floor division" en anglais).
print(35 // 5)        # => 7
print(type(35 // 5))  # => <class 'int'> (type() sera vu au chap. 6)

# Les résultats de divisions entières sont tronqués à l'entier inférieur…
print(5 // 3)  # => 1

# …y compris pour les nombres négatifs ! -5 / 3 vaut -1.666…, et l'entier
# inférieur ("floor", le "plancher") est -2, pas -1
print(-5 // 3)  # => -2

# Diviser par un float retournera toujours un float… tout en tronquant
# quand même le quotient à l'entier (c'est rarement ce que l'on cherche !)
print(5.0 // 3.0)  # => 1.0
print(-5.0 // 3.0)  # => -2.0

# Pour obtenir le reste d'une division euclidienne, on utilise l'opérateur
# modulo `%`
print(7 % 3)      # => 1 (en effet 7 = 3 * 2 + 1)
print(17 % 5)     # => 2 (en effet 17 = 5 * 3 + 2)

# Cet opérateur est très intéressant notamment pour les tests de parité (savoir
# si un nombre est pair ou impair) : si le reste de la division par 2 est 0, le
# nombre est pair
print(7 % 2)       # => 1 (7 est impair)
print(8 % 2)       # => 0 (8 est pair)
print(7 % 2 == 0)  # => False (7 est impair, donc le reste n'est pas 0)

# Plus généralement, `a % b == 0` signifie "a est un multiple de b"
print(15 % 5)  # => 0 (15 est un multiple de 5)

# Le modulo fonctionne aussi avec les floats
print(7.5 % 2)  # => 1.5 (7.5 = 2 * 3 + 1.5)

# Avec des nombres négatifs, le résultat de % a toujours le signe du diviseur
# (le nombre de droite). C'est cohérent avec // : on a toujours
# a == (a // b) * b + (a % b)
print(-7 % 3)   # => 2 (car -7 = 3 * (-3) + 2)
print(7 % -3)   # => -2 (car 7 = -3 * (-3) + (-2))

# La fonction intégrée divmod() calcule le quotient ET le reste en une fois.
# Elle retourne deux valeurs entre parenthèses (un "tuple", cf. chap. 17) :
print(divmod(17, 5))   # => (3, 2)
print(divmod(-17, 5))  # => (-4, 3)

# Exemple d'utilisation : convertir 135 minutes en heures et minutes
print(135 // 60, "h", 135 % 60, "min")  # => 2 h 15 min


# La division par zéro
#######################

# Comme en mathématiques, diviser par zéro est impossible : Python soulève une
# erreur "ZeroDivisionError". Cela vaut pour /, // et %, avec des ints comme
# avec des floats. (Les try … except permettent de continuer l'exécution, cf.
# chap. 1 et chap. 26.)
try:
    print(1 / 0)
except ZeroDivisionError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    print(7 % 0.0)
except ZeroDivisionError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# De même, un calcul dont le résultat est trop grand pour un float provoque
# une erreur "OverflowError" ("débordement")
try:
    print(10.0 ** 400)
except OverflowError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# (Le texte de cette erreur peut varier selon le système d'exploitation.)

# Avec des ints, en revanche, aucun problème : ils sont arbitrairement grands !
print(10 ** 40)  # => 10000000000000000000000000000000000000000


# Arrondis
###########

# La fonction intégrée round() arrondit un nombre à l'entier le plus proche…
print(round(3.7))   # => 4
print(round(-3.7))  # => -4
print(round(3.2))   # => 3

# …ou à un nombre donné de chiffres après la virgule, passé en 2e paramètre
print(round(3.14159, 2))  # => 3.14
print(round(1234.5678, -2))  # => 1200.0 (arrondi à la centaine)

"""
Attention, deux pièges avec round() :

1. Quand le nombre est exactement à mi-chemin (x.5), Python arrondit vers
   l'entier PAIR le plus proche (on parle d'"arrondi bancaire"). Cela évite de
   fausser les moyennes en arrondissant toujours vers le haut.
"""
print(round(2.5))  # => 2 (et non 3 !)
print(round(3.5))  # => 4

"""
2. À cause de la représentation approchée des floats, un nombre qui semble à
   mi-chemin ne l'est pas toujours : 2.675 est en réalité stocké comme
   2.67499999…
"""
print(round(2.675, 2))  # => 2.67 (et non 2.68)

# Note : round() permet d'AFFICHER un nombre arrondi, mais ne résout pas les
# problèmes de précision. Pour faire de la comptabilité exacte, on utilise le
# module `decimal` (les modules seront vus au chap. 22).

# On verra au chap. 6 qu'on peut aussi "tronquer" un float (supprimer sa partie
# décimale, sans arrondir) en le convertissant en int avec int()


# Autres fonctions utiles : min() et max()
###########################################

# Les fonctions intégrées min() et max() retournent respectivement le plus petit
# et le plus grand des nombres qu'on leur passe, séparés par des virgules
print(min(3, 8, 1))     # => 1
print(max(3, 8, 1))     # => 8
print(max(2, 7.5, -3))  # => 7.5 (on peut mélanger ints et floats)

# Pour aller plus loin (racine carrée, sinus, logarithme, pi…), il faudra
# utiliser le module `math` (cf. chap. 22).


# En bref
##########

"""
Opérateurs arithmétiques :
    +    addition                         7 + 2   => 9
    -    soustraction (ou moins unaire)   7 - 2   => 5
    *    multiplication                   7 * 2   => 14
    /    division (retourne un float)     7 / 2   => 3.5
    //   division entière ("floor")       7 // 2  => 3
    %    reste de la division (modulo)    7 % 2   => 1
    **   puissance                        7 ** 2  => 49

Fonctions intégrées : abs(), pow(), divmod(), round(), min(), max().

À retenir (IMPT) :
    - un calcul qui contient un float retourne un float ;
    - / retourne toujours un float, // et % retournent un int entre ints ;
    - les floats sont des valeurs approchées : 0.1 + 0.2 != 0.3 ;
    - diviser par zéro provoque une erreur.
"""
