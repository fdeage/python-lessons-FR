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
#  Chap. 24     #  Types construits I : les listes (II)                        #
#               #                                                              #
################################################################################
#
#  - Fonctions intégrées
#  - Autres façons de créer une liste
#  - Parcourir une liste
#  - Matrices
#  - Tri de listes
#  - D'autres méthodes sur les listes
#  - Bonus sur les listes
#
###########################################

# Fonctions intégrées
######################

"""
IMPT : Python propose des fonctions intégrées pour des listes numériques (càd
constituées d'ints ou de floats uniquement) :
    - len() retourne le nombre d'éléments de la liste
    - max() et min() retournent la plus haute et la plus basse valeur
    - sum() retourne la somme de toutes les valeurs de la liste
"""
# Rappel : list(range(5)) crée la liste des entiers de 0 à 4 (cf. chap. 13 et
# plus bas)
liste_entiers_croissants = list(range(5))
print(liste_entiers_croissants)      # => [0, 1, 2, 3, 4]

print(len(liste_entiers_croissants)) # => 5
print(max(liste_entiers_croissants)) # => 4
print(min(liste_entiers_croissants)) # => 0
print(sum(liste_entiers_croissants)) # => 10

# Ainsi, pour calculer la moyenne des notes suivantes…
notes = [17, 12, 14, 9, 19, 11, 14, 14]
# …il suffira de faire :
moyenne = sum(notes) / len(notes)
print(f"Ma moyenne est de {moyenne}")  # => Ma moyenne est de 13.75

# La liste vide a une longueur de 0
print(len([]))  # => 0

# … et sa somme vaut 0, mais max() et min() n'ont pas de sens sur une liste
# vide : ils soulèvent une erreur.
print(sum([]))  # => 0
try:
    max([])
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Note : len(), max() et min() fonctionnent aussi sur des listes de strings
(l'ordre utilisé est alors l'ordre "alphabétique" des codes des caractères,
cf. chap. 8). En revanche, sum() ne fonctionne qu'avec des nombres, et aucune
de ces fonctions n'accepte un mélange de nombres et de strings.
"""
print(max(["pomme", "banane", "kiwi"]))  # => pomme
print(min(["pomme", "banane", "kiwi"]))  # => banane
try:
    sum(["a", "b"])
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    max([1, "a"])
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
IMPT : la fonction intégrée enumerate()

Si l'on souhaite itérer sur les valeurs d'une liste tout en conservant leur
rang, on doit normalement utiliser "range(len(l))" :

Exemple :
"""
l = ["a", "b", "c"]

for i in range(len(l)):    # moche
    print(f"{i} : {l[i]}")

# Avec enumerate(), tout se fait en une ligne :
for i, j in enumerate(l):  # beau
    print(f"{i} : {j}")

"""
Les deux boucles for ci-dessus imprimeront :

0 : a
1 : b
2 : c

Explication : enumerate(l) fournit, à chaque tour de boucle, un tuple
(indice, valeur). Ce tuple est "déballé" dans les deux variables i et j,
exactement comme pour l'affectation multiple (cf. chap. 10 et 17).
"""
print(list(enumerate(l)))  # => [(0, 'a'), (1, 'b'), (2, 'c')]

# On peut faire commencer la numérotation à une autre valeur que 0 :
for rang, lettre in enumerate(l, start=1):
    print(f"{rang}. {lettre}")
"""
1. a
2. b
3. c
"""

"""
IMPT : la fonction intégrée zip()

zip() permet de parcourir plusieurs listes EN MÊME TEMPS, élément par élément
(comme une fermeture éclair, "zip" en anglais, qui associe les dents deux à
deux).
"""
prenoms = ["Ada", "Alan", "Grace"]
ages = [36, 41, 85]
for prenom, age in zip(prenoms, ages):
    print(f"{prenom} a {age} ans")
