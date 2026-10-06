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
#  Chap. 23     #  Itérables & compréhensions : corrigés                       #
#               #                                                              #
################################################################################

# On crée le fichier utilisé par les exercices 3, 4 et 10 (cf. chap. 28)
with open("courses.txt", "w") as fichier:
    fichier.write("pain\nlait\noeufs\nchocolat\nlait\npommes\n")


###################
#  Les itérables  #
###################

# 1. Affichage des trois boucles :
for x in (1, 2):
    print(x * 3)
# => 3
# => 6
for c in "oui":
    print(c + c)
# => oo
# => uu
# => ii
for cle in {"a": 1, "b": 2}:
    print(cle)
# => a
# => b
"""
Un tuple et une string se parcourent élément par élément (caractère par
caractère pour la string). Un dictionnaire se parcourt sur ses CLÉS : les
valeurs 1 et 2 ne sont jamais affichées.
"""

# 2. Valeurs des expressions :
print("ch" in "chat")       # => True (sous-chaîne présente)
print("ac" in "chat")       # => False ("a" et "c" y sont, mais pas côte à côte)
print(3 in range(3))        # => False (range(3) donne 0, 1, 2 : 3 est exclu)
print("b" in {"a": "b"})    # => False ("in" teste les clés, "b" est une valeur)
print("a" in {"a": "b"})    # => True
print(sum(range(5)))        # => 10 (0 + 1 + 2 + 3 + 4)
print(list("123"))          # => ['1', '2', '3'] (des strings, pas des ints !)
print(max("abricot"))       # => t (le caractère au plus grand code, cf. chap. 8)

# 3. Afficher les articles sans ligne vide :
# Méthode 1 : chaque ligne contient déjà son "\n", on demande à print() de ne
# pas en rajouter un.
for ligne in open("courses.txt"):
    print(ligne, end="")
# Méthode 2 : on retire le "\n" avec .strip(), et print() ajoute le sien.
for ligne in open("courses.txt"):
    print(ligne.strip())
"""
Les deux boucles affichent :
pain
lait
oeufs
chocolat
lait
pommes

Sans l'une de ces précautions, on aurait DEUX sauts de ligne après chaque
article (celui de la ligne lue + celui de print()), donc une ligne vide entre
chaque article.
"""

# 4. Compter les lignes :
nb_lignes = 0
for ligne in open("courses.txt"):
    nb_lignes += 1   # un compteur, comme au chap. 13
print(nb_lignes)  # => 6


#########################################
#  Bonus : comment fonctionne "for" ?  #
#########################################

# 5. Itérateur sur une string :
it = iter("abc")
print(next(it))  # => a
print(next(it))  # => b
print(list(it))  # => ['c'] (list() récupère ce qui RESTE dans l'itérateur)
print(list(it))  # => [] (l'itérateur est épuisé)

# 6. Boucle for réécrite avec while :
iterateur = iter([10, 20, 30])
while True:
    try:
        nombre = next(iterateur)
    except StopIteration:
        break   # plus d'éléments : on sort de la boucle
    print(nombre + 1)
# => 11
# => 21
# => 31
"""
C'est exactement ce que fait "for" pour nous : demander un itérateur, appeler
next() à chaque tour, et s'arrêter à la première StopIteration.
"""


###################################
#  Compréhensions sur des listes  #
###################################

# 7. Compréhensions simples :
print([7 * i for i in range(10)])
# => [0, 7, 14, 21, 28, 35, 42, 49, 56, 63]
print([len(mot) for mot in ["un", "deux", "trois"]])   # => [2, 4, 5]
print([ville.lower() for ville in ["Paris", "lyon", "NICE"]])
# => ['paris', 'lyon', 'nice']
print([int(s) for s in ["3", "14", "15"]])             # => [3, 14, 15]


def carre(x):
    return x ** 2


