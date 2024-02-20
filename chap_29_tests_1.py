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

try:
    assert 2 + 2 == 3  # l'égalité est fausse : assert soulève une erreur
except AssertionError:
    print("1: (Sans ce try: … except …, cette ligne créerait une erreur)")


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
"""


# Implémenter assert
#####################

"""
L'implémentation de assert est simplissime : assert se contente de crée une
erreur si la valeur qu'on lui passe évalue à False :
"""
def my_assert(var: bool, msg: str) -> None:
    if is_bool(var) == False:
        raise AssertionError(msg)


# TODO : ex



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
    print("Test: my_pop()…", end="")

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
        print("2: (Sans ce try: … except …, cette ligne créerait une erreur)")
        error_raised_native = True

    assert error_raised_native == True


    error_raised_custom = False
    try:
        ret_custom = my_pop(pop_custom)  # IndexError: pop from empty list
    except IndexError as err:
        print("3: (Sans ce try: … except …, cette ligne créerait une erreur)")
        error_raised_custom = True

    assert error_raised_custom == True
    print(" OK")

pop_native = [2, True, "Pouet", 5.4]  # => pour tester l.pop()
pop_custom = [2, True, "Pouet", 5.4]  # => pour tester my_pop(l)
test_my_pop(pop_native, pop_custom)


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

4. "Refactor" : une fois les tests passés, on commence à se soucie de la qualité
   du code.
   D'abord, allez faire un tour, soufflez, prenez du recul sur votre code.
   Ensuite, réfléchissez ! Renommez vos variables et vos fonctions, harmonisez
   leurs noms, utilisez des structures de données plus adaptées, voyez si vous
   pouvez simplifier certaines parties, ou isoler du code dans une fonction…

   Ce processus s'appelle le "refactoring" : on ne modifie plus le comportement
   de la fonction (le "quoi"), mais le "comment". À chaque modification, vous
   pourrez relancer vos tests pour vous assurer que votre changement n'a pas
   créé de "régression" (du code moins fonctionnel qu'avant modification).
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


# Les annotations de type
###############################

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


print(print_bidule("Test"))  # => None

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
    elif par2 > 5:
        return False
    else:
        return len(par1)

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

Ainsi cette fonction ne prend que des listes d'entiers :
"""
def comparer_listes_ints(a: list[int], b: list[int]) -> bool:
    return len(a) > len(b)

"""
Remarque : Python ne soulèvera pas d'erreurs si on passe autre chose à la
fonction: les annotations de type sont indicatives.
"""
print(comparer_listes_ints([2.1, 5.42, 8.89], [3.1, 7.9]))  # => True

