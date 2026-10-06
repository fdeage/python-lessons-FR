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
#  Chap. 29     #  Tests et spécification I                                    #
#               #                                                              #
################################################################################
#
#   - Tester ses fonctions avec "assert"
#   - Les 5 effets d'une fonction
#   - Implémenter assert
#   - Exemple : la fonction my_pop()
#   - La méthode "Think-Red-Green-Refactor"
#   - Les docstrings
#   - Les annotations de type
#
#############################################

# Tester ses fonctions avec "assert"
#####################################

"""
Un test est un morceau de code qui va comparer une valeur du programme à une
valeur attendue.
C'est donc UN PROGRAMME QUI TESTE UN AUTRE PROGRAMME (Inception !).

Dans 99% des cas, les tests vont se trouver dans une partie à part du programme,
et tester une fonction en particulier. On évitera de mélanger test et
comportement normal du programme.

Une fonction peut avoir plusieurs effets sur le comportement d'un programme,
il y aura donc plusieurs façons de la tester.

On utilisera le mot-clé assert suivie d'une expression booléenne pour tester ses
programmes.
"""
assert 2 + 2 == 4  # pas d'erreur

"""
Si l'expression est vraie (True), assert ne fait rien du tout : le programme
continue normalement.

Si l'expression est fausse (False), assert soulève une erreur AssertionError
(cf. chap. 26), qui interrompt le programme :
"""
try:
    assert 2 + 2 == 3  # l'égalité est fausse : assert soulève une erreur
except AssertionError:
    print("1: (Sans ce try: … except …, cette ligne créerait une erreur)")

"""
On peut ajouter après une virgule un message d'erreur, qui sera affiché si le
test échoue. C'est très utile pour savoir QUEL test a échoué, et pourquoi :
"""
try:
    assert len("abc") == 4, "La longueur de 'abc' devrait être 4"
except AssertionError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Attention : assert n'est pas une fonction mais un mot-clé. On n'écrit donc PAS
de parenthèses autour de l'expression et du message :
    assert (2 + 2 == 3, "message")  # FAUX !
Ici, on passe à assert un tuple (cf. chap. 17) non vide, qui est toujours
évalué à True (cf. chap. 21) : le test ne pourra jamais échouer !

Un test typique compare la valeur retournée par une fonction avec la valeur
que l'on attend. Par exemple, pour tester la fonction intégrée abs() (valeur
absolue), on vérifie plusieurs cas, y compris les "cas-limites" (ici 0) :
"""
assert abs(5) == 5
assert abs(-5) == 5
assert abs(0) == 0
assert abs(-2.5) == 2.5
print("Tests de abs() : OK")  # => Tests de abs() : OK


# Les 5 effets d'une fonction
##############################

"""
Il y a 5 manières pour une fonction d'avoir un effet sur le déroulement du
programme :
    1. en retournant une valeur (avec return)

    2. en imprimant une valeur (avec print())

    3. en modifiant le ou les types construits (listes, dicts…) passés en
       paramètre : on appelle ça un "effet de bord", ou "side effect".
       Attention, cela peut être source de confusion et de bugs.

    4. en modifiant une variable dite "globale". On évitera ces fonctions car
       elles sont complexes à tester correctement

    5. en soulevant une erreur pendant l'exécution

Et voici la "testabilité" de ces fonctions :
1 : idéal, ce sont les plus faciles à tester
2 : doivent rester les plus simples possibles
3 : à éviter, sauf si cela simplifie vraiment le programme
4 : à éviter absolument, sauf dans certains cas très précis
5 : privilégier l'utilisation de valeurs de retour

Note : pour tester une fonction de type 5, on vérifie qu'elle soulève bien
l'erreur attendue avec un try … except (voir l'exemple de my_pop() plus bas).

