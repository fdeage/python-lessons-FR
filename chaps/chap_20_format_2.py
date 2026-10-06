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
#  Chap. 20     #  Formatage II                                                #
#               #                                                              #
################################################################################
#
#  - Pourquoi formater son code ?
#  - La PEP 8 : nommage
#  - La PEP 8 : espaces et lignes vides
#  - La PEP 8 : longueur des lignes
#  - La PEP 8 : imports, comparaisons et commentaires
#  - La PEP 20 : le "Zen of Python"
#  - Outils de formatage
#  - Configurer son éditeur
#  - Automatiser avec git
#
##########################

# Pourquoi formater son code ?
###############################

"""
On a vu au chap. 5 que le whitespace en DÉBUT de ligne (l'indentation) changeait
le sens d'un programme Python, et qu'ailleurs il était ignoré par
l'interpréteur. Mais ce n'est pas parce que l'interpréteur l'ignore qu'il est
sans importance !

Un code est lu beaucoup plus souvent qu'il n'est écrit : par vous dans 6 mois,
par vos collègues, par la personne qui corrige votre projet… Un code bien
présenté se lit plus vite, et ses bugs se repèrent plus facilement.

"Formater" son code, c'est le présenter de façon régulière et lisible, en
suivant des règles communes. Les deux lignes suivantes font exactement la même
chose pour Python, mais pas pour un humain :
"""
resultat_moche=(3+4)*2-  1;print( resultat_moche )   # => 13
resultat_joli = (3 + 4) * 2 - 1
print(resultat_joli)  # => 13

"""
En Python, ces règles communes sont écrites dans un document officiel : la
"PEP 8" (https://peps.python.org/pep-0008). Une PEP ("Python Enhancement
Proposal") est un texte qui propose une évolution ou une convention pour le
langage. La PEP 8 est de loin la plus connue : presque tout le code Python
du monde la suit, ce qui permet de lire n'importe quel projet sans être dépaysé.

La PEP 8 elle-même rappelle qu'il faut savoir s'en écarter quand elle rend le
code moins lisible : "A Foolish Consistency is the Hobgoblin of Little Minds".
L'important est d'être COHÉRENT au sein d'un même projet.

On présente ici les règles les plus importantes.
"""


# La PEP 8 : nommage
#####################

"""
On a vu les conventions de nommage aux chap. 10 et 15. La PEP 8 tranche le
débat Snake Case / Camel Case pour Python :

| quoi                       | convention         | exemple               |
| -------------------------- | ------------------ | --------------------- |
| variables, fonctions       | snake_case         | prix_total, calculer()|
| constantes (globales)      | MAJUSCULES         | TAUX_TVA = 0.2        |
| modules (fichiers .py)     | minuscules courtes | outils.py, mon_jeu.py |
| classes (hors programme)   | CapWords           | CompteBancaire        |

À éviter :
    - les noms d'une seule lettre "l" (L minuscule), "O" (o majuscule) et "I"
      (i majuscule), qu'on confond avec 1 et 0 selon la police
    - les noms qui écrasent une fonction intégrée : list, str, sum, max… (cf.
      chap. 19)
    - les noms sans signification : truc, a2, temp3, data_final_v2…
    - les accents et caractères non-ASCII (cf. chap. 10)

Un bon nom dit CE QUE CONTIENT la variable, ou CE QUE FAIT la fonction (on
commence souvent un nom de fonction par un verbe).
"""
# 👎
def f(l):
    return sum(l) / len(l)

# 👍
def calculer_moyenne(notes):
    return sum(notes) / len(notes)

print(f([10, 14]))                 # => 12.0
print(calculer_moyenne([10, 14]))  # => 12.0 : même code, mais lisible

TAUX_TVA = 0.2  # une constante en majuscules
prix_ht = 50
prix_ttc = prix_ht * (1 + TAUX_TVA)
print(prix_ttc)  # => 60.0

"""
Note : un nom qui commence par un underscore ("_cache") signale par convention
une variable "interne", que les autres parties du programme ne devraient pas
utiliser. Un nom qui finit par un underscore ("type_", "list_") sert à éviter
un conflit avec un nom intégré ou un mot-clé.
"""


# La PEP 8 : espaces et lignes vides
#####################################

