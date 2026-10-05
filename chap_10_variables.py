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
#  Chap. 10     #  Variables I : valeurs et types                              #
#               #                                                              #
################################################################################
#
#  - Déclarer une variable
#  - Variables et types de valeurs
#  - Lire et modifier une variable
#  - Règles de nommage
#  - Conventions de nommage
#  - Quelques fonctions sur les variables
#  - Affectation multiple
#
##########################################

# Déclarer une variable
########################

"""
Une variable est un espace mémoire où l'utilisateur peut stocker une valeur.
Cet espace mémoire est nommé par l'utilisateur pour pouvoir être référencé
plus tard.

Ex :
"""
nombre_voitures = 2

"""
Cette ligne s'appelle une "affectation" (ou "assignation") : on affecte la
valeur 2 à la variable nommée nombre_voitures. Elle se lit de DROITE à
GAUCHE : "range la valeur 2 dans la variable nombre_voitures".

    nombre_voitures   =   2
    ^^^^^^^^^^^^^^^   ^   ^
           |          |   |
           |          |   +-- la valeur
           |          +------ le signe d'affectation
           +----------------- le nom de la variable

L'utilisateur peut ensuite lire le contenu de la variable et le modifier
pendant l'exécution du programme.

Lecture du contenu avec print() :
"""
print(nombre_voitures)  # => 2

# On peut ensuite modifier la variable (l'ancien contenu est écrasé) :
nombre_voitures = 5
print(nombre_voitures)  # => 5

"""
À droite du "=", on peut mettre n'importe quelle expression : Python calcule
d'abord la valeur de l'expression, PUIS la range dans la variable (cf. chap. 5).
"""
prix_total = 3 * 12.5 + 2
print(prix_total)  # => 39.5

# Une variable peut aussi servir à en calculer une autre :
prix_unitaire = 4
quantite = 3
prix = prix_unitaire * quantite
print(prix)  # => 12

"""
Une variable doit être affectée (avec =) avant d'être utilisée : l'affectation
doit être "au-dessus" de l'utilisation.

Tenter d'accéder à une variable non-définie soulèvera une exception :
"""
try:
    print(une_variable_inconnue)  # => NameError: name 'une_variable_inconnue'
    #                                              is not defined
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Note : une faute de frappe dans le nom d'une variable provoque exactement la
même erreur. Si vous voyez une NameError, vérifiez d'abord l'orthographe !
"""


# Variables et types de valeurs
################################

# Une variable peut contenir tous les types proposés par Python :
un_super_entier = 3                      # => int
un_super_flottant = 46.2                 # => float
une_super_chaine_de_caractere = "pouet"  # => string
un_super_booleen = False                 # => boolean
une_super_liste = [True, 46.2, "pouet"]  # => list (cf. chap. 16)
# ... et beaucoup d'autres.

# Le type d'une variable est celui de la valeur qu'elle contient :
print(type(un_super_entier))                # => <class 'int'>
print(type(un_super_flottant))              # => <class 'float'>
print(type(une_super_chaine_de_caractere))  # => <class 'str'>
print(type(un_super_booleen))               # => <class 'bool'>
print(type(une_super_liste))                # => <class 'list'>

# On rappelle que les int peuvent conserver des nombres très élevés
entier_gigantesque = 9999999999999999999999999999999
print(entier_gigantesque)  # => 9999999999999999999999999999999

"""
Note : contrairement à d'autres langages (C, Java…), on n'a pas besoin de
"déclarer" le type d'une variable en Python : il est déduit automatiquement de
la valeur. On dit que Python est un langage à "typage dynamique".
"""


# Lire et modifier une variable
################################

"""
On a vu que l'on pouvait écrire dans une variable (y ranger une valeur), puis
plus tard aller modifier cette valeur.

