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
#  Chap. 22     #  Modules : corrigés                                          #
#               #                                                              #
################################################################################

"""
Ce fichier se lance depuis n'importe quel dossier :
?> python3 corrs/corr_22_modules.py
?> python3 corrs/corr_22_modules.py 4 5 6     (pour l'exercice 21)
"""

####################
#  Fonctionnement  #
####################

"""
1. Un module est un fichier Python (.py) qui regroupe des fonctions, des
   variables, etc., que d'autres programmes peuvent réutiliser après l'avoir
   importé. Les fonctions intégrées (len, print, int…) sont toujours
   disponibles, sans import. Les fonctions d'un module (math.sqrt…) ne sont
   accessibles qu'après "import math" : cela évite de charger en mémoire des
   milliers de fonctions dont on n'a pas besoin.

2. NameError : à la 1re ligne, le nom math n'existe pas encore, car l'import
   n'est fait qu'à la ligne suivante. Python exécute le fichier de haut en
   bas : on met TOUJOURS les imports en haut du fichier.
"""
try:
    print(math.floor(3.7))
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

import math

print(math.floor(3.7))  # => 3


#######################################
#  Les différentes façons d'importer  #
#######################################

# 3. a) Le module entier : on préfixe par "math."
import math
print(math.sqrt(81))  # => 9.0

# b) Le module, avec un alias plus court :
import math as m
print(m.sqrt(81))     # => 9.0

# c) Uniquement la fonction : plus de préfixe
from math import sqrt
print(sqrt(81))       # => 9.0

# d) La fonction, sous un autre nom :
from math import sqrt as racine
print(racine(81))     # => 9.0

"""
4. a) "import math" : math et math.pi (pi seul n'existe pas, m non plus).
   b) "from math import pi" : seulement pi (le nom math n'est PAS créé).
   c) "import math as m" : seulement m et m.pi (le nom math n'est PAS créé :
      seul l'alias existe).

5. Le programme affiche 8.0, et non 8 : "from math import *" a importé
   math.pow, qui a remplacé ("masqué") la fonction intégrée pow. Avec
   "import *", on ne sait plus d'où viennent les noms, et un module peut
   écraser une fonction sans prévenir : c'est pour cela qu'on l'évite.
   (On ne fait pas "import *" ici, pour ne pas polluer ce fichier : on
   reproduit seulement l'effet.)
"""
print(pow(2, 3))       # => 8 (fonction intégrée)
print(math.pow(2, 3))  # => 8.0 (c'est ce qu'affiche le programme avec
#                         "import *")


############################
#  Conventions de nommage  #
############################

"""
6. Ordre de la PEP 8 : d'abord la bibliothèque standard, puis les paquets
   externes (installés avec pip), puis ses propres modules ; une ligne vide
   entre chaque groupe, et l'ordre alphabétique dans chaque groupe :

       import math
       import sys

       import numpy as np
       import pandas as pd

       import my_module

   Les alias np et pd sont des conventions universelles : tout le monde les
   reconnaît, il faut les utiliser.
"""


##########################################
#  Explorer un module : help() et dir()  #
##########################################

# 7. dir() retourne une liste de strings :
noms = dir(math)
print(len(noms))  # => 67 (le nombre exact dépend de votre version de Python)
for nom in noms:
    if nom.startswith("is"):
        print(nom)
# => isclose
# => isfinite
# => isinf
# => isnan
# => isqrt

# 8. La documentation est dans l'attribut __doc__ :
print(math.hypot.__doc__)
# => Multidimensional Euclidean distance from the origin to a point.
# => …  (le texte exact dépend de votre version de Python)
print(math.hypot(3, 4))  # => 5.0
"""
hypot() calcule la longueur de l'hypoténuse (càd la racine carrée de la somme
des carrés de ses paramètres) : racine de 3² + 4², soit 5.
"""


################################
#  Écrire ses propres modules  #
################################

