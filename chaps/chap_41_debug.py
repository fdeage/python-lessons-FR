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
#  Chap. 41     #  Débogage                                                    #
#               #                                                              #
################################################################################
#
#  - Qu'est-ce qu'un bug ?
#  - La démarche de débogage
#  - Les trois familles de bugs
#  - Lire un traceback
#  - Afficher un traceback sans planter
#  - Déboguer avec print()
#  - assert comme garde-fou
#  - Réduire au cas minimal
#  - La bisection
#  - La méthode du canard en plastique
#  - Le débogueur pdb
#  - breakpoint() et PYTHONBREAKPOINT
#  - Le débogage post-mortem
#  - Le débogueur de son éditeur
#  - Les bugs classiques du débutant
#  - En bref
#
#############################################

import traceback

# Qu'est-ce qu'un bug ?
########################

"""
Un "bug" (en français : un "bogue") est un défaut dans un programme : il ne
fait pas ce que l'on attend de lui. Il peut planter, afficher un résultat
faux, tourner à l'infini, ou… marcher 99 fois et échouer la 100e.

L'histoire raconte qu'en 1947, l'équipe de Grace Hopper (une pionnière de
l'informatique) a trouvé un vrai insecte ("bug" en anglais), un papillon de
nuit coincé dans un relais de leur ordinateur, le Harvard Mark II. Il a été
collé dans le cahier de bord avec la mention "First actual case of bug being
found". Le mot existait déjà chez les ingénieurs, mais l'anecdote est restée.

"Déboguer" (to debug), c'est trouver et corriger ces défauts.

IMPT : tout le monde écrit des bugs, les débutants comme les experts. La
différence, c'est que les experts ont une MÉTHODE pour les trouver vite. Ce
chapitre vous donne cette méthode et les outils qui vont avec.

On a déjà vu les erreurs et les exceptions au chap. 26 : relisez-le si
besoin, ce chapitre s'appuie dessus.
"""


# La démarche de débogage
##########################

"""
Face à un bug, le réflexe du débutant est de modifier le code un peu au
hasard "pour voir si ça marche". C'est la pire méthode : on perd du temps,
et on finit souvent avec deux bugs au lieu d'un.

Un débogage efficace ressemble à une enquête scientifique, en 4 étapes :

    1. REPRODUIRE : trouver une façon de déclencher le bug à coup sûr.
       Quelles données ? Quelle suite d'actions ? Un bug que l'on ne sait pas
       reproduire est presque impossible à corriger… et on ne pourra pas
       vérifier qu'il est corrigé !

    2. ISOLER : réduire la zone suspecte. Dans quelle fonction ? À quelle
       ligne la valeur devient-elle fausse ? (cf. plus bas : "Réduire au cas
       minimal" et "La bisection")

    3. FORMULER UNE HYPOTHÈSE : "je pense que la variable total n'est pas
       remise à 0 entre deux appels". Une hypothèse doit être précise et
       vérifiable.

    4. VÉRIFIER : afficher la valeur (print), poser un assert, utiliser le
       débogueur… Si l'hypothèse est fausse, on en formule une autre. Si elle
       est juste, on corrige, puis on vérifie que le bug a disparu ET que
       rien d'autre n'est cassé (les tests du chap. 29 et 37 sont là pour ça).

Conseil : notez vos hypothèses (sur papier ou dans un commentaire). Cela
évite de tourner en rond en testant trois fois la même idée.

Bonus : une fois le bug corrigé, écrivez un test qui l'aurait détecté
(cf. chap. 37). On appelle cela un test de non-régression : le bug ne pourra
plus revenir sans que l'on s'en aperçoive.
"""


# Les trois familles de bugs
#############################

