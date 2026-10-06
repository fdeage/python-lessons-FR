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
#  Chap. 46     #  Typing et annotations de type                               #
#               #                                                              #
################################################################################
#
#  - Rappel : Python est dynamiquement typé
#  - Les annotations de type
#  - Annoter variables, paramètres et retours
#  - Les annotations ne sont pas vérifiées à l'exécution
#  - Annoter les collections : list[int], dict[str, float]…
#  - Valeurs optionnelles et unions : Optional, "X | None"
#  - Any et Callable
#  - Accepter large, retourner précis : Iterable, Sequence, Mapping
#  - Les alias de types
#  - TypedDict, Literal et Final
#  - Annoter ses classes et ses dataclasses
#  - Les génériques : TypeVar
#  - "from __future__ import annotations"
#  - Vérifier ses types avec mypy
#  - D'autres outils : pyright, ty et les éditeurs
#  - Bonnes pratiques
#  - En bref
#
#############################################

import os
import tempfile
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import (Any, Final, Literal, Optional, TypedDict, TypeVar, Union,
                    get_type_hints)

"""
Ce chapitre utilise des syntaxes apparues dans différentes versions de
Python. Chacune est signalée au fur et à mesure. Le fichier complet
nécessite Python 3.10 ou plus récent.
"""


# Rappel : Python est dynamiquement typé
#########################################

"""
Au chap. 10, on a vu qu'en Python une variable n'a pas de type fixé : c'est
la VALEUR qui a un type, et une même variable peut contenir successivement
un entier, puis une chaîne. On dit que Python est "dynamiquement typé".
"""
x = 42
print(type(x))   # => <class 'int'>
x = "quarante-deux"
print(type(x))   # => <class 'str'>

"""
C'est très pratique pour écrire vite de petits programmes. Mais dans un gros
programme, cela rend certaines erreurs difficiles à repérer : on ne sait
qu'À L'EXÉCUTION qu'une fonction a reçu une chaîne au lieu d'un nombre…
parfois des heures après le lancement d'un long calcul.

D'autres langages (Java, C, Rust…) sont "statiquement typés" : chaque
variable a un type déclaré, et le compilateur refuse le programme si les
types ne collent pas, AVANT toute exécution.

Python propose un compromis : les "annotations de type" (ou "type hints").
On peut indiquer les types attendus… sans que Python ne change sa façon
d'exécuter le code.
"""


# Les annotations de type
##########################

"""
Une annotation de type est une indication, écrite dans le code, du type
attendu d'une variable, d'un paramètre ou d'une valeur de retour.

Elles servent à trois choses :
    1. DOCUMENTER : en lisant la signature d'une fonction, on sait tout de
       suite ce qu'elle attend et ce qu'elle renvoie.
    2. AIDER L'ÉDITEUR : VS Code, PyCharm… s'en servent pour proposer
       l'autocomplétion et signaler les erreurs pendant que vous tapez.
    3. VÉRIFIER : des outils comme mypy (voir plus bas) analysent tout le
       programme et détectent les incohérences de types, sans l'exécuter.

On en a déjà croisé au chap. 14 et au chap. 29 : "def f(x: int) -> int:".
Ce chapitre va beaucoup plus loin.
"""


# Annoter variables, paramètres et retours
###########################################

"""
La syntaxe :
    - pour un paramètre : "nom: type", après le nom ;
    - pour le retour : "-> type", entre la parenthèse fermante et le ":" ;
    - pour une variable : "nom: type = valeur" (Python 3.6+).
"""


def prix_ttc(prix_ht: float, taux_tva: float = 0.2) -> float:
    return prix_ht * (1 + taux_tva)


print(prix_ttc(100.0))   # => 120.0

ville: str = "Lyon"
population: int = 522_000
temperature_moyenne: float = 13.1
est_capitale: bool = False

"""
On peut lire les annotations d'une fonction dans son attribut
__annotations__ (cf. chap. 29) :
"""
print(prix_ttc.__annotations__)
# => {'prix_ht': <class 'float'>, 'taux_tva': <class 'float'>,
#     'return': <class 'float'>}

