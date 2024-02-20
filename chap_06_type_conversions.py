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
#  Chap. 6      #  Conversions : binaire, décimal et hexadécimal               #
#               #                                                              #
################################################################################
#
#  - La fonction intégrée `type()`
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
print(type("3"))  # => <class 'str'> (cf. les chaînes de caractères plus loin)

# 3 et 3.0 expriment différemment le même nombre
print(3 == 3.0)     # => True
print(3 == 3.0001)  # => False

"""
IMPT : ce signe `==` sert à tester une égalité. La ligne entière s'appelle une
"expression booléenne" : c'est un type particulier de calcul que Python va
transformer (évaluer) en "Oui" ou "Non", "Vrai" ou "Faux".

Pour tester si une variable est d'un certain type, on peut faire :
type(variable) == <le type testé>

Les principaux types sont :
-  types simples : bool, int, float
-  types construits : str, tuple, list, dict

(Nous les verrons plus en détail au chap. 10)
"""
print(type("3") == str)    # => True
print(type(3) == str)      # => False
print(type(True) == bool)  # => False


# Conversions vers le décimal
##############################

# Python s'exprime nativement en décimal (base 10), comme vous et moi
# (et comme presque tous les langages de programmation existants).
print(10)  # => 10. Ce 10 est décimal, comme vos 10 doigts

# On peut aussi écrire un nombre en binaire avec le préfixe `0b`…
0b01001101
# …et Python fera automatiquement la conversion en base 10
print(0b01001101)  # => 77

# De même, on peut écrire de l'hexadécimal avec le préfixe "0x"
print(0xA0)  # => 160 (base 10)
print(0xDF40E)  # => 914446
print(0xdf40e)  # => 914446 (les majuscules n'ont pas d'importance)

"""
On n'a donc pas besoin de fonctions pour aller vers la base 10 : il suffit
d'utiliser les écritures `0b...` et `0x...` et de laisser l'interpréteur
faire la conversion.
"""


# Conversions depuis le décimal
################################

# En sens inverse, on peut convertir du décimal en binaire avec la
# fonction intégrée `bin()`
print(bin(14))  # => '0b1110'.

# Notez les guillemets : Python retourne une string ! On le confirme en
# utilisant type()
print(type(bin(3)))  # => <class 'str'>

# On peut convertir directement de l'hexa vers du binaire
print(bin(0xA4F2))  # => '0b1010010011110010'

# Pour convertir en hexadécimal, on utilise la fonction `hex()`
print(hex(35))  # = '0x23'
# Notez que `hex()` retourne aussi une string :
print(type(hex(3)))  # => <class 'str'>

"""
Ces fonctions évitent de faire à la main des conversions entre bases.

Attention, on ne peut pas combiner ces deux fonctions, car `hex()` et `bin()`
n'acceptent que des `int` en paramètre :
"""
try:
    print(hex(bin(5)))  # => TypeError: 'str' object cannot be interpreted as an
    integer
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Conversions depuis une base arbitraire
#########################################

"""
Pour convertir en base 10 une string représentant un nombre depuis une
base arbitraire, on utilise int(string, base).

C'est un besoin rare, car les principales bases utilisées sont les bases 2, 8,
10 et 16, pour lesquels des fonctions intégrées existent déjà. Mais on ne sait
jamais !
"""
print(int("22", 3))  # 8 en base 10
print(int("221021", 5))  # 7636 en base 10
print(int("776", 8))  # 510 en base 10
print(int("7234", 10))  # 7234, on retrouve le nombre de départ