"""
1. Les erreurs de SYNTAXE (SyntaxError, IndentationError) : le code n'est pas
   du Python valide. Python refuse de lancer le programme, et indique la
   ligne fautive. Ce sont les plus faciles à corriger.

2. Les erreurs d'EXÉCUTION (TypeError, KeyError, ZeroDivisionError…) : le
   code est valide, mais une instruction échoue pendant l'exécution. Python
   s'arrête et affiche un "traceback" (cf. section suivante).

3. Les erreurs de LOGIQUE : le programme tourne jusqu'au bout sans aucune
   erreur… mais le résultat est faux. Ce sont les plus sournoises, car Python
   ne vous signale rien du tout : c'est à vous de vous en apercevoir.

Exemple de chaque famille :
"""
# 1. Syntaxe : on ne peut pas l'écrire directement dans ce fichier (il ne se
# lancerait plus du tout !). On la montre avec compile() (cf. chap. 26) :
try:
    compile("print('bonjour'", "<exemple>", "exec")
except SyntaxError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : '(' was never
# closed (<exemple>, line 1))

# 2. Exécution :
prix = {"pomme": 2.5, "poire": 3.0}
try:
    print(prix["banane"])
except KeyError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err!r})")
# => 2: (Sans ce try: … except …, cette ligne créerait : KeyError('banane'))


# 3. Logique : on veut la moyenne de 3 notes…
def moyenne_fausse(a, b, c):
    return a + b + c / 3   # … mais la priorité des opérateurs (cf. chap. 5)


print(moyenne_fausse(10, 12, 14))  # => 26.666666666666668 (au lieu de 12.0)
# Aucune erreur, aucun message : seul notre œil peut repérer le problème.
# Correction : (a + b + c) / 3


# Lire un traceback
####################

"""
Quand une exception n'est pas interceptée, Python affiche un "traceback"
(littéralement : la "trace en arrière"). Beaucoup de débutants le trouvent
effrayant et ne le lisent pas. C'est une erreur : le traceback contient
presque toujours la réponse !

Prenons ce programme, qui calcule la moyenne de chaque classe :

    def moyenne(notes):
        return sum(notes) / len(notes)

    def moyennes_par_classe(classes):
        resultat = {}
        for nom, notes in classes.items():
            resultat[nom] = moyenne(notes)
        return resultat

    classes = {"6eA": [12, 15, 9], "6eB": []}
    print(moyennes_par_classe(classes))

Il affiche :

    Traceback (most recent call last):
      File "/home/ada/cours/stats.py", line 11, in <module>
        print(moyennes_par_classe(classes))
              ~~~~~~~~~~~~~~~~~~~^^^^^^^^^
      File "/home/ada/cours/stats.py", line 7, in moyennes_par_classe
        resultat[nom] = moyenne(notes)
                        ~~~~~~~^^^^^^^
      File "/home/ada/cours/stats.py", line 2, in moyenne
        return sum(notes) / len(notes)
               ~~~~~~~~~~~^~~~~~~~~~~~
    ZeroDivisionError: division by zero

Comment le lire :

    1. IMPT : on commence par la DERNIÈRE ligne. Elle donne le TYPE de
       l'erreur (ZeroDivisionError) et un MESSAGE (division by zero). C'est
       l'information la plus importante.

    2. On remonte ensuite d'un cran : le dernier bloc "File …" indique OÙ
       l'erreur s'est produite : fichier stats.py, ligne 2, dans la fonction
       moyenne, sur l'instruction "return sum(notes) / len(notes)". Les ~~~^^^
       (Python 3.11+) soulignent même l'opération exacte : la division.

    3. Les blocs au-dessus forment la PILE D'APPELS ("call stack") : ils
       disent COMMENT on est arrivé là. Lus de haut en bas, ils suivent
       l'ordre des appels : le module principal (<module>) a appelé
       moyennes_par_classe() à la ligne 11, qui a appelé moyenne() à la
       ligne 7. D'où le titre "most recent call last" : l'appel le plus
       récent est en dernier.

Conclusion de l'enquête : moyenne() a reçu une liste vide (la classe 6eB),
et len([]) vaut 0. Le bug n'est pas forcément dans la fonction qui plante :
ici, la vraie question est "que doit-on faire d'une classe sans notes ?".

Note : l'erreur se produit souvent dans du code que l'on n'a pas écrit (une
fonction de pandas, par exemple). Dans ce cas, cherchez dans la pile le
DERNIER bloc qui concerne VOTRE fichier : c'est là que vous avez transmis une
mauvaise valeur.

Astuce : copiez la dernière ligne du traceback dans un moteur de recherche.
Quelqu'un a presque toujours rencontré la même erreur avant vous.
"""


