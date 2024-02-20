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
#  Chap. 12     #  Structures de contrôle I : if, then, else et elif           #
#               #                                                              #
################################################################################
#
#  - La structure "if"
#  - Le mot-clé "else"
#  - Le mot-clé "elif"
#  - "if" imbriqués
#  - Remarques sur l'indentation
#  - Les "one-liner" avec if
#
###################################

"""
Normalement, un programme Python est exécuté de haut en bas, ligne à ligne.

C'est le comportement par défaut, mais on peut le modifier avec des structures
de contrôle :
    1. soit pour exécuter un bloc de code seulement sous certaines conditions
       (avec le mot-clé "if", comme on le verra dans ce chapitre)

    2. soit pour exécuter un bloc de code plusieurs fois via une "boucle" (avec
       "while" et "for", cf. chap. suivant)

Ce site explique très bien le fonctionnement du bloc if (en anglais) :
https://www.learnbyexample.org/python-if-else-elif-statement/
"""

# La structure "if"
####################

"""
Voici une condition "si … alors …". On l'exprime avec le mot-clé "if" :
if <condition>:
    code… (Notez l'indentation en début de ligne !)

<condition> doit être :
    - un booléen…
    - …ou une expression qui retourne un booléen (comme une comparaison ou un
      test d'égalité)

Tout le code indenté sera exécuté si la condition est remplie. Sinon, il sera
ignoré.
"""

une_variable = 5

if une_variable > 10:
    print("une_variable est plus grande que 10")
print("Ceci n'est pas dans le bloc if et sera toujours affiché !")
"""
">" est un opérateur de comparaison, donc l'expression "une_variable > 10"
retournera un booléen.

Le 1er print() ne sera pas exécuté car la condition n'est pas remplie.
Ce code affichera donc juste le 2e print ("Ceci n'est pas dans le bloc if…")
"""

"""
Note : on peut combiner plusieurs conditions dans un "if" avec les opérateurs
booléens

cf. le cours du chap. 9 sur les expressions booléennes :
"""
if une_variable > 3 and une_variable % 2 == 0:
    print("Voilà une condition bien compliquée")
# Le print() ci-dessus sera-t-il affiché si une_variable = 5 ? Pourquoi ?

"""
Attention : si l'expression n'est pas booléenne, le programme se débrouillera
pour transformer ("caster") le résultat en booléen… (cf. chap. 9) avec des
risques de bug.

Donc, toujours utiliser des booléens avec "if" !
"""


# Le mot-clé "else"
####################

# On peut faire plus sophistiqué et rajouter un bloc exécuté si la condition
# N'EST PAS remplie. On utilisera alors "if …: … else: …""
une_variable = 12

if une_variable > 10:
    print("une_variable est plus grande que 10")
else:
    print("une_variable est plus petite ou égale à 10")
print("ceci n'est pas dans le bloc else et sera toujours affiché !")

"""
Ceci affichera :
    - une_variable est plus grande que 10
    - ceci n'est pas dans le bloc else et sera toujours affiché !

Notez bien que :
    - l'exécution passera par exactement une des deux clauses (jamais les deux,
      jamais aucune),
    - "else:" se termine aussi par ":",
    - l'indentation de "else:" commence au même niveau que le if !
"""


# Le mot-clé "elif"
####################

"""
Enfin, on peut compléter cette structure avec "elif". "elif" permet d'ajouter
une autre condition à tester, alors qu'avec "else" le bloc qui est exécuté
quand aucune condition n'est remplie : c'est le cas "par défaut".

Exemple avec cette fonction mathématique f définie par morceaux :
         / 2x + 3   si x < 0
f : x → -  3  − x   si 0 ≤ x < 2
         \\ x² − 3   si x ≥ 2
"""

# On peut reproduire cette fonction avec if …: else if: … else: …
def f(x):
    if x < 0:  # si x est négatif
        return 2 * x + 3
    elif x < 2:  # sinon, SI x < 2 (donc si 0 <= x < 2)
        return 3 - x
    else:  # dans tous les autres cas (donc si x >= 2)
        return x ** 2 - 3
# "else:" ne prend pas de condition !

print(f(-3))  # -3
print(f(1))  # 2
print(f(7))  # 46

"""
Notes :
    - "elif" sert quand on a plus de deux cas possibles,
    - il n'y a pas de limites au nombre de "elif" dans une structure if,
    - on peut utiliser "elif:" sans "else:" : dans ce cas-là il sera possible
      qu'aucune clause ne soit exécutée.
"""

# Ex :
x = 5

if x > 20_000:
    print("x est grand")
elif x < 0.001:
    print("x est tout petit")
"""
Ici rien ne s'affichera car x n'est ni grand ni petit ! pour couvrir le cas
"par défaut" , il faudra ajouter une clause "else".
"""


# Remarques sur l'indentation
##############################

"""
En Python, l'indentation sert à identifier quand on "entre dans" un bloc.
Remarquez que l'indentation augmente après chaque ":".

L'indentation en Python est donc visuelle ET sémantique : utiliser la mauvaise
identation peut créer une erreur pendant l'exécution, voire pire, changer
subtilement le sens du programme !
"""

# Exemple de code contenant un bug :
def lancer_missile():
    # (la définition de fonction crée aussi une nouvelle indentation)
    print("Boom !")

code_saisi = input("Rentrez le code secret pour lancer le missile :")

if code_saisi == "123456":
    print("Code de lancement correct")
lancer_missile()  # => Êtes-vous sûr de l'indentation de cette ligne ?


# "if" imbriqués
#################

"""
Il est tout à fait possible d'imbriquer des if, c'est-à-dire d'avoir des "if
dans des if". Mais on peut parfois les éviter en se débrouillant autrement…
"""

# Ex :
x, y, z = 7, 4, 2

if x > y:
    print(x, " est plus grand que ", y)
    if x > z:
        print(x, " est aussi plus grand que ", z)
# Notez que des if imbriqués nécessitent de bien surveiller l'indentation…

"""
Ça fonctionne très bien, mais on aurait pu se débrouiller avec un seul if, de
la façon suivante :
"""
if x > y and x > z:
    print(x, " est plus grand que ", y, " et ", z)
elif x > y:
    print(x, " est plus grand que ", y)
