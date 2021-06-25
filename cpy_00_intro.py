################################################################################
#                                                                              #
#  NNNN    NNN    SSSSSS.   IIIII   (inspiré de https://learnxinyminutes.com)  #
#  NNNNN   NNN  SSSS  SSSS   III                                               #
#  NNNNNN  NNN  SSSS         III    Licence : CC BY-SA 4.0 FR                  #
#  NNNNNNN NNN   SSSSSS      III    Félix Déage - MMXXI                        #
#  NNN NNNNNNN      SSSSS    III                                               #
#  NNN  NNNNNN        SSSS   III    Cours Python - 1ère - v.3.5                #
#  NNN   NNNNN  SSSS  SSSS   III                                               #
#  NNN    NNNN   SSSSSSSS   IIIII                                              #
#                                                                              #
################################################################################
#               #                                                              #
#  Part. 0      #  intro - lancer Python - commentaires                        #
#               #                                                              #
################################################################################

#####################################
#                                   #
# 0. Introduction                   #
# 1. Lancer Python                  #
# 2. Comment aborder ce tutoriel    #
# 3. Commentaires                   #
#                                   #
#####################################

#####################################
# 0. Introduction                   #
#####################################
#
#  - Le langage Python
#  - Python en NSI
#
#####################################

# Le langage Python
####################

"""
Python est un langage de programmation interprété créé à la fin des années 80
par Guido van Rossum (GVR). Il a été rendu public en 1991, sous license open
source (n'importe qui peut lire le code de Python puis le modifier pour
lui-même, le redistribuer, etc.).

Son nom est un hommage à la troupe britannique des Monty Python (1969-1983).

Les objectifs du langage, d'après GVR :
    - être intuitif et (presque) aussi lisible que l'anglais
    - rester raisonnablement rapide à exécuter
    - être open source, pour que chacun puisse proposer des contributions
    - pouvoir être utilisé pour les petites tâches de tous les jours (scripting)

C'est un des langage les plus populaires au monde, utilisé dans énormément
de domaines : sciences, statistiques, finance, robotique, scripting, réseau,
Web, traitement d'images, IA...

La plupart des grandes organisations (CERN, NASA, Google, gouvernements)
l'utilisent pour l'un ou l'autre de leurs projets. Instagram, DropBox, Spotify,
Pinterest, Youtube... sont des sites qui sont ou ont commencé en Python ! [0][1]

[0] https://djangostars.com/blog/10-popular-sites-made-on-django
[1] https://thenewstack.io/instagram-makes-smooth-move-python-3

Même si l'interpréteur Python est lui-même programmé en C (un des langages les
plus rapides qui soient), l'exécution de Python est plus lente que celle
d'autres langages. Qu'importe ! sa simplicité compense largement ce point. Et
de toute façon, on verra que la plupart des programmes n'ont pas besoin d'une
exécution immédiate pour être utiles...
"""


# Python en NSI
################

"""
La spécialité NSI existe en France depuis la rentrée 2019. Elle utilise Python
pour l'essentiel de la partie algorithmique du programme. En effet, même si
Python est très logique et facile d'utilisation pour les débutants, il est aussi
extrêmement efficace et performant (en plus d'être utilisé partout).

La spécialité NSI suppose que vous ne savez pas programmer en commençant
l'année : nous partirons donc de 0 en expliquant un certain nombre de concepts
universels de programmation.

En conséquence, il y aura dans ce tutoriel trois types d'apprentissage :
    1. sur le langage Python
    2. sur la programmation en général
    3. sur d'autres langages (SQL, JavaScript, HTML/CSS...)

Nous verrons que beaucoup de constructions que nous verrons avec Python cette année sont en fait communes à tous les langages.
"""


###################################
# 1. Lancer Python                #
###################################
#
#  - Via l'interpréteur Python
#  - Depuis un fichier
#  - Depuis un éditeur de texte
#  - Via un site Web
#
###################################

"""
Python est à la fois :
    - un langage de programmation...
    - ...et un programme qui va exécuter du code écrit dans ce langage.

IMPT : Il y a quatre façons de programmer avec Python :

    1. soit directement via l'interpréteur (ou "shell") Python,
    2. soit en lançant un fichier contenant du code Python,
    3. soit depuis un programme externe, comme un éditeur de texte,
    4. soit via une interface Web.
"""

# Via l'interpréteur Python
############################

