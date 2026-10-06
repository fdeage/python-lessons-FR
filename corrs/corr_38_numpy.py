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
#  Chap. 38     #  NumPy : corrigés                                            #
#               #                                                              #
################################################################################

"""
Les affichages ci-dessous ont été vérifiés avec NumPy 2.5. Avec une autre
version, la présentation des tableaux peut légèrement varier.
"""

import sys

try:
    import numpy as np
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("NumPy n'est pas installé : lancez \"pip install numpy\" (ou")
    print("\"conda install numpy\"), puis relancez ce programme.")
    sys.exit(0)


#############################################
#  Pourquoi NumPy ? Listes contre tableaux  #
#############################################

"""
1. Sans exécuter, que valent :
       a) [2, 4, 6] * 2
       b) np.array([2, 4, 6]) * 2
       c) [1, 2] + [3, 4]
       d) np.array([1, 2]) + np.array([3, 4])
   Comment reconnaît-on, à l'affichage, un tableau NumPy d'une liste ?
"""
print([2, 4, 6] * 2)                        # => [2, 4, 6, 2, 4, 6]
print(np.array([2, 4, 6]) * 2)              # => [ 4  8 12]
print([1, 2] + [3, 4])                      # => [1, 2, 3, 4]
print(np.array([1, 2]) + np.array([3, 4]))  # => [4 6]

"""
Sur une liste, * RÉPÈTE la liste et + la CONCATÈNE (cf. chap. 16). Sur un
tableau NumPy, ce sont des opérations mathématiques, faites élément par
élément.

À l'affichage, un tableau NumPy n'a PAS de virgules entre ses éléments, et
ses nombres sont alignés (d'où les espaces dans "[ 4  8 12]").
"""

"""
2. Donnez deux raisons pour lesquelles un tableau NumPy est beaucoup plus
   rapide qu'une liste pour faire des calculs.

    - Tous les éléments d'un tableau ont le MÊME type : NumPy n'a pas besoin
      de vérifier le type de chaque élément avant de calculer.
    - Les éléments sont rangés côte à côte en mémoire, et les calculs sont
      faits par du code compilé en C, et non par une boucle Python
      interprétée ligne à ligne (cf. chap. 0).
"""


########################
#  Créer des tableaux  #
########################

"""
3. Créez, avec la fonction NumPy la plus adaptée, et affichez :
       a) un tableau contenant 2, 4, 6, 8 et 10 (sans les taper un par un),
       b) un tableau de 5 zéros,
       c) un tableau de 3 lignes et 2 colonnes rempli de 1,
       d) 9 valeurs régulièrement espacées entre 0 et 2 (2 inclus),
       e) un tableau 2D à partir de la liste [[1, 2], [3, 4], [5, 6]].
"""
# a) arange(start, stop, step) : stop est EXCLU, comme pour range(). Pour
#    inclure 10, on s'arrête à 11 (ou 12).
print(np.arange(2, 11, 2))   # => [ 2  4  6  8 10]

# b) zeros() crée des floats par défaut, d'où les points :
print(np.zeros(5))           # => [0. 0. 0. 0. 0.]

# c) La forme est un TUPLE (lignes, colonnes) : attention aux deux paires de
#    parenthèses !
print(np.ones((3, 2)))
# => [[1. 1.]
#     [1. 1.]
#     [1. 1.]]

# d) linspace(start, stop, n) : n valeurs, stop INCLUS. De 0 à 2 en 9
#    valeurs, il y a 8 intervalles de 2 / 8 = 0.25.
print(np.linspace(0, 2, 9))
# => [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]

# e) Chaque liste intérieure devient une ligne :
print(np.array([[1, 2], [3, 4], [5, 6]]))
# => [[1 2]
#     [3 4]
#     [5 6]]

"""
4. Avec un générateur np.random.default_rng() de graine 7, simulez 10
   lancers d'un dé à 6 faces. Relancez le programme : obtenez-vous les mêmes
   valeurs ? Pourquoi ?
"""
rng_de = np.random.default_rng(seed=7)
print(rng_de.integers(1, 7, size=10))  # => [6 4 5 6 4 5 6 2 1 2]

