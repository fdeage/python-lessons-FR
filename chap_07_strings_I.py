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

print(s1)  # => "Ceci est une chaîne."
print(s2)  # => 'Et ceci est une chaîne aussi.'
print(s3)  # => ""

# Si on utilise des doubles quotes ("…"), on pourra y insérer des
# simples quotes
"J'aime l'aligot d'Émile"
# Inversement, si on utilise des simples quotes ('  '), on pourra y insérer
# des doubles quotes
'Je lui ai dit : "Fonce, Michel !"'

"""
Si on a besoin d'insérer des doubles quotes DANS des doubles quotes, ou
l'inverse, il faudra ÉCHAPPER ces quotes avec le caractère "backslash" : \
"""
'J\'aime l\'aligot d\'Émile'
"Je lui ai dit : \"Fonce, Michel !\""

"""
Depuis Python 3, on peut utiliser tous les caractères Unicode dans une string :
accents, diacritiques, emojis, alphabets non-latins, etc.
"""
weird_string = "¡¢£¤¥¦§ àêïœú ÇßÐÞðƓ 中野区 💅😭💉📧🚭🥺 ᠮᠣᠩᠭᠣᠯᠴᠤᠳ ‽̃ͦ"
print(weird_string)


# Accéder à un caractère
#########################

# Une string est une séquence de caractères, similaire à une liste (cf. le
# chap. 16 sur les listes)
s4 = "Ceci est une chaîne"

# On peut accéder à chaque valeur de la liste avec la syntaxe "[…]"
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

# Très important :l'indexation commence toujours, toujours à 0 en Python !
# (comme dans la quasi-totalité des langages)

# On peut accéder à une lettre mais pas la modifier une fois la chaîne créée :
try:
    s4[2] = "u"  # => TypeError: 'str' object does not support item assignment
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Caractères spéciaux et échappement
#####################################

"""
Dans une chaîne de caractères, on peut rencontrer des caractères qui ont un sens
différent de leur rendu visuel dans le code.
"""

# Exemple :
s5 = "abc\ndef\nghi"  # => Ce "\n" encode un saut de ligne (sur Linux/Mac)
print(s5)             # => … que l'on peut voir en imprimant la variable s5
"""
Résultat

abc
def
ghi
"""

"""
Ces caractères spéciaux utilisent souvent le caractère backslash : \
\r    => saut de ligne (imprimante)
\r\n  => saut de ligne (Windows)
\t    => tabulation
"""
print("Colonne 1\tColonne 2\nValeur 1\tValeur 2") # => Intercale des tabulations


"""
Ce `\` est appelé un caractère d'échappement : il change la signification du
caractère qui le suit.

Quand on souhaite vraiment avoir un backslash à l'écran, il faut "échapper" ce
caractère avec… un autre backslash
"""
print("\\")  # => "\"


# Imprimer avec `print()`
##########################

# Python propose la fonction intégrée `print()` pour imprimer du texte à l'écran
print("Salut, monde !") # => "Salut, monde !"

# `print()` peut imprimer absolument n'importe quoi : entiers, floats, strings,
# listes, booléens, range…

print([True, "pouet", 150, 2.3, range(4), [1]])  # => [True, 'pouet', 150, 2.3,
#                                                       range(0, 4), [1]]

"""
Note : dans l'interpréteur Python, si la dernière valeur retournée n'est pas
affectée dans une variable, alors Python l'imprimera même si on n'a pas appelé
print().

Ceci ne fonctionne pas si on lance un programme depuis son shell (mode 2) avec
`?> python fichier.py`

"""
"Tut tut"             # => 'Tut tut'
variable = "Tut tut"  # => (pas d'impression)

# On se servira souvent de `print()` pour afficher le résultat d'un calcul
# (cf. le chap. 14 sur les fonctions).
def ma_super_fonction(a, b):
    print("Du texte")
    return a + b

# Appeler la fonction imprimera la valeur du `print()`, puis la valeur
# retournée par la fonction
ma_super_fonction(2, 3)
# => "Du texte"
# => 5

"""
IMPT : `print()` rajoute par défaut un saut de ligne à la fin de chaque
impression. Les sauts de ligne se notent `\n`.

Pour empêcher ce fonctionnement, il faut utiliser end='' :
"""
print("test1", end='')
print("test2", end='')
print("test3")
# => imprime 'test1test2test3'

# Fonctions de base
####################

#   1. On utilise la fonction intégrée `len()` pour afficher la longueur d'une
#      chaîne
print(len("Ceci est une chaîne"))  # => 19
print(len(""))  # => 0


"""
    2. On utilise l'opérateur `+` pour lier des chaînes entre elles. Cette
       opération s'appelle une "concaténation".
"""
print("Hello " + "world!")  # => "Hello world!"

# Attention, on ne peut concaténer que des strings.
try:
    "Hello " + 42  # => TypeError: can only concatenate str (not "int") to str
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


#   3. On utilise l'opérateur `*` pour dupliquer une chaîne (string * int)
"Pouet" * 5  # => 'PouetPouetPouetPouetPouet'

# Attention, on ne peut dupliquer qu'avec des ints
try:
    "Pouet " * 3.2  # => TypeError: can't multiply sequence by non-int of type 'float'
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")


"""
    4. `.lower()` et `.upper()` servent à mettre en majuscules/minuscules, et
       `.capitalize()` met une majuscule au premier mot seulement.
"""
s = "Salut, Monde!"

print(s.lower())       # => salut, monde!
print(s.upper())       # => SALUT, MONDE!
print(s.capitalize())  # => Salut, monde!


"""
    5. `.count(str)` compte les occurrences d'une chaîne dans une autre.
       Attention, les majuscules comptent.
"""
s = "Salut, salut, salut !"
print(s.count("salut"))  # => 2
print(s.count("alut"))   # => 7


"""
    6. `.find(str)` retourne l'index (ou rang) de la première occurrence d'une
       chaîne dans une autre (et -1 si la chaîne n'existe pas).
"""
s = "Salut, Monde !"
print(s.find("Salut"))  # => 0
print(s.find("Monde"))  # => 0


"""
    7. `.replace(str)` remplace une chaîne par une autre
       chaîne dans une autre (et -1 si la chaîne n'existe pas).
"""
s = "Salut, Monde !"
print(s.replace("Monde", "Python"))


"""
    8. `.strip()` retire le whitespace (espaces, tabs...) en début et fin de
       ligne d'une chaîne. `.lstrip()` et `.rstrip()` les enlèvent à gauche et à
       droite respectivement.
"""
s = "   Salut, Monde !         "
print(s.strip())  # => 'Salut, Monde !'
print(s.lstrip())  # => 'Salut, Monde !         '
print(s.rstrip())  # => '   Salut, Monde !'


"""
  9. Enfin, on utilise la fonction intégrée `str()` pour convertir une valeur
     en string.
"""
print("Hello " + str(42))             # => "Hello 42"
print("This is " + str(False))        # => "This is False"
print("I like brackets: " + str([]))  # => "I like brackets: []"
