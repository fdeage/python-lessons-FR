################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2023                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 18     #  Types construits III : les dictionnaires                    #
#               #                                                              #
################################################################################
#
#  - Définition et utilité du dictionnaire
#  - Dictionnaire vs liste
#  - Cas d'usage
#  - Indexation de valeurs et opérations de base
#  - D'autres méthodes sur les dictionnaires
#  - Les méthodes .keys(), .values() et .items()
#
##################################################

# todo: dict()

# Définition et utilité du dictionnaire
########################################

"""
Un dictionnaire est une structure de données qui ASSOCIE DES CHOSES À
D'AUTRES CHOSES.

Les choses que l'on cherche sont appelées des CLÉS, et les choses associées
sont les VALEURS. Un dictionnaire est donc une variable de type construit
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


# Cas d'usage
##############

"""
On a vu qu'on utilisait en général la liste pour stocker un nombre indéfini
d'éléments identiques, et le dictionnaire pour un nombre connu d'éléments
différents.

Exemple :
    - On a ici un nombre inconnu au départ de joueurs (éléments
      identiques entre eux) : on utilise une liste
    - Chaque joueur a une structure connue et sans doublon : un dictionnaire
"""
joueurs = []
for i in range(3):
    nouveau_joueur = {"numéro": i, "nom": "", "score": 0, "vie": 100}
    joueurs.append(nouveau_joueur)


# Dictionnaire vs liste
########################

"""
Python a, au fond, deux structures de données fondamentales :
    1. la liste,
    2. le dictionnaire.

Ce sont deux types construits, càd qu'ils servent à stocker plusieurs éléments.
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

"""


# Indexation de valeurs et opérations de base
##############################################

# En Python, on utilise la syntaxe {clé1: valeur1, …} pour déclarer un
# dictionnaire :
mon_super_dictionnaire = {"hop": 14, "pouet": True, "tut": "pouet"}

# On accède ensuite à la valeur souhaitée avec la syntaxe "[]"
mon_super_dictionnaire["hop"]  # => 14

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
Ils y a deux différences fondamentales dans leur indexation :
    1. la liste nomme forcément ses clés avec des entiers croissants (elle
       les "indexe" en ordre croissant), alors que le dictionnaire peut
       avoir comme clé (presque) n'importe quoi
"""

# Exemple :
cles_variees = {1: "test", 3.4: "pouet", True: False, (2, 3): [1, 2]}
"""
    2. la liste peut contenir plusieurs fois le même élément, alors que
       chaque clé d'un dictionnaire doit être unique
"""

# Une liste peut contenir des doublons
lancers_de = [2, 3, 4, 5, 2]

"""
Note sur les clés des dictionnaires :
Ces clés doivent être de types immuables ("hashable"). Ces types sont :
int, float, string, booléen, tuple.

Ceci exclut : les listes, les dictionnaires et les ensembles (voir chap. 22)
"""

try:
    dict_avec_mauvaise_cle = {[1, 2]: 2}  # => TypeError: unhashable type: 'list'
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# En revanche, les VALEURS peuvent être absolument tout ce que l'on veut,
# sans restriction
valeurs_variees = {0: [1, 2, 3], 1: {1: "pouet"}, 2: {1, 2, 3}}


# D'autres méthodes sur les dictionnaires
##########################################

# On peut créer un dictionnaire vide avec {}…
dict_vide = {}

# …puis le remplir avec des couples clé/valeur
dict_vide["zéro"] = 0
dict_vide  # => {"zéro": 0}

# Tenter d'accéder à une clé non-existente crée une erreur
try:
    dict_vide["?"]  # => KeyError: '?'
except KeyError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# Note : on peut utiliser .get() pour éviter cette erreur
dict_vide.get("?")             # => None
# .get() peut prendre une valeur par défaut
value = dict_vide.get("?", 0)  # => 0

# TODO : utilie pour paramètres

# On peut aussi remplir le dictionnaire avec ".update()"" en lui passant un
# dictionnaire
dict_vide.update({"un": 1})
dict_vide  # => {"un": 1}

# .update() peut ajouter OU remplacer un couple clé/valeur :
dict_vide.update({"un": 3})
dict_vide  # => {"un": 3}, on remplace l'ancienne valeur associée
dict_vide.update({"deux": 2})
dict_vide  # => {"un": 3, "deux": 2}

"""
IMPT : on rappelle que chaque clé doit être unique au sein d'un même
dictionnaire. S'il y a un doublon de clé, la valeur retenue sera celle de la
dernière association
"""
dict_avec_doublons = {"un": 1, "deux": 2, "deux": 42, "trois": 3}
dict_avec_doublons["deux"]  # => 42 (vient après 2 dans la déclaration)

# En revanche, des clés différentes peuvent être associées à la même valeur
# sans problème
dict_avec_memes_valeurs = {0: "Pouet", 1: "Pouet", 2: "Pouet"}

# L'accès à une clé non-existente lève une KeyError
try:
    dict_avec_doublons["quatre"]  # KeyError
except KeyError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# On vérifie la présence d'une clé dans un dictionnaire avec "in"
"un" in dict_avec_doublons  # => True
1 in dict_avec_doublons  # => False

# On peut enlever des clés d'un dictionnaire avec del
del dict_avec_doublons["un"]  # Supprime la clé "un"
dict_avec_doublons  # => {"deux": 42, "trois": 3}


# Les méthodes .keys(), .values() et .items()
##############################################

# Ces trois méthodes de dictionnaire sont à bien connaître.

print(dict_avec_doublons)  # => {'deux': 42, 'trois': 3}

#   1. On obtient toutes les clés d'un dictionnnaire avec la méthode .keys().
print(dict_avec_doublons.keys())  # => dict_keys(['deux', 'trois'])

# Attention, il faut passer ces clés à list() pour avoir une liste.
print(list(dict_avec_doublons.keys()))  # => ["trois", "deux"]

# Note: l'ordre des clés n'est pas garanti.


#   2. On obtient toutes les valeurs d'un dict avec ".values()".
dict_avec_doublons.values()  # => dict_values([42, 3])

# Là aussi, il faut ensuite le passer à list() pour avoir une liste.
list(dict_avec_doublons.values())  # => [42, 3]

# Note : l'ordre des valeurs n'est pas garanti non plus.


#   3. Enfin, pour itérer sur toutes les paires clé/valeur, on utilise .items()
calories = {"pomme": 52, "banane": 89, "chocolat": 546}

for k, v in calories.items():
    print(k) if v > 500 else None  # =>'chocolat'

"""
Remarques : on utilise deux variables dans la boucle for : k sert pour les
clés du dictionnaire ("keys"), et v pour les valeurs (values).
TODO
"""

"""
Note : ces trois méthodes proposent une vue "dynamique" des dictionnaires.
Ces vues vont évoluer en même temps que le dictionnaire dont elles sont
issues !
"""
k = calories.keys()
v = calories.values()
print(k)  # => dict_keys(['pomme', 'banane', 'chocolat'])
print(v)  # => dict_values([52, 89, 546])

# On modifie ensuite notre dictionnaire…
calories["burger"] = 1_000

# …et k et v sont modifiés dynamiquement
print(k)  # => dict_keys(['pomme', 'banane', 'chocolat', 'burger'])
print(v)  # => dict_values([52, 89, 546, 1000])