"""
Le 7 de integers(1, 7) est EXCLU : on obtient bien des valeurs de 1 à 6.

Oui, on obtient les mêmes valeurs à chaque exécution : la graine (seed) fixe
le point de départ du générateur, qui produit alors toujours la même suite de
nombres "pseudo-aléatoires". Sans graine (np.random.default_rng()), les
valeurs changeraient à chaque exécution.
"""


###########################################################
#  Les attributs d'un tableau : dtype, shape, ndim, size  #
###########################################################

"""
5. Soit t = np.array([[1.5, 2, 3], [4, 5, 6]]).
   Sans exécuter, que valent t.shape, t.ndim, t.size, len(t) et t.dtype ?
   Pourquoi le type n'est-il pas int64, alors que 5 des 6 nombres sont des
   entiers ?
"""
t = np.array([[1.5, 2, 3], [4, 5, 6]])
print(t.shape)  # => (2, 3)  (2 lignes, 3 colonnes)
print(t.ndim)   # => 2       (2 dimensions)
print(t.size)   # => 6       (6 éléments en tout)
print(len(t))   # => 2       (len() donne la taille de la 1re dimension)
print(t.dtype)  # => float64

"""
Un tableau NumPy n'a qu'UN type pour tous ses éléments. Comme 1.5 ne peut pas
être un entier, NumPy choisit float64 pour tout le tableau : les entiers
deviennent 2.0, 3.0, etc.
"""
print(t)
# => [[1.5 2.  3. ]
#     [4.  5.  6. ]]

"""
6. Sans exécuter, qu'affiche ce code ? Expliquez.
       ages = np.array([18, 25, 31])
       ages[1] = 25.9
       print(ages)
"""
ages = np.array([18, 25, 31])
ages[1] = 25.9
print(ages)  # => [18 25 31]

"""
Le tableau est de type int64 : la valeur 25.9 est convertie en entier pour
pouvoir y être rangée, et cette conversion TRONQUE la partie décimale (comme
int(25.9), cf. chap. 6). NumPy ne prévient pas : c'est un piège à connaître.
"""


##########################
#  Indexation et slices  #
##########################

"""
7. Soit m = np.arange(1, 21).reshape(4, 5).
   Avec une seule indexation à chaque fois, obtenez :
       a) le nombre 14,
       b) la dernière ligne,
       c) la 2e colonne ([2 7 12 17]),
       d) le carré central [[7 8 9] [12 13 14]],
       e) une ligne sur deux (les lignes 0 et 2),
       f) la dernière colonne, à l'envers ([20 15 10 5]).
"""
m = np.arange(1, 21).reshape(4, 5)

# a) 14 est sur la ligne 2 (3e ligne) et la colonne 3 (4e colonne) :
print(m[2, 3])      # => 14

# b) Un seul indice = une ligne entière. -1 = la dernière :
print(m[-1])        # => [16 17 18 19 20]

# c) ":" = toutes les lignes, puis la colonne 1 (la 2e) :
print(m[:, 1])      # => [ 2  7 12 17]

# d) Lignes 1 et 2 (stop 3 exclu), colonnes 1 à 3 (stop 4 exclu) :
print(m[1:3, 1:4])
# => [[ 7  8  9]
#     [12 13 14]]

# e) Une slice avec un pas de 2 sur les lignes (cf. chap. 31) :
print(m[::2])
# => [[ 1  2  3  4  5]
#     [11 12 13 14 15]]

# f) Toutes les lignes à l'envers (pas de -1), et la dernière colonne :
print(m[::-1, -1])  # => [20 15 10  5]


####################
#  Vues et copies  #
####################

"""
8. Sans exécuter, qu'affiche ce code ? Corrigez-le pour que le tableau
   notes ne soit pas modifié.
"""
notes = np.array([12, 8, 15, 9])
premieres = notes[:2]
premieres[1] = 20
print(notes)  # => [12 20 15  9]