# Afficher un traceback sans planter
#####################################

"""
Parfois, on veut intercepter une erreur (pour que le programme continue)
tout en gardant le traceback pour le comprendre. Le module "traceback" de la
bibliothèque standard (importé en haut de ce fichier) sert à cela.
"""


def moyenne(notes):
    return sum(notes) / len(notes)


def moyennes_par_classe(classes):
    resultat = {}
    for nom, notes in classes.items():
        resultat[nom] = moyenne(notes)
    return resultat


classes = {"6eA": [12, 15, 9], "6eB": []}
try:
    moyennes_par_classe(classes)
except ZeroDivisionError as err:
    # traceback.format_exc() renvoie le traceback complet sous forme de
    # string, exactement comme Python l'aurait affiché :
    texte = traceback.format_exc()
    # On n'affiche que la dernière ligne (les chemins de fichiers dépendent
    # de votre ordinateur) :
    print(texte.splitlines()[-1])  # => ZeroDivisionError: division by zero

    # extract_tb() découpe le traceback en "cadres" (frames), un par appel.
    # On peut ainsi lister les fonctions traversées, dans l'ordre :
    cadres = traceback.extract_tb(err.__traceback__)
    print([cadre.name for cadre in cadres])
    # => ['<module>', 'moyennes_par_classe', 'moyenne']
    print(cadres[-1].line)  # => return sum(notes) / len(notes)

"""
Dans un vrai programme, on écrirait plutôt :

    except ZeroDivisionError:
        traceback.print_exc()   # affiche le traceback complet, sans planter

ou, mieux, on l'enverrait dans un journal avec logger.exception(), que l'on
verra au chap. 44 (Logging).
"""


# Déboguer avec print()
########################

"""
La technique la plus simple, et souvent la plus efficace : afficher les
valeurs des variables aux endroits stratégiques, pour vérifier qu'elles
valent bien ce que l'on croit.

Exemple : cette fonction doit compter les notes au-dessus de la moyenne,
mais renvoie toujours 0.
"""


def nb_au_dessus(notes):
    moy = sum(notes) / len(notes)
    compte = 0
    for note in notes:
        if note > moy:
            compte = 1      # le bug est ici… mais faisons comme si on ne le
    return compte * 0       # voyait pas (le "* 0" est un 2e bug, exprès)


print(nb_au_dessus([8, 12, 15, 9]))  # => 0 (on attendait 2)

"""
On ajoute des print() pour suivre l'exécution. Depuis Python 3.8, la syntaxe
f"{variable=}" affiche à la fois le NOM et la VALEUR : très pratique !
"""


def nb_au_dessus_debug(notes):
    moy = sum(notes) / len(notes)
    print(f"{moy=}")
    compte = 0
    for note in notes:
        if note > moy:
            compte = 1
        print(f"  {note=} {compte=}")
    print(f"{compte=} avant le return")
    return compte * 0


nb_au_dessus_debug([8, 12, 15, 9])
# => moy=11.0
# =>   note=8 compte=0
# =>   note=12 compte=1
# =>   note=15 compte=1
# =>   note=9 compte=1
# => compte=1 avant le return

"""
Les affichages révèlent les deux bugs :
    - compte reste à 1 au lieu d'augmenter : il fallait "compte += 1",
    - le return renvoie 0 alors que compte vaut 1 : le "* 0" est en trop.

Quelques conseils pour déboguer avec print() :

    - Affichez aussi le TYPE quand vous avez un doute : "12" et 12 se
      ressemblent beaucoup à l'écran !
    - Utilisez repr() (ou !r dans une f-string) pour voir les espaces et les
      caractères invisibles : print("Lyon ") et print("Lyon") donnent le même
      affichage, mais pas leur repr().
    - Préfixez vos affichages ("DEBUG", ">>>") pour les retrouver facilement…
      et SUPPRIMEZ-LES une fois le bug corrigé.
    - Si vous avez besoin de ces messages durablement, utilisez plutôt le
      module logging (cf. chap. 44).
"""
ville = "Lyon "            # un espace en trop, invisible à l'œil nu
print(ville, "|")          # => Lyon  |
print(f"{ville=}")         # => ville='Lyon '  (les guillemets le révèlent)
print(repr(ville))         # => 'Lyon '
print(ville == "Lyon")     # => False

