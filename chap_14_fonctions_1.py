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
#  Chap. 14     #  Fonctions I : built-ins, définitions, prototypes            #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Définition et utilité d'une fonction
#  - Fonctions Python intégrées
#  - Fonctions définies par l'utilisateur
#  - Où s'arrête une fonction ?
#  - Pourquoi écrire des fonctions ?
#  - Fonctions avec paramètres
#  - Le mot-clé "return"
#  - Prototype d'une fonction
#
##############################################

# Introduction
###############

"""
La fonction est un des deux concepts absolument fondamentaux pour structurer un
programme (l'autre concept étant l'objet).

Le concept est tellement répandu qu'on lui a trouvé plein de synonymes :
méthode, sous-programme ("sub-routine"), procédure, bloc, lambda, macro,
"callable"… Ces mots ont des nuances selon les langages, mais nous retiendrons
le nom "fonction". (Les "lambda" de Python sont vues au chap. 32.)

La fonction est une brique fondamentale de la programmation, quel que soit le
langage. Prenez votre temps pour bien comprendre leur intérêt et leur usage :
ce temps ne sera jamais perdu.

Pour vous mettre en appétit, voici une fonction. Ne cherchez pas encore à
tout comprendre : chaque élément sera expliqué dans la suite du chapitre.
"""


def afficher_gagnant(name, score):
    print(f"bravo {name} tu as gagné !")
    print("Ton score est :")
    print(score)
    print("tu es le meilleur !")

a = afficher_gagnant("olivier", 34)
"""
Cet appel affiche :

bravo olivier tu as gagné !
Ton score est :
34
tu es le meilleur !
"""
print(a)  # => None
"""
Surprise : a ne contient rien ("None") ! C'est parce que afficher_gagnant()
AFFICHE des choses, mais ne RETOURNE aucune valeur. On verra la différence plus
bas avec le mot-clé "return", et la valeur None au chap. 15.
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

En général, une fonction prend une ou plusieurs valeurs en paramètres et
retourne une valeur. Les fonctions en programmation entretiennent donc un
rapport étroit avec leurs consœurs des mathématiques :

    en maths :    f(x) = 2x + 1      f(3) vaut 7
    en Python :   def f(x):
                      return 2 * x + 1
                  f(3)               # => 7

On peut aussi voir une fonction comme une "boîte noire" (ou une recette de
cuisine) : on lui donne des ingrédients (les paramètres), elle fait son
travail, et elle rend un résultat (la valeur de retour).
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
range(3)  # => range(0, 3)
hex(3)    # => '0x3' (cf. chap. 6)
a = len("Une chaîne")
print(a)  # => 10

# Quelques autres built-ins très utiles :
print(abs(-4.5))            # => 4.5 (valeur absolue)
print(max(3, 9, 2))         # => 9 (le plus grand des arguments)
print(min(3, 9, 2))         # => 2 (le plus petit)
print(round(3.14159, 2))    # => 3.14 (arrondi à 2 décimales)
print(type(3.14159))        # => <class 'float'> (cf. chap. 6)
print(int("42") + 1)        # => 43 (conversion, cf. chap. 6 et 11)

"""
L'utilisateur peut utiliser ces fonctions sans savoir comment elles sont
écrites ("implémentées") : il lui suffit de savoir ce qu'elles attendent et ce
qu'elles retournent.

Pour l'appel d'une fonction, on écrit toujours :
    - son nom,
    - des parenthèses, qui contiennent les valeurs qu'on lui passe ("arguments")
      séparées par des virgules. Les parenthèses sont obligatoires, même si
      on ne passe aucune valeur : print() affiche une ligne vide.

La liste complète des built-ins (il y en a environ 70) est disponible ici :
https://docs.python.org/fr/3/library/functions.html

Astuce : dans une console Python, help(max) affiche la documentation de la
fonction max() (cf. chap. 10).
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
    - le mot-clé "def" (pour "define", "définir"),
    - le nom choisi pour la fonction (mêmes règles que pour les noms de
      variables, cf. chap. 10 et chap. 15),
    - entre parenthèses, les paramètres éventuels qu'elle accepte,
    - le caractère ":",
    - puis, sur les lignes suivantes et indenté, le code de la fonction (son
      "corps"), exactement comme pour un bloc "if" (cf. chap. 12).
