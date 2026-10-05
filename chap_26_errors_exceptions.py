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
#  Chap. 26     #  Erreurs et exceptions                                       #
#               #                                                              #
################################################################################
#
#  - Le mécanisme des erreurs en Python
#  - Lire un message d'erreur
#  - Erreurs de syntaxe et erreurs d'exécution
#  - Causes fréquentes d'erreurs
#  - La hiérarchie des exceptions
#  - Gérer les erreurs avec try: … except: …
#  - Les clauses else et finally
#  - Soulever ses propres erreurs avec raise
#  - Live and let die : quand laisser crasher ?
#
##################################################

"""
Note : ce chapitre crée EXPRÈS de nombreuses erreurs. Comme dans le reste du
cours, elles sont toutes interceptées avec "try: … except: …" pour que le
fichier reste exécutable… et c'est justement ce mécanisme que l'on va enfin
expliquer en détail !

Vocabulaire : en Python, on parle indifféremment d'"erreur" ou
d'"exception". Une exception est un objet qui décrit le problème rencontré
(son type, par ex. ZeroDivisionError, et un message).

Note : ce chapitre contient un input() : il faudra répondre à une question
dans la console.
"""

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
try:
    for i in range(6):
        print(1 / (5 - i))
except ZeroDivisionError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
0.2
0.25
0.3333333333333333
0.5
1.0
1: (Sans ce try: … except …, cette ligne créerait : division by zero)

Ce code crée une erreur ZeroDivisionError quand i vaut 5. Notez que les 5
premiers tours de boucle se sont exécutés normalement : l'erreur survient
seulement au moment où la division par 0 est tentée, et tout ce qui suit
(dans le bloc try) n'est PAS exécuté.
"""

"""
    2. il est aussi possible de créer ("soulever", "lever") soi-même une
       erreur avec le mot-clé "raise" :
"""
try:
    raise ZeroDivisionError     # => soulève la même erreur manuellement
except ZeroDivisionError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err!r})")

# Les deux codes plus haut ont exactement la même conséquence : créer une
# erreur qui va interrompre le fil normal du programme.

# On peut même rajouter un message d'erreur pour l'utilisateur
try:
    raise IndexError("Ne dépasse pas l'indice de la liste plz 😡")
except IndexError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
IMPT : il y a deux issues possibles à la survenue d'une erreur :
    1. soit l'erreur est interceptée (avec try: … except: …)
    2. soit l'erreur n'est pas interceptée et crashe le programme.

Attention : il n'y a pas de "meilleure" solution pour gérer l'erreur ! en
fonction de la situation, il peut être souhaitable de laisser crasher
(philosophie du "let it crash", voir la dernière section).

Que se passe-t-il quand une erreur survient DANS une fonction ? L'erreur
"remonte" ("se propage") : elle interrompt la fonction, puis la fonction qui
l'a appelée, puis celle qui a appelé celle-ci… jusqu'à trouver un
"try: … except: …" qui l'intercepte. Si aucun n'est trouvé, le programme
crashe.
"""

def niveau_3():
    print("niveau_3 : début")
    1 / 0                         # l'erreur survient ici…
    print("niveau_3 : fin")       # … donc cette ligne n'est jamais exécutée


def niveau_2():
    print("niveau_2 : début")
    niveau_3()                    # … elle interrompt niveau_2…
    print("niveau_2 : fin")       # … qui ne termine pas non plus


def niveau_1():
    try:
        niveau_2()
    except ZeroDivisionError as err:
        # … et elle est enfin interceptée ici, deux niveaux plus haut.
        print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("niveau_1 : le programme continue normalement")


niveau_1()
"""
niveau_2 : début
niveau_3 : début
4: (Sans ce try: … except …, cette ligne créerait : division by zero)
niveau_1 : le programme continue normalement
"""


# Lire un message d'erreur
###########################

