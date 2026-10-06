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
#  Chap. 8      #  Manipuler les strings                                       #
#               #                                                              #
################################################################################
#
#  - Chercher et remplacer dans une chaîne
#  - D'autres méthodes sur les strings
#  - Tester le contenu d'une chaîne
#  - Interpoler une chaîne
#  - Formater des nombres dans une chaîne
#  - Concaténation ou interpolation ?
#  - Conversions de caractères : chr() et ord()
#  - Chaînes longues
#
####################################################

"""
Rappel : dans ce cours, une valeur écrite seule sur une ligne (sans print())
est suivie de son résultat tel que l'afficherait l'interpréteur interactif,
c'est-à-dire avec des guillemets pour les strings (cf. chap. 7). Testez ces
lignes dans l'interpréteur !
"""

# Chercher et remplacer dans une chaîne
########################################

"""
    1. `in` et `not in` permettent de tester si une sous-chaîne figure dans une
       chaîne. Le résultat est un booléen, True ou False (cf. chap. 9).
"""
"ab" in "abcd"     # => True
"ab" in "def"      # => False
"ab" not in "def"  # => True
"AB" in "abcd"     # => False (les majuscules comptent)


"""
    2. La méthode `.find()` renvoie le rang auquel la sous-chaîne a été trouvée
       (et -1 si la sous-chaîne ne figure pas dans la chaîne)
"""
s = "abcdefgh"
s.find("cd")  # => 2
s.find("gh")  # => 6
s.find("hi")  # => -1

# Si la sous-chaîne apparaît plusieurs fois, c'est le rang de la PREMIÈRE
# occurrence qui est renvoyé. `.rfind()` renvoie celui de la dernière.
"abcabc".find("bc")   # => 1
"abcabc".rfind("bc")  # => 4
# Pour chercher une FORME plutôt qu'un texte précis (un nombre, une date…),
# on utilisera les expressions régulières (cf. chap. 42).


"""
    3. .replace() permet de remplacer une chaîne de caractères par une autre…
"""
"J'aime les pommes".replace("e", "z")  # => "J'aimz lzs pommzs"
#       …ou de la supprimer complètement (on passe une chaîne vide)
"J'aime les pommes".replace("e", "")  # => "J'aim ls pomms"
"Les chiens sont adorables.".replace("chiens", "lapins")  # => 'Les lapins sont adorables.'

# Un 3e paramètre (optionnel) limite le nombre de remplacements
"a-b-c-d".replace("-", "+", 2)  # => 'a+b+c-d'

# Rappel : la chaîne d'origine n'est jamais modifiée (cf. chap. 7). Pour
# conserver le résultat, il faut le stocker dans une variable :
phrase = "J'aime les pommes"
phrase.replace("pommes", "poires")
print(phrase)  # => J'aime les pommes (rien n'a changé !)
nouvelle_phrase = phrase.replace("pommes", "poires")
print(nouvelle_phrase)  # => J'aime les poires


# D'autres méthodes sur les strings
####################################

#   1. La méthode .split(<separateur>) sépare une chaîne en une liste de
#      sous-chaînes (par défaut, le séparateur est le whitespace : espaces,
#      tabulations, sauts de ligne…). Les listes seront vues au chap. 16.
"Il reste du fromage ?".split()  # => ['Il', 'reste', 'du', 'fromage', '?']
"12.5;17.5;18".split(";")  # => ['12.5', '17.5', '18']

# Sans séparateur, les espaces multiples sont regroupés…
"  a   b  ".split()  # => ['a', 'b']
# …mais avec un séparateur explicite, chaque séparateur compte : deux
# séparateurs consécutifs donnent une chaîne vide
"a,b,,c".split(",")  # => ['a', 'b', '', 'c']

# On peut limiter le nombre de découpes avec un 2e paramètre
"nom prénom et le reste".split(" ", 1)  # => ['nom', 'prénom et le reste']


"""
    2. La méthode `.join()` permet de convertir une liste de strings en une
       seule string
"""
lettres = ["p", "o", "u", "e", "t"]
"".join(lettres)  # => 'pouet'
"--".join(lettres)  # => 'p--o--u--e--t'
" ".join(["Salut", "c'est", "cool"])  # => "Salut c'est cool"

