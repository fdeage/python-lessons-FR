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
#  Chap. 38     #  NumPy : exercices                                           #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", essayez de prévoir le résultat
avant de lancer le programme.

Ces exercices nécessitent NumPy (cf. chapitre, section "Installer et importer
NumPy").

Les corrigés sont dans le fichier corrs/corr_38_numpy.py.
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

2. Donnez deux raisons pour lesquelles un tableau NumPy est beaucoup plus
   rapide qu'une liste pour faire des calculs.
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

4. Avec un générateur np.random.default_rng() de graine 7, simulez 10
   lancers d'un dé à 6 faces. Relancez le programme : obtenez-vous les mêmes
   valeurs ? Pourquoi ?
"""


###########################################################
#  Les attributs d'un tableau : dtype, shape, ndim, size  #
###########################################################

"""
5. Soit t = np.array([[1.5, 2, 3], [4, 5, 6]]).
   Sans exécuter, que valent t.shape, t.ndim, t.size, len(t) et t.dtype ?
   Pourquoi le type n'est-il pas int64, alors que 5 des 6 nombres sont des
   entiers ?

6. Sans exécuter, qu'affiche ce code ? Expliquez.
       ages = np.array([18, 25, 31])
       ages[1] = 25.9
       print(ages)
"""


##########################
#  Indexation et slices  #
##########################

"""
7. Soit m = np.arange(1, 21).reshape(4, 5), c'est-à-dire :
       [[ 1  2  3  4  5]
        [ 6  7  8  9 10]
        [11 12 13 14 15]
        [16 17 18 19 20]]
   Avec une seule indexation à chaque fois, obtenez :
       a) le nombre 14,
       b) la dernière ligne,
       c) la 2e colonne ([2 7 12 17]),
       d) le carré central [[7 8 9] [12 13 14]],
       e) une ligne sur deux (les lignes 0 et 2),
       f) la dernière colonne, à l'envers ([20 15 10 5]).
"""


####################
#  Vues et copies  #
####################

"""
8. Sans exécuter, qu'affiche ce code ? Corrigez-le pour que le tableau
   notes ne soit pas modifié.
       notes = np.array([12, 8, 15, 9])
       premieres = notes[:2]
       premieres[1] = 20
       print(notes)
"""


############################
#  Opérations vectorisées  #
############################

"""
9. Les prix HT d'un panier sont [12.5, 3.2, 8.0, 20.0] et les quantités
   achetées [2, 5, 1, 3]. Sans aucune boucle, calculez et affichez :
       a) les prix TTC (TVA de 20 %), arrondis à 2 décimales,
       b) le coût TTC de chaque ligne du panier (prix TTC × quantité),
       c) le total TTC du panier.

10. Sans boucle, calculez la racine carrée des nombres de 1 à 10, arrondie à
    3 décimales.
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

12. Un magasin a 3 boutiques (lignes) et vend 4 produits (colonnes). Le
    tableau ventes donne les quantités vendues :
        ventes = np.array([[10, 0, 5, 2],
                           [4, 8, 1, 0],
                           [7, 3, 6, 9]])
    Les prix des 4 produits sont [2.5, 10, 4, 1.5].
        a) Calculez le chiffre d'affaires de chaque produit dans chaque
           boutique (tableau 3 × 4), grâce au broadcasting.
        b) La boutique 2 a une promotion de 10 % sur tout, les autres non.
           Appliquez la remise avec un tableau de forme (3, 1).
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

14. Pourquoi le code suivant provoque-t-il une erreur ? Corrigez-le.
        temperatures[temperatures > 10 and temperatures < 20]
"""


##############################################
#  Fonctions d'agrégation et paramètre axis  #
##############################################

"""
15. Soit les notes de 4 élèves (lignes) dans 3 matières (colonnes) :
        notes = np.array([[14, 9, 12],
                          [8, 15, 11],
                          [17, 13, 16],
                          [10, 7, 9]])
    Calculez :
        a) la moyenne générale de toutes les notes,
        b) la moyenne de chaque élève,
        c) la moyenne de chaque matière,
        d) la meilleure note de chaque matière,
        e) le numéro (l'indice) du meilleur élève, selon sa moyenne.
    Avant d'exécuter, prévoyez la forme du résultat de b) et de c).
"""


##############################################################
#  Changer la forme : reshape, transposition, concaténation  #
##############################################################

"""
16. a) Créez les entiers de 0 à 23 avec np.arange(), puis transformez-les en
       un tableau de 4 lignes et 6 colonnes, puis de 2 × 3 × 4.
    b) Que donne .reshape(5, -1) sur ce tableau de 24 éléments ? Pourquoi ?
    c) Transposez le tableau 4 × 6 : quelle est sa nouvelle forme ?

17. On a les notes du 1er trimestre t1 = np.array([[12, 14], [9, 11]]) et
    du 2e trimestre t2 = np.array([[13, 15], [10, 8]]) (2 élèves, 2
    matières).
        a) Empilez-les pour obtenir un tableau de 4 lignes.
        b) Mettez-les côte à côte pour obtenir un tableau de 4 colonnes.
"""


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


##############################################
#  Cas pratique : un relevé de températures  #
##############################################

"""
19. Une salle de sport compte ses visiteurs chaque jour pendant 4 semaines
    (lignes) de 7 jours (colonnes, du lundi au dimanche). Le tableau est
    généré ci-dessous : ne le modifiez pas.
"""
rng = np.random.default_rng(seed=2024)
visiteurs = rng.integers(40, 120, size=(4, 7))
jours = np.array(["lun", "mar", "mer", "jeu", "ven", "sam", "dim"])
print(visiteurs)

"""
    Calculez et affichez :
        a) le nombre total de visiteurs sur les 4 semaines,
        b) le total de chaque semaine,
        c) la fréquentation moyenne de chaque jour de la semaine (arrondie à
           1 décimale), puis le nom du jour le plus fréquenté en moyenne,
        d) le nombre de journées à plus de 100 visiteurs,
        e) les jours de la semaine dont la moyenne dépasse la moyenne
           générale,
        f) l'écart de chaque journée à la moyenne de SA semaine (indice :
           reshape ou broadcasting avec un tableau de forme (4, 1)).
"""
