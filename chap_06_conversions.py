################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2023                    #
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
#  - Conversions vers le décimal
#  - Conversions depuis le décimal
#
########################################################

# Conversions vers le décimal
##############################

# Python s'exprime nativement en décimal (base 10), comme vous et moi
# (et comme presque tous les langages de programmation existants).
print(10)  # => 10. Ce 10 est décimal, comme vos 10 doigts

# On peut aussi écrire un nombre en binaire avec le préfixe "0b"…
0b01001101
# …et Python fera automatiquement la conversion en base 10
print(0b01001101)  # => 77

# De même, on peut écrire de l'hexadécimal avec le préfixe "0x"
print(0xA0)  # => 160 (base 10)
print(0xDF40E)  # => 914446
print(0xdf40e)  # => 914446 (les majuscules n'ont pas d'importance)


# Conversions depuis le décimal
################################

# En sens inverse, on peut convertir du décimal en binaire avec la
# fonction intégrée bin()
print(bin(14))  # => '0b1110'.

# Notez les guillemets : Python retourne une string ! On le confirme en
# utilisant type()
print(type(bin(3)))  # => <class 'str'>

# On peut convertir directement de l'hexa vers du binaire
print(bin(0xA4F2))  # => '0b1010010011110010'

# Pour convertir en hexadécimal, on utilise hex()
print(hex(35))  # = '0x23'
# hex() retourne aussi une string :
print(type(hex(3)))  # => <class 'str'>

# Ces fonctions évitent de faire à la main des conversions entre bases.

# Attention, on ne peut pas combiner ces deux fonctions, car hex() et bin()
# n'acceptent que des int en paramètre
try:
    print(hex(bin(5)))  # => TypeError: 'str' object cannot be interpreted as an
    integer
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# Pour convertir en base 10 une string représentant un nombre depuis une
# base arbitraire, on utilise int(string, base)
print(int("22", 3))  # 8 en base 10
print(int("221021", 5))  # 7636 en base 10
print(int("776", 8))  # 510 en base 10
print(int("7234", 10))  # 7234, on retrouve le nombre de départ
