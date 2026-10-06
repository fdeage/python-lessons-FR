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
#  Chap. 46     #  Typing et annotations de type : corrigés                    #
#               #                                                              #
################################################################################

"""
Ces corrigés nécessitent Python 3.10 ou plus récent.
"""

import math
import os
import tempfile
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from typing import Literal, TypedDict, TypeVar


##################################
#  Annotations : les bases       #
##################################

"""
1. Sans exécuter : qu'affiche ce programme ? Y a-t-il une erreur ?
"""


def carre(x: int) -> int:
    return x * x


print(carre(3))                 # => 9
print(carre(1.5))               # => 2.25
print(carre.__annotations__)
# => {'x': <class 'int'>, 'return': <class 'int'>}

# Aucune erreur à l'exécution : Python ignore les annotations. carre(1.5)
# fonctionne et renvoie un float. En revanche, mypy signalerait l'appel
# carre(1.5) : un float n'est pas un int.

"""
2. Annotez ces fonctions (paramètres et retour).
"""


def aire_rectangle(largeur: float, hauteur: float) -> float:
    return largeur * hauteur


def saluer(nom: str, poli: bool = True) -> str:
    if poli:
        return "Bonjour " + nom
    return "Salut " + nom


def afficher_total(prix: list[float]) -> None:   # pas de return → None
    print(f"Total : {sum(prix)} €")


print(aire_rectangle(3, 4.5))         # => 13.5
print(saluer("Ada", poli=False))      # => Salut Ada
afficher_total([2.5, 3.0])            # => Total : 5.5 €

# Remarques :
#   - float accepte aussi les int : aire_rectangle(3, 4.5) est correct.
#   - Le paramètre avec valeur par défaut garde sa valeur après l'annotation :
#     "poli: bool = True" (avec des espaces autour du "=", contrairement à
#     "poli=True" sans annotation, cf. chap. 20).

"""
3. Annotez ces variables.
"""
ville: str = "Grenoble"
altitude: int = 212
pluie_mm: float = 1.2
ensoleille: bool = False
print(ville, altitude, pluie_mm, ensoleille)   # => Grenoble 212 1.2 False

# En pratique, on annote rarement ce genre de variables : les vérificateurs
# devinent leur type tout seuls à partir de la valeur ("inférence").


##########################
#  Les collections       #
##########################

"""
4. Écrivez l'annotation de type de chacune de ces valeurs.
"""
a: list[int] = [1, 2, 3]
b: dict[str, float] = {"Lyon": 13.1, "Lille": 11.0}
c: tuple[str, int] = ("Paris", 75)
d: tuple[float, ...] = (1.5, 2.5, 3.5, 4.5)
e: set[str] = {"rouge", "vert"}
f: list[list[int]] = [[1, 0], [0, 1]]
g: dict[str, list[float]] = {"Lyon": [12.0, 14.5], "Brest": [10.0]}

# Attention à la différence pour les tuples :
#   tuple[str, int]      : EXACTEMENT 2 éléments, un str puis un int ;
#   tuple[float, ...]    : un nombre quelconque de floats.

"""
5. Écrivez une fonction annotée frequences(mots).
"""


def frequences(mots: list[str]) -> dict[str, int]:
    compte: dict[str, int] = {}     # annoter un dict vide aide mypy
    for mot in mots:
        compte[mot] = compte.get(mot, 0) + 1
    return compte


print(frequences(["a", "b", "a"]))   # => {'a': 2, 'b': 1}

# Pourquoi annoter "compte" ? Pour un dict VIDE, le vérificateur ne peut pas
# deviner le type des clés et des valeurs : l'annotation le lui dit.

"""
6. Écrivez une fonction annotée min_max(valeurs).
"""


def min_max(valeurs: list[float]) -> tuple[float, float]:
    return min(valeurs), max(valeurs)


print(min_max([12.5, 8.0, 15.25]))   # => (8.0, 15.25)

"""
7. Pourquoi isinstance([1, 2], list[int]) provoque-t-il une erreur ? Comment
   tester qu'une variable est une liste ?
"""
try:
    isinstance([1, 2], list[int])
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : isinstance()
#    argument 2 cannot be a parameterized generic)

print(isinstance([1, 2], list))   # => True

# list[int] est fait pour les ANNOTATIONS, pas pour les tests à l'exécution.
# Vérifier que tous les éléments sont des int demanderait de parcourir la
# liste (ce que Python refuse de faire implicitement) :
valeurs = [1, 2]
print(isinstance(valeurs, list) and all(isinstance(v, int) for v in valeurs))
# => True


############################################
#  Valeurs optionnelles et unions          #
############################################

"""
8. Écrivez une fonction annotée trouver_indice(valeurs, cible), qui renvoie
   un indice ou None, puis utilisez-la correctement.
"""


def trouver_indice(valeurs: list[int], cible: int) -> int | None:
    for i, v in enumerate(valeurs):    # cf. chap. 24
        if v == cible:
            return i
    return None


