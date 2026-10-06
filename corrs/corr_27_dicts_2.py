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
#  Chap. 27     #  Les dictionnaires (II) : corrigés                           #
#               #                                                              #
################################################################################


#############################
#  Créer des dictionnaires  #
#############################

# 1. Valeurs des expressions :
print(dict(nom="Ada", age=36))                  # => {'nom': 'Ada', 'age': 36}
print(dict([("a", 1), ("b", 2), ("a", 3)]))     # => {'a': 3, 'b': 2}
print(dict(zip("abc", [1, 2])))                 # => {'a': 1, 'b': 2}
print(dict.fromkeys("xyz", False))
# => {'x': False, 'y': False, 'z': False}
print({mot: len(mot) for mot in ["un", "deux", "trois"]})
# => {'un': 2, 'deux': 4, 'trois': 5}
print({n: n % 2 == 0 for n in range(4)})
# => {0: True, 1: False, 2: True, 3: False}
"""
- Avec dict(nom=…), les noms des arguments deviennent des clés (des strings).
- La clé "a" apparaît deux fois : la 2e valeur (3) écrase la 1re. La clé
  garde sa place d'origine (la 1re position).
- zip() s'arrête à la fin de la plus courte séquence : "c" est ignoré.
- fromkeys() parcourt l'itérable "xyz" : chaque caractère devient une clé.
"""

# 2. Pays et capitales :
pays = ["France", "Japon", "Brésil"]
capitales = ["Paris", "Tokyo", "Brasília"]
avec_zip = dict(zip(pays, capitales))
avec_comprehension = {pays[i]: capitales[i] for i in range(len(pays))}
print(avec_zip)
# => {'France': 'Paris', 'Japon': 'Tokyo', 'Brésil': 'Brasília'}
print(avec_zip == avec_comprehension)  # => True
"""
On peut aussi combiner les deux : {p: c for p, c in zip(pays, capitales)}.
La version dict(zip(…)) reste la plus courte et la plus lisible.
"""

# 3. Codes des lettres :
codes = {lettre: ord(lettre) for lettre in "python"}
print(codes)
# => {'p': 112, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}

# 4. Inverser un dictionnaire :
d = {"a": 1, "b": 2, "c": 3}
inverse = {valeur: cle for cle, valeur in d.items()}
print(inverse)  # => {1: 'a', 2: 'b', 3: 'c'}
d2 = {"a": 1, "b": 1}
print({valeur: cle for cle, valeur in d2.items()})  # => {1: 'b'}
"""
Les clés d'un dictionnaire sont uniques. Si deux clés ont la même valeur,
l'inversion produit deux fois la clé 1 : la seconde ("b") écrase la première
("a"), et une information est perdue. Inverser un dictionnaire n'est donc
sans perte que si toutes ses valeurs sont différentes.
"""


#############################################
#  D'autres méthodes sur les dictionnaires  #
#############################################

# 5. Pas à pas :
stock = {"pommes": 3, "poires": 0}
print(stock.get("kiwis"))             # => None
print(stock.get("kiwis", 0))          # => 0
print(stock.get("poires", 10))        # => 0
print(stock.pop("pommes"))            # => 3
print(stock.pop("kiwis", "absent"))   # => absent
print(stock.setdefault("poires", 5))  # => 0
print(stock.setdefault("cerises", 5))  # => 5
print(stock)                          # => {'poires': 0, 'cerises': 5}
"""
- .get() ne retourne la valeur par défaut que si la clé est ABSENTE. "poires"
  existe (avec la valeur 0) : on obtient 0, et non 10.
- .pop() retire la clé et retourne sa valeur ; avec une valeur par défaut, il
  ne plante pas si la clé est absente.
- .setdefault() ne modifie rien si la clé existe ("poires" garde 0) ; sinon,
  il AJOUTE la clé avec la valeur par défaut ("cerises").
- .get() et .pop() n'ajoutent jamais de clé : "kiwis" n'est pas dans stock.
"""

# 6. Copie ou alias :
a = {"x": 1}
b = a
c = a.copy()
b["x"] = 2
c["y"] = 3
print(a, b, c)  # => {'x': 2} {'x': 2} {'x': 1, 'y': 3}
"""
b est un second nom pour le même dictionnaire que a : modifier b modifie a.
c est une copie indépendante : elle a gardé l'ancienne valeur de "x", et la
clé "y" n'apparaît que dans c.
"""

