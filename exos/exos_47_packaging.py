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
#  Chap. 47     #  Packaging : exercices                                       #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Les questions de cours se répondent dans un commentaire ; les
commandes "?>" se testent dans un terminal (avec uv installé, cf. chapitre).

Les exercices de code n'utilisent que la bibliothèque standard (Python 3.11+
pour tomllib).
Les corrigés sont dans le fichier corrs/corr_47_packaging.py.
"""


##############################################
#  Le problème : "ça marche sur ma machine"  #
##############################################

"""
1. Citez trois raisons pour lesquelles un programme qui fonctionne sur votre
   ordinateur peut planter sur celui d'un collègue, alors que le code est
   exactement le même.

2. Vrai ou faux ? Justifiez.
     a) Installer tous ses paquets dans le Python du système est la méthode
        la plus simple et la plus sûre.
     b) Deux projets peuvent avoir besoin de deux versions différentes du même
        paquet.
     c) Le packaging ne concerne que ceux qui publient des paquets sur PyPI.
"""


###################################
#  PyPI, pip et requirements.txt  #
###################################

"""
3. Écrivez les commandes pip (forme "python3 -m pip …") pour :
     a) installer requests ;
     b) installer exactement la version 2.2.3 de pandas ;
     c) enregistrer les paquets installés dans requirements.txt ;
     d) réinstaller tout ce que contient requirements.txt.

4. Voici le contenu d'un fichier requirements.txt (dans la variable
   REQUIREMENTS ci-dessous). Écrivez une fonction lire_requirements(texte)
   qui renvoie un dictionnaire {nom du paquet: contrainte}, en ignorant les
   lignes vides et les commentaires (#). La contrainte vaut "" s'il n'y en a
   pas. Les opérateurs possibles sont "==", ">=", "~=" et "<=".
       lire_requirements(REQUIREMENTS)
       # => {'numpy': '>=1.26', 'pandas': '==2.2.3', 'requests': '',
       #     'seaborn': '~=0.13'}
"""
REQUIREMENTS = """\
# Données
numpy>=1.26
pandas==2.2.3

requests
seaborn~=0.13   # graphiques
"""


########################################
#  Les environnements virtuels (venv)  #
########################################

"""
5. Écrivez les commandes pour créer un venv dans le dossier .venv, l'activer
   (Linux/macOS), puis le désactiver. Que modifie réellement l'activation ?

6. Pourquoi ne faut-il jamais commiter le dossier .venv dans git ? Que
   commite-t-on à la place ?
"""


##########################################################
#  Où suis-je ? Inspecter son environnement depuis Python  #
##########################################################

"""
7. Écrivez une fonction rapport_environnement() qui affiche :
     - le chemin de l'interpréteur Python utilisé,
     - "venv : oui" ou "venv : non",
     - pour chaque paquet de la liste ["numpy", "pandas", "requests"], sa
       version installée ou "absent".
   Lancez votre fichier avec "python3 …" puis avec
   "uv run --with requests …" : qu'est-ce qui change ?
"""


#######################################
#  Numéros de version et contraintes  #
#######################################

"""
8. Sans exécuter : que vaut chaque expression ? Pourquoi ?
     a) "2.10" > "2.9"
     b) (2, 10) > (2, 9)
     c) "10.0" > "9.0"

9. Un paquet passe de la version 2.4.1 à :
     a) 2.4.2     b) 2.5.0     c) 3.0.0
   D'après le versionnage sémantique, dans quel(s) cas votre code risque-t-il
   de casser ?

10. Pour chaque contrainte, donnez la plus petite et la plus grande version
    autorisée (parmi des versions de la forme X.Y.Z) :
      a) ~=2.2       b) ~=2.2.1      c) >=1.5,<2