"""
Ada a 36 ans
Alan a 41 ans
Grace a 85 ans
"""
print(list(zip(prenoms, ages)))  # => [('Ada', 36), ('Alan', 41), ('Grace', 85)]

# Attention : zip() s'arrête à la fin de la liste la PLUS COURTE, sans erreur.
print(list(zip([1, 2, 3], ["a", "b"])))  # => [(1, 'a'), (2, 'b')]

# Astuce : zip() + dict() permet de créer un dictionnaire à partir de deux
# listes (cf. chap. 27)
print(dict(zip(prenoms, ages)))  # => {'Ada': 36, 'Alan': 41, 'Grace': 85}


# Autres façons de créer une liste
###################################

# Pour déclarer une liste d'éléments identiques, on utilise l'opérateur "*"
print(["a"] * 4)  # => ['a', 'a', 'a', 'a']
print([0] * 5)    # => [0, 0, 0, 0, 0] (pratique pour initialiser des compteurs)
print([1, 2] * 3) # => [1, 2, 1, 2, 1, 2]

# On peut appliquer la fonction intégrée list() sur un itérable (cf. chap. 23) :
#   - avec un argument range() pour déclarer une liste d'entiers croissants
liste_entiers_croissants = list(range(5))  # => [0, 1, 2, 3, 4]
print(list(range(2, 11, 2)))               # => [2, 4, 6, 8, 10]

#   - avec un argument de type string
liste_caracteres = list("une string")
print(liste_caracteres)
# => ['u', 'n', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']

#   - avec un tuple (cf. chap. 17)
print(list((1, 2, 3)))  # => [1, 2, 3]

#   - avec un dictionnaire : on obtient la liste de ses CLÉS (cf. chap. 27)
print(list({"a": 1, "b": 2}))  # => ['a', 'b']

#   - à partir d'une string, avec la méthode .split() (cf. chap. 8)
print("le chat dort".split())  # => ['le', 'chat', 'dort']

#   - enfin, avec une compréhension de liste (cf. chap. 23)
print([x * x for x in range(5)])  # => [0, 1, 4, 9, 16]


# Parcourir une liste
######################

"""
    Il y a deux approches pour réaliser un parcours de liste Python :

    1. itération sur les indices : on commence par énumérer l'ensemble des
       indices (càd les positions des éléments) :
"""
liste = [2, 4, 6, 8]
print(liste)  # => [2, 4, 6, 8]

for i in range(len(liste)):
    print(i)
"""
Ceci imprimera les indices des valeurs :
0
1
2
3

On accède ensuite à la valeur avec liste[i].

    2. itération sur les valeurs : on parcourt directement l'ensemble des
       éléments de la liste :
"""
for valeur in liste:
    print(valeur)
"""
Ceci imprimera les valeurs elles-mêmes :
2
4
6
8
"""

# Les deux boucles suivantes font donc la même chose :
for i in range(len(liste)):
    print(liste[i])

for valeur in liste:
    print(valeur)

"""
Dans quel cas utiliser 1 ou 2 ?

    - IMPT : par défaut, on utilise la méthode 2 (sur les valeurs) : elle est
      plus lisible et évite les erreurs d'indice (IndexError).

    - Si l'on a besoin à la fois de l'indice ET de la valeur, on utilise
      enumerate() (voir plus haut) plutôt que range(len(…)).

    - La méthode 1 (sur les indices) reste utile :
        a) quand on veut MODIFIER la liste sur place : modifier la variable
           de boucle "valeur" ne change pas la liste !
        b) quand on a besoin de comparer un élément avec son voisin
           (liste[i] et liste[i + 1]),
        c) quand on parcourt plusieurs listes de même longueur (même si zip()
           est souvent plus élégant).
"""

#   a) Modifier la liste : avec les valeurs, ça ne marche pas…
for valeur in liste:
    valeur = valeur * 10   # on modifie seulement la variable "valeur"
print(liste)  # => [2, 4, 6, 8], inchangée !

