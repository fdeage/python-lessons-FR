################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Félix Déage - 2026                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 22     #  Modules, packages et import                                 #
#               #                                                              #
################################################################################
#
#  - Fonctionnement
#  - Les différentes façons d'importer
#  - Conventions de nommage
#  - Explorer un module : help() et dir()
#  - Écrire ses propres modules
#  - Modules et packages
#  - Installer des paquets externes
#  - Quelques modules utiles
#  - Le module random
#  - Le module sys
#  - D'autres modules de la bibliothèque standard
#
#################################

# Fonctionnement
#################

"""
Les modules sont des fichiers contenant du code Python que l'on peut récupérer
("importer") depuis un autre fichier.

Ce code peut se trouver sous les trois formes suivantes :
    1. fonctions
    2. variables
    3. objets (hors programme de ce cours : vous en croiserez sans le savoir,
       par exemple les dates du chap. 30)

Le but des modules est donc de permettre d'utiliser du code défini à un
autre endroit, par une autre personne, et même dans un autre projet. Plutôt
que de tout réécrire, on réutilise du code déjà écrit, testé et documenté.

Python est livré avec des centaines de modules prêts à l'emploi : c'est la
"bibliothèque standard" (en anglais "standard library", parfois abrégée
"stdlib"). On dit souvent que Python est livré "piles incluses" ("batteries
included").
"""

# On importe un module dans son code avec le mot-clé "import"
import math

"""
Ces modules contiennent des fonctions, des objets ou des variables que l'on
peut ensuite utiliser : on devra juste "préfixer" l'appel avec le nom du module,
suivi d'un point
"""
print(math.sqrt(16))  # => 4.0 (racine carrée, ou "square root")
print(math.pi)        # => 3.141592653589793 (une variable du module)
print(math.e)         # => 2.718281828459045

# On remarque que math est un objet de type "module"
print(type(math))  # => <class 'module'>

"""
Que se passe-t-il lors d'un "import math" ?
    1. Python cherche un module nommé "math" (voir plus bas où il cherche)
    2. il exécute son code, ce qui crée ses fonctions et variables
    3. il crée la variable "math" dans notre fichier, qui désigne ce module

IMPT : un module n'est exécuté qu'UNE SEULE FOIS, au premier import. Si on
l'importe à nouveau, Python réutilise simplement le module déjà chargé.
"""

# Si on oublie l'import, ou qu'on se trompe dans le nom, Python ne connaît pas
# le nom
try:
    print(statistics.mean([1, 2, 3]))  # on n'a pas importé statistics !
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    import maths  # faute de frappe : le module s'appelle "math"
except ModuleNotFoundError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


# Les différentes façons d'importer
####################################

"""
Il y a quatre façons d'importer, à bien connaître :

    1. import module                 → on écrit module.nom
    2. from module import nom1, nom2 → on écrit directement nom1, nom2
    3. import module as alias        → on écrit alias.nom
    4. from module import *          → on écrit directement tous les noms
                                       (déconseillé)
"""

#   1. "import module" : déjà vu ci-dessus. On sait toujours d'où vient une
#      fonction en lisant le code : math.sqrt vient évidemment de math.

#   2. "from … import …" n'importe que les noms désirés, directement dans notre
#      fichier
from math import sin, pi, log

print(log(math.e ** 2))  # => 2.0 (logarithme népérien)
print(sin(pi / 2))       # => 1.0
# Cela nous évite de devoir écrire "math.sin()" ou "math.pi"

# ceil() et floor() proposent des arrondis à l'entier supérieur ou inférieur
from math import ceil, floor

print(ceil(3.7))      # => 4
print(floor(3.7))     # => 3
print(floor(-4.432))  # => -5 (l'entier inférieur d'un négatif !)

# gcd(a,b) donne le PGCD de deux nombres a et b
from math import gcd

print(gcd(15, 20))  # => 5
print(gcd(15, 30))  # => 15

"""
Attention : "from math import sqrt" n'importe QUE sqrt. La variable "math" n'est
pas créée par cette ligne (ici elle existe parce qu'on a aussi fait
"import math" plus haut).
"""

