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
#  Chap. 29     #  Tests et spécification I : corrigés                         #
#               #                                                              #
################################################################################

######################################
#  Tester ses fonctions avec assert  #
######################################

# 1. Seuls les assert dont l'expression vaut False soulèvent une erreur :
assert 3 * 2 == 6                     # OK
assert "a" in "chat"                  # OK
try:
    assert len([]) == 1               # len([]) vaut 0
except AssertionError:
    print("1: (Sans ce try: … except …, assert len([]) == 1 échouerait)")
try:
    assert 0.1 + 0.2 == 0.3           # 0.1 + 0.2 vaut 0.30000000000000004
except AssertionError:
    print("2: (Sans ce try: … except …, assert 0.1 + 0.2 == 0.3 échouerait)")
assert "Python".lower() == "python"   # OK
try:
    assert [1, 2] == [2, 1]           # l'ordre compte dans une liste
except AssertionError:
    print("3: (Sans ce try: … except …, assert [1, 2] == [2, 1] échouerait)")
"""
- 0.1 + 0.2 == 0.3 est le piège classique des floats (cf. chap. 4 et 9) : pour
  comparer des floats, on teste plutôt abs(a - b) < 0.000001.
- Deux listes sont égales si elles ont les mêmes éléments DANS LE MÊME ORDRE.
"""
assert abs((0.1 + 0.2) - 0.3) < 0.000001  # OK : la bonne façon de comparer

# 2. Tests de max() :
assert max([3, 8, 1]) == 8                # liste "normale"
assert max([-5, -2, -9]) == -2            # nombres négatifs
assert max([42]) == 42                    # un seul élément
assert max([7, 3, 7]) == 7                # plusieurs maximums égaux
assert max(["pomme", "kiwi", "abricot"]) == "pomme"  # ordre alphabétique
print("Tous les tests de max() passent")  # => Tous les tests de max() passent
"""
Remarquez qu'on ne teste pas max([]) avec assert : cet appel soulève une
ValueError. Pour le tester, on utiliserait un try/except (cf. exercice 7).
"""

# 3. Assert avec message :
age = -3
try:
    assert age >= 0, f"L'âge doit être positif, et non {age}"