"""
9. Python cherche les modules dans les dossiers de sys.path. Le 1er est le
   dossier du fichier qu'on a lancé : ici corrs/, où il n'y a pas de
   my_module.py. Il faut donc ajouter le dossier chaps/ (le dossier voisin,
   à côté de corrs/).

   (HP : __file__ est une variable qui contient le chemin du fichier en
   cours. On l'utilise plutôt que le dossier courant, pour que le programme
   fonctionne quel que soit le dossier depuis lequel on le lance.)
"""
import os
import sys

try:
    import my_module
except ImportError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

dossier_corrs = os.path.dirname(os.path.abspath(__file__))
racine_du_cours = os.path.dirname(dossier_corrs)
dossier_chaps = os.path.join(racine_du_cours, "chaps")
sys.path.append(dossier_chaps)

import my_module  # => (my_module est en train d'être importé)

print(my_module.doubler(21))  # => 42
print(my_module.VERSION)      # => 1.0

"""
10. "import my_module" exécute tout le fichier : il affiche donc
    "(my_module est en train d'être importé)", mais PAS les lignes situées
    sous "if __name__ == "__main__":".

    ?> python3 my_module.py affiche aussi ces lignes :
        (my_module est en train d'être importé)
        my_module a été lancé directement, et non importé.
        Bonjour depuis my_module !

    __name__ vaut "__main__" dans le fichier qu'on lance, et le nom du module
    ("my_module") quand il est importé. Ce "if" permet donc d'écrire du code
    (des tests, une démonstration…) qui ne s'exécute QUE si on lance le
    fichier directement.
"""
print(my_module.__name__)  # => my_module
print(__name__)            # => __main__

"""
11. Python cherche d'abord les modules dans le dossier du programme : "import
    random" importe… le fichier random.py de l'élève lui-même, et non le
    module random de Python ! Ce fichier ne contient pas de fonction randint,
    d'où l'AttributeError. Il ne faut jamais donner à ses fichiers le nom d'un
    module existant (random.py, math.py, csv.py…).
"""


#########################
#  Modules et packages  #
#########################

"""
12. Un module est UN fichier .py. Un package est un DOSSIER qui regroupe
    plusieurs modules (et éventuellement d'autres packages). Le fichier
    __init__.py fait d'un dossier un package : il est exécuté au premier
    import du package, et peut rester vide.
"""
# 13. Trois façons (le dossier chaps/ est déjà dans sys.path, exercice 9) :
import my_package.module1
print(my_package.module1.some_function())
# => Résultat de module1.some_function()

from my_package import module1
print(module1.some_function())  # => Résultat de module1.some_function()

from my_package.module1 import some_function
print(some_function())          # => Résultat de module1.some_function()

print(my_package.NOM_DU_PACKAGE)  # => my_package


####################################
#  Installer des paquets externes  #
####################################

"""
14. Ordre : d) créer l'environnement, b) l'activer (sous Windows :
    .venv\\Scripts\\activate), a) installer pandas DANS l'environnement,
    c) sauvegarder la liste des paquets.
    Le ou la collègue crée et active son propre environnement, puis lance :
        ?> python3 -m pip install -r requirements.txt
"""


# 15. On intercepte l'erreur levée quand le module est introuvable :
try:
    import numpy as np
    print("numpy est installé, version", np.__version__)
except ImportError:
    print("numpy n'est pas installé : python3 -m pip install numpy")
# => l'un des deux messages, selon votre installation


######################
#  Le module random  #
######################

from random import randint, randrange, choice, sample, shuffle, seed

# 16. Avec la même graine, les "hasards" sont TOUJOURS les mêmes : on obtient
#     les mêmes 10 lancers à chaque exécution. Pratique pour reproduire un
#     résultat (ou chercher un bug) ; sans seed(), ils changent à chaque fois.
seed(1)
lancers = []
for i in range(10):
    lancers.append(randint(1, 6))
print(lancers)  # => [2, 5, 1, 3, 1, 4, 4, 4, 6, 4]

# 17. compteurs[0] compte les 1, compteurs[1] les 2, etc. :
seed(2)
compteurs = [0, 0, 0, 0, 0, 0]
for i in range(6000):
    face = randint(1, 6)
    compteurs[face - 1] += 1
