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
#  Chap. 17     #  Types construits II : les tuples                            #
#               #                                                              #
################################################################################
#
#  - Définition et création
#  - Intérêt des tuples
#  - Opérations de base
#  - Parcourir un tuple
#  - Déballage ("unpacking")
#  - Comparer des tuples
#  - Modifier un tuple
#  - Conversions entre listes et tuples
#  - En bref
#
###############################

# Définition et création
#########################

"""
Les tuples sont des séquences d'éléments, comme des listes : la seule différence
est qu'ils sont persistants ("immutable" en anglais) : on ne peut pas les
modifier une fois créés.

À l'inverse des listes, dont la taille peut varier à l'infini, les tuples
sont utilisés quand on souhaite manipuler des ensembles de valeurs de taille
fixe : un vecteur, une ligne de base de données, des coordonnées (x, y), une
date (jour, mois, année), etc. On a ensuite la garantie que le nombre de
valeurs et leur emplacement dans le tuple ne changeront jamais.

À part ça, les tuples fonctionnent presque exactement comme des listes. En
français, on les appelle parfois "n-uplets" (ou "p-uplets").
"""

# On les déclare avec des parenthèses autour d'une séquence de valeurs…
tuple_vide = ()
tup = (1, 2, 3, 4)
print(tup)  # => (1, 2, 3, 4)

print(type(tup))  # => <class 'tuple'>
print(type(tuple_vide))  # => <class 'tuple'>
print(len(tuple_vide))   # => 0

# …mais il est fréquent de rencontrer aussi cette écriture sans parenthèses :
# ce sont en fait les VIRGULES qui créent le tuple, pas les parenthèses !
tup_alternatif = 4, 5, 6
print(tup_alternatif)  # => (4, 5, 6)

# Pour un tuple à une seule valeur, il faut ajouter une virgule finale (pour
# éviter la confusion avec un entier entre parenthèses)
(1)   # le nombre 1 entre parenthèses…
(1,)  # …un tuple à une seule valeur

print(type((1)))   # => <class 'int'>
print(type((1,)))  # => <class 'tuple'>
print(type(1,))    # => <class 'int'> (ici la virgule sépare les arguments de
#                    type() : il faut bien les parenthèses autour de "1,")

# Attention donc à la virgule oubliée en fin de ligne, source de bugs étranges :
prix = 12.5,       # oups, une virgule en trop…
print(prix)        # => (12.5,) …prix est un tuple, et non un float !

# On peut aussi créer un tuple à partir d'une autre séquence avec la fonction
# intégrée tuple() (cf. la section "Conversions" plus bas)
print(tuple("abc"))  # => ('a', 'b', 'c')
print(tuple())       # => () (un tuple vide)


# Intérêt des tuples
#####################

"""
Question : quel intérêt de ne pas pouvoir faire autant de choses qu'avec une
liste normale ?

Réponse : les tuples offrent avant tout la garantie qu'on ne va pas modifier
une valeur dans un programme. Ils permettent ainsi de simuler l'exécution du
programme plus facilement : si une fonction reçoit un tuple, on sait qu'elle
ne pourra pas le modifier "dans notre dos".

Ils ont aussi deux autres avantages, plus techniques :
    1. comme ils ne changent pas, ils peuvent servir de CLÉS dans un
       dictionnaire (on dit qu'ils sont "hashables", cf. chap. 18), ce qui est
       impossible avec une liste
    2. ils sont un peu plus légers en mémoire et un peu plus rapides à créer
       que les listes (Python sait qu'ils ne grandiront jamais)

Une règle d'usage courante :
    - liste : beaucoup d'éléments DE MÊME NATURE (des notes, des noms…), dont le
      nombre peut varier
    - tuple : quelques éléments DE NATURES DIFFÉRENTES, dont chaque position a
      un sens précis (ex. : ("Dupont", "Marie", 1987) = nom, prénom, année)
"""

# Comme pour les listes, on peut affecter plusieurs variables avec un seul
# tuple
a, b, c = (1, 2, 3)  # a vaut 1, b vaut 2 et c vaut 3
print(type(a))  # => <class 'int'>
print(type(b))  # => <class 'int'>
print(type(c))  # => <class 'int'>


# IMPT : on les utilise très souvent pour qu'une fonction retourne plusieurs
# valeurs (cf. chap. 15, "Retour multiple")
def retours_multiples(parametre):
    valeur1 = parametre * 2
    valeur2 = parametre + 8
    valeur3 = parametre / 3
    return valeur1, valeur2, valeur3  # les virgules créent un tuple !


l = retours_multiples(2)
print(l)        # => (4, 10, 0.6666666666666666)
print(type(l))  # => <class 'tuple'>

# On peut aussi directement affecter plusieurs valeurs :
a, b, c = retours_multiples(3)
print(a, b, c)   # => 6 11 1.0
print(type(a))   # => <class 'int'>
print(type(c))   # => <class 'float'> (une division "/" donne toujours un float)

# Attention, il faut avoir le même nombre de variables que de valeurs :
try:
    a, b, c, d = retours_multiples(4)
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Opérations de base
#####################

