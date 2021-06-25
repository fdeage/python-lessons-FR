################################################################################
#                                                                              #
#  NNNN    NNN    SSSSSS.   IIIII   (inspiré de https://learnxinyminutes.com)  #
#  NNNNN   NNN  SSSS  SSSS   III                                               #
#  NNNNNN  NNN  SSSS         III    Licence : CC BY-SA 4.0 FR                  #
#  NNNNNNN NNN   SSSSSS      III    Félix Déage - MMXXI                        #
#  NNN NNNNNNN      SSSSS    III                                               #
#  NNN  NNNNNN        SSSS   III    Cours Python - 1ère - v.3.4                #
#  NNN   NNNNN  SSSS  SSSS   III                                               #
#  NNN    NNNN   SSSSSSSS   IIIII                                              #
#                                                                              #
################################################################################
#               #                                                              #
#  Part. V      #  variables - saisie utilisateur                              #
#               #                                                              #
################################################################################

#######################################
#                                     #
# 10. Variables I : valeurs et types  #
# 11. Saisie utilisateur              #
#                                     #
#######################################

#######################################
# 10. Variables I : valeurs et types  #
#######################################
#
#  - Déclarer une variable
#  - Conventions de nommage
#  - Variables et types de valeurs
#  - Lire et modifier une variable
#  - HP : affectation multiple
#
#######################################

# Déclarer une variable
########################

"""
Une variable est un espace mémoire où l'utilisateur peut stocker une valeur.
Cet espace mémoire est nommé par l'utilisateur pour pouvoir être référencé
plus tard.

L'utilisateur peut ensuite lire le contenu de la variable et la modifier
pendant l'exécution du programme.
"""


# Conventions de nommage
#########################

"""
On peut nommer sa variable comme on le souhaite, ou presque. La convention
Python est de nommer ses variables avec des minuscules_et_underscores, et sans
accents.
"""
une_belle_variable = 5  # 👍
uneVariableMoche = 2    # moche
uNeVrAIEMocheté = 7     # atroce : jamais d'accents dans vos noms de variables

# Exception : on utilisera des capitales pour les variables globales (voir
# chap. 19)
VARIABLE_GLOBALE = "Des majuscules partout !"

# Python accepte tous les caractères pour les variables, mais il est
# déconseillé de s'écarter des caractères ASCII : prenez l'habitude d'écrire
# avec les 26 lettres minuscules, les 10 chiffres, et les underscore ("_")
àêïœú = 34              # ça fonctionne mais c'est moche

"""
Pourquoi est-ce dangereux ? Parce que ces caractères ne font pas partie du jeu
de caractères "ASCII" (American Standard Code for Information Interchange) :
ce jeu est composé d'une centaine de caractères "de base" garantis d'être
reconnus partout.
"""


# Variables et types de valeurs
################################

# Une variable peut contenir tous les types proposés par Python :
un_super_entier = 3                      # => int
un_super_flottant = 46.2                 # => float
une_super_chaine_de_caractere = "pouet"  # => string
un_super_booleen = False                 # => boolean
une_super_liste = [True, 46.2, "pouet"]  # => list

# On rappelle que les int peuvent conserver des nombres très élevés
entier_gigantesque = 9999999999999999999999999999999
print(entier_gigantesque)  # => 9999999999999999999999999999999


# Lire et modifier une variable
################################

# On peut écrire dans une variable (y ranger une valeur), puis plus tard aller
# modifier cette valeur.
nombre_voitures = 4
nombre_voitures += 1
nombre_voitures  # => 5

# Tenter d'accéder à une variable non-définie soulève une exception.
try:
    une_variable_inconnue  # => NameError
except NameError as err:
    print(f"1: (Sans ce try: ... except ..., cette ligne créerait : {err})")

"""
Note : l'affectation utilise le symbole "=", mais il est différent du "=" en
mathématiques : c'est un égal d'affectation.
"""

# Ainsi, cette équation n'a aucune solution en mathématiques...
nombre_voitures = nombre_voitures + 1
# ...mais en Python c'est une expression tout à fait valide, qui veut dire :
# ajoute 1 à la variable nombre_voitures.

# Note : on peut utiliser un raccourci pour l'expression précédente grâce à
# l'opérateur "+="
nombre_voitures += 7  # ajoute 7 à nombre_voitures

# IMPT : on dit qu'on "incrémente" un int quand on lui ajoute 1
nb_girafes = 5
nb_girafes += 1   # on incrémente la variable nb_girafes

# HP : les raccourcis fonctionnent aussi avec "-=", "*=" et "/=".
nombre_voitures *= 2  # multiplie nombre_voitures par 2
nombre_voitures -= 5  # enlève 5 à nombre_voitures


# HP : affectation multiple
############################

"""
Il est possible d'affecter plusieurs variables à la fois en séparant les
valeurs à affecter, et les variables, par des virgules
"""
a, b, c = 1, 2, 3
print(a) # => 1
print(b) # => 2
print(c) # => 3

# On verra plus loin que la valeur à droite s'appelle un p-uplet (chap. 17).


#######################################
# 11. Saisie utilisateur              #
#######################################
#
#  - La fonction input()
#  - Gestion d'erreurs de conversion
#
#######################################

# La fonction input()
######################

"""
On utilise la fonction intégrée input() pour demander à l'utilisateur de
saisir une valeur, qui sera ensuite retournée par input().
Cette valeur sera TOUJOURS une chaîne de caractères.
"""

# Ici la réponse de l'utilisateur sera stockée dans la variable gout
gout = input("> Tu aimes les framboises à la moutarde ? ")
type(gout)  # => <class 'string'>

# Pour travailler avec des nombres, il faudra convertir cette valeur.
# Si un entier est attendu, on utilisera int()
nombre_oreilles = int(input("> Combien d'oreilles as-tu ? "))
type(nombre_oreilles)  # => <class 'int'>

# Si l'utilisateur saisit un nombre décimal d'oreilles, on aura une
# erreur.
try:
    "> Combien d'oreilles as-tu ? "
    int("4.3")  # => ValueError: invalid literal for int()
#                                            with base 10: '4.3'
except ValueError as err:
    print(f"2: (Sans ce try: ... except ..., cette ligne créerait : {err})")

# Il faudra utiliser float() si la réponse attendue est un décimal/réel
taille = float(input("> Combien mesures-tu (en m) ? "))

"> Combien mesures-tu (en m) ? "
taille = float("1.74")
taille  # => 1.74
type(taille)  # => <class 'float'>

"""
Note : la fonction raw_input() ne sert que pour Python2, elle n'est plus
utilisée en Python3
"""


# Gestion d'erreurs de conversion
##################################

# Attention, tenter une conversion avec int() ou float() peut créer une erreur
try:
    float(input("> Entrer un float valide : "))
    "> Entrer un float valide : "
    float("3,25")
except ValueError:
    pass
# => ValueError: could not convert string to float: '3,25'

try:
    float(input("> Entrer un float valide : "))
    "> Entrer un int valide : "
    int(0.2)
# => ValueError: invalid literal for int() with base 10: '0.2'
except ValueError as err:
    print(f"3: (Sans ce try: ... except ..., cette ligne créerait : {err})")