"""
Avec NumPy, une slice est une VUE sur les mêmes données, et non une copie
(contrairement aux listes, cf. chap. 31) : modifier premieres modifie donc
aussi notes.

Correction : on fait une vraie copie avec .copy().
"""
notes = np.array([12, 8, 15, 9])
premieres = notes[:2].copy()
premieres[1] = 20
print(notes)      # => [12  8 15  9]  (inchangé)
print(premieres)  # => [12 20]


############################
#  Opérations vectorisées  #
############################

"""
9. Les prix HT d'un panier sont [12.5, 3.2, 8.0, 20.0] et les quantités
   achetées [2, 5, 1, 3]. Sans aucune boucle, calculez et affichez :
       a) les prix TTC (TVA de 20 %), arrondis à 2 décimales,
       b) le coût TTC de chaque ligne du panier (prix TTC × quantité),
       c) le total TTC du panier.
"""
prix_ht = np.array([12.5, 3.2, 8.0, 20.0])
quantites = np.array([2, 5, 1, 3])

# a) Tableau × nombre : chaque prix est multiplié par 1.2.
prix_ttc = (prix_ht * 1.2).round(2)
print(prix_ttc)            # => [15.    3.84  9.6  24.  ]

# b) Tableau × tableau de même forme : élément par élément.
couts = prix_ttc * quantites
print(couts)               # => [30.  19.2  9.6 72. ]

# c) .sum() additionne tous les éléments :
print(couts.sum().round(2))  # => 130.8

"""
10. Sans boucle, calculez la racine carrée des nombres de 1 à 10, arrondie à
    3 décimales.
"""
print(np.sqrt(np.arange(1, 11)).round(3))
# => [1.    1.414 1.732 2.    2.236 2.449 2.646 2.828 3.    3.162]

"""
np.sqrt() est une "ufunc" : elle s'applique à chaque élément. La fonction
math.sqrt() (cf. chap. 22), elle, n'accepte qu'un seul nombre.
"""


#####################
#  Le broadcasting  #
#####################

"""
11. Sans exécuter, pour chaque opération, dites si elle fonctionne, et si
    oui, quelle est la forme (shape) du résultat :
        a) un tableau (4, 3) + un tableau (3,)
        b) un tableau (4, 3) + un tableau (4,)
        c) un tableau (4, 3) + un tableau (4, 1)
        d) un tableau (4, 3) + le nombre 10

On compare les formes en partant de la DROITE : deux dimensions sont
compatibles si elles sont égales, ou si l'une vaut 1.
    a) 3 et 3 : OK. Le tableau (3,) est recopié sur les 4 lignes → (4, 3).
    b) 3 et 4 : ni égaux, ni 1 → ERREUR.
    c) 3 et 1 : OK ; 4 et 4 : OK. La colonne est recopiée sur les 3
       colonnes → (4, 3).
    d) Un nombre est compatible avec tout → (4, 3).
"""
grand = np.zeros((4, 3))
print((grand + np.ones(3)).shape)       # => (4, 3)
try:
    grand + np.ones(4)
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
print((grand + np.ones((4, 1))).shape)  # => (4, 3)
print((grand + 10).shape)               # => (4, 3)

"""
12. Un magasin a 3 boutiques (lignes) et vend 4 produits (colonnes).
        a) Calculez le chiffre d'affaires de chaque produit dans chaque
           boutique (tableau 3 × 4), grâce au broadcasting.
        b) La boutique 2 a une promotion de 10 % sur tout, les autres non.
           Appliquez la remise avec un tableau de forme (3, 1).
"""
ventes = np.array([[10, 0, 5, 2],
                   [4, 8, 1, 0],
                   [7, 3, 6, 9]])
prix_produits = np.array([2.5, 10, 4, 1.5])

