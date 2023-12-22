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
#  Chap. 5      #  Ordre des opérations (précédence), whitespace               #
#               #                                                              #
################################################################################
#
#  - Précédence
#  - Whitespace
#  - Espaces ou tabulations ?
#
###################################

# Précédence
#############

"""
Une expression est une combinaison de calculs qui peut être évaluée pour
retourner une valeur.
"""
print(2 + 3)  # => l'expression "2 + 3" est évaluée et retourne 5

"""
Dans une expression, l'ordre dans lequel les opérations sont évaluées par
Python (on appelle cela la "précédence") suit celui des opérateurs mathématiques
"""
print(2 + 3 * 6)    # => 2 + 18 => 20
print((2 + 3) * 6)  # => 5 * 6  => 30

"""
IMPT : voici l'ordre décroissant d'évaluation des opérations :
    1. exponentiation (puissance)
    2. les opérateurs *, /, //, and %, de gauche à droite
    3. les opérateurs + et -, de gauche à droite
    4. les opérateurs de comparaison, inégalité et inégalité
    5. opérateur d'assignation (a = 3)
    6. in, not in
    7. and, or, not
"""

# On peut, bien sûr, utiliser des parenthèses pour changer cette précédence
print((5 - 1) * ((7 + 1) / (3 - 1)))  # => 16.0

# Whitespace
#############

"""
Le whitespace ("espace vide") désigne tous les caractères qui servent à
espacer les mots ou les lignes les uns des autres : espaces, tabulations,
sauts de ligne, etc.

À la différence de beaucoup de langages, le whitespace en Python peut changer
le sens du programme : on dit qu'il est "sémantique" (il porte une
signification).
"""
# Exemple :
a = 2
if a + 1 == 3:
    print("a = 2")
print("pouet")
"""
Dans le programme ci-dessus, ce sont les espaces en début de ligne qui
indiquent que le premier print() est "dans" le "if". On verra que le
whitespace en DÉBUT de ligne est particulièrement important en Python.
"""

# Les espaces et tabulations ("whitespace") en milieu de ligne n'importent pas
4 - 3  # C'est la présentation recommandée mais…
4- 3   # … fonctionne aussi
4 -3   # … fonctionne aussi
4            -   3  # … aussi !

# Débat : espaces ou tabulations ?
###################################

"""
Il y a parfois confusion entre tabulations et espaces multiples en début de
ligne. Il est fortement conseillé de ne jamais mélanger les deux et de s'en
tenir à 4 espaces pour les tabulations.

La plupart des bons éditeurs de texte proposent d'afficher le whitespace pour
repérer d'un coup d'oeil celui qui est utilisé (sur Sublime Text, c'est la
ligne :
"draw_white_space": "all"
dans votre fichier de configuration).

La plupart des bons éditeurs de texte proposent aussi des plugins pour
bien formater automatiquement votre code. Vous les découvrirez par vous-même !
"""

