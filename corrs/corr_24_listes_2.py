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
#  Chap. 24     #  Les listes (II) : corrigés                                  #
#               #                                                              #
################################################################################


#########################
#  Fonctions intégrées  #
#########################

# 1. Valeurs des expressions :
print(len([3, [1, 2], "abc"]))         # => 3
print(max([4, 18, 7]))                 # => 18
print(min(["kiwi", "abricot", "pomme"]))  # => abricot
print(sum([0.5, 1.5, 2]))              # => 4.0
print(sum([]))                         # => 0
print(list(enumerate("ab")))           # => [(0, 'a'), (1, 'b')]
print(list(zip([1, 2, 3], "xy")))      # => [(1, 'x'), (2, 'y')]
"""
- len() compte les éléments du 1er niveau : la sous-liste [1, 2] et la string
  "abc" comptent chacune pour UN élément.
- min() sur des strings utilise l'ordre alphabétique (cf. chap. 9).
- sum() d'une liste contenant un float retourne un float (4.0).
- La somme d'une liste vide vaut 0.
- zip() s'arrête à la fin de l'itérable le plus court ("xy" : 2 éléments), le
  3 est donc ignoré sans erreur.
"""

# 2. Les trois lignes soulèvent une erreur :
try:
    max([])
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    sum(["1", "2"])
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    min([3, "3"])
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- max([]) : une liste vide n'a pas de plus grand élément → ValueError.
- sum() additionne à partir de 0 : 0 + "1" est impossible → TypeError.
- min() doit comparer 3 et "3" : on ne peut pas comparer un int et une string
  avec "<" → TypeError.
"""

# 3. Statistiques sur les températures :
temperatures = [14, 17, 21, 19, 12, 9, 15]
t_min = min(temperatures)
t_max = max(temperatures)
print("Minimale :", t_min)                    # => Minimale : 9
print("Maximale :", t_max)                    # => Maximale : 21
print("Amplitude :", t_max - t_min)           # => Amplitude : 12
moyenne = sum(temperatures) / len(temperatures)
print("Moyenne :", round(moyenne, 1))         # => Moyenne : 15.3
"""
La moyenne est la somme divisée par le nombre d'éléments : 107 / 7 = 15.28…,
arrondie à 15.3.
"""

# 4. Jours numérotés à partir de 1 :
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi",
         "dimanche"]
for numero, jour in enumerate(jours, start=1):
    print(f"{numero}. {jour}")
# => 1. lundi
# => 2. mardi
# => …
# => 7. dimanche
"""
enumerate() produit des couples (indice, élément) ; start=1 fait commencer la
numérotation à 1 au lieu de 0. On "déballe" chaque couple dans deux variables
(numero et jour).
"""

# 5. Jours et températures avec zip() :
for jour, temp in zip(jours, temperatures):
    print(f"{jour} : {temp}°C")
# => lundi : 14°C
# => mardi : 17°C
# => …
# => dimanche : 15°C
"""
zip() associe le 1er jour à la 1re température, le 2e au 2e, etc. C'est plus
lisible qu'une boucle sur les indices (for i in range(len(jours))).
"""


######################################
#  Autres façons de créer une liste  #
######################################

# 6. Valeurs des expressions :
print(["-"] * 3)                  # => ['-', '-', '-']
print([0, 1] * 2)                 # => [0, 1, 0, 1]
print(list(range(10, 0, -3)))     # => [10, 7, 4, 1]
print(list("2024"))               # => ['2', '0', '2', '4']
print(list((True, False)))        # => [True, False]
print("a,b,,c".split(","))        # => ['a', 'b', '', 'c']
"""
- "*" répète la liste ENTIÈRE (et non chaque élément).
- range(10, 0, -3) part de 10, recule de 3 et s'arrête AVANT 0.
- list() sur une string donne la liste de ses caractères (des strings).
- Deux virgules consécutives encadrent une chaîne vide : '' fait partie du
  résultat de .split().