# … mais avec les indices, si :
for i in range(len(liste)):
    liste[i] = liste[i] * 10
print(liste)  # => [20, 40, 60, 80]

#   b) Comparer chaque élément avec le suivant (attention à s'arrêter un cran
#      avant la fin pour ne pas dépasser l'indice maximal !)
temperatures = [12, 15, 14, 18, 21]
for i in range(len(temperatures) - 1):
    ecart = temperatures[i + 1] - temperatures[i]
    # (":+" dans l'interpolation affiche toujours le signe, même pour un nombre
    # positif)
    print(f"Du jour {i} au jour {i + 1} : {ecart:+}°C")
"""
Du jour 0 au jour 1 : +3°C
Du jour 1 au jour 2 : -1°C
Du jour 2 au jour 3 : +4°C
Du jour 3 au jour 4 : +3°C
"""

"""
On peut aussi parcourir une liste "à l'envers" avec la fonction intégrée
reversed(), qui ne modifie pas la liste :
"""
for valeur in reversed([1, 2, 3]):
    print(valeur)
"""
3
2
1
"""

"""
Enfin, on peut parcourir une liste avec une boucle while : c'est utile
quand on ne sait pas à l'avance quand s'arrêter.
"""
# Exemple : chercher le premier nombre négatif
mesures = [3, 7, -2, 5, -8]
i = 0
while i < len(mesures) and mesures[i] >= 0:
    i += 1
print(f"Premier négatif à l'indice {i}")  # => Premier négatif à l'indice 2

"""
Attention : il ne faut JAMAIS ajouter ou supprimer des éléments d'une liste
pendant qu'on la parcourt avec "for" : certains éléments seraient sautés.
"""
nombres = [1, 2, 2, 3]
for n in nombres:
    if n == 2:
        nombres.remove(n)   # mauvaise idée !
print(nombres)  # => [1, 2, 3] : un des "2" a été sauté !

# Solution : construire une nouvelle liste (par exemple avec une compréhension)
nombres = [1, 2, 2, 3]
nombres = [n for n in nombres if n != 2]
print(nombres)  # => [1, 3]


# Matrices
###########

# On peut déclarer un tableau à deux dimensions (ou matrice) avec des
# listes dans une liste
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrice[0])     # => [1, 2, 3] (la première ligne)
print(matrice[1][2])  # => 6 (ligne 1, colonne 2)
print(matrice[2][0])  # => 7

"""
Lire matrice[1][2] de gauche à droite :
    - matrice[1] est la ligne d'indice 1, c'est-à-dire [4, 5, 6],
    - puis [2] prend l'élément d'indice 2 de cette ligne : 6.
"""

# Pour avoir les dimensions de la matrice, on va utiliser len()
print(len(matrice))     # => 3, la "hauteur" de la matrice (son nombre de lignes)
print(len(matrice[0]))  # => 3, la "largeur" de la première ligne (le nombre de
# colonnes).

"""
On supposera que la largeur de la première ligne sera identique aux largeurs
des autres lignes.
"""

# On modifie un élément comme dans une liste simple :
matrice[1][1] = 0
print(matrice)  # => [[1, 2, 3], [4, 0, 6], [7, 8, 9]]

# Pour parcourir tous les éléments, on imbrique deux boucles for :
for ligne in matrice:
    for element in ligne:
        print(element, end=" ")
    print()  # saut de ligne à la fin de chaque ligne de la matrice
"""
1 2 3
4 0 6
7 8 9
"""

# Avec les indices, si l'on a besoin de connaître la position de chaque case :
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        if matrice[i][j] == 0:
            print(f"Case vide en ligne {i}, colonne {j}")
# => Case vide en ligne 1, colonne 1

"""
Note : il n'y a pas de limites au niveau d'imbrication que l'on peut atteindre !
Voici par exemple une très belle matrice 3D…
"""
liste_3d = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
print(liste_3d[1][0][1])  # => 5
# …mais en pratique on ira rarement au-delà de 2. Pour du calcul sur de grandes
# matrices, on utilisera plutôt la bibliothèque numpy (cf. chap. 38).

