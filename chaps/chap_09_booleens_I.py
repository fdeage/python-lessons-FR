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
#  Chap. 9      #  Booléens I : valeurs, opérateurs, expressions               #
#               #                                                              #
################################################################################
#
#  - Valeurs booléennes
#  - Expressions booléennes : égalité, inégalité, comparaison
#  - Comparer des strings
#  - Pièges des comparaisons
#  - Opérateurs booléens : not, and, or
#  - Combinaisons booléennes
#  - Stocker un booléen dans une variable
#
###############################################################

# Valeurs booléennes
#####################

"""
Un booléen est un type de variable qui ne peut prendre que deux
valeurs : "vrai" ou "faux".

Leur nom vient du mathématicien et philosophe britannique George Boole
(1815-1864), qui s'est intéressé à l'algèbre booléenne, utilisant uniquement
ces deux valeurs.

Les booléens sont TRÈS utilisés en informatique (on peut même dire que
toute l'informatique est juste une utilisation massive et judicieuse des
booléens…).
"""

# Voici les deux valeurs booléennes fondamentales :
True
False

# Leur type est "bool" (cf. chap. 6)
print(type(True))   # => <class 'bool'>
print(type(False))  # => <class 'bool'>

# Notez qu'ils s'écrivent sans guillemets : ce sont des valeurs, pas du texte.

# Les booléens sont "sensibles à la casse" (càd aux majuscules et minuscules)
# Ainsi le booléen True et la variable true sont deux choses différentes…
try:
    true  # => NameError: name 'true' is not defined
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# IMPT : les booléens ne sont pas des strings !
print(True == "True")  # => False
print(type("True"))    # => <class 'str'> ("True" entre guillemets est du texte)


# Expressions booléennes : égalité, inégalité, comparaison
###########################################################

"""
Une expression booléenne est un type d'expression qui s'évalue en une valeur
booléenne. Les plus connues sont les tests d'égalité et les comparaisons.
"""

#   1. Tester une égalité ("Est-ce que truc est égal à bidule ?") retourne
#      toujours un booléen. On teste avec l'opérateur "=="
1 == 1  # => True
2 == 1  # => False
print(1 == 1)  # => True

# On peut tester l'égalité de toutes sortes de valeurs :
"abc" == "abc"  # => True
"abc" == "ABC"  # => False (les majuscules comptent)
1 == 1.0        # => True (même valeur, même si les types diffèrent, cf. chap. 6)
2 + 2 == 4      # => True (le calcul est fait AVANT la comparaison, cf. chap. 5)

# Ce signe "==" revient donc à poser la question : "est-ce que 1 est égal à 1 ?"

# IMPT : attention à la confusion entre "==" et "=" ! Le égal simple ("=") est
# utilisé seulement pour affecter une valeur à une variable
a = 5   # => On met 5 dans la variable a (cf. chap. 10)
a == 5  # => On teste si a vaut 5, ce qui ici est vrai (évalue à True)


#   2. On teste une différence ("… est différent de … ?") avec
#      l'opérateur "!="
1 != 1  # => False
2 != 1  # => True


#   3. Enfin, les opérateurs de comparaison retournent aussi un booléen
1 < 10  # => True
1 > 10  # => False

# Opérateurs "supérieur ou égal" et "inférieur ou égal" :
2 <= 2  # => True
2 >= 2  # => True

# Note : on peut "enchaîner" les comparaisons en Python
1 < 2 < 3  # => True, car toutes les comparaisons sont vraies
1 < 3 < 2  # => False, car au moins une comparaison est fausse

# C'est très pratique pour tester si un nombre est dans un intervalle :
note = 14
0 <= note <= 20  # => True ("note est-elle comprise entre 0 et 20 ?")


#   4. Il y a d'autres opérateurs booléens, comme "… in …", "… is …",
#      que l'on verra plus loin ("in" au chap. 8 pour les strings et au
#      chap. 16 pour les listes, None au chap. 15, "is" au chap. 19)
"ab" in "abcd"     # => True
"ab" in "def"      # => False
a = None
a is None          # => True