age = "12"
print(age, type(age))      # => 12 <class 'str'>
print(f"{age!r}")          # => '12'  (c'est une string, pas un entier !)


# assert comme garde-fou
#########################

"""
On a vu assert au chap. 29 pour écrire des tests. On peut aussi l'utiliser
DANS le code, pour vérifier qu'une condition que l'on croit toujours vraie
l'est réellement. Si elle est fausse, le programme s'arrête immédiatement,
au plus près de la cause du problème, au lieu de continuer avec une valeur
fausse et de planter (ou pire, de se tromper) beaucoup plus loin.
"""


def taux_reussite(nb_admis, nb_candidats):
    assert nb_candidats > 0, f"nb_candidats doit être > 0, reçu {nb_candidats}"
    assert 0 <= nb_admis <= nb_candidats, f"nb_admis incohérent : {nb_admis}"
    return nb_admis / nb_candidats


print(taux_reussite(30, 40))  # => 0.75
try:
    taux_reussite(50, 40)     # une erreur de saisie : plus d'admis que de
except AssertionError as err:  # candidats
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 3: (Sans ce try: … except …, cette ligne créerait : nb_admis incohérent :
# 50)

"""
Attention :
    - assert sert à détecter les ERREURS DE PROGRAMMATION ("ça ne devrait
      jamais arriver"). Pour vérifier les données d'un utilisateur, on lève
      une vraie exception (raise ValueError(…), cf. chap. 26).
    - Les assert sont désactivés si l'on lance Python avec l'option -O
      ("optimize") : on ne doit donc jamais compter sur eux pour la logique
      du programme.
"""


# Réduire au cas minimal
#########################

"""
Quand un bug apparaît sur un gros jeu de données (un CSV de 10 000 lignes,
par exemple), on essaie de le reproduire avec le PLUS PETIT exemple possible.
C'est ce qu'on appelle un "exemple minimal reproductible" (en anglais :
"minimal reproducible example", ou MRE).

Méthode :
    1. Copiez le code dans un fichier à part (ou une cellule de notebook).
    2. Remplacez les données par quelques valeurs écrites à la main.
    3. Supprimez petit à petit tout ce qui n'est pas nécessaire pour
       déclencher le bug : si le bug persiste, la partie supprimée n'était
       pas en cause.
    4. Arrêtez-vous quand plus rien ne peut être retiré.

Souvent, le bug devient évident en cours de route. Sinon, vous avez un
exemple de 5 lignes à montrer à un collègue ou à poster sur un forum : c'est
d'ailleurs exigé sur les forums comme Stack Overflow.

Exemple : sur un fichier de ventes, le total est faux. En réduisant, on
arrive à ceci :
"""
ventes = ["12.5", "7.5", "10"]   # des valeurs lues dans un fichier : des str !
total = ""
for v in ventes:
    total += v
print(total)  # => 12.57.510  (concaténation au lieu d'addition)
# Le cas minimal rend le bug évident : il manque une conversion float(v).
total = 0
for v in ventes:
    total += float(v)
print(total)  # => 30.0


# La bisection
###############

"""
Quand on ne sait pas du tout où se trouve le bug dans un long programme, on
peut le chercher par "bisection" (on coupe en deux), comme on cherche un mot
dans un dictionnaire :

    1. On place un print() (ou un assert) au MILIEU du programme pour
       vérifier si les données sont encore correctes à cet endroit.
    2. Si elles sont correctes, le bug est dans la 2e moitié ; sinon, il est
       dans la 1re.
    3. On recommence dans la moitié fautive.

Avec un programme de 1000 lignes, il suffit d'une dizaine d'étapes pour
trouver LA ligne fautive (1000 → 500 → 250 → … → 1). C'est le même principe
que la recherche dichotomique, dont on étudiera l'efficacité au chap. 45.

Variante : commenter la moitié du code (cf. chap. 3) et voir si le bug
persiste.

Bonus : la même idée existe dans le TEMPS. Si votre programme marchait la
semaine dernière et plus aujourd'hui, l'outil "git bisect" (du logiciel de
gestion de versions git) teste automatiquement les versions intermédiaires
de votre code pour trouver la modification qui a introduit le bug.
"""


# La méthode du canard en plastique
####################################

"""
Une technique très sérieuse malgré son nom ("rubber duck debugging") :
expliquez votre code, ligne par ligne, À VOIX HAUTE, à un canard en
plastique posé sur votre bureau (ou à une plante, ou à un collègue patient).

En vous forçant à expliquer ce que fait CHAQUE ligne, vous vous apercevez
souvent qu'elle ne fait pas ce que vous pensiez. Le canard n'a rien dit,
mais le bug est trouvé !

C'est aussi pour cela qu'il est utile d'écrire sa question sur un forum :
souvent, on trouve la réponse en la rédigeant.
"""


# Le débogueur pdb
###################

"""
Un DÉBOGUEUR est un outil qui permet de mettre le programme en PAUSE à une
ligne donnée, puis d'avancer instruction par instruction en inspectant les
variables. C'est comme un print() géant, mais interactif : pas besoin de
relancer le programme à chaque nouvelle question.

Python fournit un débogueur en ligne de commande : pdb ("Python DeBugger").
Pour mettre le programme en pause, on ajoute la ligne :

    breakpoint()        # (Python 3.7+ ; avant : import pdb; pdb.set_trace())

à l'endroit voulu. Quand l'exécution atteint cette ligne, le programme
s'arrête et affiche une invite "(Pdb)" où l'on tape des commandes.

Les commandes essentielles (il suffit de taper la première lettre) :

    p expr      "print" : affiche la valeur d'une expression (p total)
    pp expr     "pretty print" : idem, joliment présenté (dicts, listes)
    l           "list" : affiche le code autour de la ligne courante
    n           "next" : exécute la ligne courante et passe à la suivante
                (si la ligne appelle une fonction, on ne rentre pas dedans)
    s           "step" : comme n, mais RENTRE dans les fonctions appelées
    c           "continue" : reprend l'exécution normale jusqu'au prochain
                breakpoint() (ou jusqu'à la fin)
    w           "where" : affiche la pile d'appels (comme un traceback)
    u / d       "up" / "down" : remonte / descend dans la pile d'appels pour
                inspecter les variables de la fonction appelante
    b n         "break" : ajoute un point d'arrêt à la ligne n
    q           "quit" : arrête le programme
    h           "help" : la liste des commandes

On peut aussi taper n'importe quelle expression Python : total * 2,
len(notes), notes[-1]… et même modifier une variable : total = 0.

Exemple de session. Le programme :

     1  def total_panier(prix, quantites):
     2      total = 0
     3      for p, q in zip(prix, quantites):
     4          breakpoint()
     5          total = p * q
     6      return total
     7
     8  print(total_panier([2.5, 4.0], [2, 3]))

La session (ce que l'on tape est après "(Pdb)") :

    > /home/ada/panier.py(4)total_panier()
    -> breakpoint()
    (Pdb) p p, q, total
    (2.5, 2, 0)
    (Pdb) n
    > /home/ada/panier.py(5)total_panier()
    -> total = p * q
    (Pdb) n
    > /home/ada/panier.py(3)total_panier()
    -> for p, q in zip(prix, quantites):
    (Pdb) p total
    5.0
    (Pdb) c
    > /home/ada/panier.py(4)total_panier()
    -> breakpoint()
    (Pdb) n
    > /home/ada/panier.py(5)total_panier()
    -> total = p * q
    (Pdb) p p, q, total
    (4.0, 3, 5.0)
    (Pdb) n
    > /home/ada/panier.py(3)total_panier()
    -> for p, q in zip(prix, quantites):
    (Pdb) p total
    12.0
    (Pdb) q

(La flèche "->" montre la PROCHAINE ligne à exécuter. Avant Python 3.13, pdb
s'arrêtait directement sur la ligne qui SUIT le breakpoint(). Selon la
version, q peut demander une confirmation : répondez y.)

Au 2e passage, total passe de 5.0 à 12.0 au lieu de 17.0 : la ligne 5 écrase
le total au lieu de l'augmenter. Il fallait écrire "total += p * q".

IMPT : n'oubliez jamais un breakpoint() dans votre code une fois le bug
corrigé : le programme s'arrêterait chez tous ses utilisateurs !
"""


# breakpoint() et PYTHONBREAKPOINT
###################################

"""
Ce fichier doit pouvoir s'exécuter jusqu'au bout sans s'arrêter : on ne
peut donc pas y laisser un breakpoint() "actif". Mais il existe une variable
d'environnement, PYTHONBREAKPOINT, qui contrôle ce que fait breakpoint() :

    PYTHONBREAKPOINT=0 python3 mon_programme.py

lance le programme en IGNORANT tous les breakpoint(). Pratique pour
exécuter d'une traite un programme truffé de points d'arrêt.

(D'autres valeurs permettent d'utiliser un autre débogueur, par exemple
PYTHONBREAKPOINT=ipdb.set_trace pour ipdb, un pdb plus confortable.)

breakpoint() relit cette variable à CHAQUE appel. On peut donc la modifier
depuis le programme lui-même, via os.environ (cf. chap. 22) :
"""
import os

ancienne_valeur = os.environ.get("PYTHONBREAKPOINT")
os.environ["PYTHONBREAKPOINT"] = "0"    # désactive les points d'arrêt

for i in range(3):
    breakpoint()                        # ignoré : le programme continue
print("Les 3 breakpoint() ont été ignorés")
# => Les 3 breakpoint() ont été ignorés

# On remet l'environnement dans son état d'origine :
if ancienne_valeur is None:
    del os.environ["PYTHONBREAKPOINT"]
else:
    os.environ["PYTHONBREAKPOINT"] = ancienne_valeur


# Le débogage post-mortem
##########################

"""
Le programme a planté, et vous auriez aimé voir les variables AU MOMENT du
plantage ? C'est le débogage "post-mortem" (après la mort du programme).

    python3 -m pdb mon_programme.py

lance le programme sous le contrôle de pdb. Il s'arrête d'abord à la
première ligne (tapez c pour continuer). Si une exception non interceptée se
produit, au lieu de quitter, pdb s'arrête sur la ligne qui a planté : on
peut alors inspecter toutes les variables (p, pp), remonter la pile (u, w)…

Variante, dans l'interpréteur interactif ou un notebook, juste après une
erreur :

    >>> import pdb
    >>> pdb.pm()        # "post mortem" : ouvre pdb là où l'erreur a eu lieu

Dans Jupyter, la commande magique %debug fait la même chose.
"""


# Le débogueur de son éditeur
##############################

"""
pdb fonctionne partout (même sur un serveur sans interface graphique), mais
les éditeurs modernes (VS Code, PyCharm, Spyder…) proposent un débogueur
graphique, souvent plus confortable. Le principe est exactement le même :

    - Point d'arrêt ("breakpoint") : on clique dans la marge, à gauche du
      numéro de ligne. Un point rouge apparaît. Pas besoin de modifier le
      code !
    - On lance le programme en mode débogage (VS Code : touche F5, ou
      "Run > Start Debugging" ; PyCharm : l'icône d'insecte).
    - Le programme s'arrête au point rouge. Une barre d'outils permet
      d'avancer :
          "Step Over" (F10)   ⇔ n dans pdb
          "Step Into" (F11)   ⇔ s
          "Step Out"          sortir de la fonction courante
          "Continue" (F5)     ⇔ c
    - Un panneau "Variables" affiche en permanence toutes les variables
      locales et globales, avec leur valeur (on peut déplier les listes et
      les dictionnaires).
    - Un panneau "Watch" permet de suivre une expression choisie (total * 2,
      len(notes)…).
    - Le panneau "Call Stack" affiche la pile d'appels : un clic sur une
      ligne montre les variables de la fonction correspondante.
    - Points d'arrêt CONDITIONNELS (clic droit sur le point rouge) : on ne
      s'arrête que si une condition est vraie, par exemple i == 500. Très
      utile dans une boucle qui ne plante qu'au 500e tour !

IMPT : apprenez à utiliser le débogueur de votre éditeur. C'est un
investissement de 30 minutes qui vous fera gagner des heures.
"""


# Les bugs classiques du débutant
##################################

"""
Voici les bugs que l'on rencontre le plus souvent en apprenant Python, avec
leur symptôme et leur correction. Apprenez à les reconnaître : ils vous
feront gagner beaucoup de temps.
"""

# 1. "=" au lieu de "==" dans une condition
#    Symptôme : SyntaxError. Python 3.10+ suggère même la correction.
try:
    compile("if x = 3:\n    pass", "<exemple>", "exec")
except SyntaxError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err.msg})")
# => 4: (Sans ce try: … except …, cette ligne créerait : invalid syntax. Maybe
# you meant '==' or ':=' instead of '='?)