except AssertionError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 4: (Sans ce try: … except …, cette ligne créerait : L'âge doit être
#    positif, et non -3)

"""
4. Avec des parenthèses, on n'écrit plus "assert condition, message" mais
   "assert (un_tuple)". Or un tuple non vide est toujours évalué à True
   (cf. chap. 21) : l'assert ne peut donc jamais échouer ! Python le détecte
   d'ailleurs et affiche "SyntaxWarning: assertion is always true".
   La bonne écriture est, sans parenthèses :
       assert x > 0, "x doit être positif"
"""


#################################
#  Les 5 effets d'une fonction  #
#################################

"""
5. - f : retourne une valeur (effet 1) : la plus facile à tester, il suffit
         d'un assert f(2, 3) == 6.
   - g : affiche une valeur (effet 2) : impossible de récupérer le résultat
         avec un assert (g retourne None).
   - h : modifie la liste passée en paramètre (effet 3, "effet de bord").
   - k : modifie une variable globale (effet 4).
   - m : soulève une erreur si x < 0 (effet 5).
"""


# 6. La version qui RETOURNE la mention :
def mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"


assert mention(18) == "Très bien"
assert mention(16) == "Très bien"     # cas-limite : exactement 16
assert mention(15.5) == "Bien"
assert mention(14) == "Bien"          # cas-limite
assert mention(12) == "Assez bien"    # cas-limite
assert mention(10) == "Passable"      # cas-limite
assert mention(9.99) == "Insuffisant"
assert mention(0) == "Insuffisant"
print(mention(13))  # => Assez bien (on peut toujours afficher le résultat !)
"""
Les cas-limites (10, 12, 14, 16) sont les plus importants à tester : c'est là
qu'on se trompe souvent entre ">" et ">=".
"""


# 7. Fonction qui soulève une erreur :
def racine(x):
    if x < 0:
        raise ValueError("racine() n'accepte pas de nombre négatif")
    return x ** 0.5


# a) Valeurs correctes :
assert racine(16) == 4.0
assert racine(0) == 0.0
assert racine(2.25) == 1.5

# b) On vérifie que l'erreur est bien soulevée :
erreur_soulevee = False
try:
    racine(-4)
except ValueError:
    erreur_soulevee = True
assert erreur_soulevee  # => pas d'erreur : racine(-4) a bien soulevé l'erreur
print("Tous les tests de racine() passent")
# => Tous les tests de racine() passent


########################
#  Implémenter assert  #
########################

# 8. assert_egal() :
def assert_egal(a, b):
    if a != b:
        raise AssertionError(f"{a} != {b}")


assert_egal(2 + 2, 4)  # rien ne se passe
try:
    assert_egal(2 + 2, 5)
except AssertionError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 5: (Sans ce try: … except …, cette ligne créerait : 4 != 5)
"""
C'est plus pratique qu'un simple assert a == b : le message indique
directement les deux valeurs comparées. C'est ce que font les outils de test
comme pytest, que l'on verra plus tard.
"""


####################################
#  Exemple : la fonction my_pop()  #
####################################

# 9. my_index() et sa fonction de test :
def my_index(liste, x):
    for i in range(len(liste)):
        if liste[i] == x:
            return i  # on s'arrête à la PREMIÈRE occurrence
    raise ValueError(f"{x} is not in list")


def index_natif(liste, x):
    return liste.index(x)


def test_my_index():
    cas = [
        ([5, 6, 7], 5),     # début
        ([5, 6, 7], 6),     # milieu
        ([5, 6, 7], 7),     # fin
        ([1, 2, 1, 2], 2),  # doublons : on attend le 1er indice (1)
        (["a", "b"], "b"),  # autre type
    ]
    for liste, x in cas:
        assert my_index(liste, x) == liste.index(x)

    # Cas "absent" : les deux doivent soulever une ValueError
    for fonction in [my_index, index_natif]:
        erreur_soulevee = False
        try:
            fonction([1, 2, 3], 42)
        except ValueError:
            erreur_soulevee = True
        assert erreur_soulevee
    print("Tous les tests de my_index() passent")


test_my_index()  # => Tous les tests de my_index() passent
"""
index_natif() "emballe" la méthode .index() dans une fonction : on peut ainsi
mettre les deux fonctions dans une liste et les tester avec la même boucle
(une fonction peut être passée comme une valeur, cf. chap. 15).
"""


# 10. Le bug : maximum commence à 0, donc une liste de nombres NÉGATIFS donne
# un résultat faux.
def my_max(liste):
    maximum = 0
    for x in liste:
        if x > maximum:
            maximum = x
    return maximum


try:
    assert my_max([-5, -2, -9]) == -2  # my_max retourne 0 !
except AssertionError:
    print("6: (Sans ce try: … except …, ce test révélerait le bug de my_max)")


# Correction : on part du premier élément de la liste.
def my_max(liste):
    maximum = liste[0]
    for x in liste[1:]:
        if x > maximum:
            maximum = x
    return maximum


assert my_max([-5, -2, -9]) == -2
assert my_max([3, 8, 1]) == 8
assert my_max([42]) == 42
"""
C'est pour cela qu'il faut tester les cas "bizarres" : le bug passait tous les
tests avec des nombres positifs.
"""


###########################################
#  La méthode "Think-Red-Green-Refactor"  #
###########################################

"""
11. Think : compter_voyelles(s) prend une str et retourne un int (>= 0).
    Cas-limites : chaîne vide (0), pas de voyelle ("rbx" : 0), majuscules
    ("AEIOUY" : 6), espaces et ponctuation (ignorés).
"""


# Red : version "vide" qui retourne le bon type…
def compter_voyelles(s):
    return 0


# … et les tests, qui échouent pour l'instant :
def test_compter_voyelles():
    assert compter_voyelles("") == 0
    assert compter_voyelles("rbx") == 0
    assert compter_voyelles("python") == 2   # y et o
    assert compter_voyelles("AEIOUY") == 6
    assert compter_voyelles("Bonjour, le monde !") == 6


try:
    test_compter_voyelles()
except AssertionError:
    print("7: (Red : les tests échouent, c'est normal à cette étape)")


# Green : une première version qui fonctionne.
def compter_voyelles(s):
    compteur = 0
    for lettre in s:
        if lettre in "aeiouyAEIOUY":
            compteur = compteur + 1
    return compteur


test_compter_voyelles()  # aucune erreur : les tests sont au vert


# Refactor : plus court, avec .lower() et sum() sur une expression génératrice
# (cf. chap. 23). Les tests passent toujours :
def compter_voyelles(s):
    return sum(1 for lettre in s.lower() if lettre in "aeiouy")


test_compter_voyelles()
print(compter_voyelles("Data Science"))  # => 5

"""
12. Think : est_bissextile(annee) prend un int et retourne un bool.
    Cas-limites : divisible par 4 (2024), pas divisible par 4 (2023),
    divisible par 100 mais pas 400 (1900), divisible par 400 (2000).
"""


# Red :
def est_bissextile(annee):
    return False


def test_est_bissextile():
    assert est_bissextile(2024) is True
    assert est_bissextile(2023) is False
    assert est_bissextile(1900) is False
    assert est_bissextile(2000) is True
    assert est_bissextile(2100) is False


try:
    test_est_bissextile()
except AssertionError:
    print("8: (Red : les tests échouent, c'est normal à cette étape)")


# Green : on suit l'énoncé à la lettre.
def est_bissextile(annee):
    if annee % 400 == 0:
        return True
    elif annee % 100 == 0:
        return False
    elif annee % 4 == 0:
        return True
    else:
        return False


test_est_bissextile()


# Refactor : une seule expression booléenne (cf. chap. 9 et 21).
def est_bissextile(annee):
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)


