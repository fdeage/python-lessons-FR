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
#  Chap. 47     #  Packaging : corrigés                                        #
#               #                                                              #
################################################################################

import os
import shutil
import subprocess
import sys
import tempfile
from importlib import metadata
from pathlib import Path


##############################################
#  Le problème : "ça marche sur ma machine"  #
##############################################

"""
1. Par exemple :
     - un paquet n'est pas installé chez le collègue (ModuleNotFoundError) ;
     - il est installé, mais dans une autre version, qui se comporte
       différemment (une fonction renommée, un résultat différent) ;
     - la version de Python elle-même diffère (une syntaxe récente comme
       f"{x=}" demande Python 3.8+, cf. chap. 8) ;
     - (bonus) le système d'exploitation diffère : chemins de fichiers,
       bibliothèques système manquantes…

2. a) Faux : tous les projets partagent alors les mêmes paquets, dans les
      mêmes versions ; mettre à jour un paquet pour un projet peut en casser
      un autre, et l'on peut même abîmer les outils du système (PEP 668).
   b) Vrai : c'est justement pour cela qu'on crée un environnement virtuel
      par projet.
   c) Faux : dès qu'on utilise un seul paquet externe, il faut déclarer ses
      dépendances pour que le projet soit reproductible (par un collègue, un
      serveur, ou soi-même dans six mois).
"""


###################################
#  PyPI, pip et requirements.txt  #
###################################

"""
3. a) python3 -m pip install requests
   b) python3 -m pip install "pandas==2.2.3"
      (les guillemets évitent que le terminal interprète certains caractères,
      comme ">" qui redirige vers un fichier !)
   c) python3 -m pip freeze > requirements.txt
   d) python3 -m pip install -r requirements.txt
"""

# 4. On parcourt les lignes ; on coupe d'abord le commentaire éventuel, puis
#    on cherche le premier opérateur présent dans la ligne.
REQUIREMENTS = """\
# Données
numpy>=1.26
pandas==2.2.3

requests
seaborn~=0.13   # graphiques
"""


def lire_requirements(texte):
    """Transforme un requirements.txt en dictionnaire {paquet: contrainte}."""
    resultat = {}
    for ligne in texte.splitlines():
        ligne = ligne.split("#")[0].strip()  # retire commentaire et espaces
        if ligne == "":
            continue  # ligne vide (ou qui ne contenait qu'un commentaire)
        for operateur in ["==", ">=", "~=", "<="]:
            if operateur in ligne:
                position = ligne.index(operateur)
                resultat[ligne[:position]] = ligne[position:]
                break
        else:  # le "else" d'un for : aucun "break" n'a eu lieu (cf. chap. 13)
            resultat[ligne] = ""
    return resultat


print(lire_requirements(REQUIREMENTS))
# => {'numpy': '>=1.26', 'pandas': '==2.2.3', 'requests': '',
#     'seaborn': '~=0.13'}


########################################
#  Les environnements virtuels (venv)  #
########################################

"""
5.  ?> python3 -m venv .venv
    ?> source .venv/bin/activate
    (.venv) ?> deactivate
    L'activation modifie seulement la variable d'environnement PATH du
    terminal (et l'invite, qui affiche "(.venv)") : la commande "python"
    désigne alors .venv/bin/python. Rien n'est copié ni installé.

6.  Le dossier .venv est lourd (des centaines de Mo), dépend de la machine
    (système, chemins, version de Python) et se recrée en une commande : il
    n'a rien à faire dans git. On l'ajoute au .gitignore et l'on commite la
    LISTE des dépendances : pyproject.toml + uv.lock (ou, à l'ancienne,
    requirements.txt).
"""


##########################################################
#  Où suis-je ? Inspecter son environnement depuis Python  #
##########################################################

# 7.
def rapport_environnement():
    """Affiche l'interpréteur, la présence d'un venv et quelques versions."""
    print("Python :", sys.executable)
    print("venv :", "oui" if sys.prefix != sys.base_prefix else "non")
    for nom in ["numpy", "pandas", "requests"]:
        try:
            print(f"  {nom} : {metadata.version(nom)}")
        except metadata.PackageNotFoundError:
            print(f"  {nom} : absent")


rapport_environnement()
# => Python : /usr/bin/python3        (VARIE selon la machine)
#    venv : non
#      numpy : absent
#      pandas : absent
#      requests : 2.32.5   (VARIE)
"""
Avec "uv run --with requests …", Python tourne dans un environnement jetable
créé par uv : le chemin de l'interpréteur change, "venv : oui" s'affiche, et
requests apparaît avec sa version.
"""