"""
Comme dans une liste, on peut ranger n'importe quoi dans un tuple, et en
autant d'exemplaires qu'on veut :
"""
pouet = (3.5, ("autre", "tuple!"), False, [2, 5, True], 42, 42)

# La syntaxe est la même que pour accéder à un élément d'une liste
print(pouet[0])  # => 3.5, comme une liste
print(pouet[1])  # => ('autre', 'tuple!')
print(pouet[1][0])  # => autre (le 1er élément du tuple contenu dans pouet)

try:
    pouet[6]  # => IndexError: tuple index out of range (cf. liste)
except IndexError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# On peut utiliser la plupart des opérations des listes sur des tuples
print(len(pouet))  # => 6
print(pouet[:2])  # => (3.5, ('autre', 'tuple!')) (cf. les slices, chap. 31)
print(pouet[-1])  # => 42
print(42 in pouet)  # => True
print("pouet" not in pouet)  # => True
print(pouet.index(False))  # => 2 (indice de la première apparition de False)
print(pouet.count(42))  # => 2 (nombre d'apparitions de 42 dans le tuple)

# Note : .index() et .count() sont les deux SEULES méthodes des tuples (une
# liste en a beaucoup plus, car la plupart servent à la modifier)

# Comme pour les listes, "+" concatène deux tuples et "*" répète un tuple. Ces
# opérations ne modifient pas les tuples d'origine : elles en créent un NOUVEAU
print((1, 2) + (3, 4))  # => (1, 2, 3, 4)
print((0,) * 5)         # => (0, 0, 0, 0, 0)
print(("a", "b") * 2)   # => ('a', 'b', 'a', 'b')

# Les fonctions intégrées min(), max() et sum() fonctionnent aussi
notes = (12, 8, 17, 14)
print(min(notes))  # => 8
print(max(notes))  # => 17
print(sum(notes))  # => 51
print(sum(notes) / len(notes))  # => 12.75 (la moyenne)

# IMPT : on peut intervertir le contenu de deux variables avec la
# syntaxe a, b = b, a
x = 2
y = 3
y, x = x, y  # y vaut maintenant 2 et x vaut 3
print(x, y)  # => 3 2

"""
Comment ça marche ? Python évalue d'abord tout le côté DROIT du "=" : il crée
le tuple (x, y), càd (2, 3). Puis il "déballe" ce tuple dans les variables du
côté GAUCHE : y reçoit 2 et x reçoit 3. Dans beaucoup d'autres langages, il
faudrait passer par une variable temporaire :
    temp = x
    x = y
    y = temp
"""


# Parcourir un tuple
#####################

# Comme une liste ou une string, on peut parcourir un tuple avec une boucle for
# (cf. chap. 13)
jours_weekend = ("samedi", "dimanche")
for jour in jours_weekend:
    print(f"Le {jour}, on se repose.")
# => Le samedi, on se repose.
# => Le dimanche, on se repose.

# On peut aussi parcourir ses indices avec range() et len()
for i in range(len(jours_weekend)):
    print(i, jours_weekend[i])
# => 0 samedi
# => 1 dimanche

# Très fréquent : une liste de tuples, que l'on "déballe" dans la boucle
eleves = [("Alice", 15), ("Bob", 12), ("Chloé", 18)]
for nom, note in eleves:
    print(f"{nom} a eu {note}/20")
# => Alice a eu 15/20
# => Bob a eu 12/20
# => Chloé a eu 18/20
"""
À chaque tour de boucle, Python prend un tuple de la liste, ex. ("Alice", 15),
et le déballe dans les deux variables nom et note (cf. section suivante).
"""


# Déballage ("unpacking")
##########################

"""
On a vu qu'on pouvait affecter les valeurs d'un tuple à plusieurs variables
d'un coup : c'est le "déballage" (en anglais : "unpacking"). L'opération
inverse, qui consiste à regrouper des valeurs dans un tuple, est
l'"emballage" ("packing").
"""
point = 3, 7      # emballage : on crée le tuple (3, 7)
px, py = point    # déballage : px vaut 3 et py vaut 7
print(px, py)     # => 3 7

# Le déballage fonctionne avec n'importe quelle séquence, pas seulement les
# tuples
premier, deuxieme, troisieme = "abc"
print(premier, troisieme)  # => a c
u, v = [10, 20]
print(u + v)  # => 30

# On peut déballer des tuples imbriqués en respectant la même "forme"
(nom, prenom), age = ("Dupont", "Marie"), 37
print(prenom, nom, age)  # => Marie Dupont 37

# Pas assez de valeurs pour le nombre de variables : erreur aussi
try:
    i, j, k = (1, 2)
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# On peut récupérer "le reste" des valeurs avec une étoile (*). La variable
# étoilée reçoit une LISTE (éventuellement vide)
tete, *queue = (1, 2, 3, 4, 5)
print(tete)   # => 1
print(queue)  # => [2, 3, 4, 5]

debut, *milieu, fin = (1, 2, 3, 4, 5)
print(milieu)  # => [2, 3, 4]