"""
Une fonction qui ne renvoie rien (pas de "return", ou "return" seul)
renvoie en fait None (cf. chap. 15) : on l'annote "-> None".
"""


def afficher_bienvenue(nom: str) -> None:
    print(f"Bienvenue, {nom} !")


afficher_bienvenue("Ada")   # => Bienvenue, Ada !

"""
Note : int est accepté là où l'on attend un float. Par convention, prix_ttc(100)
est donc correct pour les vérificateurs de types, même si 100 est un int.
"""


# Les annotations ne sont pas vérifiées à l'exécution
######################################################

"""
IMPT : Python N'UTILISE PAS les annotations quand il exécute le code. Ce
sont des indications pour les humains et les outils, rien de plus. Une
fonction annotée accepte n'importe quoi :
"""


def doubler(n: int) -> int:
    return n * 2


print(doubler(21))       # => 42
print(doubler("ha"))     # => haha  : aucune erreur, malgré l'annotation !
print(doubler([1, 2]))   # => [1, 2, 1, 2]

nombre: int = "pas un nombre"   # aucune erreur non plus
print(nombre)                   # => pas un nombre

"""
Pour qu'une erreur de type soit détectée, il faut :
    - soit un outil de vérification "statique" comme mypy (voir plus bas),
      qui lit le code sans l'exécuter ;
    - soit des vérifications explicites dans le code, avec isinstance()
      (cf. chap. 33 et 35), qui ont lieu à l'exécution.

Voici l'intérêt des annotations : cette fonction a un bogue que mypy
signalerait immédiatement, alors que Python ne le découvre qu'à l'exécution,
au moment du calcul :
"""


def moyenne(notes: list[float]) -> float:
    return sum(notes) / len(notes)


notes_saisies = ["12", "15", "9"]   # des strings, lues dans un fichier…
try:
    print(moyenne(notes_saisies))
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : unsupported operand
#    type(s) for +: 'int' and 'str')

"""
Le message d'erreur parle de "+" et de 'int' : il ne dit pas clairement que
le problème vient des données passées à moyenne(). Avec mypy, on aurait
obtenu, avant même de lancer le programme, une erreur du genre :
    Argument 1 to "moyenne" has incompatible type "list[str]";
    expected "list[float]"
"""


# Annoter les collections : list[int], dict[str, float]…
#########################################################

"""
Pour les collections, on précise le type des ÉLÉMENTS entre crochets
(Python 3.9+) :

    list[int]             une liste d'entiers
    set[str]              un ensemble de chaînes
    dict[str, float]      un dictionnaire : clés str, valeurs float
    tuple[str, int]       un tuple de EXACTEMENT 2 éléments : un str, un int
    tuple[int, ...]       un tuple d'entiers, de longueur quelconque
    list[list[float]]     une liste de listes de floats (une matrice)
"""
temperatures: list[float] = [12.5, 14.0, 9.8]
villes_visitees: set[str] = {"Lyon", "Nantes"}
populations: dict[str, int] = {"Lyon": 522_000, "Nantes": 320_000}
point: tuple[float, float] = (45.76, 4.84)   # latitude, longitude
scores: tuple[int, ...] = (12, 15, 9, 18)
matrice: list[list[float]] = [[1.0, 2.0], [3.0, 4.0]]


def plus_peuplee(populations: dict[str, int]) -> tuple[str, int]:
    ville = max(populations, key=populations.get)   # cf. chap. 27
    return ville, populations[ville]


print(plus_peuplee(populations))   # => ('Lyon', 522000)

"""
Avant Python 3.9, on ne pouvait pas écrire list[int] : il fallait importer
des versions spéciales depuis le module typing, avec une majuscule :
    from typing import List, Dict, Set, Tuple
    def f(valeurs: List[int]) -> Dict[str, int]: …
Vous rencontrerez encore souvent cette syntaxe dans du code existant. Elle
fonctionne toujours, mais elle est dépréciée.

Ces types "paramétrés" servent aux annotations, pas aux tests à
l'exécution :
"""
try:
    print(isinstance(temperatures, list[float]))
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : isinstance()
#    argument 2 cannot be a parameterized generic)

