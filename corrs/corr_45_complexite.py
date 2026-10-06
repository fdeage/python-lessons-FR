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
#  Chap. 45     #  Complexité algorithmique : corrigés                         #
#               #                                                              #
################################################################################

import math
import timeit


#######################################
#  Compter les opérations, notation O  #
#######################################

"""
1. Sans exécuter : simplifiez ces coûts avec la notation O.
       a) 5n + 3
       b) n² + 1000n
       c) 42
       d) 2n³ + n²
       e) n/2 + log₂(n)
       f) 3 × 2^n + n¹⁰
"""
# a) O(n)       : on garde le terme dominant (5n) et on oublie la constante 5.
# b) O(n²)      : pour n grand, n² finit toujours par dépasser 1000n (dès
#                 n > 1000).
# c) O(1)       : un coût constant, qui ne dépend pas de n.
# d) O(n³)
# e) O(n)       : n/2 grandit beaucoup plus vite que log₂(n).
# f) O(2^n)     : une exponentielle finit TOUJOURS par écraser un polynôme,
#                 même n¹⁰. Vérifions à partir de quand :
n = 2
while 2 ** n <= n ** 10:
    n += 1
print(n)   # => 59  : dès n = 59, 2^n dépasse n¹⁰

"""
2. Vrai ou faux ?
       a) Un algorithme O(n) est toujours plus rapide qu'un algorithme O(n²).
       b) Si un algorithme O(n²) met 1 seconde pour n = 1000, il mettra
          environ 4 secondes pour n = 2000.
       c) O(2n) et O(n) désignent la même complexité.
       d) log₂(1 milliard) est environ égal à 30.
"""
# a) FAUX. La notation O décrit la croissance pour n GRAND. Pour de petites
#    données, un algorithme O(n²) avec une petite constante peut être plus
#    rapide qu'un O(n) avec une grosse constante. Mais au-delà d'une
#    certaine taille, le O(n) gagne toujours.
# b) VRAI. n double, donc n² est multiplié par 2² = 4.
# c) VRAI. On oublie les constantes multiplicatives.
# d) VRAI :
print(round(math.log2(1_000_000_000), 1))   # => 29.9

"""
3. Un programme O(n) met 2 secondes pour traiter 1 million de lignes.
   Combien de temps environ pour 10 millions de lignes ? Et si le programme
   était O(n²) (avec les mêmes 2 secondes pour 1 million) ?
"""
# O(n) : n est multiplié par 10, donc le temps aussi : environ 20 secondes.
# O(n²) : le temps est multiplié par 10² = 100 : environ 200 secondes, soit
# plus de 3 minutes.
print(2 * 10, 2 * 10 ** 2)   # => 20 200


##########################
#  Analyser une boucle   #
##########################

"""
4. Sans exécuter : combien de fois la ligne "compteur += 1" est-elle
   exécutée, en fonction de n ? Donnez la complexité de chaque fonction.
   (voir les fonctions ci-dessous)
   Vérifiez ensuite en appelant chaque fonction avec n = 16 et n = 1024.
"""


def a(n):
    compteur = 0
    for i in range(n):
        for j in range(10):
            compteur += 1
    return compteur


def b(n):
    compteur = 0
    for i in range(n):
        compteur += 1
    for j in range(n):
        for k in range(n):
            compteur += 1
    return compteur


def c(n):
    compteur = 0
    i = 1
    while i < n:
        compteur += 1
        i = i * 2
    return compteur


def d(n):
    compteur = 0
    for i in range(n):
        j = n
        while j > 1:
            compteur += 1
            j = j // 2
    return compteur


# a : 10 × n fois → O(n). La boucle interne a un nombre FIXE de tours (10) :
#     elle ne dépend pas de n, c'est une constante.
# b : n + n² fois → O(n²). Boucle simple PUIS boucles imbriquées : on
#     additionne, et c'est le n² qui domine.
# c : i vaut 1, 2, 4, 8… : il double à chaque tour, donc il atteint n en
#     log₂(n) tours → O(log n).
# d : la boucle while fait log₂(n) tours, et elle est répétée n fois par le
#     for → n × log₂(n) → O(n log n).
for n in [16, 1024]:
    print(a(n), b(n), c(n), d(n))