"""
1. Indentation : 4 espaces par niveau, jamais de tabulations (cf. chap. 5).

2. Un espace de chaque côté des opérateurs d'affectation (=, +=…), de
   comparaison (==, <, in, is…) et des opérateurs booléens (and, or, not).
   Pour les opérateurs arithmétiques, on peut retirer les espaces autour des
   opérateurs les plus prioritaires pour montrer l'ordre des calculs (cf. la
   précédence, chap. 5) : "x = a*b + c" est accepté.

3. Un espace APRÈS une virgule ou deux-points, jamais AVANT.

4. Pas d'espace juste à l'intérieur des parenthèses, crochets et accolades, ni
   avant la parenthèse d'un appel de fonction.

5. Pas d'espace autour du "=" d'un paramètre par défaut ou d'un argument nommé
   (cf. chap. 14-15).

6. Pas d'espaces en fin de ligne ("trailing whitespace") : ils sont invisibles,
   mais polluent les comparaisons de fichiers (avec git notamment).
"""
# 👎 (fonctionne, mais à ne pas faire)
liste=[ 1,2 ,3 ]
total =sum (liste)
dico = { "a" : 1 , "b" : 2 }
print (total , dico [ "a" ])  # => 6 1

# 👍
liste = [1, 2, 3]
total = sum(liste)
dico = {"a": 1, "b": 2}
print(total, dico["a"])  # => 6 1

# Paramètres par défaut et arguments nommés : pas d'espace autour du "="
def saluer(nom, politesse="Bonjour"):
    print(f"{politesse} {nom} !")

saluer("Ada", politesse="Salut")  # => Salut Ada !
print("a", "b", sep="-")          # => a-b

"""
7. Lignes vides :
    - 2 lignes vides avant et après chaque fonction définie au niveau du fichier
    - 1 ligne vide pour séparer les "paragraphes" logiques DANS une fonction
    - pas de lignes vides en rafale ailleurs

Exemple :

    import math


    def aire_cercle(rayon):
        return math.pi * rayon ** 2


    def perimetre_cercle(rayon):
        return 2 * math.pi * rayon


    print(aire_cercle(2))

(Ce cours prend parfois des libertés avec cette règle pour rapprocher une
fonction de ses exemples.)

8. Une seule instruction par ligne : on évite le ";" pour mettre deux
   instructions sur la même ligne (comme dans resultat_moche plus haut), et on
   va à la ligne après le ":" d'un if, for, while ou def (sauf rares
   exceptions, cf. les "one-liners" du chap. 12).
"""
# 👎
if total > 5: print("grand")  # => grand

# 👍
if total > 5:
    print("grand")  # => grand


# La PEP 8 : longueur des lignes
#################################

"""
La PEP 8 recommande des lignes de 79 caractères maximum (72 pour les
commentaires et docstrings). Beaucoup de projets acceptent un peu plus : 88
(la valeur par défaut de l'outil black, voir plus bas) ou 99.

Pourquoi limiter ? Pour pouvoir lire le code sans défiler horizontalement,
afficher deux fichiers côte à côte, et parce que les lignes trop longues
sont souvent le signe d'un code trop compliqué.

Ce cours lui-même est écrit en 80 colonnes, comme le montre la bannière en
haut de chaque fichier.

Pour couper une ligne trop longue, la méthode recommandée est d'utiliser les
parenthèses, crochets ou accolades : à l'intérieur, Python ignore les sauts
de ligne.
"""
# Dans les appels de fonctions : on aligne sur la parenthèse ouvrante…
message = "Ceci est un long message"
print(message, "qui continue", "et qui ne tiendrait pas",
      "sur une seule ligne")  # => Ceci est un long message qui continue …

# …ou on passe à la ligne juste après elle, avec une indentation de 4 espaces
print(
    message,
    "sur plusieurs lignes",
)  # => Ceci est un long message sur plusieurs lignes

# Dans les listes et dictionnaires, un élément par ligne. On laisse souvent une
# virgule après le dernier élément ("trailing comma") : ajouter un élément
# ne modifiera alors qu'une seule ligne
jours = [
    "lundi",
    "mardi",
    "mercredi",
]
print(len(jours))  # => 3

# Pour les longues expressions, on ajoute des parenthèses, et on coupe AVANT
# les opérateurs (pour les voir en début de ligne)
salaire_brut = 2500
primes = 300
heures_sup = 120
cotisations = 600
salaire_net = (salaire_brut
               + primes
               + heures_sup
               - cotisations)
print(salaire_net)  # => 2320

# Les longues chaînes peuvent être coupées : deux chaînes côte à côte sont
# automatiquement collées (le chap. 8, "Chaînes longues", le fait avec des
# antislashs : les parenthèses sont plus sûres, voir ci-dessous)
phrase = ("Python colle automatiquement les chaînes "
          "écrites côte à côte.")
print(phrase)  # => Python colle automatiquement les chaînes écrites côte à côte.