"""
L'interpréteur permet de tester des commandes Python et d'y exécuter
de petits programmes. Les commandes tapées ne sont pas enregistrées,
donc on ne pourra pas y écrire de programmes sophistiqués.

Pour lancer l'interpréteur depuis une ligne de commandes :
> python
Python 3.9.1 (default, Dec 24 2020, 15:57:37)
>>> <votre code suivi de return>

Vous pouvez alors lancer des commandes Python directement
>>> x = 2
>>> print(3 + x)
5

On appelle ce signe ">>>" une "invite de commande" (ou "prompt" en anglais).
Il signifie que l'exécution du code précédent est achevée et que vous
pouvez maintenant taper du nouveau code à exécuter.

Note : Pour quitter l'interpréteur Python, on utilise quit()
>>> quit()
...et on revient au shell !

Attention à ne pas confondre le shell de l'ordinateur et le shell Python : le
shell Python a un prompt caractéristique : ">>> ".
"""


# Depuis un fichier
####################

"""
Le code Python se trouve dans des fichiers avec le suffixe ".py" : engine.py,
questionnaire.py, etc.

Pour lancer un programme contenant du code Python, on l'appelle avec :
> python mon_fichier.py

IMPT : il faut utiliser Python 3 pour vos projets. Tapez cette
commande dans un terminal pour connaître votre version
> python --version

Si la version retournée est 2.X.YY, essayez de lancer Python 3 avec
> python3

Si Python3 n'est pas installé, installez-le ! Vous perdrez beaucoup moins de
temps qu'en devant gérer les différences entre Python 2 et Python 3...
"""


# Depuis un éditeur de texte
#############################

"""
Il est aussi possible de lancer Python depuis un éditeur de texte : Sublime
Text, Visual Studio, etc., proposent cette option.

Pour cela, il faut lancer l'interprétation du code depuis une option de
l'éditeur. Sur Sublime Text, c'est Ctrl + B (ou Cmd + B sur Mac) : on appelle
cette opération un "build". Le résultat de l'exécution apparaîtra dans une
fenêtre à part.
"""


# Via un site Web
##################

"""
Dernière possibilité : coder en utilisant une plate-forme en ligne, type Repl.it
(https://repl.it). On codera alors sans quitter son navigateur Web, et sans
avoir besoin d'installer Python sur son ordinateur.

Avantages :
    1. pas besoin d'avoir Python sur son ordinateur,
    2. la version est forcément la bonne.

Inconvénients :
    1. on a besoin d'une connexion internet,
    2. l'exécution peut être plus lente que sur son propre ordinateur (mauvaise
       connexion, latence...)
    3. pour conserver le code écrit sur son ordinateur, il faudra ensuite le
       copier/coller dans des fichiers locaux

Si l'on peut, il est conseillé de coder "en local", c'est-à-dire directement sur
son ordinateur sans passer par internet, et de n'utiliser Repl.it que pour
dépanner.
"""


#####################################
# 2. Comment aborder ce tutoriel    #
#####################################
#
#  - Que faut-il ?
#  - Comment utiliser ce tutoriel ?
#  - Comment travailler ?
#
#####################################

# Que faut-il ?
################

"""
Ce tutoriel a vocation a être lu sur un ordinateur, pour pouvoir exécuter et
tester directement le code proposé. Il vous faut donc un ordinateur, idéalement
sous Linux, BSD ou Mac.

Il est aussi pensé pour être ouvert depuis un éditeur de texte proposant une
coloration syntaxique (vim, Emacs, Sublime Text, PyCharm, VS Code, Notepad++,
gedit, etc.). Nous recommandons Sublime Text.

Nous rappelons que Microsoft Word n'est pas un éditeur de texte, mais un
éditeur de mise en forme de texte. Vous ne pouvez pas vous en servir pour
écrire du code.

Les fichiers de ce cours sont exécutables, càd que vous pouvez les lancer avec
un interpréteur Python (mode 2, voir plus haut) via la commande :
?> python ce_fichier.py

Enfin tout le cours utilise Python 3.6+ (c'est-à-dire la version 3, et au moins
la sous-version 6).
"""


# Comment utiliser ce tutoriel ?
#################################

"""
La meilleure façon est de lire le cours et de retaper le code proposé dans un
shell Python.

Cela semble long, mais c'est taper du code qui vous donnera de la pratique :
rapidité, fluidité et acquisition d'automatismes. À la fin de l'année, les
meilleurs élèves ne seront pas les plus doués, mais... ceux qui auront le plus
pratiqué.

Taper les exemples dans une console vous permettra de vérifier les appels à
print(). Vous pourrez ensuite exécuter le fichier du cours pour comparer ce qui
est imprimé.

Note 1 : La fonction intégrée print() de Python permet d'afficher à l'écran le
résultat d'un calcul (voir chap. 7). Nous l'utiliserons dans tout ce cours.
Vous pouvez ainsi vérifier la plupart des calculs passés à print() : les
résultats des appels sont mis en commentaires en fin de ligne.
"""
print(1 + 2)             # => 3
print("abc")             # => abc
print(["une", "liste"])  # => ['une', 'liste']