# => 160 272 4 64
#    10240 1049600 10 10240

"""
5. Quelle est la complexité de cette fonction ? Où se cache la boucle
   "invisible" ? Réécrivez-la pour qu'elle soit en O(n).
"""


def sans_doublons(valeurs):
    resultat = []
    for v in valeurs:
        if v not in resultat:
            resultat.append(v)
    return resultat


# La boucle invisible : "v not in resultat" parcourt la liste resultat.
# Dans le pire cas (aucun doublon), resultat grandit jusqu'à n éléments :
# 0 + 1 + 2 + … + (n-1) comparaisons → O(n²).
#
# Version O(n) : on garde la liste (pour conserver l'ordre d'apparition) et
# on ajoute un set (pour tester la présence en O(1)).


def sans_doublons_rapide(valeurs):
    resultat = []
    deja_vus = set()
    for v in valeurs:
        if v not in deja_vus:      # O(1) en moyenne
            deja_vus.add(v)
            resultat.append(v)
    return resultat


print(sans_doublons([3, 1, 3, 2, 1]))          # => [3, 1, 2]
print(sans_doublons_rapide([3, 1, 3, 2, 1]))   # => [3, 1, 2]

# Note : list(dict.fromkeys(valeurs)) donne le même résultat en une ligne,
# en O(n), car les dictionnaires conservent l'ordre d'insertion (cf. chap. 27).
print(list(dict.fromkeys([3, 1, 3, 2, 1])))    # => [3, 1, 2]


#####################################
#  Complexité des opérations Python  #
#####################################

"""
6. Pour chaque opération, donnez sa complexité (n = taille de la
   structure) :
       a) liste[500]          b) liste.append(x)     c) liste.insert(0, x)
       d) x in liste          e) x in un_set         f) d["cle"]
       g) sorted(liste)       h) liste[10:20]        i) len(liste)
"""
# a) O(1)        : accès direct par l'indice.
# b) O(1)        : ajout en fin de liste.
# c) O(n)        : il faut décaler tous les éléments d'un cran.
# d) O(n)        : parcours de la liste.
# e) O(1)        : en moyenne, grâce au hachage.
# f) O(1)        : en moyenne, grâce au hachage.
# g) O(n log n)  : Timsort.
# h) O(10), soit O(1) ici : une slice coûte la taille de ce qu'elle copie
#    (20 - 10 = 10 éléments), pas la taille de la liste.
# i) O(1)        : Python stocke la longueur, il ne recompte pas.

"""
7. On reçoit chaque jour une liste de 100 000 identifiants de clients, et
   on veut savoir lesquels sont des clients "premium" (une liste de 50 000
   identifiants). Écrivez une fonction clients_premium(clients, premium) qui
   renvoie la liste des clients premium, en O(n + m).
"""


def clients_premium(clients, premium):
    premium_set = set(premium)      # O(m) : construction du set
    # Puis n tests "in" en O(1) chacun : O(n)
    return [c for c in clients if c in premium_set]


print(clients_premium(["c1", "c2", "c3", "c4"], ["c4", "c2", "c9"]))
# => ['c2', 'c4']

# Avec "c in premium" sur la LISTE, on aurait fait jusqu'à
# 100 000 × 50 000 = 5 milliards de comparaisons. Avec le set : environ
# 150 000 opérations.

"""
8. Écrivez une fonction construire_csv(lignes) qui reçoit une liste de
   listes de nombres et renvoie le texte CSV correspondant, SANS concaténer
   de chaîne dans une boucle avec "+".
"""


def construire_csv(lignes):
    textes = []
    for ligne in lignes:
        # str(x) pour chaque nombre, puis join avec des virgules
        textes.append(",".join(str(x) for x in ligne))
    return "\n".join(textes)


print(repr(construire_csv([[1, 2], [3, 4]])))   # => '1,2\n3,4'
print(construire_csv([[1.5, 2], [3, 4], [5, 6]]))
# => 1.5,2
#    3,4
#    5,6

