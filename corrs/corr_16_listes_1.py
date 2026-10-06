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
#  Chap. 16     #  Les listes (I) : corrigés                                   #
#               #                                                              #
################################################################################


########################
#  Déclarer une liste  #
########################

# 1. Nombre d'éléments :
print(len([]))                   # => 0
print(len([[]]))                 # => 1
print(len([1, [2, 3], "abc"]))   # => 3
print(len(["a", "b", "c", ""]))  # => 4
print(len([[], [], []]))         # => 3
"""
- [] est vide : 0 élément.
- [[]] contient UN élément, qui est lui-même une liste vide. Une "boîte qui
  contient une boîte vide" n'est pas vide !
- [1, [2, 3], "abc"] : la sous-liste [2, 3] et la string "abc" comptent
  chacune pour un seul élément.
- La chaîne vide "" est une valeur comme une autre : elle compte.
"""

# 2. Liste de courses :
courses = ["pain", "lait", "œufs"]
print(courses)        # => ['pain', 'lait', 'œufs']
print(type(courses))  # => <class 'list'>

# 3. Une seule liste au lieu de quatre variables :
villes = [
    "Lyon",
    "Lille",
    "Nantes",
    "Brest",
]
print(villes)  # => ['Lyon', 'Lille', 'Nantes', 'Brest']
"""
Entre crochets, les sauts de ligne sont autorisés. La virgule après "Brest"
est facultative, mais pratique : pour ajouter une ville, on ajoute une ligne
sans toucher à la précédente.
Bonus : villes[0] remplace ville_1, villes[1] remplace ville_2… et l'on peut
ajouter autant de villes que l'on veut sans créer de nouvelle variable.
"""


######################################
#  Accéder à une valeur de la liste  #
######################################

# 4. Valeurs des expressions :
notes = [12, 15, 8, 17, 10, 14]
print(notes[0])               # => 12
print(notes[3])               # => 17
print(notes[-1])              # => 14
print(notes[-2])              # => 10
print(notes[len(notes) - 1])  # => 14
print(notes[1] + notes[2])    # => 23
"""
- Les indices commencent à 0 : notes[3] est le 4e élément.
- Les indices négatifs partent de la fin : -1 est le dernier, -2
  l'avant-dernier.
- len(notes) vaut 6 : le dernier indice est donc 6 - 1 = 5, d'où le même
  résultat que notes[-1].
- notes[1] + notes[2] additionne deux VALEURS : 15 + 8 = 23.
"""

# 5. Liste de listes :
m = [[1, 2, 3], [4, 5, 6]]
print(m[1])        # => [4, 5, 6]
print(m[1][2])     # => 6
print(m[0][-1])    # => 3
print(len(m))      # => 2
print(len(m[0]))   # => 3
"""
On lit les crochets de gauche à droite : m[1] est la 2e sous-liste,
[4, 5, 6], puis [2] prend son 3e élément, 6.
len(m) compte les sous-listes (2), len(m[0]) les éléments de la 1re (3).
"""

# 6. Erreurs d'indice :
print(notes[-6])  # => 12 (pas d'erreur : -6 désigne le 1er élément)
try:
    notes[6]
except IndexError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    notes[-7]
except IndexError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    [][0]
except IndexError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
La liste a 6 éléments : les indices valides vont de 0 à 5, et de -1 à -6.
- notes[6] et notes[-7] sortent de ces limites : IndexError.
- notes[-6] est valide : c'est le premier élément.
- Une liste vide n'a aucun indice valide, pas même 0.
"""

# 7. Tests d'appartenance :
courses = ["pain", "lait", "œufs"]
print("lait" in courses)       # => True
print("Lait" in courses)       # => False
print("pain" not in courses)   # => False
print(3 in [1, [3]])           # => False
print([3] in [1, [3]])         # => True
"""
- "in" compare des valeurs exactes : "Lait" et "lait" sont deux chaînes
  différentes (la casse compte, cf. chap. 9).
- "in" ne regarde que le 1er niveau de la liste : [1, [3]] contient 1 et
  la liste [3], mais pas le nombre 3 directement.
