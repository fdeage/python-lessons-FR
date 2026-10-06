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
#  Chap. 19     #  Variables II : portée et namespaces                         #
#               #                                                              #
################################################################################
#
#  - Rappel sur les variables
#  - Les 4 portées possibles d'une variable
#  - Conflit de variables
#  - Les namespaces
#  - Bonnes pratiques
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

Il y a 4 types de portée pour une variable en Python, que l'on retient souvent
avec l'acronyme "LEGB" (de la plus restreinte à la plus large) :

    1. L comme "Local" : les variables locales et les paramètres d'une
       fonction, utilisables seulement DANS cette fonction
    2. E comme "Enclosing" (englobante) : les variables d'une fonction qui en
       contient une autre (une fonction définie DANS une autre fonction)
    3. G comme "Global" : les variables déclarées dans le fichier, en dehors de
       toute fonction, utilisables dans tout le fichier depuis leur déclaration
    4. B comme "Built-in" (intégrée) : les noms fournis par Python lui-même,
       utilisables partout : print, len, range, int, True…

IMPT : quand Python rencontre un nom, il le cherche DANS CET ORDRE : d'abord
en local, puis dans la fonction englobante, puis en global, et enfin parmi les
noms intégrés. S'il ne le trouve nulle part : NameError.

Attention : contrairement à beaucoup d'autres langages (C, Java, JavaScript
avec "let"…), il n'y a PAS de portée propre aux boucles ou aux "if" en Python
(voir plus bas, point 5).


Considérons maintenant ces portées dans le détail :

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
         - réutiliser une fonction ailleurs, puisqu'elle dépend d'une variable
           qui n'existe que dans ce fichier
"""


# Par exemple, cette variable est globale, c'est-à-dire accessible dans tout le
# code écrit en-dessous d'elle.
GLOB = 3
# Note : on écrira souvent les variables globales en majuscules (cf. chap. 10).
# Ce sont en général des CONSTANTES, càd des valeurs qu'on ne modifie jamais.

"""
    2. Les arguments d'une fonction, tout comme les variables définies à
       l'intérieur de celle-ci, n'ont pas de signification en dehors de la
       fonction.
"""

def une_fonction_avec_parametre(super_parametre):
    print(super_parametre)


# super_parametre est remplacé par 3 à l'exécution : ceci imprimera 3…
une_fonction_avec_parametre(3)  # => 3

# … mais ceci créera une erreur ("… not defined"). Pourquoi ?
try:
    print(super_parametre)  # Erreur
except NameError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# Réponse : super_parametre n'a pas d'existence hors de la fonction.

"""
    3. Les variables locales sont déclarées dans une fonction. Leur portée
       commence à leur ligne de déclaration, et se termine à la fin de la
       fonction.

       Chaque APPEL de la fonction crée de nouvelles variables locales, qui
       disparaissent à la fin de l'appel : une fonction ne "se souvient" pas
       de ses variables locales d'un appel à l'autre.
"""

# On rappelle que GLOB est une variable globale définie plus haut
def une_fonction(a):
    print(f"a = {a}")  # a est accessible dans toute la fonction
    l = 4
    print(f"l = {l}")  # l est locale donc accessible seulement après
    # "l = 4"
    print(f"GLOB = {GLOB}")  # GLOB est globale donc accessible partout
    for i in range(3):
        print(f"i = {i}")
    print(f"i après la boucle = {i}")  # i existe encore ! (cf. point 5)


# On appelle cette fonction en lui passant un paramètre
une_fonction(12)
"""
Cet appel imprimera :

a = 12
l = 4
GLOB = 3
i = 0
i = 1
i = 2
i après la boucle = 2
"""

# Les variables a, l et i n'existent pas en dehors de la fonction
try:
    print(a)  # => NameError: name 'a' is not defined
    print(l)  # (ces 2 lignes ne sont pas exécutées : l'erreur sur a interrompt
    print(i)  # le bloc try, mais elles créeraient la même erreur)
except NameError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# Une variable locale n'est utilisable qu'APRÈS sa déclaration
def utilise_trop_tot():
    print(locale_tardive)
    locale_tardive = 1

try:
    utilise_trop_tot()  # => UnboundLocalError (un cas particulier de NameError)
except NameError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
    4. Les variables englobantes ("enclosing") : si on définit une fonction à
       l'intérieur d'une autre, la fonction intérieure peut LIRE les variables
       de la fonction extérieure.
"""

