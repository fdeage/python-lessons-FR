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
#  Chap. 36     #  Générateurs (et décorateurs) : corrigés                     #
#               #                                                              #
################################################################################

import os
import sys
import itertools
import functools
import contextlib


######################################
#  Rappel : itérables et itérateurs  #
######################################

# 1. Un itérateur se souvient de sa position :
it = iter("abc")
print(next(it), next(it))   # => a b
print(list(it))             # => ['c'] : il ne restait que "c"
try:
    next(it)
except StopIteration:
    print("1: (Sans ce try: … except …, cette ligne créerait : StopIteration)")
"""
list(it) a consommé le dernier élément : l'itérateur est épuisé, et le
next() suivant soulève StopIteration (cf. chap. 23 et 36).
"""


########################################
#  Les fonctions génératrices : yield  #
########################################

# 2. On parcourt le texte, et on "cède" chaque voyelle :
def voyelles(texte):
    for lettre in texte.lower():
        if lettre in "aeiouy":
            yield lettre


print(list(voyelles("Data Science")))  # => ['a', 'a', 'i', 'e', 'e']


# 3. Un yield dans la boucle, puis un dernier yield après la boucle :
def compte_a_rebours(n):
    while n > 0:
        yield n
        n -= 1
    yield "Décollage !"


print(list(compte_a_rebours(3)))  # => [3, 2, 1, 'Décollage !']


# 4. On parcourt les indices jusqu'à l'avant-dernier :
def pairs(liste):
    for i in range(len(liste) - 1):
        yield liste[i], liste[i + 1]     # un tuple (cf. chap. 17)


print(list(pairs([1, 2, 3, 4])))  # => [(1, 2), (2, 3), (3, 4)]
"""
Variante élégante : zip(liste, liste[1:]) produit exactement les mêmes
couples (cf. chap. 24 et 31).
"""
print(list(zip([1, 2, 3, 4], [2, 3, 4])))  # => [(1, 2), (2, 3), (3, 4)]


# 5. return TERMINE le générateur ; continue ne fait que sauter un tour :
def f():
    for i in range(5):
        if i == 3:
            return
        yield i


def g():
    for i in range(5):
        if i == 3:
            continue
        yield i


print(list(f()))  # => [0, 1, 2]
print(list(g()))  # => [0, 1, 2, 4]


#########################################
#  Pas à pas : une exécution suspendue  #
#########################################

# 6.
def gen():
    print("a")
    yield 1
    print("b")
    yield 2
    print("c")


g = gen()
print("créé")
x = next(g)
print(x)
for v in g:
    print(v)
# => créé
# => a
# => 1
# => b
# => 2
# => c
"""
- g = gen() n'exécute rien : "créé" s'affiche en premier.
- next(g) exécute jusqu'au premier yield : affiche "a", et x vaut 1.
- la boucle for reprend APRÈS le premier yield : affiche "b", reçoit 2 ;
  puis reprend après le 2e yield : affiche "c", et la fonction se termine
  (StopIteration, que for intercepte silencieusement).
"""


############################
#  Un générateur s'épuise  #
############################

# 7. sum(valides) consomme tout le générateur : list(valides) est ensuite
#    une liste vide, et len(...) vaut 0 → division par zéro !
temperatures = [21, -99, 23, 22, -99, 24]
valides = (t for t in temperatures if t >= 0)
try:
    print(sum(valides) / len(list(valides)))
except ZeroDivisionError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# Solution 1 : stocker les valeurs dans une liste (qu'on peut relire)
valides = [t for t in temperatures if t >= 0]
print(sum(valides) / len(valides))   # => 22.5

# Solution 2 : recréer le générateur pour chaque utilisation
print(sum(t for t in temperatures if t >= 0)
      / sum(1 for t in temperatures if t >= 0))   # => 22.5
"""
La solution 1 est ici la plus lisible : la liste est petite. La solution 2
ne stocke jamais les données, mais les parcourt deux fois.
"""


#########################
#  Générateurs infinis  #
#########################

