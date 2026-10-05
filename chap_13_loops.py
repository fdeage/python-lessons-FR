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
#  Chap. 13     #  Structures de contrôle II : les boucles, range()            #
#               #                                                              #
################################################################################
#
#  - Utilité des boucles
#  - La boucle "while"
#  - La boucle "for" avec une collection
#  - La boucle "for" avec la fonction range()
#  - Équivalence entre "while" et "for"
#  - Les mots-clés "break" et "continue"
#  - Compteurs et accumulateurs
#  - Boucles imbriquées
#
################################################

# Utilité des boucles
######################

# Nous savons comment écrire des instructions de base.
print(32)   # => 32
a = 7       # affecte l'entier 7 à la variable a
# etc.

# mais on cherche parfois à faire des choses répétitives
a = 1
a += 1
a += 1
a += 1
a += 1
a += 1
# etc.
print(a)  # => 6

"""
Ici il pourrait être intéressant de répéter une instruction un certain nombre
de fois. Les structures pour créer ces répétitions s'appellent des boucles
("loops").

Imaginez qu'on veuille afficher les nombres de 1 à 1000 : écrire 1000 fois
print() serait long, source d'erreurs, et impossible à adapter si l'on veut
ensuite aller jusqu'à 2000. Avec une boucle, ce sont 2 lignes de code.

Python, comme la plupart des langages de programmation, propose deux
structures pour créer des boucles :
    1. la structure while ("tant que…") permet de boucler TANT QU'UNE
       CONDITION EST REMPLIE. On ne sait pas à l'avance combien de fois le code
       dans la boucle sera exécuté

    2. la structure "for" (pour tout … dans …) permet d'itérer (= répéter à
       l'identique) un nombre connu de fois. On peut itérer sur les valeurs
       d'un ensemble (liste, dictionnaire, tuples…), ou bien itérer sur une
       suite d'entiers choisis.

Vocabulaire : chaque passage dans une boucle s'appelle une "itération".

Note : les deux types de boucles sont interchangeables, c'est-à-dire que l'on
pourra toujours exprimer une boucle "for" avec une structure "while", et
(presque toujours) inversement. Cependant il y aura souvent une structure plus
simple que l'autre pour chaque situation.
"""


# La boucle "while"
####################

"""
La structure "while" crée une boucle qui va "tourner" jusqu'à ce qu'une
condition devienne fausse. Le code dans la boucle sera exécuté à chaque fois.

La syntaxe ressemble beaucoup à celle de "if" (cf. chap. 12) :
while <condition>:
    code… (indenté, comme pour "if")

La différence : avec "if", le bloc est exécuté au plus une fois ; avec
"while", la condition est re-testée après chaque exécution du bloc, et le
bloc recommence tant qu'elle reste vraie.

La condition sera souvent de type : tant que <x> est inférieur à 0… Le nombre
d'itérations est souvent inconnu au départ.
"""

# Exemple : on initialise une variable x à 0
x = 0
while x < 4:
    print(x)
    x = x + 1
"""
La boucle ci-dessus affichera :

0
1
2
3

Explication : au début, x vaut 0. Comme 0 < 4, le code "dans" la boucle while
est exécuté une première fois : il affiche 0, puis x passe à 1.
On revient alors en haut de la boucle et on teste à nouveau la condition :
1 < 4 est vrai, donc on recommence… x est incrémenté à chaque fois. Au bout
d'un moment, x vaut 4 et la condition devient fausse : le programme quitte
alors la boucle et passe à la suite.

Déroulé pas à pas ("trace" du programme, cf. chap. 1) :

    | x avant | x < 4 ?  | affiche | x après |
    |---------|----------|---------|---------|
    |    0    |  True    |    0    |    1    |
    |    1    |  True    |    1    |    2    |
    |    2    |  True    |    2    |    3    |
    |    3    |  True    |    3    |    4    |
    |    4    |  False   |    -    |    -    |  => sortie de boucle
"""
print("Après la boucle, x vaut", x)  # => Après la boucle, x vaut 4