"""
IMPT : il faut BIEN LIRE LES MESSAGES D'ERREURS : ils vous sauveront souvent…

Si l'on appelait niveau_2() SANS try, le programme crasherait avec un message
de ce genre (appelé "traceback", la "trace" des appels de fonctions) :

Traceback (most recent call last):
  File "chap_26_errors_exceptions.py", line …, in <module>
    niveau_2()
  File "chap_26_errors_exceptions.py", line …, in niveau_2
    niveau_3()
  File "chap_26_errors_exceptions.py", line …, in niveau_3
    1 / 0
ZeroDivisionError: division by zero

Comment le lire ?
    1. COMMENCEZ PAR LA DERNIÈRE LIGNE : elle donne le TYPE de l'erreur
       (ZeroDivisionError) et un MESSAGE qui l'explique (division by zero).
    2. Remontez ensuite d'une ligne : c'est l'endroit EXACT où l'erreur a eu
       lieu (fichier, numéro de ligne, fonction, et la ligne de code
       elle-même).
    3. Les lignes au-dessus montrent le chemin des appels qui a mené jusque-là
       ("most recent call last" : l'appel le plus récent est en bas). C'est
       utile quand l'erreur vient d'une fonction appelée avec de mauvais
       arguments : la cause est alors plus haut dans la trace.

Note : les versions récentes de Python (3.11+) ajoutent des "^^^^" sous la
partie exacte de la ligne qui pose problème, et parfois une suggestion
("Did you mean: …?"). Profitez-en !

Astuce : en cas de message incompréhensible, copiez la DERNIÈRE ligne dans
un moteur de recherche : quelqu'un a forcément déjà eu le même problème.
"""


# Erreurs de syntaxe et erreurs d'exécution
############################################

"""
Il y a grosso modo deux familles d'erreurs :

    1. Les erreurs de SYNTAXE (SyntaxError, et sa variante IndentationError) :
       le code n'est pas du Python valide. Python les détecte AVANT de
       commencer à exécuter le fichier, en le lisant en entier (on dit en
       le "compilant" ou "parsant"). Conséquence : si un fichier contient une
       seule erreur de syntaxe, AUCUNE ligne du fichier n'est exécutée, même
       celles qui sont avant l'erreur !

       IMPT : on ne peut donc pas intercepter une erreur de syntaxe avec
       un try: … except: … écrit dans le même fichier. La seule solution est
       de corriger le code.

    2. Les erreurs d'EXÉCUTION ("runtime errors" : ZeroDivisionError,
       TypeError, IndexError…) : le code est valide, mais une opération
       échoue au moment où elle est exécutée. Celles-ci peuvent être
       interceptées.

Exemples de code syntaxiquement invalide (à ne pas écrire tel quel dans un
fichier, sinon tout le fichier refuse de s'exécuter) :

iff True:           # => SyntaxError: invalid syntax ("iff" n'existe pas)
    print("…")

1 = x               # => SyntaxError: cannot assign to literal
[1)                 # => SyntaxError: closing parenthesis ')' does not
                    #    match opening parenthesis '['
if True             # => SyntaxError: expected ':'
    print("…")
  a = 1             # => IndentationError: unexpected indent

Pour pouvoir vous les montrer quand même dans ce fichier, on va ruser : la
fonction intégrée compile() demande à Python de lire du code contenu dans une
STRING. L'erreur de syntaxe survient alors pendant l'exécution de compile(),
et devient interceptable. (compile() n'est pas à connaître : c'est juste un
outil de démonstration ici.)
"""
codes_invalides = [
    "iff True:\n    print('Ceci n\\'est pas un if')",
    "1 = x",
    "[1)",
    "if True\n    print('oups')",
    "  a = 1",
]
for numero, code in enumerate(codes_invalides, start=5):
    try:
        compile(code, "<exemple>", "exec")
    except SyntaxError as err:
        # err.msg contient le message, sans le nom du fichier ni la ligne
        print(f"{numero}: (Sans ce try: … except …, ce code créerait : "
              f"{type(err).__name__}: {err.msg})")