def exterieure():
    message = "bonjour"  # locale pour exterieure(), englobante pour interieure()

    def interieure():
        print(message)   # trouvée dans la portée englobante (le "E" de LEGB)

    interieure()

exterieure()  # => bonjour

"""
    5. Les variables de boucle : en Python, une boucle (ou un "if") ne crée PAS
       de nouvelle portée. La variable d'une boucle for appartient donc à la
       portée où se trouve la boucle (locale dans une fonction, globale sinon),
       et elle CONTINUE D'EXISTER après la boucle, avec sa dernière valeur.

       for i in range(2):
            …
       print(i)  # => 1

       C'est ce qu'on a vu avec "i après la boucle = 2" plus haut. C'est
       une source de bugs classique : évitez de réutiliser une variable de
       boucle après la boucle.
"""
for compteur in range(5):
    pass
print(compteur)  # => 4 : compteur est une variable globale de ce fichier !

if True:
    dans_un_if = "visible"
print(dans_un_if)  # => visible : un "if" ne crée pas de portée non plus

"""
    6. Les noms intégrés ("built-in") : print, len, range, int, str, list,
       True, None… sont disponibles partout, sans rien déclarer. On verra
       dans la section "Les namespaces" qu'ils sont rangés dans un module
       spécial, nommé "builtins".
"""


# Conflit de variables
#######################

"""
Il peut arriver que deux variables avec des portées différentes portent le même
nom : la variable la plus "proche" (dans l'ordre LEGB) va alors "masquer"
l'autre. On dit en anglais qu'elle lui fait de l'ombre ("shadowing").
"""

# Exemple :
x = 5  # x est global

def definir_variable_locale(num):
    x = num
    # x est local : ce n'est pas le même que le x global plus haut
    return x

print(definir_variable_locale(43))  # => 43
print(x)  # => 5 car le x de la fonction est différent du x global

"""
IMPT : dès qu'une fonction AFFECTE une valeur à un nom (avec "="), ce nom est
local pour TOUTE la fonction. C'est pourquoi le code ci-dessous plante : Python
considère que compteur_global est local (il y a un "=" plus bas), et il n'a
pas encore de valeur au moment de la lecture.
"""
compteur_global = 0

def incrementer():
    compteur_global = compteur_global + 1  # lecture d'un local pas encore défini

try:
    incrementer()
except UnboundLocalError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

# Pour s'assurer que c'est bien la variable globale qui est modifiée, on
# utilisera le mot-clé "global"

y = 6

def definir_variable_globale(num):
    global y
    print(y)  # => 6
    y = num   # La variable globale y vaut maintenant 25
    print(y)  # => 25

definir_variable_globale(25)
print(y)  # => 25 : la variable globale a bien été modifiée

"""
De même, le mot-clé "nonlocal" permet de modifier une variable de la fonction
englobante (le "E" de LEGB) depuis une fonction imbriquée (c'est la base des
"closures", cf. chap. 32) :
"""

def compter_jusqua_trois():
    total = 0

    def ajouter_un():
        nonlocal total  # on veut le total de compter_jusqua_trois()
        total = total + 1

    ajouter_un()
    ajouter_un()
    ajouter_un()
    return total

print(compter_jusqua_trois())  # => 3

"""
Attention : "global" et "nonlocal" sont rarement une bonne idée. Il est presque
toujours plus clair de passer la valeur en paramètre et de RETOURNER le
résultat :
"""

def incrementer_proprement(valeur):
    return valeur + 1

compteur_global = incrementer_proprement(compteur_global)
print(compteur_global)  # => 1

