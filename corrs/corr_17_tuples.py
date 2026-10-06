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
#  Chap. 17     #  Les tuples : corrigés                                       #
#               #                                                              #
################################################################################


############################
#  Définition et création  #
############################

# 1. Types :
print(type((5)))         # => <class 'int'>
print(type((5,)))        # => <class 'tuple'>
print(type(()))          # => <class 'tuple'>
print(type(("a")))       # => <class 'str'>
print(type(("a",)))      # => <class 'tuple'>
print(type(tuple("ab")))  # => <class 'tuple'>
x = 5,
print(x)                 # => (5,)
"""
- Ce sont les VIRGULES qui créent un tuple, pas les parenthèses : (5) et
  ("a") sont simplement 5 et "a" entre parenthèses.
- () est l'exception : des parenthèses vides créent bien un tuple vide.
- x = 5, crée un tuple à un élément, même sans parenthèses.
"""

# 2. Le bug de la virgule :
prix = 12.5,
total = prix * 2
print(total)  # => (12.5, 12.5)
"""
La virgule en fin de ligne fait de prix un TUPLE (12.5,). Multiplier un tuple
par 2 le répète (comme pour une liste ou une string), au lieu de calculer.
Correction : on retire la virgule.
"""
prix = 12.5
total = prix * 2
print(total)  # => 25.0

# 3. Un point :
point = (3, -2)
print(f"x = {point[0]}, y = {point[1]}")  # => x = 3, y = -2


########################
#  Intérêt des tuples  #
########################

# 4. Liste ou tuple ?
"""
a) Liste : le nombre de notes augmente au fil de l'année, et toutes ont la
   même nature.
b) Tuple : toujours 2 valeurs, et chaque position a un sens précis (1re =
   latitude, 2e = longitude).
c) Tuple : 3 valeurs fixes (jour, mois, année), qui ne changent pas.
d) Liste : on ajoute et on retire des articles.
e) Tuple : toujours 3 composantes, chacune avec un rôle précis.

La règle : beaucoup d'éléments de même nature, en nombre variable → liste ;
quelques éléments de natures différentes, à des positions fixes → tuple.
"""
naissance = (14, 7, 1998)
couleur = (255, 128, 0)
notes = [12, 15]
notes.append(9)  # possible avec une liste, impossible avec un tuple
print(naissance, couleur, notes)  # => (14, 7, 1998) (255, 128, 0) [12, 15, 9]


# 5. Fonction min_max() :
def min_max(nombres):
    plus_petit = nombres[0]
    plus_grand = nombres[0]
    for n in nombres:
        if n < plus_petit:
            plus_petit = n
        if n > plus_grand:
            plus_grand = n
    return plus_petit, plus_grand  # la virgule crée un tuple


mini, maxi = min_max([7, 2, 9, 4])
print(mini, maxi)  # => 2 9
print(min_max([7, 2, 9, 4]))  # => (2, 9)
"""
"return plus_petit, plus_grand" retourne UN tuple de deux valeurs, que l'on
déballe aussitôt dans deux variables. Ce sont deux "if" séparés (et non un
"elif") : le premier élément est à la fois le plus petit et le plus grand
au départ.
"""


# 6. Division euclidienne :
def division(a, b):
    return a // b, a % b


q, r = division(17, 5)
print(q, r)  # => 3 2
print(divmod(17, 5))  # => (3, 2)
"""
17 = 5 × 3 + 2 : le quotient vaut 3 et le reste 2. La fonction intégrée
divmod() (cf. chap. 4) fait exactement la même chose, et retourne elle
aussi un tuple.
"""


########################
#  Opérations de base  #
########################

# 7. Valeurs des expressions :
t = (4, 8, 15, 16, 23, 42)
print(t[2])         # => 15
print(t[-1])        # => 42
print(len(t))       # => 6
print(15 in t)      # => True
print(t.index(16))  # => 3
print(t.count(4))   # => 1
print(sum(t))       # => 108
print(max(t))       # => 42
"""
On accède aux éléments d'un tuple exactement comme à ceux d'une liste.
.index(16) donne la POSITION de 16 (indice 3), .count(4) le NOMBRE de fois où
4 apparaît (une fois).
"""

