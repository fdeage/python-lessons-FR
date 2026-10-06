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
#  Chap. 18     #  Types construits III : les dictionnaires (I)                #
#               #                                                              #
################################################################################
#
#  - Définition et utilité du dictionnaire
#  - Dictionnaire vs liste
#  - Cas d'usage
#  - Indexation de valeurs et opérations de base
#  - Ajouter, modifier et supprimer des valeurs
#  - Tester la présence d'une clé
#  - Parcourir un dictionnaire
#  - En bref
#
##################################################

# Définition et utilité du dictionnaire
########################################

"""
Un dictionnaire est une structure de données qui ASSOCIE DES CHOSES À
D'AUTRES CHOSES.

Les choses que l'on cherche sont appelées des CLÉS, et les choses associées
sont les VALEURS. Un dictionnaire est donc une valeur de type construit
contenant des "couples CLÉ-VALEUR".

IMPT : chaque clé est toujours unique au sein d'un même dictionnaire : on est
sûr qu'à chaque clé ne peut correspondre qu'UNE SEULE VALEUR.

Pourquoi ce mot "dictionnaire" ?

Dans un dictionnaire papier, la clé est le mot cherché, et la valeur
est la ou les définitions données par le dictionnaire. L'annuaire est un très
bon exemple de dictionnaire : chaque clé (une personne) est associée à un
numéro de téléphone.

Dans d'autres langages, on appellera aussi parfois le dictionnaire un "hash",
une "map", une "lookup table" (table d'indexation), un "associative array"
(tableau associatif)…
"""


# Dictionnaire vs liste
########################

"""
Python a, au fond, deux structures de données fondamentales :
    1. la liste,
    2. le dictionnaire.

Ce sont deux types construits, c'est-à-dire qu'ils servent à stocker plusieurs
éléments.
La plupart des autres structures Python en découlent ou en sont des variantes.

À quoi servent ces deux structures ?
    1. La liste sert à stocker UNE QUANTITÉ VARIABLE, ORDONNÉE, D'ÉLÉMENTS
       SOUVENT SIMILAIRES.
       Ex. : voitures = [voiture5, voiture23, voiture4]

       => les éléments sont similaires, et l'ordre des voitures compte. Les
       éléments peuvent être identiques. L'association de chaque élément se fait
       simplement à son ordre dans la liste (son index)

    2. Le dictionnaire sert à stocker UNE QUANTITÉ FIXE D'ÉLÉMENTS DISTINCTS ET
       CONNUS À L'AVANCE, POUR LESQUELS L'ORDRE N'IMPORTE PAS.
       Ex. : voiture23 = {"modele": "Renault R5", "année": 1987, "couleur":
       "rouge"}

       => les éléments sont différents, et l'ordre n'a pas d'importance (année
       n'arrive pas "avant" couleur). Il y a une seule année et une seule
       couleur par voiture.

Rappel :
| structure                      | liste      | dictionnaire        |
| ------------------------------ | ---------- | ------------------- |
| nombre de valeurs              | variable   | fixe (en général)   |
| doublons possibles             | oui        | non (pour les clés) |
| l'ordre des valeurs compte     | oui        | non                 |
| valeurs similaires entre elles | en général | rarement            |

Note sur l'ordre : depuis Python 3.7, un dictionnaire se "souvient" de l'ordre
dans lequel on a ajouté les clés (quand on l'affiche ou qu'on le parcourt, les
clés apparaissent dans cet ordre). Mais cet ordre n'a pas de SENS : on n'accède
jamais à une valeur par sa position, seulement par sa clé. Deux dictionnaires
qui contiennent les mêmes couples dans un ordre différent sont donc égaux :
"""
print({"a": 1, "b": 2} == {"b": 2, "a": 1})  # => True


# Cas d'usage
##############

"""
On a vu qu'on utilisait en général la liste pour stocker un nombre indéfini
d'éléments de même nature, et le dictionnaire pour un nombre connu d'éléments
différents.

Exemple :
    - On a ici un nombre inconnu au départ de joueurs (éléments de même
      nature) : on utilise une liste
    - Chaque joueur a une structure connue et sans doublon : un dictionnaire
"""
joueurs = []
for i in range(3):
    nouveau_joueur = {"numéro": i, "nom": "", "score": 0, "vie": 100}
    joueurs.append(nouveau_joueur)

print(len(joueurs))  # => 3 (une liste de 3 dictionnaires)
print(joueurs[1])    # => {'numéro': 1, 'nom': '', 'score': 0, 'vie': 100}