"""
Détail du fonctionnement : la chaîne sur laquelle on appelle .join() est le
SÉPARATEUR. Elle est insérée ENTRE chaque élément de la liste (pas avant le
premier, ni après le dernier). Ainsi, pour :
    "--".join(["p", "o", "u"])
Python construit : "p" + "--" + "o" + "--" + "u", soit 'p--o--u'.

Tous les éléments de la liste doivent être des strings, sinon Python soulève
une erreur :
"""
try:
    "-".join(["a", 1, "b"])  # => TypeError: sequence item 1: expected str
    #                                         instance, int found
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# .split() et .join() sont "inverses" l'un de l'autre. On les combine souvent,
# par exemple pour changer de séparateur :
"12.5;17.5;18".split(";")  # => ['12.5', '17.5', '18']
", ".join("12.5;17.5;18".split(";"))  # => '12.5, 17.5, 18'

"""
Note : vous trouveriez plus logique d'écrire
lettres.join("--")    au lieu de     "--".join(lettres)  ? Moi aussi :)
"""


#   3. Les méthodes .upper() et .lower() changent la capitalisation d'une string
s2 = "aBcdEFgh"
s2.upper()  # => 'ABCDEFGH'
s2.lower()  # => 'abcdefgh'

# C'est très utile pour comparer des chaînes sans tenir compte des majuscules :
"Python".lower() == "PYTHON".lower()  # => True


"""
    4. La méthode .capitalize() va capitaliser la première lettre seulement, et
       mettre les autres lettres en minuscule. La méthode .title() capitalise
       la première lettre de CHAQUE mot.
"""
s2.capitalize()  # => 'Abcdefgh'
"le petit chat".title()  # => 'Le Petit Chat'


"""
    5. Les méthodes .lstrip(), .rstrip() et .strip() enlèvent les espaces à
       droite et à gauche d'une chaîne (lstrip : left, rstrip : right, strip :
       les deux)
"""
"    des espaces  ".rstrip()    # => '    des espaces'
"    des espaces  ".lstrip()    # => 'des espaces  '
"    des espaces     ".strip()  # => 'des espaces'

# On peut aussi leur indiquer quels caractères enlever :
"...Bonjour !!!".strip(".!")  # => 'Bonjour '


"""
    6. Les méthodes .rjust(n) et .ljust(n) permettent de donner à une string
       une largeur fixe, ce qui est très pratique pour un affichage en
       colonnes de largeur fixe. .center(n) centre la chaîne.
"""
"abc".rjust(8)  # => '     abc'
"abc".ljust(8)  # => 'abc     '
"abc".center(9, "*")  # => '***abc***' (2e paramètre : caractère de remplissage)
"42".zfill(5)   # => '00042' (complète avec des zéros à gauche)

# Exemple d'affichage en colonnes :
print("Pommes".ljust(10) + "3".rjust(5))
print("Kiwis".ljust(10) + "12".rjust(5))
# => Pommes        3
# => Kiwis        12


"""
    7. La méthode .count(str) compte le nombre de sous-chaînes dans une chaîne.
"""
"Python est un langage Pythonique et puissant. Ô Python !".count("Python")  # => 3


# Tester le contenu d'une chaîne
#################################

"""
Certaines méthodes retournent un booléen (True ou False, cf. chap. 9) selon le
contenu de la chaîne :
    - .startswith(s) : la chaîne commence-t-elle par s ?
    - .endswith(s)   : la chaîne se termine-t-elle par s ?
    - .isdigit()     : la chaîne ne contient-elle que des chiffres ?
    - .isalpha()     : la chaîne ne contient-elle que des lettres ?
    - .isspace()     : la chaîne ne contient-elle que du whitespace ?
    - .isupper() / .islower() : est-elle tout en majuscules/minuscules ?
"""
"Bonjour".startswith("Bon")  # => True
"photo.jpg".endswith(".jpg")  # => True
"photo.png".endswith(".jpg")  # => False

"42".isdigit()   # => True
"4.2".isdigit()  # => False (le point n'est pas un chiffre)
"-4".isdigit()   # => False (le signe moins non plus)
"".isdigit()     # => False (une chaîne vide ne contient aucun chiffre)

"abc".isalpha()  # => True
"ab1".isalpha()  # => False
"   ".isspace()  # => True
"ABC".isupper()  # => True

"""
Ces méthodes nous serviront par exemple à vérifier une saisie utilisateur
avant de la convertir en nombre (cf. chap. 11).
"""


# Interpoler une chaîne
########################

"""
L'interpolation sert à insérer des variables dans des chaînes de caractère.
C'est très utile car un texte affiché par un programme doit souvent varier en
fonction d'une saisie utilisateur, d'une variable du programme, etc.
"""

# Quand on veut afficher du texte et une variable, on a vu qu'on pouvait
# concaténer des strings avec l'opérateur "+"
nom = "Michelle"
print("Je m'appelle " + nom)  # => Je m'appelle Michelle