Exemple (pas bien) :
"""
def compute_and_print_result_1(a, b):
    calcul_complexe = (pow(a, b) % 2) * 3
    print(f"Résultat : {calcul_complexe}")


"""
Cette fonction calcule une valeur et imprime du texte. Elle ne retourne rien et
est donc complexe à tester : pour cette raison, ON ÉVITERA DE MÉLANGER CALCUL
ET AFFICHAGE DE RÉSULTATS.

Exemple (bien) :
"""
def compute_result(a, b):
    return (pow(a, b) % 2) * 3


def compute_and_print_result_2(a, b):
    calcul_complexe = compute_result(a, b)
    print(f"Résultat : {calcul_complexe}")


"""
Ce découpage permet de tester la fonction de calcul : la fonction d'affichage
ne fait plus… qu'afficher !

On peut maintenant tester facilement compute_result(). Calculons à la main :
    - pow(2, 3) = 8, 8 % 2 = 0, 0 * 3 = 0
    - pow(3, 2) = 9, 9 % 2 = 1, 1 * 3 = 3
"""
assert compute_result(2, 3) == 0
assert compute_result(3, 2) == 3
compute_and_print_result_2(3, 2)  # => Résultat : 3


# Implémenter assert
#####################

"""
L'implémentation de assert est simplissime : assert se contente de créer une
erreur si la valeur qu'on lui passe évalue à False.