"""
D'autres exemples typiques de dictionnaires :
    - un annuaire : {"Alice": "06 12 34 56 78", "Bob": "07 98 76 54 32"}
    - une traduction : {"chat": "cat", "chien": "dog"}
    - une fiche (une "ligne" de données) : {"nom": "Dupont", "âge": 37}
    - un compteur : {"a": 3, "b": 1} (combien de fois chaque lettre apparaît)
    - une configuration : {"langue": "fr", "plein_ecran": True}

En Data Science, on manipulera très souvent des LISTES DE DICTIONNAIRES : chaque
dictionnaire est une ligne d'un tableau, et chaque clé le nom d'une colonne.
"""


# Indexation de valeurs et opérations de base
##############################################

# En Python, on utilise la syntaxe {clé1: valeur1, …} pour déclarer un
# dictionnaire :
mon_super_dictionnaire = {"hop": 14, "pouet": True, "tut": "pouet"}
print(mon_super_dictionnaire)  # => {'hop': 14, 'pouet': True, 'tut': 'pouet'}
print(type(mon_super_dictionnaire))  # => <class 'dict'>

# Un dictionnaire vide se déclare avec deux accolades
dict_vide = {}
print(len(dict_vide))  # => 0

# len() donne le nombre de couples clé-valeur
print(len(mon_super_dictionnaire))  # => 3

# On accède ensuite à la valeur souhaitée avec la syntaxe "[]", en donnant la
# CLÉ entre les crochets
print(mon_super_dictionnaire["hop"])  # => 14
print(mon_super_dictionnaire["tut"])  # => pouet

# IMPT : la méthode des listes pour accéder à une valeur ne fonctionne pas :
try:
    mon_super_dictionnaire[0]  # => KeyError: 0, car 0 n'est pas une clé
except KeyError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# Un dictionnaire ressemble finalement beaucoup à une liste : une liste
# associe un indice à une valeur…
l = ["a", "b", "c"]
l[0] = "a"
l[1] = "b"
l[2] = "c"

# …mais on peut en faire autant avec un dictionnaire :
d = {0: "a", 1: "b", 2: "c"}
d[0] = "a"
d[1] = "b"
d[2] = "c"

"""
Il y a deux différences fondamentales dans leur indexation :
    1. la liste nomme forcément ses clés avec des entiers croissants (elle
       les "indexe" en ordre croissant), alors que le dictionnaire peut
       avoir comme clé (presque) n'importe quoi
"""

# Exemple :
cles_variees = {1: "test", 3.4: "pouet", "abc": False, (2, 3): [1, 2]}
print(cles_variees[3.4])     # => pouet
print(cles_variees[(2, 3)])  # => [1, 2] (un tuple comme clé, cf. chap. 17)

# Attention : True et 1 sont considérés comme la MÊME clé, car True == 1
# (cf. chap. 21) ! La 2e association écrase la première :
piege = {1: "un", True: "vrai"}
print(piege)  # => {1: 'vrai'}
"""
    2. la liste peut contenir plusieurs fois le même élément, alors que
       chaque clé d'un dictionnaire doit être unique
"""

# Une liste peut contenir des doublons
lancers_de = [2, 3, 4, 5, 2]

# …alors que si on répète une clé dans un dictionnaire, seule la DERNIÈRE
# association est conservée : elle écrase les précédentes
notes = {"maths": 12, "maths": 15}
print(notes)  # => {'maths': 15}

# En revanche, des clés DIFFÉRENTES peuvent être associées à la même valeur
# sans aucun problème : ce sont les clés qui doivent être uniques, pas les
# valeurs
memes_valeurs = {"lundi": "cours", "mardi": "cours", "mercredi": "repos"}
print(len(memes_valeurs))  # => 3

"""
Note sur les clés des dictionnaires :
Ces clés doivent être de types immuables ("hashable"). Ces types sont :
int, float, string, booléen, None, tuple (à condition que le tuple ne contienne
lui-même que des valeurs immuables).

Pourquoi ? Pour retrouver très vite une valeur, Python calcule à partir de la
clé un nombre, son "hash" (fonction intégrée hash()), qui lui indique où
ranger la valeur en mémoire. Si la clé pouvait changer, son hash changerait, et
Python ne retrouverait plus la valeur !

Ceci exclut : les listes, les dictionnaires et les ensembles (voir chap. 25)
"""