"""

# 8. Un "if" avec "not in" :
if "beurre" not in courses:
    print("Pensez au beurre !")  # => Pensez au beurre !


#####################################
#  Modifier une valeur de la liste  #
#####################################

# 9. Trace du programme :
nombres = [1, 2, 3]
nombres[0] = nombres[2]  # nombres[2] vaut 3 : nombres devient [3, 2, 3]
nombres[2] = 0           # nombres devient [3, 2, 0]
print(nombres)           # => [3, 2, 0]

# 10. Échanger le premier et le dernier élément :
couleurs = ["rouge", "vert", "bleu", "jaune"]
temp = couleurs[0]          # on met de côté le 1er élément…
couleurs[0] = couleurs[-1]  # … avant de l'écraser par le dernier…
couleurs[-1] = temp         # … puis on place l'ancien 1er à la fin
print(couleurs)  # => ['jaune', 'vert', 'bleu', 'rouge']
"""
Sans la variable temp, on perdrait "rouge" dès la 2e ligne. Grâce à -1, le
code fonctionne quelle que soit la longueur de la liste.
(Au chap. 17, on verra une écriture plus courte :
couleurs[0], couleurs[-1] = couleurs[-1], couleurs[0].)
"""

# 11. Erreurs de modification :
lettres = ["a", "b", "c"]
lettres[-1] = "z"  # pas d'erreur : on remplace le dernier élément
print(lettres)     # => ['a', 'b', 'z']
try:
    lettres[3] = "d"
except IndexError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    "abc"[0] = "z"
except TypeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- lettres[3] n'existe pas : on ne peut REMPLACER qu'un élément existant.
  Pour en ajouter un, il faut .append() (section suivante).
- Une string n'est pas modifiable (cf. chap. 7) : TypeError.
"""


##################################
#  Longueur d'une liste : len()  #
##################################

# 12. Longueurs :
print(len([1, [2, 3], []]))  # => 3
print(len([[]]))             # => 1
print(len([""]))             # => 1
print(len("abc"))            # => 3
print(len(["abc"]))          # => 1
"""
- len("abc") compte les caractères d'une string (3), alors que len(["abc"])
  compte les éléments d'une liste qui contient UNE string (1).
- [""] contient un élément : la chaîne vide.
"""

# 13. Dernier et avant-dernier élément :
animaux = ["chat", "chien", "lapin", "hamster"]
print(animaux[-1])                # => hamster
print(animaux[len(animaux) - 1])  # => hamster
print(animaux[-2])                # => lapin
"""
animaux[-1] est l'écriture la plus courte et la plus lisible. La version
avec len() montre pourquoi le dernier indice vaut toujours len(liste) - 1.
"""


########################################################
#  .append(), .extend(), .pop(), del et l'opérateur +  #
########################################################

# 14. append et extend :
a = [1]
a.append(2)       # a vaut [1, 2]
a.append([3, 4])  # a vaut [1, 2, [3, 4]] : la liste est ajoutée telle quelle
a.extend([5])     # a vaut [1, 2, [3, 4], 5] : on ajoute les ÉLÉMENTS de [5]
print(a, len(a))  # => [1, 2, [3, 4], 5] 4
"""
.append() ajoute toujours UN élément (ici, une liste entière), alors que
.extend() ajoute un par un les éléments de la liste qu'on lui donne.
"""

# 15. Ce que retournent pop() et append() :
x = [1, 2, 3]
y = x.pop()       # retire 3 de x, et le RETOURNE : y vaut 3
z = x.append(9)   # ajoute 9 à x, et retourne None
print(x, y, z)    # => [1, 2, 9] 3 None
"""
Piège classique : .append() modifie la liste "en place" et ne retourne rien
(None). Écrire x = x.append(9) ferait donc perdre la liste !
"""

# 16. del et pop(i) :
l = [10, 20, 30, 40]
del l[1]         # on supprime 20 : l vaut [10, 30, 40]
print(l.pop(1))  # => 30 (l'élément d'indice 1 APRÈS la suppression)
print(l)         # => [10, 40]
"""
Après del l[1], les éléments suivants se sont décalés vers la gauche : 30 est
maintenant à l'indice 1. del ne retourne rien, .pop() retourne l'élément.
"""

# 17. "+" et .extend() :
a = [1, 2]
b = a + [3]
print(a, b)    # => [1, 2] [1, 2, 3]
a.extend([3])
print(a)       # => [1, 2, 3]
"""
"+" crée une NOUVELLE liste et laisse a intacte, alors que .extend() modifie
a elle-même.
"""