"""
On peut aussi couper une ligne avec un antislash "\" en fin de ligne, mais
c'est déconseillé : un simple espace après l'antislash suffit à créer une
erreur, et cet espace est invisible !
"""
somme = 1 + 2 + \
    3
print(somme)  # => 6 (fonctionne, mais préférez les parenthèses)


# La PEP 8 : imports, comparaisons et commentaires
###################################################

"""
1. Les imports (cf. chap. 22) :
    - tout en haut du fichier, après les commentaires d'en-tête
    - un module par ligne
    - groupés dans cet ordre, séparés par une ligne vide :
        1. modules de la bibliothèque standard (math, os, random…)
        2. modules tiers installés (numpy, pandas…)
        3. vos propres modules
    - pas de "from … import *" (on ne sait plus d'où viennent les noms)

    import math
    import os

    import numpy as np

    import mon_module

(Ce cours importe souvent des modules au milieu des fichiers, pour les
présenter au moment où on en parle : ne le faites pas dans vos projets.)
"""

"""
2. Les comparaisons :
    - avec None, on utilise "is" ou "is not", jamais "==" (cf. chap. 15)
    - on ne compare pas un booléen à True ou False : "if est_valide:" plutôt
      que "if est_valide == True:"
    - on écrit "if x not in liste:" plutôt que "if not x in liste:"
"""
est_valide = True
valeur = None

# 👎
if est_valide == True and valeur == None:
    print("valide")  # => valide

# 👍
if est_valide and valeur is None:
    print("valide")  # => valide

if 4 not in liste:
    print("4 n'est pas dans la liste")  # => 4 n'est pas dans la liste

"""
3. Les commentaires (cf. chap. 3) :
    - un "#" suivi d'un espace : "# comme ceci", pas "#comme cela"
    - en fin de ligne : au moins DEUX espaces avant le "#"
    - un commentaire explique POURQUOI on fait quelque chose, pas ce que fait
      le code (le code le dit déjà) ; ce cours est une exception, car il est
      fait pour apprendre !
    - un commentaire faux est pire que pas de commentaire : mettez-les à jour
      en même temps que le code
    - les docstrings (cf. chap. 3) utilisent toujours des triples guillemets
      doubles

4. Les guillemets : Python accepte '…' et "…" (cf. chap. 7). La PEP 8 ne
   choisit pas, mais demande d'être cohérent. Ce cours utilise les guillemets
   doubles.
"""
delai = 30
delai = delai + 5  # 👎 : ajoute 5 à delai (on le voit déjà !)
delai = delai + 5  # 👍 : marge de sécurité, le serveur répond parfois lentement
print(delai)  # => 40


# La PEP 20 : le "Zen of Python"
#################################

"""
La PEP 20 résume en 19 aphorismes la philosophie de Python. Elle est cachée
dans Python lui-même : il suffit d'importer le module "this" (on verra les
imports au chap. 22) pour l'afficher.
"""
import this  # => affiche "The Zen of Python, by Tim Peters" et les aphorismes

"""
Quelques aphorismes à méditer (traduits) :
    - "Beautiful is better than ugly." : le beau vaut mieux que le laid
    - "Explicit is better than implicit." : l'explicite vaut mieux que
      l'implicite
    - "Simple is better than complex." : le simple vaut mieux que le complexe
    - "Readability counts." : la lisibilité compte
    - "Errors should never pass silently." : les erreurs ne devraient jamais
      passer inaperçues (cf. chap. 26)
    - "There should be one-- and preferably only one --obvious way to do it." :
      il devrait y avoir une façon évidente de faire les choses, et de
      préférence une seule
"""


# Outils de formatage
######################

