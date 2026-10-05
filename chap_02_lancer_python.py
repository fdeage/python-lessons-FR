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
#  2. En lançant un fichier depuis le shell
#  3. Depuis un éditeur de texte
#  4. Depuis un notebook Jupyter/Lab
#  5. Via un site Web
#  6. Mode interactif vs fichier : la différence qui piège
#  7. Quelle méthode choisir ?
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
###############################

"""
L'interpréteur (ou "shell") Python permet de tester des commandes Python et d'y
exécuter de petits programmes (les commandes tapées ne seront pas enregistrées,
donc on ne va pas y écrire de longs programmes très sophistiqués).

On lance le shell Python depuis le shell de l'ordinateur :
> python
Python 3.12.3 (main, Apr 10 2024, 05:33:47)
>>> <votre code suivi de return>

Selon votre système, la commande s'appelle `python`, `python3` ou, sur
Windows, `py`. Essayez-les dans cet ordre si la première ne fonctionne pas.

IMPT : il faut utiliser Python 3 pour vos projets. Tapez cette commande dans
un terminal pour connaître votre version
> python --version

Si la version retournée est 2.X.YY, essayez de lancer Python 3 avec
> python3

Si Python3 n'est pas installé, installez-le ! Vous perdrez beaucoup moins de
temps qu'en devant gérer les différences entre Python 2 et Python 3…
(Téléchargement officiel : https://www.python.org/downloads ; sur Linux, passez
plutôt par le gestionnaire de paquets de votre distribution.)


Une fois l'interpréteur Python lancé, vous pourrez lancer vos commandes Python :
>>> x = 2
>>> print(3 + x)
5

On appelle ce signe ">>>" une "invite de commande" (ou "prompt" en anglais).
Il signifie que l'exécution du code précédent est achevée et que vous
pouvez maintenant taper du nouveau code à exécuter.

Quand une instruction s'étend sur plusieurs lignes (comme un "if", cf.
chap. 12), le prompt devient "..." : l'interpréteur attend la suite. On termine
le bloc en laissant une ligne vide (Entrée deux fois) :
>>> if x > 1:
...     print("x est plus grand que 1")
...
x est plus grand que 1

Attention à ne pas confondre le shell de l'ordinateur et le shell Python : le
shell Python a un prompt caractéristique : ">>> ".

Quelques astuces dans l'interpréteur :
    - les flèches haut/bas permettent de retrouver les commandes précédentes,
    - help(print) affiche la documentation de la fonction print() (touche "q"
      pour sortir de l'aide),
    - Ctrl + C interrompt un calcul trop long ou un programme "bloqué".

Note : Pour quitter l'interpréteur Python, on utilise quit() (ou Ctrl + D sur
Linux/macOS, Ctrl + Z puis Entrée sur Windows)
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

Python lit alors le fichier de haut en bas, exécute chaque instruction dans
l'ordre, puis s'arrête à la fin du fichier (ou à la première erreur non
interceptée, cf. chap. 26). Seul ce qui est explicitement affiché (avec print(),
par exemple) apparaît dans le terminal.

Attention : le terminal doit être "placé" dans le dossier qui contient le
fichier. Sinon, il faut donner le chemin complet :
> python /home/moi/cours/chap_02_lancer_python.py

On change de dossier dans le terminal avec la commande `cd` (pour "change
directory") :
> cd /home/moi/cours
> python chap_02_lancer_python.py

Ce fichier lui-même est un programme Python : lancez-le ! Il affichera les
lignes suivantes.
"""
print("Bonjour ! Ce fichier vient d'être exécuté par Python.")
# => Bonjour ! Ce fichier vient d'être exécuté par Python.

"""
Bonus : l'option `-i` exécute le fichier, puis ouvre l'interpréteur interactif
au lieu de quitter. On peut alors inspecter les variables du programme :
> python -i mon_fichier.py
>>>
"""


# 3. Depuis un éditeur de texte
################################

