################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Claude Opus 5.5 - 2026                #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 38     #  NumPy                                                       #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Installer et importer NumPy
#  - Pourquoi NumPy ? Listes contre tableaux
#  - Créer des tableaux
#  - Les attributs d'un tableau : dtype, shape, ndim, size
#  - Indexation et slices
#  - Vues et copies
#  - Opérations vectorisées
#  - Le broadcasting
#  - Masques booléens et filtrage
#  - Fonctions d'agrégation et paramètre axis
#  - Changer la forme : reshape, transposition, concaténation
#  - Les valeurs manquantes : NaN
#  - Cas pratique : un relevé de températures
#  - Et ensuite ?
#
##############################

# Introduction
###############

"""
NumPy ("Numerical Python") est LA bibliothèque de calcul numérique de Python.
Elle fournit un nouveau type d'objet, le tableau à N dimensions ("ndarray",
pour "N-dimensional array"), et des centaines de fonctions mathématiques pour
le manipuler.

Pourquoi est-ce si important ? Parce que presque toute la Data Science en
Python est construite sur NumPy :
    - pandas (cf. chap. 39) stocke ses colonnes dans des tableaux NumPy,
    - matplotlib (cf. chap. 40) trace des tableaux NumPy,
    - scikit-learn (Machine Learning, cf. chap. 51), SciPy (calcul
      scientifique), les bibliothèques d'images, etc. manipulent tous des
      tableaux NumPy.

Comprendre NumPy, c'est donc comprendre ce qui se passe "sous le capot" de
tous ces outils.

Ce chapitre suppose que vous connaissez les listes (chap. 16 et 24), les
boucles (chap. 13), les compréhensions (chap. 23), les modules (chap. 22) et
les slices (chap. 31).

Note : l'affichage des tableaux peut légèrement varier selon votre version de
NumPy. Ce chapitre a été vérifié avec NumPy 2.x ; presque tout fonctionne à
l'identique avec NumPy 1.x.
"""


# Installer et importer NumPy
##############################

"""
Comme pandas, NumPy ne fait pas partie de la bibliothèque standard : il faut
l'installer une fois (cf. chap. 0 et chap. 22) :
    ?> pip install numpy
ou
    ?> conda install numpy

On l'importe ensuite, par convention, sous l'alias "np". Tout le monde utilise
cet alias : vous le retrouverez dans toutes les documentations et tous les
tutoriels.

Comme au chap. 39, on protège l'import avec try … except (cf. chap. 26) : si
NumPy n'est pas installé, le programme affiche un message et s'arrête
proprement au lieu de crasher.
"""
import sys
import timeit

try:
    import numpy as np
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("NumPy n'est pas installé : lancez \"pip install numpy\" (ou")
    print("\"conda install numpy\"), puis relancez ce programme.")
    sys.exit(0)

print(np.__version__)  # => 2.5.3 (variable : dépend de votre installation)


# Pourquoi NumPy ? Listes contre tableaux
##########################################

"""
Imaginons qu'on veuille augmenter de 10 % une série de prix. Avec une liste
Python, il faut une boucle (ou une compréhension, cf. chap. 23) :
"""
prix = [10.0, 20.0, 35.0, 4.5]
prix_augmentes = [p * 1.1 for p in prix]
print(prix_augmentes)  # => [11.0, 22.0, 38.5, 4.95]

"""
Et attention : l'opérateur * sur une liste ne fait PAS ce qu'on attend d'un
calcul. Il RÉPÈTE la liste (cf. chap. 16) :
"""
print([1, 2, 3] * 2)  # => [1, 2, 3, 1, 2, 3]

"""
Avec NumPy, on convertit la liste en tableau avec np.array(), et les
opérations s'appliquent directement à TOUS les éléments, sans boucle :
"""
prix_np = np.array([10.0, 20.0, 35.0, 4.5])
print(prix_np * 1.1)          # => [11.   22.   38.5   4.95]
print(np.array([1, 2, 3]) * 2)  # => [2 4 6]

