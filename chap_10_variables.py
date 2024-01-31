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
#  Chap. 10     #  Variables I : valeurs et types                              #
#               #                                                              #
################################################################################
#
#  - Déclarer une variable
#  - Variables et types de valeurs
#  - Lire et modifier une variable
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
L'utilisateur peut ensuite lire le contenu de la variable et le modifier
pendant l'exécution du programme.

Lecture du contenu avec print() :
"""
print(nombre_voitures)  # => 2

# On peut ensuite modifier la variable (l'ancien contenu est écrasé) :
nombre_voitures = 5
print(nombre_voitures)  # => 5

"""
Une variable doit être affectée (avec =) avant d'être utilisée : l'affectation
doit être "au-dessus" de l'utilisation.

Tenter d'accéder à une variable non-définie soulèvera une exception :
"""
try:
    print(une_variable_inconnue)  # => NameError
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Variables et types de valeurs
################################

# Une variable peut contenir tous les types proposés par Python :
un_super_entier = 3                      # => int
un_super_flottant = 46.2                 # => float
une_super_chaine_de_caractere = "pouet"  # => string
un_super_booleen = False                 # => boolean
une_super_liste = [True, 46.2, "pouet"]  # => list
# ... et beaucoup d'autres.

# On rappelle que les int peuvent conserver des nombres très élevés
entier_gigantesque = 9999999999999999999999999999999
print(entier_gigantesque)  # => 9999999999999999999999999999999


# Lire et modifier une variable
################################

"""
On a vu que l'on pouvait écrire dans une variable (y ranger une valeur), puis
plus tard aller modifier cette valeur.

Il n'y a pas de limite au nombre de réécriture possible. On peut aussi changer
le type de valeur stockée.
"""
nombre_voitures = 7.51
nombre_voitures = True
nombre_voitures = 2
# ...

"""
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
…mais en Python c'est une expression tout à fait valide, qui veut dire :
ajoute 1 à la variable nombre_voitures.
"""

"""
On peut utiliser un raccourci pour l'expression précédente grâce à
l'opérateur "+="
"""
nombre_voitures += 7  # ajoute 7 à nombre_voitures

# Ces raccourcis fonctionnent aussi avec "-=", "*=" et "/=".
nombre_voitures *= 2  # multiplie nombre_voitures par 2
nombre_voitures -= 5  # enlève 5 à nombre_voitures
nombre_voitures /= 5  # divise nombre_voitures par 2

# Enfin, on dit qu'on "incrémente" une variable quand on lui ajoute 1
nb_girafes = 5
nb_girafes += 1   # on incrémente la variable nb_girafes


# Conventions de nommage
#########################

"""
On peut nommer sa variable comme on le souhaite, ou presque. Cela ne signifie
pas qu'il est bien de faire n'importe quoi !

Il y a deux styles principaux (ou conventions) :
    1. le "Snake Case" (minuscules et underscores),
    2. le "Camel Case" (majuscules)

Il est fortement recommandé de se tenir à un seul style. Ce tutoriel utilise la
convention "Snake Case". Quelle que soit votre convention, tenez-vous y !
(c'est le but d'une convention)
"""
une_variable_en_snake_case = 5      # 👍
une_variable_avec_un_chiffre_2 = 7  # 👍
uneVariableEnCamelCase = 7          # 👍
une_Variable_Moche = 2              # moche
uNeVrAIEMocheté = 666               # atroce

# On n'utilisera que des majuscules pour les variables globales (voir chap. 19)
VARIABLE_GLOBALE = "Des majuscules partout !"

"""
Python accepte tous les caractères pour les variables, mais il est
déconseillé de s'écarter des caractères ASCII : prenez l'habitude d'écrire
avec les 26 lettres minuscules, les 10 chiffres, et les underscore ("_")
"""
àêïœú = 34              # ça fonctionne mais c'est moche

"""
Pourquoi est-ce dangereux ? Parce que ces caractères ne font pas partie du jeu
de caractères "ASCII" (American Standard Code for Information Interchange) :
ce jeu réduit est composé d'une centaine de caractères "de base" garantis d'être
reconnus partout.
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

#   2. La fonction str() peut les transformer en string :
print(str(a))  # => '2'
print(str(b))  # => 'test'
print(str(c))  # => 'False'

# Note : print() appelle toujours str() sur les variables passées en paramètre :

#   3. La fonction dir() est extrêmement pratique : elle retourne toutes les
#      méthodes que l'on peut appeler sur l'objet a !
print(dir(a))

#   4. La fonction help() retourne une aide sur le type de l'objet
help(a)  # => Help on int object: …


# Affectation multiple
############################

"""
Il est possible d'affecter plusieurs variables à la fois en séparant les
valeurs à affecter, et les variables, par des virgules
"""
a, b, c = 1, 2, 3
print(a) # => 1
print(b) # => 2
print(c) # => 3

"""
On verra plus loin que la valeur à droite est un "tuple" (chap. 17).
"""