"""
IMPT : piège classique ! Pour créer une matrice remplie de 0, on pourrait être
tenté d'écrire [[0] * 3] * 3… mais les 3 lignes sont alors LA MÊME liste
(elles ont la même adresse mémoire, cf. chap. 19) :
"""
piege = [[0] * 3] * 3
piege[0][0] = 1
print(piege)  # => [[1, 0, 0], [1, 0, 0], [1, 0, 0]] : les 3 lignes ont changé !

# La bonne façon : une compréhension, qui crée une NOUVELLE liste par ligne
correct = [[0] * 3 for _ in range(3)]
correct[0][0] = 1
print(correct)  # => [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
# (Le nom de variable "_" signifie par convention "variable inutilisée".)


# Tri de listes
################

"""
On a deux options ici :
    1. trier la liste "en place" avec la méthode .sort()
    2. retourner une nouvelle valeur qui contient la liste triée avec sorted()
"""

#   1. On utilise .sort() pour trier une liste "sur place", sans rien retourner…
desordre = [2, 3, 7, 1, 9, 4]
s = desordre.sort()
print(s)         # => None. .sort() ne retourne rien !
print(desordre)  # => [1, 2, 3, 4, 7, 9], la liste de départ est modifiée

#   2. … et on utilise sorted() pour retourner une liste triée sans changer
# l'original
desordre2 = [2, 3, 7, 1, 9, 4]
print(sorted(desordre2))  # => [1, 2, 3, 4, 7, 9]
print(desordre2)  # => [2, 3, 7, 1, 9, 4], la liste de départ n'est pas modifiée

"""
IMPT : erreur fréquente, écrire l = l.sort() : comme .sort() retourne None,
on perd sa liste !

Note : sorted() accepte n'importe quel itérable (string, tuple, set,
dictionnaire…) et retourne toujours une LISTE.
"""
print(sorted("python"))     # => ['h', 'n', 'o', 'p', 't', 'y']
print(sorted((3, 1, 2)))    # => [1, 2, 3]

# Note : on inverse une liste sur place avec .reverse()
desordre.reverse()
print(desordre)  # => [9, 7, 4, 3, 2, 1]

# Pour trier dans l'ordre décroissant, on utilise le paramètre reverse=True
# (il fonctionne avec .sort() comme avec sorted())
print(sorted(desordre2, reverse=True))  # => [9, 7, 4, 3, 2, 1]

"""
Les strings sont triées selon l'ordre des codes de caractères (cf. chap. 8) :
les majuscules passent AVANT les minuscules, et les lettres accentuées APRÈS.
"""
print(sorted(["banane", "Pomme", "abricot", "école"]))
# => ['Pomme', 'abricot', 'banane', 'école']

"""
Pour choisir le critère de tri, on passe une fonction au paramètre "key" :
Python appelle cette fonction sur chaque élément, et trie selon les valeurs
retournées. (On passe la fonction elle-même, SANS parenthèses, cf. chap. 15
sur l'adresse d'une fonction.)
"""
mots = ["kiwi", "ananas", "fraise", "noix"]
print(sorted(mots, key=len))  # => ['kiwi', 'noix', 'ananas', 'fraise']
# Note : en cas d'égalité, l'ordre de départ est conservé (on dit que le tri
# est "stable") : kiwi reste avant noix.
# On verra au chap. 32 comment écrire ces petites fonctions sur place, avec
# le mot-clé lambda.

# Avec une fonction définie par l'utilisateur :
def derniere_lettre(mot):
    return mot[-1]


print(sorted(mots, key=derniere_lettre))  # => ['fraise', 'kiwi', 'ananas', 'noix']

