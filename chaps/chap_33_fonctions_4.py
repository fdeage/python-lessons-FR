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
#  Chap. 33     #  Fonctions IV : la récursivité                               #
#               #                                                              #
################################################################################
#
#  - Une fonction qui s'appelle elle-même
#  - Le cas de base
#  - La pile d'appels, pas à pas
#  - Exemple classique : la factorielle
#  - Récursivité sur les listes et les chaînes
#  - Parcourir des données imbriquées
#  - Fibonacci : le piège des calculs répétés
#  - Mémoïser avec un dictionnaire
#  - RecursionError et limite de récursion
#  - Récursif ou itératif ?
#  - En bref
#
#############################################

# Une fonction qui s'appelle elle-même
#######################################

"""
On sait qu'une fonction peut en appeler une autre (cf. chap. 15). Rien
n'empêche une fonction de s'appeler… ELLE-MÊME ! On parle alors de fonction
"récursive", et de "récursivité".

L'idée : pour résoudre un gros problème, on le ramène à une version PLUS
PETITE du même problème, que l'on résout de la même façon… jusqu'à tomber
sur un problème si petit que la réponse est évidente.

Exemple de la vie courante : compter les personnes dans une file d'attente.
Vous ne voyez pas le bout de la file, alors vous demandez à la personne
devant vous : "combien y a-t-il de personnes devant toi ?". Elle pose la
même question à la personne devant elle, et ainsi de suite… La toute
première personne, qui n'a personne devant elle, répond "0". Chacun ajoute
alors 1 à la réponse reçue et la transmet à la personne derrière.

Premier exemple en Python : un compte à rebours.
"""


def compte_a_rebours(n):
    if n == 0:
        print("Décollage !")
    else:
        print(n)
        compte_a_rebours(n - 1)   # appel récursif, avec un n plus petit


compte_a_rebours(3)
# => 3
#    2
#    1
#    Décollage !

"""
Déroulons :
    compte_a_rebours(3) affiche 3, puis appelle compte_a_rebours(2),
    qui affiche 2, puis appelle compte_a_rebours(1),
    qui affiche 1, puis appelle compte_a_rebours(0),
    qui affiche "Décollage !" et NE S'APPELLE PLUS : c'est fini.

On aurait évidemment pu écrire ce programme avec une boucle while (cf. chap.
13). Mais certains problèmes sont BEAUCOUP plus simples à exprimer de façon
récursive, comme on le verra avec les données imbriquées.
"""


# Le cas de base
#################

"""
Toute fonction récursive doit contenir deux ingrédients : IMPT

    1. un CAS DE BASE (ou "condition d'arrêt") : un cas simple où la
       fonction renvoie un résultat directement, SANS s'appeler ;
    2. un APPEL RÉCURSIF sur un problème PLUS PETIT, qui se rapproche du
       cas de base à chaque fois.

Si l'un des deux manque, la fonction s'appelle à l'infini (on verra plus
bas ce qui se passe alors).

Exemple : la somme des entiers de 1 à n.
    somme(n) = n + somme(n - 1)    (appel récursif sur un problème plus petit)
    somme(0) = 0                   (cas de base)
"""


def somme_jusqua(n):
    if n == 0:                       # 1. cas de base
        return 0
    return n + somme_jusqua(n - 1)   # 2. appel récursif


print(somme_jusqua(4))    # => 10   (4 + 3 + 2 + 1 + 0)
print(somme_jusqua(100))  # => 5050

"""
Méthode pour écrire une fonction récursive (à appliquer à chaque fois !) :
    1. Quel est le cas le plus simple, dont je connais la réponse ?
       → c'est le cas de base (souvent : 0, 1, liste vide, chaîne vide).
    2. Si je SUPPOSE que la fonction marche déjà pour un problème un peu
       plus petit, comment j'en déduis la réponse pour le problème actuel ?
       → c'est l'appel récursif.
    3. Est-ce que chaque appel se rapproche bien du cas de base ?

Le point 2 demande un petit acte de foi : on fait confiance à l'appel
récursif, sans essayer de le dérouler entièrement dans sa tête.

Attention aux cas de base trop étroits : somme_jusqua(-1) appellerait
somme_jusqua(-2), puis -3… sans jamais atteindre 0 ! Une version plus
robuste utilise "n <= 0" comme cas de base.
"""