# 18. Une pile d'assiettes :
pile = []
pile.append("bleue")
pile.append("verte")
pile.append("rouge")   # la rouge est sur le dessus
retiree = pile.pop()   # .pop() retire le DERNIER élément ajouté
print(retiree)  # => rouge
print(pile)     # => ['bleue', 'verte']
"""
Une liste utilisée avec .append() et .pop() se comporte comme une pile : le
dernier élément posé est le premier retiré. On appelle cela une pile "LIFO"
("Last In, First Out").
"""

# 19. Ajouter au début :
nombres = [1, 2, 3]
nombres = [0] + nombres
print(nombres)  # => [0, 1, 2, 3]
"""
[0] + nombres crée une nouvelle liste qui commence par 0, et l'on réaffecte
la variable nombres. Attention : il faut mettre 0 dans une liste, car on ne
peut additionner une liste qu'avec une autre liste.
(Le chap. 24 présente la méthode .insert(), qui fait la même chose.)
"""


####################################
#  Parcourir une liste avec "for"  #
####################################

# 20. Afficher les courses :
for article in courses:
    print("-", article)
# => - pain
# => - lait
# => - œufs

# 21. Compter les notes supérieures ou égales à 10 :
notes = [12, 15, 8, 17, 10, 14, 6]
nb_moyenne = 0
for note in notes:
    if note >= 10:
        nb_moyenne += 1
print(nb_moyenne)  # => 5
"""
C'est un compteur (cf. chap. 13) : il démarre à 0 et augmente de 1 à chaque
note qui vérifie la condition. Attention au ">=" : 10 doit être compté.
"""

# 22. La plus grande note, sans max() :
plus_grande = notes[0]   # on part du 1er élément…
for note in notes:
    if note > plus_grande:
        plus_grande = note  # … et on le remplace dès qu'on trouve mieux
print(plus_grande)  # => 17
"""
Pourquoi partir de notes[0] et pas de 0 ? Parce que si toutes les valeurs
étaient négatives, la réponse 0 serait fausse. On part donc d'une vraie
valeur de la liste.
"""

# 23. Les carrés de 1 à 10 :
carres = []
for n in range(1, 11):   # 11 est exclu (cf. chap. 13)
    carres.append(n ** 2)
print(carres)  # => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 24. Fonction moyenne() :
def moyenne(nombres):
    if len(nombres) == 0:
        return 0
    total = 0
    for nombre in nombres:
        total += nombre
    return total / len(nombres)


print(moyenne([12, 15, 8]))  # => 11.666666666666666
print(moyenne([]))           # => 0
"""
On traite d'abord la liste vide : sans ce test, total / len(nombres)
diviserait par 0 et provoquerait une ZeroDivisionError (cf. chap. 4).
"""


# 25. Fonction mots_longs() :
def mots_longs(mots, n):
    resultat = []
    for mot in mots:
        if len(mot) > n:
            resultat.append(mot)
    return resultat


animaux = ["chat", "éléphant", "rat", "girafe"]
print(mots_longs(animaux, 4))  # => ['éléphant', 'girafe']
print(animaux)  # => ['chat', 'éléphant', 'rat', 'girafe'] (inchangée)
"""
On construit une nouvelle liste résultat au fur et à mesure : la liste de
départ n'est pas modifiée. "chat" a exactement 4 lettres : il n'a pas PLUS de
4 lettres, il est donc exclu.
"""


# 26. Fonction inverser() :
def inverser(liste):
    resultat = []
    for element in liste:
        resultat = [element] + resultat  # on ajoute chaque élément AU DÉBUT
    return resultat


depart = [1, 2, 3, 4]
print(inverser(depart))  # => [4, 3, 2, 1]
print(depart)            # => [1, 2, 3, 4] (inchangée)
"""
Déroulons la boucle :
    élément 1 : resultat = [1]
    élément 2 : resultat = [2, 1]
    élément 3 : resultat = [3, 2, 1]
    élément 4 : resultat = [4, 3, 2, 1]
(On verra des façons plus courtes au chap. 24, avec .reverse() et
reversed(), et au chap. 31, avec liste[::-1].)
"""
