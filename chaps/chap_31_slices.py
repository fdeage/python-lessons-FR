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
#  Chap. 31     #  Slices                                                      #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Syntaxe
#  - Indexation négative
#  - Exemples de Slices
#  - Pas (Step) dans les Slices
#  - Modifier une liste avec les slices
#  - Slices avec d'autres types construits
#  - Copie de séquences avec slices
#  - Conclusion
#
############################################

# Introduction
###############

"""
Les slices ("tranches") sont une technique pour extraire des portions de
séquences (listes, tuples, chaînes de caractères) en utilisant des indices de
début, d'arrêt et, éventuellement, un pas.

On a vu qu'on pouvait accéder à UNE valeur d'une séquence avec son indice entre
crochets (cf. chap. 7 pour les strings, chap. 16 pour les listes) :
"""
ma_liste = ["a", "b", "c", "d", "e"]
print(ma_liste[1])  # => b

"""
Les slices permettent d'accéder à PLUSIEURS valeurs consécutives d'un coup, en
une seule expression, sans écrire de boucle.

Sans slice, pour récupérer les valeurs d'indice 1 à 3, il faudrait écrire :
"""
extrait = []
for i in range(1, 4):
    extrait.append(ma_liste[i])
print(extrait)  # => ['b', 'c', 'd']

# Avec une slice, c'est beaucoup plus court :
print(ma_liste[1:4])  # => ['b', 'c', 'd']

"""
IMPT : une slice retourne une NOUVELLE séquence (une copie de la portion
demandée), du même type que la séquence d'origine : une slice de liste est une
liste, une slice de string est une string, etc. La séquence d'origine n'est pas
modifiée.
"""
print(ma_liste)  # => ['a', 'b', 'c', 'd', 'e'] (inchangée)


# Syntaxe
##########

"""
La syntaxe générale d'un slice est la suivante :

sequence[begin:stop:step]

Mais on peut aussi trouver les séquences suivantes :
sequence[begin:]       (de begin jusqu'à la fin)
sequence[:stop]        (du début jusqu'à stop, non inclus)
sequence[begin:stop]   (de begin à stop, non inclus)
sequence[:]            (toute la séquence)

begin : L'indice de départ (inclusif). Par défaut : le début de la séquence.
stop : L'indice d'arrêt (non inclusif). Par défaut : la fin de la séquence.
step (facultatif) : Le pas, c'est-à-dire l'écart entre deux indices
successifs. Par défaut : 1 (on prend tous les éléments).

IMPT : comme pour range() (cf. chap. 13), l'indice de départ est inclus, mais
pas l'indice d'arrêt. Ainsi, sequence[begin:stop] contient (stop - begin)
éléments.
"""

ma_liste = [i for i in range(10)]  # compréhension de liste, cf. chap. 23
print(ma_liste)  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice de l'indice 2 à l'indice 5 (l'indice 6 n'est pas inclus)
print(ma_liste[2:6])  # => [2, 3, 4, 5] (6 - 2 = 4 éléments)

# Slice avec un pas de 2
print(ma_liste[1:9:2])  # => [1, 3, 5, 7]

# Slice complète, identique à la liste initiale
print(ma_liste[:])  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
Astuce pour bien visualiser : imaginez que les indices désignent les
"séparations" ENTRE les éléments, et non les éléments eux-mêmes :

     +---+---+---+---+---+
     | a | b | c | d | e |
     +---+---+---+---+---+
     0   1   2   3   4   5
    -5  -4  -3  -2  -1

La slice [1:4] prend tout ce qui est entre la séparation 1 et la séparation 4 :
"b", "c" et "d".
"""


# Indexation négative
######################

"""
En Python, vous pouvez utiliser des indices négatifs pour compter à partir de
la fin de la séquence. Par exemple, -1 désigne le dernier élément, -2
l'avant-dernier, et ainsi de suite (cf. chap. 16).