# Convention : on nomme "_" une variable dont on ne veut pas se servir
annee, _, _ = (2024, 2, 20)  # seule l'année nous intéresse
print(annee)  # => 2024


# Comparer des tuples
######################

"""
On peut comparer deux tuples avec ==, !=, <, >, etc. (cf. chap. 9).

    - "==" vérifie que les deux tuples ont exactement les mêmes éléments, dans
      le même ordre.
    - "<" et ">" comparent les tuples élément par élément, de gauche à droite,
      comme on range des mots dans un dictionnaire papier (on dit que c'est
      l'ordre "lexicographique") : dès que deux éléments diffèrent, c'est eux
      qui décident du résultat.
"""
print((1, 2, 3) == (1, 2, 3))  # => True
print((1, 2, 3) == (3, 2, 1))  # => False : l'ordre compte !
print((1, 2) == [1, 2])        # => False : un tuple n'est pas une liste
print((1, 2, 3) < (1, 3, 0))   # => True, car 2 < 3 (les 1ers sont égaux)
print((2, 0) > (1, 99))        # => True, car 2 > 1 : la suite est ignorée
print((1, 2) < (1, 2, 0))      # => True : le tuple le plus court est "avant"

# Pratique pour comparer des dates sous la forme (année, mois, jour) :
date1 = (2023, 12, 25)
date2 = (2024, 1, 15)
print(date1 < date2)  # => True : 2023 < 2024, on ne regarde même pas les mois


# Modifier un tuple
####################

# Si on essaie de modifier le tuple, les méthodes courantes échoueront :
try:
    tup[0] = 1  # => TypeError: 'tuple' object does not support item assignment
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    tup.append(4)  # => AttributeError: 'tuple' object has no attribute 'append'
except AttributeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    del tup[0]  # => TypeError: 'tuple' object doesn't support item deletion
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")

# Cependant, certaines modifications sont quand même possibles :

# 1. On peut toujours modifier le CONTENU d'un type construit dans un tuple
print(pouet)  # => (3.5, ('autre', 'tuple!'), False, [2, 5, True], 42, 42)
print(pouet[3])  # => [2, 5, True]

pouet[3][0] = 15  # => le tuple contient toujours la même liste, c'est le
# CONTENU de cette dernière qui change
print(pouet[3])  # => [15, 5, True]
print(pouet)  # => (3.5, ('autre', 'tuple!'), False, [15, 5, True], 42, 42)

"""
Le tuple garantit seulement que ses "cases" désignent toujours les mêmes
objets. Si l'un de ces objets est lui-même modifiable (une liste), il peut
changer. Un tel tuple ne peut d'ailleurs plus servir de clé de dictionnaire.
"""

# 2. On peut réaffecter le nom d'un tuple à une autre valeur
pouet = "pouet"  # => Pas d'erreur, car le tuple auquel la variable pouet
# faisait référence ne change pas : c'est la variable qui désigne maintenant
# autre chose (cf. chap. 10)
print(pouet)  # => pouet

# 3. On peut enfin remplacer un tuple par un tuple plus grand
tup = tup + (5, 6, 7)
print(tup)  # => (1, 2, 3, 4, 5, 6, 7)
# (En fait, il s'agit aussi d'une réaffectation : "tup + (5, 6, 7)" crée un
# NOUVEAU tuple, et la variable tup désigne désormais ce nouveau tuple)

# 4. Pour "modifier" un élément, on construit donc un nouveau tuple :
coord = (10, 20, 30)
coord = (coord[0], 99, coord[2])  # on remplace le 2e élément
print(coord)  # => (10, 99, 30)


# Conversions entre listes et tuples
#####################################

"""
Si on a vraiment besoin de modifier un tuple, on peut le convertir en liste
avec list(), faire les modifications, puis le reconvertir avec tuple().
"""
couleurs = ("rouge", "vert", "bleu")
liste_couleurs = list(couleurs)   # => ['rouge', 'vert', 'bleu']
liste_couleurs.append("jaune")
liste_couleurs[0] = "orange"
couleurs = tuple(liste_couleurs)
print(couleurs)  # => ('orange', 'vert', 'bleu', 'jaune')

# À l'inverse, on peut "geler" une liste en tuple pour la protéger
scores = [3, 1, 2]
scores_figes = tuple(scores)
print(scores_figes)  # => (3, 1, 2)


# En bref
##########

"""
| opération                    | liste           | tuple                 |
| ---------------------------- | --------------- | --------------------- |
| déclaration                  | [1, 2, 3]       | (1, 2, 3) ou 1, 2, 3  |
| un seul élément              | [1]             | (1,)                  |
| accès : x[0], x[-1], len(x)  | oui             | oui                   |
| "in", "+", "*", for          | oui             | oui                   |
| modification : x[0] = …      | oui             | NON                   |
| .append(), .pop(), del       | oui             | NON                   |
| clé de dictionnaire          | NON             | oui (si son contenu   |
|                              |                 | est lui-même fixe)    |

IMPT : retenez surtout
    - la virgule pour le tuple à un élément : (1,)
    - le retour multiple des fonctions : return a, b
    - le déballage : a, b = b, a
"""
