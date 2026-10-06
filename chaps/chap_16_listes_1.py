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
#  Chap. 16     #  Types construits I : les listes (I)                         #
#               #                                                              #
################################################################################
#
#  - Définition et intérêt
#  - Déclarer une liste
#  - Accéder à une valeur de la liste
#  - Modifier une valeur de la liste
#  - Longueur d'une liste : `len()`
#  - `.append()`, `.extend()`, `.pop()`, `del` et `+`
#  - Parcourir une liste avec "for"
#  - En bref
#
###########################################

"""
Introduction : les types construits

Nous allons nous intéresser maintenant à ce qu'on appelle les "types
construits" (par opposition aux "types simples" que sont les booléens, ints et
floats).

Les types construits permettent de stocker non pas une seule valeur, mais
plusieurs valeurs en même temps.

Les principaux types construits de Python sont :
    - les strings (chap. 7),
    - les listes (chap. 16),
    - les tuples (chap. 17),
    - les dictionnaires (chap. 18),
    - les ensembles (chap. 25)

Les strings ressemblent à un type simple, mais supportent des opérateurs de
types construits. Elles sont en fait très similaires à des listes de caractères.
"""


# Définition et intérêt
########################

"""
Les listes (similaires aux "tableaux" d'autres langages, comme les "arrays"
en C ou en JavaScript) sont des valeurs qui permettent de stocker des
séquences d'éléments, de toute nature : strings, ints… ou même d'autres
listes !

On peut y ranger simultanément des valeurs de nature différente.

Une liste est :
    - ordonnée : chaque élément a une position (un "indice") fixe, et l'ordre
      d'insertion est conservé,
    - modifiable (on dit "mutable") : on peut ajouter, retirer ou remplacer
      des éléments après sa création,
    - de taille variable : elle grandit ou rétrécit selon les besoins.
"""

# Les listes sont utiles quand on commence à avoir plusieurs variables de même
# nature. Par exemple :
voiture_1 = "bleue"
voiture_2 = "rouge"
voiture_3 = "jaune"
voiture_4 = "verte"
# …

"""
Si l'on souhaite conserver plus de voitures, il faudra créer une nouvelle
variable à chaque fois, avec le bon numéro à la fin, ce qui pose plusieurs
problèmes :
    - comment ajouter ou supprimer facilement une voiture ?
    - comment s'assurer que l'on ne se trompe pas dans la numérotation ?

Heureusement Python, comme la plupart des langages, nous propose un type pour
"ranger" différentes valeurs dans une seule : la liste.
"""

# On la déclare avec la syntaxe "[…]"
voitures = [voiture_1, voiture_2, voiture_3]
# ou directement :
voitures = ["bleue", "rouge", "jaune"]
print(voitures)  # => ['bleue', 'rouge', 'jaune']

"""
On voit déjà ses intérêts :
    - on centralise dans la même variable de valeurs qui "vont ensemble"
    - on évite toute confusion sur la numérotation des valeurs, qui est gérée
      par la liste (on le verra plus loin)
"""


# Déclarer une liste
#####################

# Cette syntaxe crée une liste vide, que l'on pourra remplir plus tard
li = []
print(li)        # => []
print(type(li))  # => <class 'list'>

# Pour pré-remplir une liste, on énumère les valeurs en les séparant par ","
liste_pre_remplie = [4, 5, 6]

# On peut mélanger les types dans une même liste, et même les imbriquer
liste_variee = ["pouet", 3, 4.5, True, [], "Hop", [1, 2, 3]]

"""
liste_variee contient 7 valeurs, dans l'ordre :
    0. une `string` : "pouet"
    1. un `int` : 3
    2. un `float` : 4.5
    3. un `bool` True
    4. une `list` (vide)
    5. encore une `string`
    6. et enfin une autre `list` : [1, 2, 3]

Remarque : la liste vide [] à l'indice 4 compte bien comme UNE valeur, même si
elle ne contient rien. De même, [1, 2, 3] à l'indice 6 compte pour une seule
valeur de liste_variee (une liste "imbriquée").

Pour la lisibilité, on peut écrire une longue liste sur plusieurs lignes :
entre crochets, les sauts de ligne sont autorisés. La virgule après le
dernier élément est optionnelle (mais pratique pour en ajouter un plus tard).
"""
jours = [
    "lundi",
    "mardi",
    "mercredi",
    "jeudi",
    "vendredi",
]
print(jours)  # => ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']


# Accéder à une valeur de la liste
###################################

"""
Une fois ces valeurs stockées dans la liste, on peut y accéder en partant de
leur "ordre" dans la liste.

IMPT: cet ordre commence toujours à 0.

On écrit le nom de la liste, suivi de l'indice entre crochets : c'est la même
syntaxe que pour accéder à un caractère d'une string (cf. chap. 7).
"""
liste_variee[0]  # => "pouet"
liste_variee[3]  # => True
liste_variee[6]  # => [1, 2, 3]