print(isinstance(temperatures, list))   # => True : ceci fonctionne


# Valeurs optionnelles et unions : Optional, "X | None"
########################################################

"""
Souvent, une fonction renvoie une valeur… OU None si elle n'a rien trouvé
(cf. chap. 15). On l'annote "X | None" (Python 3.10+) :
"""


def chercher_ville(code_postal: str) -> str | None:
    annuaire = {"69001": "Lyon", "44000": "Nantes"}
    return annuaire.get(code_postal)   # None si le code est absent


print(chercher_ville("69001"))   # => Lyon
print(chercher_ville("99999"))   # => None

"""
L'intérêt : l'annotation RAPPELLE à celui qui utilise la fonction qu'il doit
traiter le cas None. mypy signale une erreur si l'on écrit
chercher_ville("…").upper() sans avoir vérifié que le résultat n'est pas
None :
"""
resultat = chercher_ville("99999")
if resultat is not None:
    print(resultat.upper())
else:
    print("Ville inconnue")   # => Ville inconnue

"""
Plus généralement, "A | B" signifie "A ou B" :
"""


def formater(valeur: int | float | str) -> str:
    return f"[{valeur}]"


print(formater(3), formater(2.5), formater("ok"))   # => [3] [2.5] [ok]

"""
Avant Python 3.10, on écrivait la même chose avec le module typing :
    Optional[str]            ⇔   str | None
    Union[int, float, str]   ⇔   int | float | str
Ces deux formes sont strictement équivalentes :
"""
print(Optional[str] == (str | None))               # => True
print(Union[int, float] == (int | float))          # => True

"""
Attention à ne pas confondre :
    - un paramètre "optionnel" au sens de "qui a une valeur par défaut"
      (cf. chap. 15) : def f(taux: float = 0.2) ;
    - un paramètre qui PEUT VALOIR None : def f(taux: float | None = None).
"""


# Any et Callable
##################

"""
Any signifie "n'importe quel type" : le vérificateur ne contrôle plus rien.
C'est une porte de sortie quand le type est vraiment impossible à décrire,
mais il faut l'utiliser avec parcimonie : Any désactive la vérification.
"""


def decrire(valeur: Any) -> str:
    return f"{valeur!r} est de type {type(valeur).__name__}"


print(decrire(3.14))       # => 3.14 est de type float
print(decrire([1, "a"]))   # => [1, 'a'] est de type list

"""
Callable décrit une FONCTION (cf. chap. 32 : les fonctions sont des objets
comme les autres). La syntaxe est :
    Callable[[type_param1, type_param2, …], type_retour]
On l'importe depuis collections.abc (Python 3.9+ ; avant : depuis typing).
"""


def appliquer(fonction: Callable[[float], float],
              valeurs: list[float]) -> list[float]:
    return [fonction(v) for v in valeurs]


def celsius_vers_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


print(appliquer(celsius_vers_fahrenheit, [0.0, 100.0, 37.0]))
# => [32.0, 212.0, 98.6]
print(appliquer(lambda v: round(v), [1.4, 2.6]))   # => [1, 3]


# Accepter large, retourner précis : Iterable, Sequence, Mapping
#################################################################

"""
Prenons une fonction qui calcule le total de valeurs. Si on l'annote avec
list[float], on interdit (pour mypy) de lui passer un tuple, un set ou un
générateur… alors qu'elle fonctionnerait parfaitement avec eux !

Le module collections.abc propose des types plus GÉNÉRAUX, qui décrivent ce
que l'on fait avec l'objet plutôt que ce qu'il est :

    Iterable[X]   on peut le parcourir avec for (liste, tuple, set, dict,
                  générateur, fichier… cf. chap. 23 et 36)
    Sequence[X]   on peut le parcourir, ET utiliser len() et les indices
                  [i] (liste, tuple, str, range…)
    Mapping[K, V] on peut faire d[cle], .keys(), .items()… (dict…)

IMPT : la règle d'or est "accepter large, retourner précis" :
    - pour les PARAMÈTRES, utilisez le type le plus général possible, pour
      que la fonction soit utilisable dans un maximum de situations ;
    - pour le RETOUR, utilisez le type le plus précis, pour que l'appelant
      sache exactement ce qu'il reçoit.
"""