"""
Ceci affichera (le texte exact des messages varie selon la version de Python) :

5: (Sans ce try: … except …, ce code créerait : SyntaxError: invalid syntax)
6: (Sans ce try: … except …, ce code créerait : SyntaxError: cannot assign to literal…)
7: (Sans ce try: … except …, ce code créerait : SyntaxError: closing parenthesis ')' does not match opening parenthesis '[')
8: (Sans ce try: … except …, ce code créerait : SyntaxError: expected ':')
9: (Sans ce try: … except …, ce code créerait : IndentationError: unexpected indent)

(Ici, type(err).__name__ donne le nom du type d'erreur, sous forme de string.)
"""


# Causes fréquentes d'erreurs
##############################

"""
Certaines sont très classiques (SyntaxError, dépasser les limites d'une liste,
appeler une méthode de liste sur une string, etc.). D'autres sont beaucoup plus
rares.

Pour chacune, on donne le type et le message que Python afficherait.
"""

#   1. Dépasser les limites d'une liste
depassement = [1, 2, 3]
try:
    depassement[42]  # => IndexError: list index out of range
except IndexError as err:
    print(f"10: (Sans ce try: … except …, cette ligne créerait : {err})")

#   2. Utiliser une méthode qui n'existe pas pour un objet
try:
    "abc".bizarre()  # => AttributeError: 'str' object has no attribute 'bizarre'
except AttributeError as err:
    print(f"11: (Sans ce try: … except …, cette ligne créerait : {err})")

#   3. Utiliser une variable du mauvais type (ici un int au lieu d'une string)
try:
    "Hello " + 42    # => TypeError: can only concatenate str (not "int") to str
except TypeError as err:
    print(f"12: (Sans ce try: … except …, cette ligne créerait : {err})")

# … ou appeler une fonction avec un mauvais nombre d'arguments
try:
    len("a", "b")    # => TypeError: len() takes exactly one argument (2 given)
except TypeError as err:
    print(f"13: (Sans ce try: … except …, cette ligne créerait : {err})")

#   4. Faire une conversion impossible entre deux types
try:
    int("abc")       # => ValueError: invalid literal for int() with base 10: 'abc'
except ValueError as err:
    print(f"14: (Sans ce try: … except …, cette ligne créerait : {err})")

#   5. Utiliser une variable non-définie (souvent une faute de frappe !)
try:
    print(variable_jamais_definie)  # => NameError: name '…' is not defined
except NameError as err:
    print(f"15: (Sans ce try: … except …, cette ligne créerait : {err})")

#   6. Utiliser un mot-clé non-défini : c'est une SyntaxError, qu'on ne peut
#      pas intercepter (voir la section précédente)
#
#      iff True:      # => SyntaxError: invalid syntax (iff)
#          print("Ceci n'est pas un if")

#   7. Utiliser une valeur qui n'est pas dans une liste
l2 = [1]
try:
    l2.remove(2)     # => ValueError: list.remove(x): x not in list
except ValueError as err:
    print(f"16: (Sans ce try: … except …, cette ligne créerait : {err})")

#   8. Référencer une valeur qui n'est pas dans un dictionnaire
d = {0: "zéro", 1: "un"}
try:
    d[2]             # => KeyError: 2
except KeyError as err:
    print(f"17: (Sans ce try: … except …, cette ligne créerait : {err})")

#   9. Se tromper d'indentation en début de ligne : là aussi, c'est une erreur
#      de syntaxe (IndentationError), impossible à intercepter
#
#        a = 1         # => IndentationError: unexpected indent

#   10. Importer un module qui n'existe pas (ou qui n'est pas installé,
#       cf. chap. 22)
try:
    import module_qui_n_existe_pas  # => ModuleNotFoundError: No module named …
except ImportError as err:
    print(f"18: (Sans ce try: … except …, cette ligne créerait : {err})")
# Note : ModuleNotFoundError est un cas particulier d'ImportError (voir la
# hiérarchie des exceptions plus bas), c'est pourquoi "except ImportError"
# l'intercepte.

#   11. Ouvrir un fichier qui n'existe pas (cf. chap. 28)
try:
    open("fichier_qui_n_existe_pas.txt")  # => FileNotFoundError: [Errno 2] …
except FileNotFoundError as err:
    print(f"19: (Sans ce try: … except …, cette ligne créerait : {err})")

