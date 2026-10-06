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
#  Chap. 47     #  Packaging : pip, conda, poetry et uv                        #
#               #                                                              #
################################################################################
#
#  - Le problème : "ça marche sur ma machine"
#  - PyPI, pip et requirements.txt
#  - Les environnements virtuels (venv)
#  - Où suis-je ? Inspecter son environnement depuis Python
#  - Numéros de version et contraintes
#  - conda et mamba
#  - poetry
#  - Le standard : pyproject.toml
#  - Les fichiers "lock"
#  - uv : l'outil tout-en-un
#  - Les commandes uv essentielles
#  - Démonstration réelle avec uv
#  - Scripts autonomes (PEP 723)
#  - Les outils en ligne de commande : uvx
#  - Construire et publier un package
#  - En bref : quel outil choisir ?
#
##############################

# Le problème : "ça marche sur ma machine"
###########################################

"""
Dès qu'un programme utilise des paquets externes (numpy, pandas, requests…,
cf. chap. 22 et 38 à 40), trois questions se posent :

    1. QUELS paquets faut-il installer pour que le programme fonctionne ?
    2. En QUELLE version ? pandas 1.5 et pandas 3.0 ne se comportent pas
       exactement pareil (cf. chap. 39) : un code écrit pour l'une peut
       planter avec l'autre.
    3. Comment éviter que deux projets se GÊNENT ? Si le projet A a besoin de
       numpy 1.26 et le projet B de numpy 2.2, on ne peut pas installer les
       deux "pour tout l'ordinateur".

Sans réponse claire, on obtient le fameux "ça marche sur ma machine" : le
programme tourne chez son auteur, mais plante chez sa collègue, sur le serveur
ou dans six mois, parce que les paquets installés ne sont pas les mêmes.

Le "packaging" (gestion des paquets), c'est l'ensemble des outils et des
bonnes pratiques qui répondent à ces questions :
    - DÉCLARER les dépendances d'un projet (dans un fichier texte),
    - les INSTALLER dans un environnement isolé, propre au projet,
    - FIGER les versions exactes pour reproduire l'environnement à l'identique,
    - et, éventuellement, DISTRIBUER son propre code comme un paquet.

Ce chapitre fait le tour des outils historiques (pip, venv, conda, poetry),
car vous les croiserez partout, puis présente uv, l'outil moderne que nous
utiliserons exclusivement dans la suite du cours.

Note : la plupart des commandes de ce chapitre se tapent dans un TERMINAL
(précédées de "?>", cf. chap. 2), pas dans Python. La partie exécutable de ce
fichier affiche des informations sur VOTRE installation : sa sortie varie donc
d'un ordinateur à l'autre (c'est signalé à chaque fois).
"""


# PyPI, pip et requirements.txt
################################

"""
PyPI (Python Package Index, https://pypi.org) est l'entrepôt officiel des
paquets Python : plus de 500 000 projets, que n'importe qui peut publier.
Quand on "installe pandas", on télécharge en réalité un fichier depuis PyPI.

pip est l'installeur historique, livré avec Python. Rappel du chap. 22 :
    ?> python3 -m pip install pandas            # installer
    ?> python3 -m pip install "pandas==2.2.3"   # une version précise
    ?> python3 -m pip install --upgrade pandas  # mettre à jour
    ?> python3 -m pip uninstall pandas          # désinstaller
    ?> python3 -m pip list                      # lister ce qui est installé

Pour partager la liste des dépendances, la convention historique est un
fichier requirements.txt, une dépendance par ligne :

    numpy>=1.26
    pandas==2.2.3
    requests

    ?> python3 -m pip freeze > requirements.txt   # écrit TOUT l'installé
    ?> python3 -m pip install -r requirements.txt # réinstalle tout ailleurs

Limites de pip seul :
    - il installe dans le Python "global" si on ne l'en empêche pas (d'où les
      environnements virtuels, section suivante) ;
    - "pip freeze" mélange ce que VOUS avez demandé (pandas) et ce dont pandas
      a besoin (numpy, python-dateutil, pytz…) : impossible de savoir, plus
      tard, lesquelles on peut supprimer ;
    - requirements.txt n'est qu'une convention, pas un standard : il ne décrit
      ni le nom du projet, ni la version de Python requise ;
    - il est lent sur les gros projets.
"""