"""
Mais dès qu'on veut faire plus compliqué (prendre deux variables, ou utiliser
la variable au milieu d'un texte, par exemple), la concaténation est peu
pratique.

Exemple : on souhaite afficher un texte contenant un nom et un âge contenus
dans une variable. Avec la concaténation, cela donne :
"""
age = 15
nom = "Michelle"
print("Je m'appelle " + nom + " et j'ai " + str(age) + " ans.")
# => Je m'appelle Michelle et j'ai 15 ans.

"""
…mais c'est complexe : il faut bien penser aux espaces entre les mots, à
convertir les nombres en strings, etc.

L'interpolation règle la plupart de ces difficultés.
"""

"""
Il y a deux méthodes pour interpoler une chaîne de caractères :
    1. La méthode "historique" consiste à utiliser la méthode .format() sur une
       string en lui passant les paramètres souhaités. Chaque paire
       d'accolades "{}" est remplacée, dans l'ordre, par un paramètre.
"""
"{} peuvent être {}".format("Les chaînes", "interpolées")  # => 'Les chaînes
#                                                      peuvent être interpolées'

# Note : .format() convertit automatiquement depuis des entiers ou des floats,
# donc on n'aura pas besoin d'utiliser str() !
"Une string et {}".format(5)  # => 'Une string et 5'

# Même si cela ne se fait plus trop, on peut aussi référencer les variables par
# leur index…
"Je m'appelle {1} et j'ai {0} ans.".format(age, nom)  # => "Je m'appelle
#                                                     Michelle et j'ai 15 ans."
# …ou par un nom :
"{nom} a {age} ans".format(nom="Léa", age=20)  # => 'Léa a 20 ans'

"""
    2. Depuis Python 3.6, on peut aussi utiliser les "f-strings" pour
       interpoler une chaîne avec des variables. La syntaxe en devient beaucoup
       plus lisible, et c'est la méthode la plus utilisée aujourd'hui
"""
f"Salut {nom} !"  # => 'Salut Michelle !'  (Notez le "f" en début de chaîne)
f"Je m'appelle {nom} et j'ai {age} ans."  # => "Je m'appelle Michelle et j'ai
#                                              15 ans."
print(f"Je m'appelle {nom} et j'ai {age} ans.")
# => Je m'appelle Michelle et j'ai 15 ans.

# Entre les accolades, on peut mettre n'importe quelle expression Python : un
# calcul, un appel de méthode…
print(f"L'an prochain, j'aurai {age + 1} ans.")  # => L'an prochain, j'aurai 16 ans.
print(f"EN MAJUSCULES : {nom.upper()}")  # => EN MAJUSCULES : MICHELLE

# Depuis Python 3.8, écrire "=" après l'expression affiche aussi son nom :
# très pratique pour déboguer !
print(f"{age=}")  # => age=15

# Si on a besoin d'écrire de vraies accolades, on les double :
print(f"{{nom}} vaut {nom}")  # => {nom} vaut Michelle


# Formater des nombres dans une chaîne
#######################################

"""
Les f-strings (et .format()) acceptent, après le nom de la variable, deux
points ":" suivis d'une "spécification de format" qui indique COMMENT afficher
la valeur. Les plus utiles :
    - {x:.2f}  : un float avec 2 chiffres après la virgule ("f" pour float)
    - {x:8}    : sur une largeur d'au moins 8 caractères
    - {x:>8}   : aligné à droite sur 8 caractères (< : gauche, ^ : centré)
    - {x:05}   : sur 5 caractères, complété par des zéros
    - {x:,}    : avec un séparateur de milliers
    - {x:.1%}  : en pourcentage, avec 1 décimale
"""
pi = 3.14159
n = 7
print(f"{pi:.2f}")     # => 3.14
print(f"{pi:.4f}")     # => 3.1416 (la valeur est arrondie, pas tronquée)
print(f"[{n:>5}]")     # => [    7]
print(f"[{n:<5}]")     # => [7    ]
print(f"[{'ab':^6}]")  # => [  ab  ]
print(f"{n:05}")       # => 00007
print(f"{1234567.891:,.2f}")  # => 1,234,567.89 (séparateur à l'anglaise)
print(f"{0.256:.1%}")  # => 25.6%

# On retrouve exactement les mêmes spécifications avec .format() :
print("{:.2f}".format(pi))  # => 3.14

"""
Note : on a déjà vu au chap. 6 les spécifications "b" et "x", qui affichent un
entier en binaire ou en hexadécimal :
"""
print(f"{255:x} {5:08b}")  # => ff 00000101

# Exemple : un petit ticket de caisse aligné
print(f"{'Pommes':<10}{3.5:>8.2f} €")
print(f"{'Kiwis':<10}{12:>8.2f} €")
# => Pommes        3.50 €
# => Kiwis        12.00 €


