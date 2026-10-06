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
#  Chap. 0      #  Introduction                                                #
#               #                                                              #
################################################################################
#
#  - Le langage Python
#  - Un langage interprété
#  - Python en Data Science
#  - Que faut-il pour commencer ?
#  - Votre premier programme
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

Python est développé par une communauté de volontaires, coordonnée depuis 2001
par une association à but non lucratif : la Python Software Foundation (PSF).
L'interpréteur officiel (appelé "CPython", car il est écrit en C) est distribué
sous la licence "PSF License Agreement". C'est une licence open source dite
"permissive" :
    - on peut utiliser Python gratuitement, y compris pour un usage commercial,
    - on peut lire, modifier et redistribuer son code-source,
    - on peut même l'intégrer dans un logiciel propriétaire (fermé), à
      condition de conserver la mention de copyright et le texte de la licence.

À la différence d'une licence "copyleft" (comme la GPL, utilisée par Linux),
la licence PSF n'oblige pas à publier ses propres modifications sous la même
licence. C'est l'une des raisons pour lesquelles les entreprises adoptent
Python aussi facilement. Le texte complet est consultable sur :
https://docs.python.org/3/license.html

Note : ce sont deux choses différentes ! Python (le langage et l'interpréteur)
est sous licence PSF ; les programmes que VOUS écrivez en Python vous
appartiennent et vous les publiez sous la licence de votre choix. Ce cours, par
exemple, est sous licence CC BY-SA 4.0 (voir l'en-tête du fichier).

Une dernière précision historique : il existe deux grandes versions du langage,
Python 2 (2000) et Python 3 (2008), qui ne sont pas totalement compatibles.
Python 2 n'est plus maintenu depuis le 1er janvier 2020 : ce cours utilise
exclusivement Python 3.

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
de données et le Machine Learning (introduction au chap. 51).

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

Un "package" (ou "bibliothèque", "library" en anglais) est un ensemble de code
écrit par d'autres, que l'on peut réutiliser dans ses propres programmes. Le
fonctionnement des packages sera détaillé au chap. 22. Pour la Data Science,
les plus connus sont :
    - NumPy : calcul scientifique, tableaux de nombres (cf. chap. 38),
    - pandas : manipulation de tableaux de données (cf. chap. 39),
    - Matplotlib : graphiques (cf. chap. 40),
    - seaborn : graphiques statistiques (cf. chap. 50),
    - scikit-learn : Machine Learning (cf. chap. 51).

Ils ne sont pas fournis avec Python : il faut les installer, par exemple avec
la commande suivante tapée dans un terminal (pas dans Python !) :
?> python3 -m pip install numpy

(ou `conda install numpy` si vous utilisez conda).
"""
# Ex : importation de la bibliothèque numpy pour le calcul scientifique.
#
# Le bloc "try: … except …: …" ci-dessous permet de ne pas interrompre le
# programme si numpy n'est pas installé (cf. chap. 1, note 2, et chap. 26 pour
# le détail). Vous pouvez l'ignorer pour l'instant : retenez seulement que
# "import numpy" charge la bibliothèque.
try:
    import numpy

    # Si tout va bien, on pourra utiliser ce package et, par exemple, imprimer
    # sa version :
    print(numpy.__version__)  # => 2.5.3 (selon la version installée)
except ModuleNotFoundError as err:
    # Si numpy n'est pas installé, Python soulève une erreur
    # "ModuleNotFoundError", que l'on intercepte ici pour afficher un conseil.
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("   numpy est absent : essayez `python3 -m pip install numpy`")


# Votre premier programme
##########################

"""
Par tradition, le premier programme que l'on écrit dans un nouveau langage
affiche simplement "Hello, World!" ("Bonjour, le monde !") à l'écran.

En Python, il tient en une seule ligne :
"""
print("Bonjour, le monde !")  # => Bonjour, le monde !

"""
Quelques remarques sur cette ligne, que l'on détaillera dans les prochains
chapitres :
    - print() est une "fonction" intégrée à Python : elle affiche à l'écran ce
      qu'on lui donne entre parenthèses (cf. chap. 7 et chap. 14),
    - le texte entre guillemets est une "chaîne de caractères" (une "string",
      cf. chap. 7),
    - tout ce qui suit le # est un "commentaire", ignoré par Python (cf.
      chap. 3).

Comparez avec le même programme en Java, un autre langage très utilisé :

    public class Main {
        public static void main(String[] args) {
            System.out.println("Bonjour, le monde !");
        }
    }

On comprend pourquoi Python est réputé pour sa simplicité !

Python peut aussi servir de calculatrice :
"""
print(2 + 3)       # => 5
print(7 * 6)       # => 42
print(2 ** 10)     # => 1024 (2 puissance 10, cf. chap. 4)

"""
Pour exécuter ce fichier et voir ces résultats s'afficher, rendez-vous au
chap. 2 ("Lancer Python").
"""
