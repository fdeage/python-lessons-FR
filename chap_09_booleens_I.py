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
#  Chap. 9      #  Booléens I : valeurs, opérateurs, expressions                 #
#               #                                                              #
################################################################################
#
#  - Valeurs booléennes
#  - Expressions booléennes : égalité, inégalité, comparaison
#  - Opérateurs booléens : not, and, or
#  - Combinaisons booléennes
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

# Les booléens sont "sensibles à la casse" (càd aux majuscules et minuscules)
# Ainsi le booléen True et la variable true sont deux choses différentes…
try:
    true  # => NameError: name 'true' is not defined
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# IMPT: les booléens ne sont pas des strings !
print(True == "True")  # => False


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

# Ce signe "==" revient donc à poser la question : "est-ce que 1 est égal à 1 ?"

# IMPT : attention à la confusion entre "==" et "=" ! Le égal simple ("=") est
# utilisé seulement pour affecter une valeur à une variable
a = 5   # => On met 5 dans la variable a
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


#   4. Il y a d'autres opérateurs booléens, comme "… in …", "… is …",
#      que l'on verra plus loin
"ab" in "abcd"     # => True
"ab" in "def"      # => False
a = None
a is None          # => True


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
i > 5 or i % 2 == 1   # => True, car la deuxième condition est vraie
i > 51 or i % 2 == 1  # => False, car les deux conditions sont fausses

"""
On notera que "and" et "or" aussi sont sensibles à la casse :
Not False             # => SyntaxError: invalid syntax (Not)
True And False        # => SyntaxError: invalid syntax (And)
"""

"""
Note : on appelle parfois "or" et "and" des "opérateurs coupe-circuit"
("short-circuit operators") : en effet, dans certains cas, la deuxième condition
ne sera pas exécutée.
"""

# Exemple :
def ma_fonction():
    print("Pouet")

#   - avec "or" :
1 == 2 or ma_fonction()   # => "Pouet"
1 == 1 or ma_fonction()   # => ma_fonction() ne sera jamais appelée…
"""
Explication :
la 1ère condition ("1 == 1") est suffisante pour que toute l'expression soit
évaluée à True, donc ma_fonction() n'est pas appelée.
"""

#   - avec "and" :
1 == 1 and ma_fonction()  # => "Pouet"
1 == 2 and ma_fonction()  # => ma_fonction() ne sera jamais appelée non plus
"""
Explication :
la 1ère condition ("1 == 1") est suffisante pour que toute l'expression soit
évaluée à False.
"""


# Combinaisons booléennes
##########################

"""
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