"""
Note 2 : dans certains fichiers, des erreurs intentionnelles ont été laissées
dans le code. Elles sont signalées dans le code. On utilise un mécanisme de
gestion d'erreurs ("try ... except ...") pour empêcher ces erreurs
d'interrompre le programme. Ce mécanisme n'est pas à connaître au début : il
sera abordé en détail au chap. 23.
"""
try:
    1 / 0   # la division par 0 va créer une erreur...
except ZeroDivisionError as err:
    # ... mais cette erreur est "interceptée" : le programme continue.
    print(f"1: (Sans ce try: ... except ..., cette ligne créerait : {err})")

"""
Notez que les affichages d'erreurs sont numérotés : vous pourrez donc les
identifier plus tard dans la console.

Note 3 : les points importants sont notés "IMPT" et vous devez absolument les
connaître. Les points hors-programme de NSI sont notés "HP" : ils sont laissés
pour votre curiosité uniquement.
"""


# Comment travailler ?
#######################

"""
Vous aurez souvent besoin de vous repasser mentalement le "film" du programme, pas à pas. Prenez l'habitude de simuler DANS VOTRE TÊTE son fonctionnement :

    - Identifiez le flux du programme : y a-t-il des conditionnels (chap. 12) ?
      des boucles (chap. 13) ? des appels de fonctions (chap. 14) ?
    - Déterminez la valeur de chaque variable utilisée à chaque ligne du
      programme, y compris pour des types construits (chap. 16).
    - Demandez-vous, à chaque appel de fonction, ce que valent ses paramètres.
      Remplacez mentalement les paramètres de fonction par les valeurs utilisées.
    - Après être passé dans la fonction, déterminez sa valeur de retour. Cette
      valeur est-elle conservée par la fonction appelante ?
    - Au besoin, modifiez le programme proposé : testez avec d'autres valeurs,
      d'autres combinaisons, et exécutez le nouveau programme. Testez, testez,
      testez !

Cela vous prendra beaucoup de temps et d'efforts au début, puis de moins en
moins. Un·e bon·ne programmeur·se doit pouvoir remplacer l'ordinateur et faire
"tourner" un programme de tête !

Concernant le cours : prenez l'habitude de piocher au cas par cas dans chaque
chapitre, en prenant ce dont vous avez besoin. N'hésitez pas à lire le cours en diagonale, tester un morceau de code, puis revenir au cours pour revoir un
détail ou un exemple.

Python a beaucoup de fonctionnalités : n'essayez pas de tout apprendre tout de
suite, et concentrez-vous sur ce dont vous avez besoin. Vous apprendrez plus
vite et avec moins d'efforts.
"""


###################################
# 3. Commentaires                 #
###################################
#
#  - Commentaires simples
#  - Commentaires longs
#
###################################

# Commentaires simples
#######################

# Un commentaire de ligne commence par un dièse (#), souvent suivi
# d'une espace. On peut commenter une ligne de code en insérant un "#" au début.
# La ligne ne sera alors plus considérée comme du code, mais comme du texte.
# Elle ne sera plus exécutée.

# Ainsi, ce fichier de tutoriel est du code Python, mais toute la mise en
# forme du texte est réalisée avec des commentaires !

# Il peut être pratique de laisser du code sous forme commentée, pour pouvoir
# le décommenter plus tard si besoin.

# La plupart des éditeurs proposent un raccourci clavier pour commenter son
# code.

# Bien commenter son code est souvent utile, mais rarement indispensable.
# En général, si on écrit du code clair et qui utilise des noms de variables et
# de fonctions explicites, on pourra (presque) se passer de commentaires.

# Commenter peut néanmoins être utile pour rappeler une difficulté que l'on a
# rencontrée en codant (et que l'on a peur d'oublier).


# Commentaires longs
#####################

"""
On peut aussi faire des commentaires longs avec trois guillemets doubles. On
n'est alors plus obligé de répéter # à chaque début de ligne.

Ce format de commentaire est fréquent en introduction de fonction, pour annoncer
ce que fait le code introduit (docstring).

On finira ensuite le commentaire de la même façon, comme ceci :
"""