On peut donc la recoder avec une fonction, un "if" (cf. chap. 12) et le mot-clé
"raise" (qui soulève une erreur, cf. chap. 26) :
"""
def my_assert(var: bool, msg: str = "") -> None:
    if not var:
        raise AssertionError(msg)


"""
(Pour la notation "var: bool" et "-> None", voir la section "Les annotations de
type" à la fin de ce chapitre. Pour la valeur par défaut msg="", cf. chap. 15.)

Exemples :
"""
my_assert(2 + 2 == 4)  # pas d'erreur, rien ne se passe
my_assert(len([1, 2, 3]) == 3, "La liste devrait avoir 3 éléments")  # idem

try:
    my_assert(2 + 2 == 3, "2 + 2 ne fait pas 3 !")
except AssertionError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Notre fonction se comporte donc exactement comme assert. On peut même le
vérifier… avec assert, en utilisant une variable qui retient si une erreur a
été soulevée :
"""
erreur_soulevee = False
try:
    my_assert(False, "test")
except AssertionError:
    erreur_soulevee = True

assert erreur_soulevee  # => pas d'erreur : my_assert() a bien soulevé l'erreur

"""
Remarques :
    - on écrit "if not var" plutôt que "if var == False" : ainsi, comme pour
      assert, une valeur "falsy" (0, "", [], None…, cf. chap. 21) fera aussi
      échouer le test.
    - HP : le vrai mot-clé assert est désactivé quand on lance Python avec
      l'option -O ("optimisation") : on ne l'utilisera donc jamais pour
      vérifier des données en production, seulement pour tester son code.
"""


# Exemple : la fonction my_pop()
#################################

"""
On veut recoder manuellement la méthode .pop() de la liste. Cette méthode
enlève à la liste sa dernière valeur, puis la retourne.

On veut coder une fonction my_pop() qui fasse exactement la même chose. Pour
les tests, on va partir de deux listes identiques, auxquelles on appliquera à
chacune une fonction. On comparera ensuite automatiquement les listes obtenues.
"""
def my_pop(l):
    if len(l) == 0:
        raise IndexError("Trying to pop() from empty list!")
    last = l[-1]   # raccourci pour liste[len(liste) - 1]
    del l[-1]
    return last


"""
Il y a ici deux choses à tester :
    1. la valeur de retour,
    2. la liste elle-même, qui a été modifiée par l'appel.

On va donc devoir appeler assert avant et après les appels de fonction.
Note : reponse1 == reponse2 retourne toujours un booléen.
"""
def test_my_pop(pop_native, pop_custom):
    print("Test: my_pop()…")

    for _ in range(len(pop_native)):
        # Listes égales avant appels ?
        assert pop_native == pop_custom

        ret_native = pop_native.pop()
        ret_custom = my_pop(pop_custom)
        # Listes égales après appels ?
        assert pop_native == pop_custom

        # Les valeurs de retour sont-elles égales ?
        assert ret_native == ret_custom

    """
    Pour tester les erreurs, on appelle "une fois de trop" les deux fonctions,
    et on s'assure qu'elles soulèvent bien chacune une erreur.
    """
    error_raised_native = False
    try:
        ret_native = pop_native.pop()    # IndexError: pop from empty list
    except IndexError as err:
        print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
        error_raised_native = True

    assert error_raised_native == True


    error_raised_custom = False
    try:
        ret_custom = my_pop(pop_custom)  # IndexError: pop from empty list
    except IndexError as err:
        print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
        error_raised_custom = True

    assert error_raised_custom == True
    print("Test: my_pop()… OK")

pop_native = [2, True, "Pouet", 5.4]  # => pour tester l.pop()
pop_custom = [2, True, "Pouet", 5.4]  # => pour tester my_pop(l)
test_my_pop(pop_native, pop_custom)
# => Test: my_pop()…
#    4: (Sans ce try: … except …, cette ligne créerait : pop from empty list)
#    5: (Sans ce try: … except …, cette ligne créerait : Trying to pop() from empty list!)
#    Test: my_pop()… OK

"""
Remarques :
    - Si un seul des assert échoue, l'erreur AssertionError interrompt le
      programme, et le message "OK" ne s'affiche jamais : on sait tout de suite
      qu'il y a un problème.
    - Après le test, les deux listes sont vides : la fonction de test les a
      modifiées (effet de bord, voir plus haut) !
"""
print(pop_native, pop_custom)  # => [] []

"""
Pour bien comprendre l'intérêt des tests, voici une version BOGUÉE de my_pop(),
qui retourne la dernière valeur… mais oublie de la supprimer de la liste :
"""
def my_pop_bugge(l):
    return l[-1]


"""
Le test des valeurs de retour passerait au premier appel, mais le test de la
liste après l'appel échoue : le bug est détecté automatiquement.
"""
liste_a = [1, 2, 3]
liste_b = [1, 2, 3]
ret_a = liste_a.pop()
ret_b = my_pop_bugge(liste_b)
assert ret_a == ret_b  # OK : les deux retournent 3…
try:
    assert liste_a == liste_b, f"{liste_a} != {liste_b}"  # … mais les listes diffèrent
except AssertionError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")


# La méthode "Think-Red-Green-Refactor"
########################################

"""
Ce drôle de nom désigne une logique de test où l'on va écrire les tests avant le
code.

1. "Think" : prenez un papier et un stylo et réfléchissez à ce que votre
   code doit faire. C'est l'étape la plus difficile.

   Vous pouvez déjà découper votre code en fonctions, sans écrire leur
   contenu. Retournez simplement des valeurs du bon type.

2. "Red" : écrivez quelques tests de vos fonctions. Vous savez ce que la
   fonction doit retourner, donc utilisez des assertions pour préciser ce qui
   est attendu. Vos tests ne passeront pas (ils seront "rouges").

3. "Green" : écrire le code de chaque fonction, fonction par fonction, jusqu'à
   ce que vos tests passent au vert. Ne vous souciez pas de faire du code joli
   au début, juste fonctionnel. Assurez-vous que vos tests couvrent tout !
   Pensez aux cas-limites, bizarres, etc. : listes vides, valeurs négatives,
   None, string vide…

4. "Refactor" : une fois les tests passés, on commence à se soucier de la qualité
   du code.
   D'abord, allez faire un tour, soufflez, prenez du recul sur votre code.
   Ensuite, réfléchissez ! Renommez vos variables et vos fonctions, harmonisez
   leurs noms, utilisez des structures de données plus adaptées, voyez si vous
   pouvez simplifier certaines parties, ou isoler du code dans une fonction…

   Ce processus s'appelle le "refactoring" : on ne modifie plus le comportement
   de la fonction (le "quoi"), mais le "comment". À chaque modification, vous
   pourrez relancer vos tests pour vous assurer que votre changement n'a pas
   créé de "régression" (du code moins fonctionnel qu'avant modification).

Exemple complet : on veut une fonction est_palindrome(s) qui retourne True si
la chaîne s se lit de la même façon dans les deux sens ("kayak", "radar"…).

1. Think : la fonction prend une string et retourne un booléen. Cas-limites :
   la chaîne vide et une chaîne d'un caractère sont des palindromes. On ignore
   les majuscules ("Kayak" est un palindrome).

2. Red : on écrit d'abord une version "vide" qui retourne une valeur du bon
   type, puis les tests. Ici, les tests échouent (on les protège avec try pour
   que ce fichier reste exécutable).
"""


def est_palindrome(s):
    return False  # version "vide" : retourne juste un booléen


def test_est_palindrome():
    assert est_palindrome("kayak") == True
    assert est_palindrome("Kayak") == True
    assert est_palindrome("radar") == True
    assert est_palindrome("python") == False
    assert est_palindrome("") == True
    assert est_palindrome("a") == True


try:
    test_est_palindrome()
except AssertionError:
    print("7: (Sans ce try: … except …, cette ligne créerait une AssertionError)")

"""
3. Green : on écrit le code jusqu'à ce que les tests passent. On rappelle que
   s[::-1] retourne la chaîne s à l'envers (cf. chap. 31 sur les slices), et
   que .lower() met une chaîne en minuscules (cf. chap. 8).
"""


def est_palindrome(s):
    s_min = s.lower()
    inverse = ""
    for c in s_min:
        inverse = c + inverse
    if inverse == s_min:
        return True
    else:
        return False


test_est_palindrome()  # pas d'erreur : les tests sont "verts"
print("Tests de est_palindrome() : OK")  # => Tests de est_palindrome() : OK

"""
4. Refactor : le code fonctionne, mais on peut le simplifier. Une comparaison
   retourne déjà un booléen : le "if … else" est inutile (cf. chap. 9). On
   relance ensuite les tests pour vérifier qu'on n'a rien cassé.
"""


def est_palindrome(s):
    s_min = s.lower()
    return s_min == s_min[::-1]


test_est_palindrome()  # toujours pas d'erreur : pas de régression
print("Tests de est_palindrome() après refactoring : OK")
# => Tests de est_palindrome() après refactoring : OK

"""
(Note : on a redéfini trois fois la fonction est_palindrome() : à chaque fois,
la nouvelle définition remplace l'ancienne, cf. chap. 14.)

Au chap. 37 (Tests II), on verra comment automatiser ces tests avec pytest.
"""


# Les docstrings
######################

"""
Une docstring est une chaîne de caractères multi-lignes placée sous la
définition d'une fonction, qui sert à renseigner sur son comportement :
    1. ce que la fonction accepte comme paramètres,
    2. éventuellement, le pourquoi de son fonctionnement, sa performance, ses
       cas-limites,
    3. enfin, ce qu'elle retourne.

C'est une très bonne habitude de commenter intelligemment toutes ses fonctions.

La docstring est une string comme une autre, mais Python la conserve et la
rattache à la fonction : on peut l'afficher avec help(fonction), ou avec
l'attribut __doc__ (cf. chap. 3).
"""

# Ex. avec une qui fonction prend une string et retourne un booléen :
def fn_exemple_1(s):
    """(str) -> bool
    Cette fonction retourne True si la chaîne est non-nulle, et False sinon.
    """
    return len(s) > 0


# Ex. avec une fonction qui prend deux entiers et retourne un tuple :
def fn_exemple_2(a, b):
    """(int, int) -> tuple[int, int]
    Cette fonction retourne un tuple de deux valeurs.
    """
    return (a + b, a - b)


print(fn_exemple_1("abc"))   # => True
print(fn_exemple_2(5, 3))    # => (8, 2)
print(fn_exemple_1.__doc__)
# => (str) -> bool
#    Cette fonction retourne True si la chaîne est non-nulle, et False sinon.
# (Avant Python 3.13, l'indentation de la 2e ligne est conservée à l'affichage.)


# Les annotations de type
###############################

# (Pour aller plus loin : Optional, Callable, TypedDict, mypy… cf. chap. 46.)

"""
L'annotation de type ("type hint") consiste à indiquer dans l'en-tête d'une
fonction :
  - les valeurs acceptées en paramètres, et leur type
  - le type de la valeur retournée

C'est une pratique optionnelle qui aide à avoir une idée du comportement de la
fonction.

On utilise ":" pour les paramètres, et "->" pour la valeur de retour. Ainsi,
cette fonction indique qu'elle prend une string en paramètre, et ne retourne
rien :
"""
def print_bidule(parametre: str) -> None:
    print(f"Le paramètre est : {parametre}")
    # Sans mot-clé return, une fonction retournera None par défaut


print(print_bidule("Test"))
# => Le paramètre est : Test
#    None

# Inversement, cette fonction de comparaison retourne toujours un booléen :
def comparer_listes(a: list, b: list) -> bool:
    return len(a) > len(b)


print(comparer_listes([2], [3, 7]))        # => False
print(comparer_listes([2, 5, 8], [3, 7]))  # => True

"""
Remarque : une annotation de type suppose que votre fonction retourne des
valeurs de type homogène…

Ainsi, cette fonction n'est pas annotable :
"""
def une_fonction_bizarre(par1, par2):
    """(????) -> (????)."""
    if len(par2) == 0:
        return "la chaîne est vide"
    elif len(par2) > 5:
        return False
    else:
        return len(par1)


"""
Selon ses paramètres, elle retourne une string, un booléen ou un int : il est
impossible de lui donner un type de retour unique. C'est le signe d'une
fonction mal conçue, difficile à utiliser… et à tester !
"""
print(une_fonction_bizarre("abc", ""))        # => la chaîne est vide
print(une_fonction_bizarre("abc", "abcdefg"))  # => False
print(une_fonction_bizarre("abc", "ab"))       # => 3

"""
Les types utilisables pour les annotations sont :
   - None (ne retourne rien)
   - int
   - float
   - bool
   - str
   - list
   - tuple
   - dict

Pour les types construits, on peut même aller plus loin et spécifier leur
contenu avec la syntaxe "type[type]":
   - list[bool] (pour une liste ne contenant que des booléens)
   - tuple[str, int] (pour un tuple ayant toujours comme première valeur une
     string, et comme deuxième un int)

Attention, les valeurs contenues dans le type construit doivent toutes être de
même nature.

Note : cette syntaxe list[int], tuple[str, int]… n'est disponible qu'à partir
de Python 3.9. Avec une version plus ancienne, la définition de fonction
ci-dessous soulève une erreur TypeError.

Ainsi cette fonction ne prend que des listes d'entiers :
"""
def comparer_listes_ints(a: list[int], b: list[int]) -> bool:
    return len(a) > len(b)

"""
Remarque : Python ne soulèvera pas d'erreurs si on passe autre chose à la
fonction : les annotations de type sont indicatives.

Ici, on passe des listes de floats alors que la fonction annonce des listes
d'ints : Python ne dit rien.
"""
print(comparer_listes_ints([2.1, 5.42, 8.89], [3.1, 7.9]))  # => True

"""
HP : des outils externes, comme mypy (https://mypy-lang.org), savent lire ces
annotations et détecter ce genre d'erreurs AVANT l'exécution du programme.
Beaucoup d'éditeurs de texte (VS Code, PyCharm…) le font aussi en soulignant
le code suspect.

Les annotations sont stockées dans l'attribut __annotations__ de la fonction :
"""
print(comparer_listes.__annotations__)
# => {'a': <class 'list'>, 'b': <class 'list'>, 'return': <class 'bool'>}