# Les environnements virtuels (venv)
#####################################

r"""
Un environnement virtuel ("venv") est un DOSSIER qui contient son propre
interpréteur Python (en fait, un lien vers celui du système) et son propre
dossier de paquets (site-packages). Chaque projet a le sien : les paquets
installés dans l'un n'existent pas pour les autres. Le problème 3 est réglé.

    ?> python3 -m venv .venv            # crée le dossier .venv dans le projet
    ?> source .venv/bin/activate        # l'active (Linux / macOS)
    ?> .venv\Scripts\activate           # l'active (Windows)
    (.venv) ?> python -m pip install pandas   # installé DANS .venv seulement
    (.venv) ?> deactivate               # revient au Python du système

"Activer" un venv ne fait que modifier la variable PATH du terminal, pour que
la commande "python" désigne .venv/bin/python. Rien de magique : on peut aussi
lancer directement .venv/bin/python mon_script.py sans activer.

IMPT : bonnes pratiques
    - un venv PAR projet, dans un dossier .venv à la racine du projet ;
    - on ne commite JAMAIS le dossier .venv dans git (il pèse des centaines de
      Mo et dépend de la machine) : on l'ajoute au .gitignore, et on commite
      seulement la LISTE des dépendances ;
    - un venv se jette et se recrée sans regret : il ne contient rien
      d'unique.

Sur certaines distributions Linux récentes, pip refuse même d'installer quoi
que ce soit hors d'un venv (erreur "externally-managed-environment") : c'est
la PEP 668, qui protège les paquets Python du système.
"""


# Où suis-je ? Inspecter son environnement depuis Python
#########################################################

"""
Python sait dans quel environnement il tourne : le module sys (cf. chap. 22)
donne deux chemins :
    - sys.prefix      : le dossier de l'environnement ACTUEL ;
    - sys.base_prefix : le dossier du Python "de base" qui l'a créé.
Dans un venv, les deux diffèrent ; sinon, ils sont égaux.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from importlib import metadata  # bibliothèque standard depuis Python 3.8
from pathlib import Path        # cf. chap. 22

print("Python utilisé :", sys.executable)
# => /usr/bin/python3 (VARIE selon votre machine)
print("Version :", sys.version_info[:3])
# => (3, 14, 4) (VARIE)


def dans_un_venv():
    """Retourne True si le programme tourne dans un environnement virtuel."""
    return sys.prefix != sys.base_prefix


print("Dans un venv ?", dans_un_venv())
# => False avec "python3 chap_47_packaging.py",
#    True avec "uv run chap_47_packaging.py" (VARIE)

"""
Le module importlib.metadata (bibliothèque standard, Python 3.8+) lit les
informations des paquets INSTALLÉS : leur version, leurs dépendances… C'est
ce que font pip et uv pour afficher leurs listes.