# 7. Réglages :
defaut = {"langue": "fr", "theme": "clair", "taille": 12}
choix = {"theme": "sombre", "taille": 14}
reglages = defaut.copy()
reglages.update(choix)
print(reglages)  # => {'langue': 'fr', 'theme': 'sombre', 'taille': 14}
print({**defaut, **choix})
# => {'langue': 'fr', 'theme': 'sombre', 'taille': 14}
print(defaut)    # => {'langue': 'fr', 'theme': 'clair', 'taille': 12}
"""
Dans les deux cas, ce qui vient en dernier (choix) l'emporte en cas de clé
commune. Sans .copy(), .update() aurait modifié defaut lui-même. Depuis
Python 3.9, on peut aussi écrire defaut | choix.
"""


# 8. Stock restant :
def stock_restant(stock, produit):
    return stock.get(produit, 0)


print(stock_restant({"pain": 4}, "pain"))  # => 4
print(stock_restant({"pain": 4}, "lait"))  # => 0


#################################################
#  Les méthodes .keys(), .values() et .items()  #
#################################################

notes = {"Ana": 15, "Bob": 9, "Chloé": 17, "Djamel": 11}

# 9. a) Liste des prénoms :
print(list(notes.keys()))  # => ['Ana', 'Bob', 'Chloé', 'Djamel']
# (list(notes) donne le même résultat : parcourir un dict, c'est parcourir
# ses clés.)

# 9. b) Moyenne de la classe :
print(sum(notes.values()) / len(notes))  # => 13.0

# 9. c) Meilleure note :
print(max(notes.values()))  # => 17

# 9. d) Chaque élève avec sa note :
for eleve, note in notes.items():
    print(f"{eleve} : {note}/20")
# => Ana : 15/20
# => Bob : 9/20
# => Chloé : 17/20
# => Djamel : 11/20

# 9. e) Ordre alphabétique inverse :
print(sorted(notes, reverse=True))  # => ['Djamel', 'Chloé', 'Bob', 'Ana']

# 10. Élèves qui ont la moyenne, et élèves en échec :
admis = [eleve for eleve, note in notes.items() if note >= 10]
echecs = {eleve: note for eleve, note in notes.items() if note < 10}
print(admis)   # => ['Ana', 'Chloé', 'Djamel']
print(echecs)  # => {'Bob': 9}

# 11. Les vues sont dynamiques :
d = {"a": 1}
cles = d.keys()
d["b"] = 2
print(list(cles))  # => ['a', 'b']
"""
.keys() ne retourne pas une copie figée des clés, mais une "vue" sur le
dictionnaire : elle reflète toutes les modifications faites ensuite. Pour
obtenir une photo des clés à un instant donné, il faut écrire list(d.keys()).
"""

# 12. Supprimer pendant le parcours :
prix = {"pain": 1.2, "fromage": 7.5, "vin": 12.0, "lait": 0.9}
try:
    for produit in prix:
        if prix[produit] > 5:
            del prix[produit]
except RuntimeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
On ne peut pas changer la taille d'un dictionnaire pendant qu'on le parcourt
(RuntimeError: dictionary changed size during iteration). Solution : parcourir
une COPIE des clés, obtenue avec list() :
"""
prix = {"pain": 1.2, "fromage": 7.5, "vin": 12.0, "lait": 0.9}
for produit in list(prix):
    if prix[produit] > 5:
        del prix[produit]
print(prix)  # => {'pain': 1.2, 'lait': 0.9}
# Ou, plus simplement, on construit un nouveau dictionnaire filtré :
prix = {"pain": 1.2, "fromage": 7.5, "vin": 12.0, "lait": 0.9}
prix = {p: v for p, v in prix.items() if v <= 5}
print(prix)  # => {'pain': 1.2, 'lait': 0.9}


#######################################
#  Exemple : compter des occurrences  #
#######################################

# 13. Compter les lettres :
def compter_lettres(texte):
    compteur = {}
    for lettre in texte:
        if lettre != " ":
            compteur[lettre] = compteur.get(lettre, 0) + 1
    return compteur


print(compter_lettres("la lune"))
# => {'l': 2, 'a': 1, 'u': 1, 'n': 1, 'e': 1}
"""
compteur.get(lettre, 0) vaut 0 la première fois qu'on rencontre une lettre
(elle n'est pas encore une clé), puis le nombre d'apparitions déjà comptées.
"""

# 14. Lettre la plus fréquente :
compte = compter_lettres("abracadabra")
print(compte)
# => {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
print(max(compte, key=compte.get))  # => a
"""
max(compte) seul comparerait les CLÉS (et retournerait "r", la plus grande
dans l'ordre alphabétique). Avec key=compte.get, max() compare compte.get(cle)
pour chaque clé, c'est-à-dire les nombres d'apparitions.
"""


# 15. Regrouper par initiale :
def regrouper_par_initiale(mots):
    groupes = {}
    for mot in mots:
        groupes.setdefault(mot[0], []).append(mot)
    return groupes


print(regrouper_par_initiale(["pomme", "kiwi", "poire", "banane", "kaki"]))
# => {'p': ['pomme', 'poire'], 'k': ['kiwi', 'kaki'], 'b': ['banane']}
"""
groupes.setdefault(mot[0], []) retourne la liste associée à l'initiale si
elle existe déjà ; sinon, elle crée une liste vide pour cette initiale, et la
retourne. Dans les deux cas, on peut appeler .append() directement sur le
résultat. Version équivalente, plus longue :
    if mot[0] not in groupes:
        groupes[mot[0]] = []
    groupes[mot[0]].append(mot)
"""


#############################
#  Dictionnaires imbriqués  #
#############################

carnet = {
    "ana": {"tel": "0601020304", "ville": "Lyon", "age": 28},
    "bob": {"tel": "0611223344", "ville": "Paris", "age": 35},
    "chloe": {"tel": "0699887766", "ville": "Lyon", "age": 22},
}

# 16. Accès imbriqués :
print(carnet["bob"]["ville"])  # => Paris
print(len(carnet["ana"]))      # => 3
try:
    carnet["djamel"]["tel"]
except KeyError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
carnet["ana"] est un dictionnaire de 3 clés (tel, ville, age). "djamel"
n'est pas une clé de carnet : la KeyError se produit dès le 1er crochet, et le
message indique la clé fautive ('djamel').
"""

# 17. Modifier et ajouter :
carnet["bob"]["ville"] = "Marseille"
carnet["djamel"] = {"tel": "0700000000", "ville": "Paris", "age": 41}
print(carnet["bob"]["ville"])  # => Marseille
print(len(carnet))             # => 4

# 18. Contacts lyonnais et âge moyen :
for prenom, infos in carnet.items():
    if infos["ville"] == "Lyon":
        print(prenom)
# => ana
# => chloe
ages = [infos["age"] for infos in carnet.values()]
print(sum(ages) / len(ages))  # => 31.5
"""
On parcourt carnet.items() : prenom est la clé, et infos le dictionnaire
imbriqué du contact. Pour l'âge moyen, seules les valeurs nous intéressent :
on parcourt carnet.values().
"""

# 19. Nombre de contacts par ville :
par_ville = {}
for infos in carnet.values():
    ville = infos["ville"]
    par_ville[ville] = par_ville.get(ville, 0) + 1
print(par_ville)  # => {'Lyon': 2, 'Marseille': 1, 'Paris': 1}


##############################################
#  Dictionnaires et paramètres de fonctions  #
##############################################

# 20. Cadre avec options :
def cadre(texte, options=None):
    if options is None:
        options = {}
    bord = options.get("bord", "#")
    marge = options.get("marge", 1)
    milieu = bord + " " * marge + texte + " " * marge + bord
    print(bord * len(milieu))
    print(milieu)
    print(bord * len(milieu))


cadre("Salut", {"bord": "*", "marge": 3})
# => *************
# => *   Salut   *
# => *************
cadre("Salut")
# => #########
# => # Salut #
# => #########
"""
options.get() fournit une valeur par défaut pour chaque option absente. Pour
rendre options elle-même facultative, on lui donne la valeur par défaut None
(plutôt que {} : une valeur par défaut mutable est partagée entre tous les
appels, ce qui provoque des bugs surprenants dès qu'on la modifie).
"""


# 21. Déballer un dictionnaire avec "**" :
def adresse(rue, ville, code_postal):
    return f"{rue}, {code_postal} {ville}"


infos = {"ville": "Lyon", "rue": "3 rue Mercière", "code_postal": "69002"}
print(adresse(**infos))  # => 3 rue Mercière, 69002 Lyon
"""
adresse(**infos) équivaut à :
    adresse(ville="Lyon", rue="3 rue Mercière", code_postal="69002")
Ce sont des arguments NOMMÉS : chacun va dans le paramètre qui porte son nom,
quel que soit l'ordre. En revanche, les clés doivent correspondre exactement
aux noms des paramètres, sinon on obtient une TypeError.
"""


# 22. Profil avec **infos :
def creer_profil(nom, **infos):
    profil = {"nom": nom}
    profil.update(infos)
    return profil


print(creer_profil("Ada", age=36, ville="Londres"))
# => {'nom': 'Ada', 'age': 36, 'ville': 'Londres'}
print(creer_profil("Alan"))  # => {'nom': 'Alan'}
"""
**infos récupère tous les arguments nommés supplémentaires dans un
dictionnaire (vide si on n'en passe aucun). On aurait aussi pu écrire :
    return {"nom": nom, **infos}
"""