#######################################
#  Numéros de version et contraintes  #
#######################################

"""
8. a) False : les chaînes se comparent caractère par caractère ; après
      "2." on compare "1" et "9", et "1" < "9".
   b) True : les tuples se comparent élément par élément, et 10 > 9.
   c) False : "1" < "9" dès le premier caractère.
"""
print("2.10" > "2.9")      # => False
print((2, 10) > (2, 9))    # => True
print("10.0" > "9.0")      # => False

"""
9. a) 2.4.2 : correctif, pas de risque (en principe).
   b) 2.5.0 : nouvelles fonctionnalités compatibles, pas de risque (en
      principe).
   c) 3.0.0 : version MAJEURE, changements incompatibles possibles : c'est là
      que le code risque de casser.
   ("en principe" : tous les projets ne respectent pas parfaitement SemVer,
   d'où l'intérêt des fichiers lock.)

10. a) ~=2.2   : de 2.2.0 (incluse) à 3.0.0 (exclue), donc jusqu'à 2.x.y.
    b) ~=2.2.1 : de 2.2.1 (incluse) à 2.3.0 (exclue), donc jusqu'à 2.2.x.
    c) >=1.5,<2 : de 1.5.0 (incluse) à 2.0.0 (exclue).
"""


# 11.
def version_en_tuple(version):
    """Convertit "1.10.2" en (1, 10, 2)."""
    return tuple(int(morceau) for morceau in version.split("."))


def completer(t, longueur):
    """Complète un tuple avec des zéros : (2, 2) -> (2, 2, 0)."""
    return t + (0,) * (longueur - len(t))


def satisfait(version, contrainte):
    """True si version respecte la contrainte (==, >=, < ou ~=)."""
    operateur = contrainte[:2] if contrainte[:2] in ("==", ">=", "~=") else "<"
    cible = version_en_tuple(contrainte[len(operateur):])
    v = version_en_tuple(version)
    n = max(len(v), len(cible))
    v_c, cible_c = completer(v, n), completer(cible, n)
    if operateur == "==":
        return v_c == cible_c
    if operateur == ">=":
        return v_c >= cible_c
    if operateur == "<":
        return v_c < cible_c
    # "~=" : au moins la cible, et même "préfixe" sauf le dernier nombre.
    # ~=2.2.1 -> préfixe (2, 2) ; ~=2.2 -> préfixe (2,)
    prefixe = cible[:-1]
    return v_c >= cible_c and v[:len(prefixe)] == prefixe


print(satisfait("2.10.0", ">=2.9"))   # => True
print(satisfait("3.0.0", "~=2.2"))    # => False
print(satisfait("2.2.9", "~=2.2.1"))  # => True
print(satisfait("2.3.0", "~=2.2.1"))  # => False
print(satisfait("1.4", "<1.5"))       # => True
print(satisfait("2.2", "==2.2.0"))    # => True (2.2 et 2.2.0 sont égales)

"""
Remarque : dans un vrai programme, on utiliserait le paquet "packaging"
(SpecifierSet, cf. chapitre), qui gère aussi les versions "rc", "b", "a",
"post"… Écrire la fonction soi-même permet de comprendre ce qu'il fait.
"""

# 12. Une compréhension de liste avec condition (cf. chap. 23) :
VERSIONS = ["1.9.9", "2.0.0", "2.1.0", "2.1.5", "2.9.3", "3.0.0", "3.1.0"]
print([v for v in VERSIONS if satisfait(v, "~=2.1")])
# => ['2.1.0', '2.1.5', '2.9.3']


######################################
#  conda, poetry et pyproject.toml   #
######################################

"""
13. conda reste préférable quand on a besoin de bibliothèques NON-Python
    (C/C++/Fortran, CUDA pour les GPU, GDAL pour la cartographie, R…) qu'il
    sait installer avec leurs dépendances système.
    Inconvénients : environnements lourds, paquets parfois en retard sur
    PyPI, mélange conda + pip source de casse, résolution plus lente,
    conditions de licence du canal "defaults" pour les grandes organisations.
"""

# 14.
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

try:
    import tomllib  # Python 3.11+
except ImportError:
    print("(tomllib demande Python 3.11+ : exercices 14 et 15 sautés)")