Si le paquet n'est pas installé, il lève l'erreur PackageNotFoundError.
"""


def version_installee(nom):
    """Retourne la version installée d'un paquet, ou None s'il est absent."""
    try:
        return metadata.version(nom)
    except metadata.PackageNotFoundError:
        return None


for nom in ["pip", "numpy", "pandas", "requests"]:
    v = version_installee(nom)
    if v is None:
        print(f"{nom:10} : non installé")
    else:
        print(f"{nom:10} : version {v}")
# => (VARIE : dépend de ce qui est installé dans votre environnement)
#    pip        : non installé
#    numpy      : non installé
#    pandas     : non installé
#    requests   : version 2.32.5

try:
    metadata.version("un-paquet-qui-n-existe-pas")
except metadata.PackageNotFoundError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : No package metadata
#    was found for un-paquet-qui-n-existe-pas)

# On peut aussi lister TOUS les paquets installés (comme "pip list") :
noms = sorted(d.metadata["Name"] for d in metadata.distributions())
print(len(noms), "paquets installés")  # => 76 paquets installés (VARIE)


# Numéros de version et contraintes
####################################

"""
La plupart des paquets suivent le "versionnage sémantique" (SemVer) :
MAJEUR.MINEUR.CORRECTIF, par exemple 2.2.3.
    - CORRECTIF (2.2.3 → 2.2.4) : corrections de bugs, rien ne casse ;
    - MINEUR    (2.2.3 → 2.3.0) : nouvelles fonctionnalités, rien ne casse ;
    - MAJEUR    (2.2.3 → 3.0.0) : changements INCOMPATIBLES, votre code peut
      casser (c'est le cas de pandas 3 ou de numpy 2).
Il existe aussi des versions de test : "3.0.0rc1" (release candidate),
"2.0.0b2" (bêta), "1.0.0a1" (alpha).

Pour déclarer une dépendance, on écrit une CONTRAINTE de version (PEP 440) :
    pandas            n'importe quelle version (déconseillé pour un projet)
    pandas==2.2.3     exactement celle-ci
    pandas>=2.0       2.0 ou plus récente
    pandas>=2.0,<3    entre 2.0 (inclus) et 3 (exclu)
    pandas~=2.2       "compatible" : >=2.2 et <3.0
    pandas~=2.2.1     "compatible" : >=2.2.1 et <2.3
    pandas!=2.1.0     toutes sauf celle-ci (un bug connu, par exemple)

IMPT : piège classique, on ne compare PAS des versions comme des chaînes.
"""
print("1.10.0" > "1.9.0")  # => False : comparaison caractère par caractère !
# ("1" == "1", "." == ".", puis "1" < "9" : la chaîne "1.10.0" est plus petite)

"""
Il faut les découper et comparer des nombres. Les tuples se comparent élément
par élément (cf. chap. 17) : c'est exactement ce qu'il nous faut.
"""


def version_en_tuple(version):
    """Convertit "1.10.2" en (1, 10, 2). Ne gère que les chiffres."""
    return tuple(int(morceau) for morceau in version.split("."))


print(version_en_tuple("1.10.0"))                   # => (1, 10, 0)
print(version_en_tuple("1.10.0") > version_en_tuple("1.9.0"))  # => True

# Notre fonction maison est volontairement simple : elle ne connaît pas les
# versions de test.
try:
    version_en_tuple("3.0.0rc1")
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : invalid literal for
#    int() with base 10: '0rc1')

"""
Dans un vrai programme, on utilise le paquet "packaging" (celui qu'utilisent
pip et uv), qui implémente toute la PEP 440. Il n'est pas toujours installé :
on protège donc l'import (cf. chap. 26).
"""
try:
    from packaging.specifiers import SpecifierSet
    from packaging.version import Version
except ImportError:
    print("(le paquet 'packaging' n'est pas installé : "
          "'uv run --with packaging chap_47_packaging.py' pour voir la suite)")
else:
    print(Version("1.10.0") > Version("1.9.0"))      # => True
    print(Version("3.0.0rc1") < Version("3.0.0"))    # => True
    compatible = SpecifierSet("~=2.2")
    print("2.2.3" in compatible)  # => True
    print("2.9.0" in compatible)  # => True
    print("3.0.0" in compatible)  # => False


# conda et mamba
#################

"""
conda est le gestionnaire de paquets ET d'environnements de la distribution
Anaconda, très répandue en Data Science et à l'université.

Sa particularité : il ne gère pas que des paquets Python. Il installe aussi
des bibliothèques écrites en C, C++ ou Fortran (BLAS, CUDA, GDAL…), et même
d'autres langages (R). Historiquement, c'était LA solution pour installer
numpy ou scipy sur Windows, quand pip n'y arrivait pas.

    ?> conda create -n meteo python=3.12 pandas   # crée un environnement
    ?> conda activate meteo                        # l'active
    ?> conda install -c conda-forge seaborn        # canal conda-forge
    ?> conda env export > environment.yml          # sauvegarde l'environnement
    ?> conda env create -f environment.yml         # le recrée ailleurs

mamba (et micromamba) est une réécriture beaucoup plus rapide de conda, avec
les mêmes commandes.

Limites :
    - les paquets conda ne viennent pas de PyPI mais de "canaux" (defaults,
      conda-forge) : certains paquets y manquent ou sont en retard ;
    - mélanger "conda install" et "pip install" dans un même environnement
      est une source classique de casse ;
    - les environnements sont lourds (souvent plusieurs Go) ;
    - la distribution Anaconda (canal "defaults") est soumise à des
      conditions de licence pour les grandes organisations.

Aujourd'hui, numpy, pandas, scikit-learn ou pytorch s'installent sans souci
depuis PyPI ("wheels" précompilées) : conda reste utile surtout quand on a
besoin de bibliothèques système non-Python.
"""


# poetry
#########

"""
poetry (2018) a été l'un des premiers outils "tout-en-un" : il crée le venv,
déclare les dépendances dans un fichier pyproject.toml, fige les versions dans
un fichier poetry.lock et sait publier un paquet.

    ?> poetry new meteo            # crée un projet
    ?> poetry add pandas           # ajoute une dépendance (et l'installe)
    ?> poetry add --group dev pytest
    ?> poetry install              # installe tout ce qui est déclaré
    ?> poetry run python main.py   # lance un programme dans le venv
    ?> poetry build                # construit le paquet
    ?> poetry publish              # le publie sur PyPI

poetry a popularisé les bonnes idées que l'on retrouve partout aujourd'hui :
pyproject.toml, fichier lock, séparation des dépendances de développement.
Ses limites : il est écrit en Python (donc lent sur la résolution des gros
projets), il ne sait pas installer Python lui-même, et ses premières versions
utilisaient un format de pyproject.toml non standard ([tool.poetry]).
"""


# Le standard : pyproject.toml
###############################

"""
pyproject.toml est LE fichier standard de description d'un projet Python
(PEP 518, PEP 621). Tous les outils modernes le lisent : uv, poetry (2.0+),
pip, ruff, pytest, black, mypy… (cf. chap. 20 pour la configuration de ruff).

Il est écrit en TOML, un format de configuration simple : des sections
[entre crochets] et des lignes "clé = valeur". Exemple commenté :

    [project]                          # section standard (PEP 621)
    name = "meteo"                     # nom du paquet
    version = "0.1.0"                  # sa version (SemVer)
    description = "Analyse de relevés météo"
    readme = "README.md"
    requires-python = ">=3.10"         # versions de Python acceptées
    dependencies = [                   # dépendances nécessaires à l'exécution
        "pandas>=2.2",
        "requests~=2.32",
    ]

    [project.scripts]                  # commandes installées avec le paquet
    meteo = "meteo.cli:main"           # "meteo" lance la fonction main()

    [dependency-groups]                # dépendances de DÉVELOPPEMENT (PEP 735)
    dev = ["pytest>=8", "ruff"]        # utiles pour coder, pas pour utiliser

    [build-system]                     # comment construire le paquet
    requires = ["uv_build>=0.8"]
    build-backend = "uv_build"

    [tool.ruff]                        # réglages propres à un outil
    line-length = 80

Depuis Python 3.11, la bibliothèque standard sait lire le TOML (tomllib) :
"""
TOML_EXEMPLE = """
[project]
name = "meteo"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["pandas>=2.2", "requests~=2.32"]

[dependency-groups]
dev = ["pytest>=8", "ruff"]
"""

try:
    import tomllib  # Python 3.11+
except ImportError:
    print("(tomllib demande Python 3.11+ : section sautée)")
else:
    config = tomllib.loads(TOML_EXEMPLE)
    print(type(config))                      # => <class 'dict'>
    print(config["project"]["name"])         # => meteo
    print(config["project"]["dependencies"])
    # => ['pandas>=2.2', 'requests~=2.32']
    print(config["dependency-groups"]["dev"])  # => ['pytest>=8', 'ruff']

# Un fichier TOML devient donc un simple dictionnaire imbriqué (cf. chap. 27).


# Les fichiers "lock"
######################

"""
pyproject.toml décrit ce que l'on ACCEPTE ("pandas>=2.2"). Mais si l'on
installe le projet aujourd'hui puis dans six mois, on n'obtiendra pas la même
version : pandas 2.2.3 aujourd'hui, pandas 3.1 plus tard…

Le fichier "lock" (verrou) enregistre la version EXACTE de CHAQUE paquet
installé, y compris les dépendances des dépendances (numpy, pytz…), avec une
empreinte (hash) de chaque fichier téléchargé. Réinstaller depuis le lock
redonne exactement le même environnement, sur n'importe quelle machine.

    outil    fichier de déclaration    fichier lock
    -----    ----------------------    ------------------------------
    pip      requirements.txt          (pip freeze, approximation)
    conda    environment.yml           (conda-lock, outil séparé)
    poetry   pyproject.toml            poetry.lock
    uv       pyproject.toml            uv.lock

IMPT : le fichier lock est généré automatiquement (on ne l'édite jamais à la
main) et on le COMMITE dans git, avec pyproject.toml. Le dossier .venv, lui,
ne se commite pas : le lock suffit à le recréer.
"""


# uv : l'outil tout-en-un
##########################

"""
uv (https://docs.astral.sh/uv, 2024) est développé par Astral, les auteurs de
ruff (cf. chap. 20). Il remplace à lui seul pip, venv, pip-tools, pipx,
pyenv, poetry et twine :
    - il installe Python lui-même (plus besoin de l'installer à la main) ;
    - il crée et gère le venv automatiquement ;
    - il lit et écrit pyproject.toml (format standard) et uv.lock ;
    - il est écrit en Rust : 10 à 100 fois plus rapide que pip, avec un cache
      global qui évite de retélécharger les mêmes paquets ;
    - il lance des outils et des scripts sans rien installer durablement.

À partir d'ici, et pour TOUT le reste du cours, nous utilisons uv.

Installation (une seule fois, dans un terminal) :
    ?> curl -LsSf https://astral.sh/uv/install.sh | sh          # Linux / macOS
    ?> powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows
    ?> uv --version
On peut aussi l'installer avec pip, brew, winget…

Et Python lui-même :
    ?> uv python install 3.13    # télécharge et installe Python 3.13
    ?> uv python list            # versions disponibles / installées
    ?> uv python pin 3.13        # fixe la version du projet (.python-version)
"""

uv_present = shutil.which("uv")  # chemin de l'exécutable uv, ou None
print("uv est installé :", uv_present is not None)
# => True si uv est installé sur votre machine (VARIE)


# Les commandes uv essentielles
################################

"""
Le cycle de vie d'un projet avec uv :

    ?> uv init meteo             # crée le dossier meteo/ avec pyproject.toml,
    ?> cd meteo                  #   .python-version, main.py, README.md, .git
    ?> uv add pandas requests    # ajoute les dépendances : met à jour
                                 #   pyproject.toml ET uv.lock, ET installe
                                 #   dans .venv (créé si besoin)
    ?> uv add "numpy>=2"         # avec une contrainte de version
    ?> uv add --dev pytest ruff  # dépendance de développement
    ?> uv remove requests        # retire une dépendance
    ?> uv run main.py            # lance main.py DANS le venv du projet
    ?> uv run pytest             # lance un outil installé dans le venv
    ?> uv lock                   # recalcule uv.lock (sans installer)
    ?> uv lock --upgrade         # met à jour les versions dans le lock
    ?> uv sync                   # installe EXACTEMENT ce que dit uv.lock
    ?> uv tree                   # arbre des dépendances

IMPT : "uv run" synchronise automatiquement le venv avant de lancer le
programme. Plus besoin d'activer quoi que ce soit : on tape "uv run" devant
la commande, et c'est tout. Une collègue qui récupère le projet tape juste
"uv run main.py" : uv installe la bonne version de Python, crée le venv,
installe les paquets du lock, puis lance le programme.

Essais ponctuels, sans rien ajouter au projet :
    ?> uv run --with pandas python      # un Python où pandas est disponible
    ?> uv run --with requests mon_script.py
C'est ce que nous utilisons pour vérifier les chapitres 38 à 40 de ce cours.

Compatibilité : pour les habitués de pip, uv propose les mêmes commandes,
en beaucoup plus rapide :
    ?> uv venv                           # équivaut à python -m venv .venv
    ?> uv pip install pandas             # équivaut à pip install pandas
    ?> uv pip install -r requirements.txt
    ?> uv pip compile requirements.in -o requirements.txt
Utile pour migrer un vieux projet ; pour un nouveau projet, préférez
uv add / uv run.
"""


# Démonstration réelle avec uv
###############################

"""
Si uv est installé, on crée ici un VRAI petit projet, dans un dossier
temporaire (supprimé automatiquement à la fin du bloc "with", cf. chap. 36),
puis on le lance avec "uv run". Aucune dépendance n'est déclarée : la
démonstration fonctionne sans connexion Internet (option --offline).

Le module subprocess (bibliothèque standard) lance une commande du terminal
depuis Python : run() attend la fin de la commande et récupère sa sortie.
"""
PYPROJECT_DEMO = """\
[project]
name = "demo-meteo"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = []

[tool.uv]
package = false
"""

MAIN_DEMO = """\
import sys
print("Bonjour depuis le venv du projet :", sys.prefix != sys.base_prefix)
"""

if uv_present is None:
    print("(uv n'est pas installé : démonstration sautée)")
else:
    with tempfile.TemporaryDirectory() as dossier:
        projet = Path(dossier)
        (projet / "pyproject.toml").write_text(PYPROJECT_DEMO, encoding="utf-8")
        (projet / "main.py").write_text(MAIN_DEMO, encoding="utf-8")
        try:
            resultat = subprocess.run(
                ["uv", "run", "--offline", "--quiet", "main.py"],
                cwd=projet,                # lancé DANS le dossier du projet
                capture_output=True,       # récupère la sortie au lieu de
                text=True,                 #   l'afficher, sous forme de str
                timeout=120,               # abandonne après 2 minutes
                # variable d'environnement qui fait taire un avertissement
                # de uv sur certains systèmes de fichiers :
                env={**os.environ, "UV_LINK_MODE": "copy"},

            )
        except subprocess.TimeoutExpired:
            print("(uv a mis trop de temps : démonstration interrompue)")
        else:
            print(resultat.stdout.strip())
            # => Bonjour depuis le venv du projet : True
            fichiers = sorted(p.name for p in projet.iterdir())
            print(fichiers)
            # => ['.venv', 'main.py', 'pyproject.toml', 'uv.lock']
            # uv a créé tout seul le venv (.venv) et le fichier lock (uv.lock)
            lock = (projet / "uv.lock").read_text(encoding="utf-8")
            print(lock.splitlines()[:3])
            # => ['version = 1', 'revision = 3', 'requires-python = ">=3.9"']
            #    (le format exact VARIE selon la version de uv)
    # Ici, le dossier temporaire et tout son contenu ont été supprimés.


# Scripts autonomes (PEP 723)
##############################

"""
Pour un simple script (un seul fichier), créer tout un projet est excessif.
La PEP 723 permet d'écrire les dépendances DANS le script, dans un
commentaire spécial :

    # /// script
    # requires-python = ">=3.12"
    # dependencies = [
    #     "requests<3",
    #     "pandas",
    # ]
    # ///

    import pandas as pd
    import requests
    …

    ?> uv run releve.py
uv lit ce bloc, prépare un environnement jetable avec pandas et requests (mis
en cache), puis lance le script. On envoie un seul fichier à un collègue, il
tape "uv run releve.py", et tout fonctionne.

Pour ajouter une dépendance à ce bloc sans l'écrire à la main :
    ?> uv add --script releve.py requests
Et l'on peut même rendre le script exécutable directement, avec un shebang
(cf. chap. 3) : #!/usr/bin/env -S uv run --script

Pour Python, ce bloc n'est qu'un commentaire : le script reste un fichier
Python ordinaire.
"""
SCRIPT_DEMO = """\
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
print("Script autonome lancé par uv")
"""

if uv_present is not None:
    with tempfile.TemporaryDirectory() as dossier:
        script = Path(dossier) / "autonome.py"
        script.write_text(SCRIPT_DEMO, encoding="utf-8")
        try:
            resultat = subprocess.run(
                ["uv", "run", "--offline", "--quiet", str(script)],
                capture_output=True, text=True, timeout=120,
            )
            print(resultat.stdout.strip())  # => Script autonome lancé par uv
        except subprocess.TimeoutExpired:
            print("(uv a mis trop de temps)")


# Les outils en ligne de commande : uvx
########################################

"""
Certains paquets sont des OUTILS que l'on lance dans un terminal : ruff
(cf. chap. 20), black, mypy (cf. chap. 46), jupyter, httpie… On ne veut pas
forcément les ajouter à chaque projet.

    ?> uvx ruff check .            # lance ruff dans un env. jetable (en cache)
    ?> uvx ruff@0.9.0 check .      # une version précise
    ?> uvx --from jupyterlab jupyter lab
    ?> uv tool install ruff        # installe durablement la commande "ruff"
    ?> uv tool list                # outils installés
    ?> uv tool upgrade --all

"uvx" est un raccourci pour "uv tool run". C'est l'équivalent de pipx.
"""


# Construire et publier un package
###################################

"""
Pour partager son code comme un vrai paquet (installable avec "uv add" par
d'autres), on adopte la structure "src", recommandée :

    meteo/
    ├── pyproject.toml        # avec une section [build-system]
    ├── uv.lock
    ├── README.md
    ├── src/
    │   └── meteo/            # le package (cf. chap. 22)
    │       ├── __init__.py
    │       ├── lecture.py
    │       └── cli.py
    └── tests/                # les tests (cf. chap. 37)
        └── test_lecture.py

    ?> uv init --package meteo    # crée directement cette structure
    ?> uv build                   # construit dist/meteo-0.1.0.tar.gz (sources)
                                  #   et dist/meteo-0.1.0-py3-none-any.whl
    ?> uv publish                 # envoie dist/ sur PyPI (compte et jeton
                                  #   d'API nécessaires)

Le fichier .whl ("wheel", roue) est le format d'installation standard : une
simple archive zip que pip et uv savent décompresser au bon endroit.

Conseil : entraînez-vous d'abord sur TestPyPI (https://test.pypi.org), un
PyPI de test : "uv publish --publish-url https://test.pypi.org/legacy/".
"""


# En bref : quel outil choisir ?
#################################

"""
    besoin                       pip+venv   conda    poetry   uv
    ---------------------------  --------   ------   ------   ------
    installer des paquets PyPI   oui        partiel  oui      oui
    paquets non-Python (C, R…)   non        OUI      non      non
    installer Python lui-même    non        oui      non      oui
    venv automatique             non        oui      oui      oui
    pyproject.toml standard      -          non      oui      oui
    fichier lock                 non        externe  oui      oui
    scripts autonomes (PEP 723)  non        non      non      oui
    outils CLI (comme pipx)      non        non      non      oui
    construire / publier         externe    non      oui      oui
    vitesse                      moyenne    lente    moyenne  très rapide

IMPT : pour ce cours, et pour vos projets, utilisez uv :
    ?> uv init mon_projet && cd mon_projet
    ?> uv add pandas matplotlib
    ?> uv add --dev pytest ruff
    ?> uv run main.py
Gardez pip, conda et poetry en tête pour LIRE les projets existants (et
"uv pip" pour les migrer en douceur), mais ne démarrez plus de projet avec.

Les chapitres suivants qui utilisent des paquets externes (48 pandas II,
49 requests, 50 seaborn, 51 Machine Learning) s'installent donc avec
"uv add …" et se lancent avec "uv run …".
"""
