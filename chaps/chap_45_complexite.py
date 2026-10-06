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
#  Chap. 45     #  Complexité algorithmique                                    #
#               #                                                              #
################################################################################
#
#  - Pourquoi s'intéresser à la complexité ?
#  - Compter les opérations plutôt que les secondes
#  - La notation "grand O"
#  - Les grandes classes de complexité
#  - Analyser une boucle
#  - Complexité des opérations Python
#  - Recherche linéaire et recherche dichotomique
#  - Algorithmes de tri
#  - Récursivité et complexité
#  - Complexité en mémoire
#  - Mesurer pour de vrai : timeit et perf_counter
#  - Vectoriser avec numpy
#  - Règles pratiques
#  - En bref
#
#############################################

import math
import random
import sys
import time
import timeit


# Pourquoi s'intéresser à la complexité ?
##########################################

"""
Jusqu'ici, on s'est surtout demandé si un programme était CORRECT : est-ce
qu'il donne le bon résultat ? (cf. chap. 29 et 37 sur les tests)

Mais un programme correct peut être INUTILISABLE : s'il met trois jours à
traiter un fichier d'un million de lignes, il ne sert à rien. En Data Science,
où l'on manipule souvent de gros volumes de données, c'est une question
centrale.

La "complexité" d'un algorithme mesure la façon dont son coût (en temps ou en
mémoire) GRANDIT quand la taille des données grandit. On note généralement n
la taille des données (le nombre d'éléments d'une liste, de lignes d'un
fichier…).

Exemple : on veut savoir si une liste contient des doublons. Voici deux
fonctions correctes. Pour les comparer, elles renvoient leur réponse ET le
nombre d'opérations effectuées (des comparaisons, ici).
"""


def a_des_doublons_lent(valeurs):
    nb_operations = 0
    # On compare chaque élément à tous ceux qui sont après lui
    for i in range(len(valeurs)):
        for j in range(i + 1, len(valeurs)):
            nb_operations += 1
            if valeurs[i] == valeurs[j]:
                return True, nb_operations
    return False, nb_operations


def a_des_doublons_rapide(valeurs):
    nb_operations = 0
    deja_vus = set()          # un ensemble : cf. chap. 25
    for v in valeurs:
        nb_operations += 1
        if v in deja_vus:     # "in" sur un set est quasi instantané
            return True, nb_operations
        deja_vus.add(v)
    return False, nb_operations


valeurs = list(range(1000))   # 1000 valeurs, toutes différentes
print(a_des_doublons_lent(valeurs))    # => (False, 499500)
print(a_des_doublons_rapide(valeurs))  # => (False, 1000)

"""
Pour 1000 éléments, la première fonction fait 499 500 comparaisons, la
seconde 1000 : environ 500 fois moins !

Et l'écart se creuse quand n grandit. Pour un million d'éléments :
    - la version lente ferait environ 500 MILLIARDS de comparaisons, soit
      plusieurs heures de calcul en Python ;
    - la version rapide en ferait un million : une fraction de seconde.

IMPT : sur de petites données, presque tout algorithme est rapide. C'est sur
les GRANDES données que la complexité fait la différence.
"""


# Compter les opérations plutôt que les secondes
#################################################

"""
Pourquoi compter des opérations plutôt que mesurer des secondes ?

Parce que le temps d'exécution dépend de beaucoup de choses qui n'ont rien
à voir avec l'algorithme :
    - la puissance de l'ordinateur,
    - les autres programmes qui tournent en même temps,
    - la version de Python,
    - …et même le hasard : deux mesures successives diffèrent souvent.

Le NOMBRE d'opérations, lui, ne dépend que de l'algorithme et des données.
On compte en général les opérations "élémentaires" : une comparaison, une
addition, une affectation, un accès à un élément de liste…

Exemple : combien d'opérations pour calculer la somme d'une liste ?
"""


def somme(liste):
    total = 0              # 1 affectation
    for x in liste:        # la boucle tourne n fois…
        total = total + x  # … et fait 1 addition + 1 affectation par tour
    return total           # 1 retour