11. Écrivez une fonction version_en_tuple(version) qui convertit "1.10.2" en
    (1, 10, 2), puis une fonction satisfait(version, contrainte) qui renvoie
    True si la version respecte la contrainte. Gérez les opérateurs "==",
    ">=", "<" et "~=" (rappel : "~=2.2" signifie ">=2.2 et <3.0", et
    "~=2.2.1" signifie ">=2.2.1 et <2.3"). Pour comparer des tuples de
    longueurs différentes, complétez le plus court avec des zéros.
        satisfait("2.10.0", ">=2.9")   # => True
        satisfait("3.0.0", "~=2.2")    # => False
        satisfait("2.2.9", "~=2.2.1")  # => True
        satisfait("2.3.0", "~=2.2.1")  # => False

12. Avec votre fonction satisfait(), affichez les versions de la liste
    VERSIONS ci-dessous qui respectent "~=2.1".
"""
VERSIONS = ["1.9.9", "2.0.0", "2.1.0", "2.1.5", "2.9.3", "3.0.0", "3.1.0"]


######################################
#  conda, poetry et pyproject.toml   #
######################################

"""
13. Dans quel cas conda reste-t-il préférable à un outil qui ne gère que les
    paquets PyPI ? Citez deux inconvénients de conda.

14. Le fichier PYPROJECT ci-dessous décrit un projet. Avec tomllib
    (Python 3.11+), affichez :
      a) le nom et la version du projet ;
      b) la version minimale de Python demandée ;
      c) la liste des dépendances, une par ligne ;
      d) le nombre de dépendances de développement.

15. Ajoutez au dictionnaire obtenu une dépendance "seaborn>=0.13" (dans la
    liste, sans modifier le texte), puis affichez la liste triée par ordre
    alphabétique.
"""
PYPROJECT = """\
[project]
name = "analyse-velos"
version = "0.3.1"
requires-python = ">=3.11"
dependencies = [
    "pandas>=2.2",
    "requests~=2.32",
    "matplotlib",
]

[dependency-groups]
dev = ["pytest>=8", "ruff", "mypy"]
"""


#########################
#  Les fichiers "lock"  #
#########################

"""
16. Quelle est la différence entre pyproject.toml et uv.lock ? Lequel
    modifie-t-on à la main ? Lesquels commite-t-on ?
"""


####################
#  uv en pratique  #
####################

"""
17. Écrivez la suite de commandes uv pour :
      a) créer un projet "meteo" et entrer dans son dossier ;
      b) fixer la version de Python du projet à 3.13 ;
      c) ajouter pandas et requests ;
      d) ajouter pytest comme dépendance de développement ;
      e) lancer le fichier main.py ;
      f) retirer requests ;
      g) sur un autre ordinateur, après un "git clone", installer exactement
         les mêmes versions que vous.
    Testez-les dans un dossier temporaire !

18. Quelle commande permet de lancer une seule fois un script avec pandas,
    SANS l'ajouter à aucun projet ? Et de lancer l'outil ruff sans
    l'installer ?

19. Écrivez une fonction bloc_script(dependances, python=">=3.11") qui
    renvoie le bloc de métadonnées PEP 723 (une chaîne) correspondant.
        print(bloc_script(["pandas", "requests<3"]))
        # => # /// script
        #    # requires-python = ">=3.11"
        #    # dependencies = [
        #    #     "pandas",
        #    #     "requests<3",
        #    # ]
        #    # ///

20. Dans un dossier temporaire, créez avec Python un fichier
    salut.py commençant par le bloc de l'exercice 19 (sans dépendance),
    suivi de print("Salut !"). Si uv est installé (shutil.which), lancez-le
    avec subprocess.run(["uv", "run", "--offline", …]) et affichez sa sortie.
"""


######################################
#  Construire et publier un package  #
######################################

"""
21. Dessinez (en commentaire) l'arborescence d'un projet "src" nommé
    "velos", avec un module lecture.py, un module stats.py et un dossier de
    tests. Quelles commandes uv construisent puis publient le paquet ? Que
    contient le dossier dist/ ensuite ?

22. Bilan : pour chacune de ces situations, quel outil ou quelle commande
    utiliseriez-vous ?
      a) démarrer un nouveau projet d'analyse de données ;
      b) installer une bibliothèque C (GDAL) avec ses dépendances système ;
      c) reprendre un vieux projet qui n'a qu'un requirements.txt ;
      d) lancer black une fois, pour essayer.
"""
