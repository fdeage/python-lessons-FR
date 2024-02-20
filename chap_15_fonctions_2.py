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
#  Chap. 15     #  Fonctions II : valeurs de retour                            #
#               #                                                              #
################################################################################
#
#  - Conventions de nommage
#  - Arguments vs paramètres
#  - La valeur None
#  - Différence entre return et print()
#  - Imbrication de fonctions
#  - Retour multiple
#  - L'adresse d'une fonction
#
#############################################

# Conventions de nommage
#########################

"""
Comme pour les variables, on peut appeler sa fonction comme on veut,
mais on a tendance à suivre des conventions. Il est recommandé de suivre la
convention que l'on utilise pour les variables (cf. chap. 10).
"""
# Snake Case
def jolie_fonction():
    print("Minuscules et underscores, tout va bien.")


# Camel Case
def JolieFonction2():
    print("On peut ajouter des chiffres à la fin")


def FonctION_TRÈS_Moche():
    print("Moche ! Il faut éviter les accents, ainsi que mélanger les styles")


# Arguments vs paramètres
###############################

"""
cf. https://docs.python.org/3/faq/programming.html#what-is-the-difference-between-arguments-and-parameters

Quelle différence existe-t-il entre arguments ou paramètres ? Vous entendrez
et lirez parfois les deux… Il y a en fait une confusion à éviter : on parle
de paramètres pendant la définition de la fonction, et d'arguments au moment
de l'appel.

En bref, les paramètres d'une fonction définissent le type d'arguments qu'une
fonction peut accepter.

Exemple :

def test(argA, argB):
    …
=> argA et argB sont les paramètres de la fonction

test(1, 2)
=> 1 et 2 sont les arguments de l'appel
"""


# La valeur None
#################

"""
None est une valeur particulière en Python : elle désigne… l'absence de valeur.

On obtient la valeur None quand une fonction ne retourne rien :
    - soit quand il manque le mot-clé "return" à là fin d'une fonction,
    - soit quand ce mot-clé n'est pas associé à une valeur.
"""

# Exemple :
def fonction_sans_retour():
    2 + 3  # on oublie "return" devant 2 + 3…


print(fonction_sans_retour())  # => None

# Exemple :
def fonction_sans_valeur_de_retour():
    2 + 3
    return

print(fonction_sans_valeur_de_retour())  # => None

"""
Attention : pour tester si une fonction retourne None, on utilisera
"… is None" au lieu # de "… == None"
"""
fonction_sans_retour() is None  # => True

"""
Remarque : évidemment, on obtiendra le même résultat si on essaie d'affecter la
valeur de retour à une variable
"""
a = fonction_sans_retour()
print(a)  # => None

# Remarque : on aura le même résultat si on utilise un return "vide"
def fonction_avec_retour_vide(a):
    if a < 0:
        return
    return a

print(fonction_avec_retour_vide(17))  # => 17
print(fonction_avec_retour_vide(-4))  # => None

# Remarquez que None est différent de 0…
print(None == 0)  # => False
# … et que None est aussi différent de False
print(None == False)  # => False

"""
Attention : si None est testé dans une expression booléenne, il sera converti en
False, comme le montre l'exemple suivant
"""
def f():
    return


if f():
    print("a")  # => pas imprimé
else:
    print("b")  # => imprimé


# Différence entre return et print()
#####################################

"""
On voit souvent les nouveaux programmeurs Python confondre return et print().

Ayez bien en tête ce qu'ils font tous les deux :
    - "return" est un mot-clé qui permet de retourner une valeur depuis une
      fonction : l'appel de fonction sera remplacé par la valeur retournée
    - print() est une fonction intégrée qui permet d'afficher une valeur à
      l'écran.
"""

# Exemple :
def un_calcul(x, y, z):
    return x * y + z


"""
Ici la fonction un_calcul() n'imprime rien car elle ne contient aucun appel
à print(). Elle se contente de retourner un résultat.
"""
resultat = un_calcul(2, 3, 5)  # rien n'est imprimé à l'écran…

# …donc il faudra ensuite utiliser print() pour imprimer ce résultat
print(resultat)  # => 11

# On aurait pu aussi gagner du temps en mettant le print() dans la fonction
def un_calcul(x, y, z):
    print(x * y + z)


n = un_calcul(2, 3, 5)  # => 11

# La fonction un_calcul() ne retourne rien, donc n contient None
print(n)  # => None

# Autre exemple
def retours_multiples(param):
    if param % 2 == 0:
        return "pair"
    print("Ceci ne sera pas imprimé si param est pair, car return quitte la fonction")
    return "impair"


# Le premier appel imprimera "pair"
retours_multiples(2)

"""
Le deuxième appel imprimera :
"Pas imprimé si parametre est pair, car return quitte la fonction".

Remarquez que "impair" ne sera pas imprimé !
"""
retours_multiples(3)


# Imbrication de fonctions
###########################

# Jeu : tentez de simuler ce que va imprimer le programme suivant
def a():
    print("toto")
    return "tutu"


def b():
    print("titi")
    print(a())
    return "tyty"
    print("tutu")


def c():
    print("tata")
    b()
    print(b())
    return "tete"


print(c())

"""
Réponse :

tata
titi
toto
tutu
titi
toto
tutu
tyty
tete
"""


# Retour multiple
##################

"""
On a vu qu'une fonction pouvait prendre plusieurs variables en paramètres. On
va voir qu'elle peut aussi retourner plusieurs valeurs en utilisant un tuple
(cf. chap. 17 sur les tuples)
"""


def retour_multiple_1(parametre):
    valeur1 = parametre * 2
    valeur2 = parametre + 8
    valeur3 = parametre / 3
    return (valeur1, valeur2, valeur3)  # Ceci est un tuple


# On peut affecter ces valeurs à une variable qui contiendra le tuple
retours = retour_multiple_1(2)
type(retours)  # => <class 'tuple'>

print(retours)  # (4, 10, 0.6666666666666666)
print(retours[0])  # => 4
print(retours[1])  # => 10
print(retours[2])  # => 0.6666666666666666

# Enfin, on peut les affecter directement à plusieurs valeurs
def retour_multiple_2(parametre):
    valeur1 = parametre < 0
    valeur2 = f"Ce parametre vaut {parametre}"
    return valeur1, valeur2  # => les parenthèses autour du tuple sont optionnelles


a, b = retour_multiple_2(-2)
print(a)  # => True
print(b)  # => Ce parametre vaut -2


# L'adresse d'une fonction
################################

# Ceci n'est pas à comprendre absolument !

def test_adresse():
    print("yolo")

# On pourra être décontenancé si l'on oublie les parenthèses lors d'un appel…
print(test_adresse)  # => <function test_adresse at 0x1097679d0>

"""
Explication : sans les parenthèses, on n'imprimera pas la valeur retourné par la
fonction au moment de l'appel, mais… l'adresse en mémoire où est stockée la
fonction ! (par convention, cette adresse est écrite en hexadécimal)
"""

# On découvrira plus tard que cette adresse peut être affectée à une variable,
# comme n'importe quelle valeur !
a = test_adresse
print(a)     # => <function test_adresse at 0x1097679d0>

# a est une variable contenant une fonction…
type(a)  # => <class 'function'>
# …et cette fonction peut être exécutée !
a()      # => 'yolo'