# Trier des strings sans tenir compte des majuscules :
print(sorted(["banane", "Pomme", "abricot"], key=str.lower))
# => ['abricot', 'banane', 'Pomme']

# Trier des tuples : Python compare d'abord le 1er élément, puis le 2e en cas
# d'égalité, etc.
eleves = [("Zoé", 14), ("Adam", 17), ("Léa", 14)]
print(sorted(eleves))  # => [('Adam', 17), ('Léa', 14), ('Zoé', 14)]

# Pour trier les élèves par note :
def note(eleve):
    return eleve[1]


print(sorted(eleves, key=note, reverse=True))
# => [('Adam', 17), ('Zoé', 14), ('Léa', 14)]

# On ne peut pas trier une liste qui mélange des types non comparables :
try:
    sorted([3, "a", 1])
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")


# D'autres méthodes sur les listes
###################################

"""
On a déjà vu .append(), .pop(), .extend() (chap. 16), .sort() et .reverse().
Voici les autres méthodes utiles. Attention à bien distinguer les méthodes
qui MODIFIENT la liste (et retournent None) de celles qui retournent une
information sans la modifier.
"""
fruits = ["pomme", "kiwi", "banane", "kiwi"]

#   1. .insert(<indice>, <valeur>) insère une valeur à l'indice donné ; les
#      éléments suivants sont décalés vers la droite.
fruits.insert(1, "cerise")
print(fruits)  # => ['pomme', 'cerise', 'kiwi', 'banane', 'kiwi']
fruits.insert(0, "abricot")  # insertion au début
print(fruits)  # => ['abricot', 'pomme', 'cerise', 'kiwi', 'banane', 'kiwi']

#   2. .remove(<valeur>) supprime la PREMIÈRE occurrence d'une valeur (à
#      la différence de del et .pop() qui travaillent avec un indice)
fruits.remove("kiwi")
print(fruits)  # => ['abricot', 'pomme', 'cerise', 'banane', 'kiwi']

# Si la valeur n'existe pas, .remove() soulève une ValueError :
try:
    fruits.remove("mangue")
except ValueError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

#   3. .pop(<indice>) supprime ET retourne l'élément à l'indice donné
#      (sans argument, c'est le dernier, cf. chap. 16)
premier = fruits.pop(0)
print(premier)  # => abricot
print(fruits)   # => ['pomme', 'cerise', 'banane', 'kiwi']

#   4. .index(<valeur>) retourne l'indice de la première occurrence
print(fruits.index("banane"))  # => 2
try:
    fruits.index("mangue")
except ValueError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")

# Pour éviter cette erreur, on vérifie d'abord avec "in" :
if "mangue" in fruits:
    print(fruits.index("mangue"))
else:
    print("Pas de mangue")  # => Pas de mangue

#   5. .count(<valeur>) compte le nombre d'occurrences d'une valeur
lancers = [6, 2, 6, 3, 6, 1]
print(lancers.count(6))  # => 3
print(lancers.count(5))  # => 0

#   6. .copy() retourne une copie de la liste (voir le bonus plus bas)
copie = fruits.copy()
print(copie)  # => ['pomme', 'cerise', 'banane', 'kiwi']

#   7. .clear() vide la liste
copie.clear()
print(copie)   # => []
print(fruits)  # => ['pomme', 'cerise', 'banane', 'kiwi'] (l'original est intact)

"""
Résumé :

| méthode             | modifie la liste ? | retourne            |
| ------------------- | ------------------ | ------------------- |
| .append(x)          | oui                | None                |
| .extend(iterable)   | oui                | None                |
| .insert(i, x)       | oui                | None                |
| .remove(x)          | oui                | None                |
| .pop() / .pop(i)    | oui                | l'élément supprimé  |
| .clear()            | oui                | None                |
| .sort()             | oui                | None                |
| .reverse()          | oui                | None                |
| .index(x)           | non                | un indice (int)     |
| .count(x)           | non                | un nombre (int)     |
| .copy()             | non                | une nouvelle liste  |
"""