def total(valeurs: Iterable[float]) -> float:
    resultat = 0.0
    for v in valeurs:
        resultat += v
    return resultat


print(total([1.5, 2.5]))                 # => 4.0  (une liste)
print(total((1.0, 2.0, 3.0)))            # => 6.0  (un tuple)
print(total(x / 2 for x in range(4)))    # => 3.0  (un générateur)


def premier_et_dernier(elements: Sequence[str]) -> tuple[str, str]:
    # Sequence : on a besoin des indices, un simple Iterable ne suffit pas
    return elements[0], elements[-1]


print(premier_et_dernier(["lundi", "mardi", "mercredi"]))
# => ('lundi', 'mercredi')
print(premier_et_dernier("abc"))   # => ('a', 'c') : une str est une Sequence


def cles_triees(d: Mapping[str, int]) -> list[str]:
    return sorted(d.keys())


print(cles_triees({"b": 2, "a": 1}))   # => ['a', 'b']


# Les alias de types
#####################

"""
Quand un type devient long, on peut lui donner un nom : c'est un "alias".
Il suffit de l'affecter à une variable (avec une majuscule, comme une
classe).
"""
Coordonnees = tuple[float, float]               # (latitude, longitude)
Releves = dict[str, list[float]]                # ville -> températures


def moyennes_par_ville(releves: Releves) -> dict[str, float]:
    return {ville: sum(t) / len(t) for ville, t in releves.items()}


def distance_approx(a: Coordonnees, b: Coordonnees) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


releves: Releves = {"Lyon": [12.0, 14.0], "Brest": [10.0, 11.0, 12.0]}
print(moyennes_par_ville(releves))   # => {'Lyon': 13.0, 'Brest': 11.0}
print(round(distance_approx((45.76, 4.84), (47.22, -1.55)), 2))   # => 6.55

"""
Les alias rendent les signatures plus lisibles, et permettent de changer
une définition à un seul endroit (cf. chap. 14 : "source unique de
vérité").

Note : depuis Python 3.12, on peut aussi écrire
    type Releves = dict[str, list[float]]
avec le mot-clé "type". On garde ici la forme simple, compatible avec les
versions précédentes.
"""


# TypedDict, Literal et Final
##############################

"""
1. TypedDict (Python 3.8+) : en Data Science, on manipule souvent des
   dictionnaires qui représentent un "enregistrement" (une ligne de
   données), avec des clés fixes de types différents. dict[str, Any] serait
   trop vague. TypedDict décrit précisément chaque clé :
"""


class Station(TypedDict):
    nom: str
    altitude: int
    temperatures: list[float]


chamonix: Station = {"nom": "Chamonix", "altitude": 1035,
                     "temperatures": [-2.0, 1.5, 4.0]}
print(chamonix["altitude"])   # => 1035
print(type(chamonix))         # => <class 'dict'> : c'est un dict normal !

"""
À l'exécution, un TypedDict est un simple dictionnaire. Mais mypy vérifie
que l'on n'oublie pas de clé, que l'on n'en invente pas
(chamonix["altitud"] serait signalé) et que les valeurs ont le bon type.

2. Literal (Python 3.8+) : la valeur doit être l'une de celles listées.
   Idéal pour les paramètres qui n'acceptent que quelques chaînes précises :
"""
Agregation = Literal["moyenne", "min", "max"]


def agreger(valeurs: list[float], methode: Agregation) -> float:
    if methode == "moyenne":
        return sum(valeurs) / len(valeurs)
    elif methode == "min":
        return min(valeurs)
    else:
        return max(valeurs)


