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
#  Chap. 12     #  Structures de contrôle I : if, then, else et elif           #
#               #                                                              #
################################################################################
#
#  - La structure "if"
#  - Le mot-clé "else"
#  - Le mot-clé "elif"
#  - Remarques sur l'indentation
#  - "if" imbriqués
#  - Le mot-clé "pass"
#  - Pièges fréquents
#  - Les "one-liner" avec if
#
###################################

"""
Normalement, un programme Python est exécuté de haut en bas, ligne à ligne.

C'est le comportement par défaut, mais on peut le modifier avec des structures
de contrôle :
    1. soit pour exécuter un bloc de code seulement sous certaines conditions
       (avec le mot-clé "if", comme on le verra dans ce chapitre)

    2. soit pour exécuter un bloc de code plusieurs fois via une "boucle" (avec
       "while" et "for", cf. chap. suivant)

Ce site explique très bien le fonctionnement du bloc if (en anglais) :
https://www.learnbyexample.org/python-if-else-elif-statement/
"""

# La structure "if"
####################

"""
Voici une condition "si … alors …". On l'exprime avec le mot-clé "if" :
if <condition>:
    code… (Notez l'indentation en début de ligne !)

<condition> doit être :
    - un booléen…
    - …ou une expression qui retourne un booléen (comme une comparaison ou un
      test d'égalité)

Tout le code indenté sera exécuté si la condition est remplie. Sinon, il sera
ignoré.
"""

une_variable = 5

if une_variable > 10:
    print("une_variable est plus grande que 10")
print("Ceci n'est pas dans le bloc if et sera toujours affiché !")
"""
">" est un opérateur de comparaison, donc l'expression "une_variable > 10"
retournera un booléen.

Le 1er print() ne sera pas exécuté car la condition n'est pas remplie.
Ce code affichera donc juste le 2e print ("Ceci n'est pas dans le bloc if…")

Décortiquons la syntaxe, élément par élément :
    - le mot-clé "if" (en minuscules : "If" ou "IF" ne fonctionnent pas),
    - la condition, ici "une_variable > 10" (pas besoin de parenthèses
      autour, contrairement à d'autres langages comme C ou JavaScript),
    - le caractère ":" en fin de ligne, OBLIGATOIRE : il annonce qu'un bloc
      de code va suivre,
    - le bloc lui-même, c'est-à-dire toutes les lignes indentées (décalées
      vers la droite, en général de 4 espaces) qui suivent.

Le bloc s'arrête à la première ligne qui revient au niveau d'indentation du
"if" : c'est le cas du 2e print() ci-dessus.
"""

# Si la condition est remplie, TOUTES les lignes du bloc sont exécutées, dans
# l'ordre :
une_variable = 15

if une_variable > 10:
    print("une_variable est plus grande que 10")  # => imprimé
    print("…et cette ligne aussi est dans le bloc")  # => imprimé
    une_variable = une_variable - 10  # un bloc peut contenir n'importe quel code
print(une_variable)  # => 5 (toujours exécuté, hors du bloc)

# La condition peut utiliser tous les opérateurs de comparaison du chap. 9 :
# ==, !=, <, <=, >, >=, ainsi que "in" et "not in" (cf. chap. 8)
mot = "python"
if mot == "python":
    print("C'est bien le mot python")  # => imprimé
if "y" in mot:
    print("Le mot contient un y")  # => imprimé
if mot != "java":
    print("Ce n'est pas java")  # => imprimé

"""
IMPT : on teste l'égalité avec "==" (deux signes "égal"), jamais avec "=" qui
sert à l'affectation (cf. chap. 10). Écrire "if mot = 'python':" est une
erreur de syntaxe (SyntaxError) : le programme refusera même de démarrer.
C'est pour cette raison que cet exemple n'est pas dans un try … except …
(cf. chap. 26) : il est simplement laissé en commentaire.
"""
# if mot = "python":   # SyntaxError: invalid syntax
#     print("…")

"""
Note : on peut combiner plusieurs conditions dans un "if" avec les opérateurs
booléens

cf. le cours du chap. 9 sur les expressions booléennes :
"""
if une_variable > 3 and une_variable % 2 == 0:
    print("Voilà une condition bien compliquée")
# Le print() ci-dessus sera-t-il affiché si une_variable = 5 ? Pourquoi ?

"""
Réponse : non. "une_variable > 3" est vrai (5 > 3), mais "une_variable % 2 == 0"
est faux (5 est impair : le reste de sa division par 2 vaut 1). Or "and"
exige que les deux conditions soient vraies (cf. chap. 9).

On peut aussi écrire des encadrements, comme en mathématiques :
"""
note = 14
if 10 <= note < 16:
    print("Note correcte, entre 10 (inclus) et 16 (exclu)")  # => imprimé