"""

# 7. 26 compteurs à zéro :
compteurs = [0] * 26
print(len(compteurs))  # => 26
"""
[0] * 26 est sans danger, car 0 est un entier (immuable). Avec des listes
imbriquées, c'est une autre histoire : cf. exercice 17.
"""


#########################
#  Parcourir une liste  #
#########################

# 8. prix n'est pas modifiée :
prix = [10, 20, 30]
for p in prix:
    p = p * 2
print(prix)  # => [10, 20, 30]
"""
À chaque tour, p reçoit la VALEUR d'un élément. "p = p * 2" donne une nouvelle
valeur à la variable p, mais ne touche pas à la liste : le lien entre p et la
case de la liste est perdu dès la réaffectation.
"""

# 9. Doubler sur place : il faut passer par les indices.
prix = [10, 20, 30]
for i in range(len(prix)):
    prix[i] = prix[i] * 2
print(prix)  # => [20, 40, 60]
"""
prix[i] = … modifie la case numéro i de la liste elle-même. C'est le cas où on
a besoin de l'indice (méthode 2 du chapitre) plutôt que de la valeur seule.
"""

# 10. Hausse ou baisse :
ventes = [120, 135, 128, 150, 149, 170]
for i in range(1, len(ventes)):
    if ventes[i] > ventes[i - 1]:
        print(f"Mois {i + 1} : hausse")
    else:
        print(f"Mois {i + 1} : baisse")
# => Mois 2 : hausse
# => Mois 3 : baisse
# => Mois 4 : hausse
# => Mois 5 : baisse
# => Mois 6 : hausse
"""
On a besoin de l'élément courant ET du précédent : on parcourt les indices à
partir de 1 (le 1er mois n'a pas de prédécesseur), et on compare ventes[i] à
ventes[i - 1]. Avec zip(), on aurait aussi pu écrire :
    for avant, apres in zip(ventes, ventes[1:]): …
(les slices comme ventes[1:] sont détaillées au chap. 31).
"""


# 11. Premier mot de plus de 6 lettres, avec while :
def indice_mot_long(mots):
    i = 0
    while i < len(mots) and len(mots[i]) <= 6:
        i += 1
    if i < len(mots):
        return i
    return None


print(indice_mot_long(["chat", "lapin", "hippopotame", "crocodile"]))  # => 2
print(indice_mot_long(["a", "b"]))                                     # => None
"""
La condition "i < len(mots)" est testée EN PREMIER : si on a dépassé la fin de
la liste, "and" court-circuite (cf. chap. 9) et mots[i] n'est jamais évalué,
ce qui évite une IndexError. En sortie de boucle, si i vaut len(mots), c'est
qu'aucun mot ne convenait.
"""

# 12. Supprimer pendant qu'on parcourt :
notes = [8, 9, 14, 7, 12]
for n in notes:
    if n < 10:
        notes.remove(n)
print(notes)  # => [9, 14, 12]
"""
Le 9 n'est pas supprimé ! Quand on retire le 8 (indice 0), tous les éléments
reculent d'une case : le 9 passe à l'indice 0. Mais la boucle passe à
l'indice 1, qui contient maintenant 14 : le 9 a été "sauté".

Règle : on ne modifie pas la taille d'une liste qu'on est en train de
parcourir. On construit plutôt une nouvelle liste :
"""
notes = [8, 9, 14, 7, 12]
notes_gardees = []
for n in notes:
    if n >= 10:
        notes_gardees.append(n)
print(notes_gardees)  # => [14, 12]
# Ou, en une ligne, avec une compréhension (cf. chap. 23) :
print([n for n in notes if n >= 10])  # => [14, 12]


##############
#  Matrices  #
##############

grille = [["X", "O", "X"],
          [" ", "X", "O"],
          ["O", " ", "X"]]

# 13. Accès aux cases :
print(grille[1][2])    # => O
print(grille[2][0])    # => O
print(len(grille))     # => 3
print(len(grille[0]))  # => 3
"""
grille[1] est la 2e ligne ([" ", "X", "O"]) ; grille[1][2] en est la 3e case.
len(grille) compte les lignes, len(grille[0]) les cases de la 1re ligne (le
nombre de colonnes).
"""

# 14. Affichage de la grille :
for ligne in grille:
    print("|".join(ligne))
# => X|O|X
# =>  |X|O
# => O| |X
"""
.join() (cf. chap. 8) colle les éléments d'une liste de strings, avec "|"
entre chaque élément.
"""

# 15. Cases vides :
nb_vides = 0
for i in range(len(grille)):
    for j in range(len(grille[i])):
        if grille[i][j] == " ":
            nb_vides += 1
            print("Case vide :", (i, j))
print("Nombre de cases vides :", nb_vides)
# => Case vide : (1, 0)
# => Case vide : (2, 1)
# => Nombre de cases vides : 2
"""
Deux boucles imbriquées : i parcourt les lignes, j les colonnes. On a besoin
des indices (et pas seulement des valeurs) pour afficher les coordonnées.
"""

# 16. Diagonale principale :
gagne = grille[0][0] == "X" and grille[1][1] == "X" and grille[2][2] == "X"
print(gagne)  # => True
# Version avec une boucle, qui marche pour n'importe quelle taille de grille :
gagne = True
for i in range(len(grille)):
    if grille[i][i] != "X":
        gagne = False
print(gagne)  # => True
"""
Sur la diagonale principale, l'indice de ligne est égal à l'indice de colonne :
ce sont les cases grille[i][i].
"""

# 17. Le piège de la multiplication de listes imbriquées :
m = [[0] * 2] * 2
m[0][1] = 5
print(m)  # => [[0, 5], [0, 5]]
"""
"* 2" ne copie pas la sous-liste [0, 0] : il met DEUX FOIS LA MÊME sous-liste
dans m. Modifier m[0] modifie donc aussi m[1], puisque c'est le même objet.

Correction : on crée une nouvelle sous-liste pour chaque ligne.
"""
m = [[0] * 2 for _ in range(2)]
m[0][1] = 5
print(m)  # => [[0, 5], [0, 0]]


###################
#  Tri de listes  #
###################

# 18. sorted() contre .sort() :
l = [3, 1, 2]
print(sorted(l))  # => [1, 2, 3]
print(l)          # => [3, 1, 2]
print(l.sort())   # => None
print(l)          # => [1, 2, 3]
"""
sorted() RETOURNE une nouvelle liste triée et ne touche pas à l'original.
.sort() trie la liste SUR PLACE et retourne None : c'est pourquoi on n'écrit
jamais l = l.sort() (l vaudrait None).
"""

# 19. Trier des prénoms :
prenoms = ["Zoé", "adam", "Léa", "bob"]
# a) Ordre par défaut :
print(sorted(prenoms))  # => ['Léa', 'Zoé', 'adam', 'bob']
"""
Les strings sont comparées par code de caractère (cf. chap. 8) : toutes les
majuscules (codes 65 à 90) passent avant toutes les minuscules (97 à 122).
"""
# b) Sans tenir compte des majuscules :
print(sorted(prenoms, key=str.lower))  # => ['adam', 'bob', 'Léa', 'Zoé']
"""
key=str.lower : Python compare les versions en minuscules, mais la liste
retournée contient les prénoms d'origine.
"""
# c) Par longueur décroissante :
print(sorted(prenoms, key=len, reverse=True))
# => ['adam', 'Zoé', 'Léa', 'bob']
"""
"adam" (4 lettres) est en tête, puis les trois prénoms de 3 lettres. Ceux-ci
restent dans leur ordre d'origine : le tri de Python est STABLE (des éléments
égaux pour la clé ne sont pas réordonnés).
"""


# 20. Trier des élèves par moyenne décroissante :
def moyenne_eleve(eleve):
    return eleve[2]


classe = [("Ana", 17, 14.5), ("Bob", 16, 12.0), ("Chloé", 17, 16.0)]
classement = sorted(classe, key=moyenne_eleve, reverse=True)
print(classement)
# => [('Chloé', 17, 16.0), ('Ana', 17, 14.5), ('Bob', 16, 12.0)]
print(classement[0][0])  # => Chloé
"""
On passe la FONCTION moyenne_eleve (sans parenthèses !) au paramètre key :
sorted() l'appelle sur chaque tuple et trie selon la valeur retournée (la
moyenne, à l'indice 2).
"""


# 21. Médiane :
def mediane(nombres):
    tries = sorted(nombres)  # sorted() ne modifie pas la liste d'origine
    n = len(tries)
    milieu = n // 2
    if n % 2 == 1:
        return tries[milieu]
    return (tries[milieu - 1] + tries[milieu]) / 2


print(mediane([3, 1, 2]))     # => 2
print(mediane([4, 1, 3, 2]))  # => 2.5
valeurs = [4, 1, 3, 2]
mediane(valeurs)
print(valeurs)                # => [4, 1, 3, 2] (non modifiée)
"""
- Si n est impair (3), l'élément du milieu est à l'indice n // 2 = 1.
- Si n est pair (4), les deux éléments du milieu sont aux indices 1 et 2,
  c'est-à-dire milieu - 1 et milieu.
