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
#  Chap. 32     #  Fonctions III : paramètres avancés et lambda                #
#               #                                                              #
################################################################################
#
#  - Rappels
#  - Un nombre quelconque d'arguments : *args
#  - Un nombre quelconque d'arguments nommés : **kwargs
#  - L'ordre des paramètres
#  - Déballer des arguments à l'appel
#  - Les paramètres "keyword-only"
#  - Les fonctions sont des objets
#  - Les fonctions anonymes : lambda
#  - Trier et chercher avec key=lambda
#  - map() et filter()
#  - map/filter ou compréhensions ?
#  - Fonctions imbriquées et closures
#  - En bref
#
#############################################

# Rappels
##########

"""
Aux chap. 14 et 15, on a vu comment définir une fonction avec "def", lui
passer des arguments, lui donner des paramètres par défaut et l'appeler avec
des arguments nommés. Petit rappel :
"""


def saluer(prenom, formule="Bonjour"):
    return f"{formule} {prenom} !"


print(saluer("Ada"))                      # => Bonjour Ada !
print(saluer("Ada", "Salut"))             # => Salut Ada !
print(saluer(formule="Coucou", prenom="Alan"))  # => Coucou Alan !

"""
Rappel du vocabulaire (cf. chap. 15) :
    - les PARAMÈTRES sont les noms écrits dans la définition (prenom, formule),
    - les ARGUMENTS sont les valeurs passées à l'appel ("Ada", "Salut"),
    - un argument "positionnel" est associé à un paramètre selon sa position,
    - un argument "nommé" (keyword argument) l'est grâce à son nom :
      formule="Coucou".

Problème : avec ce que l'on sait, une fonction a un nombre FIXE de
paramètres. Comment écrire une fonction comme print(), qui accepte 1, 2 ou
50 arguments ? C'est l'objet de la première partie de ce chapitre.

Dans la seconde partie, on verra qu'en Python, une fonction est une valeur
comme une autre : on peut la ranger dans une variable, la passer à une autre
fonction… ce qui ouvre beaucoup de possibilités (lambda, map, filter, key=).
"""


# Un nombre quelconque d'arguments : *args
###########################################

"""
Si on place une étoile "*" devant le nom d'un paramètre, ce paramètre va
RAMASSER tous les arguments positionnels (non nommés) qui restent, et les
ranger dans un TUPLE (cf. chap. 17).

Par convention, on appelle ce paramètre "args" (pour "arguments"), mais
n'importe quel nom fonctionne : c'est l'étoile qui compte. IMPT
"""


def somme(*args):
    print(type(args), args)
    total = 0
    for nombre in args:   # args est un tuple : on peut le parcourir
        total += nombre
    return total


print(somme(1, 2))         # => <class 'tuple'> (1, 2)
#                               3
print(somme(1, 2, 3, 4))   # => <class 'tuple'> (1, 2, 3, 4)
#                               10
print(somme())             # => <class 'tuple'> ()
#                               0
"""
Que l'on passe 0, 2 ou 4 arguments, ils arrivent tous dans le tuple args.

On peut combiner des paramètres "normaux" et *args. Les paramètres normaux
sont remplis d'abord, dans l'ordre ; *args prend tout le reste :
"""


def moyenne_eleve(nom, *notes):
    if len(notes) == 0:
        return f"{nom} : pas de note"
    return f"{nom} : {sum(notes) / len(notes):.1f}"


print(moyenne_eleve("Ada", 12, 15, 18))  # => Ada : 15.0
print(moyenne_eleve("Alan", 9.5))        # => Alan : 9.5
print(moyenne_eleve("Grace"))            # => Grace : pas de note
"""
Ici, "Ada" va dans nom, et (12, 15, 18) va dans notes.

Note : on connaît déjà des fonctions de ce type ! print() et max() acceptent
un nombre quelconque d'arguments :
"""
print(max(3, 8, 1, 6))  # => 8
"""
Attention : un paramètre étoilé ne ramasse que des arguments POSITIONNELS.
Si on lui passe un argument nommé qu'elle ne connaît pas, la fonction
proteste :
"""
try:
    somme(1, 2, bonus=3)
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# Pour recevoir aussi des arguments nommés quelconques, il faut **kwargs…


# Un nombre quelconque d'arguments nommés : **kwargs
#####################################################

