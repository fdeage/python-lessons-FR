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
#  Chap. 25     #  Types construits IV : les ensembles                         #
#               #                                                              #
################################################################################
#
#  - Usage et propriétés
#  - Opérations sur les ensembles
#  - Cas d'usage : dédoublonner et tester l'appartenance
#  - Exemple avec les anagrammes
#  - Logique ensembliste
#  - Bonus : les frozensets
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
    - les valeurs ne sont pas ordonnées à l'intérieur de l'ensemble

IMPT : comme l'ordre n'est pas garanti, l'affichage d'un ensemble peut varier
d'une exécution à l'autre (surtout avec des strings). Les résultats indiqués
après "=>" dans ce chapitre peuvent donc apparaître dans un autre ordre chez
vous : c'est normal.
"""

# On utilise une syntaxe qui ressemble à celle des dictionnaires… sauf
# qu'il n'y a que des clés !
un_ensemble = {1, 1, 2, 2, 3, 4}
print(un_ensemble)  # => {1, 2, 3, 4} (les doublons "sautent")

# Comme {} désigne déjà le dictionnaire vide, on crée un set vide avec set()
ensemble_vide = set()
print(type({}))             # => <class 'dict'>
print(type(ensemble_vide))  # => <class 'set'>
print(ensemble_vide)        # => set()

# On peut aussi créer un ensemble à partir de n'importe quel itérable
# (cf. chap. 23) avec la fonction set() :
print(set([3, 1, 3, 2]))    # => {1, 2, 3}
print(len(set("abracadabra")))  # => 5 (les lettres a, b, r, c, d)

# Un set peut stocker presque n'importe quel type de valeur…
ensemble_varie = {"abc", 13, False, 4.2}

# …sauf les habituelles valeurs à problèmes, mutables, comme les listes et les
# dictionnaires ("non-hashable values", cf. chap. 18 : ce sont les mêmes
# restrictions que pour les clés de dictionnaires)
ensemble_ok = {(1, 2), 1}  # valide car les tuples sont immuables

try:
    ensemble_ko = {[1, 2], 1}  # => TypeError: unhashable type: 'list'
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# Comme l'ensemble n'est pas ordonné, ses éléments n'ont pas d'indice : on ne
# peut pas écrire un_ensemble[0].
try:
    un_ensemble[0]
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Attention : 1 et True (ainsi que 0 et False) sont considérés comme égaux par
Python (cf. chap. 21) : ils ne peuvent donc pas cohabiter dans un ensemble.
"""
print({1, True, 0, False})  # => {0, 1}

"""
Deux ensembles sont égaux s'ils contiennent les mêmes éléments, quel que soit
l'ordre dans lequel on les a écrits :
"""
print({1, 2, 3} == {3, 2, 1})  # => True
print([1, 2, 3] == [3, 2, 1])  # => False (pour les listes, l'ordre compte)


# Opérations sur les ensembles
###############################

#   1. On unit un ensemble à un autre avec .union()
set1 = {"1", "2" , "3"}
set2 = {1, 2, 3}
print(set1.union(set2))  # => {1, 2, 3, '1', '2', '3'} (ordre non garanti)
# Note : "1" (une string) et 1 (un int) sont deux valeurs différentes !

#   2. On peut bien sûr utiliser len() sur un ensemble
print(len(un_ensemble))  # => 4

#   3. On utilise la méthode .add() pour ajouter un élément à un set…
un_ensemble.add(5)
print(un_ensemble)       # => {1, 2, 3, 4, 5}
print(len(un_ensemble))  # => 5

# Les sets ne peuvent pas avoir de doublons (c'est leur intérêt : on a la
# garantie que chaque élément est unique)
un_ensemble.add(5)
print(un_ensemble)       # => toujours {1, 2, 3, 4, 5}
print(len(un_ensemble))  # => toujours 5

# … et .update() pour ajouter tous les éléments d'un itérable
un_ensemble.update([6, 7, 1])
print(un_ensemble)       # => {1, 2, 3, 4, 5, 6, 7}

#   4. On vérifie la présence d'un objet dans un set avec "… in …"
print(2 in un_ensemble)        # => True
print(149 in un_ensemble)      # => False
print(149 not in un_ensemble)  # => True

#   5. On enlève un élément avec la méthode .remove()
un_ensemble.remove(7)
print(un_ensemble)  # => {1, 2, 3, 4, 5, 6}

