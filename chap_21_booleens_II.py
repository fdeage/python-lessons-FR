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
#  Chap. 21     #  Booléens II                                                 #
#               #                                                              #
################################################################################
#
#  - Tables de vérité
#  - Les lois de De Morgan
#  - Calculs avec les booléens et conversions
#  - Valeurs "vraies" et "fausses" : bool()
#  - Ce que retournent vraiment "and" et "or"
#  - Égalité et identité : "==" et "is"
#  - all() et any()
#  - Les opérateurs bit à bit
#
###############################################################

# Tables de vérité
###################

"""
On peut résumer le fonctionnement de "not", "and" et "or" avec des tables, qu'on
appelle des tables de vérité.

Chaque cellule de la table sera une combinaison booléenne :
    - de la valeur sur la même ligne à gauche (T ou F)
    - de la valeur sur la même colonne en haut (T ou F)

Table de vérité de l'opérateur "and" :
     |   T   |   F   |
 --- | ----- | ----- |
 T   | True  | False |
 F   | False | False |

Table de vérité de l'opérateur "or" :
     |   T  |   F   |
 --- | ---- | ----- |
 T   | True | True  |
 F   | True | False |

Table de vérité de l'opérateur "not" (ne prend qu'un paramètre) :
     |  not  |
 --- | ----- |
 T   | False |
 F   | True  |

On peut aussi écrire une table de vérité avec une ligne par combinaison
possible des entrées. C'est plus pratique quand il y a plus de deux entrées
(avec n entrées, il y a 2 ** n lignes) :

  A     | B     | A and B | A or B
 ------ | ----- | ------- | ------
  True  | True  | True    | True
  True  | False | False   | True
  False | True  | False   | True
  False | False | False   | False
"""

# On peut faire calculer cette table par Python avec deux boucles (chap. 13) :
for A in (True, False):
    for B in (True, False):
        print(A, B, A and B, A or B)
# => True True True True
# => True False False True
# => False True False True
# => False False False False

"""
Le "OU exclusif" (XOR) est vrai si UN SEUL des deux termes est vrai, mais pas
les deux. Python n'a pas de mot-clé "xor", mais pour deux booléens, il suffit de
tester s'ils sont différents avec "!=" :

  A     | B     | A != B (xor)
 ------ | ----- | ------------
  True  | True  | False
  True  | False | True
  False | True  | True
  False | False | False
"""
fromage = True
dessert = True
print(fromage != dessert)  # => False : "fromage OU dessert", mais pas les deux !


# Les lois de De Morgan
########################

"""
Les lois de De Morgan (du nom du mathématicien Augustus De Morgan) expliquent
comment "distribuer" un not sur un and ou un or :

    not (A and B)  est équivalent à  (not A) or (not B)
    not (A or B)   est équivalent à  (not A) and (not B)

En français : "il est faux que (il pleut ET il fait froid)" revient à dire
"il ne pleut pas OU il ne fait pas froid".

C'est très utile pour simplifier ou réécrire une condition de if (chap. 12).
"""
# On peut le vérifier pour toutes les combinaisons :
for A in (True, False):
    for B in (True, False):
        print((not (A and B)) == ((not A) or (not B)),
              (not (A or B)) == ((not A) and (not B)))
# => True True (4 fois : les deux lois sont toujours vérifiées)

"""
Attention à la précédence (cf. chap. 5) : "not" est MOINS prioritaire que
"==", donc sans les parenthèses autour de "not (A and B)", Python lirait
"not ((A and B) == …)". Dans le doute, mettez des parenthèses !
"""

# Exemple d'utilisation : ces deux conditions sont équivalentes
age = 25
if not (age < 18 or age > 65):
    print("âge actif")   # => âge actif
if age >= 18 and age <= 65:
    print("âge actif")   # => âge actif (plus lisible : pas de "not")
if 18 <= age <= 65:
    print("âge actif")   # => âge actif (encore plus lisible, cf. chap. 9)


# Calculs avec les booléens et conversions
###########################################

"""
Attention : si vous utilisez True ou False dans un calcul arithmétique (avec
"+", "-", "*"…), ils seront automatiquement convertis ("castés") en entiers.

True et False valent en fait 1 et 0.
"""
True + True    # => 2
False + False  # => 0
True + False   # => 1
True * 8       # => 8
False - 5      # => -5

