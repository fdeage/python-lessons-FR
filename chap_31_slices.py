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
#  Chap. 31     #  Slices                                                      #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Syntaxe
#  - Indexation négative
#  - Exemples de Slices
#  - Pas (Step) dans les Slices
#  - Slices avec d'autres types construits
#  - Copie de séquences avec slices
#  - Conclusion
#
############################################

# TODO

"""
Les slices sont une technique pour extraire des portions de séquences (listes,
tuples, chaînes de caractères) en utilisant des indices de début, d'arrêt et,
éventuellement, des indices de pas.

Les slices permettent de travailler de manière efficace avec de grandes
quantités de données sans avoir à créer des copies inutiles en mémoire.
"""

# Syntaxe des Slices
#####################

"""
La syntaxe générale d'un slice est la suivante :

sequence[begin:stop:step]

Mais on peut aussi trouver les séquences suivantes :
sequence[begin:]
sequence[:stop]
sequence[begin:stop]

begin : L'indice de départ (inclusif).
stop : L'indice d'arrêt (non inclusif).
step (facultatif) : Le pas, c'est-à-dire le nombre d'éléments à sauter entre
chaque élément inclus.
"""

ma_liste = [i for i in range(10)]
print(ma_liste)  # => [0, 1, 2, …, 9]

# Slice de l'indice 2 à l'indice 5 (les indices 5 et 6 ne sont pas inclus)
print(ma_liste[2:6])  # => [2, 3, 4, 5]

# Slice avec un pas de 2
print(ma_liste[1:9:2])  # => [1, 3, 5, 7]

# Slice complète, identique à la liste initiale
print(ma_liste[:])  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


copie_liste = ma_liste[:]  # Crée une copie de ma_liste
copie_liste[0] = 100
print(copie_liste[0])  # => 100 (la liste originale est inchangée)
print(ma_liste[0])     # => 1 (la liste originale est inchangée)


# Indexation négative
#######################

"""
En Python, vous pouvez utiliser des indices négatifs pour compter à partir de la fin de la séquence. Par exemple, -1 désigne le dernier élément, -2 l'avant-dernier, et ainsi de suite.
"""
print(ma_liste[-3:-1])  # => [7, 8]


# Slices d'autres types construits
###################################

# Slices d'un tuple
mon_tuple = (10, 20, 30, 40, 50)
print(mon_tuple[1:4])  # => (20, 30, 40)


# Slices d'une string
ma_chaine = "Python est génial"
print(ma_chaine[7:12])  # => 'est g'

# Il n'y a pas de slice sur les dictionnaires…
try:
    mon_dict = {'a': 1, 'b': 2}
    mon_dict[:1] # => Lève une TypeError: unhashable type: 'slice'
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# …ni sur les ensembles :
try:
    mon_set = {'a', 'b'}
    mon_set[:1] # => Lève une TypeError: 'set' object is not subscriptable
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
