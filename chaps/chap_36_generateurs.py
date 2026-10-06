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
#  Chap. 36     #  Générateurs (et décorateurs)                                #
#               #                                                              #
################################################################################
#
#  - Rappel : itérables et itérateurs
#  - Les fonctions génératrices : "yield"
#  - Pas à pas : une exécution suspendue
#  - Un générateur s'épuise
#  - Générateurs infinis
#  - Évaluation paresseuse et mémoire
#  - Pipelines de générateurs
#  - Déléguer avec "yield from"
#  - Expressions génératrices
#  - Bonus : les décorateurs
#  - Bonus : "with" et les gestionnaires de contexte
#
##########################################################

import os
import sys
import time
import itertools
import functools
import contextlib


# Rappel : itérables et itérateurs
###################################

"""
Au chap. 23, on a vu qu'un "itérable" est un objet que l'on peut parcourir
avec une boucle for : liste, tuple, string, dictionnaire, ensemble, range,
fichier…

On a aussi vu ce que fait for "en coulisses" :
    1. il demande un "itérateur" à l'itérable avec iter(),
    2. il appelle next() sur cet itérateur pour obtenir chaque élément,
    3. il s'arrête quand next() soulève l'erreur StopIteration.
"""
fruits = ["pomme", "kiwi", "poire"]
it = iter(fruits)       # on fabrique un itérateur à partir de la liste
print(next(it))         # => pomme
print(next(it))         # => kiwi
print(next(it))         # => poire
try:
    next(it)            # plus rien à donner…
except StopIteration:
    print("1: (Sans ce try: … except …, cette ligne créerait : StopIteration)")

"""
IMPT : un itérateur est un objet qui "se souvient" d'où il en est, et qui
donne les éléments UN PAR UN, à la demande.

Question : comment écrire NOUS-MÊMES un itérateur, qui calcule ses éléments
au fur et à mesure ? Réponse : avec une fonction génératrice.
"""


# Les fonctions génératrices : "yield"
#######################################

"""
Une fonction génératrice ressemble à une fonction normale (cf. chap. 14),
mais elle utilise le mot-clé "yield" (en anglais : "produire", "céder")
au lieu de (ou en plus de) "return".

    def ma_fonction():          def mon_generateur():
        return 1                    yield 1
                                    yield 2
                                    yield 3

La différence est énorme :
    - "return" renvoie UNE valeur et TERMINE la fonction ;
    - "yield" renvoie une valeur et MET LA FONCTION EN PAUSE. Au prochain
      next(), la fonction reprend exactement là où elle s'était arrêtée,
      avec toutes ses variables locales intactes.
"""
def un_deux_trois():
    yield 1
    yield 2
    yield 3


# IMPT : appeler une fonction génératrice n'exécute PAS son code ! Cela crée
# un objet "générateur", qui est un itérateur.
gen = un_deux_trois()
print(type(gen))        # => <class 'generator'>
print(next(gen))        # => 1
print(next(gen))        # => 2
print(next(gen))        # => 3

# Comme c'est un itérateur, on peut le parcourir avec for (qui s'occupe des
# next() et de StopIteration pour nous) :
for nombre in un_deux_trois():
    print(nombre, end=" ")
print()                 # => 1 2 3

# …ou le transformer en liste, en tuple, etc. :
print(list(un_deux_trois()))   # => [1, 2, 3]
print(sum(un_deux_trois()))    # => 6

"""
En pratique, yield est presque toujours dans une boucle. Voici notre propre
version de range(), qui produit les nombres de debut (inclus) à fin (exclu) :
"""
def mon_range(debut, fin, pas=1):
    n = debut
    while n < fin:
        yield n         # on "cède" n, puis on attend le next() suivant
        n += pas        # …et on reprend ici


print(list(mon_range(0, 10, 3)))   # => [0, 3, 6, 9]