# Concaténation ou interpolation ?
###################################

"""
On dispose donc de trois façons de construire une chaîne contenant des
variables :
"""
prix = 12
print("Le livre coûte " + str(prix) + " euros.")   # concaténation
print("Le livre coûte {} euros.".format(prix))     # .format()
print(f"Le livre coûte {prix} euros.")             # f-string
# => Le livre coûte 12 euros. (trois fois)

"""
Laquelle choisir ?
    - La concaténation (+) convient pour coller deux ou trois chaînes simples
      ("Bonjour " + nom). Dès qu'il y a des nombres ou plusieurs variables,
      elle devient illisible et source d'erreurs (espaces oubliés, str()
      oublié, cf. le TypeError du chap. 7).
    - Les f-strings sont aujourd'hui la solution recommandée dans presque tous
      les cas : le texte final se "lit" directement dans le code, les
      conversions sont automatiques, et on peut formater les nombres.
    - .format() reste utile quand le modèle de texte est défini AVANT de
      connaître les valeurs (par exemple un modèle stocké dans une variable et
      réutilisé plusieurs fois), ou pour du code qui doit tourner sur des
      versions de Python antérieures à 3.6.
"""
modele = "Bonjour {}, bienvenue !"
print(modele.format("Ana"))   # => Bonjour Ana, bienvenue !
print(modele.format("Omar"))  # => Bonjour Omar, bienvenue !


# Conversions de caractères : chr() et ord()
#############################################

# On peut convertir chaque caractère en son indice Unicode, et inversement :

#   1. chr() renvoie le caractère associé à un indice Unicode
chr(65)      # => 'A'
chr(97)      # => 'a'
chr(233)     # => 'é'
chr(128561)  # => '😱'

#   2. Inversement, ord() renvoie un indice Unicode associé à un caractère
ord("A")    # => 65
ord("a")    # => 97
ord("à")    # => 224
ord("😱")   # => 128561

# D'où il s'ensuit que :
chr(ord("A"))  # => 'A'
ord(chr(65))   # => 65

"""
On remarque que les codes ASCII des majuscules/minuscules sont décalés de 32.

On rappelle que les caractères ASCII sont aussi des caractères Unicode, et
vont jusqu'à 127 seulement.
"""
ord("a") - ord("A")  # => 32
chr(ord("G") + 32)   # => 'g'

# Comme les lettres se suivent dans la table, on peut "avancer" d'une lettre :
chr(ord("a") + 1)  # => 'b'
# (c'est le principe du "chiffre de César", un des plus vieux codes secrets !)

# On peut combiner avec hex() (cf. chap. 6) pour retrouver le code \u… du
# chap. 7 :
hex(ord("é"))  # => '0xe9'
print("é")  # => é


# Chaînes longues
##################

# La syntaxe utilisée pour les commentaires longs peut aussi servir pour créer
# des chaînes de plusieurs lignes !
s = """Ceci est
une chaîne
vraiment très longue"""
print(s)
"""
Imprimera :

Ceci est
une chaîne
vraiment très longue
"""

# On peut s'en servir pour de la documentation :
documentation = """
Ce bloc de texte sert à documenter le code.
Il peut contenir des explications détaillées sur le fonctionnement du programme.
"""

# Note : les chaînes longues sont très utilisées pour documenter du code (cf.
# les "docstrings" du chap. 3).

# Si on ne souhaite pas avoir de sauts de ligne, on pourra utiliser des "\" en
# fin de chaque ligne : Python colle alors automatiquement les morceaux.
# ATTENTION : il faut penser aux espaces à la fin de chaque morceau !
query = "SELECT action.descr as \"action\", " \
"role.id as role_id, " \
"role.descr as role " \
"FROM " \
"public.role, " \
"public.record_def, " \
"public.action " \
"WHERE role.id = role_action_def.role_id AND " \
"record_def.id = role_action_def.def_id;"

# L'impression se fera sur une seule ligne
print(query)
# => SELECT action.descr as "action", role.id as role_id, role.descr as role FROM public.role, public.record_def, public.action WHERE role.id = role_action_def.role_id AND record_def.id = role_action_def.def_id;

"""
Sans les espaces en fin de morceau, on obtiendrait par exemple
"role.descr as roleFROM public.role", ce qui n'est pas une requête valide !

Une autre façon, souvent préférée, est de mettre les morceaux entre
parenthèses : deux chaînes écrites côte à côte sont automatiquement collées,
et on n'a plus besoin des "\".
"""
query2 = ("SELECT nom, age "
          "FROM eleves "
          "WHERE age > 15;")
print(query2)  # => SELECT nom, age FROM eleves WHERE age > 15;