try:
    # => TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
    dict_avec_mauvaise_cle = {[1, 2]: 2}
    # (le texte exact du message dépend de votre version de Python)
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# En revanche, les VALEURS peuvent être absolument tout ce que l'on veut,
# sans restriction
valeurs_variees = {0: [1, 2, 3], 1: {1: "pouet"}, 2: (1, 2, 3)}
print(valeurs_variees[0])     # => [1, 2, 3]
print(valeurs_variees[1][1])  # => pouet (on "enchaîne" les crochets)
# (On détaillera ces dictionnaires "imbriqués" au chap. 27.)

"""
IMPT : la recherche d'une clé dans un dictionnaire est quasi instantanée, même
s'il contient des millions de clés (grâce au hash). Chercher une valeur dans une
liste, au contraire, oblige Python à la parcourir élément par élément.
"""


# Ajouter, modifier et supprimer des valeurs
#############################################

# On ajoute un nouveau couple clé-valeur en affectant une valeur à une clé qui
# n'existe pas encore…
inventaire = {"pommes": 3, "poires": 5}
inventaire["kiwis"] = 12
print(inventaire)  # => {'pommes': 3, 'poires': 5, 'kiwis': 12}

# …et on modifie une valeur avec exactement la même syntaxe, si la clé existe
# déjà : l'ancienne valeur est remplacée
inventaire["pommes"] = 10
print(inventaire)  # => {'pommes': 10, 'poires': 5, 'kiwis': 12}

# On peut bien sûr utiliser l'ancienne valeur pour calculer la nouvelle
inventaire["poires"] = inventaire["poires"] + 1
inventaire["poires"] += 1  # (même chose en plus court)
print(inventaire["poires"])  # => 7

"""
Attention : on ne peut lire une clé que si elle existe. Ici "bananes" n'est pas
une clé, donc on ne peut pas lui ajouter 1 :
"""
try:
    inventaire["bananes"] += 1  # => KeyError: 'bananes'
except KeyError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# On supprime un couple clé-valeur avec le mot-clé "del" (comme pour les
# listes, cf. chap. 16)
del inventaire["kiwis"]
print(inventaire)  # => {'pommes': 10, 'poires': 7}

# Supprimer une clé inexistante crée aussi une erreur
try:
    del inventaire["kiwis"]  # => KeyError: 'kiwis' (on vient de la supprimer)
except KeyError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# Note : on verra au chap. 27 d'autres méthodes utiles : .get(), .update(),
# .pop(), .keys(), .values(), .items()…


# Tester la présence d'une clé
###############################

"""
Pour éviter les KeyError, on vérifie qu'une clé existe avec "… in …" (et son
complément "… not in …"), comme pour les listes. Attention : "in" cherche
parmi les CLÉS, pas parmi les valeurs !
"""
print("pommes" in inventaire)   # => True
print("kiwis" in inventaire)    # => False
print(10 in inventaire)         # => False : 10 est une valeur, pas une clé
print("kiwis" not in inventaire)  # => True

# Exemple classique : compter les lettres d'un mot
compteur = {}
for lettre in "abracadabra":
    if lettre in compteur:
        compteur[lettre] += 1  # la lettre a déjà été vue : on ajoute 1
    else:
        compteur[lettre] = 1   # 1re apparition : on crée la clé
print(compteur)  # => {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}


# Parcourir un dictionnaire
############################

"""
Une boucle for sur un dictionnaire parcourt ses CLÉS (cf. chap. 13). On peut
ensuite récupérer chaque valeur avec les crochets.
"""
capitales = {"France": "Paris", "Italie": "Rome", "Japon": "Tokyo"}
for pays in capitales:
    print(f"{pays} : capitale {capitales[pays]}")
# => France : capitale Paris
# => Italie : capitale Rome
# => Japon : capitale Tokyo

# Note : on verra au chap. 27 la méthode .items(), qui permet de récupérer
# directement la clé ET la valeur à chaque tour de boucle, ainsi que les
# autres façons de parcourir un dictionnaire (et le piège qui consiste à le
# modifier pendant le parcours).


# En bref
##########

"""
| opération                        | syntaxe                    |
| -------------------------------- | -------------------------- |
| déclarer                         | d = {"a": 1, "b": 2}       |
| dictionnaire vide                | d = {}                     |
| lire une valeur                  | d["a"]                     |
| ajouter ou modifier              | d["c"] = 3                 |
| supprimer                        | del d["a"]                 |
| tester une clé                   | "a" in d                   |
| nombre de couples                | len(d)                     |
| parcourir les clés               | for cle in d: …            |

IMPT : les clés sont uniques et immuables ; les valeurs peuvent être
n'importe quoi.
"""