"""
On a déjà rencontré "**kwargs" au chap. 27 (dictionnaires II). Rappel :
avec DEUX étoiles, le paramètre ramasse tous les arguments NOMMÉS qui
restent, et les range dans un DICTIONNAIRE : le nom de l'argument devient la
clé, sa valeur devient la valeur. IMPT

Par convention, on l'appelle "kwargs" ("keyword arguments").
"""


def fiche(**kwargs):
    print(type(kwargs))
    for cle, valeur in kwargs.items():
        print(f"  {cle} -> {valeur}")


fiche(nom="Lovelace", prenom="Ada", naissance=1815)
# => <class 'dict'>
#      nom -> Lovelace
#      prenom -> Ada
#      naissance -> 1815

"""
Exemple plus utile : une fonction qui fabrique une ligne de tableau de
données, avec des colonnes facultatives.
"""


def ligne_csv(identifiant, **colonnes):
    morceaux = [str(identifiant)]
    for nom_colonne in sorted(colonnes):   # trier les clés : ordre stable
        morceaux.append(f"{nom_colonne}={colonnes[nom_colonne]}")
    return ";".join(morceaux)


print(ligne_csv(1, ville="Lyon", temp=21.5))  # => 1;temp=21.5;ville=Lyon
print(ligne_csv(2))                           # => 2

"""
On peut bien sûr combiner *args et **kwargs. C'est très fréquent pour écrire
une fonction qui accepte "n'importe quoi" et le transmet à une autre :
"""


def tout_accepter(*args, **kwargs):
    print("positionnels :", args)
    print("nommés       :", kwargs)


tout_accepter(1, "deux", 3.0, couleur="bleu", taille=12)
# => positionnels : (1, 'deux', 3.0)
#    nommés       : {'couleur': 'bleu', 'taille': 12}


# L'ordre des paramètres
#########################

"""
Dans la définition d'une fonction, les différentes sortes de paramètres
doivent apparaître dans cet ordre précis : IMPT

    def f(a, b, c=0, *args, d, e=5, **kwargs):
          ────  ───  ─────  ────────  ────────
           1     2     3       4         5

    1. les paramètres positionnels obligatoires,
    2. les paramètres avec une valeur par défaut,
    3. *args,
    4. les paramètres "keyword-only" (voir plus bas),
    5. **kwargs, toujours en dernier.

En pratique, on n'utilise presque jamais tout en même temps ! Retenez
surtout : obligatoires, puis par défaut, puis *args, puis **kwargs.

Si on ne respecte pas cet ordre, Python refuse la définition dès la lecture
du fichier : c'est une erreur de SYNTAXE (cf. chap. 26), qu'un try ne peut
pas intercepter. On la démontre donc avec compile(), qui analyse une chaîne
de code sans l'exécuter :
"""
code_faux = "def f(**kwargs, *args):\n    pass"
try:
    compile(code_faux, "<exemple>", "exec")
except SyntaxError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

code_faux_2 = "def f(a=1, b):\n    pass"
try:
    compile(code_faux_2, "<exemple>", "exec")
except SyntaxError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
Le 2e cas est classique : un paramètre obligatoire (b) ne peut pas suivre
un paramètre qui a une valeur par défaut (a=1). Sinon, avec f(5), Python ne
saurait pas si 5 est pour a ou pour b.

Et à l'APPEL, la règle est similaire : les arguments positionnels d'abord,
les arguments nommés ensuite.
"""
try:
    compile('saluer(formule="Salut", "Ada")', "<exemple>", "exec")
except SyntaxError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")


# Déballer des arguments à l'appel
###################################

"""
Les étoiles ont un deuxième usage, symétrique du premier : à l'APPEL d'une
fonction, elles "déballent" une séquence ou un dictionnaire. IMPT

    - dans une DÉFINITION, * et ** EMBALLENT (ramassent les arguments),
    - dans un APPEL, * et ** DÉBALLENT (répartissent les valeurs).