for cible in [7, 4]:
    indice = trouver_indice([3, 7, 1, 7], cible)
    if indice is None:
        print(f"{cible} : absent")
    else:
        print(f"{cible} : trouvé en position {indice}")
# => 7 : trouvé en position 1
#    4 : absent

# IMPT : on teste "is None", et pas "if not indice" ! L'indice 0 est une
# valeur valide, mais il est "faux" en booléen (cf. chap. 21) : "if not
# indice" confondrait "trouvé en position 0" et "absent".

"""
9. Réécrivez ces annotations avec la syntaxe moderne (Python 3.10+).
"""
# a) Optional[int]            →  int | None
# b) Union[str, bytes]        →  str | bytes
# c) Optional[list[str]]      →  list[str] | None
# d) Union[int, float, None]  →  int | float | None

"""
10. Quelle est la différence entre ces deux signatures ?
        def f(seuil: float = 0.5) -> bool: …
        def g(seuil: float | None = None) -> bool: …
"""
# - f : seuil est un paramètre optionnel (il a une valeur par défaut), mais
#   c'est TOUJOURS un float : dans la fonction, on peut calculer avec.
# - g : seuil peut valoir None. Dans la fonction, il faut traiter ce cas
#   (par exemple "si aucun seuil n'est donné, on le calcule à partir des
#   données") avant de l'utiliser, sinon mypy signale une erreur.


#####################################
#  Any, Callable, Iterable…         #
#####################################

"""
11. Annotez appliquer_deux_fois avec Callable, et testez-la.
"""


def appliquer_deux_fois(f: Callable[[int], int], x: int) -> int:
    return f(f(x))


print(appliquer_deux_fois(lambda n: n + 3, 10))   # => 16

# Callable[[int], int] : "une fonction qui prend UN paramètre int et renvoie
# un int". Les paramètres sont entre crochets, dans une liste.

"""
12. Peut-on annoter moyenne avec Iterable[float] ? Quel type plus général
    convient ?
"""
# Non : la fonction utilise len(valeurs), et un Iterable n'a pas forcément
# de longueur (un générateur, par exemple). mypy le signalerait.
# Sequence[float] convient : il accepte les listes, les tuples, les range…
# tout ce qui a une longueur et des indices.


def moyenne(valeurs: Sequence[float]) -> float:
    return sum(valeurs) / len(valeurs)


print(moyenne([10, 20]), moyenne((1.0, 2.0, 3.0)))   # => 15.0 2.0

# (Pour accepter vraiment n'importe quel itérable, il faudrait compter les
# éléments au fur et à mesure, sans len().)

"""
13. Écrivez une fonction annotée compter_positifs(valeurs) qui accepte
    n'importe quel itérable de nombres.
"""


def compter_positifs(valeurs: Iterable[float]) -> int:
    return sum(1 for v in valeurs if v > 0)


print(compter_positifs([3, -1, 0, 5]))              # => 2
print(compter_positifs((-2.5, 4.0)))                # => 1
print(compter_positifs(x - 2 for x in range(5)))    # => 2

# Iterable : on ne fait que parcourir les valeurs avec un for (caché dans
# l'expression génératrice). C'est le type le plus général possible.


#############################################
#  Alias, TypedDict, Literal, Final         #
#############################################

"""
14. Créez un alias Matrice, puis une fonction annotée transposer.
"""
Matrice = list[list[float]]


def transposer(m: Matrice) -> Matrice:
    # La ligne i du résultat est la colonne i de m (cf. chap. 23)
    return [[ligne[i] for ligne in m] for i in range(len(m[0]))]


print(transposer([[1.0, 2.0], [3.0, 4.0]]))   # => [[1.0, 3.0], [2.0, 4.0]]
print(transposer([[1.0, 2.0, 3.0]]))          # => [[1.0], [2.0], [3.0]]

"""
15. Créez un TypedDict Livre, puis une fonction note_moyenne(livre).
"""


class Livre(TypedDict):
    titre: str
    auteur: str
    annee: int
    notes: list[int]


def note_moyenne(livre: Livre) -> float:
    return sum(livre["notes"]) / len(livre["notes"])


dune: Livre = {"titre": "Dune", "auteur": "Frank Herbert", "annee": 1965,
               "notes": [5, 4, 5, 3]}
print(note_moyenne(dune))   # => 4.25

# Avantage du TypedDict : mypy signalerait une faute de frappe comme
# livre["note"] ou livre["anne"], ou une année écrite sous forme de str.

"""
16. Écrivez une fonction annotée arrondir(valeur, mode), avec Literal.
"""
Mode = Literal["haut", "bas", "proche"]


def arrondir(valeur: float, mode: Mode) -> int:
    if mode == "haut":
        return math.ceil(valeur)
    elif mode == "bas":
        return math.floor(valeur)
    return round(valeur)


print(arrondir(2.4, "haut"), arrondir(2.6, "bas"), arrondir(2.6, "proche"))
# => 3 2 3

