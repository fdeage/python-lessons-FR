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
#  Chap. 15     #  Fonctions II : valeurs de retour                            #
#               #                                                              #
################################################################################
#
#  - Le mot-clé "return"
#  - La valeur None
#  - Différence entre return et print()
#  - Imbrication de fonctions
#  - Retour multiple
#
#############################################

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
