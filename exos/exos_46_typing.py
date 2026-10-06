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
#  Chap. 46     #  Typing et annotations de type : exercices                   #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Rappel : Python n'utilise pas les annotations à l'exécution. Pour
vérifier vraiment vos annotations, installez mypy (uv add --dev mypy, ou
python3 -m pip install mypy) et lancez "mypy exos_46_typing.py".

Les corrigés sont dans le fichier corrs/corr_46_typing.py.
Ces exercices nécessitent Python 3.10 ou plus récent.
"""


##################################
#  Annotations : les bases       #
##################################

"""
1. Sans exécuter : qu'affiche ce programme ? Y a-t-il une erreur ?
       def carre(x: int) -> int:
           return x * x

       print(carre(3))
       print(carre(1.5))
       print(carre.__annotations__)

2. Annotez ces fonctions (paramètres et retour) :
       def aire_rectangle(largeur, hauteur):
           return largeur * hauteur

       def saluer(nom, poli=True):
           if poli:
               return "Bonjour " + nom
           return "Salut " + nom

       def afficher_total(prix):
           print(f"Total : {sum(prix)} €")

3. Annotez ces variables :
       ville = "Grenoble"
       altitude = 212
       pluie_mm = 1.2
       ensoleille = False
"""


##########################
#  Les collections       #
##########################

"""
4. Écrivez l'annotation de type de chacune de ces valeurs :
       a) [1, 2, 3]
       b) {"Lyon": 13.1, "Lille": 11.0}
       c) ("Paris", 75)
       d) (1.5, 2.5, 3.5, 4.5)   (longueur quelconque)
       e) {"rouge", "vert"}
       f) [[1, 0], [0, 1]]
       g) {"Lyon": [12.0, 14.5], "Brest": [10.0]}

5. Écrivez une fonction annotée frequences(mots) qui reçoit une liste de
   chaînes et renvoie un dictionnaire {mot: nombre d'apparitions}.
       frequences(["a", "b", "a"])  => {'a': 2, 'b': 1}

6. Écrivez une fonction annotée min_max(valeurs) qui reçoit une liste de
   floats et renvoie un tuple (minimum, maximum).

7. Pourquoi cette ligne provoque-t-elle une erreur ? Comment tester qu'une
   variable est une liste ?
       isinstance([1, 2], list[int])
"""


############################################
#  Valeurs optionnelles et unions          #
############################################

"""
8. Écrivez une fonction annotée trouver_indice(valeurs, cible) qui renvoie
   l'indice de la première occurrence de cible dans une liste d'entiers, ou
   None si elle est absente. Utilisez la syntaxe "X | None".
   Puis utilisez-la correctement : affichez "trouvé en position …" ou
   "absent" selon le cas.

9. Réécrivez ces annotations avec la syntaxe moderne (Python 3.10+) :
       a) Optional[int]
       b) Union[str, bytes]
       c) Optional[list[str]]
       d) Union[int, float, None]

10. Quelle est la différence entre ces deux signatures ?
        def f(seuil: float = 0.5) -> bool: …
        def g(seuil: float | None = None) -> bool: …
"""


#####################################
#  Any, Callable, Iterable…         #
#####################################

"""
11. Annotez cette fonction avec Callable :
        def appliquer_deux_fois(f, x):
            return f(f(x))
    (f reçoit un int et renvoie un int.)
    Testez-la avec lambda n: n + 3 et la valeur 10.

12. Cette fonction n'accepte (pour mypy) que des listes :
        def moyenne(valeurs: list[float]) -> float:
            return sum(valeurs) / len(valeurs)
    Peut-on l'annoter avec Iterable[float] ? Pourquoi ? Quel type plus
    général convient ?

13. Écrivez une fonction annotée compter_positifs(valeurs) qui accepte
    n'importe quel itérable de nombres (liste, tuple, générateur…) et
    renvoie le nombre de valeurs strictement positives. Testez-la avec une
    liste, un tuple et un générateur.
"""


#############################################
#  Alias, TypedDict, Literal, Final         #
#############################################

"""
14. Créez un alias Matrice pour "liste de listes de floats", puis une
    fonction annotée transposer(m: Matrice) -> Matrice.
        transposer([[1.0, 2.0], [3.0, 4.0]])  => [[1.0, 3.0], [2.0, 4.0]]

15. Créez un TypedDict Livre avec les clés titre (str), auteur (str),
    annee (int) et notes (list[int]). Écrivez une fonction annotée
    note_moyenne(livre: Livre) -> float, et testez-la.

16. Écrivez une fonction annotée arrondir(valeur, mode) où mode ne peut
    valoir que "haut", "bas" ou "proche" (utilisez Literal). Elle renvoie
    math.ceil, math.floor ou round de la valeur.
"""


##############################################
#  Classes, dataclasses et génériques       #
##############################################

"""
17. Annotez complètement cette classe :
        class Thermometre:
            def __init__(self, lieu, valeurs=None):
                self.lieu = lieu
                self.valeurs = valeurs if valeurs is not None else []

            def ajouter(self, v):
                self.valeurs.append(v)

            def maximum(self):
                return max(self.valeurs) if self.valeurs else None

18. Transformez cette classe en dataclass annotée :
        class Point:
            def __init__(self, x, y, nom="?"):
                self.x = x
                self.y = y
                self.nom = nom
    Vérifiez avec print() que le __repr__ est généré automatiquement.

19. Écrivez une fonction générique dernier(elements) qui renvoie le dernier
    élément d'une séquence, annotée avec un TypeVar.

20. Écrivez une fonction générique filtrer(elements, condition) annotée
    avec un TypeVar : elle reçoit un itérable de T et une fonction T -> bool,
    et renvoie la liste des éléments qui vérifient la condition.
        filtrer([1, 5, 8, 3], lambda n: n > 4)  => [5, 8]
"""


##############################
#  Vérifier avec mypy        #
##############################

"""
21. Sans exécuter mypy : quelles erreurs signalerait-il dans ce code ?
        def taux(reussis: int, total: int) -> float:
            return reussis / total

        def mention(note: float) -> str:
            if note >= 16:
                return "très bien"
            elif note >= 12:
                return "bien"

        resultat: int = taux(3, 4)
        print(taux("3", 4))

22. (Si mypy est installé) Écrivez le code de l'exercice 21 dans un fichier
    temporaire et vérifiez vos réponses avec mypy, comme dans le chapitre.
"""