Utiliser .sort() aurait modifié la liste de l'appelant : c'est pourquoi on
utilise sorted().
"""


######################################
#  D'autres méthodes sur les listes  #
######################################

# 22. Pas à pas :
l = ["a", "b", "c", "b"]
l.insert(1, "z")        # l vaut ['a', 'z', 'b', 'c', 'b']
l.remove("b")           # l vaut ['a', 'z', 'c', 'b'] (seul le 1er "b" part)
print(l.pop(0))         # => a  (l vaut ['z', 'c', 'b'])
print(l.index("b"))     # => 2
print(l.count("b"))     # => 1
print(l.append("d"))    # => None (l vaut ['z', 'c', 'b', 'd'])
print(l)                # => ['z', 'c', 'b', 'd']
"""
- .insert(1, "z") place "z" à l'indice 1 et décale le reste vers la droite.
- .remove() ne retire que la PREMIÈRE occurrence.
- .pop(0) retire ET retourne l'élément d'indice 0.
- .append(), comme la plupart des méthodes qui modifient la liste, retourne
  None.
"""


# 23. Retirer toutes les occurrences :
def retirer_tout(liste, valeur):
    for _ in range(liste.count(valeur)):
        liste.remove(valeur)


lettres = ["a", "b", "a", "c", "a"]
retirer_tout(lettres, "a")
print(lettres)  # => ['b', 'c']
"""
On compte d'abord les occurrences, puis on appelle .remove() autant de fois.
La fonction ne retourne rien : elle modifie la liste reçue, qui est le même
objet que celui de l'appelant (cf. chap. 19).
"""

# 24. File d'attente :
file = ["Ana", "Bob"]
file.append("Chloé")       # arrive en fin de file
file.insert(0, "Djamel")   # coupe-file : en tête
servi = file.pop(0)        # la première personne est servie
print(servi)               # => Djamel
file.remove("Bob")         # Bob quitte la file
print(file)                # => ['Ana', 'Chloé']


##########################
#  Bonus sur les listes  #
##########################

# 25. Copie ou pas copie ?
a = [1, 2]
b = a
c = a.copy()
b.append(3)
print(a, b, c)                 # => [1, 2, 3] [1, 2, 3] [1, 2]
print(a is b, a is c, a == b)  # => True False True
"""
"b = a" ne copie pas : a et b sont deux noms pour LA MÊME liste. Ajouter 3 via
b modifie donc aussi a. c est une vraie copie, indépendante.
"is" teste si c'est le même objet, "==" si les contenus sont égaux.
"""

# 26. Comparaisons de listes :
print([1, 2] == [2, 1])     # => False
print([2, 1] > [1, 9, 9])   # => True
print(["b"] < ["a", "z"])   # => False
"""
- L'ordre compte : [1, 2] et [2, 1] sont différentes.
- Les listes se comparent élément par élément, comme des mots dans le
  dictionnaire : dès que deux éléments diffèrent, ils décident du résultat.
  2 > 1 dès le 1er élément, donc [2, 1] > [1, 9, 9], quelle que soit la suite.
- "b" > "a", donc ["b"] est plus grande que ["a", "z"].
"""

# 27. Déballage avec "*" :
premier, *milieu, dernier = [5, 10, 15, 20, 25]
print(premier)  # => 5
print(milieu)   # => [10, 15, 20]
print(dernier)  # => 25
"""
La variable étoilée récupère, SOUS FORME DE LISTE, tout ce qui n'est pas pris
par les autres variables.
"""

# 28. Liste → string :
date = [2024, 3, 15]
print("-".join(str(n) for n in date))  # => 2024-3-15
"""
.join() n'accepte que des strings : il faut d'abord convertir chaque entier
avec str(). Ici, on passe à .join() une expression génératrice (cf. chap. 23) ;
on aurait aussi pu lui passer une compréhension de liste :
"-".join([str(n) for n in date]).
"""