Avec une étoile, chaque élément d'une liste (ou d'un tuple…) devient un
argument positionnel :
"""


def volume(longueur, largeur, hauteur):
    return longueur * largeur * hauteur


dimensions = [2, 3, 4]
print(volume(*dimensions))   # => 24
# … équivaut à volume(dimensions[0], dimensions[1], dimensions[2])

# Sans l'étoile, toute la liste irait dans le 1er paramètre :
try:
    volume(dimensions)
except TypeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

# Exemple très courant : afficher les éléments d'une liste séparés par des
# espaces, sans crochets ni virgules.
mesures = [12.5, 13.1, 11.8]
print(mesures)    # => [12.5, 13.1, 11.8]
print(*mesures)   # => 12.5 13.1 11.8
print(*mesures, sep=" | ")  # => 12.5 | 13.1 | 11.8

"""
Avec deux étoiles, chaque couple clé/valeur d'un dictionnaire devient un
argument nommé (déjà vu au chap. 27) :
"""
options = {"prenom": "Grace", "formule": "Hello"}
print(saluer(**options))   # => Hello Grace !
# … équivaut à saluer(prenom="Grace", formule="Hello")

"""
Les clés doivent correspondre EXACTEMENT aux noms des paramètres :
"""
try:
    saluer(**{"prénom": "Grace"})   # accent : ce n'est pas le même nom !
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")


# Les paramètres "keyword-only"
################################

"""
Parfois, on veut OBLIGER l'appelant à nommer un argument, pour que l'appel
soit lisible. Comparez :
    exporter(donnees, True, False)                     # True ? False ? hein ?
    exporter(donnees, entete=True, ecraser=False)      # clair !

Pour cela, on place une étoile seule "*" dans la liste des paramètres : tous
les paramètres situés APRÈS elle ne peuvent être passés que par leur nom
("keyword-only" = "seulement par mot-clé").
"""


def exporter(donnees, *, entete=True, ecraser=False):
    return f"{len(donnees)} lignes, entete={entete}, ecraser={ecraser}"


donnees = [[1, 2], [3, 4], [5, 6]]
print(exporter(donnees))
# => 3 lignes, entete=True, ecraser=False
print(exporter(donnees, ecraser=True))
# => 3 lignes, entete=True, ecraser=True

try:
    exporter(donnees, False, True)   # interdit : il faut nommer
except TypeError as err:
    print(f"7: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
De même, tout paramètre placé après *args est forcément keyword-only
(puisque *args a déjà ramassé tous les arguments positionnels) :
"""


def journal(*messages, niveau="INFO"):
    for message in messages:
        print(f"[{niveau}] {message}")


journal("Démarrage", "Lecture du fichier")
# => [INFO] Démarrage
#    [INFO] Lecture du fichier
journal("Fichier introuvable", niveau="ERREUR")
# => [ERREUR] Fichier introuvable

"""
Vous avez déjà utilisé des paramètres keyword-only sans le savoir : les
paramètres sep et end de print() (cf. chap. 7), et key et reverse de
sorted() (cf. chap. 24), ne peuvent être passés que par leur nom.

Bonus : depuis Python 3.8, une barre oblique "/" fait l'inverse : les
paramètres placés AVANT elle sont "positional-only" (on ne peut pas les
nommer). C'est surtout utilisé dans les fonctions intégrées, on le verra
parfois dans la documentation, par ex. : len(obj, /).
"""


# Les fonctions sont des objets
################################

"""
On a vu au chap. 15 qu'un nom de fonction sans parenthèses désigne la
fonction elle-même (son "adresse"), et qu'avec parenthèses, on l'APPELLE.

En Python, une fonction est une valeur comme une autre (on dit que les
fonctions sont des "objets de première classe"). On peut donc :
    1. la ranger dans une variable,
    2. la ranger dans une liste ou un dictionnaire,
    3. la passer en argument à une autre fonction (déjà vu au chap. 15),
    4. la renvoyer comme résultat d'une fonction (voir les closures plus bas).
"""


def doubler(x):
    return x * 2


def carre(x):
    return x ** 2


# 1. Dans une variable : f et doubler désignent LA MÊME fonction
f = doubler
print(f(21))             # => 42
print(f is doubler)      # => True
print(doubler.__name__)  # => doubler (le nom d'origine)
print(f.__name__)        # => doubler (f n'est qu'un autre nom)

# 2. Dans un dictionnaire : un petit "menu" d'opérations
operations = {"double": doubler, "carré": carre, "valeur absolue": abs}
for nom, fonction in operations.items():
    print(nom, "->", fonction(-3))
# => double -> -6
#    carré -> 9
#    valeur absolue -> 3


# 3. En argument : une fonction qui applique une autre fonction à une liste
def appliquer(fonction, valeurs):
    resultats = []
    for v in valeurs:
        resultats.append(fonction(v))
    return resultats


