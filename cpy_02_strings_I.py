################################################################################
#                                                                              #
#  NNNN    NNN    SSSSSS.   IIIII   (inspiré de https://learnxinyminutes.com)  #
#  NNNNN   NNN  SSSS  SSSS   III                                               #
#  NNNNNN  NNN  SSSS         III    Licence : CC BY-SA 4.0 FR                  #
#  NNNNNNN NNN   SSSSSS      III    Félix Déage - MMXXI                        #
#  NNN NNNNNNN      SSSSS    III                                               #
#  NNN  NNNNNN        SSSS   III    Cours Python - 1ère - v.3.4                #
#  NNN   NNNNN  SSSS  SSSS   III                                               #
#  NNN    NNNN   SSSSSSSS   IIIII                                              #
#                                                                              #
################################################################################
#               #                                                              #
#  Part. II     #  chaînes de caractères I                                     #
#               #                                                              #
################################################################################

####################################################
# 7. Chaînes de caractère : les bases              #
####################################################
#
#  - Déclarer des chaînes de caractères
#  - Accéder à un caractère
#  - HP : caractères spéciaux et échappement
#  - Imprimer avec print()
#  - Opérations de base
#
####################################################

# Déclarer des chaînes de caractères (ou strings)
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
# Inversement, si on utilise des simples quotes ('   '), on pourra y insérer
# des doubles quotes
'Je lui ai dit : "Fonce, Michel !"'

"""
Depuis Python 3, on peut utiliser tous les caractères Unicode dans une string :
accents, diacritiques, emojis, alphabets non-latins, etc.
"""
s = "¡¢£¤¥¦§ àêïœú ÇßÐÞðƓ 中野区 💅😭💉📧🚭🥺 ᠮᠣᠩᠭᠣᠯᠴᠤᠳ ‽̃ͦ"

"""
HP : si on a besoin d'insérer des doubles quotes DANS des doubles quotes, ou
l'inverse, il faudra ÉCHAPPER ces quotes avec le caractère "backslash" : \
"""
'J\'aime l\'aligot d\'Émile'
"Je lui ai dit : \"Fonce, Michel !\""

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
# …
s4[15]  # => 'a'
s4[16]  # => 'î'
s4[17]  # => 'n'
s4[18]  # => 'e'

# IMPT : l'indexation commence toujours, toujours à 0 en Python !

# Cependant,  on ne peut pas modifier une chaîne déjà créée
try:
    s4[2] = "u"  # => TypeError: 'str' object does not support item assignment
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# HP : Caractères spéciaux et échappement
##########################################

"""
Dans une chaîne de caractères, on peut rencontrer des caractères qui ont un sens
différent de leur rendu visuel dans le code.
"""

# Exemple :
s5 = "abc\ndef\nghi"  # => Ce "\n" est en fait un saut de ligne sur Linux/Mac
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


# Ce \ est appelé un caractère d'échappement : il transforme la signification du
# caractère qui le suit immédiatement.

# Quand on souhaite vraiment avoir un backslash à l'écran, il faut "échapper" ce
# caractère avec… un autre backslash
print("\\")  # => "\"

# Imprimer avec print()
########################

# Python a une fonction intégrée print() pour imprimer du texte à l'écran
print("Salut, monde !") # => "Salut, monde !"

# …mais print() peut imprimer absolument tout et n'importe quoi : entiers,
# floats, strings, listes, booléens, range…

print([True, "pouet", 150, 2.3, range(4), [1]])  # => [True, 'pouet', 150, 2.3,
#                                                       range(0, 4), [1]]

"""
Note : dans l'interpréteur Python, si la dernière valeur retournée n'est pas
affectée dans une variable, alors Python l'imprimera même si on n'a pas appelé
print().

Ceci ne fonctionne pas si on lance un programme depuis son shell (mode 2) avec
?> python fichier.py

"""
"Tut tut"             # => 'Tut tut'
variable = "Tut tut"  # => (pas d'impression)

# On se servira souvent de print() pour afficher le résultat d'un calcul.
# (cf. le chap. 14 sur les fonctions)
def ma_super_fonction(a, b):
    print("Du texte")
    return a + b

# Appeler la fonction imprimera la valeur du print(), puis la valeur
# retournée par la fonction
ma_super_fonction(2, 3)
# => "Du texte"
# => 5

"""
IMPT : print() rajoute par défaut un saut de ligne à la fin de chaque
impression. Les sauts de ligne se notent "\n".

Pour empêcher ce fonctionnement, il faut passer en paramètre la chaîne vide
"""
print("toto", end='')  # => pas de saut en fin de ligne

# Opérations de base
#####################

#   1. On utilise l'opérateur "+" pour lier des chaînes entre elles
"Hello " + "world!"  # => "Hello world!"
# IMPT : cette opération s'appelle une "concaténation"

# Attention, on ne peut concaténer que des strings
try:
    "Hello " + 42  # => TypeError: can only concatenate str (not "int") to str
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


#   2. On utilise l'opérateur "*" pour dupliquer une chaîne (string * int)
"Pouet" * 5  # => 'PouetPouetPouetPouetPouet'


#   3. On utilise la fonction intégrée len() pour afficher la longueur d'une
#      chaîne
len("Ceci est une chaîne")  # => 19
len("")  # => 0


#   4. On utilise la fonction intégrée str() pour convertir une valeur en string
"Hello " + str(42)             # => "Hello 42"
"This is " + str(False)        # => "This is False"
"I like brackets: " + str([])  # => "I like brackets: []"