# 8. Concaténation et répétition :
print((1, 2) + (3,))       # => (1, 2, 3)
print(("ab",) * 3)         # => ('ab', 'ab', 'ab')
print((0,) * 0)            # => ()
print(((1, 2),) + (3, 4))  # => ((1, 2), 3, 4)
"""
- (3,) est un tuple d'un élément : on peut donc le concaténer.
- Répéter 0 fois donne un tuple vide.
- ((1, 2),) est un tuple qui contient UN élément, le tuple (1, 2) : le
  résultat a donc 3 éléments.
"""

# 9. Erreurs :
print(t + (5,))  # => (4, 8, 15, 16, 23, 42, 5) (pas d'erreur)
try:
    t + 5
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    t[10]
except IndexError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    t.index(99)
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- On ne peut concaténer un tuple qu'avec un autre tuple : t + 5 est une
  TypeError, alors que t + (5,) fonctionne.
- t[10] : le tuple n'a que 6 éléments → IndexError.
- .index() cherche une valeur absente → ValueError.
"""

# 10. Rotation de trois variables :
a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)  # => 2 3 1
"""
Python évalue d'abord tout le côté droit : (b, c, a) vaut (2, 3, 1). Puis il
déballe ce tuple dans a, b et c. Les valeurs ont "tourné" d'un cran.
"""


########################
#  Parcourir un tuple  #
########################

# 11. Les étapes numérotées :
etapes = ("Paris", "Lyon", "Marseille")
for i in range(len(etapes)):
    print(f"Étape {i + 1} : {etapes[i]}")
# => Étape 1 : Paris
# => Étape 2 : Lyon
# => Étape 3 : Marseille
"""
range(len(etapes)) parcourt les indices 0, 1, 2. On affiche i + 1 pour
commencer la numérotation à 1. (Le chap. 24 présente enumerate(), qui
simplifie ce genre de boucle.)
"""

# 12. Le panier :
panier = [("stylo", 1.5, 4), ("cahier", 2.5, 2), ("sac", 24.0, 1)]
total = 0
for nom, prix, quantite in panier:
    prix_ligne = prix * quantite
    print(f"{nom} : {prix_ligne} €")
    total += prix_ligne
print(f"Total : {total} €")
# => stylo : 6.0 €
# => cahier : 5.0 €
# => sac : 24.0 €
# => Total : 35.0 €
"""
À chaque tour, un tuple du panier est déballé dans les trois variables nom,
prix et quantite. C'est beaucoup plus lisible que article[0], article[1]…
"""

# 13. Le meilleur élève :
eleves = [("Alice", 15), ("Bob", 12), ("Chloé", 18), ("Dan", 9)]
meilleur_nom, meilleure_note = eleves[0]
for nom, note in eleves:
    if note > meilleure_note:
        meilleur_nom = nom
        meilleure_note = note
print(meilleur_nom)  # => Chloé
"""
Même méthode que pour chercher un maximum (cf. corrigés du chap. 16) : on part
du premier élève, et on le remplace dès qu'on trouve une meilleure note. On
garde le nom ET la note, car c'est le nom que l'on veut afficher.
"""


#############################
#  Déballage ("unpacking")  #
#############################

# 14. Déballages :
a, *b = "hello"
print(a, b)        # => h ['e', 'l', 'l', 'o']
*debut, fin = (1, 2, 3)
print(debut, fin)  # => [1, 2] 3
x, (y, z) = 1, (2, 3)
print(x, y, z)     # => 1 2 3
_, milieu, _ = (7, 8, 9)
print(milieu)      # => 8
"""
- La variable étoilée reçoit "tout le reste", toujours sous forme de LISTE,
  même si l'on déballe une string ou un tuple.
