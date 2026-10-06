################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Félix Déage - 2026                    #
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
#  - Paramètres par défaut et arguments nommés
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

Les règles sont les mêmes que pour les noms de variables : lettres, chiffres
et "_", sans commencer par un chiffre, et sans utiliser un mot-clé réservé
(def, if, for, return…).
"""
# Snake Case : c'est la convention recommandée par la PEP 8 pour les fonctions
def jolie_fonction():
    print("Minuscules et underscores, tout va bien.")


# Camel Case (ici avec une majuscule initiale, on parle aussi de "Pascal Case")
def JolieFonction2():
    print("On peut ajouter des chiffres à la fin")
# Ça fonctionne, mais en Python ce style est réservé aux noms de classes
# (cf. chap. 34) : on l'évite pour les fonctions.


def FonctION_TRÈS_Moche():
    print("Moche ! Il faut éviter les accents, ainsi que mélanger les styles")
# Python 3 accepte les accents dans les noms, mais c'est déconseillé : tout le
# monde n'a pas un clavier français, et la plupart des projets sont en anglais.

# Les trois fonctions s'appellent de la même façon :
jolie_fonction()       # => Minuscules et underscores, tout va bien.
JolieFonction2()       # => On peut ajouter des chiffres à la fin
FonctION_TRÈS_Moche()  # => Moche ! Il faut éviter les accents, ainsi que…

"""
Conseil : une fonction FAIT quelque chose, on la nomme donc souvent avec un
verbe : calculer_moyenne(), afficher_score(), convertir_en_euros()…
Une fonction qui retourne un booléen commence souvent par "est_" ou "a_" (en
anglais "is_" ou "has_") : est_pair(n), a_le_permis(personne)…
"""


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

Pour s'en souvenir : le paramètre est la "case vide" prévue dans la définition,
l'argument est la valeur concrète que l'on met dans la case au moment de
l'appel. Une même fonction a toujours les mêmes paramètres, mais chaque appel
peut lui passer des arguments différents.
"""


# Paramètres par défaut et arguments nommés
############################################

"""
On peut donner une valeur par défaut à un paramètre, avec "=" dans la
définition. Si l'argument correspondant n'est pas passé lors de l'appel, c'est
la valeur par défaut qui est utilisée : le paramètre devient optionnel.
"""


def saluer(nom, salutation="Bonjour"):
    print(f"{salutation} {nom} !")


saluer("Ada")           # => Bonjour Ada !     (valeur par défaut)
saluer("Ada", "Salut")  # => Salut Ada !       (on remplace la valeur par défaut)

"""
Vous connaissez déjà une fonction avec des paramètres par défaut : print() !
Son paramètre "end" vaut "\n" (saut de ligne) par défaut, et "sep" vaut " "
(cf. chap. 7). Et range() aussi : son pas vaut 1 par défaut (cf. chap. 13).

IMPT : les paramètres avec valeur par défaut doivent être placés APRÈS les
paramètres sans valeur par défaut. Ceci est une erreur de syntaxe :

def saluer(salutation="Bonjour", nom):  # SyntaxError: non-default argument
    …                                   # follows default argument
"""

"""
Lors de l'appel, on peut aussi préciser le nom du paramètre auquel on passe
chaque argument : on parle d'"arguments nommés" (en anglais "keyword
arguments"). L'ordre n'a alors plus d'importance.
"""


def decrire_animal(espece, nom, age):
    print(f"{nom} est un {espece} de {age} ans")


decrire_animal("chat", "Félix", 3)                # => Félix est un chat de 3 ans
decrire_animal(nom="Félix", age=3, espece="chat")  # => Félix est un chat de 3 ans
decrire_animal("chat", age=3, nom="Félix")         # => Félix est un chat de 3 ans

"""
Les arguments nommés rendent l'appel plus lisible, surtout quand une fonction
a beaucoup de paramètres. Vous les avez déjà utilisés avec print(…, end=" ").

Règle : les arguments "positionnels" (non nommés) doivent être placés AVANT
les arguments nommés.

decrire_animal(nom="Félix", "chat", 3)  # SyntaxError: positional argument
                                        # follows keyword argument

Un argument nommé doit aussi correspondre à un paramètre qui existe :
"""
try:
    decrire_animal("chat", "Félix", 3, couleur="roux")
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => TypeError: decrire_animal() got an unexpected keyword argument 'couleur'

# Paramètres par défaut et arguments nommés se combinent très bien :
def calculer_prix(prix_ht, taux_tva=0.2, remise=0):
    return prix_ht * (1 + taux_tva) - remise


print(calculer_prix(100))                  # => 120.0
print(calculer_prix(100, remise=10))       # => 110.0 (taux par défaut conservé)
print(calculer_prix(100, taux_tva=0.055))  # => 105.5

"""
Attention : n'utilisez jamais une liste (ou un autre type modifiable, cf.
chap. 16) comme valeur par défaut : la même liste serait partagée entre tous
les appels, ce qui crée des bugs surprenants. On utilisera None à la place
(voir la section suivante).
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
"… is None" au lieu de "… == None". Les deux fonctionnent ici, mais "is"
est la forme recommandée par la PEP 8 (car None est une valeur unique : on
teste si c'est "le même objet", et pas seulement "une valeur égale").
"""
fonction_sans_retour() is None  # => True
fonction_sans_retour() is not None  # => False

