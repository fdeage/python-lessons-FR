################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2023                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #
#  Chap. 13     #  Structures de contrôle II : les boucles, range()
#               #                                                              #
################################################################################
#
#  - Utilité des boucles
#  - La boucle "while"
#  - La boucle "for" avec une collection
#  - La boucle "for" avec la fonction range()
#  - Les mots-clés "break" et "continue"
#
###########################################################

# Utilité des boucles
######################

# Nous savons comment écrire des instructions de base.
print(32)   # imprime 32
a = 7       # affecte l'entier 7 à la variable a
# etc.

# TODO:
# mais on cherche parfois des choses repetitives
a = 1
a += 1
a += 1
a += 1
a += 1
a += 1


"""
Mais il pourrait être intéressant de répéter une instruction un certain nombre
de fois. Les structures pour créer ces répétitions s'appellent des boucles
("loops").

Python, comme la plupart des langages de programmation, propose deux
structures pour créer des boucles :
    1. la structure while ("tant que…") permet de boucler TANT QU'UNE
       CONDITION EST REMPLIE. On ne sait pas à l'avance combien de fois le code
       dans la boucle sera exécuté

    2. la structure "for" (pour tout … dans …) permet d'itérer (= répéter à
       l'identique) un nombre connu de fois. On peut itérer sur les valeurs
       d'un ensemble (liste, dictionnaire, tuples…), ou bien itérer sur une
       suite d'entiers choisis.

Note : les deux types de boucles sont interchangeables, c'est-à-dire que l'on
pourra toujours exprimer une boucle "while" avec une structure "for", et
inversement. Cependant il y aura souvent une structure plus simple que
l'autre pour chaque situation.
"""


# La boucle "while"
####################

"""
La structure "while" crée une boucle qui va "tourner" jusqu'à ce qu'une
condition devienne fausse. Le code dans la boucle sera exécuté à chaque fois.

La condition sera souvent de type : tant que <x> est inférieur à 0… Le nombre
d'itérations est souvent inconnu au départ.
"""

# Exemple : on initialise une variable x à 4
x = 0
while x < 4:
    print(x)
    x = x + 1
"""
La fonction ci-dessus affichera :

0
1
2
3

Explication : au début, x vaut 0. Comme 0 < 4, le code "dans" la boucle while
est exécuté à chaque fois.
x est incrémenté à chaque fois. Au bout d'un moment, x vaut 4 et la condition
devient fausse : le programme quitte alors la boucle.
"""

# Note : pour créer une boucle qui tourne à l'infini, il suffit de passer une
# expression qui sera toujours vraie :
while True:
    print("Cette boucle ne s'arrêtera jamais")
# C'est logique, puisque True… est toujours vrai !

# Idem avec une expression booléenne :
while 1 < 4:
    print("Cette boucle ne s'arrêtera jamais")
# En effet, 1 < 4 est toujours vrai. On peut même écrire directement :

"""
IMPT: attention, il est fréquent quand on commence la programmation d'écrire
des boucles infinies involontaires ! Si vous ne modifiez pas de variable
dans la boucle, celle-ci n'a aucune chance de s'arrêter…
"""

# Exemple :
i = 0
while i < 4:
    print("Cette boucle ne s'arrêtera jamais car on ne modifie pas i")
    # i = i + 1      # On oublie d'incrémenter i
# Cette boucle tournera à l'infini.

"""
IMPT : Pour interrompre un programme, il faut presser "ctrl + C". Autrement, une
boucle infinie dans votre programme prendra tout le CPU disponible sur votre
ordinateur… jusqu'à ce que celui-ci crashe !
"""


# La boucle "for" avec une collection
######################################

"""
La boucle "for" sert à exécuter un bloc de code UN NOMBRE DÉTERMINÉ DE FOIS.
Contrairement aux boucles avec "while", ce nombre est connu au départ.

Une boucle avec for "itère sur" quelque chose : elle va parcourir UNE FOIS ET
UNE SEULE chaque terme d'un ensemble que l'on devra lui fournir.

Il y a deux façons d'itérer avec for :
    1. avec un ensemble de valeurs contenu dans une variable (liste,
       dictionnaire, tuple…), qu'on appellera une "collection"
    2. avec une liste de valeurs retournée par la fonction range()

On s'intéresse ici au premier cas : avec une collection, c'est-à-dire un
ensemble de valeurs.

La syntaxe utilisée sera :
for une_variable in <ensemble>:
    code…

Exemple :
"""
mammiferes = ["chien", "chat", "souris"]
for animal in mammiferes:
    print(f"{animal} est un mammifère")