print([carre(n) for n in range(1, 11)])
# => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
d) Attention à bien appeler int() sur chaque élément : int(["3", "14"]) sur
   la liste entière soulèverait une TypeError.
e) range(1, 11) : la borne de droite est exclue, il faut donc 11 pour aller
   jusqu'à 10 (cf. chap. 13).
"""

# 8. Boucle traduite en compréhension :
resultat = []
for i in range(1, 6):
    resultat.append(i * 10 + 1)
resultat_comp = [i * 10 + 1 for i in range(1, 6)]
print(resultat_comp)              # => [11, 21, 31, 41, 51]
print(resultat == resultat_comp)  # => True
"""
Méthode (cf. chapitre) : on part de [], on y met ce qui était dans .append(…)
("i * 10 + 1"), puis la ligne du for sans les ":".
"""

# 9. Compréhension traduite en boucle :
initiales = []
for prenom in ["Ada", "Grace", "Alan"]:
    initiales.append(prenom[0])
print(initiales)  # => ['A', 'G', 'A']

# 10. Les articles sans "\n" :
articles = [ligne.strip() for ligne in open("courses.txt")]
print(articles)  # => ['pain', 'lait', 'oeufs', 'chocolat', 'lait', 'pommes']


########################################
#  Conditions sur les compréhensions  #
########################################

# 11. Valeurs des listes :
print([x for x in range(10) if x % 3 == 0])          # => [0, 3, 6, 9]
print([x * 2 for x in [1, -2, 3, -4] if x > 0])      # => [2, 6]
print(["+" if x > 0 else "-" for x in [1, -2, 3, -4]])
# => ['+', '-', '+', '-']
print([c for c in "programmation" if c not in "aeiouy"])
# => ['p', 'r', 'g', 'r', 'm', 'm', 't', 'n']
"""
- 2e liste : on FILTRE d'abord (on garde 1 et 3), puis on applique x * 2.
- 3e liste : pas de filtre, on garde les 4 éléments mais on choisit ce qu'on
  met à leur place.
"""

# 12. Compréhensions avec condition :
print([n for n in range(1, 21) if n % 2 == 1])
# => [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# (On aurait aussi pu écrire list(range(1, 21, 2)), sans compréhension.)
animaux = ["chat", "éléphant", "rat", "girafe", "ours"]
print([a for a in animaux if len(a) > 4])  # => ['éléphant', 'girafe']
notes = [12, 8, 15, 9, 17, 11]
moyenne = sum(notes) / len(notes)
print(moyenne)                                 # => 12.0
print([n for n in notes if n > moyenne])       # => [15, 17]
"""
c) On calcule la moyenne UNE SEULE FOIS avant la compréhension. Écrire
   "if n > sum(notes) / len(notes)" fonctionnerait aussi, mais recalculerait
   la moyenne pour chaque note.