# Comparer des strings
#######################

"""
Les opérateurs de comparaison fonctionnent aussi avec des strings. Python
compare alors les chaînes dans l'ordre "alphabétique" (on dit "lexicographique",
comme dans un dictionnaire) : il compare le 1er caractère de chaque chaîne,
puis le 2e s'ils sont égaux, etc.
"""
"abc" < "abd"      # => True ("c" vient avant "d")
"pomme" < "poire"  # => False ("m" vient APRÈS "i")
"a" < "ab"         # => True (une chaîne plus courte vient avant)

"""
Attention : cet ordre n'est pas tout à fait l'ordre alphabétique habituel ! Les
caractères sont en fait comparés selon leur numéro Unicode (cf. chap. 8 et
la fonction ord()). Or toutes les majuscules ont un numéro plus petit que les
minuscules :
"""
"Z" < "a"  # => True (ord("Z") vaut 90, ord("a") vaut 97)

# De même, des chiffres dans une chaîne sont comparés caractère par caractère,
# et non comme des nombres :
"10" < "9"  # => True ("1" vient avant "9")
10 < 9      # => False (ici on compare bien des nombres)


# Pièges des comparaisons
##########################

"""
    1. On ne peut pas comparer avec "<" ou ">" des valeurs de types
       incompatibles (un nombre et une chaîne, par exemple) : cela n'a pas de
       sens, donc Python soulève une erreur.
"""
try:
    1 < "a"  # => TypeError: '<' not supported between instances of 'int'
    #                         and 'str'
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# En revanche, "==" fonctionne toujours : deux valeurs de types incompatibles
# sont simplement différentes
1 == "1"  # => False

"""
    2. IMPT : les floats ne sont pas exacts (cf. chap. 4, où l'on a vu que
       0.1 + 0.2 donne 0.30000000000000004). Il ne faut donc JAMAIS tester
       l'égalité de deux floats calculés avec "==" !
"""
0.1 + 0.2 == 0.3  # => False (!!)

# On teste plutôt si la différence entre les deux est très petite (abs() donne
# la valeur absolue, cf. chap. 4) :
abs((0.1 + 0.2) - 0.3) < 0.000001  # => True


# Opérateurs booléens : not, and, or
#####################################

"""
Il existe 3 opérateurs booléens pour travailler avec des variables booléennes :
    1. "not", pour obtenir la négation d'un booléen
    2. "and", pour obtenir une expression vraie si les DEUX termes sont vrais
    3. "or", pour obtenir une expression vraie si AU MOINS UN terme est vrai
"""

#   1. On obtient la négation, "l'opposé" d'un booléen avec l'opérateur "not"
not True   # => False
not False  # => True
not 1 == 2 # => True


#   2. "and" combine deux valeurs booléennes et retourne True si les deux sont
#      vraies, et False si au moins une valeur est fausse
True and False  # => False
i = 34
i > 5 and i % 2 == 1  # => False, car la deuxième condition est fausse
i > 5 and i % 2 == 0  # => True, car les deux conditions sont vraies


#   3. "or" combine deux valeurs booléennes et retourne True si au moins l'une
#      des deux est vraie, et False seulement si les deux sont fausses
True or False   # => True
i = 34
i > 5 or i % 2 == 1   # => True, car la première condition est vraie
i > 51 or i % 2 == 1  # => False, car les deux conditions sont fausses

"""
Note : le "or" de Python est un "ou inclusif" : l'expression est vraie si l'un
OU l'autre est vrai, ou LES DEUX. C'est différent du "ou" du langage courant,
souvent exclusif ("fromage ou dessert" : pas les deux !).
"""
True or True  # => True

"""
On notera que "not", "and" et "or" aussi sont sensibles à la casse (ces lignes
sont dans une chaîne, car une SyntaxError empêcherait le fichier de se lancer) :
Not False             # => SyntaxError: invalid syntax (Not)
True And False        # => SyntaxError: invalid syntax (And)

Notez aussi qu'on ne peut pas utiliser les symboles "&&", "||" ou "!" que
l'on trouve dans d'autres langages (C, Java, JavaScript…) : en Python, on écrit
les mots "and", "or" et "not".
"""

