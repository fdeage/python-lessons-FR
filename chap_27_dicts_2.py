################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2024                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 27     #  Types construits III : les dictionnaires (II)               #
#               #                                                              #
################################################################################
#
#  - Créer des dictionnaires
#  - D'autres méthodes sur les dictionnaires
#  - Les méthodes .keys(), .values() et .items()
#  - Exemple : compter des occurrences
#  - Dictionnaires imbriqués
#  - Dictionnaires et paramètres de fonctions
#
##################################################

# Créer des dictionnaires
##########################

"""
On a vu au chap. 18 la syntaxe de base {clé1: valeur1, clé2: valeur2, …}.
Il existe plusieurs autres façons de créer un dictionnaire.
"""

#   1. La syntaxe "littérale" avec les accolades, déjà vue :
capitales = {"France": "Paris", "Italie": "Rome"}
print(capitales)  # => {'France': 'Paris', 'Italie': 'Rome'}

#   2. La fonction intégrée dict() sans argument crée un dictionnaire vide
#      (équivalent à {})
print(dict())  # => {}

#   3. dict() avec des arguments "nommés" (nom=valeur) : chaque nom devient une
#      clé (de type string). C'est très lisible, mais cela ne fonctionne que si
#      les clés sont des noms de variables valides (pas d'espace, pas de
#      chiffre au début, cf. chap. 10).
voiture = dict(modele="R5", annee=1987, couleur="rouge")
print(voiture)  # => {'modele': 'R5', 'annee': 1987, 'couleur': 'rouge'}

#   4. dict() avec une liste de couples (clé, valeur), sous forme de tuples
#      (cf. chap. 17)
couples = [("un", 1), ("deux", 2), ("trois", 3)]
print(dict(couples))  # => {'un': 1, 'deux': 2, 'trois': 3}

#   5. dict() avec zip(), pour associer deux listes élément par élément
#      (cf. chap. 24)
pays = ["Espagne", "Portugal"]
villes = ["Madrid", "Lisbonne"]
print(dict(zip(pays, villes)))  # => {'Espagne': 'Madrid', 'Portugal': 'Lisbonne'}

#   6. La méthode dict.fromkeys() crée un dictionnaire dont toutes les clés ont
#      la même valeur de départ (pratique pour initialiser des compteurs)
print(dict.fromkeys(["a", "b", "c"], 0))  # => {'a': 0, 'b': 0, 'c': 0}

#   7. Une compréhension de dictionnaire (cf. chap. 23)
print({n: n ** 2 for n in range(4)})  # => {0: 0, 1: 1, 2: 4, 3: 9}

#   8. Enfin, dict() appliqué à un dictionnaire en crée une copie (voir
#      .copy() plus bas)
copie_capitales = dict(capitales)
print(copie_capitales == capitales)  # => True


# D'autres méthodes sur les dictionnaires
##########################################

# On peut créer un dictionnaire vide avec {}…
dict_vide = {}

# …puis le remplir avec des couples clé/valeur
dict_vide["zéro"] = 0
print(dict_vide)  # => {'zéro': 0}

# Tenter d'accéder à une clé non-existante crée une erreur
try:
    dict_vide["?"]  # => KeyError: '?'
except KeyError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# Note : on peut utiliser .get() pour éviter cette erreur
print(dict_vide.get("?"))      # => None
# .get() peut prendre une valeur par défaut
value = dict_vide.get("?", 0)
print(value)                   # => 0
# Si la clé existe, .get() retourne simplement la valeur associée
print(dict_vide.get("zéro", 42))  # => 0

"""
IMPT : .get() est très utile quand une valeur peut être absente, par
exemple pour des paramètres optionnels : on fournit une valeur par défaut
plutôt que de crasher (voir la dernière section du chapitre).

Attention : .get() n'ajoute PAS la clé au dictionnaire.
"""
print(dict_vide)  # => {'zéro': 0}

# On peut aussi remplir le dictionnaire avec ".update()" en lui passant un
# dictionnaire
dict_vide.update({"un": 1})
print(dict_vide)  # => {'zéro': 0, 'un': 1}

