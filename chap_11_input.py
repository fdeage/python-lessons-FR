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
#  Chap. 11     #  Saisie utilisateur                                          #
#               #                                                              #
################################################################################
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
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

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
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
