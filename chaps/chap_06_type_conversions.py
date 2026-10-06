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
#  Chap. 6      #  Conversions : types, binaire, décimal et hexadécimal        #
#               #                                                              #
################################################################################
#
#  - La fonction intégrée `type()`
#  - Conversions entre types : int(), float(), str()
#  - Arrondir un nombre : round()
#  - Les bases de numération
#  - Conversions vers le décimal
#  - Conversions depuis le décimal
#  - Conversions depuis une base arbitraire
#
############################################

# La fonction intégrée `type()`
################################

# On peut utiliser la fonction intégrée `type()` pour déterminer le type d'une
# valeur
print(type(3))    # => <class 'int'>
print(type(3.0))  # => <class 'float'>
print(type("3"))  # => <class 'str'> (cf. les chaînes de caractères, chap. 7)

# 3 et 3.0 expriment différemment le même nombre
print(3 == 3.0)     # => True
print(3 == 3.0001)  # => False

"""
IMPT : ce signe `==` sert à tester une égalité. La ligne entière s'appelle une
"expression booléenne" : c'est un type particulier de calcul que Python va
transformer (évaluer) en "Oui" ou "Non", "Vrai" ou "Faux" (en Python : True ou
False, cf. chap. 9).

Pour tester si une variable est d'un certain type, on peut faire :
type(variable) == <le type testé>

Les principaux types sont :
-  types simples : bool, int, float
-  types construits : str, tuple, list, dict

(Nous les verrons plus en détail au chap. 10)
"""
print(type("3") == str)    # => True
print(type(3) == str)      # => False
print(type(3) == int)      # => True
print(type(True) == bool)  # => True

"""
Note : même si 3 == 3.0, leurs types sont différents. L'égalité "==" compare
les VALEURS, pas les types :
"""
print(type(3) == type(3.0))  # => False


# Conversions entre types : int(), float(), str()
##################################################

"""
Chaque type de base possède une fonction intégrée du même nom, qui permet de
convertir une valeur vers ce type :
    - int()   convertit vers un entier,
    - float() convertit vers un flottant,
    - str()   convertit vers une chaîne de caractères (cf. chap. 7).

Ces conversions sont fondamentales : on s'en servira en permanence, par
exemple pour transformer en nombre ce qu'un utilisateur a tapé au clavier
(cf. chap. 11).
"""

#   1. float() transforme un entier en flottant : la valeur ne change pas, seul
#      le type change
print(float(7))         # => 7.0
print(type(float(7)))   # => <class 'float'>

#   2. int() transforme un flottant en entier en SUPPRIMANT la partie
#      décimale. On dit qu'il "tronque" le nombre : il n'arrondit pas !
print(int(3.2))    # => 3
print(int(3.99))   # => 3 (et non 4 !)
print(int(-3.99))  # => -3 (la troncature se fait "vers 0")