"""
Au total : environ 2n + 2 opérations. Pour n = 10 : 22 opérations, pour
n = 1000 : 2002 opérations.

On ne cherche pas à être précis à l'unité près : ce qui compte, c'est que le
nombre d'opérations est PROPORTIONNEL à n. Si la liste est deux fois plus
longue, la fonction travaille deux fois plus.
"""
print(somme([3, 1, 4, 1, 5]))  # => 14


# La notation "grand O"
########################

"""
Pour dire "le coût est proportionnel à n", les informaticiens écrivent :
    O(n)        (on lit "grand O de n")

La notation O garde seulement le terme qui grandit le plus vite, et oublie
les constantes multiplicatives :
    - 2n + 2         →  O(n)
    - 3n² + 5n + 100 →  O(n²)
    - 7              →  O(1)       (coût constant, indépendant de n)
    - n²/2           →  O(n²)

Pourquoi a-t-on le droit d'oublier tout ça ? Parce que, quand n devient
grand, le terme dominant écrase les autres. Vérifions :
"""
for n in [10, 100, 1000, 10000]:
    f = 3 * n ** 2 + 5 * n + 100
    part_n2 = 3 * n ** 2 / f * 100   # part du terme 3n² dans le total, en %
    print(f"n = {n:>5} : 3n²+5n+100 = {f:>11}, dont {part_n2:.2f} % pour 3n²")
# => n =    10 : 3n²+5n+100 =         450, dont 66.67 % pour 3n²
#    n =   100 : 3n²+5n+100 =       30600, dont 98.04 % pour 3n²
#    n =  1000 : 3n²+5n+100 =     3005100, dont 99.83 % pour 3n²
#    n = 10000 : 3n²+5n+100 =   300050100, dont 99.98 % pour 3n²

"""
Dès n = 1000, le terme 3n² représente plus de 99,8 % du total : les autres
termes sont négligeables.

Note : en toute rigueur, O(…) désigne une borne supérieure, et l'on distingue
le "pire cas", le "meilleur cas" et le "cas moyen". Sauf mention contraire,
quand on parle de complexité, on parle du PIRE CAS : c'est une garantie.
"""


# Les grandes classes de complexité
####################################

"""
Voici les complexités que l'on rencontre le plus souvent, de la meilleure à
la pire :

    O(1)        constante      accéder à liste[i], tester "x in un_set"
    O(log n)    logarithmique  recherche dichotomique dans une liste triée
    O(n)        linéaire       parcourir une liste, sum(), max(), "x in liste"
    O(n log n)  quasi-linéaire trier avec sorted()
    O(n²)       quadratique    deux boucles imbriquées sur les données
    O(2^n)      exponentielle  essayer toutes les combinaisons possibles

Rappel : log₂(n) est le nombre de fois qu'on peut diviser n par 2 avant
d'arriver à 1. Par exemple log₂(1024) = 10, car 1024 = 2¹⁰. Le logarithme
grandit TRÈS lentement : log₂(1 milliard) ≈ 30 seulement.

Calculons le nombre d'opérations pour différentes tailles n. Pour 2^n, le
nombre est si grand qu'on affiche seulement son nombre de chiffres.
"""
print(f"{'n':>9} | {'log n':>5} | {'n log n':>10} | {'n²':>15} | 2^n")
for n in [10, 100, 1000, 1_000_000]:
    log_n = math.log2(n)
    nb_chiffres_2n = int(n * math.log10(2)) + 1   # nombre de chiffres de 2^n
    print(f"{n:>9} | {log_n:>5.0f} | {n * log_n:>10.0f} | {n ** 2:>15} | "
          f"{nb_chiffres_2n} chiffres")
# =>         n | log n |    n log n |              n² | 2^n
#           10 |     3 |         33 |             100 | 4 chiffres
#          100 |     7 |        664 |           10000 | 31 chiffres
#         1000 |    10 |       9966 |         1000000 | 302 chiffres
#      1000000 |    20 |   19931569 |   1000000000000 | 301030 chiffres