# La pile d'appels, pas à pas
##############################

"""
Comment Python s'y retrouve-t-il, avec toutes ces fonctions "en cours" en
même temps ? Chaque appel de fonction a ses PROPRES variables locales
(cf. chap. 19) : le n de somme_jusqua(4) n'est pas le même que celui de
somme_jusqua(3).

Python range ces appels en cours dans une "pile d'appels" (call stack),
comme une pile d'assiettes : chaque nouvel appel est posé au-dessus ; quand
un appel se termine (return), on l'enlève, et on reprend celui du dessous,
là où il s'était arrêté. IMPT

Ajoutons des print() (avec un décalage proportionnel à la profondeur) pour
VOIR la pile grandir puis se vider :
"""


def somme_tracee(n, profondeur=0):
    decalage = "    " * profondeur
    print(f"{decalage}appel somme({n})")
    if n == 0:
        print(f"{decalage}cas de base : renvoie 0")
        return 0
    resultat = n + somme_tracee(n - 1, profondeur + 1)
    print(f"{decalage}somme({n}) renvoie {n} + somme({n - 1}) = {resultat}")
    return resultat


somme_tracee(3)
# => appel somme(3)
#        appel somme(2)
#            appel somme(1)
#                appel somme(0)
#                cas de base : renvoie 0
#            somme(1) renvoie 1 + somme(0) = 1
#        somme(2) renvoie 2 + somme(1) = 3
#    somme(3) renvoie 3 + somme(2) = 6

"""
Lisez la trace de haut en bas :
    - à la DESCENTE, chaque appel attend le résultat du suivant : aucun
      calcul n'est encore fait, les additions sont "en suspens" ;
    - au cas de base, on obtient enfin une valeur (0) ;
    - à la REMONTÉE, chaque appel termine son addition et renvoie son
      résultat à celui qui l'a appelé.

La pile ressemble à ceci au moment le plus profond :

    ┌────────────────────────┐
    │ somme(0) → renvoie 0   │  ← sommet de la pile (appel en cours)
    ├────────────────────────┤
    │ somme(1) attend…       │
    ├────────────────────────┤
    │ somme(2) attend…       │
    ├────────────────────────┤
    │ somme(3) attend…       │
    ├────────────────────────┤
    │ programme principal    │
    └────────────────────────┘

C'est cette même pile que l'on voit dans un traceback (cf. chap. 26) : la
liste des fonctions en cours au moment de l'erreur !
"""


# Exemple classique : la factorielle
#####################################

"""
La factorielle de n, notée n!, est le produit des entiers de 1 à n :
    5! = 5 × 4 × 3 × 2 × 1 = 120
Par convention, 0! = 1. (Elle sert en probabilités : n! est le nombre de
façons de ranger n objets.)

On remarque que 5! = 5 × 4!, et plus généralement n! = n × (n - 1)! :
c'est une définition récursive toute trouvée.
"""


def factorielle(n):
    if n <= 1:                         # cas de base : 0! = 1! = 1
        return 1
    return n * factorielle(n - 1)      # appel récursif


print(factorielle(0))   # => 1
print(factorielle(5))   # => 120
print(factorielle(20))  # => 2432902008176640000
"""
Les entiers Python n'ayant pas de limite de taille (cf. chap. 4), on peut
calculer de très grandes factorielles :
"""
print(len(str(factorielle(100))))  # => 158 (chiffres !)

"""
Le module math propose déjà math.factorial() (cf. chap. 22) : en pratique,
utilisez-la. L'intérêt ici est de comprendre le mécanisme.
"""
import math  # noqa: E402 (import en milieu de fichier, pour le cours)

print(math.factorial(5) == factorielle(5))  # => True

"""
Autre exemple : la puissance, avec puissance(x, n) = x × puissance(x, n-1)
et puissance(x, 0) = 1.
"""


def puissance(x, n):
    if n == 0:
        return 1
    return x * puissance(x, n - 1)


print(puissance(2, 10))  # => 1024
print(puissance(3, 0))   # => 1


# Récursivité sur les listes et les chaînes
############################################