#   3. On peut raccourcir un nom de module (lui donner un alias) avec "as"
import math as m

print(m.cos(0))                     # => 1.0
print(math.sqrt(16) == m.sqrt(16))  # => True
print(math.sqrt == m.sqrt)          # => True : c'est la même fonction

"""
Les alias sont surtout utiles pour les modules au nom long, utilisés très
souvent. En Data Science, certains alias sont des conventions universelles, que
tout le monde utilise :

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

On peut aussi renommer un seul nom importé :
"""
from math import factorial as fact
print(fact(5))  # => 120 (5! = 5 * 4 * 3 * 2 * 1)

"""
    4. On peut importer tous les noms d'un module avec "from … import *" :

        from math import *
        print(sqrt(2))     # fonctionne sans préfixe

       …mais c'est fortement déconseillé (cf. PEP 8, chap. 20) :
         - on ne sait plus d'où vient chaque nom en lisant le code
         - cela peut ÉCRASER silencieusement des noms existants (cf. les
           namespaces, chap. 19). Ex. : math définit sa propre fonction pow(),
           qui retourne toujours un float. Après "from math import *",
           pow(2, 3) ne vaut plus 8 (fonction intégrée), mais 8.0 !

       On ne l'exécute donc pas ici, pour ne pas "polluer" la suite du fichier.
"""
print(pow(2, 3))       # => 8 (la fonction intégrée pow())
print(math.pow(2, 3))  # => 8.0 (la fonction pow() du module math)

"""
Laquelle choisir ?
    - "import module" est le plus clair et le plus sûr : à privilégier
    - "from module import nom" quand on utilise souvent quelques noms précis
    - "import module as alias" pour les conventions (np, pd, plt)
    - jamais "from module import *" dans un vrai programme
"""


# Conventions de nommage
#########################

"""
Quelques règles de capitalisation (cf. PEP 8, chap. 20) que vous retrouverez
dans tous les modules :
    1. les fichiers (donc les modules) commencent par une *minuscule* :
       `person.py`, `car.py`, `my_module.py`
    2. les classes (que l'on ne verra pas dans ce cours) commencent par une
       *majuscule* : `class Person:`, `class Car(Vehicle):`
    3. les fonctions/méthodes commencent par une *minuscule* : `def compute(param):`,
       `def run(self):`
    4. les constantes d'un module sont en majuscules : `math.pi` est une
       exception historique, mais on trouve par ex. `sys.maxsize` ou
       `string.ascii_letters`

IMPT : un nom de module doit être un nom de variable valide : pas d'espace,
pas de tiret, pas de point, ne commence pas par un chiffre. "mon-module.py" ou
"2_test.py" ne pourront pas être importés avec "import" !
"""


# Explorer un module : help() et dir()
#######################################

"""
On peut utiliser help() pour avoir des informations sur le contenu du module :
dans une console Python (chap. 2), tapez

>>> help(math)        # documentation complète du module
>>> help(math.cos)    # documentation d'une seule fonction

La documentation s'affiche alors page par page : on avance avec les flèches ou
Espace, et on quitte avec la touche "q". C'est extrêmement utile pour voir
l'utilisation des fonctions du module !
Ex. cos(x, /)   Return the cosine of x (measured in radians).

(On n'appelle pas help() dans ce fichier pour ne pas bloquer son exécution.)

Cette documentation vient en fait de la docstring de chaque fonction (cf.
chap. 3), qu'on peut aussi afficher directement :
"""
print(math.cos.__doc__)  # => Return the cosine of x (measured in radians).

# La fonction intégrée dir() permet de voir quels fonctions et objets un
# module définit
print(dir(math))
"""
 => ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil',
 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc',
 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum',
 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan',
 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf',
 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder',
 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

(la liste exacte dépend de votre version de Python : chaque version ajoute
quelques fonctions)
"""

# Les noms entourés de "__" (on dit "dunder", pour "double underscore") sont
# des informations spéciales sur le module
print(math.__name__)  # => math

"""
Enfin, la documentation officielle de la bibliothèque standard, en français,
détaille chaque module avec des exemples :
https://docs.python.org/fr/3/library/index.html
"""


# Écrire ses propres modules
#############################