"""
Lisons ce tableau pour n = 1 million :
    - O(log n) : 20 opérations. Instantané.
    - O(n) : 1 million. Une fraction de seconde en Python.
    - O(n log n) : 20 millions. Quelques secondes au pire.
    - O(n²) : 1000 milliards. Des heures, voire des jours.
    - O(2^n) : un nombre à 301 030 chiffres. L'univers n'y suffirait pas.

IMPT : un algorithme exponentiel est inutilisable dès que n dépasse quelques
dizaines. Un algorithme quadratique devient pénible au-delà de quelques
dizaines de milliers d'éléments.

Ces nombres sont si grands que Python lui-même refuse (depuis la version
3.11) de convertir en texte un entier de plus de 4300 chiffres, par sécurité :
"""
try:
    print(str(2 ** 20_000))   # 2^20000 a 6021 chiffres
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : Exceeds the limit
#    (4300 digits) for integer string conversion; use
#    sys.set_int_max_str_digits() to increase the limit)
# (Avant Python 3.11, la conversion fonctionne et affiche les 6021 chiffres.)


# Analyser une boucle
######################

"""
Pour trouver la complexité d'un programme, on regarde surtout ses BOUCLES :
combien de fois chaque instruction est-elle exécutée ?

Écrivons quelques fonctions qui comptent simplement leurs tours de boucle.
"""


def une_boucle(n):
    operations = 0
    for i in range(n):
        operations += 1
    return operations


def deux_boucles_imbriquees(n):
    operations = 0
    for i in range(n):
        for j in range(n):        # n tours… pour CHACUN des n tours de i
            operations += 1
    return operations


def boucle_triangulaire(n):
    operations = 0
    for i in range(n):
        for j in range(i):        # 0 tour, puis 1, puis 2… puis n-1
            operations += 1
    return operations


def boucle_par_moities(n):
    operations = 0
    while n > 1:
        n = n // 2                # on divise le problème par 2 à chaque tour
        operations += 1
    return operations


def deux_boucles_successives(n):
    operations = 0
    for i in range(n):
        operations += 1
    for i in range(n):            # cette boucle vient APRÈS la première
        operations += 1
    return operations


for n in [8, 16, 1024]:
    print(n, une_boucle(n), deux_boucles_imbriquees(n),
          boucle_triangulaire(n), boucle_par_moities(n),
          deux_boucles_successives(n))
# => 8 8 64 28 3 16
#    16 16 256 120 4 32
#    1024 1024 1048576 523776 10 2048

"""
Analysons chaque fonction :
    - une_boucle : n opérations → O(n).
    - deux_boucles_imbriquees : n × n opérations → O(n²). Quand n double
      (8 → 16), le travail est multiplié par 4 (64 → 256).
    - boucle_triangulaire : 0 + 1 + 2 + … + (n-1) = n(n-1)/2 opérations.
      C'est la moitié du carré… mais c'est toujours O(n²), car on oublie la
      constante 1/2. (C'est le cas de a_des_doublons_lent, plus haut.)
    - boucle_par_moities : on divise n par 2 à chaque tour : log₂(n) tours
      → O(log n). Pour n = 1024, seulement 10 tours !
    - deux_boucles_successives : n + n = 2n opérations → O(n). Deux boucles
      L'UNE APRÈS L'AUTRE s'additionnent (O(n) + O(n) = O(n)), alors que deux
      boucles L'UNE DANS L'AUTRE se multiplient (O(n) × O(n) = O(n²)).

IMPT : boucles successives → on additionne ; boucles imbriquées → on
multiplie.

Attention aux boucles CACHÉES : certaines instructions d'apparence anodine
contiennent elles-mêmes une boucle. Par exemple "x in liste" parcourt la
liste. Ce code a donc DEUX boucles imbriquées, même s'il n'a qu'un "for" :
"""


def elements_communs(liste_a, liste_b):
    communs = []
    for x in liste_a:          # n tours…
        if x in liste_b:       # … et "in" sur une liste parcourt liste_b !
            communs.append(x)
    return communs


print(elements_communs([1, 2, 3, 4], [3, 4, 5]))  # => [3, 4]
# Complexité : O(n × m), où n et m sont les tailles des deux listes. Avec
# set(liste_b), le "in" devient O(1) et la fonction passe en O(n + m).


# Complexité des opérations Python
###################################