"""
Exemple plus "données" : produire uniquement les valeurs valides d'une liste
de mesures (on ignore les None et les valeurs négatives, qui sont des
erreurs de capteur).
"""
def mesures_valides(mesures):
    for m in mesures:
        if m is not None and m >= 0:
            yield m


releves = [12.5, None, 13.1, -999, 14.0, None, 12.8]
print(list(mesures_valides(releves)))  # => [12.5, 13.1, 14.0, 12.8]

"""
On aurait pu faire la même chose avec une liste et .append() :

    def mesures_valides_liste(mesures):
        resultat = []
        for m in mesures:
            if m is not None and m >= 0:
                resultat.append(m)
        return resultat

La version avec yield est plus courte (pas de liste intermédiaire à gérer)
et, on le verra plus bas, elle ne crée jamais toute la liste en mémoire.

Note : une fonction génératrice peut aussi contenir "return" (sans valeur) :
il termine le générateur, exactement comme si on arrivait à la fin de la
fonction. Le next() suivant soulève alors StopIteration.
"""
def jusqu_a_zero(nombres):
    for n in nombres:
        if n == 0:
            return      # fin du générateur
        yield n


print(list(jusqu_a_zero([4, 7, 0, 5, 2])))  # => [4, 7]


# Pas à pas : une exécution suspendue
######################################

"""
Pour bien voir ce qui se passe, ajoutons des print() dans un générateur, et
appelons next() à la main. Faites "tourner" le programme dans votre tête
avant de regarder la sortie (cf. chap. 1) !
"""
def bavard():
    print("  [début de la fonction]")
    yield "A"
    print("  [reprise après A]")
    yield "B"
    print("  [reprise après B, fin de la fonction]")


g = bavard()            # n'affiche RIEN : le code n'a pas encore démarré
print("générateur créé")
# => générateur créé

print(next(g))
# =>   [début de la fonction]
# => A

print(next(g))
# =>   [reprise après A]
# => B

try:
    next(g)             # la fonction reprend après B, puis se termine
except StopIteration:
    print("2: (Sans ce try: … except …, cette ligne créerait : StopIteration)")
# =>   [reprise après B, fin de la fonction]
# => 2: (Sans ce try: … except …, cette ligne créerait : StopIteration)

"""
Récapitulons ce "film" :

    instruction       ce qui s'exécute dans bavard()          valeur reçue
    ---------------   -------------------------------------   ------------
    g = bavard()      rien du tout                            (générateur)
    next(g)           du début jusqu'au 1er yield (inclus)    "A"
    next(g)           du 1er yield jusqu'au 2e yield          "B"
    next(g)           du 2e yield jusqu'à la fin              StopIteration

IMPT : entre deux next(), la fonction est "congelée" : ses variables locales
gardent leur valeur. C'est ce qui permet au compteur n de mon_range() de
continuer là où il en était.
"""


# Un générateur s'épuise
#########################

"""
Comme tout itérateur (cf. chap. 23), un générateur ne se parcourt qu'UNE
SEULE FOIS. Une fois arrivé au bout, il est "épuisé" et ne donne plus rien.
"""
carres = (n * n for n in range(4))   # (expression génératrice, cf. plus bas)
print(list(carres))   # => [0, 1, 4, 9]
print(list(carres))   # => [] : épuisé !

"""
C'est un piège fréquent : on calcule par exemple le maximum, puis la somme…
et la somme vaut 0, car max() a déjà consommé tous les éléments.
"""
valeurs = mesures_valides(releves)
print(max(valeurs))   # => 14.0
print(sum(valeurs))   # => 0 (le générateur était déjà épuisé)

"""
Deux solutions :
    1. recréer un générateur à chaque fois (rappeler la fonction) ;
    2. si on doit relire les données plusieurs fois, les stocker dans une
       liste avec list(), en acceptant d'utiliser plus de mémoire.
"""
print(sum(mesures_valides(releves)))  # => 52.4 (générateur tout neuf)

