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
#  Chap. 5      #  Ordre des opérations (précédence), whitespace               #
#               #                                                              #
################################################################################
#
#  - Précédence des opérateurs
#  - Whitespace
#  - Espaces ou tabulations ?
#
###################################

# Précédence des opérateurs
############################

"""
DÉFINITION :
Une EXPRESSION est une combinaison de calculs qui peut être évaluée pour
retourner une valeur.
"""
print(2 + 3)  # => l'expression "2 + 3" est évaluée et retourne 5
print(1 + 1 ==  2)  # => l'expression est évaluée et retourne True

"""
Dans une expression, l'ordre dans lequel les opérations sont évaluées par
Python (on appelle cela la "précédence") suit grosso modo celui des opérateurs
mathématiques :
"""
print(2 + 3 * 6)    # => 2 + 18 => 20
print((2 + 3) * 6)  # => 5 * 6  => 30

"""
Voici l'ordre décroissant d'évaluation des opérations :
    1. l'exponentiation (ou puissance), `**`
    2. les opérateurs `*`, `/`, `//`, and `%`, de gauche à droite
    3. les opérateurs `+` et `-`, de gauche à droite
    4. les opérateurs de comparaison, inégalité et inégalité (`==`, `!=`, `<`,
       `>`)
    5. l'opérateur d'assignation `=` (comme dans `a = 3`)
    6. `in` et `not in`
    7. `and`, `or` et `not` (cf. chap. 9)

On peut, bien sûr, utiliser des parenthèses pour changer cette précédence :
"""
print((5 - 1) * ((7 + 1) / (3 - 1)))  # => 16.0

"""
L'ordre n'est pas à connaître, il faut juste savoir qu'il y en a un. En cas
de doute, utilisez des parenthèses !

Par défaut, les opérations au sein du même niveau de précédence sont
évaluées de gauche à droite.
"""


# Whitespace
#############

"""
Le whitespace ("espace vide") désigne tous les caractères qui servent à
espacer les mots ou les lignes les uns des autres : espaces, tabulations,
sauts de ligne, etc.

À la différence de beaucoup de langages, le whitespace en Python peut changer
le sens du programme : on dit qu'il est "sémantique" (= il porte une
signification).

Exemple :
"""
a = 2
if a + 1 == 3:
    print("a = 2")
print("pouet")
"""
Dans le programme ci-dessus, ce sont les espaces en début de ligne qui
indiquent que le premier print() est "dans le if". On verra que le
whitespace en DÉBUT de ligne est particulièrement important en Python.

En revanche, les espaces et tabulations ("whitespace") en milieu de ligne
n'importent pas :
"""
4 - 3  # C'est la présentation recommandée mais…
4- 3   # … fonctionne aussi
4 -3   # … fonctionne aussi
4            -   3  # … aussi !


# Débat : espaces ou tabulations ?
###################################

"""
Il y a parfois confusion entre tabulations et espaces multiples en début de
ligne.

Une tabulation (`\t`) est un caractère spécial, différent d'une suite d'espaces.
Il sert originellement à aligner du texte sur différents curseurs de ligne.
Certains éditeurs le remplacent par des espaces, d'autres non.

Il est fortement conseillé de ne JAMAIS mélanger espaces et tabulations. Mieux,
de ne jamais utiliser de tabulations DU TOUT, et d'utiliser 4 espaces pour
toutes les identations (cf. https://peps.python.org/pep-0008/#indentation).

La plupart des bons éditeurs de texte proposent une option pour afficher le
whitespace, afin de repérer d'un coup d'oeil celui qui est utilisé (sur Sublime
Text, c'est la ligne : "draw_white_space": "all" dans votre fichier de
configuration).

La plupart des bons éditeurs de texte proposent aussi des plugins pour
bien formater automatiquement votre code : ils intègrent des formatteurs comme
black, autopep8, yapf... Vous les découvrirez par vous-même !
"""