"""
Les modules Python sont juste des fichiers Python.
Vous pouvez écrire les vôtres et les importer aussi. Le nom du module
sera le nom du fichier, SANS l'extension ".py". On pourra importer toutes les
fonctions définies avec le mot-clé "def", et toutes les variables.

Par exemple, si on a un fichier `my_module.py` (il se trouve à côté de ce
fichier, ouvrez-le !) qui contient la fonction `my_function()`, on l'utilisera
comme ceci :
"""

import my_module  # => (my_module est en train d'être importé)
result = my_module.my_function()
print(result)                # => Bonjour depuis my_module !
print(my_module.doubler(21)) # => 42
print(my_module.VERSION)     # => 1.0

# On le réimporte : rien ne s'affiche, car le module n'est exécuté qu'une fois
import my_module

# Les autres syntaxes fonctionnent aussi
from my_module import doubler
print(doubler(5))  # => 10

"""
Où Python cherche-t-il les modules ? Dans une liste de dossiers, rangée dans la
variable sys.path (on verra le module sys plus bas), dans cet ordre :
    1. le dossier du fichier que l'on exécute (c'est pour cela que
       "import my_module" fonctionne : il est dans le même dossier)
    2. les dossiers de la bibliothèque standard
    3. le dossier "site-packages", où sont installés les paquets externes (cf.
       "Installer des paquets externes" plus bas)

IMPT : piège classique, ne nommez JAMAIS un de vos fichiers comme un module
existant (random.py, math.py, turtle.py…) ! Puisque le dossier courant est
regardé en premier, "import random" importerait VOTRE fichier à la place du
vrai module, et plus rien ne fonctionnerait.

Note : après un import, vous verrez apparaître un dossier "__pycache__" à côté
de vos modules. Python y range une version "précompilée" (fichiers .pyc) de vos
modules, pour les charger plus vite la fois suivante. Vous pouvez l'ignorer ou
le supprimer sans risque (on l'exclut en général de git, avec un fichier
.gitignore).
"""

"""
Le nom __name__ :

Chaque module a une variable __name__ qui contient son nom. Mais le fichier
qu'on LANCE directement (avec ?> python fichier.py) reçoit un nom spécial :
"__main__".
"""
print(my_module.__name__)  # => my_module
print(__name__)            # => __main__ (c'est ce fichier qu'on a lancé)

"""
Cela permet d'écrire du code qui s'exécute seulement quand on lance le fichier,
mais PAS quand on l'importe (pour des tests ou une démonstration, par exemple).
C'est une construction extrêmement courante, en fin de module :

    if __name__ == "__main__":
        print("Ce fichier a été lancé directement")

Essayez : ?> python my_module.py affiche un message de plus que
"import my_module".
"""


# Modules et packages
######################

"""
Un module Python est un fichier Python unique (avec une extension .py) qui
contient du code Python à importer, sous trois formes :
    1. des fonctions
    2. des classes
    3. des variables.

Tout le code réside dans un seul fichier. On peut l'importer et le réutiliser
depuis d'autres fichiers Python via un import.

Un package Python est un dossier qui contient plusieurs modules Python. Il
inclut un fichier spécial `__init__.py` (qui peut être vide ou contenir du code
d'initialisation du package).

Les packages sont utilisés pour organiser des modules apparentés dans une
hiérarchie de répertoires. Ils permettent de créer des espaces de noms
(namespaces, cf. chap. 19) et d'éviter les conflits de noms, ce qui facilite la
structuration de grands projets.

Par exemple, le package `my_package` (à côté de ce fichier) a cette structure :

    my_package/
        __init__.py
        module1.py      (contient some_function())
        module2.py      (contient another_function())

On peut utiliser ses modules comme ceci :
"""

from my_package import module1
result = module1.some_function()
print(result)  # => Résultat de module1.some_function()

from my_package import module2
result = module2.another_function()
print(result)
# => module2.another_function() utilise : Résultat de module1.some_function()

"""
Les mêmes syntaxes que pour les modules fonctionnent, avec un point pour
séparer le package du module :
"""
import my_package.module1               # → my_package.module1.some_function()
print(my_package.module1.some_function())  # => Résultat de module1.some_function()