# … qui soulève une KeyError si l'élément n'existe pas
try:
    un_ensemble.remove(37)
except KeyError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# Note : pour enlever une valeur sans risquer de soulever une erreur, on peut
# utiliser la méthode .discard()
un_ensemble.discard(37)  # => rien ne se passe si 37 n'est pas dans le set
un_ensemble.discard(6)
print(un_ensemble)       # => {1, 2, 3, 4, 5}

# .pop() retire et retourne un élément "au hasard" (en fait, un élément
# quelconque : on ne choisit pas lequel)
element = un_ensemble.pop()
print(element)       # => 1 (en pratique souvent le plus petit int, mais ce
                     #       n'est pas garanti)
un_ensemble.add(element)

#   6. On peut itérer sur les valeurs d'un set comme n'importe quel itérable
#      (dans un ordre non garanti)
for x in un_ensemble:
    print(x)
"""
1
2
3
4
5
"""

#   7. Pour obtenir les éléments dans l'ordre, on utilise sorted(), qui
#      retourne une liste triée (cf. chap. 24)
print(sorted({"pomme", "kiwi", "abricot"}))  # => ['abricot', 'kiwi', 'pomme']

#   8. On peut créer un ensemble avec une compréhension (cf. chap. 23)
print({x % 3 for x in range(10)})  # => {0, 1, 2}

#   9. Enfin on utilise la méthode .clear() pour vider le set
un_ensemble.clear()
print(un_ensemble)  # => set() (et non {}, qui est le dictionnaire vide)


# Cas d'usage : dédoublonner et tester l'appartenance
######################################################

"""
Les deux usages les plus fréquents des ensembles en pratique :

    1. IMPT : supprimer les doublons d'une liste. On convertit la liste en
       ensemble, puis (si besoin) de nouveau en liste. Attention : l'ordre de
       départ est perdu.
"""
visiteurs = ["ana", "bob", "ana", "chloé", "bob", "ana"]
uniques = set(visiteurs)
print(len(uniques))     # => 3 visiteurs différents
print(sorted(uniques))  # => ['ana', 'bob', 'chloé']

"""
    2. Tester très rapidement si un élément fait partie d'une grande
       collection. Pour une liste, "in" doit parcourir les éléments un par un
       (c'est lent si la liste est longue) ; pour un ensemble, Python sait
       directement où chercher grâce au "hash" de la valeur : la recherche est
       quasi instantanée, quelle que soit la taille de l'ensemble.
"""
mots_interdits = {"zut", "flûte", "crotte"}
phrase = "zut alors j'ai oublié mes clés"
for mot in phrase.split():
    if mot in mots_interdits:
        print(f"Mot interdit : {mot}")  # => Mot interdit : zut

"""
En contrepartie, un ensemble prend un peu plus de place en mémoire qu'une
liste et ne conserve ni l'ordre ni les doublons. On choisira donc :
    - une liste quand l'ordre ou les doublons comptent,
    - un ensemble quand seule compte la présence ou l'absence d'un élément.
"""


# Exemple avec les anagrammes
##############################

# Les ensembles permettent de dire très rapidement si deux strings utilisent
# les mêmes lettres…
def ont_memes_lettres(s1, s2):
    return set(s1) == set(s2)

# …car set() ne va garder qu'une instance de chaque lettre, et que l'ordre
# n'importe pas
print(ont_memes_lettres("elvis", "live"))   # => False (il manque le "s")
print(ont_memes_lettres("elvis", "lives"))  # => True

"""
Attention : ce n'est pas tout à fait un test d'anagramme ! Comme les ensembles
"oublient" les doublons, "aab" et "abb" seraient considérés comme anagrammes
alors qu'ils n'ont pas le même nombre de "a".
"""
print(ont_memes_lettres("aab", "abb"))  # => True… mais ce ne sont pas des anagrammes

# Un vrai test d'anagramme compare les lettres TRIÉES (cf. chap. 24) : on
# garde ainsi les doublons.
def sont_anagrammes(s1, s2):
    return sorted(s1) == sorted(s2)


print(sont_anagrammes("elvis", "lives"))  # => True
print(sont_anagrammes("aab", "abb"))      # => False
print(sont_anagrammes("chien", "niche"))  # => True