"""

# Exemple :
def ma_premiere_fonction():
    print("Cette première fonction imprime toujours la même chaîne")
    print("Super !")
print("Ce print s'affiche tout le temps")  # => imprimé (hors de la fonction)

# Puis, comme en maths, on va "appeler" notre fonction en écrivant son nom suivi
# de "()"
ma_premiere_fonction()

# L'appel de cette fonction va lancer l'exécution du code contenu dans la
# définition de la fonction et imprimer :
# => Cette première fonction imprime toujours la même chaîne
# => Super !

# On note que ma_premiere_fonction ne prend aucun paramètre et ne retourne rien.

# Une fois définie, une fonction peut être appelée autant de fois qu'on veut :
ma_premiere_fonction()  # => imprime à nouveau les deux lignes
ma_premiere_fonction()  # => … et encore une fois

"""
IMPT : définir une fonction n'exécute pas son code ! La ligne "def …" ne fait
qu'enregistrer la fonction sous un nom. Le code ne s'exécute qu'au moment de
l'appel, et à chaque appel.

Appeler une fonction AVANT de l'avoir définie provoque une erreur, car Python
lit le fichier de haut en bas et ne connaît pas encore ce nom :
"""
try:
    fonction_pas_encore_definie()
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => NameError: name 'fonction_pas_encore_definie' is not defined


def fonction_pas_encore_definie():
    print("Trop tard !")


fonction_pas_encore_definie()  # => Trop tard ! (maintenant elle existe)

"""
Remarque : comme un bloc "if", le corps d'une fonction ne peut pas être vide.
Si l'on veut définir une fonction qu'on écrira plus tard, on utilise "pass"
(cf. chap. 12) :
"""


def fonction_a_ecrire_plus_tard():
    pass


fonction_a_ecrire_plus_tard()  # ne fait rien, mais ne plante pas


# Où s'arrête une fonction ?
#############################

"""
Comme pour "if" et les boucles, c'est l'INDENTATION qui délimite le corps de
la fonction : la fonction s'arrête à la première ligne qui revient au niveau
d'indentation du "def".
"""


def saluer():
    print("Bonjour !")        # dans la fonction
    print("Comment ça va ?")  # dans la fonction aussi
print("Hors de la fonction")  # => imprimé tout de suite, une seule fois

saluer()
saluer()
"""
Ce code affichera :

Hors de la fonction
Bonjour !
Comment ça va ?
Bonjour !
Comment ça va ?

Le print() non indenté est exécuté au moment où Python lit le fichier, AVANT
les appels : il ne fait pas partie de la fonction.

Les lignes vides ne terminent pas une fonction : seule l'indentation compte.
Par convention (PEP 8), on laisse deux lignes vides avant et après une
définition de fonction, pour bien la distinguer du reste du code.
"""


# Pourquoi écrire des fonctions ?
##################################

"""
Écrire une fonction demande un petit effort au départ. Cet effort est vite
rentabilisé, car un code est lu et modifié bien plus souvent qu'il n'est écrit.

Les avantages des fonctions :

    1. Concision : un bloc de code utilisé à plusieurs endroits n'est écrit
       qu'une seule fois. Le programme est plus court.

    2. Cohérence (une "source unique de vérité", ou "single source of truth") :
       le comportement est défini à UN SEUL endroit. Si l'on doit le
       corriger ou le modifier, on ne le fait qu'une fois, et tous les appels
       en profitent. Avec du code copié-collé, on risque d'oublier une des
       copies, et le programme devient incohérent. C'est le principe "DRY" :
       "Don't Repeat Yourself" ("ne vous répétez pas").

    3. Lisibilité : un nom de fonction bien choisi explique ce que fait le
       code. "calculer_prix_ttc(prix)" se comprend mieux que la formule qu'elle
       contient.

    4. Découpage : on peut décomposer un gros problème en petits problèmes,
       résolus chacun par une fonction, que l'on peut écrire et tester
       séparément (cf. chap. 29 sur les tests).

    5. Rapidité de développement : une fonction déjà écrite et testée peut
       être réutilisée telle quelle, y compris dans d'autres programmes (cf.
       chap. 22 sur les modules).
