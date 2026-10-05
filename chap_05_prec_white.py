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
#  Chap. 5      #  Ordre des opérations (précédence), whitespace               #
#               #                                                              #
################################################################################
#
#  - Précédence des opérateurs
#  - Associativité : de gauche à droite… sauf exception
#  - Whitespace
#  - Les erreurs d'indentation
#  - Espaces ou tabulations ?
#  - Couper une ligne trop longue
#  - Le whitespace recommandé (PEP 8)
#
###################################

# Précédence des opérateurs
############################

"""
DÉFINITION :
Une EXPRESSION est une combinaison de valeurs et d'opérateurs (ou d'appels de
fonction) qui peut être évaluée pour retourner une valeur.
"""
print(2 + 3)  # => 5 (l'expression "2 + 3" est évaluée et retourne 5)
print(1 + 1 == 2)  # => True (l'expression est évaluée et retourne True)
# (True est une valeur "booléenne", qui signifie "vrai" : cf. chap. 9)

"""
Dans une expression, l'ordre dans lequel les opérations sont évaluées par
Python (on appelle cela la "précédence") suit grosso modo celui des opérateurs
mathématiques :
"""
print(2 + 3 * 6)    # => 20 (2 + 18 : la multiplication passe avant)
print((2 + 3) * 6)  # => 30 (5 * 6 : les parenthèses passent avant tout)

"""
Voici l'ordre décroissant d'évaluation des opérations (du plus prioritaire au
moins prioritaire) :
    1. les parenthèses `( … )`
    2. l'exponentiation (ou puissance), `**`
    3. le signe d'un nombre : `-x` (moins "unaire") et `+x`
    4. les opérateurs `*`, `/`, `//` et `%`
    5. les opérateurs `+` et `-` (addition et soustraction)
    6. les opérateurs de comparaison, d'égalité et d'inégalité (`==`, `!=`,
       `<`, `>`, `<=`, `>=`), ainsi que `in`, `not in`, `is` et `is not`
       (cf. chap. 9, 16 et 19)
    7. `not`, puis `and`, puis `or` (cf. chap. 9)

Remarque : l'affectation `=` (comme dans `a = 3`, cf. chap. 10) ne fait PAS
partie de cette liste. Ce n'est pas un opérateur mais une instruction : on
évalue d'abord TOUTE l'expression à droite du `=`, puis on range le résultat
dans la variable.

On peut, bien sûr, utiliser des parenthèses pour changer cette précédence :
"""
print((5 - 1) * ((7 + 1) / (3 - 1)))  # => 16.0
# Détail : (7 + 1) => 8, (3 - 1) => 2, 8 / 2 => 4.0, (5 - 1) => 4,
# et enfin 4 * 4.0 => 16.0

# Quelques exemples (essayez de trouver le résultat avant de lire la réponse !)
print(2 * 3 ** 2)   # => 18 (3 ** 2 = 9 d'abord, puis 2 * 9)
print(17 % 5 * 2)   # => 4 (même niveau : de gauche à droite, 17 % 5 = 2, puis
#                       2 * 2)
print(1 + 2 < 4)    # => True (1 + 2 = 3 d'abord, puis 3 < 4)

# Attention au moins unaire : il passe APRÈS la puissance
print(-2 ** 2)    # => -4 (c'est -(2 ** 2), et non (-2) ** 2)
print((-2) ** 2)  # => 4

"""
L'ordre n'est pas à connaître par cœur, il faut juste savoir qu'il y en a un.
En cas de doute, utilisez des parenthèses ! Elles ne coûtent rien et rendent
le code plus lisible, même quand elles ne sont pas strictement nécessaires.
"""


# Associativité : de gauche à droite… sauf exception
#####################################################

