################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Félix Déage - 2026                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 25     #  Les ensembles : corrigés                                    #
#               #                                                              #
################################################################################

"""
L'ordre d'affichage d'un ensemble n'étant pas garanti, les ensembles sont
affichés triés avec sorted() (qui retourne une LISTE) dans ce corrigé.
"""


#########################
#  Usage et propriétés  #
#########################

# 1. Valeurs des expressions :
print(len({1, 2, 2, 3, 3, 3}))      # => 3
print(len(set("mississippi")))      # => 4
print(type({}))                     # => <class 'dict'>
print(type(set()))                  # => <class 'set'>
print({1, 2, 3} == {3, 1, 2})       # => True
print(len({1, True, 1.0}))          # => 1
"""
- Les doublons disparaissent : il reste 1, 2 et 3.
- "mississippi" ne contient que 4 lettres différentes : m, i, s et p.
- {} est le dictionnaire vide ; l'ensemble vide s'écrit set().
- L'ordre d'écriture ne compte pas pour comparer deux ensembles.
- 1, True et 1.0 sont égaux pour Python (1 == True == 1.0) : l'ensemble n'en
  garde qu'un seul (le premier ajouté, 1).
"""

# 2. Seules b, c et d soulèvent une erreur :
a = {(1, 2), "abc", 3.5}  # OK : un tuple est immuable, donc "hashable"
try:
    b = {[1, 2], 3}
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
ensemble = {1, 2, 3}
try:
    c = ensemble[0]  # Python 3.14 repère même {1, 2, 3}[0] AVANT l'exécution
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    d = set([[1], [2]])
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- b et d : une liste est mutable, elle ne peut pas être élément d'un ensemble
  (TypeError: unhashable type: 'list'). Pour d, c'est la même chose : set()
  essaie d'ajouter chaque sous-liste dans l'ensemble.
- c : un ensemble n'est pas ordonné, ses éléments n'ont donc pas d'indice
  (TypeError: 'set' object is not subscriptable).