print(agreger([3.0, 9.0, 6.0], "moyenne"))   # => 6.0
print(agreger([3.0, 9.0, 6.0], "max"))       # => 9.0
# agreger([3.0], "médiane") serait signalé par mypy : "médiane" n'est pas
# dans la liste. (À l'exécution, la fonction renverrait max, sans erreur !)

"""
3. Final (Python 3.8+, bonus) : indique qu'une variable est une CONSTANTE,
   qui ne doit pas être réaffectée. Python n'empêche rien, mais mypy
   signale toute réaffectation.
"""
TAUX_TVA: Final = 0.2
ZERO_ABSOLU_CELSIUS: Final[float] = -273.15
print(TAUX_TVA, ZERO_ABSOLU_CELSIUS)   # => 0.2 -273.15


# Annoter ses classes et ses dataclasses
#########################################

"""
Dans une classe (cf. chap. 34), on annote les méthodes comme des fonctions.
On n'annote PAS self (son type est évident). Une méthode peut renvoyer un
objet de sa propre classe : on écrit alors le nom de la classe entre
guillemets (car la classe n'est pas encore complètement définie à cet
endroit).
"""


class Compteur:
    def __init__(self, depart: int = 0) -> None:   # __init__ renvoie None
        self.valeur: int = depart

    def incrementer(self, pas: int = 1) -> "Compteur":
        self.valeur += pas
        return self

    def __repr__(self) -> str:
        return f"Compteur({self.valeur})"


c = Compteur()
print(c.incrementer().incrementer(5))   # => Compteur(6)

"""
Avec les dataclasses (cf. chap. 35), les annotations sont OBLIGATOIRES :
c'est justement grâce à elles que @dataclass trouve les attributs et écrit
__init__ et __repr__ pour vous.
"""


@dataclass
class Mesure:
    ville: str
    temperature: float
    humidite: int = 50
    tags: list[str] = field(default_factory=list)


m = Mesure("Lyon", 21.5)
print(m)   # => Mesure(ville='Lyon', temperature=21.5, humidite=50, tags=[])

"""
La fonction typing.get_type_hints() renvoie les annotations d'une classe ou
d'une fonction sous forme de dictionnaire :
"""
print(get_type_hints(Mesure))
# => {'ville': <class 'str'>, 'temperature': <class 'float'>,
#     'humidite': <class 'int'>, 'tags': list[str]}

"""
Note : même avec une dataclass, les types ne sont pas vérifiés à
l'exécution :
"""
bizarre = Mesure(ville=42, temperature="chaud")   # aucune erreur…
print(bizarre.temperature)                        # => chaud
# … mais mypy signalerait les deux arguments.


# Les génériques : TypeVar
###########################

"""
Prenons une fonction qui renvoie le premier élément d'une séquence. Comment
l'annoter ?
    - Sequence[Any] -> Any : on perd l'information. Si on lui passe une
      liste de str, mypy ne sait pas que le résultat est une str.
    - Il faut dire : "si on reçoit une séquence de T, on renvoie un T", T
      étant n'importe quel type. C'est une "variable de type".
"""
T = TypeVar("T")


def premier(elements: Sequence[T]) -> T:
    return elements[0]


print(premier([3, 1, 4]))          # => 3      (mypy sait que c'est un int)
print(premier(["a", "b"]))         # => a      (mypy sait que c'est une str)

"""
On dit que premier() est une fonction "générique". Depuis Python 3.12, on
peut l'écrire sans TypeVar, avec une syntaxe plus courte :
    def premier[T](elements: Sequence[T]) -> T: …
On garde ici la forme avec TypeVar, qui fonctionne sur toutes les versions.
"""


def regrouper_par(elements: Iterable[T],
                  cle: Callable[[T], str]) -> dict[str, list[T]]:
    groupes: dict[str, list[T]] = {}
    for e in elements:
        groupes.setdefault(cle(e), []).append(e)   # cf. chap. 27
    return groupes


