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
#  Chap. 27     #  Types construits III : les dictionnaires (II)               #
#               #                                                              #
################################################################################
#
#  - Créer des dictionnaires
#  - D'autres méthodes sur les dictionnaires
#  - Les méthodes .keys(), .values() et .items()
#
##################################################

# Créer des dictionnaires
##########################
# todo: dict()


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