"""
Moralité : un ensemble est l'outil idéal quand on ne s'intéresse qu'à la
PRÉSENCE des éléments, pas à leur nombre.
"""


# Logique ensembliste
######################

"""
Cette partie n'est pas indispensable, mais elle est très élégante. Chaque
opération existe sous deux formes : un opérateur, et une méthode équivalente.
Les opérateurs exigent deux sets ; les méthodes acceptent n'importe quel
itérable en argument.
"""
un_ensemble = {1, 2, 3, 4, 5}
autre_ensemble = {3, 4, 5, 6}

# On trouve les "intersections" de deux sets (les éléments communs) avec
# l'opérateur "&"
print(un_ensemble & autre_ensemble)              # => {3, 4, 5}
print(un_ensemble.intersection(autre_ensemble))  # => {3, 4, 5}

# On fait l'union de plusieurs sets (tous les éléments) avec "|"
print(un_ensemble | autre_ensemble)       # => {1, 2, 3, 4, 5, 6}
print(un_ensemble.union(autre_ensemble))  # => {1, 2, 3, 4, 5, 6}

# On fait la différence de deux sets (ce qui est à gauche mais pas à droite)
# avec "-"
print({1, 2, 3, 4} - {2, 3, 5})             # => {1, 4}
print({1, 2, 3, 4}.difference([2, 3, 5]))   # => {1, 4}
# Attention, la différence n'est pas symétrique :
print({2, 3, 5} - {1, 2, 3, 4})             # => {5}

# La différence symétrique (ce qui est dans l'un OU l'autre, mais pas dans les
# deux) s'obtient avec "^"
print({1, 2, 3, 4} ^ {2, 3, 5})                       # => {1, 4, 5}
print({1, 2, 3, 4}.symmetric_difference({2, 3, 5}))   # => {1, 4, 5}

# Le set de gauche est-il un sur-ensemble du set de droite ?
print({1, 2} >= {1, 2, 3})           # => False
print({1, 2, 3}.issuperset({1, 2}))  # => True

# Le set de gauche est-il un sous-ensemble du set de droite ?
print({1, 2} <= {1, 2, 3})           # => True
print({1, 2}.issubset({1, 2, 3}))    # => True

# "<" et ">" testent l'inclusion STRICTE (sans égalité)
print({1, 2} < {1, 2})               # => False
print({1, 2} <= {1, 2})              # => True

# Deux sets sont-ils disjoints (aucun élément en commun) ?
print({1, 2}.isdisjoint({3, 4}))     # => True

"""
Ces opérations ne modifient pas les ensembles de départ : elles retournent un
NOUVEL ensemble. Pour modifier un ensemble sur place, on utilise les versions
"augmentées" (comme "+=" pour les nombres, cf. chap. 10) : "|=", "&=", "-=",
"^=".
"""
a = {1, 2, 3}
a |= {4}
print(a)  # => {1, 2, 3, 4}
a -= {1, 2}
print(a)  # => {3, 4}

# Exemple concret : comparer les inscrits de deux ateliers
python = {"ana", "bob", "chloé", "djamel"}
sql = {"bob", "djamel", "emma"}
print(sorted(python & sql))  # => ['bob', 'djamel'] (inscrits aux deux)
print(sorted(python | sql))  # => ['ana', 'bob', 'chloé', 'djamel', 'emma'] (tous)
print(sorted(python - sql))  # => ['ana', 'chloé'] (Python uniquement)
print(sorted(python ^ sql))  # => ['ana', 'chloé', 'emma'] (un seul atelier)


# Bonus : les frozensets
#########################

"""
Un set est mutable : on ne peut donc pas l'utiliser comme clé de dictionnaire,
ni le mettre dans un autre set. Python propose une version IMMUABLE de
l'ensemble : le frozenset (ensemble "gelé"). C'est au set ce que le tuple est
à la liste (cf. chap. 17).
"""
gele = frozenset([1, 2, 3])
print(gele)               # => frozenset({1, 2, 3})
print(2 in gele)          # => True
print(gele | {4})         # => frozenset({1, 2, 3, 4}) (nouvel objet)

try:
    gele.add(4)
except AttributeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# Un frozenset peut être une clé de dictionnaire ou l'élément d'un set :
ensemble_d_ensembles = {frozenset({1, 2}), frozenset({3})}
print(len(ensemble_d_ensembles))  # => 2