from my_package.module1 import some_function  # → some_function()
print(some_function())  # => Résultat de module1.some_function()

import my_package.module2 as mod2       # → mod2.another_function()
print(mod2 is module2)  # => True : c'est le même module (importé une fois)

# Le code de __init__.py a été exécuté au premier import du package
print(my_package.NOM_DU_PACKAGE)  # => my_package

"""
Les grandes bibliothèques sont des packages, souvent avec des sous-packages.
Ex. : os.path est le module "path" du package "os", et "matplotlib.pyplot"
est le module "pyplot" du package "matplotlib".

En résumé, un module est un fichier Python unique, tandis qu'un package est un
répertoire qui peut contenir plusieurs modules connexes, organisés dans une
structure hiérarchique.

Note : on emploie aussi souvent le mot "bibliothèque" (en anglais "library",
qu'on traduit à tort par "librairie") pour désigner un module ou un package
qu'on peut installer et réutiliser.
"""


# Installer des paquets externes
#################################

"""
La bibliothèque standard ne contient pas tout. Des centaines de milliers de
paquets supplémentaires, écrits par la communauté, sont disponibles sur PyPI
(le "Python Package Index", https://pypi.org) : numpy, pandas, matplotlib,
requests, scikit-learn…

IMPT : un paquet externe doit être INSTALLÉ avant de pouvoir être importé.
Sinon, l'import crée une erreur ModuleNotFoundError, comme pour une faute de
frappe.

On installe un paquet avec l'outil pip, depuis un terminal (PAS depuis la
console Python) :

?> python3 -m pip install numpy           # installer un paquet
?> python3 -m pip install numpy pandas    # en installer plusieurs
?> python3 -m pip install --upgrade numpy # mettre à jour

(Aujourd'hui, on préfère l'outil uv, plus rapide et plus complet :
?> uv add numpy
cf. chap. 47.)
?> python3 -m pip uninstall numpy         # désinstaller
?> python3 -m pip list                    # lister les paquets installés
?> python3 -m pip show numpy              # infos sur un paquet installé

Remarque : on peut souvent taper simplement "pip install …", mais
"python3 -m pip" garantit qu'on installe le paquet pour LE Python que l'on
utilise (il y en a parfois plusieurs sur une même machine).
"""

# Un paquet tiers peut être absent : on peut le vérifier avec try/except (cf.
# chap. 26)
try:
    import numpy as np
    print(np.sqrt(16))  # => 4.0
except ModuleNotFoundError:
    print("(numpy n'est pas installé : tapez 'python3 -m pip install numpy' "
          "dans un terminal)")

"""
L'option "-m" de python :

"python3 -m nom_du_module" lance un module installé comme un programme. Beaucoup
d'outils Python s'utilisent ainsi :

?> python3 -m pip install …      # l'installeur de paquets
?> python3 -m venv .venv         # créer un environnement virtuel (voir plus bas)
?> python3 -m http.server        # un petit serveur web dans le dossier courant
?> python3 -m timeit "sum(range(100))"   # chronométrer une instruction
?> python3 -m this               # le Zen of Python (cf. chap. 20)

Les environnements virtuels :

Si tous vos projets installent leurs paquets au même endroit, ils finiront par
entrer en conflit (un projet a besoin de pandas 1.5, un autre de pandas 2.2…).
La solution : créer un "environnement virtuel" (virtualenv, ou "venv") par
projet, càd un dossier qui contient un Python et ses paquets, isolés du reste.

?> cd mon_projet
?> python3 -m venv .venv              # crée le dossier .venv
?> source .venv/bin/activate          # l'active (Linux / macOS)
?> .venv\\Scripts\\activate           # l'active (Windows)
(.venv) ?> pip install pandas         # installe pandas DANS .venv seulement
(.venv) ?> deactivate                 # revient au Python "normal"

On note souvent la liste des paquets d'un projet dans un fichier
"requirements.txt", pour qu'une autre personne puisse tout réinstaller :

?> pip freeze > requirements.txt      # enregistre les paquets installés
?> pip install -r requirements.txt    # les réinstalle ailleurs

Le chap. 47 présente les outils modernes (pyproject.toml, fichiers lock, uv),
que l'on utilise à partir de là.

D'autres outils font la même chose de façon plus complète : conda (très
utilisé en Data Science, avec la distribution Anaconda), poetry, ou uv (très
rapide).
"""