"""

# Exemple : sans fonction, on répète la même formule (TVA à 20 %)…
prix_livre = 10
prix_stylo = 2
print(prix_livre * 1.2)  # => 12.0
print(prix_stylo * 1.2)  # => 2.4
# … si le taux de TVA change, il faudra modifier CHAQUE ligne.


# Avec une fonction, la formule n'existe qu'à un seul endroit :
def afficher_prix_ttc(prix_ht):
    print(prix_ht * 1.2)  # le taux n'est écrit qu'ici


afficher_prix_ttc(prix_livre)  # => 12.0
afficher_prix_ttc(prix_stylo)  # => 2.4
# (la notion de paramètre, ici prix_ht, est détaillée juste en-dessous)


# Fonctions avec paramètres
############################

"""
Notre première fonction ne prenait aucun paramètre et était donc condamnée à
avoir toujours le même comportement. Mais on peut rendre sa fonction
"configurable" en lui donnant un ou des paramètres.

Un paramètre est une variable, nommée entre les parenthèses du "def", qui
recevra une valeur au moment de l'appel. À l'intérieur de la fonction, on
l'utilise comme n'importe quelle variable.
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
valeurs passées en arguments de l'appel (2 et 3) : parametre1 vaut 2, et
parametre2 vaut 3. C'est l'ORDRE des arguments qui compte : le 1er argument
va dans le 1er paramètre, le 2e dans le 2e, etc.
"""

"""
L'exécution va alors "rentrer" dans la fonction, ce qui donnera :

1er paramètre : 2, 2ème : 3
Leur somme vaut : 5
Leur produit vaut : 6
"""

"""
Ainsi, avec des paramètres de fonction, chaque appel pourra donner un résultat
commun (affichage des paramètres, de leur somme, de leur produit) mais
différent pour chaque appel.
"""

# Exercice : trouvez ce que cet appel va imprimer à l'écran
ma_deuxieme_fonction(3, 5)

# Les arguments peuvent être des valeurs, des variables ou des expressions :
longueur = 4
ma_deuxieme_fonction(longueur, longueur * 2)
# => 1er paramètre : 4, 2ème : 8
# => Leur somme vaut : 12
# => Leur produit vaut : 32

"""
Les noms des paramètres n'ont aucun lien avec les noms des variables passées
en arguments : ci-dessus, la variable "longueur" est passée, mais dans la
fonction, sa valeur s'appelle "parametre1". (La "portée" des variables sera
détaillée au chap. 19.)

Comme Python ne vérifie pas les types, une même fonction peut marcher avec
plusieurs types… ou planter :
"""
ma_deuxieme_fonction(1.5, 2)  # fonctionne avec des floats
# => 1er paramètre : 1.5, 2ème : 2
# => Leur somme vaut : 3.5
# => Leur produit vaut : 3.0

try:
    ma_deuxieme_fonction("a", "b")  # "a" + "b" marche, mais pas "a" * "b"…
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
Remarquez que les deux premières lignes ("1er paramètre : a, 2ème : b" et
"Leur somme vaut : ab") ont bien été imprimées avant l'erreur : la fonction
s'exécute ligne à ligne, jusqu'à ce que l'erreur l'interrompe.
"""


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
    print("Cette fonction n'est pas très intéressante… elle retourne toujours 5.")
    return 5


# On appelle ensuite la fonction : l'exécution "passe dans la fonction"
a = fonction_sans_parametre()
# => Cette fonction n'est pas très intéressante… elle retourne toujours 5.
print(a)  # => 5 (l'appel de la fonction est remplacé par la valeur qu'elle retourne)

