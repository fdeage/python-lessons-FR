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
#  Chap. 12     #  Structures de contrôle I : if, then, else et elif           #
#               #                                                              #
################################################################################
#
#  - La structure "if"
#  - Le mot-clé "else"
#  - Le mot-clé "elif"
#  - Remarques sur l'indentation
#  - Les "one-liner" avec if
#
###########################################################

"""
Normalement, un programme Python est exécuté de haut en bas, ligne à ligne.

C'est le comportement par défaut, mais on peut le modifier avec des structures
de contrôle :
    1. soit pour exécuter un bloc de code seulement sous certaines conditions
       (avec le mot-clé "if", comme on le verra dans ce chapitre)

    2. soit pour exécuter un bloc de code plusieurs fois (avec "while" et "for",
       cf. chap. suivant)
"""

# TODO: https://www.learnbyexample.org/python-if-else-elif-statement/



# La structure "if"
####################

"""
Voici une condition "si … alors …". On l'exprime avec le mot-clé "if" :
if <condition>:
    code… (Notez l'indentation en début de ligne)

La <condition> doit être :
    - un booléen…
    - …ou une expression qui retourne un booléen (comme une comparaison ou un
      test d'égalité)
"""

une_variable = 5

if une_variable > 10:
    print("une_variable est plus grande que 10")
print("Ceci n'est pas dans le bloc if et sera toujours affiché !")
"""
Le 1er print() ne sera pas exécuté car la condition n'est pas remplie.
Ce code affichera donc juste le 2e print ("Ceci n'est pas dans le bloc if…")
"""

"""
Note : on peut combiner plusieurs conditions dans un "if" avec les opérateurs
booléens

cf. le cours du chap. 9 sur les expressions booléennes :
"""
if une_variable > 3 and 3 == 3 and not (une_variable < 2):
    print("Voilà une condition bien compliquée")
# Le print() ci-dessus sera-t-il affiché ? Pourquoi ?


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

# Ceci affichera :
#    - une_variable est plus grande que 10
#    - ceci n'est pas dans le bloc else et sera toujours affiché !


# Le mot-clé "elif"
####################

"""
Enfin, on peut compléter cette structure avec "elif".
"else" introduit un bloc qui est exécuté dès que la condition du "if" n'est
pas remplie.
"elif" permet d'ajouter une condition.

Exemple avec cette fonction mathématique f définie par morceaux
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


print(f(-3))  # -3
print(f(1))  # 2
print(f(7))  # 46

"""
Note : il n'y a pas de limites au nombre de "elif" dans une structure if
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

def lancer_missile():
    print("Boom !")
    # …
    # du code qui lance des missiles


code_saisi = "123465"

if code_saisi == "123456":
    print("Code de lancement correct")
lancer_missile()  # => Êtes-vous sûr de l'indentation de cette ligne ?


# Les "one-liners" avec if
##############################

"""
Un "one-liner" est une expression sophistiquée de Python tenant sur une ligne
(cf. https://wiki.python.org/moin/Powerful%20Python%20One-Liners)

S'il n'y pas de bloc "else" ou "elif", et que le code dans le "if tient sur une
ligne, alors il est possible de tout écrire d'affilée :
"""
t = 5
if t > 2: print(t)  # => 5

"""
Enfin, il est possible d'utiliser un "if ternaire" en mettant un "if / else"
APRÈS la valeur retournée.

C'est à la fois très élégant et très inhabituel, et jamais indispensable : dans
le doute, utilisez la syntaxe classique !
"""
print("yo!" if 0 > 1 else "no!")  # => "no!"

# Cela est exactement la même chose que
if 0 > 1:
    print("yo!")
else:
    print("no!")  # => "no!"