# arrondir(2.4, "superieur") serait signalé par mypy. À l'exécution, en
# revanche, la fonction renverrait round(2.4) sans broncher : pour une
# protection à l'exécution, il faudrait ajouter un "raise ValueError"
# (cf. chap. 26).


##############################################
#  Classes, dataclasses et génériques       #
##############################################

"""
17. Annotez complètement la classe Thermometre.
"""


class Thermometre:
    def __init__(self, lieu: str, valeurs: list[float] | None = None) -> None:
        self.lieu = lieu
        self.valeurs: list[float] = valeurs if valeurs is not None else []

    def ajouter(self, v: float) -> None:
        self.valeurs.append(v)

    def maximum(self) -> float | None:
        return max(self.valeurs) if self.valeurs else None


t = Thermometre("Lyon")
print(t.maximum())   # => None
t.ajouter(14.5)
t.ajouter(17.0)
print(t.maximum())   # => 17.0

# - On n'annote pas self.
# - __init__ renvoie toujours None.
# - valeurs vaut None par défaut (pour éviter le piège de la liste mutable
#   par défaut, cf. chap. 34) : son type est donc "list[float] | None".
# - maximum() renvoie None si aucune valeur n'a été ajoutée.

"""
18. Transformez la classe Point en dataclass annotée.
"""


@dataclass
class Point:
    x: float
    y: float
    nom: str = "?"


print(Point(1.0, 2.5))           # => Point(x=1.0, y=2.5, nom='?')
print(Point(0, 0, "origine"))    # => Point(x=0, y=0, nom='origine')

# @dataclass lit les annotations pour écrire __init__, __repr__ et __eq__ à
# notre place (cf. chap. 35).

"""
19. Écrivez une fonction générique dernier(elements), annotée avec un
    TypeVar.
"""
T = TypeVar("T")


def dernier(elements: Sequence[T]) -> T:
    return elements[-1]


print(dernier([1, 2, 3]))        # => 3
print(dernier("abc"))            # => c
print(dernier((True, False)))    # => False

# Grâce au TypeVar, mypy sait que dernier([1, 2, 3]) est un int et que
# dernier("abc") est une str. (Depuis Python 3.12 : def dernier[T](…).)

"""
20. Écrivez une fonction générique filtrer(elements, condition).
"""


def filtrer(elements: Iterable[T], condition: Callable[[T], bool]) -> list[T]:
    return [e for e in elements if condition(e)]


print(filtrer([1, 5, 8, 3], lambda n: n > 4))               # => [5, 8]
print(filtrer(["kiwi", "ananas", "fraise"], lambda m: "a" in m))
# => ['ananas', 'fraise']

# Le même T apparaît trois fois : les éléments, le paramètre de la
# condition, et les éléments du résultat ont tous le même type.


##############################
#  Vérifier avec mypy        #
##############################

"""
21. Sans exécuter mypy : quelles erreurs signalerait-il dans ce code ?
"""
code_exercice = '''
def taux(reussis: int, total: int) -> float:
    return reussis / total


def mention(note: float) -> str:
    if note >= 16:
        return "très bien"
    elif note >= 12:
        return "bien"


resultat: int = taux(3, 4)
print(taux("3", 4))
'''
# Trois erreurs :
#   1. mention() : si note < 12, la fonction n'atteint aucun return et
#      renvoie donc None, alors qu'elle annonce une str ("Missing return
#      statement").
#   2. resultat est annoté int, mais taux() renvoie un float.
#   3. taux("3", 4) : on passe une str là où un int est attendu.
# Remarquez qu'à l'exécution, seule la troisième provoquerait une erreur…
# et seulement au moment de la division.

"""
22. (Si mypy est installé) Vérifiez vos réponses avec mypy.
"""
try:
    from mypy import api as mypy_api
except ImportError:
    mypy_api = None
    print("mypy n'est pas installé : exercice 22 sauté.")
    print("Pour l'installer : uv add --dev mypy (ou : python3 -m pip install "
          "mypy)")

if mypy_api is not None:
    with tempfile.TemporaryDirectory() as dossier:
        chemin = os.path.join(dossier, "ex21.py")
        with open(chemin, "w", encoding="utf-8") as fichier:
            fichier.write(code_exercice)
        sortie, _, code_retour = mypy_api.run(
            [chemin, "--cache-dir", os.path.join(dossier, "cache"),
             "--no-color-output", "--no-error-summary"])
        for ligne in sortie.splitlines():
            print(ligne.replace(dossier + os.sep, ""))
# => ex21.py:6: error: Missing return statement  [return]
#    ex21.py:13: error: Incompatible types in assignment (expression has
#    type "float", variable has type "int")  [assignment]
#    ex21.py:14: error: Argument 1 to "taux" has incompatible type "str";
#    expected "int"  [arg-type]
# (Sortie obtenue avec mypy 2.4 ; la formulation peut varier selon la
# version. Le dossier temporaire, et donc le cache de mypy, est supprimé à
# la sortie du bloc with.)
