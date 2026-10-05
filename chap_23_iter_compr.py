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
#  Chap. 23     #  Itérables & compréhensions                                  #
#               #                                                              #
################################################################################
#
#  - Les itérables
#  - Bonus : comment fonctionne "for" ?
#  - Compréhensions sur des listes
#  - Conditions sur les compréhensions
#  - Compréhensions sur des matrices
#  - Compréhensions chaînées
#  - Compréhensions avancées
#  - Quand (ne pas) utiliser une compréhension ?
#
###########################################

"""
Ce fichier utilise un fichier "exemple.txt". Pour que le chapitre soit
exécutable tel quel, on commence par créer ce fichier ; il sera supprimé à la
fin du chapitre. Ne vous souciez pas pour l'instant du code ci-dessous : la
gestion des fichiers sera détaillée au chap. 28.
"""
with open("exemple.txt", "w") as fichier:
    fichier.write("aaaa\nbbbbbb\ncccc\ndddddd\neeeeeeeeeeeeeee\nfffff\n"
                  "gg gg gg\nhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\niiiii\n")


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

#   5. L'objet retourné par range() (cf. chap. 13) est lui aussi un itérable.
#      Il ne "contient" pas réellement ses nombres : il les fabrique un par
#      un, au fur et à mesure du parcours. C'est pourquoi range(1_000_000_000)
#      ne prend presque pas de place en mémoire.
for i in range(3):
    print(i)
"""
0
1
2
"""

#   6. Les ensembles (sets, cf. chap. 25) sont des itérables, mais l'ordre de
#      parcours n'y est pas garanti.

"""
    7. Enfin, un descripteur de fichier ("file descriptor") retourné par open()
       est aussi un itérable : on le parcourt LIGNE PAR LIGNE.
       Voici le contenu du fichier "exemple.txt" créé plus haut :
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
    # fin de ligne (chaque ligne lue contient déjà son propre "\n", cf. chap. 7)
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

Note : en toute rigueur il faudrait aussi fermer le fichier ; on verra au
chap. 28 la bonne façon de faire, avec "with open(…) as …".
"""

"""
On peut utiliser la syntaxe "… in …" avec tous les itérables. "in" retourne
True si l'élément est dans l'itérable, et False sinon.
"""
print(1 in [1, 2, 3])  # => True
print("p" in "pouet")  # => True
print("r" in "pouet")  # => False
print(0 in d)          # => True (pour un dictionnaire, "in" teste les CLÉS)
print("zéro" in d)     # => False ("zéro" est une valeur, pas une clé)
print(7 in range(10))  # => True

# Avec une string, "in" cherche même des sous-chaînes entières :
print("oue" in "pouet")  # => True

# Avec un fichier, "in" cherche parmi les lignes (avec leur "\n" final !) :
print("cccc\n" in open("exemple.txt"))  # => True
print("cccc" in open("exemple.txt"))    # => False, à cause du "\n" manquant

"""
Cette syntaxe offre la même garantie que "for" : chaque élément sera parcouru
au plus UNE FOIS (le parcours s'arrête dès que l'élément est trouvé).

IMPT : de nombreuses fonctions intégrées acceptent N'IMPORTE QUEL itérable en
argument, et pas seulement des listes : list(), tuple(), set(), sum(), min(),
max(), sorted(), len() (pour la plupart), etc.
"""
print(list("abc"))       # => ['a', 'b', 'c']
print(tuple(range(4)))   # => (0, 1, 2, 3)
print(sum(range(101)))   # => 5050
print(max("pouet"))      # => u (le caractère le plus "grand", cf. chap. 8)
print(list(d))           # => [0, 1] (les clés du dictionnaire)


# Bonus : comment fonctionne "for" ?
#####################################

"""
Ce paragraphe n'est pas indispensable, mais il explique ce qui se passe
"sous le capot" d'une boucle for.

Pour parcourir un itérable, Python lui demande d'abord un "itérateur" avec la
fonction intégrée iter(). Un itérateur est un objet qui se souvient de l'endroit
où l'on en est dans le parcours. On lui demande l'élément suivant avec la
fonction intégrée next().
"""
iterateur = iter(["a", "b", "c"])
print(next(iterateur))  # => a
print(next(iterateur))  # => b
print(next(iterateur))  # => c