"""
Ce programme affichera :

chien est un mammifère
chat est un mammifère
souris est un mammifère
"""

# Autre exemple avec une string (c'est un itérable !) :
s = "abcdef"
for c in s:
    print(c)
"""
Ce programme affichera :

a
b
c
d
e
f
"""

"""
IMPT : "for" ne fonctionne qu'avec un itérable.

Pour plus de détails sur les itérables, voir le chap. 21 de ce cours plus loin.
"""


# La boucle for avec la fonction range()
#########################################

"""
On aura souvent besoin de passer dans une boucle un nombre n de fois.
Python propose une solution intéressante : la fonction range().

range(n) va retourner un itérable de n valeurs, allant de 0 à n - 1, sur lequel
"for" pourra itérer.
"""
range(5)  # => retourne l'itérable [0 - 1 - 2 - 3 - 4]

for i in range(5):
    print(i)
"""
Ce programme affichera :

0
1
2
3
4
"""


"""
IMPT : range(n) contient n valeurs mais va de 0 à n - 1 !

range(debut, fin) retourne un itérable qui va de debut à fin - 1.
Par exemple, ce programme affichera :
  4
  5
  6
  7
"""
for i in range(4, 8):
    print(i)

"""
Enfin, range(debut, fin, pas)" retourne un itérable de nombres de début
à fin en incrémentant du pas à chaque fois (le "pas" est l'écart entre deux
valeurs consécutives).

Si le pas n'est pas indiqué, la valeur par défaut est 1.
"""
for i in range(4, 8, 2):
    print(i)
"""
Ceci affichera :

4
6
8
"""

"""
On peut combiner range() avec input() pour des résultats intéressants…
Ainsi le code ci-dessous affichera tous les anniversaires, en commençant par 1
"""
age = int(input("> Quel est ton âge ?"))

for i in range(1, age + 1):
    print(f"Joyeux anniversaire, tu as {i} ans !")

# Attention : un range() n'est pas une liste, même s'il y ressemble…
type(range(5))  # => <class 'range'>

# …heureusement on peut facilement le transformer en liste avec list()
type(list(range(5)))  # => <class 'list'>

# Pour résumer :
list(range(10))         # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 11))      # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(0, 30, 5))   # => [0, 5, 10, 15, 20, 25]
list(range(0, 10, 3))   # => [0, 3, 6, 9]
list(range(0, -10, -1)) # => [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
list(range(0))          # => []
list(range(1, 0))       # => []


# Équivalence entre "while" et "for"
#####################################

"""
Une boucle "for" est en réalité un raccourci pour une boucle "while".
Ainsi…
"""
i = 0
while i < 5:
    print(i)
    i = i + 1

# …peut-il s'écrire plus simplement :
for i in range(5):
    print(i)

# Exercice : passez le temps suffisant pour comprendre pourquoi ces deux
# boucles font la même chose…

"""
"for" est donc plus "expressif" puisqu'il gère automatiquement la création et
l'incrémentation de la variable.

On utilisera donc "while" seulement quand on ne peut pas faire autrement.
"""


# Les mots-clés "break" et "continue"
######################################

# L'instruction "break" permet de quitter une boucle (for ou while)
while True:
    print("La boucle est infinie mais ceci ne sera imprimé qu'une seule fois")
    break  # On sort de la boucle infinie

for i in range(6):
    print("On devrait avoir 6 print mais ceci sera imprimé une seule fois")
    break  # On sort de la boucle for après une itération…
#            ce qui a peu d'intérêt

# L'instruction "continue" permet d'aller à la fin d'une boucle sans exécuter
# la fin des instructions. On l'utilisera souvent avec une structure "if"
for i in range(6):
    print("Imprimé à chaque fois")
    if i > 4:
        continue
    print("Imprimé pour i de 0 à 4")

while True:
    print("Toujours imprimé")
    continue
    print("Jamais imprimé")

"""
Ces instructions, break et continue, sont peu utilisées, car on peut souvent
les remplacer par une autre structure… mais il faut savoir les comprendre
dans un programme.
"""