- Pour un tuple imbriqué, on reproduit la même "forme" à gauche du "=".
- "_" est une convention pour une valeur dont on ne se sert pas.
"""

# 15. Erreurs de déballage :
try:
    a, b = (1, 2, 3)
except ValueError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    a, b, c = "ab"
except ValueError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
a, b = "ab"
print(a, b)  # => a b (pas d'erreur)
"""
Le nombre de variables doit être égal au nombre de valeurs : trop de valeurs
ou pas assez provoquent une ValueError. "ab" contient bien 2 caractères :
la dernière ligne fonctionne.
"""


# 16. Fonction premier_et_dernier() :
def premier_et_dernier(sequence):
    return sequence[0], sequence[-1]


premier, dernier = premier_et_dernier([3, 1, 4, 1, 5])
print(premier, dernier)  # => 3 5
premier, dernier = premier_et_dernier("Python")
print(premier, dernier)  # => P n
"""
Les indices 0 et -1 fonctionnent sur toutes les séquences : listes, tuples
et strings. La fonction n'a donc pas besoin de savoir ce qu'elle reçoit.
"""


#########################
#  Comparer des tuples  #
#########################

# 17. Comparaisons :
print((1, 2) == (2, 1))                         # => False
print((3, 1) < (2, 9))                          # => False
print(("Dupont", "Marie") < ("Dupont", "Paul"))  # => True
print((1, 2) < (1, 2))                          # => False
print((0,) < (0, 0))                            # => True
print((5, 2) == [5, 2])                         # => False
"""
- "==" exige les mêmes éléments, dans le même ordre.
- "<" compare élément par élément : 3 > 2, donc (3, 1) n'est pas "avant"
  (2, 9), quel que soit le reste.
- Les noms sont égaux, on compare donc les prénoms : "Marie" < "Paul" (ordre
  alphabétique, cf. chap. 9).
- Deux tuples égaux ne sont pas "strictement plus petits" l'un que l'autre.
- (0,) est un "début" de (0, 0) : le plus court est classé avant.
- Un tuple n'est jamais égal à une liste, même avec le même contenu.
"""

# 18. La date la plus ancienne :
dates = [(2024, 3, 15), (2023, 12, 1), (2024, 1, 30)]
plus_ancienne = dates[0]
for date in dates:
    if date < plus_ancienne:
        plus_ancienne = date
print(plus_ancienne)  # => (2023, 12, 1)
print(min(dates))     # => (2023, 12, 1)
"""
min() utilise "<" pour comparer les éléments. Or les tuples se comparent
élément par élément : d'abord l'année, puis le mois, puis le jour. C'est
exactement l'ordre chronologique ! C'est pour cela qu'on range les dates
dans l'ordre (année, mois, jour) et non (jour, mois, année).
"""


#######################
#  Modifier un tuple  #
#######################

# 19. Contenu modifiable, tuple non modifiable :
t = (1, [2, 3])
t[1].append(4)
print(t)  # => (1, [2, 3, 4])
t = t + (5,)
print(t)  # => (1, [2, 3, 4], 5)
try:
    t[0] = 0
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- t[1] est une liste : on peut modifier son CONTENU, le tuple désigne
  toujours la même liste.
- t = t + (5,) ne modifie pas le tuple : on crée un NOUVEAU tuple, et la
  variable t le désigne désormais.
- t[0] = 0 tente de modifier une "case" du tuple : TypeError.
"""

# 20. "Modifier" une couleur :
orange = (255, 128, 0)
# a) en construisant un nouveau tuple :
nouvelle = (orange[0], 64, orange[2])
print(nouvelle)  # => (255, 64, 0)
# b) en passant par une liste :
composantes = list(orange)
composantes[1] = 64
nouvelle = tuple(composantes)
print(nouvelle)  # => (255, 64, 0)
print(orange)    # => (255, 128, 0) (le tuple de départ n'a pas changé)
"""
La méthode a) est la plus courte pour un petit tuple. La méthode b) est
pratique quand il y a beaucoup de modifications à faire.
"""


########################################
#  Conversions entre listes et tuples  #
########################################

# 21. Conversions :
print(list((1, 2)))         # => [1, 2]
print(tuple([3]))           # => (3,)
print(tuple("hey"))         # => ('h', 'e', 'y')
print(list(tuple("ab")))    # => ['a', 'b']
print(tuple(range(3)))      # => (0, 1, 2)
"""
list() et tuple() acceptent n'importe quelle séquence : une liste, un tuple,
une string (découpée en caractères) ou un range.
"""


# 22. Fonction ajouter_note() :
def ajouter_note(notes, note):
    return notes + (note,)  # (note,) : un tuple d'un seul élément


notes_t1 = (12, 15)
notes_t2 = ajouter_note(notes_t1, 9)
print(notes_t2)  # => (12, 15, 9)
print(notes_t1)  # => (12, 15) (inchangé)
"""
On ne peut pas modifier un tuple : la fonction en crée un NOUVEAU. Sans la
virgule, notes + (note) essaierait d'additionner un tuple et un int, ce qui
provoquerait une TypeError.
"""