# .update() peut ajouter OU remplacer un couple clé/valeur :
dict_vide.update({"un": 3})
print(dict_vide)  # => {'zéro': 0, 'un': 3}, on remplace l'ancienne valeur associée
dict_vide.update({"deux": 2})
print(dict_vide)  # => {'zéro': 0, 'un': 3, 'deux': 2}

"""
IMPT : on rappelle que chaque clé doit être unique au sein d'un même
dictionnaire. S'il y a un doublon de clé, la valeur retenue sera celle de la
dernière association
"""
dict_avec_doublons = {"un": 1, "deux": 2, "deux": 42, "trois": 3}
print(dict_avec_doublons["deux"])  # => 42 (vient après 2 dans la déclaration)

# En revanche, des clés différentes peuvent être associées à la même valeur
# sans problème
dict_avec_memes_valeurs = {0: "Pouet", 1: "Pouet", 2: "Pouet"}

# L'accès à une clé non-existante lève une KeyError
try:
    dict_avec_doublons["quatre"]  # KeyError
except KeyError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# On vérifie la présence d'une clé dans un dictionnaire avec "in"
print("un" in dict_avec_doublons)  # => True
print(1 in dict_avec_doublons)     # => False ("in" teste les clés, pas les valeurs)

# len() donne le nombre de couples clé/valeur
print(len(dict_avec_doublons))  # => 3

# On peut enlever des clés d'un dictionnaire avec del
del dict_avec_doublons["un"]  # Supprime la clé "un"
print(dict_avec_doublons)  # => {'deux': 42, 'trois': 3}

# … ou avec .pop(), qui supprime la clé ET retourne la valeur associée
stock = {"pommes": 3, "poires": 5, "kiwis": 0}
nb_kiwis = stock.pop("kiwis")
print(nb_kiwis)  # => 0
print(stock)     # => {'pommes': 3, 'poires': 5}

# Comme pour [], .pop() d'une clé absente crée une KeyError… sauf si on donne
# une valeur par défaut
try:
    stock.pop("mangues")
except KeyError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
print(stock.pop("mangues", 0))  # => 0

# .setdefault() retourne la valeur d'une clé si elle existe ; sinon, il AJOUTE
# la clé avec la valeur par défaut, et retourne celle-ci
print(stock.setdefault("pommes", 100))  # => 3 (la clé existe, rien ne change)
print(stock.setdefault("cerises", 10))  # => 10 (la clé est ajoutée)
print(stock)  # => {'pommes': 3, 'poires': 5, 'cerises': 10}

# .copy() crée une copie (superficielle, cf. chap. 24) du dictionnaire. Comme
# pour les listes, "=" ne copie PAS : il donne un second nom au même objet.
alias = stock
copie = stock.copy()
stock["pommes"] = 0
print(alias["pommes"])  # => 0 (alias et stock sont le même dictionnaire)
print(copie["pommes"])  # => 3 (la copie est indépendante)

# .clear() vide le dictionnaire
copie.clear()
print(copie)  # => {}

# On peut fusionner deux dictionnaires avec l'opérateur "|" (Python 3.9+) :
# en cas de clé commune, c'est la valeur de DROITE qui l'emporte.
defaut = {"couleur": "noir", "taille": 12}
choix = {"taille": 14}
print(defaut | choix)  # => {'couleur': 'noir', 'taille': 14}
# Avant Python 3.9, on écrira {**defaut, **choix} (voir la dernière section)
print({**defaut, **choix})  # => {'couleur': 'noir', 'taille': 14}


# Les méthodes .keys(), .values() et .items()
##############################################

# Ces trois méthodes de dictionnaire sont à bien connaître.

print(dict_avec_doublons)  # => {'deux': 42, 'trois': 3}

#   1. On obtient toutes les clés d'un dictionnaire avec la méthode .keys().
print(dict_avec_doublons.keys())  # => dict_keys(['deux', 'trois'])

# Attention, il faut passer ces clés à list() pour avoir une liste.
print(list(dict_avec_doublons.keys()))  # => ['deux', 'trois']