else:
    config = tomllib.loads(PYPROJECT)
    projet = config["project"]
    print(projet["name"], projet["version"])  # => analyse-velos 0.3.1
    print(projet["requires-python"])          # => >=3.11
    for dependance in projet["dependencies"]:
        print("-", dependance)
    # => - pandas>=2.2
    #    - requests~=2.32
    #    - matplotlib
    print(len(config["dependency-groups"]["dev"]))  # => 3

    # 15. C'est un simple dictionnaire de listes (cf. chap. 27) :
    projet["dependencies"].append("seaborn>=0.13")
    print(sorted(projet["dependencies"]))
    # => ['matplotlib', 'pandas>=2.2', 'requests~=2.32', 'seaborn>=0.13']
    # (le texte PYPROJECT, lui, n'a pas changé : on n'a modifié que sa
    # copie en mémoire. En vrai, c'est "uv add seaborn" qui édite le fichier.)


#########################
#  Les fichiers "lock"  #
#########################

"""
16. pyproject.toml DÉCLARE ce que le projet accepte ("pandas>=2.2"), écrit
    par un humain (ou par "uv add"). uv.lock FIGE les versions exactes de
    TOUS les paquets (dépendances des dépendances comprises), avec leurs
    empreintes : il est généré par uv, on ne l'édite JAMAIS à la main.
    On commite les DEUX (mais pas .venv).
"""


####################
#  uv en pratique  #
####################

"""
17. a) ?> uv init meteo
       ?> cd meteo
    b) ?> uv python pin 3.13
    c) ?> uv add pandas requests
    d) ?> uv add --dev pytest
    e) ?> uv run main.py
    f) ?> uv remove requests
    g) ?> uv sync          (ou directement "uv run main.py", qui synchronise
                            tout seul avant de lancer le programme)

18. ?> uv run --with pandas mon_script.py
    ?> uvx ruff check .        (raccourci de "uv tool run ruff check .")
"""


# 19. On construit la chaîne ligne par ligne, puis on les joint (cf. chap. 8).
def bloc_script(dependances, python=">=3.11"):
    """Renvoie le bloc de métadonnées PEP 723 d'un script autonome."""
    lignes = ["# /// script", f'# requires-python = "{python}"']
    if dependances:
        lignes.append("# dependencies = [")
        for dep in dependances:
            lignes.append(f'#     "{dep}",')
        lignes.append("# ]")
    else:
        lignes.append("# dependencies = []")
    lignes.append("# ///")
    return "\n".join(lignes)


print(bloc_script(["pandas", "requests<3"]))
# => # /// script
#    # requires-python = ">=3.11"
#    # dependencies = [
#    #     "pandas",
#    #     "requests<3",
#    # ]
#    # ///

# 20. Le dossier temporaire est supprimé automatiquement à la fin du "with".
if shutil.which("uv") is None:
    print("(uv n'est pas installé : exercice 20 sauté)")
else:
    with tempfile.TemporaryDirectory() as dossier:
        script = Path(dossier) / "salut.py"
        contenu = bloc_script([], python=">=3.9") + '\nprint("Salut !")\n'
        script.write_text(contenu, encoding="utf-8")
        try:
            resultat = subprocess.run(
                ["uv", "run", "--offline", "--quiet", str(script)],
                capture_output=True, text=True, timeout=120,
                env={**os.environ, "UV_LINK_MODE": "copy"},
            )
            print(resultat.stdout.strip())  # => Salut !
        except subprocess.TimeoutExpired:
            print("(uv a mis trop de temps)")


######################################
#  Construire et publier un package  #
######################################

"""
21. velos/
    ├── pyproject.toml
    ├── uv.lock
    ├── README.md
    ├── src/
    │   └── velos/
    │       ├── __init__.py
    │       ├── lecture.py
    │       └── stats.py
    └── tests/
        ├── test_lecture.py
        └── test_stats.py

    ?> uv build      # construit le paquet
    ?> uv publish    # l'envoie sur PyPI (avec un jeton d'API)
    dist/ contient alors une archive des sources (velos-0.1.0.tar.gz) et une
    "wheel" prête à installer (velos-0.1.0-py3-none-any.whl).

22. a) uv : "uv init", puis "uv add pandas …", puis "uv run …".
    b) conda (ou mamba) : il installe les bibliothèques C et leurs
       dépendances système, ce que les outils PyPI ne font pas.
    c) "uv pip install -r requirements.txt" pour démarrer vite, puis
       migrer : "uv init" et "uv add -r requirements.txt" importe les
       dépendances dans pyproject.toml.
    d) "uvx black ." : black est lancé dans un environnement jetable, sans
       rien installer dans le projet.
"""
