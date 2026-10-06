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
#  Chap. 31     #  Slices : corrigés                                           #
#               #                                                              #
################################################################################

"""
Pour tous les exercices, on note les indices sous chaque élément :

    l =   [10, 20, 30, 40, 50, 60, 70]
    indice  0   1   2   3   4   5   6
    négatif -7 -6  -5  -4  -3  -2  -1
"""
l = [10, 20, 30, 40, 50, 60, 70]


#############
#  Syntaxe  #
#############

# 1. Rappel : l'indice de début est inclus, celui de fin est EXCLU.
print(l[2:5])    # => [30, 40, 50] (indices 2, 3 et 4)
print(l[:3])     # => [10, 20, 30] (du début jusqu'à l'indice 3, exclu)
print(l[4:])     # => [50, 60, 70] (de l'indice 4 jusqu'à la fin)
print(l[:])      # => [10, 20, 30, 40, 50, 60, 70] (toute la liste)
print(l[1:6:2])  # => [20, 40, 60] (indices 1, 3 et 5)
print(l[5:2])    # => [] (le début est après la fin : slice vide)

# 2. Nombre d'éléments :
print(len(l[1:5]))  # => 4
print(len(l[3:7]))  # => 4
"""
l[debut:fin] contient fin - debut éléments (5 - 1 = 4, 7 - 3 = 4). C'est l'un
des avantages de la convention "fin exclue".
"""


#########################
#  Indexation négative  #
#########################

# 3. Les indices négatifs comptent depuis la fin (-1 : le dernier).
print(l[-1])     # => 70 (un indice seul : un élément, pas une liste)
print(l[-3:])    # => [50, 60, 70] (les 3 derniers)
print(l[:-2])    # => [10, 20, 30, 40, 50] (tout sauf les 2 derniers)
print(l[-5:-2])  # => [30, 40, 50] (indices -5, -4 et -3)
print(l[1:-1])   # => [20, 30, 40, 50, 60] (sans le premier ni le dernier)
print(l[-2:2])   # => [] (-2 correspond à l'indice 5, qui est après 2)


########################
#  Exemples de slices  #
########################

# 4. a) b) c)
print(l[:3])    # => [10, 20, 30]
print(l[-3:])   # => [50, 60, 70]
print(l[1:-1])  # => [20, 30, 40, 50, 60]

# 4. d) Les deux moitiés : len(l) // 2 vaut 7 // 2 = 3.
milieu = len(l) // 2
print(l[:milieu])  # => [10, 20, 30]
print(l[milieu:])  # => [40, 50, 60, 70]
"""
l[:milieu] + l[milieu:] redonne toujours la liste complète, quel que soit
milieu : aucun élément n'est perdu ni dupliqué.
"""

# 5. Seul l'accès à un indice seul (a) soulève une erreur :
try:
    print(l[10])
except IndexError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : list index out of
#    range)
print(l[5:100])  # => [60, 70] (une slice s'arrête au bout, sans erreur)
print(l[100:])   # => [] (une slice vide, toujours sans erreur)


# 6. La slice ne provoque jamais d'erreur, même si la liste est courte :
def apercu(liste, n):
    if len(liste) > n:
        return liste[:n] + ["…"]
    return liste[:n]


print(apercu([1, 2, 3, 4, 5], 3))  # => [1, 2, 3, '…']
print(apercu([1, 2], 3))           # => [1, 2]


###################
#  Le pas (step)  #
###################

# 7. Le pas indique l'écart entre deux indices successifs.
print(l[::2])     # => [10, 30, 50, 70] (indices 0, 2, 4, 6)
print(l[1::3])    # => [20, 50] (indices 1 et 4 ; 7 n'existe pas)
print(l[::-1])    # => [70, 60, 50, 40, 30, 20, 10] (la liste à l'envers)
print(l[5:1:-2])  # => [60, 40] (indices 5 et 3, en reculant ; 1 exclu)
print(l[1:5:-1])  # => [] (on recule, mais 1 est AVANT 5 : slice vide)

# 8. Sommes par parité de l'indice :
nombres = list(range(1, 21))
print(sum(nombres[::2]))   # => 100 (1 + 3 + 5 + … + 19)
print(sum(nombres[1::2]))  # => 110 (2 + 4 + 6 + … + 20)
"""
Attention à la confusion : les éléments d'indice PAIR sont ici les nombres
IMPAIRS, car la liste commence à 1 et les indices à 0.
"""


# 9. Une string retournée avec [::-1] :
def est_palindrome(phrase):
    lettres = phrase.lower().replace(" ", "")
    return lettres == lettres[::-1]


print(est_palindrome("Kayak"))                         # => True
print(est_palindrome("Esope reste ici et se repose"))  # => True
print(est_palindrome("Python"))                        # => False


########################################
#  Modifier une liste avec les slices  #
########################################

# 10. a) On remplace 2 éléments par 1 seul (les tailles peuvent différer) :
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
jours[1:3] = ["MILIEU"]
print(jours)  # => ['lundi', 'MILIEU', 'jeudi', 'vendredi']