"""
Il est aussi possible de lancer Python depuis un éditeur de texte : Sublime
Text, Visual Studio Code, PyCharm, etc., proposent cette option. C'est souvent
la méthode la plus pratique car on n'a pas à quitter son fichier de code.

Pour cela, il faut lancer l'interprétation du code depuis une option de
l'éditeur. Sur Sublime Text, c'est Ctrl + B (ou Cmd + B sur Mac) : le résultat
de l'exécution apparaîtra dans une console à part. Sur VS Code (avec
l'extension Python), c'est le bouton "▷" en haut à droite, ou F5 pour lancer
avec le débogueur.

Vérifiez que l'éditeur utilise bien Python 3 (et le bon Python, si vous en
avez plusieurs installés) : c'est souvent indiqué dans la barre d'état en bas
de la fenêtre.
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

Un notebook (fichier `.ipynb`) est découpé en "cellules" : des cellules de code
que l'on exécute une par une (Maj + Entrée), et des cellules de texte. Le
résultat de chaque cellule s'affiche juste en dessous, y compris des tableaux
et des graphiques : c'est idéal pour explorer des données.

Installation et lancement (dans un terminal) :
> python3 -m pip install jupyterlab
> jupyter lab

C'est une des méthodes les plus faciles une fois Jupyter installé. Le seul
inconvénient est qu'il y a moins de fonctionnalités d'édition et de raccourcis
clavier que sur un éditeur graphique "complet" (type Sublime Text ou VS Code).

Attention à un piège classique : on peut exécuter les cellules dans n'importe
quel ordre. Un notebook peut donc "marcher" chez vous et pas chez les autres,
parce qu'une cellule dont il dépend a été exécutée, puis modifiée ou supprimée.
Avant de partager un notebook, relancez-le entièrement ("Restart Kernel and Run
All Cells").
"""


# 5. Via un site Web
#####################

"""
Dernière possibilité : coder en utilisant une plate-forme en ligne, comme
Replit (https://replit.com) ou Google Colab (https://colab.research.google.com,
qui propose des notebooks Jupyter en ligne). On codera alors sans quitter son
navigateur Web, et sans avoir besoin d'installer Python sur son ordinateur.

Avantages :
    1. pas besoin d'avoir Python sur son ordinateur,
    2. les packages sont déjà installés, la version de Python est bonne.

Inconvénients :
    1. on a besoin d'une connexion internet permanente,
    2. l'exécution peut être plus lente que sur son propre ordinateur (mauvaise
       connexion, latence…),
    3. pour conserver le code écrit sur son ordinateur, il faudra ensuite le
       copier/coller dans des fichiers locaux,
    4. votre code (et vos données !) sont stockés chez un tiers : attention aux
       données confidentielles.

Si l'on peut, il est conseillé de coder "en local", c'est-à-dire directement sur
son ordinateur, sans passer par internet, et de n'utiliser ces sites que pour
dépanner.
"""


# 6. Mode interactif vs fichier : la différence qui piège
##########################################################

"""
IMPT : dans l'interpréteur interactif (et dans un notebook), la valeur d'une
expression tapée seule est affichée automatiquement :
>>> 2 + 3
5
>>> "abc"
'abc'

Mais DANS UN FICHIER, une expression seule est calculée… puis oubliée : rien ne
s'affiche ! Les deux lignes suivantes ne produisent donc aucun affichage quand
on exécute ce fichier :
"""
2 + 3
"abc"

# Pour voir un résultat quand on exécute un fichier, il faut le demander
# explicitement avec print() :
print(2 + 3)  # => 5
print("abc")  # => abc

"""
Remarquez une petite différence : l'interpréteur affiche 'abc' avec des
guillemets (il montre la "représentation" de la valeur), alors que print()
affiche abc sans guillemets (il montre le texte lui-même). On y reviendra au
chap. 7.

C'est pour cette raison que ce cours utilise print() partout : les fichiers
doivent pouvoir être exécutés tels quels.
"""


# 7. Quelle méthode choisir ?
##############################

"""
En résumé :
    - pour tester une ligne de code ou vérifier un résultat : l'interpréteur
      (méthode 1),
    - pour écrire un vrai programme, que l'on garde et que l'on fait évoluer :
      un fichier .py, lancé depuis l'éditeur ou le terminal (méthodes 2 et 3),
    - pour explorer et visualiser des données : un notebook (méthode 4),
    - en dépannage, sans ordinateur configuré : un site Web (méthode 5).

Pour suivre ce cours, le plus efficace est d'ouvrir le fichier du chapitre dans
votre éditeur, et d'avoir à côté un interpréteur Python ouvert pour retaper et
modifier les exemples (cf. chap. 1).

Dernière vérification : le code ci-dessous affiche la version de Python qui
exécute ce fichier. Il utilise le module "sys", que l'on verra au chap. 22.
"""
import sys

# Le résultat dépend de votre installation, par exemple :
print(sys.version)  # => 3.14.4 (main, Aug 20 2026, 10:41:58) [GCC 15.2.0]