# a) (3, 4) × (4,) : les prix sont recopiés sur chacune des 3 lignes.
ca = ventes * prix_produits
print(ca)
# => [[25.   0.  20.   3. ]
#     [10.  80.   4.   0. ]
#     [17.5 30.  24.  13.5]]

# b) Un coefficient par BOUTIQUE, donc par ligne : il faut une colonne de
#    forme (3, 1). La boutique 2 est la 3e ligne (indice 2).
remises = np.array([1, 1, 0.9]).reshape(3, 1)
print(remises.shape)  # => (3, 1)
print(ca * remises)
# => [[25.    0.   20.    3.  ]
#     [10.   80.    4.    0.  ]
#     [15.75 27.   21.6  12.15]]

"""
Avec un tableau de forme (3,), NumPy aurait essayé d'aligner les 3
coefficients sur les 4 COLONNES : c'est une erreur (cf. exercice 11 b).
"""


##################################
#  Masques booléens et filtrage  #
##################################

"""
13. Soit temperatures = np.array([12, 18, 25, 31, 8, 22, 35, 15]).
        a) Affichez les températures strictement supérieures à 20.
        b) Affichez celles comprises entre 10 et 20 (inclus).
        c) Combien de jours a-t-il fait plus de 30 degrés ? (sans len())
        d) Quelle proportion des jours a-t-il fait moins de 15 degrés ?
        e) Remplacez par 30 toutes les températures supérieures à 30, dans
           une copie du tableau.
        f) Avec np.where(), créez un tableau de "chaud" (> 20) ou "frais".
"""
temperatures = np.array([12, 18, 25, 31, 8, 22, 35, 15])

# a) La comparaison crée un masque, qu'on met entre crochets :
print(temperatures[temperatures > 20])  # => [25 31 22 35]

# b) & (et non and), et des parenthèses autour de chaque condition :
print(temperatures[(temperatures >= 10) & (temperatures <= 20)])
# => [12 18 15]

# c) True vaut 1 et False vaut 0 : la somme du masque compte les True.
print((temperatures > 30).sum())   # => 2

# d) La moyenne du masque donne la proportion de True : 2 jours sur 8.
print((temperatures < 15).mean())  # => 0.25

# e) .copy() pour ne pas modifier l'original, puis affectation à travers un
#    masque :
plafonnees = temperatures.copy()
plafonnees[plafonnees > 30] = 30
print(plafonnees)    # => [12 18 25 30  8 22 30 15]
print(temperatures)  # => [12 18 25 31  8 22 35 15]  (inchangé)

# f) np.where(condition, si_vrai, si_faux), élément par élément :
print(np.where(temperatures > 20, "chaud", "frais"))
# => ['frais' 'frais' 'chaud' 'chaud' 'frais' 'chaud' 'chaud' 'frais']

"""
14. Pourquoi le code suivant provoque-t-il une erreur ? Corrigez-le.
        temperatures[temperatures > 10 and temperatures < 20]
"""
try:
    temperatures[temperatures > 10 and temperatures < 20]
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
"and" a besoin de savoir si CHAQUE côté est vrai ou faux dans son ensemble.
Or "temperatures > 10" est un tableau de 8 booléens : il n'est ni vrai ni
faux, d'où l'erreur ("ambiguous").