print(regrouper_par(["pomme", "poire", "kiwi"], lambda mot: mot[0]))
# => {'p': ['pomme', 'poire'], 'k': ['kiwi']}


# "from __future__ import annotations"
#######################################

"""
Vous verrez souvent cette ligne en haut des fichiers :
    from __future__ import annotations
(Elle doit être la toute première instruction du fichier : c'est pourquoi
ce chapitre ne l'utilise pas lui-même.)

Elle demande à Python de NE PAS ÉVALUER les annotations au moment où il lit
la définition d'une fonction, mais de les garder sous forme de texte. Deux
avantages :
    1. on peut utiliser les syntaxes récentes (list[int], int | None) avec
       des versions plus anciennes de Python (dès 3.7), car Python ne les
       évalue jamais ;
    2. on peut faire référence à une classe qui n'est pas encore définie
       sans mettre son nom entre guillemets (le "Compteur" plus haut).

Démontrons-le : on exécute un petit programme avec et sans cette ligne
(exec() exécute du code contenu dans une chaîne, cf. chap. 26).
"""
code = """
def f(x: int) -> int:
    return x
print(f.__annotations__)
"""
exec(code)
# => {'x': <class 'int'>, 'return': <class 'int'>}
exec("from __future__ import annotations\n" + code)
# => {'x': 'int', 'return': 'int'}  : les annotations sont restées du texte

"""
Note : depuis Python 3.14, Python évalue de toute façon les annotations "à
la demande" (de façon paresseuse), ce qui règle le second problème sans
cette ligne. Elle reste utile pour la compatibilité avec les anciennes
versions.
"""


# Vérifier ses types avec mypy
###############################

"""
mypy est l'outil historique de vérification des types en Python. Il LIT
votre code sans l'exécuter, et signale les incohérences.

Installation (c'est un paquet externe, cf. chap. 22 et 47) :
    uv add --dev mypy               (dans un projet géré avec uv)
    python3 -m pip install mypy     (avec pip)

Utilisation, dans un terminal :
    mypy mon_programme.py

Pour la démonstration, on écrit un petit programme avec deux erreurs de
type dans un dossier temporaire, et on appelle mypy depuis Python grâce à
son module mypy.api.
"""
try:
    from mypy import api as mypy_api
except ImportError:
    mypy_api = None
    print("mypy n'est pas installé : la démonstration est sautée.")
    print("Pour l'installer : uv add --dev mypy (ou : python3 -m pip install "
          "mypy)")

programme_avec_erreurs = '''
def moyenne(notes: list[float]) -> float:
    return sum(notes) / len(notes)


def chercher(code: str) -> str | None:
    return {"69001": "Lyon"}.get(code)


print(moyenne(["12", "15"]))
print(chercher("69001").upper())
'''

if mypy_api is not None:
    with tempfile.TemporaryDirectory() as dossier:   # cf. chap. 36
        chemin = os.path.join(dossier, "exemple.py")
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(programme_avec_erreurs)
        # --cache-dir : on range le cache de mypy dans le dossier temporaire,
        # pour ne laisser aucun fichier ".mypy_cache" derrière nous.
        sortie, erreurs, code_retour = mypy_api.run(
            [chemin, "--cache-dir", os.path.join(dossier, "cache"),
             "--no-color-output", "--no-error-summary"])
        # On retire le chemin du dossier temporaire, qui change à chaque fois
        for ligne in sortie.splitlines():
            print(ligne.replace(dossier + os.sep, ""))
        print("code de retour :", code_retour)
# => exemple.py:10: error: List item 0 has incompatible type "str"; expected
#    "float"  [list-item]
#    exemple.py:10: error: List item 1 has incompatible type "str"; expected
#    "float"  [list-item]
#    exemple.py:11: error: Item "None" of "str | None" has no attribute
#    "upper"  [union-attr]
#    code de retour : 1
# (Sortie obtenue avec mypy 2.4 ; la formulation peut varier selon la
# version.)