# On construit une liste de morceaux, puis un seul join() final : chaque
# caractère n'est copié qu'une fois, la fonction est en O(taille du texte).


####################################################
#  Recherche linéaire et recherche dichotomique   #
####################################################

"""
9. Sans exécuter : combien d'étapes, au maximum, faut-il à une recherche
   dichotomique dans une liste triée de :
       a) 16 éléments ?   b) 1000 éléments ?   c) 1 million d'éléments ?
       d) 1 milliard d'éléments ?
"""
# À chaque étape, on divise la zone de recherche par 2 : le nombre maximum
# d'étapes est le nombre de divisions par 2 nécessaires pour arriver à une
# zone vide, soit ⌊log₂(n)⌋ + 1.
for n in [16, 1000, 1_000_000, 1_000_000_000]:
    print(n, math.floor(math.log2(n)) + 1)
# => 16 5
#    1000 10
#    1000000 20
#    1000000000 30

"""
10. Écrivez une fonction recherche_dichotomique(liste, cible) qui renvoie
    l'indice de la cible dans la liste triée, ou -1 si elle est absente.
    Testez-la sur [3, 8, 15, 21, 42, 57, 60] avec 42, 3, 60 et 10.
"""


def recherche_dichotomique(liste, cible):
    gauche, droite = 0, len(liste) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste[milieu] == cible:
            return milieu
        elif liste[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1


triee = [3, 8, 15, 21, 42, 57, 60]
print([recherche_dichotomique(triee, x) for x in [42, 3, 60, 10]])
# => [4, 0, 6, -1]

# Pensez toujours à tester les cas limites : le premier élément, le dernier,
# un élément absent… et la liste vide :
print(recherche_dichotomique([], 5))   # => -1

"""
11. Modifiez votre fonction pour qu'elle AFFICHE la zone de recherche
    (gauche, droite) à chaque étape. Faites-la tourner sur l'exemple
    précédent avec la cible 10.
"""


def recherche_dichotomique_bavarde(liste, cible):
    gauche, droite = 0, len(liste) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        print(f"zone [{gauche}, {droite}], milieu {milieu} : "
              f"{liste[milieu]}")
        if liste[milieu] == cible:
            return milieu
        elif liste[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    print(f"zone vide (gauche = {gauche} > droite = {droite})")
    return -1


print(recherche_dichotomique_bavarde(triee, 10))
# => zone [0, 6], milieu 3 : 21
#    zone [0, 2], milieu 1 : 8
#    zone [2, 2], milieu 2 : 15
#    zone vide (gauche = 2 > droite = 1)
#    -1

# 21 > 10 : on va à gauche ; 8 < 10 : on va à droite ; 15 > 10 : on va à
# gauche… et la zone devient vide : 10 n'est pas dans la liste. Notez que
# gauche (2) indique la position où il FAUDRAIT insérer 10 pour garder la
# liste triée (c'est ce que renvoie bisect.bisect_left).

"""
12. On doit chercher 1000 valeurs dans une liste de 1 million d'éléments
    non triée. Que vaut-il mieux faire :
        a) 1000 recherches linéaires ?
        b) trier la liste, puis faire 1000 recherches dichotomiques ?
        c) construire un set, puis faire 1000 tests "in" ?
"""
n, k = 1_000_000, 1000
print(f"a) {k * n:.0e}")                                   # => a) 1e+09
print(f"b) {n * math.log2(n) + k * math.log2(n):.0e}")     # => b) 2e+07
print(f"c) {n + k:.0e}")                                   # => c) 1e+06
# a) 1000 × 1 million = 1 milliard d'opérations : de loin le pire.
# b) le tri (≈ 20 millions) domine ; les recherches ne coûtent presque rien.
# c) construire le set coûte ≈ 1 million, puis chaque test est O(1). C'est
#    le meilleur choix… à condition d'avoir la mémoire pour le set.


#########################
#  Algorithmes de tri   #
#########################

"""
13. Le tri à bulles. Écrivez une fonction tri_bulles(liste) qui renvoie
    (liste_triée, nombre_de_comparaisons), sans modifier la liste
    d'origine. Testez-la sur [5, 1, 4, 2, 8]. Quelle est sa complexité ?
"""


def tri_bulles(liste):
    liste = liste.copy()
    comparaisons = 0
    n = len(liste)
    for passage in range(n - 1):
        # Après chaque passage, le plus grand élément restant est à sa
        # place définitive à la fin : inutile de le comparer à nouveau.
        for i in range(n - 1 - passage):
            comparaisons += 1
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
    return liste, comparaisons


print(tri_bulles([5, 1, 4, 2, 8]))   # => ([1, 2, 4, 5, 8], 10)

# Comparaisons : (n-1) + (n-2) + … + 1 = n(n-1)/2 → O(n²). Pour n = 5 : 10.

"""
14. Améliorez tri_bulles : si un passage complet ne fait AUCUN échange, la
    liste est triée et on peut s'arrêter. Combien de comparaisons sur une
    liste déjà triée de 1000 éléments ? Quelle est la complexité dans le
    meilleur cas ?
"""


def tri_bulles_ameliore(liste):
    liste = liste.copy()
    comparaisons = 0
    n = len(liste)
    for passage in range(n - 1):
        echange = False
        for i in range(n - 1 - passage):
            comparaisons += 1
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                echange = True
        if not echange:
            break             # aucun échange : la liste est triée
    return liste, comparaisons


print(tri_bulles_ameliore([5, 1, 4, 2, 8]))       # => ([1, 2, 4, 5, 8], 9)
# (La liste est triée dès le 2e passage ; le 3e passage (2 comparaisons) ne
# fait aucun échange, donc on s'arrête : 4 + 3 + 2 = 9 au lieu de 10.)
print(tri_bulles_ameliore(list(range(1000)))[1])  # => 999
print(tri_bulles(list(range(1000)))[1])           # => 499500

# Sur une liste déjà triée, un seul passage suffit : n - 1 comparaisons.
# Meilleur cas : O(n). Pire cas (liste à l'envers) : toujours O(n²).

"""
15. Sans exécuter : pour trier 1 million d'éléments, combien de comparaisons
    environ font :
        a) un tri par sélection (n(n-1)/2) ?
        b) sorted() (environ n × log₂(n)) ?
"""
n = 1_000_000
print(f"{n * (n - 1) // 2:,}")        # => 499,999,500,000
print(f"{round(n * math.log2(n)):,}")  # => 19,931,569
# Environ 500 milliards contre 20 millions : 25 000 fois moins pour
# sorted(). (Le format ":," ajoute un séparateur de milliers, cf. chap. 8.)


################################
#  Récursivité et complexité   #
################################

"""
16. Sans exécuter : quelle est la complexité de ces fonctions récursives ?
    (voir somme et puissance_rapide ci-dessous)
"""


def somme(liste):
    if not liste:
        return 0
    return liste[0] + somme(liste[1:])


def puissance_rapide(x, n):
    if n == 0:
        return 1
    moitie = puissance_rapide(x, n // 2)
    if n % 2 == 0:
        return moitie * moitie
    return moitie * moitie * x


print(somme([1, 2, 3, 4]))        # => 10
print(puissance_rapide(2, 10))    # => 1024

# somme : n appels récursifs (la liste perd un élément à chaque fois). Mais
#   CHAQUE appel fait liste[1:], qui COPIE la liste : n-1, puis n-2…
#   éléments copiés. Total : O(n²) ! (La version avec une boucle, ou sum(),
#   est O(n).) C'est encore une "boucle cachée".
# puissance_rapide : n est divisé par 2 à chaque appel → log₂(n) appels,
#   chacun en O(1) → O(log n). Bien mieux que les n multiplications d'une
#   boucle naïve.

"""
17. Écrivez une version de puissance_rapide qui compte ses appels, et
    comparez avec le nombre de multiplications d'une boucle naïve, pour
    x = 2 et n = 1000.
"""
nb_appels = 0


def puissance_rapide_comptee(x, n):
    global nb_appels
    nb_appels += 1
    if n == 0:
        return 1
    moitie = puissance_rapide_comptee(x, n // 2)
    if n % 2 == 0:
        return moitie * moitie
    return moitie * moitie * x


def puissance_naive(x, n):
    resultat = 1
    multiplications = 0
    for i in range(n):
        resultat = resultat * x
        multiplications += 1
    return resultat, multiplications


nb_appels = 0
r1 = puissance_rapide_comptee(2, 1000)
r2, nb_mult = puissance_naive(2, 1000)
print(r1 == r2 == 2 ** 1000)   # => True
print(nb_appels, nb_mult)      # => 11 1000

# 11 appels (n = 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0) contre 1000
# multiplications. C'est l'algorithme d'"exponentiation rapide", utilisé
# notamment en cryptographie, avec des n gigantesques.


#############################
#  Mémoire et mesures       #
#############################

"""
18. Quelle est la complexité en MÉMOIRE de :
        a) sum([x ** 2 for x in range(n)])
        b) sum(x ** 2 for x in range(n))
        c) a_des_doublons_rapide du chapitre (avec un set)
"""
# a) O(n) : la compréhension de liste construit TOUTE la liste en mémoire
#    avant que sum() ne commence.
# b) O(1) : l'expression génératrice produit les valeurs une par une ;
#    sum() les additionne au fur et à mesure (cf. chap. 36).
# c) O(n) : dans le pire cas (aucun doublon), le set contient les n valeurs.

"""
19. Avec timeit, mesurez le temps de "x in liste" et de "x in un_set" pour
    des structures de 1 000, 10 000 et 100 000 éléments (x étant le dernier
    élément). Comment évoluent les temps quand n est multiplié par 10 ?
"""
for n in [1_000, 10_000, 100_000]:
    liste = list(range(n))
    un_set = set(liste)
    x = n - 1
    t_liste = timeit.timeit(lambda: x in liste, number=100)
    t_set = timeit.timeit(lambda: x in un_set, number=100)
    print(f"n = {n:>6} : liste {t_liste:.5f} s, set {t_set:.7f} s")
# => n =   1000 : liste 0.00051 s, set 0.0000028 s
#    n =  10000 : liste 0.00523 s, set 0.0000027 s
#    n = 100000 : liste 0.05408 s, set 0.0000029 s
# (Temps variables selon la machine.)
#
# Pour la liste, le temps est multiplié par 10 environ quand n est multiplié
# par 10 : c'est la signature d'un O(n). Pour le set, le temps ne bouge
# pratiquement pas : O(1).

"""
20. Moyenne glissante sur [10, 12, 11, 13, 15, 14, 16, 18, 17], fenêtre de
    3 jours.
        a) version simple ;   b) version en O(n).
"""


def moyenne_glissante_simple(valeurs, k):
    resultat = []
    for i in range(k - 1, len(valeurs)):
        fenetre = valeurs[i - k + 1:i + 1]    # les k dernières valeurs
        resultat.append(sum(fenetre) / k)     # sum() : k opérations
    return resultat


def moyenne_glissante_rapide(valeurs, k):
    resultat = []
    somme_fenetre = sum(valeurs[:k])          # la première fenêtre
    resultat.append(somme_fenetre / k)
    for i in range(k, len(valeurs)):
        somme_fenetre += valeurs[i]           # la valeur qui entre
        somme_fenetre -= valeurs[i - k]       # la valeur qui sort
        resultat.append(somme_fenetre / k)
    return resultat


temperatures = [10, 12, 11, 13, 15, 14, 16, 18, 17]
print(moyenne_glissante_simple(temperatures, 3))
# => [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0]
print(moyenne_glissante_rapide(temperatures, 3))
# => [11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0]

# a) Pour chacun des n jours, on fait une slice et une somme de k valeurs :
#    O(n × k). Avec une fenêtre de 30 jours sur 10 ans de données, c'est 30
#    fois plus de travail que nécessaire.
# b) Chaque jour ne coûte que 2 opérations (un ajout, un retrait) : O(n),
#    quelle que soit la taille de la fenêtre.
# En pandas (cf. chap. 39 et 48), on écrirait simplement
# serie.rolling(3).mean(), qui utilise ce même principe.