Il n'y a pas de limite au nombre de réécritures possibles. On peut aussi
changer le type de valeur stockée : le type de la variable change alors avec
sa valeur (c'est le "typage dynamique").
"""
nombre_voitures = 7.51
print(type(nombre_voitures))  # => <class 'float'>
nombre_voitures = True
print(type(nombre_voitures))  # => <class 'bool'>
nombre_voitures = "abc"
print(type(nombre_voitures))  # => <class 'str'>
nombre_voitures = 2
print(type(nombre_voitures))  # => <class 'int'>

"""
C'est pratique, mais cela demande de l'attention : seule la DERNIÈRE valeur
affectée compte. Si on oublie qu'une variable contient maintenant une chaîne,
on aura des surprises :
"""
variable_piege = "abc"
try:
    variable_piege + 3  # => TypeError: can only concatenate str (not "int")
    #                                    to str
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
IMPT : en pratique, gardez toujours le même type de valeur dans une variable
donnée. Une variable nommée nombre_voitures devrait contenir… un nombre !

Il peut être intéressant d'ajouter une valeur fixe à la valeur déjà présente
dans la variable. Pour cela, on peut écrire :
"""
nombre_voitures = nombre_voitures + 3
print(nombre_voitures)  # => 5 (on a ajouté 3 à la dernière valeur, 2)

"""
Note : l'affectation utilise le symbole "=", mais il est différent du "=" en
mathématiques : c'est un égal d'affectation.

Ainsi, cette équation n'a aucune solution en mathématiques…
"""
nombre_voitures = nombre_voitures + 1
"""
…mais en Python c'est une instruction tout à fait valide, qui veut dire :
"calcule nombre_voitures + 1 (soit 5 + 1), puis range le résultat (6) dans
nombre_voitures".
"""
print(nombre_voitures)  # => 6

"""
On peut utiliser un raccourci pour l'expression précédente grâce à
l'opérateur "+="
"""
nombre_voitures += 7  # ajoute 7 à nombre_voitures
print(nombre_voitures)  # => 13

# Ces raccourcis fonctionnent aussi avec "-=", "*=" et "/=".
nombre_voitures *= 2  # multiplie nombre_voitures par 2
print(nombre_voitures)  # => 26
nombre_voitures -= 5  # enlève 5 à nombre_voitures
print(nombre_voitures)  # => 21
nombre_voitures /= 5  # divise nombre_voitures par 5
print(nombre_voitures)  # => 4.2 (la division "/" donne toujours un float, cf.
#                                chap. 4)

# Ils existent aussi pour "//", "%" et "**" :
x = 17
x //= 5  # x = x // 5
print(x)  # => 3
x **= 2  # x = x ** 2
print(x)  # => 9
x %= 4   # x = x % 4
print(x)  # => 1

# Le raccourci "+=" fonctionne aussi avec les strings (concaténation) :
message = "Bonjour"
message += " tout le monde"
print(message)  # => Bonjour tout le monde

# Enfin, on dit qu'on "incrémente" une variable quand on lui ajoute 1, et
# qu'on la "décrémente" quand on lui enlève 1
nb_girafes = 5
nb_girafes += 1   # on incrémente la variable nb_girafes
print(nb_girafes)  # => 6
nb_girafes -= 1   # on décrémente la variable nb_girafes
print(nb_girafes)  # => 5

"""
Note : contrairement à d'autres langages (C, Java, JavaScript…), il n'existe
pas d'opérateur "++" ou "--" en Python. On écrit toujours "+= 1".
"""


# Règles de nommage
####################

"""
Le nom d'une variable doit respecter quelques règles, sinon Python soulève une
SyntaxError (et le fichier ne peut même pas être lancé, c'est pourquoi ces
exemples sont dans une chaîne) :
    - il ne contient que des lettres, des chiffres et des underscores ("_") :
      pas d'espace, de tiret, d'apostrophe, de point…
          nombre voitures = 2   # => SyntaxError (espace)
          nombre-voitures = 2   # => SyntaxError (Python lit une soustraction)
    - il ne commence pas par un chiffre :
          2voitures = 2         # => SyntaxError
    - il ne doit pas être un "mot-clé" réservé de Python, comme if, else,
      for, while, def, return, True, False, None, and, or, not, in, is,
      import, class…
          if = 3                # => SyntaxError
          True = 1              # => SyntaxError
"""

# Les noms sont sensibles à la casse : age et Age sont deux variables
# DIFFÉRENTES
age = 20
Age = 30
print(age)  # => 20
print(Age)  # => 30

"""
Attention : certains noms ne sont pas interdits, mais sont déjà utilisés par
des fonctions intégrées : print, str, int, float, len, type, list, input…

Si on écrit par exemple "str = 'texte'", la variable str "cache" la fonction
str(), qui ne fonctionnera plus jusqu'à la fin du programme :
    str = "texte"
    str(5)  # => TypeError: 'str' object is not callable

N'utilisez donc jamais ces noms pour vos variables !
"""


# Conventions de nommage
#########################

"""
On peut nommer sa variable comme on le souhaite, ou presque. Cela ne signifie
pas qu'il est bien de faire n'importe quoi !

Il y a deux styles principaux (ou conventions) :
    1. le "Snake Case" (minuscules et underscores),
    2. le "Camel Case" (majuscules au début de chaque mot)

Il est fortement recommandé de se tenir à un seul style. Ce tutoriel utilise la
convention "Snake Case", qui est celle recommandée par le guide de style
officiel de Python (la "PEP 8", cf. https://peps.python.org/pep-0008). Quelle
que soit votre convention, tenez-vous y ! (c'est le but d'une convention)
"""
une_variable_en_snake_case = 5      # 👍
une_variable_avec_un_chiffre_2 = 7  # 👍
uneVariableEnCamelCase = 7          # 👍 (mais pas la convention Python)
une_Variable_Moche = 2              # moche
uNeVrAIEMocheté = 666               # atroce

# On n'utilisera que des majuscules pour les variables globales (voir chap. 19)
VARIABLE_GLOBALE = "Des majuscules partout !"

"""
Choisissez surtout des noms PARLANTS, qui décrivent le contenu de la variable.
Vous (ou vos collègues) relirez votre code bien plus souvent que vous ne
l'écrirez :
"""
x = 3.5 * 4          # 👎 que représente x ?
prix_ttc = 3.5 * 4   # 👍 on comprend tout de suite

"""
Les noms d'une seule lettre (i, j, x, n…) sont réservés aux cas où leur sens
est évident : un compteur de boucle (cf. chap. 13), une coordonnée, etc.

Python accepte tous les caractères pour les variables, mais il est
déconseillé de s'écarter des caractères ASCII : prenez l'habitude d'écrire
avec les 26 lettres minuscules, les 10 chiffres, et les underscore ("_")
"""
àêïœú = 34              # ça fonctionne mais c'est moche

"""
Pourquoi est-ce dangereux ? Parce que ces caractères ne font pas partie du jeu
de caractères "ASCII" (American Standard Code for Information Interchange) :
ce jeu réduit est composé d'une centaine de caractères "de base" garantis d'être
reconnus partout. Certains claviers ne permettent pas de les taper, et certains
caractères se ressemblent à s'y méprendre (le "a" latin et le "а" cyrillique,
par exemple).

Enfin, on écrit les noms de variables en anglais dans la plupart des projets
professionnels. Ce cours utilise le français pour faciliter la lecture.
"""


# Quelques fonctions sur les variables
#######################################

# Prenons des variables toute bêtes :
a = 2
b = "test"
c = False

#   1. La fonction type() retourne leur type :
print(type(a))  # => <class 'int'>
print(type(b))  # => <class 'str'>
print(type(c))  # => <class 'bool'>

#   2. La fonction str() peut les transformer en string (cf. chap. 6) :
print(str(a))  # => 2
print(str(b))  # => test
print(str(c))  # => False
print(type(str(a)))  # => <class 'str'>

# Note : print() appelle toujours str() sur les variables passées en paramètre.
# Les deux lignes suivantes impriment donc exactement la même chose :
print(a)       # => 2
print(str(a))  # => 2

#   3. La fonction dir() est extrêmement pratique : elle retourne toutes les
#      méthodes que l'on peut appeler sur l'objet a !
print(dir(a))  # => ['__abs__', '__add__', '__and__', …] (une très longue
#                     liste)

# Essayez par exemple avec une string : vous y retrouverez les méthodes vues
# au chap. 8 (upper, lower, split, join…)
print(dir(b))  # => [… 'join', 'ljust', 'lower', …]

#   4. La fonction help() affiche une aide sur le type de l'objet :
#          help(a)  # => Help on int object: …
#      Testez-la dans l'interpréteur (cf. chap. 2) : l'aide est très longue, et
#      elle s'ouvre dans un afficheur qui bloque le programme jusqu'à ce que
#      vous appuyiez sur "q". On peut aussi demander de l'aide sur une
#      fonction précise :
#          help(len)  # => Help on built-in function len…


# Affectation multiple
#######################

"""
Il est possible d'affecter plusieurs variables à la fois en séparant les
valeurs à affecter, et les variables, par des virgules
"""
a, b, c = 1, 2, 3
print(a)  # => 1
print(b)  # => 2
print(c)  # => 3

"""
On verra plus loin que la valeur à droite est un "tuple" (chap. 17).

Il doit y avoir exactement autant de variables que de valeurs :
"""
try:
    a, b = 1, 2, 3  # => ValueError: too many values to unpack (expected 2)
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    a, b, c = 1, 2  # => ValueError: not enough values to unpack (expected 3,
    #                                got 2)
except ValueError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
L'affectation multiple permet d'échanger le contenu de deux variables en une
seule ligne. En effet, Python évalue TOUTES les valeurs de droite AVANT de
les affecter à gauche :
"""
a = 1
b = 2
a, b = b, a
print(a)  # => 2
print(b)  # => 1

"""
Dans la plupart des autres langages, il faudrait passer par une variable
temporaire :
"""
a = 1
b = 2
temporaire = a  # on met la valeur de a de côté
a = b           # a vaut maintenant 2
b = temporaire  # b récupère l'ancienne valeur de a, soit 1
print(a, b)  # => 2 1

# Enfin, on peut donner la même valeur à plusieurs variables d'un coup :
x = y = z = 0
print(x, y, z)  # => 0 0 0