Correction : on utilise l'opérateur &, qui combine les deux masques élément
par élément, avec des parenthèses (car & est prioritaire sur > et <).
"""
print(temperatures[(temperatures > 10) & (temperatures < 20)])  # => [12 18 15]


##############################################
#  Fonctions d'agrégation et paramètre axis  #
##############################################

"""
15. Soit les notes de 4 élèves (lignes) dans 3 matières (colonnes).
    Calculez :
        a) la moyenne générale de toutes les notes,
        b) la moyenne de chaque élève,
        c) la moyenne de chaque matière,
        d) la meilleure note de chaque matière,
        e) le numéro (l'indice) du meilleur élève, selon sa moyenne.
    Avant d'exécuter, prévoyez la forme du résultat de b) et de c).
"""
notes = np.array([[14, 9, 12],
                  [8, 15, 11],
                  [17, 13, 16],
                  [10, 7, 9]])

# a) Sans axis, on agrège tout le tableau :
print(notes.mean())  # => 11.75

# b) Une moyenne par élève, donc par LIGNE : axis=1 (la dimension des
#    colonnes "disparaît"). Le tableau (4, 3) donne un résultat de forme (4,).
moyennes_eleves = notes.mean(axis=1)
print(moyennes_eleves.round(2))  # => [11.67 11.33 15.33  8.67]

# c) Une moyenne par matière, donc par COLONNE : axis=0 (la dimension des
#    lignes "disparaît"). Résultat de forme (3,).
print(notes.mean(axis=0))  # => [12.25 11.   12.  ]

# d) Même logique, avec max :
print(notes.max(axis=0))   # => [17 15 16]

# e) argmax() renvoie l'INDICE de la plus grande valeur :
print(moyennes_eleves.argmax())  # => 2  (le 3e élève)


##############################################################
#  Changer la forme : reshape, transposition, concaténation  #
##############################################################

"""
16. a) Créez les entiers de 0 à 23 avec np.arange(), puis transformez-les en
       un tableau de 4 lignes et 6 colonnes, puis de 2 × 3 × 4.
    b) Que donne .reshape(5, -1) sur ce tableau de 24 éléments ? Pourquoi ?
    c) Transposez le tableau 4 × 6 : quelle est sa nouvelle forme ?
"""
# a)
nombres = np.arange(24)
tableau = nombres.reshape(4, 6)
print(tableau)
# => [[ 0  1  2  3  4  5]
#     [ 6  7  8  9 10 11]
#     [12 13 14 15 16 17]
#     [18 19 20 21 22 23]]
print(nombres.reshape(2, 3, 4).shape)  # => (2, 3, 4)
# (un tableau 3D : 2 "blocs" de 3 lignes et 4 colonnes ; 2 × 3 × 4 = 24)

# b) -1 demande à NumPy de calculer la dimension manquante : 24 / 5 n'est
#    pas un entier, c'est donc impossible.
try:
    nombres.reshape(5, -1)
except ValueError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# c) La transposition échange lignes et colonnes :
print(tableau.T.shape)  # => (6, 4)

"""
17. On a les notes du 1er trimestre t1 et du 2e trimestre t2 (2 élèves, 2
    matières).
        a) Empilez-les pour obtenir un tableau de 4 lignes.
        b) Mettez-les côte à côte pour obtenir un tableau de 4 colonnes.
"""
t1 = np.array([[12, 14], [9, 11]])
t2 = np.array([[13, 15], [10, 8]])

# a) vstack ("vertical stack") ajoute des lignes :
print(np.vstack([t1, t2]))
# => [[12 14]
#     [ 9 11]
#     [13 15]
#     [10  8]]

# b) hstack ("horizontal stack") ajoute des colonnes :
print(np.hstack([t1, t2]))
# => [[12 14 13 15]
#     [ 9 11 10  8]]

# (np.concatenate([t1, t2], axis=0) et axis=1 donnent les mêmes résultats.)


##################################
#  Les valeurs manquantes : NaN  #
##################################

"""
18. Soit mesures = np.array([2.5, np.nan, 3.1, 2.8, np.nan, 3.4]).
        a) Sans exécuter, que vaut mesures.mean() ? Et mesures[1] == np.nan ?
        b) Comptez les valeurs manquantes.
        c) Calculez la moyenne en ignorant les valeurs manquantes, de deux
           façons différentes.
        d) Remplacez les valeurs manquantes par la moyenne des autres.