"""
Remarquez l'affichage : un tableau s'affiche entre crochets, mais SANS
virgules entre les éléments. C'est la façon la plus simple de distinguer, à
l'écran, un tableau NumPy d'une liste. Les nombres sont alignés en colonnes, et
"11." est un raccourci pour "11.0".

Les deux grandes différences entre une liste et un tableau NumPy :

    1. IMPT : tous les éléments d'un tableau ont le MÊME type (que des
       entiers, que des floats…), alors qu'une liste peut tout mélanger.

    2. IMPT : un tableau a une taille fixe, et ses éléments sont rangés côte
       à côte en mémoire. NumPy peut ainsi faire ses calculs en C (cf. chap.
       0), beaucoup plus vite qu'une boucle Python.

Mesurons la différence de vitesse avec le module timeit (cf. chap. 22) : on
calcule le carré d'un million de nombres, 10 fois de suite.
"""
grande_liste = list(range(1_000_000))
# np.arange() est l'équivalent NumPy de range() (cf. plus bas)
grand_tableau = np.arange(1_000_000)

duree_liste = timeit.timeit(lambda: [x ** 2 for x in grande_liste], number=10)
duree_numpy = timeit.timeit(lambda: grand_tableau ** 2, number=10)
print(f"Liste : {duree_liste:.3f} s")    # => Liste : 0.382 s (variable)
print(f"NumPy : {duree_numpy:.3f} s")    # => NumPy : 0.007 s (variable)
print(f"NumPy est environ {duree_liste / duree_numpy:.0f} fois plus rapide")
# => NumPy est environ 54 fois plus rapide (variable selon la machine)

"""
Les temps exacts dépendent de votre ordinateur, mais NumPy est typiquement
des dizaines de fois plus rapide. Sur des millions de lignes de données, cela
fait la différence entre une seconde et une minute.

Note : "lambda: …" crée une petite fonction sans nom, que timeit appelle
plusieurs fois. Les lambdas sont expliquées au chap. 32.
"""


# Créer des tableaux
#####################

"""
1. À partir d'une liste (ou d'une liste de listes pour un tableau 2D) :
"""
a = np.array([3, 1, 4, 1, 5])
print(a)        # => [3 1 4 1 5]
print(type(a))  # => <class 'numpy.ndarray'>

matrice = np.array([[1, 2, 3],
                    [4, 5, 6]])
print(matrice)
# => [[1 2 3]
#     [4 5 6]]

"""
Un tableau 2D, c'est un tableau de lignes : chaque liste intérieure devient
une ligne. Comme pour les matrices en listes de listes (cf. chap. 24), toutes
les lignes doivent avoir la même longueur :
"""
try:
    np.array([[1, 2, 3], [4, 5]])  # lignes de longueurs différentes
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
2. Des tableaux "pré-remplis", très utiles pour démarrer un calcul :
"""
print(np.zeros(4))        # => [0. 0. 0. 0.]
print(np.ones((2, 3)))    # tableau de 2 lignes et 3 colonnes rempli de 1
# => [[1. 1. 1.]
#     [1. 1. 1.]]
print(np.full(3, 7))      # => [7 7 7]

"""
Attention : pour un tableau 2D, la taille se donne sous forme de TUPLE
(lignes, colonnes) : np.ones((2, 3)), avec deux paires de parenthèses.

3. Des suites de nombres :
    - np.arange(start, stop, step) : comme range() (cf. chap. 13), stop est
      exclu, mais le pas peut être un float,
    - np.linspace(start, stop, n) : n valeurs régulièrement espacées, stop
      INCLUS. Très pratique pour tracer des courbes (cf. chap. 40).
"""
print(np.arange(5))            # => [0 1 2 3 4]
print(np.arange(2, 10, 3))     # => [2 5 8]
print(np.arange(0, 1, 0.25))   # => [0.   0.25 0.5  0.75]
print(np.linspace(0, 1, 5))    # => [0.   0.25 0.5  0.75 1.  ]

"""
4. Des nombres aléatoires. La méthode moderne (recommandée depuis NumPy 1.17)
consiste à créer un "générateur" avec np.random.default_rng(), puis à lui
demander des nombres.