# Quand il n'y a plus d'éléments, next() soulève l'erreur StopIteration…
try:
    next(iterateur)
except StopIteration as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err!r})")

"""
… et c'est précisément cette erreur que "for" intercepte pour savoir quand
s'arrêter ! La boucle :

for x in ["a", "b", "c"]:
    print(x)

est donc équivalente à :
"""
iterateur = iter(["a", "b", "c"])
while True:
    try:
        x = next(iterateur)
    except StopIteration:
        break
    print(x)
"""
a
b
c

(La gestion des erreurs avec try … except sera détaillée au chap. 26.)

Conséquence importante : un itérateur ne se parcourt qu'UNE SEULE FOIS. Une
fois épuisé, il est vide.
"""
iterateur = iter([1, 2, 3])
print(list(iterateur))  # => [1, 2, 3]
print(list(iterateur))  # => [] : l'itérateur est déjà épuisé !

# Un fichier ouvert est lui-même un itérateur : une fois lu jusqu'au bout,
# un nouveau parcours ne donne plus rien.
fo = open("exemple.txt")
print(len(list(fo)))  # => 9 (le fichier a 9 lignes)
print(len(list(fo)))  # => 0 (on est déjà à la fin du fichier)
fo.close()


# Compréhensions sur des listes
################################

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
Explication : on va appliquer l'expression de gauche "2 * x" à chaque élément
de la liste l1, et obtenir une NOUVELLE liste contenant les résultats. La liste
l1 n'est pas modifiée.

Lisez la compréhension "à l'anglaise" : "2 fois x, pour chaque x dans l1".

Note : le nom de la variable (ici x) est libre, et elle n'existe qu'à
l'intérieur de la compréhension.
"""
print(l1)  # => [0, 1, 2, 3, 4, 5], inchangée

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

#   - Convertir une liste de strings en entiers (très utile après un input()
#     ou la lecture d'un fichier, cf. chap. 11 et 28) :
saisies = ["12", "7", "42"]
nombres = [int(s) for s in saisies]
print(nombres)       # => [12, 7, 42]
print(sum(nombres))  # => 61

#   - Appeler une fonction sur chaque élément :
def carre(x):
    return x ** 2


print([carre(n) for n in range(1, 6)])  # => [1, 4, 9, 16, 25]

#   - Lire les lignes d'un fichier en retirant le "\n" final de chacune :
lignes = [ligne.strip() for ligne in open("exemple.txt")]
print(lignes[:3])  # => ['aaaa', 'bbbbbb', 'cccc'] (pour [:3], cf. chap. 31)

"""
Les compréhensions sont un outil très puissant et parfois assez complexe
à visualiser… il est donc recommandé de beaucoup s'entraîner !

Note : les compréhensions sont un raccourci pour créer une liste rapidement,
mais on pourra toujours générer la même liste avec une boucle.

Ainsi ces deux constructions sont équivalentes :
"""
l_iter = []
for i in range(10):
    l_iter.append(2 * i + 3)

l_comp = [2 * i + 3 for i in range(10)]
print(l_iter == l_comp)  # => True

"""
IMPT : pour "traduire" une boucle en compréhension :
    1. on part de la liste vide [],
    2. on y met d'abord ce qui était dans .append(…),
    3. puis la ligne "for … in …" (sans les ":").
"""


# Conditions sur les compréhensions
####################################

"""
Si on veut conserver uniquement certaines valeurs de l'itérable, on ajoutera
une condition "if" à la fin de la compréhension :

[ <expression> for <variable> in <itérable> if <expression booléenne> ]

