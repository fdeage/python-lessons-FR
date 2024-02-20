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
#  Chap. 2      #  Lancer Python                                               #
#               #                                                              #
################################################################################
#
#  1. Via l'interpréteur Python
#  2. Depuis un shell
#  3. Depuis un éditeur de texte
#  4. Depuis un notebook
#  5. Via un site Web
#
###################################

"""
Python désigne deux choses à la fois :
    1. un langage de programmation…
    2. …et un programme qui va exécuter du code écrit dans ce langage.

Il y a plusieurs façons de programmer avec Python :

    1. via l'interpréteur Python,
    2. depuis un "shell" en lançant un fichier contenant du code Python,
    3. depuis un programme externe, comme un éditeur de texte,
    4. depuis un notebook Jupyter/Lab,
    5. via une interface Web.

Les méthodes 1. et 2. supposent que l'on a accès à un terminal,
c'est-à-dire une interface en ligne de commande, ou "shell" (Powershell sur
Windows, Terminal.app sur macOS, ou n'importe quel terminal sur Linux).

Nous privilégions les méthodes 3. et 4.
"""


# 1. Via l'interpréteur Python
############################

"""
L'interpréteur (ou "shell") Python permet de tester des commandes Python et d'y
exécuter de petits programmes (les commandes tapées ne seront pas enregistrées,
donc on ne va pas y écrire de longs programmes très sophistiqués).

On lance le shell Python depuis le shell de l'ordinateur :
> python
Python 3.9.1 (default, Dec 24 2020, 15:57:37)
>>> <votre code suivi de return>

IMPT : il faut utiliser Python 3 pour vos projets. Tapez cette commande dans
un terminal pour connaître votre version
> python --version

Si la version retournée est 2.X.YY, essayez de lancer Python 3 avec
> python3

Si Python3 n'est pas installé, installez-le ! Vous perdrez beaucoup moins de
temps qu'en devant gérer les différences entre Python 2 et Python 3…


Une fois l'interpréteur Python lancé, vous pourrez lancer vos commandes Python :
>>> x = 2
>>> print(3 + x)
5

On appelle ce signe ">>>" une "invite de commande" (ou "prompt" en anglais).
Il signifie que l'exécution du code précédent est achevée et que vous
pouvez maintenant taper du nouveau code à exécuter.

Attention à ne pas confondre le shell de l'ordinateur et le shell Python : le
shell Python a un prompt caractéristique : ">>> ".

Note : Pour quitter l'interpréteur Python, on utilise quit()
>>> quit()
…et on revient au shell de l'ordinateur.
"""


# 2. En lançant un fichier depuis le shell
###########################################

"""
Le code Python se trouve dans des fichiers avec le suffixe ".py" : `engine.py`,
`questionnaire.py`, etc.

Pour lancer un programme contenant du code Python, on l'"appelle" (depuis le
shell) avec :
> python mon_fichier.py
"""


# 3. Depuis un éditeur de texte
################################

"""
Il est aussi possible de lancer Python depuis un éditeur de texte : Sublime
Text, Visual Studio Code, PyCharm, etc., proposent cette option. C'est souvent la
méthode la plus pratique car on n'a pas à quitter son fichier de code.

Pour cela, il faut lancer l'interprétation du code depuis une option de
l'éditeur. Sur Sublime Text, c'est Ctrl + B (ou Cmd + B sur Mac) : le résultat
de l'exécution apparaîtra dans une console à part.
"""


# 4. Depuis un notebook Jupyter/Lab
####################################

"""
C'est une option en plein essor depuis quelques années, qui allie le meilleur
de plusieurs mondes :
    - On peut travailler avec ses fichiers en local,
    - On a une interface qui mélange écriture de code et exécution,
    - L'interface est graphique et très pratique,
    - C'est une approche très standard que tout le monde utilise.

C'est une des méthodes les plus faciles une fois Jupyter installé. Le seul
inconvénient est qu'il y a moins de fonctionnalités d'édition et de raccourcis
clavier que sur un éditeur graphique "complet" (type Sublime Text ou VS Code)
"""


# 5. Via un site Web
#####################

"""
Dernière possibilité : coder en utilisant une plate-forme en ligne, comme
Repl.it (https://repl.it). On codera alors sans quitter son navigateur Web,
et sans avoir besoin d'installer Python sur son ordinateur.

Avantages :
    1. pas besoin d'avoir Python sur son ordinateur,
    2. les packages sont déjà installés, la version de Python est bonne.

Inconvénients :
    1. on a besoin d'une connexion internet permanente,
    2. l'exécution peut être plus lente que sur son propre ordinateur (mauvaise
       connexion, latence…),
    3. pour conserver le code écrit sur son ordinateur, il faudra ensuite le
       copier/coller dans des fichiers locaux.

Si l'on peut, il est conseillé de coder "en local", c'est-à-dire directement sur
son ordinateur, sans passer par internet, et de n'utiliser Repl.it que pour
dépanner.
"""