"""
Note sur l'ordre : depuis Python 3.7, un dictionnaire CONSERVE L'ORDRE
D'INSERTION des clés (c'était déjà le cas en pratique en 3.6). Les clés
sortent donc dans l'ordre où elles ont été ajoutées. Mais attention, cet ordre
n'a pas de "sens" : on ne peut pas accéder à un élément par sa position
(dict_avec_doublons[0] cherche la CLÉ 0), et deux dictionnaires avec les mêmes
couples dans un ordre différent sont égaux.
"""
print({"a": 1, "b": 2} == {"b": 2, "a": 1})  # => True

#   2. On obtient toutes les valeurs d'un dict avec ".values()".
print(dict_avec_doublons.values())  # => dict_values([42, 3])

# Là aussi, il faut ensuite le passer à list() pour avoir une liste.
print(list(dict_avec_doublons.values()))  # => [42, 3]

# On peut appliquer directement sum(), max(), etc. sur les valeurs
print(sum(dict_avec_doublons.values()))  # => 45

# Pour savoir si une VALEUR est présente, on utilise "in" sur .values()
print(42 in dict_avec_doublons.values())  # => True

#   3. Enfin, pour itérer sur toutes les paires clé/valeur, on utilise .items()
calories = {"pomme": 52, "banane": 89, "chocolat": 546}
print(calories.items())
# => dict_items([('pomme', 52), ('banane', 89), ('chocolat', 546)])

for k, v in calories.items():
    print(k) if v > 500 else None  # => chocolat

"""
Remarques : on utilise deux variables dans la boucle for : k sert pour les
clés du dictionnaire ("keys"), et v pour les valeurs (values).

Comment ça marche ? .items() fournit, à chaque tour de boucle, un tuple
(clé, valeur), que Python "déballe" dans les deux variables k et v (comme pour
enumerate(), cf. chap. 24). On choisira de préférence des noms de variables
parlants :
"""
for aliment, kcal in calories.items():
    if kcal > 500:
        print(f"Attention, {aliment} : {kcal} kcal pour 100 g !")
# => Attention, chocolat : 546 kcal pour 100 g !

"""
(La première version, avec le "if … else …" sur une ligne (cf. chap. 12), est
plus courte mais moins lisible : préférez la seconde.)

Les trois façons de parcourir un dictionnaire :
"""
for aliment in calories:             # sur les clés (équivaut à .keys())
    print(aliment, end=" ")
print()                              # => pomme banane chocolat
for kcal in calories.values():       # sur les valeurs
    print(kcal, end=" ")
print()                              # => 52 89 546
for aliment, kcal in calories.items():  # sur les couples
    print(f"{aliment}={kcal}", end=" ")
print()                              # => pomme=52 banane=89 chocolat=546

# Pour parcourir les clés dans l'ordre alphabétique, on utilise sorted()
for aliment in sorted(calories):
    print(aliment, end=" ")
print()  # => banane chocolat pomme

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

"""
Attention : on ne peut pas ajouter ou supprimer des clés PENDANT qu'on
parcourt un dictionnaire. On parcourt alors une copie des clés, obtenue avec
list() :
"""
try:
    for aliment in calories:
        if calories[aliment] > 500:
            del calories[aliment]
except RuntimeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# (Notez que "chocolat" a quand même été supprimé avant que l'erreur ne
# survienne, au tour de boucle suivant : le dictionnaire est dans un état
# "à moitié modifié", ce qui est justement le danger.)

for aliment in list(calories):  # list() crée une copie figée des clés
    if calories[aliment] > 500:
        del calories[aliment]
print(calories)  # => {'pomme': 52, 'banane': 89}


# Exemple : compter des occurrences
####################################

"""
Un usage très fréquent des dictionnaires : compter combien de fois apparaît
chaque élément (des mots dans un texte, des catégories dans des données…).
Les éléments sont les clés, et les compteurs les valeurs.
"""
texte = "le chat et le chien et le poisson"

# Version 1 : avec un test "in"
compteur = {}
for mot in texte.split():
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1
print(compteur)
# => {'le': 3, 'chat': 1, 'et': 2, 'chien': 1, 'poisson': 1}