# Les opérateurs de comparaison vont convertir True et False en ints (1 et 0)
0 == False     # => True
1 == True      # => True
2 == True      # => False
-5 != False    # => True

# En fait, le type bool est une sorte d'int (un "sous-type")
print(int(True), int(False))   # => 1 0
print(isinstance(True, int))   # => True
print(type(True))              # => <class 'bool'>

# Une utilisation pratique (et assumée) : compter les True d'une liste
reponses_justes = [True, False, True, True]
print(sum(reponses_justes))    # => 3

# Cela donnera parfois d'étranges calculs :
(2 + 2 == 4) + (2 + 2 == 3) + (1 == 1)  # => 2

"""
Explication : ici l'opérateur "+" va entraîner une conversion de
True et False en leur équivalent numérique (1 et 0).

Conclusion : n'utilisez pas de booléens avec des opérateurs arithmétiques :
utilisez… les opérateurs booléens vus plus haut ! (Exception tolérée : le
sum() d'une liste de booléens pour les compter.)
"""


# Valeurs "vraies" et "fausses" : bool()
#########################################

"""
Inversement, on peut convertir n'importe quelle valeur en booléen avec la
fonction intégrée bool(). C'est ce que fait Python automatiquement quand on met
autre chose qu'un booléen dans un "if" ou un "while" (cf. chap. 12).

La règle est simple. Sont considérées comme FAUSSES ("falsy") :
    - False et None
    - le zéro de chaque type numérique : 0, 0.0
    - toutes les collections VIDES : "", [], (), {}, set() (cf. chap. 25)

Tout le reste est considéré comme VRAI ("truthy") : n'importe quel nombre non
nul (même négatif), n'importe quelle chaîne non vide (même " " ou "False" !),
n'importe quelle liste non vide (même [0] ou [False]), etc.
"""
print(bool(0))        # => False
print(bool(0.0))      # => False
print(bool(""))       # => False
print(bool([]))       # => False
print(bool({}))       # => False
print(bool(None))     # => False

print(bool(42))       # => True
print(bool(-0.5))     # => True
print(bool(" "))      # => True (un espace, ce n'est pas une chaîne vide)
print(bool("False"))  # => True (c'est une chaîne non vide !)
print(bool([0]))      # => True (une liste qui contient un élément)

# On peut donc écrire des conditions "raccourcies"…
panier = []
if not panier:
    print("Le panier est vide")  # => Le panier est vide

nom = "Ada"
if nom:
    print(f"Bonjour {nom}")      # => Bonjour Ada

"""
…ce qui est très courant en Python, et recommandé par la PEP 8 (cf. chap. 20)
pour tester si une collection est vide.

Attention au piège : "if x:" est faux aussi quand x vaut 0. Si vous voulez
tester qu'une variable n'est pas None, écrivez explicitement "if x is not
None:".
"""
quantite = 0
if quantite:
    print("Jamais affiché : 0 est considéré comme faux")
if quantite is not None:
    print("La quantité est connue : 0")  # => La quantité est connue : 0

# Piège classique avec input() (chap. 11) : input() retourne une string, et
# bool("0") vaut True, car "0" est une chaîne non vide !
print(bool("0"))       # => True
print(bool(int("0")))  # => False


# Ce que retournent vraiment "and" et "or"
###########################################

"""
On a dit au chap. 9 que "and" et "or" retournaient un booléen. C'est vrai si
on leur donne des booléens… mais en réalité, ils retournent toujours L'UN DE
LEURS DEUX OPÉRANDES (sans le convertir) :

    - "A or B" retourne A si A est "vrai", sinon B
    - "A and B" retourne A si A est "faux", sinon B

C'est la suite logique du coupe-circuit vu au chap. 9 : Python s'arrête dès
qu'il connaît le résultat, et renvoie la dernière valeur qu'il a regardée.
"""
print(0 or 5)          # => 5 (0 est faux, donc on retourne le 2e)
print(3 or 5)          # => 3 (3 est vrai, inutile de regarder la suite)
print("" or "défaut")  # => défaut
print(0 and 5)         # => 0 (0 est faux : le "and" est forcément faux)
print(3 and 5)         # => 5 (3 est vrai, c'est donc le 2e qui décide)
print(None or [] or "dernier")  # => dernier (le 1er "vrai", ou le dernier)