# Exemple 2 : on va essayer de faire retourner une valeur différente qui varie
# suivant les paramètres qui sont passés à la fonction
def ajouter_nombres(x, y):
    print(f"On ajoute les nombres {x} et {y}")
    return x + y
    print("Ceci n'est jamais affiché")


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
La valeur retournée peut être utilisée partout où l'on pourrait écrire une
valeur : dans un calcul, une condition, ou même comme argument d'une autre
fonction.
"""
total = ajouter_nombres(1, 2) * 10  # => On ajoute les nombres 1 et 2
print(total)  # => 30 (car l'appel est remplacé par 3, et 3 * 10 = 30)

if ajouter_nombres(2, 2) == 4:  # => On ajoute les nombres 2 et 2
    print("2 + 2 font bien 4")  # => imprimé

print(ajouter_nombres(ajouter_nombres(1, 1), 10))
# => On ajoute les nombres 1 et 1     (l'appel intérieur est exécuté d'abord)
# => On ajoute les nombres 2 et 10
# => 12

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

"""
On peut donc utiliser plusieurs "return" dans une fonction, par exemple un
dans chaque branche d'un "if" : le premier "return" atteint met fin à la
fonction (on l'a déjà vu avec la fonction f(x) "définie par morceaux" du
chap. 12) :
"""


def signe(n):
    if n > 0:
        return "positif"
    if n < 0:
        return "négatif"
    return "nul"  # pas besoin de "else" : si on arrive ici, n vaut 0


print(signe(12))  # => positif
print(signe(-3))  # => négatif
print(signe(0))   # => nul

"""
"return" fonctionne aussi au milieu d'une boucle (cf. chap. 13) : il quitte la
boucle ET la fonction d'un coup.
"""


def premier_multiple(n, debut):
    for i in range(debut, debut + n):
        if i % n == 0:
            return i  # on a trouvé : inutile de continuer la boucle


print(premier_multiple(7, 50))  # => 56

"""
On reverra en détail au chap. 15 la différence entre "return" et print(), qui
est source de nombreuses confusions.
"""


# Prototype d'une fonction
###########################

"""
On a vu qu'une fonction Python pouvait prendre un certain nombre de
paramètres. Le nom d'une fonction, associé à ses paramètres, est appelé son
prototype (on trouvera parfois aussi les termes de "signature", d'"interface",
ou d'"API").

On devra respecter cette interface en appelant la fonction : les valeurs
passées en arguments lors de l'appel de la fonction doivent correspondre à
ses paramètres !
"""

# Ainsi, avec la fonction suivante…
def somme_3_entiers(a, b, c):
    print(a + b + c)

somme_3_entiers(1, 2, 3)  # => 6 (3 arguments pour 3 paramètres : tout va bien)

try:
    # …cet appel générera une erreur TypeError: somme_3_entiers() takes 3
    # positional arguments but 4 were given
    somme_3_entiers(1, 2, 3, 4)
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    # … et de même s'il manque un argument
    somme_3_entiers(1, 2)
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# => TypeError: somme_3_entiers() missing 1 required positional argument: 'c'

"""
Le prototype est donc un "contrat" entre celui qui écrit la fonction et celui
qui l'utilise. Pour l'utiliser correctement, il faut connaître :
    - son nom,
    - ses paramètres (combien, dans quel ordre, de quel type),
    - ce qu'elle retourne (et de quel type).

On documente ce contrat avec une docstring (cf. chap. 3), placée juste sous la
ligne "def". C'est elle que help() affiche :
"""


def aire_rectangle(longueur, largeur):
    """Retourne l'aire d'un rectangle de dimensions longueur × largeur."""
    return longueur * largeur


print(aire_rectangle(3, 4))  # => 12
print(aire_rectangle.__doc__)  # __doc__ contient la docstring de la fonction
# => Retourne l'aire d'un rectangle de dimensions longueur × largeur.

"""
On peut aussi indiquer les types attendus avec des "annotations" (ou "type
hints") : elles ne changent rien à l'exécution, mais documentent le contrat
et aident les éditeurs de texte à détecter les erreurs (cf. chap. 29).
"""


def aire_rectangle_annotee(longueur: float, largeur: float) -> float:
    """Retourne l'aire d'un rectangle de dimensions longueur × largeur."""
    return longueur * largeur


print(aire_rectangle_annotee(2.5, 2))  # => 5.0