test_est_bissextile()
print(est_bissextile(2028))  # => True


####################
#  Les docstrings  #
####################

# 13. Docstring de repeter() :
def repeter(mot, n):
    """(str, int) -> str
    Retourne une chaîne contenant n fois le mot, séparé par des espaces.
    Si n vaut 0, retourne la chaîne vide.
    """
    return " ".join([mot] * n)


print(repeter("ha", 3))   # => ha ha ha
print(repeter.__doc__)
# => (str, int) -> str
#    Retourne une chaîne contenant n fois le mot, séparé par des espaces.
#    Si n vaut 0, retourne la chaîne vide.
# (Avant Python 3.13, l'indentation des lignes 2 et 3 est conservée.)


#############################
#  Les annotations de type  #
#############################

# 14. Avec annotations :
def repeter(mot: str, n: int) -> str:
    """Retourne une chaîne contenant n fois le mot, séparé par des espaces."""
    return " ".join([mot] * n)


def compter_voyelles(s: str) -> int:
    """Retourne le nombre de voyelles (aeiouy, sans tenir compte de la casse)
    de la chaîne s."""
    return sum(1 for lettre in s.lower() if lettre in "aeiouy")


print(repeter.__annotations__)
# => {'mot': <class 'str'>, 'n': <class 'int'>, 'return': <class 'str'>}
print(compter_voyelles.__annotations__)
# => {'s': <class 'str'>, 'return': <class 'int'>}


# 15. Les annotations ne sont PAS vérifiées par Python :
def double(x: int) -> int:
    return x * 2


print(double("ab"))  # => abab
"""
Python ne refuse pas l'appel : les annotations sont des indications pour le
lecteur (et pour des outils comme mypy, cf. chapitre), pas des contraintes.
"ab" * 2 est une opération valide, qui duplique la chaîne.
"""