"""
Respecter toutes ces règles à la main est fastidieux. Heureusement, des outils
le font pour nous. On en distingue deux familles :

    1. Les LINTERS ("vérificateurs") analysent le code SANS LE MODIFIER, et
       signalent les écarts à la PEP 8 et les erreurs probables (variable
       inutilisée, import oublié…). Ex. :
         - pycodestyle : vérifie uniquement la PEP 8
         - flake8 : pycodestyle + détection d'erreurs simples (pyflakes)
         - pylint : très complet (et très bavard), donne une note sur 10

    2. Les FORMATTEURS RÉÉCRIVENT le code automatiquement dans un style
       standard. Ex. :
         - black : le plus répandu, presque pas configurable (c'est voulu :
           "on ne discute plus du style"). Il coupe les lignes à 88 caractères
           et utilise les guillemets doubles.
         - autopep8, yapf : plus configurables
         - isort : trie uniquement les imports

    3. ruff, plus récent, fait les deux (linter ET formatteur) : il remplace
       flake8, isort et black, et il est extrêmement rapide. C'est aujourd'hui
       un bon choix par défaut.

Ces outils sont des paquets à installer (cf. chap. 22), puis à lancer depuis
un terminal (cf. chap. 2), sur un fichier ou un dossier entier :

?> pip install ruff black flake8

(ou, sans rien installer : ?> uvx ruff check . — cf. chap. 47)

?> flake8 mon_fichier.py
mon_fichier.py:3:6: E225 missing whitespace around operator

?> black mon_fichier.py          # reformate le fichier
?> black --check .               # vérifie tout le dossier sans rien modifier
?> black --diff mon_fichier.py   # montre ce qui serait modifié

?> ruff check mon_fichier.py     # linter
?> ruff check --fix .            # corrige automatiquement ce qui peut l'être
?> ruff format .                 # formatteur (style quasi identique à black)

Dans la sortie de flake8 ci-dessus, "3:6" désigne la ligne 3, colonne 6, et
"E225" le code de la règle enfreinte : on peut chercher ce code sur Internet
pour en avoir l'explication.

On configure ces outils dans un fichier "pyproject.toml" à la racine du
projet, par exemple :

    [tool.ruff]
    line-length = 79

    [tool.ruff.lint]
    select = ["E", "F", "I"]   # règles PEP 8, pyflakes et tri des imports

    [tool.black]
    line-length = 79

Enfin, on peut désactiver une règle pour UNE ligne avec un commentaire spécial
(à utiliser avec parcimonie) :
"""
import os, sys  # noqa: E401 (2 imports sur une ligne : flake8 et ruff ne le
# signaleront pas ici)


# Configurer son éditeur
#########################

"""
L'idéal est que le formatage se fasse tout seul, sans y penser. Tous les bons
éditeurs (cf. chap. 1) savent :
    - afficher une ligne verticale à 79 ou 88 colonnes ("ruler")
    - afficher le whitespace et supprimer les espaces de fin de ligne
    - remplacer les tabulations par 4 espaces
    - souligner en direct les erreurs signalées par le linter
    - lancer le formatteur à chaque enregistrement ("format on save")

Exemples :

    - VS Code : installer l'extension "Ruff" (ou "Black Formatter"), puis
      dans les réglages (settings.json) :
        "[python]": {
            "editor.formatOnSave": true,
            "editor.defaultFormatter": "charliermarsh.ruff"
        },
        "editor.rulers": [79],
        "files.trimTrailingWhitespace": true

    - Sublime Text : installer via Package Control "LSP" et "LSP-ruff" (ou
      "sublack" pour black), puis dans les préférences :
        "rulers": [79],
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true

    - PyCharm : le formatage PEP 8 est intégré (Code > Reformat Code), et
      on peut ajouter black ou ruff dans les réglages ("Tools").

Il existe aussi un format standard, indépendant de l'éditeur : le fichier
".editorconfig" à la racine du projet (https://editorconfig.org), reconnu par
la plupart des éditeurs :

    [*.py]
    indent_style = space
    indent_size = 4
    trim_trailing_whitespace = true
    insert_final_newline = true
"""


# Automatiser avec git
#######################

"""
Dans un projet à plusieurs, on veut garantir que TOUT le code envoyé est bien
formaté, même si quelqu'un a oublié de configurer son éditeur. On utilise pour
cela un "git hook" : un script que git lance automatiquement à certains
moments, par exemple juste avant chaque commit ("pre-commit").

Le plus simple est d'utiliser l'outil "pre-commit" (https://pre-commit.com) :

    1. on l'installe : ?> pip install pre-commit

    2. on décrit les vérifications voulues dans un fichier
       ".pre-commit-config.yaml" à la racine du dépôt git :

        repos:
          - repo: https://github.com/astral-sh/ruff-pre-commit
            rev: vX.Y.Z    # à remplacer par la dernière version publiée
            hooks:
              - id: ruff
                args: [--fix]
              - id: ruff-format

    3. on active le hook dans le dépôt : ?> pre-commit install

Désormais, chaque "git commit" lance ruff sur les fichiers modifiés. Si un
fichier est mal formaté, il est corrigé, et le commit est refusé : il suffit
de vérifier les modifications, de les ajouter (git add) et de recommencer.

On peut aussi lancer toutes les vérifications à la main :
?> pre-commit run --all-files

Enfin, on peut relancer les mêmes vérifications sur un serveur à chaque envoi
du code (on parle d'"intégration continue", ou CI, par ex. avec GitHub
Actions) : le code mal formaté ne peut alors plus entrer dans le projet.
"""
