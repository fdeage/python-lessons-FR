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
#  Chap. 0      #  Introduction                                                #
#               #                                                              #
################################################################################
#
#  - Le langage Python
#  - Un langage interprété
#  - Python en Data Science
#  - Que faut-il pour commencer ?
#
#####################################

# Le langage Python
####################

"""
Python est un langage de programmation créé à la fin des années 80 par
Guido van Rossum (GVR). Il a été rendu public en 1991, sous license
open-source (n'importe qui peut lire le code de Python puis le modifier pour
lui-même, le redistribuer, etc.).

Son nom est un hommage à la troupe britannique des Monty Python (1969-1983).

Les objectifs du langage, d'après GVR :
    - être intuitif et (presque) aussi lisible que l'anglais
    - rester raisonnablement rapide à exécuter
    - être open-source, pour que chacun puisse proposer des contributions
    - pouvoir être utilisé pour les petites tâches de tous les jours (scripting)

C'est un des langage les plus populaires au monde, utilisé dans énormément
de domaines : sciences, statistiques, finance, robotique, scripting, réseau,
Web, traitement d'images, IA…

La plupart des grandes organisations (CERN, NASA, Google, gouvernements)
l'utilisent pour l'un ou l'autre de leurs projets. Instagram, DropBox, Spotify,
Pinterest, Youtube… sont des sites qui sont ou ont commencé en Python ! [0][1]

Python utilise la Python Software Foundation License, qui est une licence open source, mais il pourrait être utile de donner plus de détails pour une compréhension approfondie.

[0] https://djangostars.com/blog/10-popular-sites-made-on-django
[1] https://thenewstack.io/instagram-makes-smooth-move-python-3
"""


# Un langage interprété
########################

"""
Python est un langage dit "interprété" : il est parcouru ligne à ligne par un
programme (l'"interpréteur") qui va lire les instructions (le "code-source" et
l'exécuter en même temps. Cela permet plus de flexibilité, au détriment de la
performance.

Ainsi, même si l'interpréteur Python est lui-même programmé en C (un des
langages les plus rapides qui soient), l'exécution de Python est plus lente que
celle d'autres langages, notamment des langages compilés. Mais :
    - cette différence est négligeable dans de nombreuses applications,
    - il est possible d'appeler du code écrit en C pour les parties critiques
      (NumPy, par exemple),
    - sa simplicité compense largement ce point,
    - de toute façon, on verra que la plupart des programmes n'ont pas besoin
      d'une exécution immédiate pour être utiles…
"""


# Python en Data Science
#########################

"""
Python est très logique et facile d'utilisation pour les débutants, mais il est
aussi extrêmement efficace et performant (en plus d'être utilisé partout). On
le trouvera extrêmement fréquemment dans le calcul scientifique, le traitement
de données et le Machine Learning.

Ce cours suppose que vous ne savez pas programmer : nous partirons donc de 0 en
expliquant un certain nombre de concepts universels de programmation. En effet,
beaucoup de constructions que nous verrons avec Python sont en fait communes
à presque tous les langages.

En conséquence, il y aura dans ce tutoriel trois types d'apprentissage :
    1. sur la programmation en général
    2. sur le langage Python
    3. parfois, sur d'autres langages (SQL, JavaScript, HTML/CSS…)
"""

# Que faut-il pour commencer ?
###############################

"""
Vous avez besoin, au minimum :
    - d'un ordinateur (avec clavier/souris/écran)
    - d'un système d'exploitation (Linux/macOS/Windows/autre) : préférez les
      OS de type UNIX, comme Linux ou macOS (sur Windows, essayer de travailler
      dans un environnement POSIX avec MinGW ou docker)
    - d'un éditeur de texte
    - d'une version de Python3 fonctionnelle.

Idéalement, vous aurez aussi besoin d'un gestionnaire de packages : `pip` ou
`conda`, par exemple. Assurez-vous que les packages installés sont utilisables
depuis votre éditeur de texte !
"""
# Ex : importation de la bibliothèque numpy pour le calcul scientifique
import numpy

# Si tout va bien, on pourra utiliser ce package et, par exemple, imprimer sa
# version :
print(numpy.__version__) # => 1.23.3