# Version 2 : plus courte, avec .get() et une valeur par défaut de 0
compteur = {}
for mot in texte.split():
    compteur[mot] = compteur.get(mot, 0) + 1
print(compteur)
# => {'le': 3, 'chat': 1, 'et': 2, 'chien': 1, 'poisson': 1}

# Pour trouver le mot le plus fréquent, on passe la méthode .get au paramètre
# key de max() (cf. chap. 24) : max() compare alors les VALEURS associées.
print(max(compteur, key=compteur.get))  # => le

"""
Note : le module collections (cf. chap. 22) propose un type Counter qui fait
tout ce travail automatiquement : collections.Counter(texte.split()).
"""


# Dictionnaires imbriqués
##########################

"""
Les valeurs d'un dictionnaire peuvent être n'importe quoi, y compris des
listes ou d'autres dictionnaires (cf. chap. 18). C'est ainsi qu'on représente
des données structurées (c'est d'ailleurs très proche du format JSON, très
utilisé sur le Web).
"""
eleves = {
    "ana": {"age": 17, "notes": [12, 15, 18]},
    "bob": {"age": 16, "notes": [9, 11]},
}

# On enchaîne les crochets, de gauche à droite :
print(eleves["ana"]["age"])       # => 17
print(eleves["bob"]["notes"][0])  # => 9

# On modifie une valeur imbriquée de la même façon
eleves["bob"]["notes"].append(14)
print(eleves["bob"])  # => {'age': 16, 'notes': [9, 11, 14]}

# Parcours : le nom de chaque élève, avec sa moyenne
for nom, infos in eleves.items():
    moyenne = sum(infos["notes"]) / len(infos["notes"])
    print(f"{nom} : {moyenne:.2f}")
"""
ana : 15.00
bob : 11.33

(":.2f" dans l'interpolation affiche le nombre avec 2 décimales.)
"""


# Dictionnaires et paramètres de fonctions
###########################################

"""
1. Un dictionnaire d'options

Quand une fonction a beaucoup de réglages, on peut les regrouper dans un
dictionnaire, et utiliser .get() pour fournir une valeur par défaut à chaque
réglage absent.
"""
def afficher_titre(texte, options):
    symbole = options.get("symbole", "*")
    largeur = options.get("largeur", 20)
    print(symbole * largeur)
    print(texte.center(largeur))  # .center() centre le texte sur la largeur
    print(symbole * largeur)


afficher_titre("Bonjour", {})                 # tous les réglages par défaut
afficher_titre("Salut", {"symbole": "="})     # on ne change que le symbole
"""
********************
      Bonjour
********************
====================
       Salut
====================
"""

"""
2. Déballer un dictionnaire dans les paramètres avec "**"

Pour rappel, lors d'un appel de fonction, on peut nommer les arguments :
f(a=1, b=2). Avec "**", Python transforme chaque couple clé/valeur d'un
dictionnaire en argument nommé.
"""
def presenter(nom, age):
    print(f"{nom} a {age} ans")


presenter(nom="Ada", age=36)            # => Ada a 36 ans (arguments nommés)
personne = {"nom": "Alan", "age": 41}
presenter(**personne)                   # => Alan a 41 ans
# … équivaut à presenter(nom="Alan", age=41)

"""
3. Recevoir des arguments nommés en nombre quelconque avec "**kwargs"

À l'inverse, dans la DÉFINITION d'une fonction, un paramètre précédé de "**"
récupère tous les arguments nommés sous forme de dictionnaire. Par
convention, on l'appelle "kwargs" ("keyword arguments"). Son pendant pour les
arguments positionnels, "*args", est vu au chap. 32.
"""
def fiche(**kwargs):
    print(type(kwargs))  # c'est un simple dictionnaire
    for cle, valeur in kwargs.items():
        print(f"  {cle} : {valeur}")


fiche(modele="R5", annee=1987)
"""
<class 'dict'>
  modele : R5
  annee : 1987
"""

"""
Ce mécanisme est très utilisé par les bibliothèques de Data Science (pandas,
matplotlib…), dont les fonctions acceptent souvent des dizaines de réglages
optionnels.
"""