# Si la condition est fausse dès le départ, le bloc n'est jamais exécuté :
x = 10
while x < 4:
    print("Jamais imprimé")

"""
Exemple typique de "while" : on ne sait pas à l'avance combien de tours il
faudra. Combien de fois peut-on diviser 1000 par 2 avant de passer sous 1 ?
"""
nombre = 1000
nb_divisions = 0
while nombre >= 1:
    nombre = nombre / 2
    nb_divisions += 1
print(nb_divisions)  # => 10 (car 2 ** 10 = 1024 > 1000)

"""
Autre usage typique : redemander une saisie tant qu'elle n'est pas correcte
(cf. chap. 11 sur input()). Ici, on limite aussi le nombre d'essais pour ne
pas boucler indéfiniment.
"""
mot_de_passe = ""
essais = 0
while mot_de_passe != "sesame" and essais < 3:
    mot_de_passe = input("> Mot de passe (indice : sesame) ? ")
    essais += 1

if mot_de_passe == "sesame":
    print(f"Accès autorisé après {essais} essai(s)")
else:
    print("Trop d'essais : accès refusé")

# Note : pour créer une boucle qui tourne à l'infini, il suffit de passer une
# expression qui sera toujours vraie :
# while True:
#     print("Cette boucle ne s'arrêtera jamais")
# C'est logique, puisque True… est toujours vrai !

# Idem avec une expression booléenne :
# while 1 < 4:
#     print("Cette boucle ne s'arrêtera jamais")
# En effet, 1 < 4 est toujours vrai. On verra plus loin comment sortir d'une
# boucle "while True" avec le mot-clé "break".

"""
IMPT: attention, il est fréquent quand on commence la programmation d'écrire
des boucles infinies involontaires ! Si vous ne modifiez pas de variable
dans la boucle, celle-ci n'a aucune chance de s'arrêter…
"""

# Exemple :
i = 0
# while i < 4:
#     print("Cette boucle ne s'arrêtera jamais car on ne modifie pas i")
#     # On a oublié la ligne "i = i + 1" : i vaut 0 pour toujours
# Cette boucle tournera à l'infini.

"""
IMPT : Pour interrompre un programme, il faut presser "ctrl + C". Autrement, une
boucle infinie dans votre programme prendra tout le CPU disponible sur votre
ordinateur… jusqu'à ce que vous l'arrêtiez !

Pour éviter les boucles infinies, posez-vous trois questions :
    1. ma variable est-elle bien initialisée AVANT la boucle ?
    2. la condition est-elle vraie au départ (sinon on n'entre jamais) ?
    3. le bloc modifie-t-il bien une variable de la condition, de façon à ce
       qu'elle finisse par devenir fausse ?
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

À chaque itération, une_variable prend automatiquement la valeur suivante de
l'ensemble : pas besoin de l'initialiser ni de l'incrémenter soi-même.

Exemple (on utilise ici une liste, notée entre crochets : les listes seront
détaillées au chap. 16) :
"""
mammiferes = ["chien", "chat", "souris"]
for animal in mammiferes:
    print(f"{animal} est un mammifère")

"""
Ce programme affichera :

chien est un mammifère
chat est un mammifère
souris est un mammifère

Au 1er tour, animal vaut "chien" ; au 2e, "chat" ; au 3e, "souris". Il n'y a
plus de valeur : la boucle s'arrête. Le nom "animal" est choisi librement
(c'est une variable comme une autre) : choisissez un nom parlant !
"""

# Autre exemple avec une string (c'est un itérable !) :
s = "abcdef"

for c in s:
    print(c)

"""
Ce programme affichera chaque caractère sur une ligne :

a
b
c
d
e
f
"""

# Les valeurs de la collection peuvent être de types différents :
test = [[3, 4, 5], True, "abcd", 6.4]

for i in test:
    print(i)

"""
Ce programme affichera :

[3, 4, 5]
True
abcd
6.4

Notez que la liste [3, 4, 5] est affichée en entier : "for" ne parcourt que le
premier niveau de la collection (pour parcourir aussi la liste intérieure, il
faudrait une boucle imbriquée, voir plus bas).
"""