"""
Pour analyser un programme, il faut connaître le coût des opérations de base
de Python. Voici les plus courantes (n = taille de la structure) :

    Listes (cf. chap. 16 et 24)
        liste[i], liste[i] = x, len(liste)      O(1)
        liste.append(x), liste.pop()            O(1)  (en fin de liste)
        liste.insert(0, x), liste.pop(0)        O(n)  (au début !)
        x in liste, liste.index(x)              O(n)
        liste.remove(x), del liste[i]           O(n)
        sorted(liste), liste.sort()             O(n log n)
        min(liste), max(liste), sum(liste)      O(n)
        liste[a:b] (slice, cf. chap. 31)        O(b - a) : on copie

    Dictionnaires et ensembles (cf. chap. 18, 25 et 27)
        d[cle], d[cle] = v, cle in d            O(1) en moyenne
        x in un_set, un_set.add(x)              O(1) en moyenne

    Strings (cf. chap. 7 et 8)
        len(s), s[i]                            O(1)
        sous_chaine in s, s.replace(…)          O(n)
        s1 + s2                                 O(len(s1) + len(s2))

Pourquoi insert(0, x) est-il coûteux ? Une liste Python range ses éléments
côte à côte en mémoire, comme des livres sur une étagère. Ajouter un livre au
BOUT de l'étagère est immédiat ; en ajouter un au DÉBUT oblige à décaler tous
les autres d'un cran. (Le module collections propose une "deque", optimisée
pour ajouter et retirer aux deux bouts en O(1) : cf. chap. 43.)

Pourquoi "in" est-il O(1) sur un set ou un dict ? Grâce au "hachage" (cf.
chap. 18) : Python calcule directement, à partir de la valeur, la case où
elle devrait se trouver. Pas besoin de tout parcourir. ("En moyenne", car
dans des cas très rares plusieurs valeurs tombent dans la même case.)

IMPT : si vous testez souvent "x in collection" sur de grandes données,
utilisez un set ou un dict, pas une liste.

Un piège classique : construire une longue chaîne par concaténations
successives. Chaque "+" crée une NOUVELLE chaîne et recopie tout ce qui a
déjà été construit (les strings sont immuables, cf. chap. 7). Le coût total
est donc 1 + 2 + 3 + … + n, soit O(n²) caractères recopiés dans le pire cas.
"""
mots = ["la", "complexité", "compte"]

phrase = ""
for mot in mots:
    phrase = phrase + mot + " "   # recopie toute la phrase à chaque tour
print(phrase.strip())             # => la complexité compte

phrase = " ".join(mots)           # une seule construction : O(n)
print(phrase)                     # => la complexité compte

"""
(En pratique, CPython optimise parfois la concaténation en boucle, mais il ne
faut pas compter dessus : " ".join() est la bonne façon de faire.)
"""


# Recherche linéaire et recherche dichotomique
###############################################

"""
Problème : trouver la position d'une valeur dans une liste.

1. La recherche "linéaire" (ou "séquentielle") : on regarde les éléments un
   par un, du début à la fin. C'est ce que font "in" et .index().
   Complexité : O(n). Dans le pire cas (valeur à la fin, ou absente), on
   regarde les n éléments.
"""


def recherche_lineaire(liste, cible):
    etapes = 0
    for i in range(len(liste)):
        etapes += 1
        if liste[i] == cible:
            return i, etapes       # trouvé : on renvoie la position
    return -1, etapes              # pas trouvé : -1 par convention


"""
2. La recherche "dichotomique" (ou "binaire") : si la liste est TRIÉE, on
   peut faire beaucoup mieux, comme quand on cherche un mot dans un
   dictionnaire papier :
       - on ouvre au milieu ;
       - si le mot cherché est avant, on recommence dans la moitié gauche,
         sinon dans la moitié droite ;
       - on continue jusqu'à trouver le mot (ou une zone vide).
   À chaque étape, on élimine LA MOITIÉ des candidats : il faut donc au plus
   log₂(n) étapes. Complexité : O(log n).
"""


def recherche_dichotomique(liste, cible):
    gauche = 0                    # la zone de recherche est
    droite = len(liste) - 1       # liste[gauche], …, liste[droite]
    etapes = 0
    while gauche <= droite:
        etapes += 1
        milieu = (gauche + droite) // 2
        if liste[milieu] == cible:
            return milieu, etapes
        elif liste[milieu] < cible:
            gauche = milieu + 1   # la cible est à droite du milieu
        else:
            droite = milieu - 1   # la cible est à gauche du milieu
    return -1, etapes