"""

# 3. Lettres de "banane" :
lettres_vues = set()
for lettre in "banane":
    lettres_vues.add(lettre)
print(len(lettres_vues))     # => 3
print(sorted(lettres_vues))  # => ['a', 'b', 'e', 'n']
"""
Les "a" et "n", ajoutés plusieurs fois, ne sont gardés qu'une seule fois.
sorted() les retourne dans l'ordre alphabétique. On aurait pu écrire
directement set("banane").
"""


##################################
#  Opérations sur les ensembles  #
##################################

# 4. Pas à pas :
s = {10, 20}
s.add(30)               # s vaut {10, 20, 30}
s.add(10)               # 10 y est déjà : rien ne change
s.update([40, 20, 50])  # s vaut {10, 20, 30, 40, 50}
s.discard(99)           # 99 n'y est pas : rien ne se passe, sans erreur
s.remove(50)            # s vaut {10, 20, 30, 40}
print(len(s))           # => 4
print(25 in s, 25 not in s)  # => False True
print(sorted(s))        # => [10, 20, 30, 40]

# 5. .remove() contre .discard() :
nombres = {1, 2, 3}
try:
    nombres.remove(7)
except KeyError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
nombres.discard(7)  # aucune erreur
print(sorted(nombres))  # => [1, 2, 3]
"""
Les deux retirent un élément, mais .remove() soulève une KeyError si
l'élément est absent, alors que .discard() ne fait rien. On utilise
.discard() quand l'absence de l'élément est normale, et .remove() quand elle
signale un problème qu'on veut voir.
"""

# 6. Longueurs des mots :
phrase = "le petit chat boit du lait chaud"
longueurs = {len(mot) for mot in phrase.split()}
print(sorted(longueurs))  # => [2, 4, 5]
"""
Les mots ont pour longueurs 2, 5, 4, 4, 2, 4, 5 : l'ensemble ne garde que les
valeurs distinctes.
"""


# 7. Initiales :
def initiales(mots):
    return {mot[0].lower() for mot in mots}


print(sorted(initiales(["Pomme", "poire", "Kiwi", "abricot"])))
# => ['a', 'k', 'p']
"""
"Pomme" et "poire" donnent toutes les deux "p" une fois passées en minuscules
avec .lower() : l'ensemble ne le garde qu'une fois.
"""


#########################################################
#  Cas d'usage : dédoublonner et tester l'appartenance  #
#########################################################

# 8. Adresses différentes :
emails = ["ana@mail.fr", "bob@mail.fr", "ana@mail.fr",
          "chloe@mail.fr", "bob@mail.fr"]
uniques = set(emails)
print(len(uniques))     # => 3
print(sorted(uniques))  # => ['ana@mail.fr', 'bob@mail.fr', 'chloe@mail.fr']


# 9. Doublons :
def a_des_doublons(liste):
    return len(set(liste)) < len(liste)


print(a_des_doublons([1, 2, 3, 2]))  # => True
print(a_des_doublons([1, 2, 3]))     # => False
"""
Si l'ensemble est plus petit que la liste, c'est que des doublons ont été
supprimés lors de la conversion.
"""


# 10. Dédoublonner en conservant l'ordre :
def dedoublonner(liste):
    deja_vus = set()
    resultat = []
    for element in liste:
        if element not in deja_vus:
            resultat.append(element)
            deja_vus.add(element)
    return resultat


print(dedoublonner([3, 1, 3, 2, 1]))  # => [3, 1, 2]
"""
list(set(liste)) supprimerait bien les doublons, mais l'ordre de départ
serait perdu. Ici, la LISTE resultat garde l'ordre, et l'ENSEMBLE deja_vus
permet de tester très rapidement si un élément a déjà été rencontré. On
aurait pu tester "element not in resultat", mais ce test devient lent quand
la liste est longue.
"""

# 11. Filtrer les mots vides :
mots_vides = {"le", "la", "les", "de", "du", "un", "une", "et"}
phrase = "le chat et la souris jouent dans le jardin de la maison"
mots_utiles = [mot for mot in phrase.split() if mot not in mots_vides]
print(mots_utiles)
# => ['chat', 'souris', 'jouent', 'dans', 'jardin', 'maison']
"""
On teste "mot not in mots_vides" pour CHAQUE mot de la phrase. Avec un
ensemble, chaque test est quasi instantané ; avec une liste, Python devrait
comparer le mot à chaque mot vide un par un. Sur un vrai texte (des milliers
de mots, des centaines de mots vides), la différence est énorme. L'ordre des
mots vides et leurs doublons n'ont de toute façon aucune importance ici.
"""


#################################
#  Exemple avec les anagrammes  #
#################################

def ont_memes_lettres(s1, s2):
    return set(s1) == set(s2)


def sont_anagrammes(s1, s2):
    return sorted(s1) == sorted(s2)


# 12. Résultats :
print(ont_memes_lettres("ironique", "onirique"))  # => True
print(sont_anagrammes("ironique", "onirique"))    # => True
print(ont_memes_lettres("pas", "spa"))            # => True
print(ont_memes_lettres("papa", "pa"))            # => True
print(sont_anagrammes("papa", "pa"))              # => False
"""
"ironique" et "onirique" sont de vrais anagrammes (mêmes lettres, autant de
fois chacune). En revanche "papa" et "pa" ont les mêmes lettres, mais pas en
même nombre : ont_memes_lettres() se fait piéger, pas sont_anagrammes().
"""


# 13. Pangramme :
def est_pangramme(phrase):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(phrase.lower())


print(est_pangramme("Portez ce vieux whisky au juge blond qui fume"))
# => True
print(est_pangramme("Bonjour tout le monde"))  # => False
"""
On vérifie que l'alphabet est INCLUS dans l'ensemble des caractères de la
phrase (passée en minuscules). Les espaces et la ponctuation font partie de
set(phrase), mais ce n'est pas gênant : on teste seulement que chaque lettre
y est. On aurait aussi pu écrire :
    alphabet.issubset(phrase.lower())
car les méthodes acceptent n'importe quel itérable, ou encore :
    len(alphabet - set(phrase.lower())) == 0
