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
#  Chap. 21     #  Itérables & compréhensions                                  #
#               #                                                              #
################################################################################
#
#  - Les itérables
#  - Compréhensions sur des listes
#  - Conditions sur les compréhensions
#  - Compréhensions sur des matrices
#  - Compréhensions chaînées
#  - Compréhensions avancées
#
###########################################

"""
Ce fichier appelle le fichier "exemple.txt".
"""

# Les itérables
################

"""
Un "itérable" est un objet Python sur lequel on peut itérer,
c'est-à-dire qu'on peut le parcourir séquentiellement avec "for".
Ce parcours garantit de PASSER UNE ET UNE SEULE FOIS dans chaque élément.

Quels sont les itérables en Python ?
"""

#   1. La liste est bien sûr un itérable
l = [1, 2, 3]
for i in l:
    print(i)
"""
1
2
3
"""

#   2. Le tuple, qui est au fond simplement une liste immuable, est un itérable
t = (4, 5, 6)
for i in t:
    print(i)
"""
4
5
6
"""

#   3. Un dictionnaire est un itérable. Note : on itère sur les clés du
#      dictionnaire, pas ses valeurs !
d = {0: "zéro", 1: "un"}
for i in d:
    print(i)
"""
0
1
"""

#   4. Surprise : une string est aussi un itérable !
s = "Pouet"
for c in s:
    print(2 * c)
"""
PP
oo
uu
ee
tt
"""

"""
    5. Enfin, un descripteur de fichier ("file descriptor") retourné par open()
       est aussi un itérable.
       Voici le contenu d'un fichier "exemple.txt" :
aaaa
bbbbbb
cccc
dddddd
eeeeeeeeeeeeeee
fffff
gg gg gg
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
iiiii
"""

# On va utiliser cette syntaxe
for line in open("exemple.txt", "r"):
    # On rappelle que l'option end='' évite d'insérer un saut de ligne à chaque
    # fin de ligne
    print(line, end="")
"""
Cette boucle imprimera, ligne par ligne, le fichier plus haut :

aaaa
bbbbbb
cccc
dddddd
eeeeeeeeeeeeeee
fffff
gg gg gg
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
iiiii
"""

"""
On peut utiliser la syntaxe  "… in …" avec tous les itérables, sauf
les fichiers. "in" retourne True si l'élément est dans l'itérable, et False
sinon.
"""
1 in [1, 2, 3]  # => True
"p" in "pouet"  # => True
"r" in "pouet"  # => False

"""
Cette syntaxe offre la même garantie que "for" : chaque élément sera parcouru
exactement UNE FOIS ET UNE SEULE.
"""


# Compréhensions de liste
##########################

"""
Python propose une méthode pour créer automatiquement une collection avec un
itérable : les compréhensions.

La syntaxe est la suivante (pour une liste) :
[ <expression> for <variable> in <itérable> ]

Les compréhensions se font le plus souvent sur des listes.
"""

# Exemple avec une liste basique dont on va doubler toutes les valeurs
l1 = list(range(6))  # => [0, 1, 2, 3, 4, 5]
l2 = [2 * x for x in l1]
print(l2)  # => [0, 2, 4, 6, 8, 10]

"""
Explication : on va appliquer la fonction de gauche "2 * x" à chaque élément
de la liste l, et obtenir une nouvelle liste contenant les résultats.
"""

# Quelques autres compréhensions possibles :
#   - Ajouter/soustraire une valeur constante aux termes d'une liste :
l3 = [i - 3 for i in range(5)]
print(l3)  # => [-3, -2, -1, 0, 1]

#   - Doubler les caractères dans une string :
l4 = [c * 2 for c in "spam"]
print(l4)  # => ['ss', 'pp', 'aa', 'mm']

#   - Mettre en majuscules toutes les strings d'une liste :
fruits = ["banane", "pomme", "citron"]
f = [fruit.upper() for fruit in fruits]
# (On rappelle que .upper() permet de mettre une chaîne en majuscule)
print(f)  # => ['BANANE', 'POMME', 'CITRON']

#   - Remplacer des strings par leur longueur et y ajouter 10 :
l5 = [len(fruit) + 10 for fruit in fruits]
print(l5)  # => [16, 15, 16]

