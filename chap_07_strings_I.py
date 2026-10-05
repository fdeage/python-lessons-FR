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
#  Chap. 7      #  Strings I                                                   #
#               #                                                              #
################################################################################
#
#  - Déclarer des strings
#  - Accéder à un caractère
#  - Caractères spéciaux et échappement
#  - Imprimer avec print()
#  - Fonctions de base
#
###########################################

# Déclarer des strings (ou chaînes de caractères)
##################################################

"""
Les chaînes (ou "strings", ou str) sont une suite de caractères
représentant du texte. Elles ne peuvent pas être modifiées une fois créées.
"""

# Elles sont créées avec " " ou ' '
s1 = "Ceci est une chaîne."
s2 = 'Et ceci est une chaîne aussi.'
s3 = ""  # => la chaîne vide (de longueur 0)

print(s1)  # => Ceci est une chaîne.
print(s2)  # => Et ceci est une chaîne aussi.
print(s3)  # => (une ligne vide)

"""
Note : print() affiche le CONTENU de la chaîne, sans les guillemets. Les
guillemets ne font pas partie du texte : ils servent seulement à indiquer à
Python où la chaîne commence et où elle finit.

Dans l'interpréteur interactif (cf. chap. 2), en revanche, une chaîne est
affichée AVEC ses guillemets (simples), pour bien montrer que c'est une
string. C'est pourquoi, dans ce cours, les résultats en commentaire :
    - n'ont pas de guillemets après un print(),
    - ont des guillemets quand on écrit juste une valeur sans print(), comme
      on le ferait dans l'interpréteur.
"""

# Les simples et doubles quotes sont strictement équivalentes :
print("abc" == 'abc')  # => True

# Si on utilise des doubles quotes ("…"), on pourra y insérer des
# simples quotes
"J'aime l'aligot d'Émile"
# Inversement, si on utilise des simples quotes ('  '), on pourra y insérer
# des doubles quotes
'Je lui ai dit : "Fonce, Michel !"'

r"""
Si on a besoin d'insérer des doubles quotes DANS des doubles quotes, ou
l'inverse, il faudra ÉCHAPPER ces quotes avec le caractère "backslash" : \
"""
print('J\'aime l\'aligot d\'Émile')        # => J'aime l'aligot d'Émile
print("Je lui ai dit : \"Fonce, Michel !\"")  # => Je lui ai dit : "Fonce, Michel !"

# Sans échappement, Python croirait que la chaîne s'arrête au 2e guillemet, et
# le reste de la ligne n'aurait aucun sens : ce serait une SyntaxError (une
# erreur de syntaxe, qui empêcherait même le fichier de se lancer).
#     'J'aime l'aligot'  # => SyntaxError

"""
Depuis Python 3, on peut utiliser tous les caractères Unicode dans une string :
accents, diacritiques, emojis, alphabets non-latins, etc.
"""
weird_string = "¡¢£¤¥¦§ àêïœú ÇßÐÞðƓ 中野区 💅😭💉📧🚭🥺 ᠮᠣᠩᠭᠣᠯᠴᠤᠳ ‽̃ͦ"
print(weird_string)  # => (l'affichage dépend des polices de votre terminal)

"""
Note : "Unicode" est une norme internationale qui attribue un numéro unique à
chaque caractère de (presque) toutes les écritures du monde. On verra au
chap. 8 comment manipuler ces numéros avec chr() et ord().
"""


# Accéder à un caractère
#########################

# Une string est une séquence de caractères, similaire à une liste (cf. le
# chap. 16 sur les listes)
s4 = "Ceci est une chaîne"

# On peut accéder à chaque caractère de la chaîne avec la syntaxe "[…]"
s4[0]   # => 'C'
s4[1]   # => 'e'
s4[2]   # => 'c'
s4[3]   # => 'i'
s4[4]   # => ' '
s4[5]   # => 'e'
s4[6]   # => 's'
s4[7]   # => 't'
s4[8]   # => ' '
# …
s4[15]  # => 'a'
s4[16]  # => 'î'
s4[17]  # => 'n'
s4[18]  # => 'e'

print(s4[0])  # => C

"""
Le nombre entre crochets s'appelle l'"indice" (ou "index", ou "rang") du
caractère. Représentons la chaîne avec ses indices :

     C  e  c  i     e  s  t     u  n  e     c  h  a  î  n  e
     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18

IMPT : l'indexation commence toujours, toujours à 0 en Python !
(comme dans la quasi-totalité des langages)

Conséquence : le dernier caractère d'une chaîne de 19 caractères est à
l'indice 18 (et non 19).
"""

# Demander un indice qui n'existe pas crée une erreur :
try:
    s4[19]  # => IndexError: string index out of range