Ces indices négatifs fonctionnent aussi dans les slices :
"""
print(ma_liste[-3:-1])  # => [7, 8] (le dernier, d'indice -1, est exclu)
print(ma_liste[-3:])    # => [7, 8, 9] (les 3 derniers éléments)
print(ma_liste[:-3])    # => [0, 1, 2, 3, 4, 5, 6] (tout sauf les 3 derniers)

# On peut même mélanger indices positifs et négatifs :
print(ma_liste[2:-2])  # => [2, 3, 4, 5, 6, 7] (sans les 2 premiers ni les 2 derniers)


# Exemples de Slices
#####################

"""
Voici quelques slices très courantes, à connaître :
"""
lettres = ["a", "b", "c", "d", "e", "f"]

print(lettres[:2])   # => ['a', 'b'] (les 2 premiers éléments)
print(lettres[2:])   # => ['c', 'd', 'e', 'f'] (tout sauf les 2 premiers)
print(lettres[-2:])  # => ['e', 'f'] (les 2 derniers éléments)
print(lettres[:-1])  # => ['a', 'b', 'c', 'd', 'e'] (tout sauf le dernier)
print(lettres[1:-1])  # => ['b', 'c', 'd', 'e'] (sans le premier ni le dernier)

"""
Remarque : lettres[:2] + lettres[2:] redonne toujours la liste complète, quel
que soit l'indice choisi. C'est pratique pour "couper" une séquence en deux :
"""
n = 4
print(lettres[:n] + lettres[n:])  # => ['a', 'b', 'c', 'd', 'e', 'f']

"""
IMPT : contrairement à l'accès par indice, une slice ne soulève JAMAIS d'erreur
si les indices dépassent les limites de la séquence : elle s'arrête simplement
au bout.
"""
try:
    print(lettres[10])
except IndexError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

print(lettres[4:10])   # => ['e', 'f'] (pas d'erreur !)
print(lettres[10:20])  # => [] (une liste vide, pas d'erreur non plus)

# Si begin est après stop, la slice est vide :
print(lettres[4:2])  # => []

"""
Exemple d'utilisation : afficher les premiers éléments d'une liste pour avoir
un aperçu, sans risquer d'erreur si elle est plus courte que prévu.
"""
notes = [12, 15, 9]
print(f"Les 5 premières notes : {notes[:5]}")  # => Les 5 premières notes : [12, 15, 9]


# Pas (Step) dans les Slices
#############################

"""
Le troisième paramètre, le pas, permet de ne prendre qu'un élément sur deux,
sur trois, etc.
"""
print(ma_liste[::2])   # => [0, 2, 4, 6, 8] (les éléments d'indice pair)
print(ma_liste[1::2])  # => [1, 3, 5, 7, 9] (les éléments d'indice impair)
print(ma_liste[::3])   # => [0, 3, 6, 9] (un élément sur trois)

"""
Le pas peut aussi être négatif : la slice parcourt alors la séquence de droite
à gauche. Dans ce cas, begin doit être APRÈS stop.
"""
print(ma_liste[7:2:-1])  # => [7, 6, 5, 4, 3]
print(ma_liste[2:7:-1])  # => [] (begin est avant stop : la slice est vide)

"""
IMPT : la slice [::-1] retourne la séquence à l'envers. C'est une astuce
très courante :
"""
print(ma_liste[::-1])  # => [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(ma_liste[::-2])  # => [9, 7, 5, 3, 1]

# Un pas nul n'a pas de sens, et soulève une erreur :
try:
    print(ma_liste[::0])
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


# Modifier une liste avec les slices
#####################################

"""
Les listes sont modifiables (cf. chap. 16) : on peut donc aussi utiliser une
slice à GAUCHE du signe "=", pour remplacer toute une portion de liste d'un
coup.
"""
chiffres = [0, 1, 2, 3, 4, 5]
chiffres[1:3] = ["un", "deux"]
print(chiffres)  # => [0, 'un', 'deux', 3, 4, 5]

# La portion remplacée et la nouvelle portion n'ont pas besoin d'avoir la même
# taille : la liste s'agrandit ou rétrécit.
chiffres[1:3] = ["X"]
print(chiffres)  # => [0, 'X', 3, 4, 5]

# Une slice vide permet d'insérer des éléments sans rien supprimer :
chiffres[1:1] = ["insertion", "ici"]
print(chiffres)  # => [0, 'insertion', 'ici', 'X', 3, 4, 5]

# Avec "del" (cf. chap. 16), on supprime toute une portion :
del chiffres[1:4]
print(chiffres)  # => [0, 3, 4, 5]

"""
Attention : on ne peut pas faire cela avec les tuples ni les strings, qui sont
immuables (cf. chap. 17 et chap. 7).
"""
try:
    ma_chaine = "Python"
    ma_chaine[0:2] = "Ca"
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# Pour "modifier" une string, on en crée une nouvelle à partir de slices :
ma_chaine = "Python"
nouvelle_chaine = "C" + ma_chaine[1:]
print(nouvelle_chaine)  # => Cython


# Slices avec d'autres types construits
########################################

"""
Les slices fonctionnent sur toutes les "séquences", c'est-à-dire les types
construits dont les éléments sont ordonnés et accessibles par un indice :
listes, tuples, strings, et même range() (cf. chap. 13).
"""

# Slices d'un tuple : on obtient un tuple
mon_tuple = (10, 20, 30, 40, 50)
print(mon_tuple[1:4])  # => (20, 30, 40)

# Slices d'une string : on obtient une string
ma_chaine = "Python est génial"
print(ma_chaine[7:12])  # => est g
print(ma_chaine[:6])    # => Python
print(ma_chaine[::-1])  # => lainég tse nohtyP

"""
Exemple : tester si un mot est un palindrome (s'il se lit de la même façon
dans les deux sens) devient très simple :
"""
mot = "kayak"
print(mot == mot[::-1])  # => True

"""
Exemple : récupérer l'extension d'un nom de fichier (cf. chap. 28), en
cherchant la position du dernier point avec .rfind() (cf. chap. 8) :
"""
nom_fichier = "rapport.final.csv"
position_point = nom_fichier.rfind(".")
print(nom_fichier[position_point + 1:])  # => csv
print(nom_fichier[:position_point])      # => rapport.final

# Slices d'un range : on obtient un range (qui ne contient que les valeurs
# demandées)
print(range(10)[2:5])        # => range(2, 5)
print(list(range(10)[2:5]))  # => [2, 3, 4]

"""
Il n'y a pas de slice sur les dictionnaires… En effet, un dictionnaire n'est
pas une séquence : on y accède par une clé, pas par une position (cf. chap. 18).