# Quelques modules utiles
##########################

# Modules de la bibliothèque standard : ils sont TOUJOURS disponibles (à de
# rares exceptions près, voir tkinter ci-dessous)
import math      # maths classiques (sinus, log/exp, racines…)
import random    # pour générer des nombres aléatoires
import os        # pour accéder aux commandes du système d'exploitation
import sys       # pour gérer des paramètres que l'on passe au programme
import zlib      # pour la compression de données
import time      # heure, date et chronomètre (cf. chap. 30)
import datetime  # pour manipuler des dates, créer des intervalles (cf. chap. 30)
import re        # pour utiliser les expressions régulières (cf. chap. 42)
import logging   # journaliser les événements d'un programme (cf. chap. 44)
import timeit    # mesurer le temps d’exécution d’une fonction.
import statistics  # moyenne, médiane, écart-type…
import collections  # des types construits supplémentaires (Counter…)
import csv       # lire et écrire des fichiers CSV (cf. chap. 28)
import json      # lire et écrire des données au format JSON

# tkinter (fenêtres graphiques, jeux…) et turtle (la tortue Python, équivalent
# de Scratch, qui utilise tkinter) font partie de la bibliothèque standard,
# mais certaines installations de Python (notamment sous Linux) ne les
# fournissent pas : on les importe donc prudemment. Importer ces modules
# n'ouvre aucune fenêtre : il faudrait pour cela appeler leurs fonctions.
try:
    import tkinter   # pour afficher des fenêtres graphiques, faire des jeux…
    import turtle    # la tortue Python (équivalent de Scratch)
    print("tkinter et turtle sont disponibles")
except ImportError:
    print("(tkinter n'est pas installé : sous Ubuntu/Debian, installez le "
          "paquet python3-tk)")

# Et parmi les paquets externes les plus connus en Data Science (à installer
# avec pip, cf. plus haut) :
#   numpy       : calcul numérique sur des tableaux de nombres (cf. chap. 38)
#   pandas      : manipulation de tableaux de données (cf. chap. 39)
#   matplotlib  : tracer des graphiques (cf. chap. 40)
#   seaborn     : graphiques statistiques (cf. chap. 50)
#   scikit-learn: Machine Learning (cf. chap. 51)
#   requests    : télécharger des données sur le Web (cf. chap. 49)


# Le module random
###################

"""
On rappelle que le module random permet de générer des nombres de façon
pseudo-aléatoire.

"Pseudo"-aléatoire, car un ordinateur ne sait pas vraiment tirer au hasard :
il calcule une suite de nombres qui en a l'air, à partir d'un nombre de départ
(la "graine", ou "seed"). Par défaut, la graine change à chaque exécution
(elle dépend de l'heure, notamment), donc les résultats aussi.

IMPT : toutes les valeurs affichées dans cette section changent donc à chaque
exécution : les valeurs en commentaire ne sont que des exemples.

On va importer ici les fonctions qui nous intéressent pour ce cours.
"""

# Les deux fonctions à connaître sont random et randint
from random import random, randint

# Attention à ne pas confondre le module random et la fonction random() : après
# cette ligne, le nom "random" désigne la FONCTION, et plus le module (cf. les
# namespaces, chap. 19). C'est pour cela que l'on préfère souvent
# "import random", puis random.random() et random.randint().

#   1. random() renvoie un float au hasard entre 0 (inclus) et 1 (exclu)
print(random())  # => 0.6434991611426172 (par exemple)
print(random())  # => 0.7056264837248809 (par exemple)
print(random())  # => 0.3684008576885187 (par exemple)

# Pour un float entre a et b, on multiplie et on décale : ici entre 10 et 20
print(10 + random() * 10)  # => 17.31… (par exemple)

#   2. randint(a, b) renvoie un int au hasard entre a et b inclus
print(randint(2, 4))  # => 2 (par exemple)
print(randint(2, 4))  # => 4
print(randint(2, 4))  # => 2
print(randint(2, 4))  # => 3
print(randint(2, 4))  # => …

