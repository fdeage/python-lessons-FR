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
#  - Le mot-clé "return"
#  - Prototype d'une fonction
#
#########################################################

# Introduction
###############

"""
La fonction est un des deux concepts absolument fondamentaux pour structurer un
programme (l'autre concept étant l'objet).

Le concept est tellement repandu qu'on lui a trouvé plein de synonymes :
method, sub-routine, co-routine, procedure, block, lambda, macro, callable…
nous retiendrons le nom "fonction".

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
écrites ("implémentées").
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
    print(f"Leur produit vaut : {parametre1 * parametre2}")
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


# Le mot-clé "return"
######################

"""
Le mot-clé "return" est la dernière brique conceptuelle pour comprendre les
fonctions. C'est aussi la plus "magique", et celle qui pose le plus de
difficultés au début !

En bref :
Toute fonction a la possibilité de "retourner" une valeur avec "return".

Au moment où on exécute le programme, ce mot-clé "return" :
    1. quitte la fonction en cours,
    2. revient au code qui a appelé la fonction,
    3. remplace l'appel de fonction par la valeur donnée à "return"
"""

# Exemple 1 : une fonction qui retourne toujours 5
def fonction_sans_parametre():
    print(f"Cette fonction n'est pas très intéressante… elle retourne toujours 5.")
    return 5


# On appelle ensuite la fonction : l'exécution "passe dans la fonction"
a = fonction_sans_parametre()
# => "Cette fonction retourne toujours 5. Elle n'est pas très intéressante…"
print(a)  # => 5 (l'appel de la fonction est remplacé par la valeur qu'elle retourne)

# Exemple 2 : on va essayer de faire retourner une valeur différente qui varie
# suivant les paramètres qui sont passés à la fonction
def ajouter_nombres(x, y):
    print(f"On ajoute les nombres {x} et {y}")
    return x + y


# On appelle la fonction dans notre code, avec 5 et 6 en paramètre
somme = ajouter_nombres(5, 6)

"""
À ce moment-là, le programme va "rentrer" dans la fonction et remplacer x et
y par 5 et 6.

L'appel à print() deviendra :
"On ajoute les nombres 5 et 6"

Enfin, l'appel de fonction est remplacé à l'exécution par 11.
"""
print(somme)  # => 11

"""
IMPT : il faut noter que "return" interrompt toujours l'exécution de la
fonction : les lignes situées en-dessous ne seront pas exécutées !

Exemple 3 : du code inutile (non-exécuté)
"""

def dire_si_negatif(a):
    if a < 0:
        return True
        print(f"{a} est négatif")  # Ce print() ne sera jamais exécuté
    else:
        return False
        print(f"{a} est positif ou nul")  # Celui-ci est inutile aussi
    print(
        'Comme chaque branche du "if" ci-dessus contient un return, ce \
    code ne sera jamais exécuté'
    )


# Les deux appels ci-dessous n'imprimeront rien
x = dire_si_negatif(-7)
y = dire_si_negatif(13)

# Il faudra donc imprimer le contenu de x et y avec print()
print(x)  # => True
print(y)  # => False


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