# La valeur obtenue s'utilise comme n'importe quelle autre valeur :
print(liste_variee[1] + 10)       # => 13
print(liste_variee[0].upper())    # => POUET (méthode de string, cf. chap. 8)

# Pour une liste dans une liste, on enchaîne les crochets :
print(liste_variee[6][0])  # => 1 (le 1er élément de la liste [1, 2, 3])

# L'accès au dernier élément peut aussi se faire "par la fin" avec "-n"
liste_variee[-1]  # => [1, 2, 3]
liste_variee[-2]  # => "Hop" (l'avant-dernier élément)

"""
Résumé des indices pour la liste ["a", "b", "c", "d"] :

    valeur :              "a"   "b"   "c"   "d"
    indice positif :       0     1     2     3
    indice négatif :      -4    -3    -2    -1

On peut aussi extraire plusieurs éléments d'un coup avec la syntaxe
liste[debut:fin] : ce sont les "slices", détaillées au chap. 31.
"""

# Accéder à un élément en dehors des limites soulève une IndexError
try:
    liste_variee[7]  # => Lève une IndexError
except IndexError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# La liste vide ne contient, par définition, aucune valeur. Même l'indice 0
# n'existe pas !
liste_vide = []
try:
    liste_vide[0]  # => Lève aussi une IndexError
except IndexError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Pour tester si une valeur est dans une liste, on peut utiliser "… in …" et
son complément "… not in …"
"""
print(1 in liste_pre_remplie)      # => False
print(1 not in liste_pre_remplie)  # => True
print(5 in liste_pre_remplie)      # => True

# C'est très pratique dans un "if" (cf. chap. 12) :
if "rouge" in voitures:
    print("Il y a une voiture rouge")  # => Il y a une voiture rouge


# Modifier une valeur de la liste
##################################

"""
Contrairement aux strings, qui ne sont pas modifiables (cf. chap. 7), on peut
remplacer un élément d'une liste en lui affectant une nouvelle valeur :
"""
voitures = ["bleue", "rouge", "jaune"]
voitures[1] = "noire"  # on remplace l'élément d'indice 1
print(voitures)  # => ['bleue', 'noire', 'jaune']

voitures[-1] = "grise"  # fonctionne aussi avec les indices négatifs
print(voitures)  # => ['bleue', 'noire', 'grise']

# On ne peut pas créer un nouvel élément de cette façon : l'indice doit exister
try:
    voitures[3] = "verte"
except IndexError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# => IndexError: list assignment index out of range
# (pour ajouter un élément, on utilisera .append(), voir plus bas)

# À comparer avec les strings, qui ne se modifient pas :
mot = "bleue"
try:
    mot[0] = "B"
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# => TypeError: 'str' object does not support item assignment


# Longueur d'une liste : `len()`
#################################

"""
La fonction intégrée len() (cf. chap. 7 et 14) retourne le nombre d'éléments
d'une liste.
"""
print(len(voitures))      # => 3
print(len(liste_variee))  # => 7 (les listes imbriquées comptent pour 1)
print(len([]))            # => 0

"""
IMPT : le dernier indice d'une liste vaut toujours len(liste) - 1, puisqu'on
commence à compter à 0. C'est pour cela que liste_variee[7] provoquait une
IndexError plus haut : liste_variee a 7 éléments, d'indices 0 à 6.
"""
print(voitures[len(voitures) - 1])  # => grise (équivalent à voitures[-1])


# `.append()`, `.extend()`, `.pop()`, `del` et `+`
###################################################

"""
Une liste dispose de "méthodes", c'est-à-dire de fonctions qui lui sont
propres. On les appelle avec la syntaxe liste.methode(…), comme les méthodes
des strings (cf. chap. 8).

Différence importante avec les strings : les méthodes des listes MODIFIENT
DIRECTEMENT la liste (on dit qu'elles agissent "en place"), et retournent en
général None.
"""

#   1. On ajoute des objets à la fin d'une liste avec la méthode `.append()`

# On vérifie que `li` est vide au départ
print(li)  # => []

li.append(1)  # `li` vaut maintenant `[1]`
li.append(2)  # `li` vaut maintenant `[1, 2]`
li.append(4)  # `li` vaut maintenant `[1, 2, 4]`
li.append(3)  # `li` vaut maintenant `[1, 2, 4, 3]`
print(li)     # => [1, 2, 4, 3]

# Attention : .append() ne retourne rien (None), il modifie la liste :
resultat = li.append(5)
print(resultat)  # => None
print(li)        # => [1, 2, 4, 3, 5]
li.pop()         # on retire le 5 pour la suite (voir ci-dessous)

# .append() ajoute toujours UN SEUL élément… même si c'est une liste :
autre = [1, 2]
autre.append([3, 4])
print(autre)       # => [1, 2, [3, 4]] (la liste [3, 4] est UN élément)
print(len(autre))  # => 3

#   2. Pour ajouter PLUSIEURS éléments, on utilise la méthode `.extend()`
autre = [1, 2]
autre.extend([3, 4])
print(autre)  # => [1, 2, 3, 4]


#   3. On enlève le dernier élément d'une liste avec la méthode `.pop()`.
#      Contrairement à .append(), .pop() RETOURNE l'élément enlevé :
dernier = li.pop()  # => `dernier` vaut 3, `li` vaut maintenant `[1, 2, 4]`
print(dernier, li)  # => 3 [1, 2, 4]

# On peut ensuite le remettre en place
li.append(dernier)  # `li` vaut de nouveau `[1, 2, 4, 3]`

# .pop() accepte aussi un indice : il enlève (et retourne) l'élément à cet
# indice. Les éléments suivants sont "décalés" vers la gauche.
premier = li.pop(0)
print(premier, li)  # => 1 [2, 4, 3]
li = [1, 2, 4, 3]   # on remet li dans son état précédent pour la suite

# .pop() sur une liste vide provoque une erreur :
try:
    [].pop()
except IndexError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
# => IndexError: pop from empty list

"""
    4. Pour supprimer un élément à un rang arbitraire sans le récupérer, on
       peut aussi utiliser l'instruction `del` (ce n'est pas une fonction ni
       une méthode, mais un mot-clé de Python).