"""

# 13. Remplacer les températures négatives :
temperatures = [3, -2, 0, 7, -5, 12]
print([0 if t < 0 else t for t in temperatures])  # => [3, 0, 0, 7, 0, 12]
"""
Il faut un "if … else …" à GAUCHE : on veut garder TOUS les éléments (même
longueur), seulement transformer certains d'entre eux. Un "if" à droite
FILTRERAIT les températures négatives, et la liste serait plus courte :
"""
print([t for t in temperatures if t >= 0])  # => [3, 0, 7, 12] (filtre)

# 14. Corriger la compréhension :
"""
"else" ne peut pas être utilisé seul à droite. Selon ce qu'on voulait faire :
"""
print([x if x > 2 else 0 for x in range(5)])  # => [0, 0, 0, 3, 4] (transformation)
print([x for x in range(5) if x > 2])         # => [3, 4] (filtre)


#####################################
#  Compréhensions sur des matrices  #
#####################################

notes = [[12, 15, 9], [8, 11, 14], [17, 13, 16]]

# 15. Première note, moyenne et meilleure note de chaque élève :
print([eleve[0] for eleve in notes])                 # => [12, 8, 17]
print([sum(eleve) / len(eleve) for eleve in notes])  # => [12.0, 11.0, 15.333333333333334]
print([max(eleve) for eleve in notes])               # => [15, 14, 17]
"""
Chaque élément parcouru (eleve) est une LIGNE de la matrice, donc une liste :
on peut lui appliquer [0], sum(), len(), max()…
"""

# 16. Toutes les notes + 1 :
print([[n + 1 for n in eleve] for eleve in notes])
# => [[13, 16, 10], [9, 12, 15], [18, 14, 17]]
"""
La compréhension extérieure parcourt les lignes ; pour chaque ligne, la
compréhension intérieure fabrique une nouvelle ligne.
"""

# 17. Table de multiplication :
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for ligne in table:
    print(ligne)
# => [1, 2, 3, 4, 5]
# => [2, 4, 6, 8, 10]
# => [3, 6, 9, 12, 15]
# => [4, 8, 12, 16, 20]
# => [5, 10, 15, 20, 25]


#############################
#  Compréhensions chaînées  #
#############################

# 18. Combinaisons :
print([a + b for a in "xy" for b in "123"])
# => ['x1', 'x2', 'x3', 'y1', 'y2', 'y3']
"""
2 × 3 = 6 éléments. Le premier "for" est la boucle extérieure : on garde "x"
pendant qu'on parcourt "123", puis on passe à "y".
"""

# 19. Aplatir la matrice et calculer la moyenne de la classe :
toutes_les_notes = [n for eleve in notes for n in eleve]
print(toutes_les_notes)  # => [12, 15, 9, 8, 11, 14, 17, 13, 16]
print(sum(toutes_les_notes) / len(toutes_les_notes))  # => 12.777777777777779

# 20. Deux dés dont la somme vaut 7 :
couples = [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7) if d1 + d2 == 7]
print(couples)       # => [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]
print(len(couples))  # => 6
"""
Sur les 36 combinaisons possibles, 6 donnent 7 : la probabilité de faire 7
avec deux dés est donc de 6/36 = 1/6. (C'est la somme la plus probable !)
"""


#############################
#  Compréhensions avancées  #
#############################

# 21. Dictionnaire des cubes :
print({n: n ** 3 for n in range(1, 6)})  # => {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# 22. Dictionnaire {fruit: nombre de lettres} :
fruits = ["pomme", "kiwi", "banane"]
print({fruit: len(fruit) for fruit in fruits})
# => {'pomme': 5, 'kiwi': 4, 'banane': 6}

# 23. Somme des carrés des nombres pairs de 0 à 100 :
print(sum(x ** 2 for x in range(0, 101, 2)))           # => 171700
print(sum(x ** 2 for x in range(101) if x % 2 == 0))   # => 171700 (idem)
"""
Pas besoin de crochets : l'expression génératrice calcule les carrés un par un
et sum() les additionne au fur et à mesure, sans créer de liste en mémoire.
"""

# 24. Générateur parcouru deux fois :
gen = (x + 1 for x in range(3))
print(list(gen))  # => [1, 2, 3]
print(list(gen))  # => [] : un générateur est un itérateur, il s'épuise


################################################
#  Quand (ne pas) utiliser une compréhension ?  #
################################################

"""
25. a) Une boucle for : on veut un EFFET (afficher), pas une nouvelle liste.
       [print(x) for x in l] créerait une liste inutile de None.
    b) Une compréhension : on construit une nouvelle liste à partir d'une
       autre, en une ligne lisible :
           prix_ttc = [p * 1.2 for p in prix_ht]
    c) Une boucle for : le traitement comporte plusieurs étapes et remplit
       trois listes ; une compréhension serait illisible (voire impossible).
    d) Une compréhension avec condition (un filtre) :
           valides = [e for e in emails if "@" in e]
"""

# Nettoyage : on supprime le fichier créé au début
import os
os.remove("courses.txt")