# 2. Une mauvaise indentation : le return est DANS la boucle
#    Symptôme : la fonction s'arrête au premier tour (bug de logique).
def somme_fausse(nombres):
    total = 0
    for n in nombres:
        total += n
        return total        # indenté d'un cran de trop !


def somme(nombres):
    total = 0
    for n in nombres:
        total += n
    return total            # après la boucle


print(somme_fausse([1, 2, 3]), somme([1, 2, 3]))  # => 1 6


# 3. L'erreur "off-by-one" (décalage de un)
#    Symptôme : il manque le dernier élément (ou il y en a un de trop).
#    On veut la somme des entiers de 1 à 10 :
print(sum(range(1, 10)))   # => 45 : range(1, 10) s'arrête à 9 (cf. chap. 13)
print(sum(range(1, 11)))   # => 55 : correct

notes = [12, 15, 9]
try:
    for i in range(len(notes) + 1):  # un tour de trop
        notes[i]
except IndexError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 5: (Sans ce try: … except …, cette ligne créerait : list index out of
# range)


# 4. Une liste comme valeur par défaut d'un paramètre
#    Symptôme : la liste "se souvient" des appels précédents.
#    La valeur par défaut est créée UNE SEULE FOIS, à la définition de la
#    fonction (cf. chap. 15), et partagée par tous les appels.
def ajouter_note_fausse(note, notes=[]):
    notes.append(note)
    return notes


print(ajouter_note_fausse(12))  # => [12]
print(ajouter_note_fausse(15))  # => [12, 15]  (on attendait [15] !)


def ajouter_note(note, notes=None):
    if notes is None:           # la bonne pratique : None par défaut, puis
        notes = []              # une NOUVELLE liste à chaque appel
    notes.append(note)
    return notes


print(ajouter_note(12))  # => [12]
print(ajouter_note(15))  # => [15]


# 5. Modifier une liste pendant qu'on la parcourt (cf. chap. 24)
#    Symptôme : des éléments sont "sautés".
#    On veut supprimer les notes sous la moyenne (10) :
notes = [5, 3, 12, 8]
for note in notes:
    if note < 10:
        notes.remove(note)
print(notes)  # => [3, 12]  (le 3 a été sauté !)
# Quand on supprime le 5, tout se décale : le 3 prend sa place (indice 0),
# mais la boucle passe à l'indice 1… et ne voit jamais le 3.
# Correction : construire une NOUVELLE liste (cf. chap. 23).
notes = [5, 3, 12, 8]
notes = [note for note in notes if note >= 10]
print(notes)  # => [12]

# 6. Écraser une fonction intégrée avec une variable
#    Symptôme : "TypeError: 'int' object is not callable" plus loin.
sum = 0                   # on croit créer une simple variable "somme"…
for n in [1, 2, 3]:
    sum += n
try:
    print(sum([4, 5]))    # … mais sum() n'est plus la fonction intégrée !
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 6: (Sans ce try: … except …, cette ligne créerait : 'int' object is not
# callable)
del sum                   # on supprime notre variable : sum() redevient la
print(sum([4, 5]))        # => 9   fonction intégrée (cf. chap. 19)
# Correction : choisir un autre nom (total, somme…). Évitez aussi : list,
# dict, str, max, min, input, id, type… (cf. chap. 10)

# 7. Oublier de convertir une saisie (input() renvoie toujours une str)
#    On simule ici la saisie de l'utilisateur :
saisie = "12"             # comme si on avait fait saisie = input("Âge ? ")
print(saisie * 2)         # => 1212  (répétition de string, cf. chap. 7)
try:
    print(saisie + 1)
except TypeError as err:
    print(f"7: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 7: (Sans ce try: … except …, cette ligne créerait : can only concatenate
# str (not "int") to str)
print(int(saisie) + 1)    # => 13  (correction : int(), cf. chap. 11)


# 8. Oublier le return
#    Symptôme : la fonction renvoie None, et l'erreur apparaît plus loin.
def prix_ttc_faux(prix_ht):
    prix_ht * 1.2         # calculé… puis perdu !


def prix_ttc(prix_ht):
    return prix_ht * 1.2


print(prix_ttc_faux(10))  # => None
try:
    print(prix_ttc_faux(10) + 5)
except TypeError as err:
    print(f"8: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 8: (Sans ce try: … except …, cette ligne créerait : unsupported operand
# type(s) for +: 'NoneType' and 'int')
print(prix_ttc(10) + 5)   # => 17.0
# IMPT : si vous voyez "NoneType" dans un message d'erreur, cherchez une
# fonction qui ne renvoie rien (ou une méthode comme .sort() ou .append(),
# qui modifient la liste et renvoient None, cf. chap. 16 et 24).


# 9. Comparer des floats avec == (cf. chap. 4)
print(0.1 + 0.2 == 0.3)            # => False
print(abs((0.1 + 0.2) - 0.3) < 1e-9)  # => True (on compare à une tolérance)
# (math.isclose(0.1 + 0.2, 0.3) fait la même chose proprement, cf. chap. 22)


# 10. Copier une liste avec "=" (cf. chap. 19 et 24)
#     Symptôme : modifier la "copie" modifie aussi l'original.
originale = [1, 2, 3]
copie = originale          # pas une copie : un 2e nom pour la même liste
copie.append(4)
print(originale)           # => [1, 2, 3, 4]
vraie_copie = originale.copy()
vraie_copie.append(5)
print(originale)           # => [1, 2, 3, 4]  (inchangée cette fois)


# En bref
##########

"""
    La démarche :  reproduire → isoler → hypothèse → vérifier → test de
                   non-régression
    Traceback :    lire la DERNIÈRE ligne (type + message), puis remonter
                   jusqu'au dernier bloc qui concerne VOTRE fichier
    traceback.format_exc()     le traceback sous forme de string
    print(f"{x=}")             nom + valeur (Python 3.8+) ; repr() pour voir
                               les espaces ; type() en cas de doute
    assert condition, "msg"    garde-fou contre les erreurs de programmation
    Cas minimal :  réduire les données et le code jusqu'à l'essentiel
    Bisection :    couper le programme en deux pour localiser le bug
    breakpoint()   pause dans pdb : p, n, s, c, l, w, q
    PYTHONBREAKPOINT=0         ignore tous les breakpoint()
    python3 -m pdb f.py        débogage post-mortem
    Éditeur :      points d'arrêt dans la marge, F5, panneau Variables

Au chap. 44, on verra comment remplacer les print() de débogage par un vrai
journal (logging), que l'on peut garder dans le programme et activer ou
désactiver à volonté.
"""