"""
Attention : si l'expression n'est pas booléenne, le programme se débrouillera
pour transformer ("caster") le résultat en booléen… (cf. chap. 21) avec des
risques de bug.

Par exemple, un nombre non nul est considéré comme vrai, et 0 comme faux. Une
chaîne non vide est considérée comme vraie, et la chaîne vide "" comme fausse.
"""
if 42:
    print("42 est considéré comme vrai !")  # => imprimé
if "":
    print("Ceci ne sera jamais imprimé : la chaîne vide est considérée fausse")
if "False":
    print('Piège : la CHAÎNE "False" n\'est pas vide, donc elle est vraie !')
    # => imprimé

"""
Donc, toujours utiliser des booléens avec "if" !
"""


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

"""
Ceci affichera :
    - une_variable est plus grande que 10
    - ceci n'est pas dans le bloc else et sera toujours affiché !

Notez bien que :
    - l'exécution passera par exactement une des deux clauses (jamais les deux,
      jamais aucune),
    - "else:" se termine aussi par ":",
    - l'indentation de "else:" commence au même niveau que le if !
    - "else" ne prend jamais de condition : il couvre "tous les autres cas".
"""

# Avec une autre valeur, c'est le bloc "else" qui est exécuté :
une_variable = 3

if une_variable > 10:
    print("une_variable est plus grande que 10")
else:
    print("une_variable est plus petite ou égale à 10")  # => imprimé

# Exemple classique : tester la parité d'un nombre avec le modulo (cf. chap. 4)
nombre = 7
if nombre % 2 == 0:
    print(nombre, "est pair")
else:
    print(nombre, "est impair")  # => 7 est impair

"""
Un "else" doit toujours suivre directement un bloc "if" : un "else" isolé, ou
séparé de son "if" par une ligne non indentée, est une erreur de syntaxe.

if nombre > 0:
    print("positif")
print("une ligne au milieu")
else:                         # SyntaxError: invalid syntax
    print("négatif ou nul")
"""


# Le mot-clé "elif"
####################

"""
Enfin, on peut compléter cette structure avec "elif". "elif" permet d'ajouter
une autre condition à tester, alors qu'avec "else" le bloc qui est exécuté
quand aucune condition n'est remplie : c'est le cas "par défaut".

Exemple avec cette fonction mathématique f définie par morceaux :
         / 2x + 3   si x < 0
f : x → -  3  − x   si 0 ≤ x < 2
         \\ x² − 3   si x ≥ 2
"""

"""
On peut reproduire cette fonction avec "if …: … elif …: … else: …".

Note : on utilise ici "def" et "return" pour définir une fonction Python.
Ce sera expliqué en détail au chap. 14 : pour l'instant, retenez simplement
que f(x) "renvoie" le résultat du calcul situé après le "return" qui est
exécuté.
"""
def f(x):
    if x < 0:  # si x est négatif
        return 2 * x + 3
    elif x < 2:  # sinon, SI x < 2 (donc si 0 <= x < 2)
        return 3 - x
    else:  # dans tous les autres cas (donc si x >= 2)
        return x ** 2 - 3
# "else:" ne prend pas de condition !

print(f(-3))  # => -3   (premier cas : 2 * (-3) + 3)
print(f(1))   # => 2    (deuxième cas : 3 - 1)
print(f(7))   # => 46   (troisième cas : 7 ** 2 - 3)
print(f(2))   # => 1    (x = 2 n'est pas < 2 : on tombe dans le "else")

"""
Notes :
    - "elif" est la contraction de "else if" ("sinon, si…"),
    - "elif" sert quand on a plus de deux cas possibles,
    - il n'y a pas de limites au nombre de "elif" dans une structure if,
    - on peut utiliser "elif:" sans "else:" : dans ce cas-là il sera possible
      qu'aucune clause ne soit exécutée.

IMPT : les conditions sont testées DANS L'ORDRE, de haut en bas, et seul le
PREMIER bloc dont la condition est vraie est exécuté. Les suivants sont
ignorés, même si leur condition est vraie aussi !
"""

# Exemple : attribuer une mention à une note sur 20
note = 17

if note >= 16:
    print("Très bien")  # => Très bien
elif note >= 14:
    print("Bien")  # 17 >= 14 est vrai aussi, mais ce bloc n'est pas exécuté !
elif note >= 12:
    print("Assez bien")
elif note >= 10:
    print("Passable")
else:
    print("Recalé")

# Si l'on se trompe dans l'ordre des conditions, le résultat devient faux :
if note >= 10:
    print("Passable")  # => Passable… alors que la note vaut 17 !