print(appliquer(carre, [1, 2, 3]))    # => [1, 4, 9]
print(appliquer(doubler, [1, 2, 3]))  # => [2, 4, 6]
print(appliquer(str, [1, 2, 3]))      # => ['1', '2', '3']

"""
Remarquez qu'on écrit appliquer(carre, …) et PAS appliquer(carre(), …) :
on passe la fonction elle-même, c'est appliquer() qui l'appellera. Avec les
parenthèses, on appellerait carre() tout de suite… sans argument :
"""
try:
    appliquer(carre(), [1, 2, 3])
except TypeError as err:
    print(f"8: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Une fonction qui reçoit (ou renvoie) une autre fonction s'appelle une
"fonction d'ordre supérieur". sorted(), min(), max(), map() et filter() en
sont des exemples, comme on va le voir.
"""


# Les fonctions anonymes : lambda
##################################

"""
Souvent, la fonction que l'on veut passer en argument est minuscule et ne
sert qu'une fois. Écrire un "def" complet est alors un peu lourd.

Le mot-clé "lambda" permet de créer une petite fonction SANS NOM ("anonyme"),
directement à l'endroit où on en a besoin. Syntaxe :

    lambda <paramètres> : <expression>

La lambda renvoie automatiquement la valeur de l'expression (pas besoin de
"return"). Les deux écritures suivantes sont équivalentes : IMPT
"""


def triple(x):
    return x * 3


triple_lambda = lambda x: x * 3   # noqa: E731 (voir la remarque plus bas)

print(triple(5))         # => 15
print(triple_lambda(5))  # => 15
print(triple_lambda)     # => <function <lambda> at 0x…> (adresse variable)

# Une lambda peut avoir 0, 1 ou plusieurs paramètres, et des valeurs par défaut
addition = lambda a, b: a + b          # noqa: E731
print(addition(2, 3))                   # => 5
hasard = lambda: 4                      # noqa: E731
print(hasard())                         # => 4
tva = lambda prix, taux=0.2: prix * (1 + taux)  # noqa: E731
print(tva(100))                         # => 120.0

# On peut même utiliser une expression conditionnelle (cf. chap. 12)
signe = lambda n: "positif" if n >= 0 else "négatif"  # noqa: E731
print(signe(-7))                        # => négatif

"""
Les limites de lambda :
    - une seule EXPRESSION : pas de boucle for, pas de "if" en bloc, pas de
      plusieurs lignes, pas d'affectation avec "=" ;
    - pas de nom (dans les messages d'erreur, elle s'appelle "<lambda>"),
      donc moins pratique à déboguer ;
    - pas de docstring.

Remarque de style : la PEP 8 (cf. chap. 20) DÉCONSEILLE de ranger une lambda
dans une variable comme on vient de le faire (c'était pour l'exemple : les
commentaires "noqa" disent aux outils de ne pas le signaler). Si on veut
donner un nom à une fonction, on utilise def ! Une lambda s'utilise
directement là où on en a besoin, typiquement en argument d'une autre
fonction : c'est ce que l'on va voir maintenant.
"""


# Trier et chercher avec key=lambda
####################################

"""
Au chap. 24, on a vu que sorted() accepte un paramètre key : une fonction
appliquée à chaque élément pour obtenir la "clé" de tri. On écrivait une
fonction avec def exprès. Avec lambda, on l'écrit sur place : IMPT
"""
mots = ["ananas", "kiwi", "fraise", "noix"]
print(sorted(mots, key=lambda mot: len(mot)))
# => ['kiwi', 'noix', 'ananas', 'fraise']
print(sorted(mots, key=lambda mot: mot[-1]))   # trié selon la dernière lettre
# => ['fraise', 'kiwi', 'ananas', 'noix']

"""
Note : key=lambda mot: len(mot) est équivalent à key=len, plus court. Une
lambda qui se contente d'appeler une fonction est inutile : passez
directement la fonction !