print(compteurs)  # => [985, 995, 995, 1021, 967, 1037]
"""
Chaque face sort environ 1000 fois (6000 / 6), mais jamais exactement : c'est
le hasard. Plus on fait de lancers, plus les proportions se rapprochent de
1/6 (c'est la "loi des grands nombres").
"""

# 18. a) choice() choisit un élément au hasard :
eleves = ["Ada", "Alan", "Grace", "Linus"]
seed(3)
print(choice(eleves))       # => Alan (avec cette graine)
# b) sample() tire des éléments DIFFÉRENTS (sans remise) :
print(sample(range(1, 50), 6))  # => [38, 35, 9, 24, 39, 31] (avec cette
#                                   graine)
# c) shuffle() modifie la liste sur place : on mélange donc une copie.
ordre_de_passage = list(eleves)
shuffle(ordre_de_passage)
print(ordre_de_passage)  # => ['Alan', 'Linus', 'Grace', 'Ada'] (avec cette
#                            graine)
print(eleves)            # => ['Ada', 'Alan', 'Grace', 'Linus'] (inchangée)

"""
19. randrange(0, 10, 2) fonctionne comme range(0, 10, 2) : 0, 2, 4, 6 ou 8
    (10 est exclu). randint(0, 10), lui, INCLUT ses deux bornes : un entier
    de 0 à 10.
"""


###################
#  Le module sys  #
###################

# 20.
print(sys.version)                 # => 3.14.4 (…) : votre version de Python
print(sys.version_info >= (3, 6))  # => True

# 21. Les paramètres commencent à l'indice 1 ; on les convertit en nombres :
total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])
print(total)  # => 0 sans paramètre ; 15.0 avec les paramètres 4 5 6
"""
On utilise float() plutôt que int(), pour accepter aussi des nombres à
virgule (écrits avec un point : 2.5).
"""


##################################################
#  D'autres modules de la bibliothèque standard  #
##################################################

# 22.
import statistics

notes = [8, 12, 15, 10, 18, 12]
print(statistics.mean(notes))    # => 12.5
print(statistics.median(notes))  # => 12.0 (moyenne des 2 valeurs du milieu,
#                                   12 et 12, une fois les notes triées)
print(round(statistics.stdev(notes), 2))  # => 3.56 (écart-type, arrondi)

# 23. On construit d'abord la phrase sans les espaces :
import collections

phrase = "le python est un langage de programmation"
compte = collections.Counter(phrase.replace(" ", ""))
print(compte.most_common(3))  # => [('e', 4), ('n', 4), ('a', 4)]
"""
Les trois lettres apparaissent 4 fois chacune. En cas d'égalité,
most_common() les classe dans l'ordre de leur première apparition dans la
phrase : "e" (dans "le"), puis "n" (dans "python"), puis "a" (dans "un
langage").
"""

# 24. dumps() : dictionnaire → texte ; loads() : texte → dictionnaire.
import json

eleve = {"nom": "Ada", "notes": [15, 18], "inscrit": True}
texte = json.dumps(eleve)
print(texte)        # => {"nom": "Ada", "notes": [15, 18], "inscrit": true}
print(type(texte))  # => <class 'str'>
eleve2 = json.loads(texte)
print(eleve2 == eleve)  # => True
"""
Dans le texte JSON, True devient "true" (en minuscules, comme en
JavaScript) ; loads() le reconvertit en True.
"""

# 25. On met la boucle dans une fonction, que timeit appellera :
import timeit


def somme_avec_boucle():
    total = 0
    for i in range(1000):
        total += i
    return total


duree_sum = timeit.timeit("sum(range(1000))", number=10000)
duree_boucle = timeit.timeit(somme_avec_boucle, number=10000)
print(duree_sum < duree_boucle)  # => True
print(round(duree_boucle / duree_sum, 1), "fois plus lent avec la boucle")
# => 2.6 fois plus lent avec la boucle (par exemple : la valeur dépend de
#    votre machine et de votre version de Python)
"""
sum() est écrite en C à l'intérieur de Python : elle est plusieurs fois plus
rapide qu'une boucle écrite en Python. Préférez les fonctions intégrées
quand elles existent !
"""