"""
Par défaut, les opérations au sein du même niveau de précédence sont
évaluées de gauche à droite (on dit qu'elles sont "associatives à gauche").

C'est important pour la soustraction et la division, où l'ordre change le
résultat :
"""
print(10 - 4 - 3)    # => 3 (c'est (10 - 4) - 3)
print(10 - (4 - 3))  # => 9
print(100 / 10 / 5)  # => 2.0 (c'est (100 / 10) / 5)
print(7 // 2 * 2)    # => 6 (c'est (7 // 2) * 2 = 3 * 2)

# Exception : l'exponentiation est évaluée de DROITE à GAUCHE, comme en
# mathématiques (2 puissance 3 puissance 2 se lit 2^(3^2))
print(2 ** 3 ** 2)    # => 512 (c'est 2 ** (3 ** 2) = 2 ** 9)
print((2 ** 3) ** 2)  # => 64 (c'est 8 ** 2)


# Whitespace
#############

"""
Le whitespace ("espace vide") désigne tous les caractères qui servent à
espacer les mots ou les lignes les uns des autres : espaces, tabulations,
sauts de ligne, etc.

À la différence de beaucoup de langages, le whitespace en Python peut changer
le sens du programme : on dit qu'il est "sémantique" (= il porte une
signification).

Exemple (la structure "if" sera vue en détail au chap. 12 : elle exécute les
lignes en retrait seulement si la condition est vraie) :
"""
a = 2
if a + 1 == 3:
    print("a = 2")  # => a = 2
print("pouet")  # => pouet
"""
Dans le programme ci-dessus, ce sont les espaces en début de ligne qui
indiquent que le premier print() est "dans le if". On verra que le
whitespace en DÉBUT de ligne est particulièrement important en Python.

Ces espaces en début de ligne s'appellent l'"indentation" (ou le "retrait").
Là où d'autres langages (C, Java, JavaScript…) utilisent des accolades { }
pour délimiter les blocs de code, Python utilise uniquement l'indentation.
C'est ce qui rend le code Python si aéré et lisible… mais aussi ce qui oblige à
être rigoureux.

Comparez avec cette version, où le second print() est AUSSI dans le if : la
seule différence est l'indentation de la dernière ligne.
"""
a = 5
if a + 1 == 3:
    print("a = 2")
    print("pouet")  # rien n'est affiché : la condition est fausse

"""
En revanche, les espaces et tabulations ("whitespace") en milieu de ligne
n'importent pas :
"""
print(4 - 3)  # => 1 (c'est la présentation recommandée mais…)
print(4- 3)   # => 1 (… fonctionne aussi)
print(4 -3)   # => 1 (… fonctionne aussi)
print(4            -   3)  # => 1 (… aussi !)

# Attention : on ne peut pas mettre d'espace AU MILIEU d'un nom ou d'un
# opérateur composé de plusieurs caractères : `* *` n'est pas `**`, et
# `pri nt` n'est pas `print`.

# Les lignes vides n'ont pas non plus d'importance pour Python : elles servent
# seulement à aérer le code et à séparer visuellement ses différentes parties.


# Les erreurs d'indentation
############################

"""
Si l'indentation est incohérente, Python refuse d'exécuter le programme et
signale une "IndentationError" (erreur d'indentation). C'est une erreur de
SYNTAXE : elle est détectée avant même l'exécution de la première ligne du
fichier.

Pour pouvoir vous montrer ces erreurs sans empêcher ce fichier de
s'exécuter, on utilise ci-dessous la fonction exec(), qui exécute du code
Python contenu dans une chaîne de caractères ("\n" représente un saut de ligne,
cf. chap. 7). Vous n'aurez jamais besoin d'exec() dans ce cours : retenez
seulement le code qu'on lui passe, écrit en commentaire au-dessus.

Note : le texte exact des erreurs peut varier selon votre version de Python.
"""

# Erreur n° 1 : une ligne indentée sans raison
#   x = 1
#     y = 2
try:
    exec("x = 1\n    y = 2")
except IndentationError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# Erreur n° 2 : un bloc (après les ":" du if) qui n'est pas indenté
#   if True:
#   print("oups")
try:
    exec("if True:\nprint('oups')")
except IndentationError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# Erreur n° 3 : mélange de tabulations et d'espaces dans un même bloc
# (l'erreur s'appelle alors "TabError", c'est un cas particulier
# d'IndentationError)
try:
    exec("if True:\n\tx = 1\n        y = 2")
except IndentationError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")


# Espaces ou tabulations ?
###########################

"""
Il y a parfois confusion entre tabulations et espaces multiples en début de
ligne.

Une tabulation (`\t`) est un caractère spécial, différent d'une suite d'espaces.
Il sert originellement à aligner du texte sur différents curseurs de ligne.
Certains éditeurs le remplacent par des espaces, d'autres non. Le problème :
une tabulation et quatre espaces se ressemblent à l'écran, mais Python les
considère comme différents (cf. l'erreur n° 3 ci-dessus).

Il est fortement conseillé de ne JAMAIS mélanger espaces et tabulations. Mieux,
de ne jamais utiliser de tabulations DU TOUT, et d'utiliser 4 espaces pour
toutes les indentations (cf. https://peps.python.org/pep-0008/#indentation).

Bonne nouvelle : la plupart des éditeurs peuvent être configurés pour insérer
4 espaces quand on appuie sur la touche Tab. Vérifiez que c'est le cas du
vôtre ! (Sur Sublime Text : "translate_tabs_to_spaces": true et
"tab_size": 4 ; sur VS Code, c'est le réglage par défaut pour Python.)

La plupart des bons éditeurs de texte proposent aussi une option pour afficher
le whitespace, afin de repérer d'un coup d'œil celui qui est utilisé (sur
Sublime Text, c'est la ligne : "draw_white_space": "all" dans votre fichier de
configuration).

La plupart des bons éditeurs de texte proposent aussi des plugins pour
bien formater automatiquement votre code : ils intègrent des formateurs comme
black, autopep8, yapf… Ils seront présentés au chap. 20.
"""


# Couper une ligne trop longue
###############################

"""
Une instruction Python tient normalement sur une seule ligne : le saut de
ligne marque la fin de l'instruction. Mais une expression longue devient vite
illisible. Il y a deux façons de l'écrire sur plusieurs lignes.

1. (Recommandé) Entourer l'expression de parenthèses : à l'intérieur de
   parenthèses (ou de crochets [ ] et d'accolades { }, cf. chap. 16 et 18),
   les sauts de ligne et l'indentation sont ignorés.
"""
total = (1 + 2 + 3
         + 4 + 5
         + 6)
print(total)  # => 21

# Les parenthèses d'un appel de fonction fonctionnent de la même façon
print(
    1 + 2,
    3 + 4,
)  # => 3 7

"""
2. Terminer la ligne par une barre oblique inversée `\\` (un "backslash"), qui
   signifie "l'instruction continue à la ligne suivante". C'est moins
   recommandé : un simple espace après le `\\` provoque une erreur, invisible à
   l'œil nu.
"""
total = 1 + 2 + 3 \
    + 4 + 5
print(total)  # => 15


# Le whitespace recommandé (PEP 8)
###################################

"""
La "PEP 8" est le guide de style officiel de Python
(https://peps.python.org/pep-0008). Elle n'est pas obligatoire, mais presque
tout le monde la suit : du code qui la respecte est plus facile à lire par les
autres. Voici ses principales recommandations sur le whitespace :

    - indentation de 4 espaces (cf. plus haut) ;
    - lignes de 79 caractères maximum (on coupe les lignes trop longues, cf.
      plus haut) ;
    - une espace de chaque côté des opérateurs `=`, `+`, `-`, `==`, etc. :
          x = 2 + 3       plutôt que    x=2+3
    - on peut toutefois "coller" les opérateurs les plus prioritaires pour
      faire ressortir la précédence :
          y = x*2 + 1     (plutôt que y = x * 2 + 1, au choix)
    - pas d'espace juste à l'intérieur des parenthèses, ni avant une virgule ;
      une espace après la virgule :
          print(1, 2)     plutôt que    print( 1 , 2 )
    - pas d'espace entre le nom d'une fonction et sa parenthèse :
          print(3)        plutôt que    print (3)
    - pas d'espaces inutiles en fin de ligne ("trailing whitespace") ;
    - des lignes vides pour séparer les parties du programme (deux lignes vides
      autour des définitions de fonctions, cf. chap. 14).

Le formatage du code (et les outils qui l'automatisent) est détaillé au
chap. 20.
"""
x = 2 + 3
y = x*2 + 1
print(x, y)  # => 5 11
