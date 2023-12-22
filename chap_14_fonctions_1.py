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
#  Chap. 14     #  Fonctions I : built-ins, définitions, prototypes            #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Définition et utilité d'une fonction
#  - Fonctions Python intégrées
#  - Fonctions définies par l'utilisateur
#  - Fonctions avec paramètres
#  - Prototype d'une fonction
#  - Conventions de nommage
#  - Arguments vs paramètres
#  - L'adresse d'une fonction
#
#########################################################

# Introduction
###############

"""
La fonction est un des deux concepts absolument fondamentaux pour structurer un
programme (l'autre concept étant l'objet).

Le concept est tellement repandu qu'on lui a trouvé plein de synonymes :
method, sub-routine, co-routine, procedure, block, lambda, macro, callable…

La fonction est une brique fondamentale de la programmation, quel que soit le
langage. Prenez votre temps pour bien comprendre leur intérêt et leur usage :
ce temps ne sera jamais perdu.
"""


# Définition et utilité d'une fonction
#######################################

"""
Une fonction est un bloc de code nommé, paramétrable et utilisable à d'autres
endroits du programme.

On utilise essentiellement les fonctions pour :
    1. décomposer un programme complexe en une série de blocs plus simples,
    2. isoler un ensemble de lignes de code pour le mettre en commun entre
       plusieurs endroits du programme.

En général, une fonction prend un ou plusieurs valeurs en paramètres et
retourne une valeur. Les fonctions en programmation entretiennent donc un
rapport étroit avec leurs consoeurs des mathématiques.
"""


# Fonctions Python intégrées
#############################

"""
Python propose des fonctions intégrées, accessibles depuis n'importe où dans
le programme : on les appelle aussi "built-ins".
"""

# On a vu certains de ces built-ins : input(), print(), range()…
# nom = input("Quel est ton nom ? ")
# print(nom)
range(3)
hex(3)
len("Une chaîne")

"""
L'utilisateur peut utiliser ces fonctions sans savoir comment elles sont
écrites (codées).
"""


# Fonctions définies par l'utilisateur
#######################################

"""
L'utilisateur a aussi la possibilité d'ajouter ses propres fonctions à la
liste des fonctions intégrées à Python.

Une fonction utilisateur doit être définie (écrite) avant d'être appelée
(utilisée) : après l'avoir nommée et défini son comportement, l'utilisateur
peut appeler sa fonction.

Pour définir une fonction, il faut dans l'ordre :
    - le mot-clé "def"
    - le nom choisi pour la fonction
    - entre parenthèses, les paramètres éventuels qu'elle accepte,
    - le caractère ":"
"""

# Exemple :
def ma_premiere_fonction():
    print("Cette première fonction imprime toujours la même chaîne")


# Puis, comme en maths, on va "appeler" notre fonction en écrivant son nom suivi
# de "()"
ma_premiere_fonction()

# L'appel de cette fonction va lancer l'exécution du code contenu dans la
# définition de la fonction et imprimer :
"Cette première fonction imprime toujours la même chaîne"

# On note que ma_premiere_fonction ne prend aucun paramètre et ne retourne rien.


# Fonctions avec paramètres
############################

"""
Notre première fonction ne prenait aucun paramètre et était donc condamnée à
avoir toujours le même comportement. Mais on peut rendre sa fonction
"configurable" en lui donnant un ou des paramètres.
"""


def ma_deuxieme_fonction(parametre1, parametre2):
    print(f"1er paramètre : {parametre1}, 2ème : {parametre2}")
    print(f"Leur somme vaut : {parametre1 + parametre2}")
    produit = parametre1 * parametre2
    print(f"Leur produit vaut : {produit}")
"""
IMPT : on rappelle que ce code ne fait que définir une fonction : tant qu'on
ne l'aura pas appelée, le code contenu à l'intérieur ne sera pas exécuté !
"""

# Prenez quelques secondes pour imaginer ce que fera l'appel suivant…
ma_deuxieme_fonction(2, 3)

"""
Réponse :
On remplace les paramètres dans la définition de la fonction par les
valeurs passées en arguments de l'appel (2 et 3)
"""

"""
L'exécution va alors "rentrer" dans la fonction, ce qui donnera :

"1er paramètre : 2, 2ème : 2"
"Leur somme vaut : 5"
"Leur produit vaut : 6"
"""

"""
Ainsi, avec des paramètres de fonction, chaque appel pourra donner un résultat
commun (affichage des paramètres, de leur somme, de leur produit) mais
différent pour chaque appel.
"""

# Exercice : trouvez ce que cet appel va imprimer à l'écran
ma_deuxieme_fonction(3, 5)


# Prototype d'une fonction
###########################

"""
On a vu qu'une fonction Python pouvait prendre un certain nombre de
paramètres. Le nom d'une fonction, associé à ses paramètres, est appelé son
prototype (on trouvera parfois aussi son "interface", ou son "API").

On devra respecter cette interface en appelant la fonction : les valeurs
passées en arguments lors de l'appel de la fonction doivent correspondre à
ses paramètres !
"""

# Ainsi, avec la fonction suivante…
def somme_3_entiers(a, b, c):
    print(a + b + c)

try:
    # …cet appel générera une erreur TypeError: somme_3_entiers() takes 3
    # positional arguments but 4 were given
    somme_3_entiers(1, 2, 3, 4)
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Conventions de nommage
#########################

# Comme pour les variables, on peut appeler sa fonction comme on veut,
# mais on a tendance à suivre certaines conventions :
def jolie_fonction():
    print("Minuscules et underscores, tout va bien.")


def jolie_fonction_2():
    print("On peut ajouter des chiffres à la fin, après un underscore")


def FonctionTrèsMoche():
    print("Moche ! Il faut éviter les majuscules et les accents")
    print("Il faut aussi séparer les mots par des underscores")


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


# L'adresse d'une fonction
################################

def test_adresse():
    print("yolo")

# On pourra être décontenancé si l'on oublie les parenthèses lors d'un appel…
print(test_adresse)  # => <function test_adresse at 0x1097679d0>

"""
Explication : sans les parenthèses, on n'imprimera pas la valeur retourné par la
fonction au moment de l'appel, mais… l'adresse en mémoire où est stockée la
fonction ! (par convention cette adresse est écrite en hexadécimal)
"""

# On découvrira plus tard que cette adresse peut être affectée à une variable,
# comme n'importe quelle valeur !
a = test_adresse
print(a)     # => <function test_adresse at 0x1097679d0>

# a est une variable contenant une fonction…
type(a)  # => <class 'function'>
# …et cette fonction peut être exécutée !
a()      # => 'yolo'
