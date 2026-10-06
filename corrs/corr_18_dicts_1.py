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
#  Chap. 18     #  Dictionnaires I : corrigés                                  #
#               #                                                              #
################################################################################

###########################################
#  Définition et utilité du dictionnaire  #
###########################################

# 1. Une fiche :
fiche = {"prenom": "Ada", "nom": "Lovelace", "age": 36}
print(fiche)  # => {'prenom': 'Ada', 'nom': 'Lovelace', 'age': 36}

# 2. Un dictionnaire vide :
stock = {}
print(len(stock))  # => 0

"""
3. a) une liste : les notes sont une suite ordonnée, sans "nom" particulier.
   b) un dictionnaire : on cherche un numéro à partir d'un NOM (la clé).
   c) un dictionnaire : mot français (clé) => mot anglais (valeur).
   d) une liste : c'est l'ordre (la position) qui compte.

   Règle générale : si on accède aux données par leur POSITION, on prend une
   liste ; si on y accède par un NOM (une clé), on prend un dictionnaire.
"""


#################################################
#  Indexation de valeurs et opérations de base  #
#################################################

capitales = {"France": "Paris", "Italie": "Rome", "Japon": "Tokyo"}

# 4. Accès par clé et longueur :
print(capitales["Italie"])  # => Rome
print(len(capitales))       # => 3 (le nombre de paires clé/valeur)

# 5. Clé absente :
try:
    capitales["Espagne"]
except KeyError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# 6. .get() avec une valeur par défaut :
print(capitales.get("Espagne", "inconnue"))  # => inconnue
print(capitales.get("Japon", "inconnue"))    # => Tokyo

# 7. capitales[0] provoque une KeyError : un dictionnaire n'a pas de positions,
#    seulement des clés. 0 est cherché comme une CLÉ, qui n'existe pas.
try:
    capitales[0]
except KeyError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


################################################
#  Ajouter, modifier et supprimer des valeurs  #
################################################

# 8. Gestion d'un stock :
stock = {"pommes": 10, "poires": 4}
stock["kiwis"] = 6        # a) nouvelle clé : ajout
print(stock)  # => {'pommes': 10, 'poires': 4, 'kiwis': 6}
stock["pommes"] = 7       # b) clé existante : modification
print(stock)  # => {'pommes': 7, 'poires': 4, 'kiwis': 6}
stock["poires"] += 3      # c) on part de la valeur existante
print(stock)  # => {'pommes': 7, 'poires': 7, 'kiwis': 6}
del stock["kiwis"]        # d) suppression
print(stock)  # => {'pommes': 7, 'poires': 7}

# 9. Contenu de d :
d = {"a": 1, "b": 2}
d["a"] = d["b"] + 10  # d["a"] vaut 12
d["c"] = d["a"] * 2   # nouvelle clé "c", qui vaut 24
d["b"] = "deux"       # une valeur peut changer de type
print(d)  # => {'a': 12, 'b': 'deux', 'c': 24}

# 10. Une clé ne peut apparaître qu'une seule fois : la 2e valeur remplace la
#     1re.
d = {"x": 1, "x": 2}
print(len(d), d["x"])  # => 1 2


##################################
#  Tester la présence d'une clé  #
##################################

# 11. ajouter_contact() :
def ajouter_contact(annuaire, nom, numero):
    """Ajoute nom => numero à l'annuaire, sauf si nom y figure déjà."""
    if nom in annuaire:
        print(f"{nom} existe déjà")
    else:
        annuaire[nom] = numero


annuaire = {}
ajouter_contact(annuaire, "Ada", "06 12 34 56 78")
ajouter_contact(annuaire, "Alan", "07 98 76 54 32")
ajouter_contact(annuaire, "Ada", "01 00 00 00 00")  # => Ada existe déjà
print(annuaire)
# => {'Ada': '06 12 34 56 78', 'Alan': '07 98 76 54 32'}
"""
Remarque : la fonction modifie directement le dictionnaire passé en
paramètre, sans avoir besoin de le retourner (cf. chap. 19).
"""