# 8.
def puissances_de_2():
    p = 1
    while True:
        yield p
        p *= 2


print(list(itertools.islice(puissances_de_2(), 10)))
# => [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


# 9. Un for dans un while True : on reparcourt la liste indéfiniment.
def cycle_jours():
    jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
    while True:
        for jour in jours:
            yield jour


for date, jour in zip(range(1, 11), cycle_jours()):
    print(f"{jour} {date}", end=" | ")
print()
# => lun 1 | mar 2 | mer 3 | jeu 4 | ven 5 | sam 6 | dim 7 | lun 8 | mar 9 |
#    mer 10 |
"""
zip() s'arrête dès que range(1, 11) est épuisé : le générateur infini ne
pose donc aucun problème. Note : itertools.cycle(jours) fait exactement la
même chose que cycle_jours().
"""

# 10.
for n in itertools.count(1):
    if n * n > 2000:
        break
print(n)   # => 45 (44 * 44 = 1936, 45 * 45 = 2025)


######################################
#  Évaluation paresseuse et mémoire  #
######################################

# 11. (Les tailles exactes dépendent de la version de Python et de la machine.)
print(sys.getsizeof(range(10)))                        # => 48
print(sys.getsizeof(range(10_000_000)))                # => 48
print(sys.getsizeof(list(range(100_000))))             # => 800056
print(sys.getsizeof((x for x in range(10_000_000))))   # => 200
"""
- range() a la même taille quel que soit le nombre d'éléments : comme un
  générateur, il calcule ses valeurs à la demande (il ne stocke que début,
  fin et pas). Mais ce n'est pas un générateur : il a une longueur, des
  indices, et ne s'épuise pas (on peut le parcourir plusieurs fois).
- La liste, elle, grandit avec le nombre d'éléments (environ 8 octets par
  élément, rien que pour les "références" vers les nombres).
"""

# 12.
CHEMIN = "exo36_ventes.txt"
with open(CHEMIN, "w", encoding="utf-8") as fichier:
    for numero in range(1000):
        fichier.write(f"vente;{numero};{numero % 50}\n")


def montants(chemin):
    with open(chemin, encoding="utf-8") as fichier:
        for ligne in fichier:              # une seule ligne en mémoire
            yield int(ligne.split(";")[2])


print(sum(montants(CHEMIN)))  # => 24500
os.remove(CHEMIN)
"""
Vérification : chaque série de 50 ventes rapporte 0 + 1 + … + 49 = 1225, et
il y a 1000 / 50 = 20 séries : 20 * 1225 = 24500.
"""


##############################
#  Pipelines de générateurs  #
##############################

# 13.
def nettoyer(lignes):
    for ligne in lignes:
        yield ligne.strip()


def non_vides(lignes):
    for ligne in lignes:
        if ligne:                 # une chaîne vide vaut False (cf. chap. 21)
            yield ligne


def capitaliser(lignes):
    for ligne in lignes:
        yield ligne.capitalize()


brut = ["  Paris ", "", "lyon", "MARSEILLE  ", "  ", "paris"]
villes = capitaliser(non_vides(nettoyer(brut)))
print(sorted(set(villes)))  # => ['Lyon', 'Marseille', 'Paris']
"""
L'ordre des étapes compte : il faut nettoyer AVANT de tester si la ligne
est vide, sinon "  " (des espaces) serait considérée comme non vide.
set() élimine le doublon "Paris" (cf. chap. 25), et sorted() trie.
"""


# 14. On remplit un paquet ; quand il est plein, on le cède et on en
#     commence un nouveau. Sans oublier le dernier paquet, incomplet !
def par_paquets(iterable, taille):
    paquet = []
    for element in iterable:
        paquet.append(element)
        if len(paquet) == taille:
            yield paquet
            paquet = []
    if paquet:                    # il reste des éléments ?
        yield paquet


print(list(par_paquets(range(7), 3)))  # => [[0, 1, 2], [3, 4, 5], [6]]
print(list(par_paquets("abcdef", 2)))  # => [['a', 'b'], ['c', 'd'], ['e', 'f']]