"""
mesures = np.array([2.5, np.nan, 3.1, 2.8, np.nan, 3.4])

# a) NaN est "contagieux" : toute opération qui l'inclut donne NaN. Et NaN
#    n'est égal à rien, pas même à lui-même.
print(mesures.mean())        # => nan
print(mesures[1] == np.nan)  # => False

# b) On ne peut donc pas tester avec == : on utilise np.isnan().
print(np.isnan(mesures).sum())  # => 2

# c) 1re façon : une fonction "nan…", qui ignore les NaN.
print(np.nanmean(mesures).round(2))   # => 2.95
#    2e façon : on filtre les NaN avec le masque inversé (~), puis mean().
print(mesures[~np.isnan(mesures)].mean().round(2))  # => 2.95
# (sans .round(2), on obtiendrait 2.9499999999999997 : c'est l'imprécision
# des floats, cf. chap. 4)

# d) np.where() : si la valeur est NaN, on met la moyenne, sinon on garde la
#    valeur.
completees = np.where(np.isnan(mesures), np.nanmean(mesures), mesures)
print(completees)  # => [2.5  2.95 3.1  2.8  2.95 3.4 ]


##############################################
#  Cas pratique : un relevé de températures  #
##############################################

"""
19. Une salle de sport compte ses visiteurs chaque jour pendant 4 semaines
    (lignes) de 7 jours (colonnes, du lundi au dimanche).
"""
rng = np.random.default_rng(seed=2024)
visiteurs = rng.integers(40, 120, size=(4, 7))
jours = np.array(["lun", "mar", "mer", "jeu", "ven", "sam", "dim"])
print(visiteurs)
# => [[ 59  94  47  57  65  64 112]
#     [103 113 119  46  51 109  46]
#     [ 53  54 113  68  61  53  76]
#     [ 87 104  89 118  48  79  85]]

"""
    Calculez et affichez :
        a) le nombre total de visiteurs sur les 4 semaines,
        b) le total de chaque semaine,
        c) la fréquentation moyenne de chaque jour de la semaine (arrondie à
           1 décimale), puis le nom du jour le plus fréquenté en moyenne,
        d) le nombre de journées à plus de 100 visiteurs,
        e) les jours de la semaine dont la moyenne dépasse la moyenne
           générale,
        f) l'écart de chaque journée à la moyenne de SA semaine.
"""
# a) Tout le tableau :
print(visiteurs.sum())  # => 2173

# b) Un total par semaine = par ligne : axis=1.
print(visiteurs.sum(axis=1))  # => [498 587 478 610]

# c) Une moyenne par jour = par colonne : axis=0. Puis argmax() donne
#    l'indice du maximum, qui sert d'indice dans le tableau jours.
moyennes_jours = visiteurs.mean(axis=0)
print(moyennes_jours.round(1))  # => [75.5 91.2 92.  72.2 56.2 76.2 79.8]
print(jours[moyennes_jours.argmax()])  # => mer

# d) Un masque, puis sa somme :
print((visiteurs > 100).sum())  # => 8

# e) On compare chaque moyenne de jour à la moyenne générale (un nombre),
#    et on utilise ce masque sur le tableau jours (même taille : 7) :
print(visiteurs.mean().round(1))                 # => 77.6
print(jours[moyennes_jours > visiteurs.mean()])  # => ['mar' 'mer' 'dim']

# f) La moyenne de chaque semaine est de forme (4,). Pour la soustraire à
#    chaque LIGNE, il faut une colonne de forme (4, 1) (cf. broadcasting).
moyennes_semaines = visiteurs.mean(axis=1).reshape(4, 1)
print((visiteurs - moyennes_semaines).round(1))
# => [[-12.1  22.9 -24.1 -14.1  -6.1  -7.1  40.9]
#     [ 19.1  29.1  35.1 -37.9 -32.9  25.1 -37.9]
#     [-15.3 -14.3  44.7  -0.3  -7.3 -15.3   7.7]
#     [ -0.1  16.9   1.9  30.9 -39.1  -8.1  -2.1]]

"""
Lecture : un nombre positif signifie que ce jour-là, la salle a eu plus de
visiteurs que la moyenne de sa semaine. Le dimanche de la 1re semaine (+40.9)
et le mercredi de la 3e (+44.7) sont des pics de fréquentation.
"""