Comme avec random.seed() (cf. chap. 22), on peut fixer une "graine" (seed) :
le générateur produit alors TOUJOURS la même suite de nombres. C'est
indispensable pour que des résultats soient reproductibles (et pour que les
`# =>` de ce cours restent justes !).
"""
rng = np.random.default_rng(seed=42)
print(rng.integers(1, 7, size=5))     # 5 lancers de dé (7 exclu)
# => [1 5 4 3 3]
print(rng.random(3))                  # 3 floats entre 0 (inclus) et 1 (exclu)
# => [0.69736803 0.09417735 0.97562235]
print(rng.normal(loc=10, scale=2, size=3).round(2))  # loi normale (moyenne 10)
# => [10.26  9.37  9.97]

"""
Note : on trouve encore beaucoup de code avec l'ancienne interface
(np.random.seed(42), np.random.randint(…)). Elle fonctionne toujours, mais
préférez default_rng() dans du code neuf.
"""


# Les attributs d'un tableau : dtype, shape, ndim, size
########################################################

"""
Tout tableau NumPy possède quelques attributs (cf. chap. 34 pour la notion
d'attribut) qui le décrivent :
    - .dtype : le type des éléments ("data type"),
    - .shape : la forme, sous forme de tuple (lignes, colonnes, …),
    - .ndim  : le nombre de dimensions,
    - .size  : le nombre total d'éléments.
"""
print(matrice.dtype)  # => int64
print(matrice.shape)  # => (2, 3)
print(matrice.ndim)   # => 2
print(matrice.size)   # => 6
print(len(matrice))   # => 2 (len() donne la taille de la 1re dimension)

print(a.shape)        # => (5,)  (un tuple d'un seul élément, cf. chap. 17)

"""
Les types les plus courants :
    - int64   : entiers sur 64 bits (int32 sur certains Windows),
    - float64 : nombres à virgule, comme les floats de Python,
    - bool    : booléens,
    - <U5     : chaînes Unicode d'au plus 5 caractères.

IMPT : NumPy choisit UN type pour tout le tableau. Si on mélange entiers et
floats, tout devient float ; si on mélange nombres et chaînes, tout devient
chaîne :
"""
print(np.array([1, 2, 3.5]))      # => [1.  2.  3.5]
print(np.array([1, 2, 3.5]).dtype)  # => float64
print(np.array([1, "deux"]))      # => ['1' 'deux']

"""
On peut choisir le type à la création, ou convertir un tableau avec
.astype() (comme int() ou float() pour une valeur, cf. chap. 6) :
"""
print(np.array([1, 2, 3], dtype=float))  # => [1. 2. 3.]
print(np.array([1.7, 2.2, -3.9]).astype(int))  # => [ 1  2 -3]
# Remarque : comme int(), .astype(int) TRONQUE (coupe la partie décimale), il
# n'arrondit pas.

"""
Conséquence du type fixe : une valeur affectée dans un tableau est convertie
dans le type du tableau, sans prévenir !
"""
entiers = np.array([1, 2, 3])
entiers[0] = 9.99
print(entiers)  # => [9 2 3]  (9.99 a été tronqué en 9 !)


# Indexation et slices
#######################

"""
Pour un tableau 1D, tout fonctionne comme pour les listes : indices à partir
de 0, indices négatifs, slices [start:stop:step] (cf. chap. 16 et 31).
"""
t = np.array([10, 20, 30, 40, 50, 60])
print(t[0])       # => 10
print(t[-1])      # => 60
print(t[1:4])     # => [20 30 40]
print(t[::2])     # => [10 30 50]
print(t[::-1])    # => [60 50 40 30 20 10]

"""
Pour un tableau 2D, on donne les deux indices DANS LES MÊMES CROCHETS,
séparés par une virgule : tableau[ligne, colonne].
"""
m = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print(m[1, 2])    # => 7   (ligne 1, colonne 2)
print(m[1][2])    # => 7   (fonctionne aussi, comme une liste de listes,
#                             mais c'est moins efficace)
print(m[-1, -1])  # => 12  (dernière ligne, dernière colonne)

"""
Et on peut mettre une slice dans chaque dimension. Le ":" seul signifie "tout"
dans cette dimension :
"""
print(m[0])       # => [1 2 3 4]   (la ligne 0 entière)
print(m[:, 0])    # => [1 5 9]     (la colonne 0 entière)
print(m[0:2, 1:3])  # les lignes 0 et 1, les colonnes 1 et 2
# => [[2 3]
#     [6 7]]

"""
IMPT : m[:, 0] (une colonne) est impossible à écrire aussi simplement avec une
liste de listes : il faudrait une compréhension [ligne[0] for ligne in m].
C'est l'une des raisons pour lesquelles on utilise NumPy (et pandas) pour les
tableaux de données.

Comme pour les listes, un indice trop grand provoque une IndexError :
"""
try:
    m[3, 0]  # il n'y a que 3 lignes (indices 0, 1 et 2)
except IndexError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Enfin, on peut modifier plusieurs éléments à la fois en affectant une slice :
"""
t2 = np.array([1, 2, 3, 4, 5])
t2[1:3] = 0
print(t2)  # => [1 0 0 4 5]


# Vues et copies
#################

"""
IMPT, et piège classique : avec une liste, une slice crée une COPIE (cf. chap.
31). Avec NumPy, une slice crée une VUE : un nouveau "regard" sur les MÊMES
données en mémoire. Modifier la vue modifie donc le tableau d'origine !
"""
original = np.array([1, 2, 3, 4, 5])
vue = original[1:4]
vue[0] = 99
print(vue)       # => [99  3  4]
print(original)  # => [ 1 99  3  4  5]  (l'original a changé !)

# Comparez avec une liste :
liste_originale = [1, 2, 3, 4, 5]
copie_liste = liste_originale[1:4]
copie_liste[0] = 99
print(liste_originale)  # => [1, 2, 3, 4, 5]  (inchangée)

"""
Pourquoi ce choix ? Pour la performance : sur un tableau d'un milliard de
nombres, copier à chaque slice serait très coûteux.

Si on veut une vraie copie indépendante, on utilise .copy() :
"""
original = np.array([1, 2, 3, 4, 5])
copie = original[1:4].copy()
copie[0] = 99
print(original)  # => [1 2 3 4 5]  (inchangé, cette fois)

"""
On peut vérifier si un tableau partage ses données avec un autre grâce à
np.shares_memory() :
"""
print(np.shares_memory(original, original[1:4]))         # => True
print(np.shares_memory(original, original[1:4].copy()))  # => False

"""
Règle simple : si vous voulez modifier un morceau de tableau sans toucher à
l'original, faites .copy(). (On retrouvera exactement le même problème avec
pandas, cf. chap. 39.)
"""


# Opérations vectorisées
#########################

"""
On appelle "opération vectorisée" une opération qui s'applique à tous les
éléments d'un tableau d'un seul coup, sans boucle écrite par le programmeur.

1. Entre un tableau et un nombre : l'opération est faite avec chaque élément.
"""
notes = np.array([12, 15, 8, 17])
print(notes + 1)    # => [13 16  9 18]
print(notes * 2)    # => [24 30 16 34]
print(notes / 20)   # => [0.6  0.75 0.4  0.85]
print(notes ** 2)   # => [144 225  64 289]
print(notes % 2)    # => [0 1 0 1]

"""
2. Entre deux tableaux de MÊME forme : l'opération est faite élément par
élément (le 1er avec le 1er, le 2e avec le 2e, etc.).
"""
quantites = np.array([3, 1, 2])
prix_unitaires = np.array([2.5, 10.0, 4.0])
print(quantites * prix_unitaires)        # => [ 7.5 10.   8. ]
print((quantites * prix_unitaires).sum())  # => 25.5 (le total de la commande)

"""
Comparez avec les listes, où + concatène (cf. chap. 16) :
"""
print([1, 2] + [3, 4])                      # => [1, 2, 3, 4]
print(np.array([1, 2]) + np.array([3, 4]))  # => [4 6]

"""
Si les formes sont incompatibles, NumPy lève une ValueError :
"""
try:
    np.array([1, 2, 3]) + np.array([1, 2])
except ValueError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
3. Les fonctions mathématiques de NumPy ("ufuncs", pour "fonctions
universelles") s'appliquent aussi à chaque élément. Elles remplacent les
fonctions du module math (cf. chap. 22), qui ne marchent que sur un nombre :
"""
x = np.array([0, 1, 4, 9])
print(np.sqrt(x))         # => [0. 1. 2. 3.]
print(np.abs(np.array([-2, 3, -5])))  # => [2 3 5]
print(np.round(np.array([1.234, 5.678]), 1))  # => [1.2 5.7]
print(np.sin(np.array([0, np.pi / 2])))       # => [0. 1.]

"""
4. Les comparaisons sont aussi vectorisées : elles renvoient un tableau de
booléens (on s'en servira juste après pour filtrer).
"""
print(notes >= 12)  # => [ True  True False  True]

"""
IMPT : dès que vous écrivez une boucle for sur un tableau NumPy, demandez-vous
s'il n'existe pas une opération vectorisée équivalente. C'est presque toujours
le cas, et c'est beaucoup plus rapide et plus lisible.
"""


# Le broadcasting
##################

"""
Le "broadcasting" (diffusion) est la règle qui permet à NumPy de faire des
opérations entre tableaux de formes DIFFÉRENTES, en "étirant" le plus petit
pour qu'il ait la forme du plus grand. On l'a déjà utilisé sans le savoir :
dans notes + 1, le nombre 1 est "étiré" en [1 1 1 1].

Exemple concret : 3 élèves (lignes), 4 matières (colonnes).
"""
notes_eleves = np.array([[12, 15, 9, 14],
                         [8, 11, 13, 10],
                         [16, 18, 14, 17]])
coefficients = np.array([2, 3, 1, 1])  # un coefficient par matière

print(notes_eleves.shape)  # => (3, 4)
print(coefficients.shape)  # => (4,)

print(notes_eleves * coefficients)
# => [[24 45  9 14]
#     [16 33 13 10]
#     [32 54 14 17]]

"""
Que s'est-il passé, pas à pas ?
    1. notes_eleves a la forme (3, 4) et coefficients la forme (4,).
    2. NumPy compare les formes en partant de la DROITE : 4 et 4 sont égaux,
       c'est compatible.
    3. coefficients n'a pas de 1re dimension : NumPy fait "comme si" on
       l'avait recopié sur chacune des 3 lignes :
           [[2 3 1 1]
            [2 3 1 1]
            [2 3 1 1]]
    4. Puis il multiplie élément par élément, comme d'habitude.

NumPy ne fait pas vraiment la copie en mémoire : il "fait comme si", ce qui
est très efficace.

On peut alors calculer la moyenne pondérée de chaque élève :
"""
total_points = (notes_eleves * coefficients).sum(axis=1)
moyennes_ponderees = total_points / coefficients.sum()
print(moyennes_ponderees.round(2))  # => [13.14 10.29 16.71]
# (le paramètre axis est expliqué un peu plus bas)

"""
La règle générale : deux dimensions sont compatibles si elles sont ÉGALES, ou
si l'une des deux vaut 1. Sinon, c'est une erreur :
"""
try:
    notes_eleves + np.array([1, 2, 3])  # formes (3, 4) et (3,) : 4 ≠ 3
except ValueError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Pour ajouter un bonus différent à chaque ÉLÈVE (donc à chaque ligne), il faut
un tableau en COLONNE, de forme (3, 1) : on l'obtient avec .reshape() (cf.
plus bas).
"""
bonus = np.array([1, 0, 2]).reshape(3, 1)
print(bonus.shape)  # => (3, 1)
print(notes_eleves + bonus)
# => [[13 16 10 15]
#     [ 8 11 13 10]
#     [18 20 16 19]]

"""
Ici, (3, 4) et (3, 1) : la dernière dimension vaut 4 et 1 (l'une vaut 1, OK),
la première vaut 3 et 3 (égales, OK). La colonne de bonus est recopiée sur les
4 colonnes.
"""


# Masques booléens et filtrage
###############################

"""
On a vu qu'une comparaison renvoie un tableau de booléens. Un tel tableau
s'appelle un "masque". IMPT : on peut l'utiliser entre crochets pour ne garder
que les éléments pour lesquels le masque vaut True.
"""
notes = np.array([12, 15, 8, 17, 6, 11])
masque = notes >= 10
print(masque)         # => [ True  True False  True False  True]
print(notes[masque])  # => [12 15 17 11]

# En une seule ligne (c'est l'écriture habituelle) :
print(notes[notes < 10])  # => [8 6]

"""
C'est l'équivalent d'une compréhension avec filtre (cf. chap. 23) :
    [n for n in notes if n < 10]
mais en plus court et plus rapide.

Pour combiner plusieurs conditions, ATTENTION : on n'utilise PAS and, or et
not (qui ne fonctionnent pas sur des tableaux), mais les opérateurs bit à bit
&, | et ~ (cf. chap. 21). Et les parenthèses autour de chaque condition sont
OBLIGATOIRES, car & est prioritaire sur >= (cf. chap. 5).
"""
print(notes[(notes >= 10) & (notes < 15)])  # => [12 11]
print(notes[(notes < 8) | (notes > 15)])    # => [17  6]
print(notes[~(notes >= 10)])                # => [8 6]

try:
    notes[(notes >= 10) and (notes < 15)]
except ValueError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Le message dit que la "valeur de vérité" d'un tableau est ambiguë : and veut
savoir si TOUT le tableau est vrai ou faux, ce qui n'a pas de sens. NumPy
propose .any() ("au moins un vrai ?") et .all() ("tous vrais ?"), comme les
fonctions any() et all() (cf. chap. 21) :
"""
print((notes >= 10).any())  # => True
print((notes >= 10).all())  # => False

"""
Astuce : comme True vaut 1 et False vaut 0, .sum() d'un masque COMPTE le
nombre de True, et .mean() en donne la proportion :
"""
print((notes >= 10).sum())   # => 4  (4 élèves ont la moyenne)
print((notes >= 10).mean())  # => 0.6666666666666666  (2/3 des élèves)

"""
Un masque permet aussi de MODIFIER uniquement certains éléments :
"""
notes_plafonnees = notes.copy()
notes_plafonnees[notes_plafonnees > 15] = 15
print(notes_plafonnees)  # => [12 15  8 15  6 11]

"""
Et np.where(condition, valeur_si_vrai, valeur_si_faux) est le "if … else …"
vectorisé (cf. le one-liner du chap. 12) :
"""
print(np.where(notes >= 10, "admis", "refusé"))
# => ['admis' 'admis' 'refusé' 'admis' 'refusé' 'admis']


# Fonctions d'agrégation et paramètre axis
###########################################

"""
Une fonction d'agrégation résume un tableau en une seule valeur : somme,
moyenne, minimum… Elles existent sous deux formes équivalentes : méthode
(notes.sum()) ou fonction (np.sum(notes)).
"""
notes = np.array([12, 15, 8, 17, 6, 11])
print(notes.sum())     # => 69
print(notes.mean())    # => 11.5
print(notes.min(), notes.max())  # => 6 17
print(notes.std().round(2))  # => 3.77 (écart-type : la dispersion des notes)
print(np.median(notes))  # => 11.5 (la médiane n'existe que comme fonction)
print(notes.argmax())  # => 3 (l'INDICE du maximum : notes[3] vaut 17)

"""
Sur un tableau 2D, ces fonctions agrègent par défaut TOUT le tableau. Le
paramètre axis permet de choisir la direction :
    - axis=0 : on agrège "en descendant" le long des lignes → un résultat par
      COLONNE,
    - axis=1 : on agrège "en traversant" les colonnes → un résultat par
      LIGNE.

Moyen mnémotechnique : axis indique la dimension qui DISPARAÎT. Le tableau a
la forme (3, 4) ; avec axis=0, la dimension 3 disparaît et il reste 4
résultats ; avec axis=1, la dimension 4 disparaît et il reste 3 résultats.
"""
# Rappel : 3 élèves (lignes) et 4 matières (colonnes)
print(notes_eleves)
# => [[12 15  9 14]
#     [ 8 11 13 10]
#     [16 18 14 17]]
print(notes_eleves.mean())          # => 13.083333333333334 (tout le tableau)
print(notes_eleves.mean(axis=0))
# => [12.         14.66666667 12.         13.66666667]
print(notes_eleves.mean(axis=1))    # => [12.5  10.5  16.25]
print(notes_eleves.max(axis=0))     # => [16 18 14 17]
# (la meilleure note de chaque matière)

"""
IMPT : ce paramètre axis se retrouve partout en Data Science, notamment dans
pandas (cf. chap. 39), avec exactement le même sens.

Note : NumPy affiche toujours les floats d'un tableau avec le même nombre de
décimales, d'où les "12." complétés par des espaces. Pour un affichage plus
lisible, on arrondit avec .round() :
"""
print(notes_eleves.mean(axis=0).round(1))  # => [12.  14.7 12.  13.7]


# Changer la forme : reshape, transposition, concaténation
###########################################################

"""
1. .reshape() réorganise les éléments dans une nouvelle forme, sans changer
leur ordre. Le nombre total d'éléments doit rester le même.
"""
suite = np.arange(1, 13)
print(suite)                 # => [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(suite.reshape(3, 4))
# => [[ 1  2  3  4]
#     [ 5  6  7  8]
#     [ 9 10 11 12]]
print(suite.reshape(2, 6))
# => [[ 1  2  3  4  5  6]
#     [ 7  8  9 10 11 12]]

# -1 signifie "calcule cette dimension toi-même" :
print(suite.reshape(4, -1).shape)  # => (4, 3)

try:
    suite.reshape(5, 3)  # 5 * 3 = 15 ≠ 12
except ValueError as err:
    print(f"7: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
À l'inverse, .ravel() (ou .flatten(), qui fait une copie) "aplatit" un tableau
en 1D :
"""
print(suite.reshape(3, 4).ravel())  # => [ 1  2  3  4  5  6  7  8  9 10 11 12]

"""
2. La transposition (.T) échange lignes et colonnes, comme la transposition de
matrice faite à la main au chap. 23 :
"""
petite = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(petite.T)
# => [[1 4]
#     [2 5]
#     [3 6]]
print(petite.shape, petite.T.shape)  # => (2, 3) (3, 2)

"""
3. La concaténation assemble plusieurs tableaux :
    - np.concatenate([a, b]) : bout à bout (le long de axis=0 par défaut),
    - np.vstack([a, b]) : empile verticalement (ajoute des lignes),
    - np.hstack([a, b]) : côte à côte (ajoute des colonnes).
"""
debut = np.array([1, 2, 3])
fin = np.array([4, 5])
print(np.concatenate([debut, fin]))  # => [1 2 3 4 5]

ligne_1 = np.array([1, 2, 3])
ligne_2 = np.array([4, 5, 6])
print(np.vstack([ligne_1, ligne_2]))
# => [[1 2 3]
#     [4 5 6]]
print(np.hstack([ligne_1, ligne_2]))  # => [1 2 3 4 5 6]

# Ajouter une colonne de totaux au tableau des notes :
totaux = notes_eleves.sum(axis=1).reshape(3, 1)
print(np.hstack([notes_eleves, totaux]))
# => [[12 15  9 14 50]
#     [ 8 11 13 10 42]
#     [16 18 14 17 65]]


# Les valeurs manquantes : NaN
###############################

"""
Dans les vraies données, il manque souvent des valeurs (capteur en panne,
case non remplie…). NumPy les représente par np.nan ("Not a Number"), une
valeur spéciale de type float.

Particularités de NaN :
    - toute opération avec NaN donne NaN ("contagion"),
    - NaN n'est égal à RIEN, pas même à lui-même !
"""
print(np.nan + 1)       # => nan
print(np.nan == np.nan)  # => False (!)

mesures = np.array([12.5, np.nan, 14.0, 13.5, np.nan])
print(mesures)          # => [12.5  nan 14.  13.5  nan]
print(mesures.mean())   # => nan  (une seule valeur manquante "contamine" tout)

"""
Comme NaN n'est égal à rien, on ne peut PAS le détecter avec == : on utilise
np.isnan(), qui renvoie un masque :
"""
print(mesures == np.nan)   # => [False False False False False] (inutile !)
print(np.isnan(mesures))   # => [False  True False False  True]
print(np.isnan(mesures).sum())  # => 2 (nombre de valeurs manquantes)

"""
Pour gérer les NaN, deux approches :
    1. les fonctions np.nan… (nansum, nanmean, nanmin, nanmax…), qui ignorent
       les NaN,
    2. filtrer les NaN avec un masque, ou les remplacer par une valeur.
"""
print(np.nanmean(mesures))  # => 13.333333333333334
print(np.nanmax(mesures))   # => 14.0
print(mesures[~np.isnan(mesures)])  # => [12.5 14.  13.5]  (sans les NaN)
print(np.where(np.isnan(mesures), 0, mesures))  # => [12.5  0.  14.  13.5  0. ]

"""
Note : un tableau d'entiers ne peut pas contenir de NaN (NaN est un float).
C'est pour cela que pandas transforme en float une colonne d'entiers à
laquelle il manque des valeurs (cf. chap. 39).
"""


# Cas pratique : un relevé de températures
###########################################

"""
Mettons tout cela ensemble. Une station météo relève la température 4 fois
par jour (à 0 h, 6 h, 12 h et 18 h) pendant une semaine. Un capteur est tombé
en panne une fois : la valeur manque.
"""
jours = np.array(["lun", "mar", "mer", "jeu", "ven", "sam", "dim"])
releves = np.array([[8.5, 7.0, 15.5, 12.0],
                    [9.0, 8.5, 17.0, 13.5],
                    [10.5, 9.5, 19.5, np.nan],
                    [7.0, 5.5, 12.0, 9.0],
                    [6.5, 5.0, 11.5, 8.5],
                    [8.0, 7.5, 16.0, 12.5],
                    [11.0, 10.0, 21.0, 16.0]])
print(releves.shape)  # => (7, 4) : 7 jours, 4 relevés par jour

# 1. Combien de relevés manquent ?
print(np.isnan(releves).sum())  # => 1

# 2. La moyenne de chaque jour (une valeur par LIGNE, donc axis=1), en
#    ignorant la valeur manquante :
moyennes_jour = np.nanmean(releves, axis=1)
print(moyennes_jour.round(1))  # => [10.8 12.  13.2  8.4  7.9 11.  14.5]

# 3. Le jour le plus chaud et le plus froid (argmax renvoie un indice, qu'on
#    utilise pour retrouver le nom du jour) :
print(jours[moyennes_jour.argmax()])  # => dim
print(jours[moyennes_jour.argmin()])  # => ven

# 4. Les jours où la moyenne a dépassé 11 degrés (masque sur un AUTRE tableau
#    de même taille : c'est très courant !) :
print(jours[moyennes_jour > 11])  # => ['mar' 'mer' 'dim']

# 5. La moyenne de chaque heure de relevé, sur la semaine (axis=0) :
heures = np.array([0, 6, 12, 18])
moyennes_heure = np.nanmean(releves, axis=0)
print(moyennes_heure.round(1))  # => [ 8.6  7.6 16.1 11.9]
print(f"Heure la plus chaude : {heures[moyennes_heure.argmax()]} h")
# => Heure la plus chaude : 12 h

# 6. L'amplitude thermique de chaque jour (max - min), vectorisée :
amplitudes = np.nanmax(releves, axis=1) - np.nanmin(releves, axis=1)
print(amplitudes)  # => [ 8.5  8.5 10.   6.5  6.5  8.5 11. ]

# 7. Conversion de tout le relevé en degrés Fahrenheit, en une ligne (les NaN
#    restent des NaN) :
print((releves * 9 / 5 + 32)[0])  # => [47.3 44.6 59.9 53.6]

"""
Avec des listes de listes, chacune de ces questions aurait demandé une ou
plusieurs boucles. Avec NumPy, chaque réponse tient en une ligne.
"""


# Et ensuite ?
###############

"""
NumPy est la fondation, mais on l'utilise rarement seul pour analyser des
données :
    - pandas (cf. chap. 39) ajoute des NOMS aux lignes et aux colonnes, des
      colonnes de types différents, la lecture de fichiers CSV… Chaque
      colonne d'un DataFrame est, en interne, un tableau NumPy, et tout ce
      qu'on a vu ici (vectorisation, masques, axis, NaN) s'y applique.
    - matplotlib (cf. chap. 40) trace des graphiques à partir de tableaux
      NumPy : np.linspace() est parfait pour générer les abscisses d'une
      courbe.

On peut toujours passer de l'un à l'autre : .tolist() convertit un tableau
en liste Python, et np.array() convertit une liste en tableau.
"""
print(np.array([1, 2, 3]).tolist())  # => [1, 2, 3]

"""
Pour aller plus loin :
    - la documentation officielle, et son guide "NumPy: the absolute basics
      for beginners" : https://numpy.org/doc/stable/user/absolute_beginners.html
    - les "100 numpy exercises", de difficulté croissante :
      https://github.com/rougier/numpy-100
"""