"""
Les listes et les chaînes se prêtent bien à la récursivité, grâce aux
slices (cf. chap. 31) : une liste, c'est son PREMIER élément suivi du
RESTE de la liste (qui est une liste plus petite).

    [3, 1, 4]  =  3  suivi de  [1, 4]
    liste[0]   →  le premier élément
    liste[1:]  →  le reste (une liste plus courte d'un élément)

Cas de base typique : la liste vide (ou la chaîne vide).
"""


def somme_liste(liste):
    if len(liste) == 0:       # cas de base : la somme d'une liste vide vaut 0
        return 0
    return liste[0] + somme_liste(liste[1:])


print(somme_liste([3, 1, 4, 1, 5]))  # => 14
print(somme_liste([]))               # => 0


def plus_grand(liste):
    if len(liste) == 1:       # cas de base : un seul élément, c'est le max
        return liste[0]
    max_du_reste = plus_grand(liste[1:])
    return liste[0] if liste[0] > max_du_reste else max_du_reste


print(plus_grand([3, 17, 4, 9]))  # => 17

"""
Avec les chaînes, même principe. Inverser une chaîne : on inverse le reste,
et on met le premier caractère à la fin.
"""


def inverser(texte):
    if texte == "":
        return ""
    return inverser(texte[1:]) + texte[0]


print(inverser("Python"))  # => nohtyP

"""
Un palindrome se lit pareil dans les deux sens ("kayak", "radar"). Version
récursive : une chaîne est un palindrome si sa première et sa dernière
lettre sont identiques ET si le "milieu" est un palindrome. Cas de base :
une chaîne de 0 ou 1 caractère est toujours un palindrome.
"""


def est_palindrome(mot):
    if len(mot) <= 1:
        return True
    if mot[0] != mot[-1]:
        return False             # 2e cas de base : on sait déjà que c'est faux
    return est_palindrome(mot[1:-1])


print(est_palindrome("kayak"))   # => True
print(est_palindrome("python"))  # => False
print(est_palindrome("radar"))   # => True

"""
Ces exemples sont pédagogiques : en vrai, on écrirait sum(liste),
max(liste), texte[::-1] et mot == mot[::-1]. De plus, chaque liste[1:]
crée une COPIE de la liste (cf. chap. 31), ce qui est lent pour de grandes
listes. Mais ils entraînent à "penser récursif", ce qui sera indispensable
pour la section suivante.
"""


# Parcourir des données imbriquées
###################################

"""
Voici où la récursivité devient vraiment utile : les données IMBRIQUÉES,
dont on ne connaît pas la profondeur à l'avance. Exemples réels :
    - des dossiers qui contiennent des fichiers et d'autres dossiers,
    - des données JSON (cf. chap. 22 et 28) : des dictionnaires qui
      contiennent des listes qui contiennent des dictionnaires…
    - un arbre généalogique, un organigramme, un menu à sous-menus…

Avec des boucles, il faudrait une boucle imbriquée par niveau… mais combien
de niveaux ? Avec la récursivité, c'est naturel : pour chaque élément, si
c'est une liste, on la traite de la même façon (appel récursif) ; sinon,
c'est un nombre (cas de base).

isinstance(valeur, list) teste si une valeur est une liste (on peut aussi
écrire type(valeur) == list, cf. chap. 6).
"""


def somme_imbriquee(donnees):
    total = 0
    for element in donnees:
        if isinstance(element, list):
            total += somme_imbriquee(element)   # sous-liste : récursion
        else:
            total += element                    # nombre : cas de base
    return total


mesures = [1, [2, 3], [4, [5, 6, [7]]], 8]
print(somme_imbriquee(mesures))  # => 36


def aplatir(donnees):
    """Renvoie une liste "plate" de tous les éléments, quelle que soit
    la profondeur d'imbrication."""
    resultat = []
    for element in donnees:
        if isinstance(element, list):
            resultat.extend(aplatir(element))
        else:
            resultat.append(element)
    return resultat


print(aplatir(mesures))  # => [1, 2, 3, 4, 5, 6, 7, 8]


def profondeur(donnees):
    """Nombre de niveaux de listes imbriquées."""
    if not isinstance(donnees, list):
        return 0
    if len(donnees) == 0:
        return 1
    return 1 + max(profondeur(element) for element in donnees)


print(profondeur(mesures))  # => 4
print(profondeur([1, 2]))   # => 1