La condition sera testée avec chaque valeur de l'itérable : seules les valeurs
pour lesquelles elle vaut True seront conservées (c'est un "filtre").
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

#   - Combiner filtre et transformation : les carrés des nombres impairs
print([x ** 2 for x in range(10) if x % 2 == 1])  # => [1, 9, 25, 49, 81]

#   - Garder les voyelles d'un mot :
print([c for c in "anticonstitutionnellement" if c in "aeiouy"])
# => ['a', 'i', 'o', 'i', 'u', 'i', 'o', 'e', 'e', 'e']

# La boucle équivalente à une compréhension avec condition :
l7_boucle = []
for i in l6:
    if i % 2 == 0:
        l7_boucle.append(i)
print(l7_boucle == l7)  # => True

"""
Attention à ne pas confondre avec le "if … else …" sur une ligne vu au
chap. 12, qui se place À GAUCHE, dans l'expression :

[ <valeur si vrai> if <condition> else <valeur si faux> for <var> in <itérable> ]

Ici on ne filtre rien : on garde TOUS les éléments, mais on choisit quoi
mettre dans la nouvelle liste.
"""
print(["pair" if i % 2 == 0 else "impair" for i in range(4)])
# => ['pair', 'impair', 'pair', 'impair']

# On peut d'ailleurs combiner les deux (attention à la lisibilité !)
print([0 if i < 0 else i for i in [-2, 5, -1, 3] if i != 3])  # => [0, 5, 0]

"""
Résumé :
    - "if" seul, À DROITE  : filtre (la nouvelle liste peut être plus courte)
    - "if … else …", À GAUCHE : transformation (même longueur que l'itérable)
    - "else" seul à droite n'existe pas :
      [x for x in l if x > 0 else 0] est une SyntaxError.
"""


# Compréhensions sur des matrices
##################################

"""
Il est possible de construire des compréhensions imbriquées avec des listes de
listes (aussi appelées matrices, cf. chap. 24).
"""

# Exemple avec une matrice 3 * 3 :
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
On peut ensuite utiliser la syntaxe [… for …] sur cette matrice : chaque
élément parcouru (row) est alors une ligne, c'est-à-dire une liste.
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

#   - Pour obtenir la somme de chaque ligne :
print([sum(row) for row in matrice])  # => [6, 15, 24]

#   - Pour obtenir la matrice suivante :
#     [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
m4 = [[3 * i + j for j in range(3)] for i in range(5)]
print(m4)  # => [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
"""
Ici, on a une compréhension DANS une compréhension : pour chaque i (chaque
ligne), la compréhension intérieure fabrique une liste de 3 valeurs (j varie
de 0 à 2).
"""

#   - Pour conserver seulement les valeurs en diagonale :
m5 = [matrice[i][i] for i in range(len(matrice))]
print(m5)  # => [1, 5, 9]

#   - Pour multiplier tous les éléments de la matrice par 10 (on garde la
#     forme de la matrice) :
print([[10 * x for x in row] for row in matrice])
# => [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

#   - Pour "transposer" la matrice (les lignes deviennent les colonnes) :
transposee = [[row[j] for row in matrice] for j in range(3)]
print(transposee)  # => [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# Compréhensions chaînées
##########################

"""
Il est à noter que l'on peut "chaîner" les compréhensions, càd avoir des
itérations sur deux variables en même temps dans la même compréhension
(attention, noeuds au cerveau possibles).

Toutes les possibilités seront alors parcourues : si l'on a une itération sur
5 valeurs, puis sur 4 valeurs, la partie à gauche sera évaluée 20 fois.
"""
double = [x + y for x in "abc" for y in "lmn"]
print(double)  # => ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
# Ceci permet de trouver rapidement toutes les combinaisons entre deux itérables

"""
IMPT : les "for" se lisent DANS LE MÊME ORDRE que des boucles imbriquées. La
compréhension ci-dessus équivaut à :
"""
double_boucle = []
for x in "abc":          # boucle extérieure (le 1er "for")
    for y in "lmn":      # boucle intérieure (le 2e "for")
        double_boucle.append(x + y)
print(double_boucle == double)  # => True

"""
Ne pas confondre les for chaînés (une seule paire de crochets, résultat
"plat") avec les compréhensions imbriquées vues plus haut (crochets dans des
crochets, résultat sous forme de matrice) :
"""
tableau = [[i + 2 * j for j in range(4)] for i in range(4)]
print(tableau)  # => voir ci-dessous
# [
#     [0, 2, 4, 6],
#     [1, 3, 5, 7],
#     [2, 4, 6, 8],
#     [3, 5, 7, 9]
# ]

# Les for chaînés permettent par exemple d'"aplatir" une matrice :
print([x for row in matrice for x in row])  # => [1, 2, 3, 4, 5, 6, 7, 8, 9]

# On peut bien sûr ajouter une condition
super_comprehension = [(a, b) for a in range(3) for b in range(3) if a > b]
print(super_comprehension)  # => [(1, 0), (2, 0), (2, 1)]


# Compréhensions avancées
##########################

"""
Les compréhensions ne servent pas qu'à créer des listes : la même syntaxe
permet de créer des dictionnaires, des ensembles, et même des "générateurs".
"""

#   1. Il est possible de partir des clés d'un dictionnaire…
poids_voitures = {"clio": 790, "406": 1230, "X5": 2170}

# …pour créer une liste à partir de ce dictionnaire ([::-1] retourne la chaîne
# à l'envers, cf. chap. 31)
print([v[::-1] for v in poids_voitures])  # => ['oilc', '604', '5X']

#   2. Compréhensions de dictionnaire : on peut aussi créer un nouveau
#      dictionnaire avec la syntaxe { <clé>: <valeur> for … in … }
#      (notez le ".items()" à droite, qui donne les couples clé/valeur,
#      cf. chap. 27)
print({key * 2: value / 10 for (key, value) in poids_voitures.items()})
# => {'clioclio': 79.0, '406406': 123.0, 'X5X5': 217.0}

# Exemple : associer chaque mot à sa longueur
print({mot: len(mot) for mot in ["chat", "chien", "hippopotame"]})
# => {'chat': 4, 'chien': 5, 'hippopotame': 11}

# Exemple : ne garder que les voitures de moins d'une tonne
print({k: v for k, v in poids_voitures.items() if v < 1000})  # => {'clio': 790}

# Exemple : inverser clés et valeurs
print({v: k for k, v in poids_voitures.items()})
# => {790: 'clio', 1230: '406', 2170: 'X5'}

#   3. Compréhensions d'ensemble (cf. chap. 25) : mêmes accolades, mais sans
#      le ":". Les doublons disparaissent.
#      (L'ordre d'affichage d'un ensemble n'est pas garanti.)
print({len(mot) for mot in ["un", "deux", "trois", "quatre", "six"]})
# => {2, 3, 4, 5, 6} (ordre non garanti)

#   4. Expressions génératrices : avec des parenthèses au lieu des crochets,
#      on n'obtient PAS un tuple, mais un "générateur" : un itérateur qui
#      calcule ses valeurs une à une, à la demande, sans créer de liste.
gen = (x ** 2 for x in range(5))
print(type(gen))  # => <class 'generator'>
print(list(gen))  # => [0, 1, 4, 9, 16]
print(list(gen))  # => [] : comme tout itérateur, il est maintenant épuisé

# C'est très pratique avec sum(), max(), any(), all() (cf. chap. 21)… : on
# peut même omettre les parenthèses quand le générateur est le seul argument.
print(sum(x ** 2 for x in range(5)))      # => 30
print(max(len(f) for f in fruits))        # => 6
print(sum(1 for c in "pouet" if c in "aeiouy"))  # => 3 (nombre de voyelles)

"""
Intérêt : sum(x for x in range(10_000_000)) ne crée jamais une liste de
10 millions d'éléments en mémoire, contrairement à
sum([x for x in range(10_000_000)]).

Note : il n'y a pas de "compréhension de tuple". Pour obtenir un tuple, on
passe une expression génératrice à tuple() :
"""
print(tuple(x * 2 for x in range(3)))  # => (0, 2, 4)


# Quand (ne pas) utiliser une compréhension ?
##############################################

"""
Une compréhension est idéale quand on veut CONSTRUIRE UNE NOUVELLE COLLECTION
à partir d'un itérable, en une ligne lisible.

On préférera une boucle "for" classique :
    - quand le traitement est long ou demande plusieurs étapes,
    - quand on ne veut pas créer de collection mais seulement produire un
      effet (afficher, écrire dans un fichier, modifier une autre variable…).
      Écrire [print(x) for x in l] fonctionne, mais crée une liste inutile de
      None : c'est une mauvaise pratique !
    - quand la compréhension devient illisible (plus de deux "for", ou des
      conditions compliquées).

Règle d'or : si vous devez relire trois fois une compréhension pour la
comprendre, réécrivez-la avec une boucle.
"""

# Nettoyage : on supprime le fichier créé au début du chapitre (le module os
# a été présenté au chap. 22, la suppression de fichiers est vue au chap. 28)
import os
os.remove("exemple.txt")
