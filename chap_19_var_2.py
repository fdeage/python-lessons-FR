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
#  Chap. 19     #  Variables II : portée et namespaces                         #
#               #                                                              #
################################################################################
#
#  - Rappel sur les variables
#  - Les 4 portées possibles d'une variable
#  - Conflit de variables
#  - todo: namespaces
#
#############################################

# Rappel sur les variables
###########################

"""
On rappelle qu'une variable est un nom (ou "symbole") associé à un espace en
mémoire où l'on peut stocker une valeur d'un certain type (int, float, tuple,
etc.).
"""

ma_super_variable = 37
"""
À l'exécution du programme, Python va associer le nom "ma_super_variable" à
une zone de la mémoire qui contient une valeur :
    - cette valeur est de type "int",
    - elle vaut 37.
"""

# Mais ce nom n'a de sens que dans un certain contexte. Ainsi ceci soulèvera
# une erreur à l'exécution
try:
    une_variable["test"] = 1
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
une_variable = {}

"""
En effet, il faudrait intervertir les deux lignes ci-dessus pour déclarer la
variable une_variable  AVANT de l'utiliser : l'association ("binding") entre
le symbole "une_variable" et un dictionnaire vide n'existe pas tant qu'on ne
l'a pas créée.
"""


# Les 4 portées possibles d'une variable
#########################################

"""
La portée d'une variable est, en gros, l'espace dans lequel elle est associée
à une valeur : c'est donc l'espace où elle est reconnue et utilisable. En
anglais, on l'appellera son "scope".

Il y a 4 types de portée pour une variable, que l'on listera ici avec leur
portée respective (par portée décroissante) :

    1. Variable globale : tout le fichier, depuis sa déclaration
    2. Argument de fonction : toute la fonction
    3. Variable locale : la fonction où la variable est déclarée, depuis
       sa déclaration
    4. Variable de boucle : seulement la boucle concernée


Considérons maintenant ces 4 portées dans le détail :

    1. Les variables globales

       Une variable déclarée en dehors d'une fonction est accessible dans tout
       le fichier, à partir de sa ligne de déclaration. Elle est alors dite
       "globale".

       IMPT : on évitera au maximum les variables globales : le fait qu'elles
       soient utilisables partout pose en fait plus de problèmes qu'autre
       chose. Notamment, il devient difficile de :
         - simuler le fonctionnement du programme dans sa tête
         - identifier la ligne de code qui pose problème en cas de bug
           ("débugger" le programme)
"""


# Par exemple, cette variable est globale, c'est-à-dire accessible dans tout le
# code écrit en-dessous d'elle.
GLOB = 3
# Note : on écrira souvent les variables globales en majuscules.

"""
    2. Les arguments d'une fonction, tout comme les variables définies à
       l'intérieur de celle-ci, n'ont pas de signification en dehors de la
       fonction.
"""

def une_fonction_avec_parametre(super_parametre):
    print(super_parametre)


# super_parametre est remplacé par 3 à l'exécution : ceci imprimera 3…
une_fonction_avec_parametre(3)

# … mais ceci créera une erreur ("… not defined"). Pourquoi ?
try:
    print(super_parametre)  # Erreur
except NameError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# Réponse : super_parametre n'a pas d'existence hors de la fonction.

"""
    3. Les variables locales sont déclarées dans une fonction. Leur portée
       commence à leur ligne de déclaration
"""

# On rappelle que g est une variable globale définie plus haut
def une_fonction(a):
    print(f"a = {a}")  # a est accessible dans toute la fonction
    l = 4
    print(f"l = {l}")  # l est locale donc accessible seulement après
    # "l = 4"
    print(f"GLOB = {GLOB}")  # GLOB est globale donc accessible partout
    for i in range(3):
        print(f"i = {i}")  # i n'est accessible que dans cette boucle


# On appelle cette fonction en lui passant un paramètre
une_fonction(12)
"""
Cet appel imprimera :

a =  12
l = 4
GLOB = 3
i = 0
i = 1
i = 2
"""

# Les variables a, l et i n'existent pas en dehors de la fonction
try:
    print(a)  # => NameError: name 'a' is not defined
    print(l)  # => NameError: name 'l' is not defined
    print(i)  # => NameError: name 'i' is not defined
except NameError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
    4. Enfin, les variables de boucle n'existent que dans la boucle. Dans
       l'exemple plus haut, la variable i existe dans la boucle for…

       for i in range(2):
            …

       …mais ni au-dessus ni en-dessous de cette boucle.
"""


# Conflit de variables
#######################

"""
Il peut arriver que deux variables avec des portées différentes entrent en
conflit : la dernière variable va alors "remplacer" l'autre.
"""

# Exemple :
x = 5  # x est global

def definir_variable_locale(num):
    x = num
    # x est local : ce n'est pas le même que le x global plus haut
    return x

print(definir_variable_locale(43))  # => 43
print(x)  # => 5 car le x de la fonction est différent du x global

# Pour s'assurer que c'est bien la variable globale qui est modifiée, on
# utilisera le mot-clé "global"

y = 6

def definir_variable_globale(num):
    global y
    print(y)  # => 6
    y = num   # La variable globale y vaut maintenant 6
    print(y)  # => 25

definir_variable_globale(25)