# 12. "in" teste les CLÉS, pas les valeurs :
print("Paris" in capitales)   # => False ("Paris" est une valeur)
print("France" in capitales)  # => True


###############################
#  Parcourir un dictionnaire  #
###############################

notes = {"Alice": 15, "Bob": 9, "Chloé": 12, "David": 18}

# 13. Affichage :
for eleve in notes:
    print(f"{eleve} : {notes[eleve]}/20")
# => Alice : 15/20
# => Bob : 9/20
# => Chloé : 12/20
# => David : 18/20

# 14. Moyenne de la classe :
somme = 0
for eleve in notes:
    somme += notes[eleve]
print(somme / len(notes))  # => 13.5

# 15. Meilleur élève :
meilleur = None
for eleve in notes:
    if meilleur is None or notes[eleve] > notes[meilleur]:
        meilleur = eleve
print(meilleur)  # => David

# 16. Élèves qui ont la moyenne :
recus = []
for eleve in notes:
    if notes[eleve] >= 10:
        recus.append(eleve)
print(recus)  # => ['Alice', 'Chloé', 'David']

# 17. Appréciations :
appreciations = {}
for eleve in notes:
    note = notes[eleve]
    if note >= 16:
        appreciations[eleve] = "Très bien"
    elif note >= 12:
        appreciations[eleve] = "Bien"
    elif note >= 10:
        appreciations[eleve] = "Passable"
    else:
        appreciations[eleve] = "Insuffisant"
print(appreciations)
# => {'Alice': 'Bien', 'Bob': 'Insuffisant', 'Chloé': 'Bien', 'David':
#     'Très bien'}


# 18. compter_lettres() :
def compter_lettres(mot):
    """Retourne un dictionnaire lettre => nombre d'occurrences dans mot."""
    compteur = {}
    for lettre in mot:
        if lettre in compteur:
            compteur[lettre] += 1
        else:
            compteur[lettre] = 1  # 1re apparition de cette lettre
    return compteur


print(compter_lettres("banane"))  # => {'b': 1, 'a': 2, 'n': 2, 'e': 1}

# 19. Inverser un dictionnaire :
nombres = {"un": 1, "deux": 2, "trois": 3}
inverse = {}
for mot in nombres:
    inverse[nombres[mot]] = mot
print(inverse)  # => {1: 'un', 2: 'deux', 3: 'trois'}
"""
Attention : si deux clés avaient la même valeur, l'une des deux serait perdue
dans le dictionnaire inversé (une clé est unique, cf. exercice 10).
"""

# 20. Traduction mot à mot :
fr_en = {"le": "the", "chat": "cat", "mange": "eats", "poisson": "fish"}
traduction = []
for mot in "le chat mange le poisson".split():
    traduction.append(fr_en.get(mot, mot))  # le mot lui-même s'il est inconnu
print(" ".join(traduction))  # => the cat eats the fish


#############################
#  Dictionnaires imbriqués  #
#############################

eleves = {
    "Alice": {"age": 15, "notes": [15, 17, 12]},
    "Bob": {"age": 16, "notes": [9, 11, 8]},
}

# 21. Accès imbriqués :
print(eleves["Bob"]["age"])       # => 16
print(eleves["Alice"]["notes"][1])  # => 17

# 22. Ajouts :
eleves["Bob"]["notes"].append(14)
eleves["Chloé"] = {"age": 15, "notes": []}
print(eleves["Bob"])    # => {'age': 16, 'notes': [9, 11, 8, 14]}
print(eleves["Chloé"])  # => {'age': 15, 'notes': []}

# 23. Moyenne de chaque élève :
for eleve in eleves:
    liste_notes = eleves[eleve]["notes"]
    if len(liste_notes) == 0:
        print(f"{eleve} : pas de note")
    else:
        somme = 0
        for note in liste_notes:
            somme += note
        print(f"{eleve} : {somme / len(liste_notes):.1f}")
# => Alice : 14.7
# => Bob : 10.5
# => Chloé : pas de note
"""
Sans le test sur la longueur, on diviserait par 0 pour Chloé :
ZeroDivisionError.
"""