##############################
#  Déléguer avec yield from  #
##############################

# 15.
def chaine(a, b):
    yield from a
    yield from b


print(list(chaine([1, 2], "xy")))  # => [1, 2, 'x', 'y']


# 16. Pour chaque clé : on la cède, puis, si la valeur est elle-même un
#     dictionnaire, on délègue à un appel récursif.
def cles_imbriquees(d):
    for cle, valeur in d.items():
        yield cle
        if isinstance(valeur, dict):
            yield from cles_imbriquees(valeur)


config = {"base": {"nom": "x", "port": 5432}, "debug": True}
print(list(cles_imbriquees(config)))  # => ['base', 'nom', 'port', 'debug']


##############################
#  Expressions génératrices  #
##############################

# 17.
phrase = "le python est un langage simple et efficace"
print(sum(len(mot) for mot in phrase.split() if len(mot) > 3))  # => 27
"""
Les mots de plus de 3 lettres : python (6), langage (7), simple (6) et
efficace (8) : 6 + 7 + 6 + 8 = 27.
"""

# 18.
print(any(x > 10 for x in [3, 8, 12]))   # => True (12 > 10)
print(all(x > 10 for x in []))           # => True (aucun contre-exemple !)
print(max((len(m), m) for m in ["chat", "hibou", "ours"]))  # => (5, 'hibou')
"""
- all() d'une séquence vide vaut True (cf. chap. 21) : "tous les éléments
  vérifient la condition" est vrai quand il n'y a aucun élément.
- max() compare des tuples (cf. chap. 17) : d'abord la longueur, puis le mot
  en cas d'égalité. On obtient le mot le plus long ET sa longueur.
"""


#############################
#  Bonus : les décorateurs  #
#############################

# 19.
def compter_appels(fonction):
    compteur = [0]       # une liste : la closure peut modifier son contenu

    @functools.wraps(fonction)
    def enveloppe(*args, **kwargs):
        compteur[0] += 1
        print(f"{fonction.__name__} appelée {compteur[0]} fois")
        return fonction(*args, **kwargs)
    return enveloppe


@compter_appels
def saluer(nom):
    return f"Bonjour {nom}"


print(saluer("Ada"))
print(saluer("Alan"))
# => saluer appelée 1 fois
# => Bonjour Ada
# => saluer appelée 2 fois
# => Bonjour Alan
"""
Avec nonlocal (cf. chap. 19), on peut utiliser un simple entier :
    compteur = 0
    def enveloppe(*args, **kwargs):
        nonlocal compteur
        compteur += 1
        …
"""


# 20.
def verifier_positifs(fonction):
    @functools.wraps(fonction)
    def enveloppe(*args, **kwargs):
        for valeur in args:
            if valeur < 0:
                raise ValueError(
                    f"{fonction.__name__} : argument négatif ({valeur})")
        return fonction(*args, **kwargs)
    return enveloppe


@verifier_positifs
def aire_rectangle(largeur, hauteur):
    return largeur * hauteur


print(aire_rectangle(3, 4))   # => 12
try:
    aire_rectangle(3, -4)
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 3: (Sans ce try: … except …, cette ligne créerait : aire_rectangle :
#    argument négatif (-4))
"""
L'intérêt : la vérification est écrite UNE fois, et on peut la réutiliser
sur n'importe quelle fonction en ajoutant simplement @verifier_positifs.
"""


###################################################
#  Bonus : with et les gestionnaires de contexte  #
###################################################

# 21. Le try/finally garantit l'affichage de la fin, même en cas d'erreur.
@contextlib.contextmanager
def section(titre):
    print(f"=== {titre} ===")
    try:
        yield
    finally:
        print("=== fin ===")


with section("Résultats"):
    print("tout va bien")
# => === Résultats ===
# => tout va bien
# => === fin ===

try:
    with section("Calcul risqué"):
        print(1 / 0)
except ZeroDivisionError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# => === Calcul risqué ===
# => === fin ===
# => 4: (Sans ce try: … except …, cette ligne créerait : division by zero)