C'est surtout pour trier des données structurées (listes de tuples, de
dictionnaires) que lambda est irremplaçable :
"""
# Une liste de tuples (ville, population en milliers, superficie en km²)
villes = [("Paris", 2103, 105), ("Lyon", 522, 48), ("Marseille", 873, 241)]

# Trier par population (l'élément d'indice 1 de chaque tuple) :
print(sorted(villes, key=lambda v: v[1]))
# => [('Lyon', 522, 48), ('Marseille', 873, 241), ('Paris', 2103, 105)]

# Trier par densité (population / superficie), de la plus forte à la plus faible
par_densite = sorted(villes, key=lambda v: v[1] / v[2], reverse=True)
for nom, pop, sup in par_densite:
    print(f"{nom:10} {pop / sup:6.2f}")
# => Paris       20.03
#    Lyon        10.88
#    Marseille    3.62

# Avec une liste de dictionnaires (le format le plus courant pour des données !)
eleves = [
    {"nom": "Ada", "note": 17},
    {"nom": "Alan", "note": 12},
    {"nom": "Grace", "note": 19},
]
classement = sorted(eleves, key=lambda e: e["note"], reverse=True)
print([e["nom"] for e in classement])  # => ['Grace', 'Ada', 'Alan']

"""
min() et max() acceptent aussi key= : ils renvoient l'ÉLÉMENT (entier) pour
lequel la clé est minimale ou maximale.
"""
print(max(eleves, key=lambda e: e["note"]))  # => {'nom': 'Grace', 'note': 19}
print(min(villes, key=lambda v: v[2])[0])  # => Lyon (plus petite superficie)

"""
Astuce : pour trier selon PLUSIEURS critères, la clé peut renvoyer un tuple
(les tuples se comparent élément par élément, cf. chap. 17). Ici : par note
décroissante (d'où le "-"), puis par nom en cas d'égalité.
"""
notes = [("Zoé", 15), ("Ali", 18), ("Bob", 15), ("Eve", 18)]
print(sorted(notes, key=lambda n: (-n[1], n[0])))
# => [('Ali', 18), ('Eve', 18), ('Bob', 15), ('Zoé', 15)]


# map() et filter()
####################

"""
Deux fonctions d'ordre supérieur classiques, que l'on retrouve dans presque
tous les langages :

    map(fonction, itérable)     applique la fonction à CHAQUE élément
    filter(fonction, itérable)  garde les éléments pour lesquels la fonction
                                renvoie une valeur vraie (cf. chap. 21)

Attention : elles ne renvoient pas une liste, mais un ITÉRATEUR (cf. chap.
23), "paresseux" : les valeurs ne sont calculées qu'au moment où on les
parcourt. Pour voir le résultat, on le convertit avec list(). IMPT
"""
temperatures_c = [12.0, 18.5, 25.0, 31.2]

en_fahrenheit = map(lambda c: c * 9 / 5 + 32, temperatures_c)
print(en_fahrenheit)        # => <map object at 0x…> (adresse variable)
print(list(en_fahrenheit))  # => [53.6, 65.3, 77.0, 88.16]

# map() avec une fonction existante : très pratique pour convertir des types
saisie = "12 7 42 3"
nombres = list(map(int, saisie.split()))
print(nombres)              # => [12, 7, 42, 3]

# filter() : garder les températures supérieures à 20 °C
chaudes = list(filter(lambda c: c > 20, temperatures_c))
print(chaudes)              # => [25.0, 31.2]

# filter() avec None : garde les valeurs "vraies" (supprime 0, "", None…)
valeurs_brutes = ["Ada", "", "Alan", None, "Grace", ""]
print(list(filter(None, valeurs_brutes)))  # => ['Ada', 'Alan', 'Grace']

"""
Comme tout itérateur, le résultat de map() ou filter() s'ÉPUISE après un
parcours (cf. chap. 23) :
"""
carres = map(lambda x: x ** 2, [1, 2, 3])
print(list(carres))  # => [1, 4, 9]
print(list(carres))  # => [] (déjà épuisé !)

"""
Bonus : map() accepte plusieurs itérables ; la fonction reçoit alors un
élément de chacun (comme avec zip(), cf. chap. 24).
"""
prix = [10, 20, 30]
quantites = [3, 1, 2]
print(list(map(lambda p, q: p * q, prix, quantites)))  # => [30, 20, 60]


# map/filter ou compréhensions ?
#################################

"""
Les compréhensions de liste (cf. chap. 23) font exactement le même travail :

    list(map(f, l))                 ⇔   [f(x) for x in l]
    list(filter(f, l))              ⇔   [x for x in l if f(x)]
    list(map(f, filter(g, l)))      ⇔   [f(x) for x in l if g(x)]
"""
nombres = [1, 2, 3, 4, 5, 6]
# Les carrés des nombres pairs, des deux façons :
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nombres))))
# => [4, 16, 36]
print([x ** 2 for x in nombres if x % 2 == 0])
# => [4, 16, 36]

"""
La 2e version est nettement plus lisible ! En Python, on préfère en général
les compréhensions. Quelques repères :
    - fonction déjà existante (int, str, len, str.upper…) : map() est court
      et clair →  list(map(int, ligne.split()))
    - besoin d'écrire une lambda : préférez une compréhension ;
    - filtrer ET transformer : compréhension, sans hésiter.

Vous croiserez quand même map() et filter() dans du code existant, et
l'idée de "passer une fonction à appliquer" est partout en Data Science :
avec pandas, on écrira par ex. df["prix"].apply(lambda p: p * 1.2)
(cf. chap. 39).
"""


# Fonctions imbriquées et closures
###################################

"""
On peut définir une fonction À L'INTÉRIEUR d'une autre fonction. La
fonction intérieure n'existe alors que dans la fonction extérieure (c'est
une variable locale comme une autre, cf. chap. 19) :
"""


def statistiques(valeurs):
    def moyenne(liste):          # fonction "auxiliaire", locale
        return sum(liste) / len(liste)

    m = moyenne(valeurs)
    ecarts = [abs(v - m) for v in valeurs]
    return m, moyenne(ecarts)    # moyenne et écart moyen


print(statistiques([10, 12, 14, 20]))  # => (14.0, 3.0)

try:
    moyenne([1, 2])   # moyenne n'existe pas en dehors de statistiques()
except NameError as err:
    print(f"9: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Plus étonnant : une fonction peut RENVOYER la fonction intérieure. Et
celle-ci se "souvient" des variables de la fonction extérieure, même après
que la fonction extérieure a terminé ! On appelle ça une "closure"
(fermeture). C'est la règle "E" (Englobante) de LEGB, cf. chap. 19.
"""