# Usage courant : donner une valeur par défaut
saisie = ""                       # imaginons que l'utilisateur n'a rien tapé
prenom = saisie or "Anonyme"
print(prenom)                     # => Anonyme

"""
"not", en revanche, retourne TOUJOURS un booléen :
"""
print(not 5)   # => False
print(not "")  # => True


# Égalité et identité : "==" et "is"
#####################################

"""
On a rencontré l'opérateur "is" au chap. 9 et au chap. 15 avec None. (Pour vos
propres objets, on pourra redéfinir "==" avec __eq__, cf. chap. 35.)

    - "a == b" teste si a et b ont la même VALEUR
    - "a is b" teste si a et b sont le MÊME OBJET en mémoire (même identité,
      donnée par la fonction intégrée id())

Deux listes peuvent avoir le même contenu sans être la même liste :
"""
liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
liste3 = liste1      # liste3 désigne LA MÊME liste que liste1

print(liste1 == liste2)  # => True : même contenu
print(liste1 is liste2)  # => False : deux listes distinctes en mémoire
print(liste1 is liste3)  # => True : c'est le même objet

liste3.append(4)
print(liste1)            # => [1, 2, 3, 4] : modifier liste3 modifie liste1 !
print(liste2)            # => [1, 2, 3]

"""
IMPT : utilisez "is" UNIQUEMENT pour comparer à None (et éventuellement à
True/False). Pour comparer des nombres ou des chaînes, utilisez toujours "==" :
le résultat de "is" sur ces valeurs dépend de détails internes de Python.
"""


# all() et any()
#################

"""
Ces deux fonctions opèrent sur des listes de booléens (chap. 16).

Elles permettent de faire des "and" ou des "or" sur une liste d'éléments
contenant autant de valeurs que l'on veut :
    - all(liste) retournera True si tous les éléments de la liste passée en
      paramètre valent True, et False sinon
    - any(liste) retournera True si au moins un élément de la liste vaut True
"""
li = [True, False, 2 == 2]
print(all(li))  # => False, car il y a au moins un False
print(any(li))  # => True, car il y a au moins un True

# all() est donc un "and" géant, et any() un "or" géant :
print(all(li) == (True and False and 2 == 2))  # => True
print(any(li) == (True or False or 2 == 2))    # => True

# Elles acceptent n'importe quelle collection (tuple, string…), et utilisent la
# conversion en booléen vue plus haut
print(all((1, 2, 3)))     # => True : aucun zéro
print(all([1, 0, 3]))     # => False : 0 est "faux"
print(any(["", "", "a"])) # => True : "a" est une chaîne non vide

# Cas particulier des listes vides : all([]) vaut True (aucun élément n'est
# faux) et any([]) vaut False (aucun élément n'est vrai)
print(all([]))  # => True
print(any([]))  # => False

# Exemple : vérifier que toutes les notes sont valides
notes = [12, 15, 21, 8]
notes_valides = []
for n in notes:
    notes_valides.append(0 <= n <= 20)
print(notes_valides)       # => [True, True, False, True]
print(all(notes_valides))  # => False : la note 21 est invalide
# (on verra au chap. 23 comment écrire ça en une ligne, avec les compréhensions)


# Les opérateurs bit à bit
###########################

"""
Il arrive qu'on ait besoin de manipuler directement les bits constituant les
nombres, par exemple dans la programmation bas niveau, la cryptographie, la conception de protocoles réseau…

On utilise alors les opérateurs bit à bit (ou bitwise), pour effectuer des opérations comme le décalage de bits, l'ET, l'OU, le OU exclusif, etc.
"""

# Ex :
a = 0b0101  # (5 en décimal, cf. chap. 6 pour la notation binaire)
b = 0b0011  # (3 en décimal)

# bin() affiche un nombre en binaire (cf. chap. 6)
print(bin(a), bin(b))  # => 0b101 0b11