# Exemple : simuler un lancer de dé à 6 faces
de = randint(1, 6)
print(f"Le dé affiche {de}")  # => Le dé affiche 5 (par exemple)

# Fonctions utiles du module random
from random import randrange, choice, shuffle, sample, seed

# HP : randrange([start], stop[, step]) fait la même chose, mais la borne de
# fin est EXCLUE (comme range(), chap. 13), et on peut y ajouter un pas
# (intervalle entre les valeurs)
print(randrange(1, 6, 2))  # Peut renvoyer 1, 3 ou 5
print(randrange(10))       # Un entier entre 0 et 9

# HP : choice(liste) tire au hasard un élément de la liste
entiers = [1, 2, 3, 4, 5]
print(choice(entiers))  # => 3 (par exemple)
print(choice(entiers))  # => 2
print(choice(entiers))  # => 3 (un même élément peut sortir plusieurs fois)
print(choice(entiers))  # => 3
print(choice(entiers))  # => 5
print(choice(["pile", "face"]))  # => pile (ou face)

# Tirer dans une liste vide est impossible
try:
    choice([])
except IndexError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# HP : shuffle(liste) mélange la liste "sur place", et ne retourne rien
# (cf. la valeur None, chap. 15)
shuffle(entiers)
print(entiers)          # => [5, 4, 2, 1, 3] (par exemple)
shuffle(entiers)
print(entiers)          # => [1, 4, 5, 3, 2]
print(shuffle(entiers))  # => None : le résultat est dans entiers, pas retourné !

# HP : sample(liste, n) va prélever aléatoirement n valeurs de la liste
print(sample(entiers, 2))  # => [3, 4] (par exemple)
print(sample(entiers, 2))  # => [3, 1]
print(sample(entiers, 2))  # => [5, 2]
# Il n'y aura pas de doublons dans le tirage (comme un tirage du loto), et
# l'ordre de la liste ne sera pas forcément respecté. La liste d'origine n'est
# pas modifiée.

# On ne peut pas prélever plus de valeurs qu'il n'y en a
try:
    sample(entiers, 10)
except ValueError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# HP : seed(n) fixe la graine. Avec la même graine, on obtient TOUJOURS la même
# suite de nombres : très utile pour reproduire une expérience (en Data Science
# et en Machine Learning notamment) ou déboguer un programme.
seed(42)
print(random())  # => 0.6394267984578837 (toujours, avec la graine 42)
print(random())  # => 0.025010755222666936
seed(42)
print(random())  # => 0.6394267984578837 : on repart du même point


# Le module sys
################

"""
Le module sys permet d'accéder aux paramètres que l'on "passe" au programme.

On donne des paramètres au programme en les écrivant à la suite après le nom du
fichier :

> python chap_22_modules.py  123   "ab"  2.4

On les récupère ensuite via sys.argv, qui contient la liste des paramètres.

Deux remarques :
    - sys.argv[0] contient le nom du programme lui-même, donc les arguments
      proprement dits commencent à l'indice 1
    - tous les paramètres sont des strings, qu'il faudra éventuellement
      convertir !
"""
print(sys.argv)  # => ['chap_22_modules.py'] (si on n'a passé aucun paramètre)

if len(sys.argv) > 3:
    print(type(sys.argv))      # => <class 'list'>
    print(len(sys.argv))       # => 4
    print(sys.argv[0])         # => chap_22_modules.py
    print(int(sys.argv[1]))    # => 123
    print(sys.argv[2])         # => ab
    print(float(sys.argv[3]))  # => 2.4

"""
Précaution utile en début de programme…
if len(sys.argv) > 3:
    …
…pour éviter d'accéder aux éléments d'une liste qui n'existent pas !

Lancez ce fichier avec les paramètres ci-dessus pour voir la différence.
"""

# sys donne aussi des informations sur Python lui-même
print(sys.version_info >= (3, 6))  # => True (comparaison de tuples, chap. 17)
print(sys.version)   # => 3.12.3 (main, …) : votre version de Python
print(sys.platform)  # => linux (ou win32, darwin pour macOS…)
print(sys.path[0])   # => le dossier de ce fichier (cf. "Écrire ses propres
#                       modules" plus haut)

