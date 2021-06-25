################################################################################
#                                                                              #
#  NNNN    NNN    SSSSSS.   IIIII   (inspiré de https://learnxinyminutes.com)  #
#  NNNNN   NNN  SSSS  SSSS   III                                               #
#  NNNNNN  NNN  SSSS         III    Licence : CC BY-SA 4.0 FR                  #
#  NNNNNNN NNN   SSSSSS      III    Félix Déage - MMXXI                        #
#  NNN NNNNNNN      SSSSS    III                                               #
#  NNN  NNNNNN        SSSS   III    Cours Python - 1ère - v.3.5                #
#  NNN   NNNNN  SSSS  SSSS   III                                               #
#  NNN    NNNN   SSSSSSSS   IIIII                                              #
#                                                                              #
################################################################################
#               #                                                              #
#  Part. XVII   #  erreurs et exceptions                                       #
#               #                                                              #
################################################################################

"""
Note : ce fichier n'est pas exécutable, car le code ci-dessous va créer EXPRÈS
des erreurs à l'exécution, dont certaines ne sont pas "interceptables" avec
"try... except".
"""

##################################################
# 23. Erreurs et exceptions                      #
##################################################
#
#  - Le mécanisme des erreurs en Python
#  - Sources d'erreurs fréquentes
#  - Gérer les erreurs avec try: ... except: ...
#  - Quand laisser crasher ?
#
##################################################

# Le mécanisme des erreurs en Python
#####################################

"""
Une erreur est un événement généré par Python qui va interrompre l'exécution
normale du programme.

En l'absence d'une gestion d'erreur dédiée, le programme va "crasher", càd
quitter après avoir affiché un message d'erreur.

Il y a deux sources possibles à une erreur :
    1. Python a rencontré une situation imprévue dans laquelle il ne sait pas
       comment continuer une exécution normale (c'est souvent le signe qu'une
       situation n'a pas été prévue par le programmeur).

Exemple : quand survient une division par 0 :
"""
for i in range(6):
    print(1 / (5 - i))
# Attention : ce code va créer une erreur ZeroDivisionError quand i vaudra 5

"""
    2. il est aussi possible de créer ("soulever") soi-même une erreur avec le
       mot-clé"raise" :
"""
raise ZeroDivisionError     # => soulève la même erreur manuellement

# On peut même rajouter un message d'erreur pour l'utilisateur
raise IndexError("Ne dépasse pas l'indice de la liste plz 😡")

"""
Il y a deux issues possibles à la survenue d'une erreur :
    1. soit l'erreur est interceptée (avec try: ... except: ...)
    2. soit l'erreur n'est pas interceptée et crashe le programme.

Il n'y a pas de "meilleure" solution pour gérer l'erreur : en fonction de la situation et du programme, il peut être souhaitable de laisser crasher
("live or let die").
"""


# Causes fréquentes d'erreurs
##############################

"""
Certaines sont très classiques (SyntaxError, dépasser les limites d'une liste,
appeler une méthode de liste sur une string, etc.). D'autres sont beaucoup plus
rares.
"""

#   1. Dépasser les limites d'une liste
depassement = [1, 2, 3]
depassement[42]  # => IndexError: list index out of range

#   2. Utiliser une méthode qui n'existe pas pour un objet
"abc".bizarre()  # => AttributeError: 'str' object has no attribute 'bizarre'

#   3. Utiliser une variable du mauvais type (ici un int au lieu d'une string)
"Hello " + 42    # => TypeError: can only concatenate str (not "int") to str

#   4. Faire une conversion impossible entre deux types
int("abc")       # => ValueError: invalid literal for int() with base 10: 'abc'

#   5. Utiliser une variable non-définie
a += 1           # => NameError: name 'a' is not defined

#   6. Utiliser un mot-clé non-défini
iff True:      # => SyntaxError: invalid syntax (iff)
    print("Ceci n'est pas un if")

#   7. Utiliser une valeur qui n'est pas dans une liste
l2 = [1]
l2.remove(2)   # ValueError: list.remove(x): x not in list

#   8. Référencer une valeur qui n'est pas dans un dictionnaire
d = {0: "zéro", 1: "un"}
d[2]           # => KeyError: 2

#   9. Se tromper d'indentation en début de ligne
  a = 1         # => IndentationError: unexpected indent

# TODO: ImportError, FileNotFoundError, ArithmeticError, AssertionError

"""
Il y a des dizaines d'autres erreurs et il ne sert à rien de toutes les
connaître. Mais il faut BIEN LIRE LES MESSAGES D'ERREURS : ils vous sauveront
souvent...
"""

# Gérer les erreurs avec try: ... except: ...
##############################################

"""
Pour intercepter une erreur, on utilisera les mots-clés "try" et "except",
que l'on mettra "autour" du code qui peut créer une erreur
"""
try:
    for i in range(6):
        print(1 / (5 - i))
except ZeroDivisionError:
    # Ici on met le code qui doit "sauver" l'exécution du programme
    print(f"Division par 0 avec {i}")
else:   # clause optionnelle, exécutée s'il n'y a PAS d'erreur
    print(f"Pas de division par 0 avec {5 - i}, cool !")

"""
Notez qu'on ne "catche" QUE les ZeroDivisionError : si on en rencontre d'autres,
elles feront planter le programme !

On peut dire à except d'intercepter plusieurs types d'erreurs :
"""

# TODO
try:
    for i in range(6):
        print(1 / (5 - i))
except ZeroDivisionError:
    print(f"Division par 0 avec {i}")
except AssertionError:
    print("Une assertion a planté")
except:
    print("Toutes les autres erreurs")
else:
    # clause optionnelle, exécutée s'il n'y a PAS d'erreur



try:
    une_fonction_qui_peut_creer_des_erreurs()
except (TypeError, NameError):
    print("TypeError et NameError ne nous gênent pas ici, on passe")

# Exemple de gestion d'erreurs d'une saisie utilisateur
while True:
    age = input('Quel est votre âge ? ')
    try:
        # int() peut créer une erreur si on lui passe une chaîne absurde
        age = int(age)
    except ValueError:
        print('Vous devez utiliser des chiffres.')
    else:
        break # Ceci permet de sortir de la boucle while

"""
HP : Pour catcher TOUTES les erreurs possibles, on peut utiliser cette syntaxe :
"""
try:
    fonction_qui_peut_planter()
# except TypeError as err:
except _ as err:
# except:   #  TOUT catcher
    print("Erreur ! Erreur ! Erreur !")
    pass


# Live and let die : quand laisser crasher ?
#############################################

"""
Que l'erreur ait été soulevée par le programme ou par "raise", cette erreur
va, par défaut, interrompre le programme. Si l'on souhaite empêcher cette
interruption, il faut demander à Python "d'intercepter" l'erreur.

Savoir quelle erreur intercepter et laquelle faire crasher le programme
n'est pas évident... ce sera à vous de décider à chaque fois !

Certains programmes critiques ne doivent JAMAIS être interrompus
(pacemakers, centrales nucléaires, ordinateur de bord d'avion, réseaux
électriques...).

Pour beaucoup d'autres (serveurs web, ordinateurs personnels, jeux...), il
est plus simple de laisser le programme crasher et le relancer ensuite.
"""

"""
Parfois la solution est de laisser crasher/éteindre puis relancer. C'est la
raison pour laquelle la première question qu'un spécialiste répond quand on a
un problème d'informatique est :

"Avez-vous essayé d'éteindre et de rallumer votre ordinateur ?"
"""