"""
Lisons ce rapport :
    - "exemple.py:10" : le fichier et le numéro de ligne ;
    - le message explique le problème : on passe des str là où on attend
      des float ;
    - le code entre crochets ([list-item], [union-attr]) identifie le type
      d'erreur ; il permet de la rechercher dans la documentation ;
    - la seconde erreur rappelle que chercher() peut renvoyer None : appeler
      .upper() sans vérifier est dangereux.
    - le code de retour vaut 1 s'il y a des erreurs, 0 sinon : pratique
      pour bloquer un commit (cf. chap. 20 : pre-commit) ou une intégration
      continue.

Remarque : mypy ne vérifie PAS les fonctions sans annotations (il les
considère comme "non typées"). On peut donc ajouter des annotations petit à
petit dans un projet existant. L'option --strict, au contraire, exige des
annotations partout.
"""


# D'autres outils : pyright, ty et les éditeurs
################################################

"""
mypy n'est pas le seul vérificateur de types :
    - pyright (Microsoft) : très rapide ; c'est lui qui travaille en coulisses
      dans l'extension Python de VS Code (sous le nom "Pylance") ;
    - ty (Astral, les créateurs de ruff et uv, cf. chap. 20 et 47) : un
      vérificateur récent, écrit en Rust, extrêmement rapide ;
    - PyCharm intègre son propre vérificateur.

Dans un éditeur bien configuré, les erreurs de types sont SOULIGNÉES pendant
que vous tapez, comme les fautes d'orthographe dans un traitement de texte.
Activez cette fonction : c'est le moyen le plus simple de profiter des
annotations au quotidien.

En Data Science, sachez que numpy et pandas fournissent leurs propres
annotations (par exemple numpy.typing.NDArray pour un tableau numpy, cf.
chap. 38), plus ou moins complètes selon les versions.
"""


# Bonnes pratiques
###################

"""
1. Annotez en priorité les SIGNATURES des fonctions (paramètres et retour).
   À l'intérieur des fonctions, les vérificateurs DEVINENT le plus souvent
   le type des variables tout seuls ("inférence de type") : x = 3 est
   évidemment un int, inutile d'écrire x: int = 3.

2. Accepter large, retourner précis : Iterable / Sequence / Mapping en
   paramètre, list / dict / tuple en retour.

3. Évitez Any autant que possible : il désactive la vérification.

4. Préférez la syntaxe moderne (list[int], int | None) si votre version de
   Python le permet ; sinon, utilisez from __future__ import annotations.

5. Utilisez des alias, des TypedDict et des dataclasses pour donner des noms
   parlants à vos structures de données.

6. Faites tourner un vérificateur régulièrement (dans l'éditeur, dans
   pre-commit, dans l'intégration continue).

7. Les annotations ne remplacent ni les tests (cf. chap. 29 et 37), ni les
   vérifications des données venant de l'extérieur (fichiers, saisies,
   API…), qui restent à faire à l'exécution.

8. Pour un petit script de 20 lignes, ne vous forcez pas : les annotations
   prennent tout leur sens dans les programmes qui grandissent, et quand on
   travaille à plusieurs.
"""


# En bref
##########

"""
    - Python est dynamiquement typé ; les annotations sont des indications,
      NON vérifiées à l'exécution.
    - Syntaxe : def f(x: int, y: float = 1.0) -> str: …  et  nom: type = …
    - Collections (3.9+) : list[int], dict[str, float], tuple[int, ...],
      set[str]. Avant 3.9 : List, Dict… depuis typing.
    - "X | None" (3.10+) ⇔ Optional[X] ; "A | B" ⇔ Union[A, B].
    - Any = pas de vérification ; Callable[[params], retour] = une fonction.
    - Paramètres : Iterable, Sequence, Mapping ; retours : types précis.
    - Alias, TypedDict, Literal, Final donnent du sens aux types.
    - Les dataclasses s'appuient sur les annotations.
    - TypeVar pour les fonctions génériques.
    - mypy, pyright, ty vérifient les types sans exécuter le code.
"""