# Pas à pas sur une petite liste triée de 8 éléments :
petite = [2, 5, 8, 12, 16, 23, 38, 56]
print(recherche_dichotomique(petite, 23))  # => (5, 2)

"""
Déroulons la recherche de 23 :
    étape 1 : gauche = 0, droite = 7, milieu = 3 : petite[3] = 12 < 23
              → on cherche à droite : gauche = 4
    étape 2 : gauche = 4, droite = 7, milieu = 5 : petite[5] = 23 → trouvé !

Maintenant sur une grande liste : un million de nombres pairs, triés.
"""
nombres = list(range(0, 2_000_000, 2))     # 0, 2, 4, …, 1 999 998
print(len(nombres))                         # => 1000000

print(recherche_lineaire(nombres, 1_999_998))      # => (999999, 1000000)
print(recherche_dichotomique(nombres, 1_999_998))  # => (999999, 20)
print(recherche_lineaire(nombres, 7))              # => (-1, 1000000)
print(recherche_dichotomique(nombres, 7))          # => (-1, 20)

"""
Un million d'étapes contre 20 ! C'est toute la puissance du O(log n).

IMPT : la recherche dichotomique ne fonctionne QUE sur une liste triée. Sur
une liste en désordre, elle ne lève pas d'erreur… elle donne simplement un
résultat faux, ce qui est bien pire :
"""
desordre = [16, 2, 56, 8, 23, 5, 38, 12]
print(recherche_dichotomique(desordre, 5))   # => (-1, 3) : 5 est pourtant là !

"""
Trier coûte O(n log n) : cela ne vaut la peine que si l'on fait ensuite
BEAUCOUP de recherches dans la même liste. Pour une seule recherche, la
recherche linéaire en O(n) est meilleure.

Note : Python fournit la recherche dichotomique dans le module bisect
(bisect.bisect_left(liste, cible) renvoie la position où la cible est, ou
devrait être insérée).
"""


# Algorithmes de tri
#####################

"""
Trier est l'une des opérations les plus fréquentes en informatique. Il
existe des dizaines d'algorithmes de tri, de complexités différentes.

1. Le tri par sélection : on cherche le plus petit élément et on le met en
   première position ; puis on cherche le plus petit parmi les éléments
   restants et on le met en deuxième position ; etc.
"""


def tri_selection(liste):
    liste = liste.copy()          # on ne modifie pas la liste d'origine
    comparaisons = 0
    n = len(liste)
    for i in range(n):
        # On cherche l'indice du minimum dans liste[i:]
        i_min = i
        for j in range(i + 1, n):
            comparaisons += 1
            if liste[j] < liste[i_min]:
                i_min = j
        # On l'échange avec l'élément en position i (cf. chap. 17)
        liste[i], liste[i_min] = liste[i_min], liste[i]
    return liste, comparaisons


print(tri_selection([5, 3, 8, 1, 9, 2]))  # => ([1, 2, 3, 5, 8, 9], 15)

"""
Deux boucles imbriquées, la seconde "triangulaire" : (n-1) + (n-2) + … + 1
= n(n-1)/2 comparaisons. Pour n = 6 : 15. Complexité : O(n²), et ce quelles
que soient les données (même si la liste est déjà triée !).

2. Le tri par insertion : on prend les éléments un par un et on insère
   chacun à sa place parmi ceux déjà triés, comme on range des cartes dans
   sa main.
"""


def tri_insertion(liste):
    liste = liste.copy()
    comparaisons = 0
    for i in range(1, len(liste)):
        valeur = liste[i]
        j = i - 1
        # On décale vers la droite les éléments plus grands que valeur
        while j >= 0:
            comparaisons += 1
            if liste[j] > valeur:
                liste[j + 1] = liste[j]
                j -= 1
            else:
                break
        liste[j + 1] = valeur
    return liste, comparaisons