except IndexError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# On peut aussi compter depuis la FIN de la chaîne avec des indices négatifs :
# -1 est le dernier caractère, -2 l'avant-dernier, etc.
s4[-1]  # => 'e'
s4[-2]  # => 'n'
print(s4[-1])  # => e

"""
Note : on peut aussi extraire un morceau entier d'une chaîne (par exemple les
5 premiers caractères) avec la syntaxe s4[0:5]. On appelle cela un "slice" :
nous verrons cela en détail au chap. 31.
"""

# On peut accéder à une lettre mais pas la modifier une fois la chaîne créée :
try:
    s4[2] = "u"  # => TypeError: 'str' object does not support item assignment
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
On dit que les strings sont "immuables" (en anglais : "immutable"). Pour
"modifier" une chaîne, il faudra en fait en créer une nouvelle (par exemple
avec les méthodes vues plus bas, ou au chap. 8).
"""


# Caractères spéciaux et échappement
#####################################

"""
Dans une chaîne de caractères, on peut rencontrer des caractères qui ont un sens
différent de leur rendu visuel dans le code.
"""

# Exemple :
s5 = "abc\ndef\nghi"  # => Ce "\n" encode un saut de ligne
print(s5)             # => … que l'on peut voir en imprimant la variable s5
"""
Résultat

abc
def
ghi
"""

# Attention : "\n" s'écrit avec deux symboles, mais c'est UN SEUL caractère !
print(len("abc\ndef"))  # => 7 (len() compte les caractères, cf. plus bas)

r"""
Ces caractères spéciaux utilisent souvent le caractère backslash : \
\n    => saut de ligne ("newline")
\t    => tabulation
\r    => retour chariot ("carriage return" : retour en début de ligne, hérité
         des machines à écrire)
\r\n  => saut de ligne utilisé dans les fichiers Windows
\'    => un simple quote
\"    => un double quote
\\    => un backslash

Note : dans vos programmes Python, "\n" suffit pour faire un saut de ligne, quel
que soit votre système d'exploitation (Linux, Mac ou Windows).
"""
print("Colonne 1\tColonne 2\nValeur 1\tValeur 2")  # => Intercale des tabulations
"""
Résultat (les colonnes sont alignées par les tabulations) :