"""
Note : on appelle parfois "or" et "and" des "opérateurs coupe-circuit"
("short-circuit operators") : en effet, dans certains cas, la deuxième condition
ne sera pas exécutée.
"""

# Exemple (les fonctions seront vues au chap. 14 : retenez juste que
# ma_fonction() imprime "Pouet" à chaque fois qu'elle est appelée) :
def ma_fonction():
    print("Pouet")

#   - avec "or" :
1 == 2 or ma_fonction()   # => imprime Pouet
1 == 1 or ma_fonction()   # => ma_fonction() ne sera jamais appelée…
"""
Explication :
la 1ère condition ("1 == 1") est suffisante pour que toute l'expression soit
évaluée à True, donc ma_fonction() n'est pas appelée.
"""

#   - avec "and" :
1 == 1 and ma_fonction()  # => imprime Pouet
1 == 2 and ma_fonction()  # => ma_fonction() ne sera jamais appelée non plus
"""
Explication :
la 1ère condition ("1 == 2") est fausse, ce qui est suffisant pour que toute
l'expression soit évaluée à False : inutile d'évaluer la suite.

Ce mécanisme est utile pour éviter des erreurs. Par exemple, on peut vérifier
qu'un nombre n'est pas nul AVANT de diviser par ce nombre :
"""
diviseur = 0
diviseur != 0 and 10 / diviseur > 1  # => False (et pas de ZeroDivisionError,
#                                        car la division n'est jamais calculée)


# Combinaisons booléennes
##########################

"""
On peut combiner autant d'opérateurs que l'on veut. Comme pour l'arithmétique
(cf. chap. 5), il y a un ordre de priorité :
    1. les comparaisons (==, !=, <, >, <=, >=, in…) d'abord,
    2. puis "not",
    3. puis "and",
    4. et enfin "or".

"and" est prioritaire sur "or", comme "*" est prioritaire sur "+" :
"""
True or False and False    # => True : se lit True or (False and False)
(True or False) and False  # => False : les parenthèses changent tout
not 1 == 2                 # => True : se lit not (1 == 2)

"""
IMPT : dès qu'une expression mélange "and" et "or", mettez des parenthèses !
Même si vous connaissez les priorités, la personne qui vous relira ne les
connaît peut-être pas.

On peut écrire des expressions très sophistiquées avec les opérateurs booléens.
Essayez de comprendre pourquoi les expressions ci-dessous retournent la valeur
en commentaire à droite…
"""
A = True
B = False

"True" == True        # => False
B and A               # => False
A and 1 == 1          # => True
B and 0 != 1          # => False
A or 1 == 2           # => True
(A and B) or ((not B) and A)  # => True
"""
Détail du dernier exemple :
    - (A and B)        => (True and False)  => False
    - (not B)          => (not False)       => True
    - ((not B) and A)  => (True and True)   => True
    - False or True    => True
"""

"""
On verra au chap. 21 un outil pour raisonner sur ces combinaisons : les tables
de vérité.
"""


# Stocker un booléen dans une variable
#######################################

"""
Une expression booléenne produit une valeur (True ou False), que l'on peut
ranger dans une variable comme n'importe quelle autre valeur (cf. chap. 10).
Cela permet de donner un nom parlant à une condition :
"""
age = 17
a_son_permis = False
est_majeur = age >= 18
peut_conduire = est_majeur and a_son_permis

print(est_majeur)     # => False
print(peut_conduire)  # => False

# Attention à ne pas confondre les deux signes "=" sur une même ligne :
# "=" range le résultat dans la variable, "==" compare.
est_pair = 34 % 2 == 0
print(est_pair)  # => True

"""
Ces variables booléennes sont très utilisées avec la structure "if" (cf.
chap. 12) :
    if peut_conduire:
        ...
"""