elif note >= 16:
    print("Très bien")  # jamais atteint : toute note >= 16 est aussi >= 10

"""
Morale : quand les conditions se recoupent, on les écrit de la plus
restrictive à la moins restrictive.

Remarquez aussi la différence entre une série de "elif" et une série de "if"
indépendants : avec des "if" séparés, CHAQUE condition est testée, et
plusieurs blocs peuvent être exécutés.
"""
if note >= 16:
    print("Très bien")  # => Très bien
if note >= 14:
    print("Bien")  # => Bien (ce "if" est indépendant du précédent)
if note >= 12:
    print("Assez bien")  # => Assez bien

# Ex :
x = 5

if x > 20_000:
    print("x est grand")
elif x < 0.001:
    print("x est tout petit")
"""
Ici rien ne s'affichera car x n'est ni grand ni petit ! pour couvrir le cas
"par défaut" , il faudra ajouter une clause "else".
"""


# Remarques sur l'indentation
##############################

"""
En Python, l'indentation sert à identifier quand on "entre dans" un bloc.
Remarquez que l'indentation augmente après chaque ":".

L'indentation en Python est donc visuelle ET sémantique : utiliser la mauvaise
identation peut créer une erreur pendant l'exécution, voire pire, changer
subtilement le sens du programme !

Rappels (cf. chap. 5) :
    - la convention (PEP 8) est d'indenter avec 4 espaces,
    - on ne mélange jamais espaces et tabulations dans un même fichier,
    - toutes les lignes d'un même bloc doivent avoir EXACTEMENT la même
      indentation.
"""

# Exemple de code contenant un bug :
def lancer_missile():
    # (la définition de fonction crée aussi une nouvelle indentation)
    print("Boom !")

code_saisi = input("Rentrez le code secret pour lancer le missile : ")

if code_saisi == "123456":
    print("Code de lancement correct")
lancer_missile()  # => Êtes-vous sûr de l'indentation de cette ligne ?

"""
Explication : l'appel lancer_missile() n'est PAS indenté. Il ne fait donc pas
partie du bloc "if" : il est exécuté dans tous les cas, que le code saisi soit
correct ou non. Essayez de lancer ce fichier en saisissant un mauvais code :
"Boom !" s'affiche quand même !

Le programme ne contient pourtant aucune erreur de syntaxe : Python ne peut pas
deviner ce que l'on voulait faire. C'est le pire type de bug, celui qui ne
provoque aucun message d'erreur.

Version corrigée (on réutilise le code déjà saisi plus haut) :
"""
if code_saisi == "123456":
    print("Code de lancement correct")
    lancer_missile()  # indenté : exécuté seulement si le code est correct
else:
    print("Code incorrect : lancement annulé")

"""
À l'inverse, une indentation incohérente provoque une erreur dès le
lancement du programme (IndentationError, une sorte de SyntaxError) :

if code_saisi == "123456":
    print("Code de lancement correct")
      lancer_missile()   # IndentationError: unexpected indent

if code_saisi == "123456":
print("Code de lancement correct")   # IndentationError: expected an indented
                                     # block after 'if' statement
"""


# "if" imbriqués
#################

"""
Il est tout à fait possible d'imbriquer des if, c'est-à-dire d'avoir des "if
dans des if". Mais on peut parfois les éviter en se débrouillant autrement…
"""

# Ex :
x, y, z = 7, 4, 2

if x > y:
    print(x, " est plus grand que ", y)
    if x > z:
        print(x, " est aussi plus grand que ", z)
# Notez que des if imbriqués nécessitent de bien surveiller l'indentation…
"""
Ce code affichera :
7  est plus grand que  4
7  est aussi plus grand que  2

Le "if" intérieur n'est testé QUE si la condition du "if" extérieur est vraie.
Chaque niveau d'imbrication ajoute 4 espaces d'indentation.

(Les doubles espaces viennent de print(), qui ajoute un espace entre chacun de
ses arguments, cf. chap. 7.)
"""

"""
Ça fonctionne très bien, mais on aurait pu se débrouiller avec un seul if, de
la façon suivante :
"""
if x > y and x > z:
    print(x, " est plus grand que ", y, " et ", z)
elif x > y:
    print(x, " est plus grand que ", y)
# => 7  est plus grand que  4  et  2

"""
Les deux versions ne sont pas strictement équivalentes (l'affichage diffère),
mais la seconde est "plus plate" : moins d'indentation, donc plus facile à
lire. Le Zen de Python le dit : "Flat is better than nested" ("mieux vaut plat
qu'imbriqué"). Tapez "import this" dans une console Python pour le lire en
entier !

Les "if" imbriqués restent utiles quand chaque niveau a ses propres "else" :
"""
age = 20
a_le_permis = False