"""
Enfin, sys.exit() arrête immédiatement le programme. On l'utilise par exemple
quand les paramètres sont incorrects :

    if len(sys.argv) < 2:
        print("Usage : python mon_programme.py <nom_de_fichier>")
        sys.exit(1)   # 1 (ou tout nombre non nul) signale une erreur

(On ne l'exécute pas ici, sinon la fin de ce fichier ne serait jamais lue !)
"""


# D'autres modules de la bibliothèque standard
###############################################

"""
Petit tour d'horizon de modules très utiles. Pour chacun, n'hésitez pas à
utiliser help() et dir(), et à consulter la documentation officielle.
"""

#   1. math : on a vu sqrt, sin, cos, log, floor, ceil, gcd, factorial…
print(math.isclose(0.1 + 0.2, 0.3))  # => True (comparer des floats, cf. chap. 4)
print(math.inf > 10 ** 100)          # => True (l'infini)

#   2. statistics : statistiques descriptives de base
notes = [12, 15, 9, 18]
print(statistics.mean(notes))    # => 13.5 (moyenne)
print(statistics.median(notes))  # => 13.5 (médiane)
print(statistics.stdev(notes))   # => 3.872983346207417 (écart-type)

#   3. collections.Counter : compter les éléments d'une séquence (un
#      dictionnaire spécialisé, cf. chap. 18 ; le module collections est
#      détaillé au chap. 43)
compte = collections.Counter("abracadabra")
print(compte["a"])            # => 5
print(compte.most_common(2))  # => [('a', 5), ('b', 2)]

#   4. os : dialoguer avec le système d'exploitation (cf. chap. 28)
print(os.getcwd())   # => /home/… : le dossier courant (dépend de votre machine)
print(os.path.join("dossier", "fichier.txt"))  # => dossier/fichier.txt
# (os.path.join utilise le bon séparateur : "/" sous Linux/macOS, "\" sous
# Windows)

#   5. time : le temps (cf. chap. 30)
debut = time.time()   # nombre de secondes écoulées depuis le 1er janvier 1970
time.sleep(0.1)       # met le programme en pause pendant 0.1 seconde
print(round(time.time() - debut, 1))  # => 0.1 (environ)

#   6. timeit : chronométrer précisément un petit morceau de code
duree = timeit.timeit("sum(range(100))", number=1000)
print(duree)  # => 0.0007… (en secondes, pour 1000 répétitions : varie selon la
#                machine)

#   7. re : les expressions régulières, pour chercher des motifs dans du texte
#      (cf. chap. 42).
#      Ici, r"\d+" signifie "un ou plusieurs chiffres" (le "r" devant la chaîne
#      empêche l'interprétation des "\", cf. l'échappement au chap. 7)
print(re.findall(r"\d+", "Il y a 3 chats et 12 chiens"))  # => ['3', '12']

#   8. zlib : compresser des données
texte = "pouet " * 100
compresse = zlib.compress(texte.encode())  # .encode() : string → octets
print(len(texte), len(compresse))  # => 600 20 (le texte, très répétitif, se
#                                     compresse bien ; la taille exacte peut
#                                     varier selon la version de zlib)
print(zlib.decompress(compresse).decode() == texte)  # => True

#   9. json : convertir des données Python en texte, et inversement (format
#      très utilisé sur le Web)
donnees = {"nom": "Ada", "langages": ["Python", "SQL"]}
print(json.dumps(donnees))  # => {"nom": "Ada", "langages": ["Python", "SQL"]}
print(json.loads('{"x": 1}')["x"])  # => 1

"""
Il en existe beaucoup d'autres : string, itertools, functools, pathlib,
datetime (chap. 30), csv (chap. 28), unittest (pour les tests, cf. chap. 29),
sqlite3 (bases de données SQL), urllib (Internet), etc.

Avant d'écrire une fonction compliquée, ayez le réflexe de chercher si elle
n'existe pas déjà dans la bibliothèque standard… ou dans un paquet de PyPI !
"""