valeurs = list(mesures_valides(releves))  # on stocke une bonne fois pour toutes
print(max(valeurs), sum(valeurs))         # => 14.0 52.4

"""
À l'inverse, une LISTE n'est pas un itérateur : chaque for (ou chaque appel
à iter()) repart du début. C'est pour cela qu'on peut la parcourir autant de
fois qu'on veut.
"""


# Générateurs infinis
######################

"""
Puisqu'un générateur ne calcule ses valeurs qu'à la demande, rien ne
l'oblige à s'arrêter ! Un "while True" dans un générateur est parfaitement
légitime : c'est celui qui l'utilise qui décidera quand s'arrêter.
"""
def entiers_naturels():
    n = 0
    while True:          # boucle infinie… mais en pause à chaque yield
        yield n
        n += 1


nat = entiers_naturels()
print(next(nat), next(nat), next(nat))   # => 0 1 2

# Attention : list(entiers_naturels()) ne se terminerait JAMAIS (et finirait
# par remplir toute la mémoire). Il faut s'arrêter soi-même, par exemple avec
# un break :
for n in entiers_naturels():
    if n * n > 50:
        break
    print(n, end=" ")
print()                  # => 0 1 2 3 4 5 6 7

"""
Exemple classique : la suite de Fibonacci, où chaque terme est la somme des
deux précédents (0, 1, 1, 2, 3, 5, 8…).
"""
def fibonacci():
    a, b = 0, 1          # affectation multiple, cf. chap. 10 et 17
    while True:
        yield a
        a, b = b, a + b


"""
Le module itertools (bibliothèque standard, cf. chap. 22) fournit des outils
pour manipuler les itérateurs. Deux d'entre eux sont très utiles avec les
générateurs infinis :
    - itertools.islice(itérateur, n) : ne garde que les n premiers éléments
      (c'est l'équivalent d'une slice [:n], cf. chap. 31, pour un itérateur)
    - itertools.count(debut, pas) : compte à l'infini, comme entiers_naturels()
"""
print(list(itertools.islice(fibonacci(), 10)))
# => [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# islice accepte aussi un début et un pas, comme les slices :
print(list(itertools.islice(fibonacci(), 10, 15)))  # => [55, 89, 144, 233, 377]

print(list(itertools.islice(itertools.count(100, 5), 4)))
# => [100, 105, 110, 115]

