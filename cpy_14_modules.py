################################################################################
#                                                                              #
#  NNNN    NNN    SSSSSS.   IIIII   (inspiré de https://learnxinyminutes.com)  #
#  NNNNN   NNN  SSSS  SSSS   III                                               #
#  NNNNNN  NNN  SSSS         III    Licence : CC BY-SA 4.0 FR                  #
#  NNNNNNN NNN   SSSSSS      III    Félix Déage - MMXXI                        #
#  NNN NNNNNNN      SSSSS    III                                               #
#  NNN  NNNNNN        SSSS   III    Cours Python - 1ère - v.3.4                #
#  NNN   NNNNN  SSSS  SSSS   III                                               #
#  NNN    NNNN   SSSSSSSS   IIIII                                              #
#                                                                              #
################################################################################
#               #                                                              #
#  Part. XIV    #  modules                                                     #
#               #                                                              #
################################################################################

#################################
# 20. Modules                   #
#################################
#
#  - Fonctionnement
#  - Remarques sur les modules
#  - Quelques modules utiles
#  - Le module random
#  - Le module sys
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
    3. objets

Le but des modules est donc de permettre de d'utiliser du code défini à un
autre endroit, par une autre personne, et même dans un autre projet.
"""

# On importe un module dans son code avec le mot-clé "import"
import math

"""
Ces modules contiennent des fonctions, des objets ou des variables que l'on
peut ensuite utiliser : on devra juste "préfixer" l'appel avec le nom du module
"""
print(math.sqrt(16))  # => 4.0 (racine carrée, ou "square root")

# On peut importer toutes les fonctions d'un module avec "from … import *"…
from math import *

# …mais c'est déconseillé : cela va importer plein de fonctions

# On utilisera plutôt "from … import …"
from math import sin, pi, log

# Ceci importera seulement les fonctions désirées.

print(log(e ** 2))  # => 2.0
print(sin(pi / 2))  # => 1.0
# Cela nous évite aussi de devoir écrire "math.sin()" ou "math.pi"

# ceil() et floor() proposent des arrondis à l'entier supérieur ou inférieur
from math import ceil, floor

print(ceil(3.7))      # => 4
print(floor(3.7))     # => 3
print(floor(-4.432))  # => -5

# gcd(a,b) donne le PGCD de deux nombres a et b
from math import gcd

print(gcd(15, 20))  # => 5
print(gcd(15, 30))  # => 15

# HP : on remarque que math est un objet de type "module"
print(type(math))  # => <class 'module'>

# HP : on peut raccourcir un nom de module (lui donner un alias) avec "as"
import math as m

print(m.cos(0))                     # => 1.0
print(math.sqrt(16) == m.sqrt(16))  # => True
print(math.sqrt == m.sqrt)          # => True


# Remarques sur les modules
############################

"""
Les modules Python sont juste des fichiers Python.
Vous pouvez écrire les vôtres et les importer aussi. Le nom du module
sera le nom du fichier. On pourra importer toutes les fonctions définies avec
le mot-clé "def".
"""

# On peut utiliser help() pour avoir des informations sur le contenu du module
help(math)
"""
C'est extrêmement utile pour voir l'utilisation des fonctions du module !
Ex. cos(x, /)   Return the cosine of x (measured in radians).
"""


# HP : la fonction intégrée dir() permet de voir quels fonctions et objets un
# module définit
import math

print(dir(math))
"""
 => ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
"""


# Quelques modules utiles
##########################

import math      # maths classiques (sinus, log/exp, racines…)
import random    # pour générer des nombres aléatoires
import os        # pour accéder aux commandes du système d'exploitation
import sys       # pour gérer des paramètres que l'on passe au programme
import zlib      # pour la compression de données
import tkinter   # pour afficher des fenêtres graphiques, faire des jeux…
import time      # heure, date et chronomètre
import datetime  # pour mesurer le temps, créer des intervalles
import turtle    # la tortue Python (équivalent de Scratch)
import re        # pour utiliser les expressions régulières ("regex")
import timeit    # mesurer le temps d’exécution d’une fonction.

# import matplotlib  # tracer des graphiques et visualiser des données


# Le module random
###################

"""
On rappelle que le module random permet de générer des nombres de façon
pseudo-aléatoire.

On va importer ici les fonctions qui nous intéressent pour ce cours.
"""

# Les deux fonctions à connaître sont random et randint
from random import random, randint

# Attention à ne pas confondre le module random et la fonction random()

#   1. random() renvoie un float au hasard entre 0 et 1
print(random())  # => 0.6434991611426172
print(random())  # => 0.7056264837248809
print(random())  # => 0.3684008576885187

#   2. randint(a, b) renvoie un int au hasard entre a et b inclus
print(randint(2, 4))  # => 2
print(randint(2, 4))  # => 4
print(randint(2, 4))  # => 2
print(randint(2, 4))  # => 3
print(randint(2, 4))  # => …

# Fonctions utiles du module random
from random import randrange, choice, shuffle, sample

# HP : randrange([start], stop[, step]) fait la même chose, mais on peut y
# ajouter un pas (intervalle entre les valeurs)
print(randrange(1, 6, 2))  # Peut renvoyer 1, 3 ou 5

# HP : choice(liste) tire au hasard un élément de la liste
entiers = [1, 2, 3, 4, 5]
print(choice(entiers))  # => 3
print(choice(entiers))  # => 2
print(choice(entiers))  # => 3
print(choice(entiers))  # => 3
print(choice(entiers))  # => 5

# HP : shuffle(liste) mélange la liste "sur place", et ne retourne rien
shuffle(entiers)
print(entiers)          # => [5, 4, 2, 1, 3]
shuffle(entiers)
print(entiers)          # => [1, 4, 5, 3, 2]

# HP : sample(liste, n) va prélever aléatoirement n valeurs de la liste
print(sample(entiers, 2))  # => [3, 4]
print(sample(entiers, 2))  # => [3, 1]
print(sample(entiers, 2))  # => [5, 2]
# Il n'y aura pas de doublons dans le tirage, et l'ordre de la liste ne sera
# pas forcément respecté.


# Le module sys
################

"""
Le module sys permet d'accéder aux paramètres que l'on "passe" au programme.

On donne des paramètres au programme en les écrivant à la suite après le nom du
fichier :

> python mon_fichier.py  123   "ab"  2.4

On les récupère ensuite via sys.argv, qui contient la liste des paramètres.

Deux remarques :
    - sys.argv[0] contient le nom du programme lui-même, donc les arguments
      proprement dits commencent à l'indice 1
    - tous les paramètres sont des strings, qu'il faudra éventuellement
      convertir !
"""
if len(sys.argv) > 3:
    print(type(sys.argv))      # => <class 'list'>
    print(len(sys.argv))       # => 4
    print(sys.argv[0])         # => 'cpy_13_modules.py'
    print(int(sys.argv[1]))    # => 123
    print(sys.argv[2])         # => 'ab'
    print(float(sys.argv[3]))  # => 2.4

"""
Précaution utile en début de programme…
if len(sys.argv) > 3:
    …
…pour éviter d'accéder aux éléments d'une liste qui n'existent pas !
"""