print(tri_insertion([5, 3, 8, 1, 9, 2]))       # => ([1, 2, 3, 5, 8, 9], 11)
print(tri_insertion([1, 2, 3, 4, 5, 6])[1])    # => 5  (déjà triée)
print(tri_insertion([6, 5, 4, 3, 2, 1])[1])    # => 15 (triée à l'envers)

"""
Le tri par insertion est O(n²) dans le pire cas (liste à l'envers), mais
seulement O(n) dans le meilleur cas (liste déjà triée) : n - 1 comparaisons.
C'est un bon exemple où le pire et le meilleur cas diffèrent.

3. sorted() et .sort() de Python utilisent "Timsort", un algorithme inventé
   en 2002 par Tim Peters pour Python. Il est en O(n log n) dans le pire cas,
   et très rapide sur des données "presque triées", fréquentes en pratique.

Comptons les comparaisons faites par sorted(). Astuce : on emballe chaque
nombre dans un objet dont la méthode __lt__ (le "<", cf. chap. 35) compte
ses appels.
"""


class NombreCompte:
    comparaisons = 0              # attribut de classe : cf. chap. 34

    def __init__(self, valeur):
        self.valeur = valeur

    def __lt__(self, autre):
        NombreCompte.comparaisons += 1
        return self.valeur < autre.valeur


random.seed(42)                   # pour des résultats reproductibles
donnees = list(range(1000))
random.shuffle(donnees)           # 1000 nombres dans le désordre

NombreCompte.comparaisons = 0
resultat = sorted(NombreCompte(x) for x in donnees)
print(NombreCompte.comparaisons)            # => 8655
print(tri_selection(donnees)[1])            # => 499500
print(tri_insertion(donnees)[1])            # => 249438

"""
Pour 1000 éléments : environ 8 650 comparaisons pour Timsort, contre près de
500 000 pour le tri par sélection et 250 000 pour le tri par insertion. Et
n log₂ n ≈ 9966 : on retrouve bien l'ordre de grandeur de O(n log n).

IMPT : n'écrivez pas vos propres algorithmes de tri dans un vrai programme :
utilisez sorted() ou .sort(). Les implémenter soi-même reste un excellent
exercice pour comprendre la complexité.

Note : on démontre qu'aucun tri qui ne fait que COMPARER des éléments ne peut
faire mieux que O(n log n) dans le pire cas. Timsort est donc optimal.
"""


# Récursivité et complexité
############################

"""
Au chap. 33, on a vu que la version naïve de Fibonacci recalcule sans cesse
les mêmes valeurs. Comptons ses appels :
"""
nb_appels = 0


def fib_naif(n):
    global nb_appels              # cf. chap. 19
    nb_appels += 1
    if n < 2:
        return n
    return fib_naif(n - 1) + fib_naif(n - 2)


for n in [10, 15, 20, 25]:
    nb_appels = 0
    resultat = fib_naif(n)
    print(f"fib({n}) = {resultat} en {nb_appels} appels")
# => fib(10) = 55 en 177 appels
#    fib(15) = 610 en 1973 appels
#    fib(20) = 6765 en 21891 appels
#    fib(25) = 75025 en 242785 appels

"""
Chaque fois que n augmente de 5, le nombre d'appels est multiplié par 11
environ. C'est une croissance EXPONENTIELLE : chaque appel en déclenche deux
autres. (Plus précisément, le nombre d'appels grandit comme 1,618^n, où
1,618 est le "nombre d'or".) fib_naif(50) demanderait des dizaines de
milliards d'appels.

Avec la mémoïsation (cf. chap. 33), chaque valeur n'est calculée qu'une
fois :
"""
memo = {}


def fib_memo(n):
    global nb_appels
    nb_appels += 1
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


for n in [10, 15, 20, 25]:
    nb_appels = 0
    memo = {}
    resultat = fib_memo(n)
    print(f"fib({n}) = {resultat} en {nb_appels} appels")
# => fib(10) = 55 en 19 appels
#    fib(15) = 610 en 29 appels
#    fib(20) = 6765 en 39 appels
#    fib(25) = 75025 en 49 appels