# On ne peut PAS utiliser les crochets sur un générateur : il n'a pas
# d'indices, puisque ses éléments n'existent pas encore !
try:
    fibonacci()[:10]
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 3: (Sans ce try: … except …, cette ligne créerait : 'generator' object
#    is not subscriptable)

# Pour numéroter des lignes ou générer des identifiants, count() est pratique
# avec zip() (cf. chap. 24), qui s'arrête dès que la liste la plus courte est
# épuisée :
for ident, nom in zip(itertools.count(1001), ["Ada", "Alan", "Grace"]):
    print(ident, nom)
# => 1001 Ada
# => 1002 Alan
# => 1003 Grace


# Évaluation paresseuse et mémoire
###################################

"""
On dit qu'un générateur est "paresseux" (en anglais : "lazy evaluation") :
il ne calcule une valeur qu'au moment où on la lui demande. À l'inverse, une
liste est "gourmande" ("eager") : toutes ses valeurs sont calculées et
stockées en mémoire dès sa création.

La fonction sys.getsizeof() (module sys, cf. chap. 22) donne la taille d'un
objet en mémoire, en octets. Comparons une liste d'un million de carrés et
le générateur équivalent :
"""
liste_carres = [n * n for n in range(1_000_000)]
gen_carres = (n * n for n in range(1_000_000))

print(sys.getsizeof(liste_carres))  # => 8448728 (environ 8 Mo !)
print(sys.getsizeof(gen_carres))    # => 208 (quelques centaines d'octets)
# (Les valeurs exactes dépendent de votre version de Python et de votre
# machine, mais l'ordre de grandeur, lui, ne change pas.)

"""
IMPT : la taille du générateur ne dépend PAS du nombre d'éléments : il ne
stocke que son "état" (où il en est), jamais les éléments eux-mêmes. Avec un
milliard de carrés, la liste ne tiendrait pas en mémoire ; le générateur, si.

Et pourtant, le résultat d'un calcul est identique :
"""
print(sum(liste_carres) == sum(gen_carres))  # => True
del liste_carres     # on libère la mémoire de la liste (cf. chap. 16)

"""
Cas d'usage n°1 en Data Science : lire un très gros fichier (plusieurs Go
de logs, un CSV énorme…). Le lire d'un coup avec .read() ou .readlines()
(cf. chap. 28) chargerait tout en mémoire. Un fichier ouvert est déjà un
itérateur sur ses lignes : on peut écrire un générateur qui lit le fichier
ligne à ligne, et ne garde en mémoire qu'UNE ligne à la fois.

Créons d'abord un fichier de "logs" de 10 000 lignes pour l'exemple (on le
supprimera à la fin du chapitre).
"""
FICHIER_LOGS = "chap36_logs.txt"
with open(FICHIER_LOGS, "w", encoding="utf-8") as f:
    for i in range(10_000):
        niveau = "ERROR" if i % 1000 == 0 else "INFO"
        f.write(f"{niveau} requête n°{i}\n")


def lire_lignes(chemin):
    """Produit les lignes du fichier une par une, sans le saut de ligne."""
    with open(chemin, encoding="utf-8") as fichier:
        for ligne in fichier:          # lecture paresseuse, ligne par ligne
            yield ligne.rstrip("\n")


# Compter les erreurs, sans jamais charger tout le fichier :
nb_erreurs = sum(1 for ligne in lire_lignes(FICHIER_LOGS)
                 if ligne.startswith("ERROR"))
print(nb_erreurs)   # => 10

# Lire seulement les 3 premières lignes (le reste du fichier n'est même pas lu)
print(list(itertools.islice(lire_lignes(FICHIER_LOGS), 3)))
# => ['ERROR requête n°0', 'INFO requête n°1', 'INFO requête n°2']

"""
Quand utiliser une liste ou un générateur ?
    - Générateur : grandes quantités de données, données infinies, lecture
      de fichiers, quand on ne parcourt les données qu'UNE fois.
    - Liste : petites données, besoin d'indices (liste[3]), de len(), de
      parcourir plusieurs fois, de trier, d'afficher…
"""
try:
    len(lire_lignes(FICHIER_LOGS))
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 4: (Sans ce try: … except …, cette ligne créerait : object of type
#    'generator' has no len())


# Pipelines de générateurs
###########################

"""
Les générateurs se combinent très bien : chacun prend un itérable en entrée
et produit un nouvel itérateur en sortie. On peut ainsi construire une
"chaîne de traitement" (un "pipeline"), comme sur une chaîne de montage :
chaque étape transforme les éléments un par un, puis les passe à la
suivante.

Exemple : un petit fichier CSV de ventes, dont certaines lignes sont vides
ou mal remplies.
"""
lignes_csv = [
    "produit;quantite;prix",
    "pomme;3;0.5",
    "",
    "poire;2;0.8",
    "kiwi;;0.3",            # quantité manquante
    "banane;6;0.25",
]


def sans_entete(lignes):
    """Étape 1 : saute la première ligne (l'en-tête)."""
    premiere = True
    for ligne in lignes:
        if premiere:
            premiere = False
            continue
        yield ligne


def non_vides(lignes):
    """Étape 2 : ignore les lignes vides."""
    for ligne in lignes:
        if ligne.strip():
            yield ligne


def decouper(lignes):
    """Étape 3 : transforme chaque ligne en liste de champs."""
    for ligne in lignes:
        yield ligne.split(";")


def convertir(enregistrements):
    """Étape 4 : convertit les champs, ignore les lignes invalides."""
    for produit, quantite, prix in enregistrements:
        try:
            yield produit, int(quantite), float(prix)
        except ValueError:
            pass        # quantité ou prix invalide : on ignore la ligne


# On "branche" les étapes les unes sur les autres. RIEN n'est encore calculé…
pipeline = convertir(decouper(non_vides(sans_entete(lignes_csv))))

# …jusqu'à ce qu'on consomme le dernier générateur :
for produit, quantite, prix in pipeline:
    print(f"{produit:<7} {quantite * prix:.2f} €")
# => pomme   1.50 €
# => poire   1.60 €
# => banane  1.50 €

"""
IMPT : chaque ligne traverse TOUT le pipeline avant que la suivante ne soit
lue. Aucune liste intermédiaire n'est créée : avec un fichier de 10 Go à la
place de lignes_csv, la mémoire utilisée serait la même.

Chaque étape est une petite fonction simple, facile à comprendre et à tester
séparément (cf. chap. 29 et 37) : c'est un excellent moyen d'organiser un
traitement de données.
"""


# Déléguer avec "yield from"
#############################

"""
Il arrive qu'un générateur doive produire tous les éléments d'un autre
itérable. On pourrait écrire une boucle :

    for x in autre_iterable:
        yield x

Depuis Python 3.3, "yield from" fait exactement cela, en une ligne.
"""
def tout_parcourir(*listes):    # *listes : nombre variable d'args, cf. chap. 32
    for liste in listes:
        yield from liste        # produit chaque élément de la liste


print(list(tout_parcourir([1, 2], (3, 4), "ab")))  # => [1, 2, 3, 4, 'a', 'b']

# yield from fonctionne avec n'importe quel itérable, y compris un autre
# générateur :
def debut_et_fin():
    yield "début"
    yield from mon_range(1, 4)   # délègue à un autre générateur
    yield "fin"


print(list(debut_et_fin()))  # => ['début', 1, 2, 3, 'fin']

"""
yield from est particulièrement élégant avec la récursivité (cf. chap. 33).
Exemple : "aplatir" une liste de listes de listes… quelle que soit la
profondeur.
"""
def aplatir(element):
    if isinstance(element, list):    # isinstance(x, type) : cf. chap. 34
        for sous_element in element:
            yield from aplatir(sous_element)   # appel récursif
    else:
        yield element


print(list(aplatir([1, [2, [3, [4, 5]], 6], [[7]]])))
# => [1, 2, 3, 4, 5, 6, 7]


# Expressions génératrices
###########################

"""
On les a vues au chap. 23 : une compréhension entre parenthèses crée un
générateur, sans avoir besoin d'écrire de fonction.

    (expression for element in iterable if condition)

Ces deux écritures sont équivalentes :
"""
def carres_pairs(n):
    for x in range(n):
        if x % 2 == 0:
            yield x * x


gen_1 = carres_pairs(10)
gen_2 = (x * x for x in range(10) if x % 2 == 0)
print(list(gen_1))   # => [0, 4, 16, 36, 64]
print(list(gen_2))   # => [0, 4, 16, 36, 64]

"""
Quand utiliser l'une ou l'autre ?
    - Expression génératrice : transformation ou filtre simple, qui tient
      sur une ligne. Idéale comme argument de sum(), max(), any(), all(),
      "".join()… (on peut alors omettre les parenthèses).
    - Fonction génératrice : logique plus complexe (plusieurs étapes, état
      à mémoriser, try/except, générateur infini…), ou quand on veut lui
      donner un nom et une docstring.
"""
mots = ["data", "science", "python", "pandas"]
print(any(len(m) > 6 for m in mots))         # => True ("science")
print("-".join(m.upper() for m in mots))     # => DATA-SCIENCE-PYTHON-PANDAS

"""
Les expressions génératrices se chaînent aussi en pipeline. Voici le même
traitement de lignes_csv que plus haut, en version compacte (les lignes
invalides sont filtrées par un test, cette fois) :
"""
lignes = (l for l in lignes_csv[1:] if l.strip())
champs = (l.split(";") for l in lignes)
valides = (c for c in champs if c[1].isdigit())
print(sum(int(c[1]) * float(c[2]) for c in valides))  # => 4.6


# Bonus : les décorateurs
##########################

"""
Cette section utilise les notions du chap. 32 : *args, **kwargs, et les
fonctions définies dans d'autres fonctions (closures).

Rappel : en Python, une fonction est une valeur comme une autre. On peut la
mettre dans une variable, la passer en argument à une autre fonction, ou la
retourner depuis une fonction (cf. chap. 15 et 32).
"""
def crier(texte):
    return texte.upper() + " !"


f = crier                   # pas de parenthèses : on ne l'appelle pas
print(f("bonjour"))         # => BONJOUR !


def appliquer_deux_fois(fonction, valeur):
    return fonction(fonction(valeur))


print(appliquer_deux_fois(crier, "hé"))  # => HÉ ! !

"""
Un DÉCORATEUR est une fonction qui prend une fonction en argument et
retourne une NOUVELLE fonction, qui "enrobe" la première pour lui ajouter
un comportement (afficher un message, chronométrer, vérifier les
arguments…), SANS modifier son code.
"""
def avec_log(fonction):
    def enveloppe(*args, **kwargs):       # accepte n'importe quels arguments
        print(f"→ appel de {fonction.__name__}{args}")
        resultat = fonction(*args, **kwargs)   # on appelle l'originale
        print(f"← {fonction.__name__} a retourné {resultat!r}")
        return resultat
    return enveloppe                       # on retourne la NOUVELLE fonction


def additionner(a, b):
    return a + b


additionner = avec_log(additionner)   # on remplace par la version "enrobée"
print(additionner(2, 3))
# => → appel de additionner(2, 3)
# => ← additionner a retourné 5
# => 5

"""
Cette écriture "additionner = avec_log(additionner)" est si fréquente que
Python propose une syntaxe dédiée : le "@" placé juste au-dessus du def.

    @avec_log                     est exactement équivalent à :
    def multiplier(a, b):             def multiplier(a, b): …
        return a * b                  multiplier = avec_log(multiplier)
"""
@avec_log
def multiplier(a, b):
    return a * b


print(multiplier(4, 5))
# => → appel de multiplier(4, 5)
# => ← multiplier a retourné 20
# => 20

"""
Petit défaut : la fonction décorée a "perdu" son nom et sa docstring. Elle
s'appelle maintenant "enveloppe" !
"""
print(multiplier.__name__)   # => enveloppe

"""
Le décorateur functools.wraps (bibliothèque standard) corrige ce problème :
on le place sur la fonction enveloppe, et il recopie le nom, la docstring,
etc. de la fonction d'origine. IMPT : prenez l'habitude de toujours
l'utiliser dans vos décorateurs.

Exemple utile : un décorateur qui chronomètre une fonction (time.perf_counter
donne un temps très précis en secondes, cf. chap. 30).
"""
def chronometre(fonction):
    @functools.wraps(fonction)
    def enveloppe(*args, **kwargs):
        debut = time.perf_counter()
        resultat = fonction(*args, **kwargs)
        duree = time.perf_counter() - debut
        print(f"{fonction.__name__} : {duree:.4f} s")
        return resultat
    return enveloppe


@chronometre
def somme_carres(n):
    """Somme des carrés de 0 à n - 1."""
    return sum(x * x for x in range(n))


print(somme_carres(1_000_000))
# => somme_carres : 0.0412 s (la durée varie selon la machine)
# => 333332833333500000
print(somme_carres.__name__)  # => somme_carres (grâce à functools.wraps)
print(somme_carres.__doc__)   # => Somme des carrés de 0 à n - 1.

"""
On peut empiler plusieurs décorateurs : ils s'appliquent de bas en haut (le
plus proche du def en premier).

Vous rencontrerez des décorateurs partout : @functools.lru_cache (mémoriser
les résultats d'une fonction, cf. chap. 33), @property, @staticmethod et
@classmethod dans les classes (cf. chap. 34-35), @pytest.mark.parametrize
dans les tests (cf. chap. 37), et dans de nombreuses bibliothèques web.
"""


# Bonus : "with" et les gestionnaires de contexte
##################################################

"""
Depuis le chap. 28, on ouvre les fichiers avec "with" :

    with open("fichier.txt") as f:
        ...

"with" garantit que le fichier sera fermé à la sortie du bloc, MÊME si une
erreur survient dedans. L'objet placé après "with" s'appelle un
"gestionnaire de contexte" ("context manager") : il sait faire quelque chose
à l'ENTRÉE du bloc, et quelque chose à la SORTIE.

Le module contextlib permet d'écrire son propre gestionnaire de contexte…
avec un générateur ! On décore une fonction génératrice qui contient UN
SEUL yield :
    - le code avant le yield s'exécute à l'entrée du bloc with,
    - la valeur produite par yield est celle que l'on récupère après "as",
    - le code après le yield s'exécute à la sortie du bloc.
"""
@contextlib.contextmanager
def chrono(nom):
    debut = time.perf_counter()
    print(f"[{nom}] début")
    try:
        yield               # ici s'exécute le contenu du bloc with
    finally:                # finally : exécuté même en cas d'erreur (chap. 26)
        duree = time.perf_counter() - debut
        print(f"[{nom}] fin ({duree:.2f} s)")


with chrono("calcul"):
    total = sum(range(1_000_000))
print(total)
# => [calcul] début
# => [calcul] fin (0.01 s) (la durée varie)
# => 499999500000

"""
Exemple avec "as" : un gestionnaire de contexte qui crée un fichier
temporaire, le donne au bloc with, puis le supprime automatiquement.
"""
@contextlib.contextmanager
def fichier_temporaire(chemin, contenu):
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)
    try:
        yield chemin        # la valeur récupérée après "as"
    finally:
        os.remove(chemin)   # nettoyage garanti, même en cas d'erreur
        print(f"{chemin} supprimé")


with fichier_temporaire("chap36_temp.txt", "a\nb\nc\n") as chemin:
    print(list(lire_lignes(chemin)))
# => ['a', 'b', 'c']
# => chap36_temp.txt supprimé
print(os.path.exists("chap36_temp.txt"))  # => False

# Le nettoyage a lieu même si le bloc soulève une erreur :
try:
    with fichier_temporaire("chap36_temp.txt", "x") as chemin:
        1 / 0
except ZeroDivisionError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
# => chap36_temp.txt supprimé
# => 5: (Sans ce try: … except …, cette ligne créerait : division by zero)

"""
Le module contextlib propose aussi quelques gestionnaires prêts à l'emploi,
par exemple contextlib.suppress(UneErreur), qui ignore silencieusement une
erreur donnée (à utiliser avec modération, cf. chap. 26 !) :
"""
with contextlib.suppress(FileNotFoundError):
    os.remove("fichier_qui_n_existe_pas.txt")   # pas d'erreur affichée
print("on continue")   # => on continue


# Nettoyage
############

# On supprime le fichier de logs créé dans la section "Évaluation paresseuse"
os.remove(FICHIER_LOGS)

"""
En résumé :
    - yield transforme une fonction en générateur : un itérateur qui calcule
      ses valeurs à la demande, et se met en pause entre deux valeurs.
    - Un générateur ne se parcourt qu'une fois, n'a ni indices ni len(), mais
      n'occupe presque pas de mémoire, et peut même être infini.
    - Les générateurs se chaînent en pipelines de traitement de données.
    - Un décorateur (@) enrobe une fonction pour lui ajouter un comportement.
    - @contextlib.contextmanager crée un gestionnaire de contexte pour "with"
      à partir d'un générateur.
"""