Python cherche donc une clé qui serait… la slice elle-même ! Selon la version
de Python, l'erreur obtenue n'est pas la même :
    - avant Python 3.12 : TypeError: unhashable type: 'slice'
    - depuis Python 3.12 : KeyError: slice(None, 1, None)
On intercepte donc les deux types d'erreurs (cf. chap. 26).
"""
try:
    mon_dict = {'a': 1, 'b': 2}
    mon_dict[:1]
except (TypeError, KeyError) as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err!r})")

# …ni sur les ensembles, qui ne sont pas ordonnés (cf. chap. 25) :
try:
    mon_set = {'a', 'b'}
    mon_set[:1]  # => Lève une TypeError: 'set' object is not subscriptable
except TypeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Pour obtenir une "tranche" d'un dictionnaire, on peut passer par une liste de
ses clés (cf. chap. 27 pour .keys()) :
"""
mon_dict = {'a': 1, 'b': 2, 'c': 3}
premieres_cles = list(mon_dict.keys())[:2]
print(premieres_cles)  # => ['a', 'b']

"""
HP : une slice est en fait un objet Python comme un autre, que l'on peut créer
avec la fonction intégrée slice(begin, stop, step) et stocker dans une
variable. sequence[slice(1, 4)] est équivalent à sequence[1:4].
"""
trois_premiers = slice(0, 3)
print(lettres[trois_premiers])    # => ['a', 'b', 'c']
print(ma_chaine[trois_premiers])  # => Pyt