if age >= 18:
    if a_le_permis:
        print("Vous pouvez louer une voiture")
    else:
        print("Vous êtes majeur, mais il vous faut le permis")  # => imprimé
else:
    print("Vous êtes trop jeune pour conduire")

"""
Exercice : réécrivez cet exemple sans "if" imbriqué, avec "if … elif … else"
et l'opérateur "and". Combien de conditions faut-il écrire ?
"""


# Le mot-clé "pass"
####################

"""
Un bloc ne peut pas être vide : Python exige au moins une instruction après
chaque ":". Quand on ne veut rien faire (par exemple parce qu'on n'a pas
encore écrit le code), on utilise le mot-clé "pass", qui signifie
littéralement "ne rien faire".
"""
temperature = 25

if temperature > 30:
    pass  # plus tard : déclencher la climatisation
else:
    print("Pas besoin de climatisation")  # => imprimé

"""
Sans "pass", ce code soulèverait une IndentationError: expected an indented
block. "pass" sert aussi pour les fonctions (cf. chap. 14) ou les boucles
(cf. chap. 13) que l'on n'a pas encore écrites.
"""


# Pièges fréquents
###################

"""
Récapitulatif des erreurs les plus courantes avec "if" :

    1. Oublier les ":" en fin de ligne :
       if x > 3          # SyntaxError: expected ':' (message de Python 3.10+,
                         # les versions antérieures disent "invalid syntax")

    2. Utiliser "=" au lieu de "==" :
       if x = 3:         # SyntaxError: invalid syntax

    3. Se tromper d'indentation (voir l'exemple du missile plus haut).

    4. Écrire une condition "or" incomplète. C'est un piège classique :
"""
couleur = "vert"

# On veut tester si la couleur est "rouge" ou "bleu"…
if couleur == "rouge" or "bleu":
    print("Bug : ceci est imprimé alors que la couleur est verte !")
    # => imprimé

"""
Explication : Python lit "(couleur == 'rouge') or ('bleu')". La première
partie est fausse, mais la seconde, la chaîne "bleu", n'est pas vide : elle
est donc considérée comme vraie (voir plus haut). La condition entière est
vraie, quelle que soit la couleur !

Il faut répéter la comparaison :
"""
if couleur == "rouge" or couleur == "bleu":
    print("Ceci n'est pas imprimé")
else:
    print("La couleur n'est ni rouge ni bleue")  # => imprimé

"""
    5. Comparer des valeurs de types différents. input() retourne toujours une
       string (cf. chap. 11) : "18" == 18 est faux !
"""
saisie = "18"  # comme si cette valeur venait de input()
if saisie == 18:
    print("Jamais imprimé : on compare une string et un int")
if int(saisie) == 18:
    print("Après conversion avec int(), la comparaison fonctionne")  # => imprimé


# Les "one-liner" avec if
##########################

"""
Quand un bloc "if" ne contient qu'une seule instruction, on peut l'écrire sur
la même ligne que la condition. C'est autorisé, mais déconseillé par la PEP 8
car moins lisible : à réserver aux cas très simples.
"""
x = 5
if x > 0: print("x est positif")  # => x est positif

"""
Plus utile : l'expression conditionnelle (on parle parfois d'"opérateur
ternaire"), qui permet de choisir entre deux VALEURS selon une condition :

    <valeur_si_vrai> if <condition> else <valeur_si_faux>

Contrairement à la structure "if" classique, c'est une expression : elle
retourne une valeur, que l'on peut affecter à une variable ou passer à une
fonction. Le "else" y est obligatoire.
"""
age = 15
statut = "majeur" if age >= 18 else "mineur"
print(statut)  # => mineur

# C'est exactement équivalent à ces quatre lignes :
if age >= 18:
    statut = "majeur"
else:
    statut = "mineur"
print(statut)  # => mineur

# Autres exemples :
x = -8
valeur_absolue = x if x >= 0 else -x
print(valeur_absolue)  # => 8

nb_pommes = 1
print(f"J'ai {nb_pommes} pomme{'s' if nb_pommes > 1 else ''}")  # => J'ai 1 pomme
nb_pommes = 3
print(f"J'ai {nb_pommes} pomme{'s' if nb_pommes > 1 else ''}")  # => J'ai 3 pommes

"""
On peut enchaîner les expressions conditionnelles, mais cela devient vite
illisible :
"""
note = 12
mention = "bien" if note >= 14 else "passable" if note >= 10 else "recalé"
print(mention)  # => passable
"""
Dans ce cas, préférez un vrai bloc "if … elif … else" !
"""