Colonne 1	Colonne 2
Valeur 1	Valeur 2
"""

r"""
Ce `\` est appelé un caractère d'échappement : il change la signification du
caractère qui le suit.

Quand on souhaite vraiment avoir un backslash à l'écran, il faut "échapper" ce
caractère avec… un autre backslash
"""
print("\\")  # => \
print("C:\\Users\\michel")  # => C:\Users\michel

"""
Pour éviter de doubler tous les backslashs, on peut aussi préfixer la chaîne
par un "r" (pour "raw", "brut") : les backslashs ne sont alors plus
interprétés. C'est pratique pour les chemins de fichiers Windows, ou pour les
expressions régulières (cf. chap. 22).
"""
print(r"C:\nouveau\dossier")  # => C:\nouveau\dossier (le \n n'est pas un saut
#                                de ligne ici !)

# Enfin, on peut insérer n'importe quel caractère Unicode avec son code
# hexadécimal (cf. chap. 6), avec \u suivi de 4 chiffres :
print("caf\u00e9")  # => café


# Imprimer avec `print()`
##########################

# Python propose la fonction intégrée `print()` pour imprimer du texte à l'écran
print("Salut, monde !")  # => Salut, monde !

# `print()` peut imprimer absolument n'importe quoi : entiers, floats, strings,
# listes, booléens, range…

print([True, "pouet", 150, 2.3, range(4), [1]])  # => [True, 'pouet', 150, 2.3,
#                                                       range(0, 4), [1]]

# On peut passer plusieurs valeurs à print(), séparées par des virgules : elles
# seront imprimées à la suite, séparées par un espace
print("Il fait", 21, "degrés")  # => Il fait 21 degrés

# Le paramètre sep permet de choisir un autre séparateur que l'espace
print("a", "b", "c", sep="-")  # => a-b-c
print("a", "b", "c", sep="")   # => abc

# Appelé sans rien, print() imprime simplement une ligne vide
print()  # => (une ligne vide)

"""
Note : dans l'interpréteur Python, si la dernière valeur retournée n'est pas
affectée dans une variable, alors Python l'imprimera même si on n'a pas appelé
print().

Ceci ne fonctionne pas si on lance un programme depuis son shell (mode 2) avec
`?> python fichier.py`
"""
"Tut tut"             # => 'Tut tut' (seulement dans l'interpréteur)
variable = "Tut tut"  # => (pas d'impression)

# On se servira souvent de `print()` pour afficher le résultat d'un calcul.
# Voici une fonction (ne vous préoccupez pas encore de la syntaxe, les
# fonctions seront vues en détail au chap. 14) :
def ma_super_fonction(a, b):
    print("Du texte")
    return a + b

# Appeler la fonction imprimera la valeur du `print()`. Dans l'interpréteur,
# la valeur retournée par la fonction sera également affichée :
ma_super_fonction(2, 3)
# => Du texte
# => 5 (seulement dans l'interpréteur)

# Pour afficher la valeur retournée dans un programme, il faut un print() :
print(ma_super_fonction(2, 3))
# => Du texte
# => 5

r"""
IMPT : `print()` rajoute par défaut un saut de ligne à la fin de chaque
impression. Les sauts de ligne se notent `\n`.

Pour empêcher ce fonctionnement, il faut utiliser end='' :
"""
print("test1", end='')
print("test2", end='')
print("test3")
# => test1test2test3

# On peut aussi choisir un autre texte de fin :
print("Chargement", end="... ")
print("terminé !")
# => Chargement... terminé !


# Fonctions de base
####################

"""
On verra plus en détail les manipulations de strings au chap. 8. Voici déjà
les outils de base.
"""

#   1. On utilise la fonction intégrée `len()` pour afficher la longueur d'une
#      chaîne (c'est-à-dire son nombre de caractères)
print(len("Ceci est une chaîne"))  # => 19
print(len(""))  # => 0
print(len("é"))  # => 1 (un caractère accentué compte pour un seul caractère)


"""
    2. On utilise l'opérateur `+` pour lier des chaînes entre elles. Cette
       opération s'appelle une "concaténation".
"""
print("Hello " + "world!")  # => Hello world!
print("Hello" + "world!")   # => Helloworld! (attention aux espaces !)

# Attention, on ne peut concaténer que des strings.
try:
    "Hello " + 42  # => TypeError: can only concatenate str (not "int") to str
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")


#   3. On utilise l'opérateur `*` pour dupliquer une chaîne (string * int)
"Pouet" * 5  # => 'PouetPouetPouetPouetPouet'
print("-" * 20)  # => -------------------- (pratique pour tracer des lignes !)

# Attention, on ne peut dupliquer qu'avec des ints
try:
    "Pouet " * 3.2  # => TypeError: can't multiply sequence by non-int of type 'float'
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")


"""
Les outils suivants sont des "méthodes" : ce sont des fonctions "attachées" à
une valeur, que l'on appelle avec un point : `valeur.methode()`.

IMPT : comme les chaînes sont immuables, ces méthodes ne modifient JAMAIS la
chaîne d'origine : elles retournent une NOUVELLE chaîne.

    4. `.lower()` et `.upper()` servent à mettre en minuscules/majuscules, et
       `.capitalize()` met une majuscule au premier mot seulement.
"""
s = "Salut, Monde!"

print(s.lower())       # => salut, monde!
print(s.upper())       # => SALUT, MONDE!
print(s.capitalize())  # => Salut, monde!
print(s)               # => Salut, Monde! (s n'a pas été modifiée)


"""
    5. `.count(str)` compte les occurrences d'une chaîne dans une autre.
       Attention, les majuscules comptent.
"""
s = "Salut, salut, salut !"
print(s.count("salut"))  # => 2 (le premier "Salut" a une majuscule)
print(s.count("alut"))   # => 3


"""
    6. `.find(str)` retourne l'index (ou rang) de la première occurrence d'une
       chaîne dans une autre (et -1 si la chaîne n'existe pas).
"""
s = "Salut, Monde !"
print(s.find("Salut"))  # => 0
print(s.find("Monde"))  # => 7
print(s.find("monde"))  # => -1 (pas trouvé : les majuscules comptent)


"""
    7. `.replace(ancienne, nouvelle)` remplace toutes les occurrences d'une
       chaîne par une autre
"""
s = "Salut, Monde !"
print(s.replace("Monde", "Python"))  # => Salut, Python !


"""
    8. `.strip()` retire le whitespace (espaces, tabs, sauts de ligne…) en
       début et fin d'une chaîne. `.lstrip()` et `.rstrip()` les enlèvent à
       gauche et à droite respectivement.
"""
s = "   Salut, Monde !         "
print(s.strip())   # => Salut, Monde !
print(s.lstrip())  # => Salut, Monde !         (les espaces de droite restent)
print(s.rstrip())  # =>    Salut, Monde !


"""
  9. Enfin, on utilise la fonction intégrée `str()` pour convertir une valeur
     en string (cf. chap. 6), ce qui permet ensuite de la concaténer.
"""
print("Hello " + str(42))             # => Hello 42
print("This is " + str(False))        # => This is False
print("I like brackets: " + str([]))  # => I like brackets: []
