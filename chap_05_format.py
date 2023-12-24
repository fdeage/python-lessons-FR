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
#  Chap. 5      #  Wwhitespace et formattage                                   #
#               #                                                              #
################################################################################
#
#  - Whitespace
#  - Espaces ou tabulations ?
#  - Formatter son code
#
###################################

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
tenir à 4 espaces pour les tabulations. C'est ce que recommande la norme
officielle dite "PEP-8" (cf. https://peps.python.org/pep-0008).

La plupart des bons éditeurs de texte proposent d'afficher le whitespace pour
repérer d'un coup d'oeil celui qui est utilisé (sur Sublime Text, c'est la
ligne :
"draw_white_space": "all"
dans votre fichier de configuration).

La plupart des bons éditeurs de texte proposent aussi des plugins pour formater
automatiquement votre code. Vous les découvrirez par vous-même !
"""


# Formatter son code
#####################

# TODO