"""
Exemple "données" : une arborescence de dossiers, représentée par des
dictionnaires (nom → taille en Ko pour un fichier, nom → dictionnaire pour
un sous-dossier). On calcule la taille totale :
"""
disque = {
    "notes.txt": 4,
    "photos": {
        "vacances.jpg": 2048,
        "chat.png": 512,
        "2023": {"neige.jpg": 1024},
    },
    "projets": {
        "python": {"chap_33.py": 20, "data.csv": 300},
        "vide": {},
    },
}


def taille_totale(dossier):
    total = 0
    for nom, contenu in dossier.items():
        if isinstance(contenu, dict):
            total += taille_totale(contenu)   # sous-dossier : récursion
        else:
            total += contenu                  # fichier : sa taille
    return total


print(taille_totale(disque))             # => 3908
print(taille_totale(disque["photos"]))   # => 3584


def afficher_arbre(dossier, niveau=0):
    for nom, contenu in dossier.items():
        if isinstance(contenu, dict):
            print("    " * niveau + nom + "/")
            afficher_arbre(contenu, niveau + 1)
        else:
            print("    " * niveau + f"{nom} ({contenu} Ko)")


afficher_arbre(disque)
# => notes.txt (4 Ko)
#    photos/
#        vacances.jpg (2048 Ko)
#        chat.png (512 Ko)
#        2023/
#            neige.jpg (1024 Ko)
#    projets/
#        python/
#            chap_33.py (20 Ko)
#            data.csv (300 Ko)
#        vide/


# Fibonacci : le piège des calculs répétés
###########################################

"""
La suite de Fibonacci commence par 0 et 1, puis chaque nombre est la somme
des deux précédents :
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
Soit : fib(0) = 0, fib(1) = 1, et fib(n) = fib(n - 1) + fib(n - 2).

La traduction récursive est immédiate, avec DEUX appels récursifs :
"""


def fib(n):
    if n < 2:              # cas de base : fib(0) = 0 et fib(1) = 1
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(11)])  # => [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

"""
Ça marche… mais c'est TRÈS lent dès que n grandit. Pourquoi ? Dessinons les
appels pour fib(5) :

                          fib(5)
                ┌───────────┴───────────┐
              fib(4)                  fib(3)
           ┌────┴────┐              ┌───┴───┐
         fib(3)    fib(2)         fib(2)  fib(1)
        ┌──┴──┐    ┌──┴──┐       ┌──┴──┐
     fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
     ┌──┴──┐
  fib(1) fib(0)

fib(3) est calculé 2 fois, fib(2) 3 fois… Le même travail est refait encore
et encore ! Comptons les appels avec une variable globale (cf. chap. 19) :
"""
nb_appels = 0


def fib_compte(n):
    global nb_appels
    nb_appels += 1
    if n < 2:
        return n
    return fib_compte(n - 1) + fib_compte(n - 2)


for n in [5, 10, 20, 25]:
    nb_appels = 0
    fib_compte(n)
    print(f"fib({n}) : {nb_appels} appels")
# => fib(5) : 15 appels
#    fib(10) : 177 appels
#    fib(20) : 21891 appels
#    fib(25) : 242785 appels

"""
Le nombre d'appels explose (il est multiplié par environ 1,6 à chaque fois
que n augmente de 1) : fib(40) demanderait plus de 300 millions d'appels,
et fib(100) des milliards d'années ! IMPT : une récursivité avec plusieurs
appels sur des sous-problèmes qui se recoupent peut devenir catastrophique.
"""


# Mémoïser avec un dictionnaire
################################

# (On mesure précisément ce gain au chap. 45 : complexité exponentielle contre
# linéaire.)

"""
Solution : se SOUVENIR des résultats déjà calculés, pour ne jamais les
recalculer. On les range dans un dictionnaire (cf. chap. 18) : la clé est n,
la valeur est fib(n). Cette technique s'appelle la "mémoïsation" (de
"mémo", pas "mémorisation" !).

Avant de calculer, on regarde dans le dictionnaire : si la réponse y est,
on la renvoie directement.
"""
memo = {}


def fib_memo(n):
    if n in memo:            # déjà calculé : on le renvoie directement
        return memo[n]
    if n < 2:
        resultat = n
    else:
        resultat = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = resultat       # on note le résultat pour la prochaine fois
    return resultat