"""
Le nombre d'appels est maintenant 2n - 1 : la complexité passe de O(1,618^n)
à O(n). En échange, on utilise un dictionnaire de taille n : on a "acheté"
du temps avec de la mémoire.

Pour analyser une fonction récursive, on se demande :
    - combien d'appels récursifs fait chaque appel ? (un seul → souvent
      linéaire ; deux ou plus → risque d'explosion exponentielle)
    - de combien la taille du problème diminue-t-elle ? (de 1 → linéaire ;
      de moitié → logarithmique, comme la recherche dichotomique)
"""


# Complexité en mémoire
########################

"""
La complexité ne concerne pas que le temps : on mesure aussi la MÉMOIRE
utilisée, avec la même notation O.

    - a_des_doublons_lent utilise O(1) mémoire supplémentaire (quelques
      variables), mais O(n²) temps ;
    - a_des_doublons_rapide utilise O(n) mémoire (l'ensemble deja_vus),
      mais seulement O(n) temps.

C'est un compromis fréquent : on gagne du temps en stockant des résultats
intermédiaires.

Exemple : une liste stocke tous ses éléments en mémoire, alors qu'un
générateur (cf. chap. 36) les produit un par un, à la demande.
"""
liste_carres = [x ** 2 for x in range(1_000_000)]
generateur_carres = (x ** 2 for x in range(1_000_000))
print(sys.getsizeof(liste_carres))       # => 8448728 (variable)
print(sys.getsizeof(generateur_carres))  # => 208 (variable)
print(sum(liste_carres) == sum(generateur_carres))  # => True

"""
Environ 8 Mo pour la liste (et encore, sans compter les entiers eux-mêmes),
contre 200 octets pour le générateur, quelle que soit sa longueur : O(n)
contre O(1) en mémoire. (Les valeurs exactes dépendent de la version de
Python et de la machine.)

La récursivité consomme aussi de la mémoire : chaque appel en cours occupe
une place dans la "pile d'appels" (cf. chap. 33). fib_memo(n) empile n
appels : sa complexité en mémoire est O(n), et Python refuse d'aller au-delà
d'environ 1000 appels empilés :
"""
try:
    memo = {}
    fib_memo(5000)
except RecursionError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : maximum recursion
#    depth exceeded)
# (Le texte exact du message varie selon la version de Python.)


# Mesurer pour de vrai : timeit et perf_counter
################################################

"""
Compter les opérations donne la TENDANCE. Mais pour savoir combien de temps
prend VRAIMENT un programme, il faut le mesurer. Python fournit deux outils
(cf. chap. 22 et 30) :

    - time.perf_counter() : un chronomètre très précis. On le lit avant et
      après le code, et on fait la différence.
    - timeit.timeit(fonction, number=k) : exécute k fois la fonction et
      renvoie le temps total. Répéter la mesure la rend plus fiable.

IMPT : les temps affichés ci-dessous VARIENT d'une machine et d'une
exécution à l'autre. Ce qui compte, ce sont les RAPPORTS entre les temps.
"""
n = 100_000
grande_liste = list(range(n))
grand_set = set(grande_liste)
cible = n - 1                     # le pire cas pour la liste : le dernier

# lambda : cf. chap. 32
temps_liste = timeit.timeit(lambda: cible in grande_liste, number=200)
temps_set = timeit.timeit(lambda: cible in grand_set, number=200)
print(f"in sur la liste : {temps_liste:.4f} s")  # => in sur la liste :
#                                                     0.1531 s (variable)
print(f"in sur le set   : {temps_set:.6f} s")    # => in sur le set   :
#                                                     0.000005 s (variable)
print(temps_liste > temps_set)                   # => True

# Avec perf_counter : comparons nos deux recherches de doublons
valeurs = list(range(3000))

debut = time.perf_counter()
a_des_doublons_lent(valeurs)
duree_lent = time.perf_counter() - debut

debut = time.perf_counter()
a_des_doublons_rapide(valeurs)
duree_rapide = time.perf_counter() - debut

print(f"lent : {duree_lent:.3f} s, rapide : {duree_rapide:.5f} s")
# => lent : 0.180 s, rapide : 0.00012 s (variable)
print(duree_lent > duree_rapide)  # => True