#   12. Les erreurs de calcul ("ArithmeticError") : la division par 0, déjà
#       vue, mais aussi un résultat trop grand pour un float
try:
    10 % 0           # => ZeroDivisionError: integer modulo by zero
except ZeroDivisionError as err:
    print(f"20: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    2.0 ** 10_000    # => OverflowError: (34, 'Numerical result out of range')
except OverflowError as err:
    print(f"21: (Sans ce try: … except …, cette ligne créerait : {err})")
# (Les ints n'ont pas de limite en Python : 2 ** 10_000 fonctionne très bien !)

#   13. Une assertion fausse (le mot-clé assert sera vu au chap. 29)
try:
    assert 1 + 1 == 3, "1 + 1 devrait valoir 3 ?!"  # => AssertionError
except AssertionError as err:
    print(f"22: (Sans ce try: … except …, cette ligne créerait : {err})")

#   14. Une fonction qui s'appelle elle-même indéfiniment
def sans_fin():
    return sans_fin()


try:
    sans_fin()       # => RecursionError: maximum recursion depth exceeded
except RecursionError as err:
    print(f"23: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Il y a des dizaines d'autres erreurs et il ne sert à rien de toutes les
connaître. Mais, encore une fois, il faut BIEN LIRE LES MESSAGES D'ERREURS.

Résumé des erreurs les plus fréquentes :

| erreur              | cause typique                                        |
| ------------------- | ---------------------------------------------------- |
| SyntaxError         | code invalide (":" oublié, parenthèse non fermée…)   |
| IndentationError    | mauvaise indentation en début de ligne               |
| NameError           | variable ou fonction inconnue (faute de frappe ?)    |
| TypeError           | opération sur un type inadapté, mauvais nb d'args    |
| ValueError          | bon type mais valeur inadaptée (int("abc"))          |
| IndexError          | indice hors des limites d'une liste/string/tuple     |
| KeyError            | clé absente d'un dictionnaire                        |
| AttributeError      | méthode ou attribut inexistant ("abc".bizarre())     |
| ZeroDivisionError   | division ou modulo par 0                             |
| ImportError         | module introuvable ou non installé                   |
| FileNotFoundError   | fichier introuvable                                  |
| AssertionError      | assert dont la condition est fausse                  |
"""


# La hiérarchie des exceptions
###############################

"""
Les types d'erreurs sont organisés en "familles", comme un arbre
généalogique : certaines erreurs sont des cas particuliers d'autres erreurs.
Voici un extrait de cette hiérarchie (la liste complète est dans la
documentation : https://docs.python.org/3/library/exceptions.html) :

BaseException
 ├── KeyboardInterrupt       (l'utilisateur a tapé Ctrl+C)
 ├── SystemExit              (le programme demande à quitter, avec sys.exit())
 └── Exception               (toutes les erreurs "normales")
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError        (erreur de recherche dans une collection)
      │    ├── IndexError
      │    └── KeyError
      ├── OSError            (erreurs du système d'exploitation)
      │    └── FileNotFoundError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── AssertionError
      ├── AttributeError
      ├── NameError
      ├── RuntimeError
      │    └── RecursionError
      ├── SyntaxError
      │    └── IndentationError
      ├── TypeError
      └── ValueError

IMPT : intercepter une erreur intercepte aussi toutes ses "descendantes".
Ainsi "except LookupError" intercepte les IndexError ET les KeyError :
"""
for collection, cle in [([1, 2], 5), ({"a": 1}, "z")]:
    try:
        collection[cle]
    except LookupError as err:
        print(f"Erreur de recherche ({type(err).__name__}) avec la clé {cle!r}")
"""
Erreur de recherche (IndexError) avec la clé 5
Erreur de recherche (KeyError) avec la clé 'z'
"""

# On peut vérifier si un type d'erreur "descend" d'un autre avec la fonction
# intégrée issubclass() :
print(issubclass(ZeroDivisionError, ArithmeticError))  # => True
print(issubclass(FileNotFoundError, OSError))          # => True
print(issubclass(KeyError, IndexError))                # => False (ce sont
                                                       #    des "cousines")

"""
Note : KeyboardInterrupt et SystemExit ne descendent PAS de Exception. C'est
voulu : un "except Exception" n'empêche pas l'utilisateur d'interrompre le
programme avec Ctrl+C.
"""


# Gérer les erreurs avec try: … except: …
##########################################

"""
Pour intercepter une erreur, on utilisera les mots-clés "try" et "except",
que l'on mettra "autour" du code qui peut créer une erreur :

try:
    <code qui peut créer une erreur>
except <TypeDErreur>:
    <code exécuté seulement si cette erreur survient>

Fonctionnement :
    1. Python exécute le bloc "try" ligne par ligne.
    2. S'il n'y a pas d'erreur, le bloc "except" est ignoré.
    3. Si une erreur survient, le reste du bloc "try" est abandonné, et Python
       cherche une clause "except" qui correspond au type de l'erreur :
        - s'il en trouve une, il exécute son bloc, puis le programme
          CONTINUE APRÈS le try: … except: … ;
        - sinon, l'erreur continue de "remonter" (et crashe le programme si
          personne d'autre ne l'intercepte).
"""
try:
    for i in range(6):
        print(1 / (5 - i))
except ZeroDivisionError:
    # Ici on met le code qui doit "sauver" l'exécution du programme
    print(f"Division par 0 avec {i}")
else:   # clause optionnelle, exécutée s'il n'y a PAS d'erreur (voir plus bas)
    print(f"Pas de division par 0 avec {5 - i}, cool !")
"""
0.2
0.25
0.3333333333333333
0.5
1.0
Division par 0 avec 5
"""

"""
Notez qu'on ne "catche" QUE les ZeroDivisionError : si on en rencontre d'autres,
elles feront planter le programme !

Pour récupérer l'objet erreur lui-même (et afficher son message), on utilise
"as" suivi d'un nom de variable (souvent "err" ou "e") : c'est ce qu'on fait
depuis le début du cours.
"""
try:
    int("douze")
except ValueError as err:
    print(f"Conversion impossible : {err}")
    # => Conversion impossible : invalid literal for int() with base 10: 'douze'

"""
On peut dire à except d'intercepter plusieurs types d'erreurs, de deux
façons :

    1. avec plusieurs clauses "except", chacune avec son propre traitement.
       Python les teste DANS L'ORDRE et n'exécute que la PREMIÈRE qui
       correspond.
"""
def diviser_element(liste, indice, diviseur):
    try:
        resultat = liste[indice] / diviseur
    except ZeroDivisionError:
        print("Division par 0 !")
    except IndexError:
        print(f"L'indice {indice} n'existe pas")
    except TypeError as err:
        print(f"Mauvais type : {err}")
    else:
        print(f"Résultat : {resultat}")


diviser_element([10, 20], 1, 4)    # => Résultat : 5.0
diviser_element([10, 20], 1, 0)    # => Division par 0 !
diviser_element([10, 20], 7, 2)    # => L'indice 7 n'existe pas
diviser_element([10, 20], 0, "2")  # => Mauvais type : unsupported operand type(s) for /: 'int' and 'str'

"""
Attention à l'ordre : comme la première clause qui correspond gagne, il faut
mettre les erreurs les plus PRÉCISES en premier. Ici, la clause
ZeroDivisionError ne serait jamais atteinte, car ArithmeticError (sa
"parente") l'intercepte avant :
"""
try:
    1 / 0
except ArithmeticError:
    print("Erreur arithmétique")      # => c'est cette clause qui s'exécute
except ZeroDivisionError:
    print("Division par 0")           # jamais atteint !

"""
    2. avec un tuple de types d'erreurs, quand le traitement est le même pour
       toutes :
"""
def une_fonction_qui_peut_creer_des_erreurs(x):
    return len(x) + x


for argument in [5, "abc"]:
    try:
        une_fonction_qui_peut_creer_des_erreurs(argument)
    except (TypeError, NameError):
        print("TypeError et NameError ne nous gênent pas ici, on passe")
# => (deux fois) TypeError et NameError ne nous gênent pas ici, on passe

"""
Exemple classique : la gestion d'erreurs d'une saisie utilisateur (cf.
chap. 11). On redemande la saisie tant qu'elle n'est pas valide.
"""
while True:
    age = input('Quel est votre âge ? ')
    try:
        # int() peut créer une erreur si on lui passe une chaîne absurde
        age = int(age)
    except ValueError:
        print('Vous devez utiliser des chiffres.')
    else:
        break # Ceci permet de sortir de la boucle while
print(f"Vous avez {age} ans.")

"""
Pour catcher TOUTES les erreurs "normales", on peut utiliser "Exception", qui
est l'ancêtre de presque toutes les erreurs (voir la hiérarchie plus haut) :
"""
def fonction_qui_peut_planter():
    return {"a": 1}["b"]


try:
    fonction_qui_peut_planter()
except Exception as err:
    print(f"Erreur ! Erreur ! Erreur ! ({type(err).__name__}: {err})")
    # => Erreur ! Erreur ! Erreur ! (KeyError: 'b')

"""
On rencontre aussi parfois un "except:" sans aucun type, qui intercepte
ABSOLUMENT TOUT, y compris Ctrl+C (KeyboardInterrupt) : c'est à éviter, on
risque d'obtenir un programme impossible à arrêter !

IMPT : de manière générale, intercepter toutes les erreurs est une mauvaise
habitude : on risque de cacher de vrais bugs (une faute de frappe dans un nom
de variable deviendrait silencieuse !). On intercepte de préférence des
erreurs PRÉCISES, qu'on sait traiter.

Si l'on veut volontairement ignorer une erreur, on utilise le mot-clé "pass",
qui signifie "ne rien faire" (un bloc ne peut pas être vide en Python) :
"""
try:
    d["clé absente"]
except KeyError:
    pass  # on ignore volontairement l'erreur

"""
Enfin, il faut garder le bloc "try" le plus COURT possible : on n'y met que la
ou les lignes susceptibles de créer l'erreur que l'on veut traiter. Sinon, on
risque d'intercepter une erreur venant d'une autre ligne, à laquelle on ne
s'attendait pas.
"""


# Les clauses else et finally
##############################

"""
Un bloc try peut comporter deux clauses optionnelles, après les "except" :

    - "else" : exécutée seulement si AUCUNE erreur n'est survenue dans le
      "try". On y met le code qui dépend de la réussite du "try", mais qui ne
      doit pas lui-même être protégé.

    - "finally" : exécutée DANS TOUS LES CAS, qu'il y ait eu une erreur ou non,
      et même si l'erreur n'a pas été interceptée. On l'utilise pour
      "faire le ménage" (fermer un fichier, une connexion…).

L'ordre complet est donc : try → except (un ou plusieurs) → else → finally.
"""
def tester(diviseur):
    try:
        resultat = 10 / diviseur
    except ZeroDivisionError:
        print("  except : division par 0")
    else:
        print(f"  else : le résultat est {resultat}")
    finally:
        print("  finally : exécuté dans tous les cas")


print("Avec 2 :")
tester(2)
"""
Avec 2 :
  else : le résultat est 5.0
  finally : exécuté dans tous les cas
"""
print("Avec 0 :")
tester(0)
"""
Avec 0 :
  except : division par 0
  finally : exécuté dans tous les cas
"""

# "finally" s'exécute même si l'erreur n'est pas interceptée par ce try-là :
try:
    try:
        int("abc")
    finally:
        print("finally : on fait le ménage avant que l'erreur ne remonte")
except ValueError as err:
    print(f"24: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
finally : on fait le ménage avant que l'erreur ne remonte
24: (Sans ce try: … except …, cette ligne créerait : invalid literal for int() with base 10: 'abc')
"""


# Soulever ses propres erreurs avec raise
##########################################

"""
On a vu au début du chapitre que "raise" permet de soulever une erreur
soi-même. C'est très utile dans ses propres fonctions, pour REFUSER des
arguments absurdes plutôt que de retourner un résultat faux :

raise <TypeDErreur>("message explicatif")

On choisit le type d'erreur le plus adapté (souvent ValueError pour une
valeur inadaptée, TypeError pour un type inadapté), et un message clair.
"""
def calculer_moyenne(notes):
    if len(notes) == 0:
        raise ValueError("impossible de calculer la moyenne d'une liste vide")
    for note in notes:
        if note < 0 or note > 20:
            raise ValueError(f"la note {note} n'est pas entre 0 et 20")
    return sum(notes) / len(notes)


print(calculer_moyenne([12, 15, 9]))  # => 12.0

try:
    calculer_moyenne([])
except ValueError as err:
    print(f"25: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    calculer_moyenne([12, 25])
except ValueError as err:
    print(f"26: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Pourquoi soulever une erreur plutôt qu'afficher un message avec print() ?
    - une erreur ARRÊTE le traitement : on est sûr de ne pas continuer avec un
      résultat absurde,
    - c'est la fonction APPELANTE qui décide quoi faire (intercepter, ou
      laisser crasher), ce qui rend la fonction réutilisable,
    - l'erreur indique précisément où et pourquoi le problème a eu lieu.

On peut aussi intercepter une erreur, faire quelque chose (par exemple
l'afficher, ou l'enregistrer dans un journal), puis la RE-SOULEVER avec "raise"
tout seul, pour la laisser continuer sa remontée :
"""
def convertir(texte):
    try:
        return int(texte)
    except ValueError:
        print(f"Problème lors de la conversion de {texte!r}")
        raise  # re-soulève la même erreur


try:
    convertir("dix")
except ValueError as err:
    print(f"27: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
Problème lors de la conversion de 'dix'
27: (Sans ce try: … except …, cette ligne créerait : invalid literal for int() with base 10: 'dix')
"""

"""
Note : on peut même créer ses propres types d'erreurs, mais cela nécessite la
notion de "classe", qui dépasse le cadre de ce cours.
"""


# Live and let die : quand laisser crasher ?
#############################################

"""
Que l'erreur ait été soulevée par le programme ou par "raise", cette erreur
va, par défaut, interrompre le programme. Si l'on souhaite empêcher cette
interruption, il faut demander à Python "d'intercepter" l'erreur.

Savoir quelle erreur intercepter et laquelle faire crasher le programme
n'est pas évident… ce sera à vous de décider à chaque fois !

Certains programmes critiques ne doivent JAMAIS être interrompus
(pacemakers, centrales nucléaires, ordinateur de bord d'avion, réseaux
électriques…).

Pour beaucoup d'autres (serveurs web, ordinateurs personnels, jeux…), il
est plus simple de laisser le programme crasher et le relancer ensuite.

Quelques repères :
    - On intercepte une erreur quand on sait QUOI FAIRE pour continuer
      proprement : redemander une saisie, utiliser une valeur par défaut,
      ignorer une ligne mal formée dans un fichier de données, réessayer une
      connexion…
    - On laisse crasher quand l'erreur révèle un BUG (une faute de frappe, une
      situation "impossible") : il vaut mieux un crash bruyant, avec un
      message clair, qu'un programme qui continue en silence avec des données
      fausses.
    - En Data Science en particulier, un résultat faux mais plausible est bien
      plus dangereux qu'un crash !

Note : il existe deux "philosophies" pour se protéger des erreurs :
    - "Look Before You Leap" (LBYL, "regarde avant de sauter") : on vérifie
      d'abord avec un if que l'opération est possible ;
    - "Easier to Ask Forgiveness than Permission" (EAFP, "il est plus facile de
      demander pardon que la permission") : on tente l'opération dans un try,
      et on gère l'erreur si elle survient. C'est le style le plus courant en
      Python.
"""
stock = {"pommes": 3}

# Style LBYL
if "poires" in stock:
    print(stock["poires"])
else:
    print("Pas de poires")  # => Pas de poires

# Style EAFP
try:
    print(stock["poires"])
except KeyError:
    print("Pas de poires")  # => Pas de poires

"""
Parfois la solution est de laisser crasher/éteindre puis relancer. C'est la
raison pour laquelle la première question qu'un spécialiste pose quand on a
un problème d'informatique est :

"Avez-vous essayé d'éteindre et de rallumer votre ordinateur ?"
"""