print(fib_memo(10))   # => 55
print(fib_memo(100))  # => 354224848179261915075 (instantané !)
print(len(memo))      # => 101 (fib(0) à fib(100) : chacun calculé UNE fois)

"""
Chaque fib(k) n'est plus calculé qu'une seule fois : on passe de milliards
d'appels à environ 200.

Bonus : Python fournit un outil tout fait qui mémoïse automatiquement une
fonction : functools.lru_cache (ou functools.cache depuis Python 3.9). Il
s'utilise avec la syntaxe "@", celle des décorateurs, que l'on verra au
chap. 36 :

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(n):
        …
"""


# RecursionError et limite de récursion
########################################

"""
Que se passe-t-il si une fonction s'appelle sans fin (cas de base oublié,
ou jamais atteint) ? La pile d'appels grandit, grandit… Pour éviter de
saturer la mémoire, Python fixe une limite au nombre d'appels imbriqués.
Au-delà, il lève une RecursionError (cf. chap. 26).
"""
import sys  # noqa: E402

print(sys.getrecursionlimit())  # => 1000 (valeur par défaut, peut varier)


def sans_fin(n):
    return sans_fin(n + 1)   # aucun cas de base !


try:
    sans_fin(0)
except RecursionError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Même avec un cas de base correct, une récursion TROP PROFONDE déclenche la
même erreur : somme_jusqua(5000) demanderait 5000 appels imbriqués.
"""
try:
    somme_jusqua(5000)
except RecursionError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Et une erreur de cas de base, déjà évoquée : somme_jusqua(-1) ne
s'arrête jamais, puisque n s'éloigne de 0 au lieu de s'en rapprocher.
"""
try:
    somme_jusqua(-1)
except RecursionError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
On PEUT augmenter la limite avec sys.setrecursionlimit(10000), mais c'est
rarement une bonne idée : au-delà d'une certaine profondeur, c'est le
programme entier qui peut planter brutalement. Si vous avez besoin de plus
de quelques centaines de niveaux, préférez une boucle.

À retenir : en Python, la récursivité convient aux problèmes de profondeur
raisonnable (arbres, données imbriquées), pas aux longues répétitions.
"""


# Récursif ou itératif ?
#########################

"""
Tout programme récursif peut être réécrit avec des boucles (on dit
"itératif"), et inversement. Comparons, pour la factorielle :
"""


def factorielle_iterative(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


print(factorielle_iterative(5))  # => 120


# Et Fibonacci, en itératif : on garde seulement les deux derniers nombres
def fib_iteratif(n):
    a, b = 0, 1                  # fib(0), fib(1)
    for _ in range(n):
        a, b = b, a + b          # on avance d'un cran (cf. chap. 17)
    return a


print(fib_iteratif(10))   # => 55
print(fib_iteratif(100))  # => 354224848179261915075

"""
Comment choisir ?

    Récursif                              Itératif
    ─────────────────────────────────     ─────────────────────────────────
    + élégant quand le problème est       + plus rapide en Python (un appel
      lui-même récursif (arbres, données    de fonction coûte cher)
      imbriquées, "diviser pour régner")  + pas de limite de profondeur
    + souvent plus court et plus proche   + plus facile à suivre pas à pas
      de la définition mathématique         pour un débutant
    − limité à ~1000 niveaux
    − risque de calculs répétés (fib)

Règle pratique :
    - une simple répétition (compter, sommer, parcourir une liste plate) :
      une boucle ;
    - une structure imbriquée de profondeur inconnue (dossiers, JSON,
      arbres) : la récursivité.
"""


# En bref
##########

"""
    def f(n):
        if <cas simple>:            # 1. cas de base : réponse directe
            return <valeur>
        return … f(<plus petit>) …  # 2. appel récursif qui s'en rapproche

    - Chaque appel a ses propres variables locales, rangées dans la pile
      d'appels ; les calculs se font à la REMONTÉE.
    - Listes / chaînes : traiter liste[0], puis récurser sur liste[1:].
    - Données imbriquées : si l'élément est une liste (isinstance), on
      récurse, sinon c'est le cas de base.
    - Plusieurs appels sur des sous-problèmes communs (fib) : mémoïser avec
      un dictionnaire.
    - Limite ≈ 1000 appels imbriqués : RecursionError au-delà.
    - Répétition simple → boucle ; structure imbriquée → récursivité.
"""