# Copie de séquences avec slices
#################################

"""
Rappel (cf. chap. 16 et chap. 19) : l'affectation "b = a" ne copie pas une
liste ! Les deux variables désignent alors la MÊME liste : modifier l'une
modifie l'autre.
"""
ma_liste = [i for i in range(10)]
meme_liste = ma_liste      # pas une copie : un deuxième nom pour la même liste
meme_liste[0] = 100
print(ma_liste[0])  # => 100 (la liste originale a été modifiée !)

"""
Comme une slice retourne une nouvelle liste, la slice complète [:] permet de
faire une vraie copie :
"""
ma_liste = [i for i in range(10)]
copie_liste = ma_liste[:]  # Crée une copie de ma_liste
copie_liste[0] = 100
print(copie_liste[0])  # => 100
print(ma_liste[0])     # => 0 (la liste originale est inchangée)

# On peut le vérifier avec l'opérateur "is", qui teste si deux variables
# désignent le même objet (cf. chap. 15) :
print(copie_liste is ma_liste)  # => False
autre_nom = ma_liste      # pas une copie, comme meme_liste plus haut
print(autre_nom is ma_liste)    # => True

"""
Remarque : copie_liste = ma_liste[:] est équivalent à
copie_liste = ma_liste.copy() ou copie_liste = list(ma_liste).

Attention (HP) : il s'agit d'une copie "superficielle" ("shallow copy"). Si la
liste contient elle-même des listes (une matrice, cf. chap. 24), les
sous-listes ne sont PAS copiées : elles restent partagées entre l'original et
la copie.
"""
matrice = [[1, 2], [3, 4]]
copie_matrice = matrice[:]
copie_matrice[0][0] = 999    # on modifie une sous-liste…
print(matrice)  # => [[999, 2], [3, 4]] (…qui est partagée avec l'original !)

copie_matrice[1] = [7, 7]    # on remplace une sous-liste entière…
print(matrice)  # => [[999, 2], [3, 4]] (…cette fois, l'original n'a pas changé)

"""
Pour copier aussi les sous-listes, on peut utiliser une compréhension
(cf. chap. 23), ou la fonction deepcopy() du module copy (cf. chap. 22) :
"""
matrice = [[1, 2], [3, 4]]
copie_profonde = [ligne[:] for ligne in matrice]
copie_profonde[0][0] = 999
print(matrice)  # => [[1, 2], [3, 4]] (l'original est intact)

"""
Remarque : copier un tuple ou une string avec [:] n'a pas d'intérêt, puisqu'ils
ne sont pas modifiables. L'interpréteur Python standard (CPython) ne prend
d'ailleurs pas la peine de créer une copie, et retourne le même objet :
"""
print(mon_tuple[:] is mon_tuple)  # => True


# Conclusion
#############

"""
À retenir :
    - sequence[begin:stop:step] : begin est inclus, stop est exclu, step vaut
      1 par défaut ;
    - les trois paramètres sont facultatifs ; les indices peuvent être négatifs
      (on compte depuis la fin) ;
    - une slice retourne une nouvelle séquence du même type, et ne soulève
      jamais d'IndexError ;
    - [::-1] retourne une séquence à l'envers, [:] fait une copie
      (superficielle) d'une liste ;
    - sur une liste, on peut remplacer ou supprimer une portion avec une slice
      à gauche du "=" ou avec "del" ;
    - les slices fonctionnent sur les séquences (listes, tuples, strings,
      range), mais pas sur les dictionnaires ni les ensembles.

Les slices sont omniprésentes en Data Science : on les retrouve, avec une
syntaxe très proche, dans les bibliothèques NumPy et pandas pour sélectionner
des lignes et des colonnes de tableaux (cf. chap. 38 et 39).
"""