"""
IMPT : "for" ne fonctionne qu'avec un itérable.

Pour plus de détails sur les itérables, voir le chap. 23 de ce cours plus loin.
"""
try:
    for chiffre in 12345:  # un int n'est pas itérable…
        print(chiffre)
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => TypeError: 'int' object is not iterable

# Pour parcourir les chiffres d'un nombre, on peut le convertir en string :
for chiffre in str(12345):
    print(chiffre, end=" ")  # end=" " : pas de retour à la ligne (cf. chap. 7)
print()  # => 1 2 3 4 5


# La boucle "for" avec la fonction range()
###########################################

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

# Si l'on n'a pas besoin de la valeur de i, la convention est de nommer la
# variable "_" :
for _ in range(3):
    print("Hip hip hip, hourra !")  # => imprimé 3 fois

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
Enfin, range(debut, fin, pas) retourne un itérable de nombres de début
à fin (exclu) en incrémentant du pas à chaque fois (le "pas" est l'écart entre
deux valeurs consécutives).

Si le pas n'est pas indiqué, la valeur par défaut est 1.
"""
for i in range(4, 8, 2):
    print(i)
"""
Ceci affichera :

4
6

(8 n'est pas affiché, car la borne de fin est toujours exclue !)
"""

# Le pas peut être négatif, pour compter à rebours :
for i in range(3, 0, -1):
    print(i)
print("Décollage !")
"""
Ceci affichera :

3
2
1
Décollage !
"""

"""
On peut combiner range() avec input() pour des résultats intéressants…
Ainsi le code ci-dessous affichera tous les anniversaires, en commençant par 1
(saisissez un nombre entier, sinon int() soulèvera une ValueError, cf.
chap. 11)
"""
age = int(input("> Quel est ton âge ? "))

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
list(range(1, 0))       # => [] (on ne peut pas aller de 1 à 0 avec un pas de +1)

# range() n'accepte que des entiers :
try:
    range(0, 1, 0.1)
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => TypeError: 'float' object cannot be interpreted as an integer

"""
Remarque : modifier la variable de boucle DANS le bloc n'a aucun effet sur
les itérations suivantes, car "for" lui redonne la valeur suivante à chaque
tour :
"""
for i in range(3):
    print(i)  # => 0, puis 1, puis 2 : la ligne suivante ne change rien
    i = 100

# Par contre, après la boucle, la variable garde sa dernière valeur :
print(i)  # => 100 (la dernière valeur qu'on lui a affectée dans le bloc)


# Équivalence entre "while" et "for"
#####################################

"""
Une boucle "for" sur range() peut toujours s'écrire avec "while" : c'est
"for" qui se charge de l'initialisation et de l'incrémentation.
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
Dans la version "while", il y a trois éléments à ne pas oublier :
    1. l'initialisation : i = 0
    2. la condition : i < 5
    3. l'incrémentation : i = i + 1
Avec "for i in range(5)", les trois sont réunis sur une seule ligne, et on ne
peut pas en oublier un : pas de risque de boucle infinie.

"for" est donc plus "expressif" puisqu'il gère automatiquement la création et
l'incrémentation de la variable.

On utilisera donc "while" seulement quand on ne peut pas faire autrement,
c'est-à-dire quand le nombre d'itérations n'est pas connu à l'avance (saisie
utilisateur, calcul qui converge, jeu qui tourne tant que le joueur n'a pas
perdu…).
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

# "break" devient utile combiné avec un "if" : on arrête de chercher dès qu'on
# a trouvé ce qu'on voulait.
# Exemple : trouver le premier multiple de 7 supérieur à 50
for n in range(50, 100):
    if n % 7 == 0:
        print(f"Le premier multiple de 7 après 50 est {n}")  # => … est 56
        break
    print(f"{n} n'est pas un multiple de 7")  # imprimé pour 50, 51… 55

# Avec "while True", "break" permet d'écrire une boucle dont la condition de
# sortie est au milieu du bloc :
compteur = 0
while True:
    compteur += 1
    if compteur == 3:
        break
print(compteur)  # => 3

# L'instruction "continue" permet de passer directement à l'itération suivante,
# sans exécuter la fin du bloc. On l'utilisera souvent avec une structure "if"
for i in range(6):
    print("Imprimé à chaque fois")
    if i > 4:
        continue
    print("Imprimé pour i de 0 à 4")

"""
Résultat : "Imprimé à chaque fois" apparaît 6 fois, et "Imprimé pour i de 0
à 4" seulement 5 fois (au dernier tour, i vaut 5 et "continue" saute le
second print).
"""

# Exemple plus parlant : afficher seulement les nombres impairs
for i in range(10):
    if i % 2 == 0:
        continue  # nombre pair : on passe au suivant
    print(i, end=" ")
print()  # => 1 3 5 7 9

# Attention avec "while" : "continue" retourne directement au test de la
# condition. Si l'incrémentation se trouve après "continue", elle est sautée…
# et la boucle devient infinie ! On incrémente donc AVANT le "continue" :
i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    print("Toujours imprimé, sauf pour i = 2 :", i)

"""
Ces instructions, break et continue, sont peu utilisées, car on peut souvent
les remplacer par une autre structure… mais il faut savoir les comprendre
dans un programme.

IMPT : "break" et "continue" n'agissent que sur la boucle la plus proche
qui les contient (voir boucles imbriquées plus bas).
"""


# Compteurs et accumulateurs
#############################

"""
Deux "motifs" (patterns) reviennent sans cesse avec les boucles :
    1. le compteur : une variable initialisée à 0 avant la boucle, et
       incrémentée de 1 à chaque fois qu'une condition est remplie,
    2. l'accumulateur : une variable initialisée avant la boucle (à 0 pour une
       somme, 1 pour un produit, "" pour une chaîne…), et mise à jour à chaque
       itération.
"""

# Compteur : combien de "a" dans cette phrase ?
phrase = "la vie est un long fleuve tranquille, a dit quelqu'un"
nb_a = 0  # initialisation AVANT la boucle
for lettre in phrase:
    if lettre == "a":
        nb_a += 1
print(nb_a)  # => 3

# Accumulateur (somme) : somme des entiers de 1 à 100
somme = 0
for i in range(1, 101):
    somme += i
print(somme)  # => 5050

# Accumulateur (produit) : factorielle de 5, soit 1 × 2 × 3 × 4 × 5
factorielle = 1  # surtout pas 0, sinon le produit vaudrait toujours 0 !
for i in range(1, 6):
    factorielle *= i
print(factorielle)  # => 120

# Accumulateur (string) : inverser une chaîne
mot = "python"
inverse = ""
for lettre in mot:
    inverse = lettre + inverse  # on ajoute chaque lettre "par la gauche"
print(inverse)  # => nohtyp

"""
IMPT : l'initialisation doit se faire AVANT la boucle. Si on écrit
"somme = 0" à l'intérieur de la boucle, la somme est remise à zéro à chaque
tour !
"""


# Boucles imbriquées
#####################

"""
Comme les "if", les boucles peuvent être imbriquées : une boucle à l'intérieur
d'une autre. Pour chaque itération de la boucle extérieure, la boucle
intérieure est exécutée EN ENTIER.
"""

# Exemple : les tables de multiplication de 1 à 3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")  # à la fin de chaque table (dans la boucle sur i seulement)
"""
Ceci affichera :

1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
---
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
---
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
---

Le bloc intérieur est donc exécuté 3 × 3 = 9 fois. Attention : avec des
boucles imbriquées, le nombre d'itérations se multiplie vite (1000 × 1000 =
un million) !
"""

# Dessiner un triangle d'étoiles : la boucle intérieure dépend de i
for i in range(1, 5):
    ligne = ""
    for _ in range(i):
        ligne += "*"
    print(ligne)
"""
Ceci affichera :

*
**
***
****
"""

# "break" ne sort que de la boucle intérieure :
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # quitte la boucle sur j… mais pas celle sur i
        print(i, j)
"""
Ceci affichera :

0 0
1 0
2 0
"""