"""
Le principe : on pose les deux nombres en binaire l'un au-dessus de l'autre, et
on applique l'opération booléenne colonne par colonne (1 = True, 0 = False) :

        0101   (a = 5)
    &   0011   (b = 3)
    --------
        0001   (= 1)
"""

"""
    1. Le ET bitwise (&) retourne un nombre dont chaque bit est le résultat de
    l'opération ET entre les bits correspondants de deux nombres (= "les deux
    bits sont activés en même temps")
"""
print(a & b)  # => 1 (0001 en binaire)


"""
    2. Le OU Bitwise (|) fait la même chose avec l'opération OU (= "l'un ou
    l'autre est activé")
"""
print(a | b)  # => 7 (0111 en binaire)


"""
    3. Le OU exclusif Bitwise (^) fait la même chose avec l'opération OU
    exclusif (= "l'un ou l'autre est activé mais pas les deux")
"""
print(a ^ b)  # => 6 (0110 en binaire)


"""
    4. Le décalage à gauche (<<) ou à droite (>>) déplace les bits d'un nombre
    vers la gauche ou la droite, remplissant les positions libres avec des zéros.
"""
print(a << 1)  # => 10 (binaire: 1010)
print(a >> 1)  # => 2 (binaire: 0010)

# Décaler de n bits vers la gauche revient à multiplier par 2 ** n, et vers la
# droite à faire une division entière par 2 ** n (cf. chap. 4)
print(3 << 4, 3 * 2 ** 4)    # => 48 48
print(100 >> 2, 100 // 4)    # => 25 25


"""
    5. Le NON bitwise (~) inverse tous les bits. À cause de la façon dont Python
    représente les entiers négatifs ("complément à deux"), ~x vaut toujours
    -x - 1 :
"""
print(~a)  # => -6
print(~0)  # => -1

"""
IMPT : ne confondez pas "&" et "and", "|" et "or", "~" et "not" ! Sur des
booléens, & et | donnent le même résultat que and et or, mais ils n'ont PAS
de coupe-circuit, et ils sont plus prioritaires que les comparaisons :
"x > 1 & x < 5" se lit "x > (1 & x) < 5" ! Utilisez and, or et not pour vos
conditions.

(Vous rencontrerez pourtant & et | avec numpy et pandas, pour combiner des
conditions sur des tableaux entiers : il faudra alors bien parenthéser.)
"""
print(True & False, True | False)  # => False True
x = 6
print(x > 1 & x < 5)       # => True (!) car évalué comme x > (1 & x) < 5,
#                            càd 6 > 0 < 5
print((x > 1) & (x < 5))   # => False avec des parenthèses (6 n'est pas < 5)
print(x > 1 and x < 5)     # => False : le plus simple, avec "and"


"""
Quelques usages :

    1. On peut utiliser l'opérateur & pour masquer ou extraire des portions
       spécifiques de bits dans un nombre.

Ainsi pour extraire les 4 bits de droite d'un nombre, on fera :
"""
nomb = 0b11101
mask = 0b01111
print(nomb & mask)  # => 13 (binaire: 01101), seuls les 4 bits à droite sont gardés

"""
    Et avec | , on peut "allumer" un bit. Exemple classique : les droits d'un
    fichier sous Linux (lecture = 4, écriture = 2, exécution = 1)
"""
LECTURE = 0b100
ECRITURE = 0b010
EXECUTION = 0b001

droits = LECTURE | ECRITURE      # on allume deux bits
print(bin(droits))               # => 0b110
print(droits & ECRITURE != 0)    # => True : le bit "écriture" est allumé
print(droits & EXECUTION != 0)   # => False : le bit "exécution" est éteint


"""
    2. On peut aussi vérifier facilement la parité d'un nombre avec & :
"""
def is_even(n):
    return n & 1 == 0

print(is_even(10))  # => True
print(is_even(7))   # => False

"""
    3. Enfin, l'opérateur XOR peut être utilisé pour échanger les valeurs de
       deux variables sans utiliser de variable temporaire.
"""
a = 10
b = 7

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)  # => 7 10

# En pratique, Python propose une syntaxe avec des tuples qui est encore
# plus simple (cf. chap. 17) :
a, b = b, a
print(a, b)  # => 10 7