"""
del li[2]  # On enlève l'élément de rang 2, `li` vaut maintenant `[1, 2, 3]`
print(li)  # => [1, 2, 3]

"""
Attention, `del` ne retourne rien ! On ne peut donc pas écrire :

valeur = del li[2]  # Soulève une erreur
"""

"""
    5. On peut additionner des listes ensemble avec l'opérateur `+`, comme pour
       les strings (on parle de "concaténation")
"""
print(li + liste_pre_remplie)  # => [1, 2, 3, 4, 5, 6]

# Note: les valeurs de `li` et `liste_pre_remplie` ne sont pas modifiées
print(li)                      # => [1, 2, 3]
print(liste_pre_remplie)       # => [4, 5, 6]

"""
C'est la différence entre `+` et `.extend()` : `+` crée une NOUVELLE liste
(qu'il faut stocker dans une variable si on veut la garder), alors que
`.extend()` modifie la liste existante.

On ne peut additionner qu'une liste avec une autre liste :
"""
try:
    li + 4
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
# => TypeError: can only concatenate list (not "int") to list

print(li + [4])  # => [1, 2, 3, 4] (il faut mettre 4 dans une liste)

"""
Note : il existe d'autres méthodes utiles (.insert(), .remove(), .index(),
.count(), .sort()…), que l'on verra au chap. 24.
"""


# Parcourir une liste avec "for"
#################################

"""
On a vu au chap. 13 que la boucle "for" pouvait parcourir une collection :
c'est la façon la plus naturelle de traiter tous les éléments d'une liste,
un par un.
"""
notes = [12, 15, 8, 17]

for note in notes:
    print(f"Note : {note}/20")
"""
Ce code affichera :

Note : 12/20
Note : 15/20
Note : 8/20
Note : 17/20
"""

# Exemple : calculer la moyenne avec un accumulateur (cf. chap. 13)
total = 0
for note in notes:
    total += note
print(total / len(notes))  # => 13.0

# On peut aussi construire une nouvelle liste au fur et à mesure :
notes_bonus = []
for note in notes:
    notes_bonus.append(note + 1)
print(notes_bonus)  # => [13, 16, 9, 18]

"""
Les différentes façons de parcourir une liste (par les indices ou par les
valeurs, avec enumerate()…) seront détaillées au chap. 24.
"""


# En bref
##########

"""
    - Une liste Python est une collection d'objets numérotés.
    - On accède à un élément de la collection à l'aide de son index (ou
      indice), compté à partir de 0. Ainsi :
"""
liste = [10, 20, 30]
print(liste[0]) # => 10
print(liste[2]) # => 30

#   - Python calcule la longueur de la liste avec l'instruction `len(liste)`
len(liste) # => 3

#   - Une liste Python est un objet modifiable (ou "mutable") :
liste[1] = 0
print(liste) # => [10, 0, 30]

"""
    - La création d'une liste Python se fait souvent par accumulation : on peut
      partir d'une liste vide…
"""
liste = []
"""
      …et lui ajouter des éléments, le plus souvent "par la droite" (ou
      "par la fin"). Il y a plusieurs possibilités pour cela :
         1. la méthode `.append()` :
"""
liste.append(2)
print(liste) # => [2]

#        2. la fusion de deux listes :

liste = liste + [4]
print(liste) # => [2, 4]
# (on peut donc ajouter "par la gauche" des éléments à une liste avec cette
# technique)

#        3. l'extension par une autre liste avec `.extend()` :
liste.extend([6, 8])
print(liste)  # => [2, 4, 6, 8]

"""
    - On retire des éléments avec `.pop()` (qui retourne l'élément enlevé) ou
      `del` (qui ne retourne rien).
    - On teste la présence d'un élément avec `in` et `not in`.
    - On parcourt les éléments un par un avec une boucle `for`.
"""