def fabrique_multiplicateur(n):
    def multiplier(x):
        return x * n     # n vient de la fonction englobante
    return multiplier    # on renvoie la fonction, SANS l'appeler


fois_3 = fabrique_multiplicateur(3)
fois_10 = fabrique_multiplicateur(10)
print(fois_3(7))    # => 21
print(fois_10(7))   # => 70
"""
Déroulons pas à pas :
    1. fabrique_multiplicateur(3) crée une fonction multiplier où n vaut 3,
       et la renvoie : fois_3 désigne cette fonction.
    2. fabrique_multiplicateur(10) crée une AUTRE fonction multiplier, où n
       vaut 10 : fois_10.
    3. fois_3(7) exécute x * n avec x = 7 et n = 3 (mémorisé) → 21.

Une fabrique de fonctions peut aussi renvoyer une lambda :
"""


def fabrique_convertisseur(taux):
    return lambda montant: round(montant * taux, 2)


euros_vers_dollars = fabrique_convertisseur(1.08)
euros_vers_livres = fabrique_convertisseur(0.85)
print(euros_vers_dollars(50))  # => 54.0
print(euros_vers_livres(50))   # => 42.5

"""
Pour MODIFIER (et pas seulement lire) une variable de la fonction
englobante, il faut le mot-clé nonlocal (cf. chap. 19) :
"""


def fabrique_compteur():
    compte = 0

    def incrementer():
        nonlocal compte
        compte += 1
        return compte
    return incrementer


compteur = fabrique_compteur()
print(compteur(), compteur(), compteur())  # => 1 2 3

"""
Les closures sont le principe de base des DÉCORATEURS, une technique
avancée que l'on verra au chap. 36.
"""


# En bref
##########

"""
    def f(*args)           args = tuple des arguments positionnels en trop
    def f(**kwargs)        kwargs = dict des arguments nommés en trop
    def f(a, b=0, *args, c, **kwargs)   ordre obligatoire des paramètres
    def f(a, *, b)         b est keyword-only : f(1, b=2)
    f(*liste)              déballe la liste en arguments positionnels
    f(**dico)              déballe le dict en arguments nommés
    g = f                  une fonction est une valeur (pas de parenthèses !)
    lambda x: x * 2        petite fonction anonyme d'une seule expression
    sorted(l, key=lambda x: x[1])      trier selon un critère calculé
    list(map(f, l))        ⇔ [f(x) for x in l]
    list(filter(f, l))     ⇔ [x for x in l if f(x)]
    def fabrique(n):       closure : la fonction intérieure se souvient de n
        return lambda x: x * n

Au chapitre suivant, on verra qu'une fonction peut… s'appeler elle-même :
c'est la récursivité (cf. chap. 33).
"""