# None a son propre type :
type(None)  # => <class 'NoneType'>

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

"""
Conséquence : une fonction qui fait print() au lieu de return est moins
réutilisable. On ne peut rien faire de son résultat (le stocker, le comparer,
faire un calcul avec), puisqu'elle n'en retourne pas !
"""
try:
    un_calcul(2, 3, 5) + 1  # => 11 est imprimé… puis on calcule None + 1
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

"""
Règle générale : une fonction de CALCUL retourne son résultat avec "return",
et c'est le code appelant qui décide de l'afficher ou non. On réserve print()
aux fonctions dont le but est justement d'afficher quelque chose.
"""

# Autre exemple
def retours_multiples(param):
    if param % 2 == 0:
        return "pair"
    print("Ceci ne sera pas imprimé si param est pair, car return quitte la fonction")
    return "impair"


# Le premier appel n'imprimera RIEN : "pair" est retourné, mais pas imprimé
retours_multiples(2)

"""
Le deuxième appel imprimera :
"Ceci ne sera pas imprimé si param est pair, car return quitte la fonction".

Remarquez que "impair" ne sera pas imprimé : il est seulement retourné, et
comme on n'en fait rien, il est "perdu" !
"""
retours_multiples(3)

# Pour voir les valeurs retournées, il faut les imprimer :
print(retours_multiples(2))  # => pair
print(retours_multiples(3))
# => Ceci ne sera pas imprimé si param est pair, car return quitte la fonction
# => impair

"""
Remarque : dans une console Python (mode interactif, cf. chap. 2), la valeur
retournée par un appel est affichée automatiquement. C'est trompeur : dans
un fichier exécuté avec "python fichier.py", seul print() affiche quelque
chose !
"""


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

Explication, étape par étape :
    1. print(c()) appelle c(). c() imprime "tata".
    2. c() appelle b() une première fois : b() imprime "titi", puis appelle
       a(), qui imprime "toto" et retourne "tutu". Ce "tutu" est passé à
       print() dans b(), qui l'imprime. b() retourne alors "tyty"… que c()
       ignore, car l'appel "b()" n'est ni imprimé ni stocké !
       (le print("tutu") après le return de b() n'est jamais exécuté)
    3. c() appelle print(b()) : b() refait exactement la même chose (titi,
       toto, tutu), puis retourne "tyty", qui est cette fois imprimé.
    4. c() retourne "tete", qui est imprimé par le print() du départ.

Une fonction peut donc en appeler une autre, qui en appelle une autre… Chaque
appel "attend" que la fonction appelée ait terminé pour continuer.
Ce mécanisme permet de construire des fonctions complexes à partir de
fonctions simples :
"""


def carre(x):
    return x * x


def somme_des_carres(a, b):
    return carre(a) + carre(b)  # on réutilise carre() deux fois


print(somme_des_carres(3, 4))  # => 25


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

print(retours)  # => (4, 10, 0.6666666666666666)
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

"""
Cette syntaxe "a, b = …" est l'affectation multiple vue au chap. 10 : la
première valeur du tuple va dans a, la seconde dans b. Il faut autant de
variables que de valeurs retournées :
"""
try:
    a, b, c = retour_multiple_2(-2)  # 3 variables pour 2 valeurs…
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# => ValueError: not enough values to unpack (expected 3, got 2)

# Exemple concret : retourner le quotient et le reste d'une division entière
def division_euclidienne(dividende, diviseur):
    return dividende // diviseur, dividende % diviseur  # cf. chap. 4


quotient, reste = division_euclidienne(17, 5)
print(quotient, reste)  # => 3 2 (car 17 = 5 * 3 + 2)


# L'adresse d'une fonction
################################

# Ceci n'est pas à comprendre absolument !

def test_adresse():
    print("yolo")

# On pourra être décontenancé si l'on oublie les parenthèses lors d'un appel…
print(test_adresse)  # => <function test_adresse at 0x1097679d0>
# (l'adresse change à chaque exécution et selon l'ordinateur)

"""
Explication : sans les parenthèses, on n'imprimera pas la valeur retourné par la
fonction au moment de l'appel, mais… l'adresse en mémoire où est stockée la
fonction ! (par convention, cette adresse est écrite en hexadécimal)
"""

# On verra (cf. chap. 32) que cette adresse peut être affectée à une variable,
# comme n'importe quelle valeur !
a = test_adresse
print(a)     # => <function test_adresse at 0x1097679d0>

# a est une variable contenant une fonction…
type(a)  # => <class 'function'>
# …et cette fonction peut être exécutée !
a()      # => yolo

"""
En Python, les fonctions sont donc des valeurs comme les autres : on peut les
stocker dans une variable, et même les passer en argument à une autre fonction.
"""


def appliquer_deux_fois(fonction, valeur):
    return fonction(fonction(valeur))


print(appliquer_deux_fois(carre, 3))  # => 81 (carre(carre(3)) = carre(9))

"""
IMPT : retenez surtout l'erreur fréquente qui consiste à oublier les
parenthèses : "test_adresse" désigne la fonction elle-même, "test_adresse()"
l'APPELLE. Sans parenthèses, le code de la fonction n'est pas exécuté !
"""
test_adresse  # n'affiche rien et n'exécute rien : la fonction n'est pas appelée