# Bonus sur les listes
#######################

"""
1. Copier une liste : "=" ne copie PAS !

L'affectation b = a ne crée pas une nouvelle liste : a et b désignent la MÊME
liste en mémoire (cf. chap. 19). Modifier l'une modifie donc "l'autre".
"""
a = [1, 2, 3]
b = a
b.append(4)
print(a)       # => [1, 2, 3, 4] : a aussi a été modifiée !
print(a is b)  # => True ("is" teste si c'est le même objet en mémoire)

# Pour obtenir une vraie copie indépendante :
c = a.copy()   # ou list(a), ou a[:] (cf. chap. 31)
c.append(5)
print(a)       # => [1, 2, 3, 4], inchangée
print(c)       # => [1, 2, 3, 4, 5]
print(a is c)  # => False
print(a == c[:4])  # => True ("==" compare les valeurs, pas l'adresse)

"""
Attention : .copy() fait une copie "superficielle" ("shallow copy") : pour une
matrice, les lignes elles-mêmes ne sont pas copiées. Pour copier entièrement
une liste de listes, on utilisera la fonction deepcopy() du module copy
(cf. chap. 22).
"""
import copy

m = [[1, 2], [3, 4]]
superficielle = m.copy()
profonde = copy.deepcopy(m)
m[0][0] = 99
print(superficielle)  # => [[99, 2], [3, 4]] : la ligne est partagée !
print(profonde)       # => [[1, 2], [3, 4]] : vraiment indépendante

"""
2. Les listes en paramètre de fonction

Comme une liste est mutable, une fonction qui modifie une liste passée en
argument modifie la liste de l'appelant (c'est un "effet de bord", cf.
chap. 29).
"""
def ajoute_zero(une_liste):
    une_liste.append(0)


ma_liste = [1, 2]
ajoute_zero(ma_liste)
print(ma_liste)  # => [1, 2, 0]

"""
3. Comparer des listes

"==" compare les listes élément par élément. "<" et ">" les comparent comme
des mots dans le dictionnaire (ordre "lexicographique") : on compare les
premiers éléments, puis les seconds en cas d'égalité, etc.
"""
print([1, 2, 3] == [1, 2, 3])  # => True
print([1, 2, 3] == [3, 2, 1])  # => False (l'ordre compte !)
print([1, 2, 3] < [1, 3])      # => True (car 2 < 3)
print([1, 2] < [1, 2, 0])      # => True (le préfixe est "plus petit")

"""
4. Déballage ("unpacking") d'une liste

Comme pour les tuples (cf. chap. 17), on peut affecter chaque élément d'une
liste à une variable. Avec "*", une variable récupère "tout le reste" sous
forme de liste.
"""
x, y, z = [10, 20, 30]
print(x, y, z)  # => 10 20 30

premier, *reste = [1, 2, 3, 4]
print(premier)  # => 1
print(reste)    # => [2, 3, 4]

*debut, dernier = [1, 2, 3, 4]
print(debut, dernier)  # => [1, 2, 3] 4

# "*" permet aussi de passer les éléments d'une liste comme arguments séparés :
print(*[1, 2, 3])           # => 1 2 3 (équivaut à print(1, 2, 3))
print(*["a", "b"], sep="-") # => a-b

"""
5. Transformer une liste en string avec .join()

C'est l'opération inverse de .split() (cf. chap. 8) : on "colle" les
éléments d'une liste de strings avec un séparateur.
"""
print(" ".join(["le", "chat", "dort"]))  # => le chat dort
print(", ".join(["a", "b", "c"]))        # => a, b, c

# Attention, .join() n'accepte que des strings : on convertit d'abord
try:
    "-".join([1, 2, 3])
except TypeError as err:
    print(f"7: (Sans ce try: … except …, cette ligne créerait : {err})")
print("-".join([str(n) for n in [1, 2, 3]]))  # => 1-2-3
