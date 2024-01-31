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
#  Chap. 25     #  Types construits IV : les ensembles                         #
#               #                                                              #
################################################################################
#
#  - Usage et propriétés
#  - Opérations sur les ensembles
#  - Exemple avec les anagrammes
#  - Logique ensembliste
#
#####################################

# Usage et propriétés
######################

"""
En Python, les ensembles (sets) servent à stocker des ensembles non-ordonnés
de valeurs. Le but est de travailler sur des ensembles au sens mathématique
(appartenance ou non, inclusion, différence). On ne se souciera pas de l'ordre
ni des doublons.

Deux propriétés importantes :
    - un ensemble ne peut avoir qu'une seule occurrence de chaque valeur
    - les valeurs ne sont pas triées à l'intérieur de l'ensemble
"""

# On utilise une syntaxe qui resssemble à celle des dictionnaires… sauf
# qu'il n'y a que des clés !
un_ensemble = {1, 1, 2, 2, 3, 4}  # => {1, 2, 3, 4} (les doublons "sautent")

# Comme {} désigne déjà le dictionnaire vide, on crée un set vide avec set()
ensemble_vide = set()

# Un set peut stocker presque n'importe quel type de valeur…
ensemble_varie = {"abc", 13, False, 4.2}

# …sauf les habituelles valeurs à problèmes, mutables, comme les listes et les
# dictionnaires ("non-hashable values")
ensemble_ok = {(1, 2), 1}  # valide car les tuples sont immuables

try:
    ensemble_ko = {[1, 2], 1}  # => TypeError: unhashable type: 'list'
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Opérations sur les ensembles
###############################

#   1. On unit un ensemble à un autre avec .union()
set1 = {"1", "2" , "3"}
set2 = {1, 2, 3}
print(set1.union(set2))  # => {1, 2, 3, '1', '2', '3'}

#   2. On peut bien sûr utiliser len() sur un ensemble
len(un_ensemble)       # => 4

#   3. On utilise la méthode .add() pour ajouter un élément à un set…
un_ensemble.add(5)     # => {1, 2, 3, 4, 5}
len(un_ensemble)       # => 5

# Les sets ne peuvent pas avoir de doublons (c'est leur intérêt : on a la
# garantie que chaque élément est unique
un_ensemble.add(5)     # toujours {1, 2, 3, 4, 5}
len(un_ensemble)       # => toujours 5

#   4. On vérifie la présence d'un objet dans un set avec "… in …"
2 in un_ensemble    # => True
149 in un_ensemble  # => False

#   5. On enlève un élément avec la méthode .remove()
un_ensemble.remove(5)  # {1, 2, 3, 4}

try:
    un_ensemble.remove(37)
except KeyError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# Note : pour enlever une valeur sans risquer de soulever une erreur, on peut
# utiliser laméthode .discard()
un_ensemble.discard(37)  # => rien ne se passe si 37 n'est pas dans le set

# On peut itérer sur les valeurs d'un set comme n'importe quel itérable
for x in un_ensemble:
    print(x)

# Enfin on utilise la méthode .clear() pour vider le set
un_ensemble.clear()
un_ensemble   # => {}


# Exemple avec les anagrammes
##############################

# Les ensembles pernettent de dire très rapidement si deux strings sont des
# anagrammes (càd sont constituées des mêmes lettres)…
def sont_anagrammes(s1, s2):
    return set(s1) == set(s2)

# …car set() ne va garder qu'une instance de chaque lettre, et que l'ordre
# n'importe pas
sont_anagrammes("elvis", "live") # => False
sont_anagrammes("elvis", "lives") # => True


# HP : logique ensembliste
###########################

# On trouve les "intersections" de deux sets avec l'opérateur "&""
autre_ensemble = {3, 4, 5, 6}
un_ensemble & autre_ensemble  # => {3, 4, 5}

# On fait l'union de plusieurs sets avec "|"
un_ensemble | autre_ensemble  # => {1, 2, 3, 4, 5, 6}

# On fait la différence de deux sets avec "-"
{1, 2, 3, 4} - {2, 3, 5}      # => {1, 4}

# Le set de gauche est-il un sur-ensemble du set de droite ?
{1, 2} >= {1, 2, 3}           # => False

# Le set de gauche est-il un sous-ensemble du set de droite ?
{1, 2} <= {1, 2, 3}           # => True