"""


#########################
#  Logique ensembliste  #
#########################

a = {1, 2, 3, 4}
b = {3, 4, 5}
c = {1, 2}

# 14. Valeurs des expressions :
print(sorted(a & b))    # => [3, 4]
print(sorted(a | b))    # => [1, 2, 3, 4, 5]
print(sorted(a - b))    # => [1, 2]
print(sorted(b - a))    # => [5]
print(sorted(a ^ b))    # => [1, 2, 5]
print(c <= a)           # => True
print(c < c)            # => False
print(a >= b)           # => False
print(c.isdisjoint(b))  # => True
"""
- a & b : les éléments communs ; a | b : tous les éléments.
- a - b : ce qui est dans a mais pas dans b (et b - a, l'inverse).
- a ^ b : ce qui n'est que dans un seul des deux.
- c <= a : c est inclus dans a. c < c est faux : l'inclusion stricte exclut
  l'égalité.
- a >= b est faux : 5 est dans b mais pas dans a.
- c et b n'ont aucun élément en commun : ils sont disjoints.
"""

# 15. Films :
films_ana = {"Alien", "Amélie", "Brazil", "Coco", "Dune"}
films_bob = {"Brazil", "Dune", "Fargo", "Heat"}
print(sorted(films_ana & films_bob))  # => ['Brazil', 'Dune']
print(sorted(films_ana | films_bob))
# => ['Alien', 'Amélie', 'Brazil', 'Coco', 'Dune', 'Fargo', 'Heat']
print(sorted(films_bob - films_ana))  # => ['Fargo', 'Heat']
print(sorted(films_ana ^ films_bob))
# => ['Alien', 'Amélie', 'Coco', 'Fargo', 'Heat']
"""
c) Bob peut conseiller à Ana les films qu'il a vus et qu'elle n'a pas vus :
   c'est la différence films_bob - films_ana (et non l'inverse !).
"""

# 16. Pas à pas :
x = {1, 2, 3}
x |= {3, 4}         # x vaut {1, 2, 3, 4}
x &= {2, 3, 4, 5}   # x vaut {2, 3, 4}
x -= {4}            # x vaut {2, 3}
print(sorted(x))    # => [2, 3]


# 17. Recrutement :
def competences_manquantes(requises, candidat):
    return sorted(requises - candidat)


def est_qualifie(requises, candidat):
    return requises <= candidat


requises = {"python", "sql", "git"}
print(competences_manquantes(requises, {"python", "excel"}))
# => ['git', 'sql']
print(est_qualifie(requises, {"git", "python", "sql", "java"}))  # => True
print(est_qualifie(requises, {"python", "excel"}))               # => False
"""
- Les compétences manquantes sont celles qui sont requises mais que le
  candidat n'a pas : requises - candidat.
- Le candidat est qualifié si les compétences requises sont INCLUSES dans les
  siennes (il peut en avoir d'autres, comme "java").
"""


############################
#  Bonus : les frozensets  #
############################

# 18. Seules la 2e et la 5e ligne soulèvent une erreur :
f = frozenset("abc")
try:
    f.add("d")
except AttributeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
g = f | {"d"}
print(sorted(g))  # => ['a', 'b', 'c', 'd']
d = {f: "lettres"}
try:
    e = {{1, 2}: "ensemble"}
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- Un frozenset est immuable : il n'a pas de méthode .add() (AttributeError).
- f | {"d"} ne modifie pas f : l'opération crée un NOUVEAU frozenset.
- Un frozenset peut être une clé de dictionnaire, puisqu'il est immuable.
- Un set "normal" est mutable : il ne peut pas être une clé (TypeError).
"""

# 19. Paires d'amis distinctes :
rencontres = [("ana", "bob"), ("bob", "ana"), ("ana", "chloé"),
              ("chloé", "ana"), ("bob", "chloé")]
paires = {frozenset(rencontre) for rencontre in rencontres}
print(len(paires))  # => 3
"""
Les tuples ("ana", "bob") et ("bob", "ana") sont différents, car l'ordre
compte dans un tuple. En revanche, frozenset(("ana", "bob")) et
frozenset(("bob", "ana")) sont égaux. On ne peut pas utiliser des sets
"normaux" ici : un ensemble ne peut pas contenir d'autres sets (mutables),
mais il peut contenir des frozensets.
"""