"""
IMPT : int() ne fait pas un arrondi, il "coupe" tout ce qui est après la
virgule. Pour arrondir, on utilisera round() (voir la section suivante).

Remarquez la différence avec la division entière "//" (cf. chap. 4), qui
arrondit toujours vers le bas, même pour les nombres négatifs :
"""
print(int(-7 / 2))  # => -3 (on tronque -3.5 vers 0)
print(-7 // 2)      # => -4 (on arrondit -3.5 vers le bas)

#   3. int() et float() savent aussi convertir des chaînes de caractères, à
#      condition que la chaîne représente bien un nombre
print(int("42"))       # => 42
print(float("3.5"))    # => 3.5
print(float("42"))     # => 42.0
print(float("1e3"))    # => 1000.0 (la notation scientifique est acceptée)

# Les espaces (et sauts de ligne) autour du nombre sont tolérés :
print(int("   42  "))  # => 42

"""
Mais si la chaîne ne représente pas un nombre valide, Python ne peut pas
"deviner" ce que vous vouliez dire et soulève une erreur (une "ValueError",
c'est-à-dire une erreur de valeur) :
"""
try:
    int("3.5")  # => ValueError: invalid literal for int() with base 10: '3.5'
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    float("abc")  # => ValueError: could not convert string to float: 'abc'
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    float("3,5")  # => ValueError : la virgule n'est pas un séparateur décimal
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
IMPT : en Python (comme dans presque tous les langages), le séparateur décimal
est le POINT, jamais la virgule.

Astuce : pour convertir "3.5" en entier, on peut passer par un flottant :
"""
print(int(float("3.5")))  # => 3

#   4. str() transforme n'importe quelle valeur en chaîne de caractères
print(str(42))    # => 42 (mais c'est maintenant le texte "42", pas le nombre)
print(str(3.0))   # => 3.0
print(type(str(42)))  # => <class 'str'>

"""
Attention : "42" (une chaîne) et 42 (un entier) sont deux valeurs différentes,
même si print() les affiche de la même façon !
"""
print("42" == 42)       # => False
print(int("42") == 42)  # => True


# Arrondir un nombre : round()
###############################

# La fonction intégrée round() arrondit un nombre à l'entier le plus proche…
print(round(3.2))   # => 3
print(round(3.7))   # => 4
print(round(-3.7))  # => -4

# … ou au nombre de décimales passé en 2e paramètre
print(round(3.14159, 2))  # => 3.14
print(round(3.14159, 4))  # => 3.1416

"""
Curiosité : quand un nombre est exactement "au milieu" (comme 2.5), Python
arrondit vers le nombre PAIR le plus proche. C'est l'"arrondi bancaire", qui
évite de toujours arrondir vers le haut (et donc de fausser les sommes de
nombreux arrondis).
"""
print(round(2.5))  # => 2 (et non 3 !)
print(round(3.5))  # => 4


# Les bases de numération
##########################

"""
Nous écrivons les nombres en base 10 (le "décimal") : on utilise 10 chiffres
(0 à 9), et la position de chaque chiffre indique une puissance de 10.

Ainsi, 2024 signifie :
    2 * 1000 + 0 * 100 + 2 * 10 + 4 * 1
soit
    2 * 10**3 + 0 * 10**2 + 2 * 10**1 + 4 * 10**0

On peut faire exactement la même chose avec n'importe quelle base :
    - en base 2 (le "binaire"), on n'a que deux chiffres : 0 et 1. Chaque
      position est une puissance de 2. C'est la base utilisée par les
      ordinateurs, dont la mémoire ne stocke que des 0 et des 1 (les "bits").
    - en base 16 (l'"hexadécimal"), on a 16 chiffres : 0 à 9, puis A (10),
      B (11), C (12), D (13), E (14) et F (15). C'est très utilisé en
      informatique car un chiffre hexadécimal correspond exactement à 4 bits.
      Vous en avez sûrement déjà vu dans les codes couleur du Web (#FF0000
      pour le rouge).
    - en base 8 (l'"octal"), on a 8 chiffres : 0 à 7. C'est plus rare, mais on
      le rencontre par exemple pour les permissions de fichiers sous Linux.

Exemple : le nombre binaire 1101 vaut
    1 * 2**3 + 1 * 2**2 + 0 * 2**1 + 1 * 2**0 = 8 + 4 + 0 + 1 = 13
"""
print(1 * 2**3 + 1 * 2**2 + 0 * 2**1 + 1 * 2**0)  # => 13

# Et le nombre hexadécimal 2F vaut 2 * 16 + 15 :
print(2 * 16 + 15)  # => 47


# Conversions vers le décimal
##############################

# Python s'exprime nativement en décimal (base 10), comme vous et moi
# (et comme presque tous les langages de programmation existants).
print(10)  # => 10. Ce 10 est décimal, comme vos 10 doigts

# On peut aussi écrire un nombre en binaire avec le préfixe `0b`…
0b01001101
# …et Python fera automatiquement la conversion en base 10
print(0b01001101)  # => 77
print(0b1101)      # => 13 (cf. le calcul de la section précédente)

# De même, on peut écrire de l'hexadécimal avec le préfixe "0x"
print(0xA0)  # => 160 (base 10)
print(0x2F)  # => 47
print(0xDF40E)  # => 914446
print(0xdf40e)  # => 914446 (les majuscules n'ont pas d'importance)

# Et de l'octal avec le préfixe "0o" (zéro, puis la lettre o)
print(0o17)  # => 15 (1 * 8 + 7)

"""
On n'a donc pas besoin de fonctions pour aller vers la base 10 : il suffit
d'utiliser les écritures `0b...`, `0x...` et `0o...` et de laisser
l'interpréteur faire la conversion.

Note : il s'agit juste d'une autre façon d'ÉCRIRE un entier. Le résultat est
un int tout à fait normal, avec lequel on peut calculer :
"""
print(type(0xA0))      # => <class 'int'>
print(0b1101 + 0x2F)   # => 60 (13 + 47)


# Conversions depuis le décimal
################################

# En sens inverse, on peut convertir du décimal en binaire avec la
# fonction intégrée `bin()`
print(bin(14))  # => 0b1110

# bin() retourne une string, même si print() n'affiche pas les guillemets.
# On le confirme en utilisant type() :
print(type(bin(3)))  # => <class 'str'>

# On peut convertir directement de l'hexa vers du binaire
print(bin(0xA4F2))  # => 0b1010010011110010

# Pour convertir en hexadécimal, on utilise la fonction `hex()`
print(hex(35))   # => 0x23
print(hex(255))  # => 0xff
# Notez que `hex()` retourne aussi une string :
print(type(hex(3)))  # => <class 'str'>

# Enfin, `oct()` convertit en octal
print(oct(8))  # => 0o10

"""
Ces fonctions évitent de faire à la main des conversions entre bases.

Attention, on ne peut pas combiner ces deux fonctions, car `hex()` et `bin()`
n'acceptent que des `int` en paramètre :
"""
try:
    print(hex(bin(5)))  # => TypeError: 'str' object cannot be interpreted as
    #                                    an integer
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# Elles n'acceptent pas non plus les floats :
try:
    print(bin(3.5))  # => TypeError: 'float' object cannot be interpreted as
    #                                 an integer
except TypeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Bonus : la fonction intégrée format() permet d'obtenir la représentation sans
le préfixe ("b" pour binaire, "x" pour hexadécimal, "o" pour octal). On peut
même imposer un nombre de chiffres en complétant par des zéros à gauche :
"""
print(format(14, "b"))    # => 1110
print(format(255, "x"))   # => ff
print(format(5, "08b"))   # => 00000101 (8 chiffres, complétés par des 0)


# Conversions depuis une base arbitraire
#########################################

"""
Pour convertir en base 10 une string représentant un nombre depuis une
base arbitraire, on utilise int(string, base).

C'est un besoin rare, car les principales bases utilisées sont les bases 2, 8,
10 et 16, pour lesquelles des préfixes existent déjà. Mais on ne sait
jamais !
"""
print(int("22", 3))      # => 8 (2 * 3 + 2)
print(int("221021", 5))  # => 7636
print(int("776", 8))     # => 510 (7 * 64 + 7 * 8 + 6)
print(int("7234", 10))   # => 7234, on retrouve le nombre de départ

"""
Vérifions le 2e exemple à la main, en base 5 (les puissances de 5 sont 1, 5,
25, 125, 625, 3125) :
    2 * 3125 + 2 * 625 + 1 * 125 + 0 * 25 + 2 * 5 + 1 * 1 = 7636
"""
print(2 * 5**5 + 2 * 5**4 + 1 * 5**3 + 0 * 5**2 + 2 * 5**1 + 1 * 5**0)
# => 7636

# C'est aussi très pratique pour convertir une string binaire ou hexadécimale
# (par exemple saisie par un utilisateur) :
print(int("1110", 2))   # => 14
print(int("ff", 16))    # => 255
print(int("0x1F", 16))  # => 31 (le préfixe est toléré)

"""
La base peut aller de 2 à 36 : au-delà de 9, on utilise les 26 lettres de
l'alphabet comme chiffres (a = 10, b = 11, …, z = 35).
"""
print(int("z", 36))  # => 35

# Évidemment, les chiffres doivent exister dans la base choisie :
try:
    int("2", 2)  # => ValueError: invalid literal for int() with base 2: '2'
except ValueError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