"""
Bonnes pratiques de mesure :
    - mesurez plusieurs fois (timeit le fait pour vous) ;
    - mesurez sur des données de taille RÉALISTE ;
    - essayez plusieurs tailles (n, 2n, 4n…) : si le temps double quand n
      double, c'est sans doute du O(n) ; s'il est multiplié par 4, du O(n²).

Dans un notebook Jupyter (cf. chap. 2), la commande magique %timeit fait
tout cela automatiquement : %timeit sorted(grande_liste)
"""


# Vectoriser avec numpy
########################

"""
Une même complexité peut cacher des temps très différents : la notation O
ignore les constantes, mais en pratique, une constante 100 fois plus petite
fait une vraie différence !

C'est ce qu'apporte numpy (cf. chap. 38) : une opération "vectorisée" comme
tableau ** 2 reste en O(n) (il faut bien traiter chaque élément), mais la
boucle est faite en C, des dizaines de fois plus vite qu'une boucle Python.
"""
try:
    import numpy as np
except ImportError:
    np = None
    print("numpy n'est pas installé : cette section est sautée.")
    print("Pour l'installer : uv add numpy (ou : python3 -m pip install numpy)")

if np is not None:
    valeurs_py = list(range(1_000_000))
    valeurs_np = np.arange(1_000_000)

    def somme_carres_python():
        return sum(x * x for x in valeurs_py)

    def somme_carres_numpy():
        return int((valeurs_np * valeurs_np).sum())

    print(somme_carres_python() == somme_carres_numpy())  # => True
    t_py = timeit.timeit(somme_carres_python, number=3)
    t_np = timeit.timeit(somme_carres_numpy, number=3)
    print(f"numpy est environ {t_py / t_np:.0f} fois plus rapide")
    # => numpy est environ 40 fois plus rapide (variable)

"""
Les deux versions sont O(n), mais numpy gagne largement grâce à sa
constante. En Data Science, la règle d'or est donc : évitez les boucles
Python sur de gros volumes, préférez les opérations vectorisées de numpy et
de pandas (cf. chap. 39).
"""


# Règles pratiques
###################

"""
1. D'abord un programme CORRECT et LISIBLE, ensuite un programme rapide.
   "L'optimisation prématurée est la source de tous les maux" (Donald Knuth).
   N'optimisez que ce qui est réellement lent… et mesurez avant !

2. Le choix de la STRUCTURE DE DONNÉES est souvent la meilleure optimisation :
   remplacer une liste par un set ou un dict pour les recherches transforme
   un O(n) en O(1), et un programme O(n²) en O(n).

3. Méfiez-vous des boucles cachées : "in" sur une liste, .index(), .remove(),
   .insert(0, …), .pop(0), les slices, les concaténations de strings…
   placés dans une boucle, ils donnent du O(n²).

4. Utilisez les outils fournis : sorted(), min(), max(), sum(), les sets,
   les dicts, le module collections (cf. chap. 43), bisect, numpy, pandas.
   Ils sont écrits en C et optimisés depuis des années.

5. Retenez les ordres de grandeur : en Python, comptez environ 10 à 100
   millions d'opérations simples par seconde. Pour n = 1 million :
   O(n) ou O(n log n) passe ; O(n²) ne passe pas.

6. Évitez les algorithmes exponentiels (essayer toutes les combinaisons…)
   dès que n dépasse 20 ou 30.
"""


# En bref
##########

"""
    - La complexité décrit comment le coût d'un algorithme GRANDIT avec la
      taille n des données. On compte des opérations, pas des secondes.
    - Notation O : on garde le terme dominant, sans les constantes
      (3n² + 5n + 100 → O(n²)). On parle du pire cas, sauf mention contraire.
    - Classes : O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n).
    - Boucles successives : on additionne. Boucles imbriquées : on multiplie.
    - "x in liste" est O(n), "x in set" et "cle in dict" sont O(1).
    - Recherche dichotomique : O(log n), mais seulement sur une liste triée.
    - Trier avec sorted() : O(n log n). Les tris "naïfs" sont en O(n²).
    - La mémoïsation transforme une récursivité exponentielle en O(n).
    - La mémoire a aussi une complexité : un générateur est O(1), une liste
      O(n).
    - Mesurez avec timeit et perf_counter ; vectorisez avec numpy.
"""