"""
Les compréhensions sont un outil très puissant et parfois assez complexe
à visualiser… il est donc recommandé de beaucoup s'entraîner !

Note : les compréhensions sont un raccourci pour créer une liste rapidement,
mais on pourra toujours générer la même liste avec une boucle.

Ainsi ces deux compréhensions sont équivalentes :
"""
l_iter = []
for i in range(10):
    l_iter.append(2 * i + 3)

l_comp = [2 * i + 3 for i in range(10)]
print(l_iter == l_comp)  # => True


# Conditions sur les compréhensions
####################################

"""
Si on veut conserver uniquement certains valeurs de l'itérable, on ajoutera
une condition "if" à la fin de la compréhension :

[ <expression> for <variable> in <itérable> if <expression booléenne>]

La condition sera testée avec chaque valeur de l'itérable.
"""

# Quelques compréhensions avec condition :
#   - Conserver seulement les valeurs paires d'une liste :
l6 = [3, 4, 2, 1, 5, 7, 12]
l7 = [i for i in l6 if i % 2 == 0]
print(l7)  # => [4, 2, 12]

#   - Conserver seulement les chaînes de longueur impaire :
def est_de_longueur_impaire(s):
    return len(s) % 2 == 1


l8 = ["abc", "ab", "abcdef", "c"]
# On peut appeler une fonction dans la condition !
l9 = [s for s in l8 if est_de_longueur_impaire(s)]
print(l9)  # => ['abc', 'c']


# Compréhensions sur des matrices
##################################

"""
Il est possible de construire des compréhensions imbriquées avec des listes de
listes (aussi appelées matrices).
"""

# Exemple avec une matrice 3 * 3 :
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
On peut ensuite utiliser la syntaxe [… for …] sur cette matrice
"""

#   - Pour prendre la deuxième valeur de chaque sous-liste :
m1 = [row[1] for row in matrice]
print(m1)  # => [2, 5, 8]

#   - Pour ajouter 7 à chaque deuxième valeur :
m2 = [row[1] + 7 for row in matrice]
print(m2)  # => [9, 12, 15]

#   - Pour ne garder que les valeurs paires de la colonne du milieu :
m3 = [row[1] for row in matrice if row[1] % 2 == 0]
print(m3)  # => [2, 8]

#   - Pour obtenir la matrice suivante :
#     [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
m4 = [[3 * i + j for j in range(3)] for i in range(5)]
print(m4)

#   - Pour conserver seulement les valeurs en diagonale :
m5 = [matrice[i][i] for i in [0, 1, 2]]
print(m5)  # => [1, 5, 9]

# Compréhensions chaînées
##########################

"""
Il est à noter que l'on peut "chaîner" les compréhensions , càd avoir des
itérations sur deux variables en même temps dans la même compréhension
(attention, noeuds au cerveau possibles).

Toutes les possibilités seront alors parcourues : si l'on a une itération sur
5 valeurs, puis sur 4 valeurs, la partie à gauche sera parcourue 20 fois.
"""
double = [x + y for x in "abc" for y in "lmn"]
double  # => ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
# Ceci permet de trouver rapidement toutes les combinaisons entre deux itérables

tableau = [[i + 2 * j for j in range(4)] for i in range(4)]
tableau  # =>
# [
#     [0, 2, 4, 6],
#     [1, 3, 5, 7],
#     [2, 4, 6, 8],
#     [3, 5, 7, 9]
# ]

# On peut bien sûr ajouter une condition
super_comprehension = [(a,b) for a in range(3) for b in range(3) if a > b]
print(super_comprehension)  # => [(1, 0),(2, 0), (2, 1)]


# Compréhensions avancées
###############################

# Il est possible de partir des clés d'un dictionnaire…
poids_voitures = {"clio": 790, "406": 1230, "X5": 2170}

# …pour créer une liste à partir de ce dictionnaire
[v[::-1] for v in poids_voitures]  # => ['oilc', '604', '5X']

# On peut aussi créer un nouveau dictionnaire à partir de ce dictionnaire
# avec la syntaxe suivante (notez le ".items()" à droite)
{key * 2: value / 10 for (key, value) in poids_voitures.items()}
# => {'clioclio': 79.0, '406406': 123.0, 'X5X5': 217.0}