"""
Note : "global" n'est nécessaire que pour RÉAFFECTER une variable globale (avec
"="). Si la variable globale est une liste ou un dictionnaire, on peut modifier
son CONTENU sans "global", car on ne change pas la variable elle-même :
"""
HISTORIQUE = []

def enregistrer(evenement):
    HISTORIQUE.append(evenement)  # pas de "=", donc pas besoin de "global"

enregistrer("connexion")
enregistrer("déconnexion")
print(HISTORIQUE)  # => ['connexion', 'déconnexion']


# Les namespaces
#################

"""
Un namespace ("espace de noms") est une table qui associe des NOMS à des
VALEURS : c'est en fait… un dictionnaire (cf. chap. 18) ! Chaque portée vue
plus haut correspond à un namespace :

    - le namespace "built-in", créé au démarrage de Python
    - le namespace global d'un fichier (on dit aussi "d'un module", cf. chap. 22)
    - un namespace local, créé à CHAQUE appel de fonction, et détruit à la fin
      de l'appel

Écrire "x = 5", c'est donc ajouter (ou modifier) la clé "x" dans le namespace
courant, avec la valeur 5.

Deux fonctions intégrées permettent de les observer :
    - globals() retourne le dictionnaire des noms globaux
    - locals() retourne le dictionnaire des noms locaux (là où on l'appelle)
"""
print("GLOB" in globals())  # => True
print(globals()["GLOB"])    # => 3 (comme si on écrivait GLOB)
print("a" in globals())     # => False (a était un paramètre de une_fonction)

def montrer_locales(p):
    v = p * 2
    print(locals())

montrer_locales(10)  # => {'p': 10, 'v': 20}

"""
La fonction intégrée dir(), appelée sans paramètre, donne la liste des noms
définis dans la portée courante.
"""
def petite_fonction():
    une_locale = 1
    une_autre = 2
    print(dir())

petite_fonction()  # => ['une_autre', 'une_locale'] (dans l'ordre alphabétique)

"""
Les noms intégrés vivent dans le namespace du module "builtins". On peut
l'importer pour les lister (on verra "import" au chap. 22) :
"""
import builtins
print("print" in dir(builtins))  # => True
print("len" in dir(builtins))    # => True

"""
IMPT : comme les noms globaux passent AVANT les noms intégrés (G avant B), on
peut "écraser" accidentellement une fonction intégrée en créant une variable
du même nom. C'est un bug très courant chez les débutants : ne nommez jamais
vos variables list, dict, str, sum, max, min, input, type, id…
"""
sum = 10  # à ne pas faire : la fonction intégrée sum() est maintenant masquée
try:
    sum([1, 2, 3])  # => TypeError: 'int' object is not callable
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")

# On répare en supprimant notre variable : Python retrouve alors le sum()
# intégré (B de LEGB)
del sum
print(sum([1, 2, 3]))  # => 6

"""
Enfin, chaque namespace est indépendant : deux fonctions peuvent avoir une
variable locale du même nom sans aucun conflit. C'est tout l'intérêt des
namespaces : on peut nommer ses variables sans se soucier des noms utilisés
ailleurs dans le programme.
"""
def fonction_1():
    resultat = "un"
    return resultat

def fonction_2():
    resultat = "deux"  # aucun rapport avec le resultat de fonction_1()
    return resultat

print(fonction_1(), fonction_2())  # => un deux


# Bonnes pratiques
###################

"""
En résumé :
    1. Préférez les variables locales : une fonction devrait recevoir ce dont
       elle a besoin via ses PARAMÈTRES, et transmettre son résultat via
       "return".
    2. Réservez les variables globales aux constantes, écrites EN_MAJUSCULES.
    3. Évitez "global" et "nonlocal", sauf cas très particulier.
    4. Ne réutilisez pas une variable de boucle après la boucle.
    5. Ne donnez jamais à une variable le nom d'une fonction intégrée.

En cas de doute sur la valeur d'une variable, appliquez la règle LEGB : cherchez
d'abord dans la fonction, puis dans la fonction englobante, puis dans le
fichier, puis parmi les noms intégrés.
"""