# 10. b) Une slice vide au début permet d'insérer :
jours[:0] = ["dimanche"]
print(jours)  # => ['dimanche', 'lundi', 'MILIEU', 'jeudi', 'vendredi']

# 10. c) del avec une slice supprime toute une portion :
del jours[-2:]
print(jours)  # => ['dimanche', 'lundi', 'MILIEU']

# 11. Valeurs successives de x :
x = [1, 2, 3, 4, 5]
x[1:3] = []
print(x)  # => [1, 4, 5] (remplacer par une liste vide = supprimer)
x[:0] = [0]
print(x)  # => [0, 1, 4, 5] (insertion au début)
x[len(x):] = [6, 7]
print(x)  # => [0, 1, 4, 5, 6, 7] (ajout à la fin, comme .extend())

# 12. On construit de NOUVELLES strings à partir de slices :
mot = "chat"
print(mot[:2] + "u" + mot[3:])  # => chut
print(mot + "eau")              # => chateau
print(mot[-1] + mot[:-1])       # => tcha
print(mot)                      # => chat (la string d'origine n'a pas changé)


###########################################
#  Slices avec d'autres types construits  #
###########################################

# 13. Les positions sont fixes dans le format ISO "aaaa-mm-jj" :
date_iso = "2024-03-15"
annee = date_iso[:4]
mois = date_iso[5:7]
jour = date_iso[8:]
print(annee, mois, jour)         # => 2024 03 15
print(f"{jour}/{mois}/{annee}")  # => 15/03/2024

# 14. Une slice est du même type que la séquence d'origine :
print((1, 2, 3, 4)[1:3])             # => (2, 3) (un tuple)
print("Bonjour"[::2])                # => Bnor (une string)
print(range(0, 100, 5)[3:6])         # => range(15, 30, 5) (un range)
print(list(range(0, 100, 5)[3:6]))   # => [15, 20, 25]

# 15. Un dictionnaire n'est pas une séquence : on accède aux valeurs par une
# clé, pas par une position.
capitales = {"France": "Paris", "Italie": "Rome", "Espagne": "Madrid"}
try:
    print(capitales[:2])
except (TypeError, KeyError) as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : slice(None, 2, None))
# (Depuis Python 3.12, c'est une KeyError : la slice est cherchée comme une
# clé. Avant, c'était une TypeError, cf. chapitre.)
# On convertit d'abord les clés en liste (l'ordre d'insertion est conservé) :
print(list(capitales)[:2])  # => ['France', 'Italie']


####################################
#  Copie de séquences avec slices  #
####################################

# 16. b est un autre NOM pour la même liste ; c est une copie :
a = [1, 2, 3]
b = a
c = a[:]
a.append(4)
print(a)  # => [1, 2, 3, 4]
print(b)  # => [1, 2, 3, 4] (b et a désignent la même liste)
print(c)  # => [1, 2, 3] (la copie n'est pas affectée)

# 17. La copie par slice est "superficielle" :
m = [[1, 2], [3, 4]]
n = m[:]
n[0].append(99)
n[1] = "remplacé"
print(m)  # => [[1, 2, 99], [3, 4]]
print(n)  # => [[1, 2, 99], 'remplacé']
"""
n est une nouvelle liste, mais ses éléments sont LES MÊMES sous-listes que
celles de m :
    - n[0].append(99) modifie la sous-liste partagée : m la voit changer ;
    - n[1] = "remplacé" remplace un élément de n uniquement : m n'est pas
      touchée.
Pour copier aussi les sous-listes, on utilise copy.deepcopy() (cf. chap. 24).
"""


##########################
#  Pour aller plus loin  #
##########################

# 18. Rotation : la fin de la liste, puis son début.
def rotation(liste, k):
    if len(liste) == 0:
        return []
    k = k % len(liste)  # tourner de 7 crans sur 5 éléments = tourner de 2
    return liste[k:] + liste[:k]


print(rotation([1, 2, 3, 4, 5], 2))  # => [3, 4, 5, 1, 2]
print(rotation([1, 2, 3, 4, 5], 7))  # => [3, 4, 5, 1, 2]
print(rotation([1, 2, 3, 4, 5], 0))  # => [1, 2, 3, 4, 5]
print(rotation([], 3))               # => []
"""
Sans le modulo, rotation([1, 2, 3, 4, 5], 7) retournerait la liste inchangée
(liste[7:] est vide et liste[:7] est la liste entière). On teste aussi la
liste vide à part : k % 0 soulèverait une ZeroDivisionError.
"""


# 19. On avance de "taille" en "taille" avec le pas de range() :
def paquets(liste, taille):
    return [liste[i:i + taille] for i in range(0, len(liste), taille)]


print(paquets([1, 2, 3, 4, 5, 6, 7], 3))  # => [[1, 2, 3], [4, 5, 6], [7]]
print(paquets(list("abcdef"), 2))  # => [['a', 'b'], ['c', 'd'], ['e', 'f']]
"""
i prend les valeurs 0, 3, 6 : on découpe liste[0:3], liste[3:6] et
liste[6:9]. La dernière slice dépasse la fin de la liste, mais une slice ne
provoque jamais d'erreur : elle s'arrête simplement au bout (exercice 5).
"""
