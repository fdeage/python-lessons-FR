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
#  Chap. 12     #  if, then, else et elif : corrigés                           #
#               #                                                              #
################################################################################

##############
#  FizzBuzz  #
##############

"""
0. écrire du code qui affiche si un nombre est pair, et sinon ne fait rien.
"""
n = 7
if n % 2 == 0:
    print(n, " est pair")

"""
1. écrire du code qui teste si un nombre est un multiple de 3 ou de 5, et affiche le texte correspondant.
"""
n = 7
if n % 3 == 0:
    print(n, " est multiple de 3")
elif n % 5 == 0:
    print(n, " est multiple de 5")
else:
    print(n, " n'est multiple ni de 3 ni de 5")


"""
2. écrire du code qui teste si un nombre est un multiple de 3, de 5 ou de 15.
Pour le texte affiché :
  - au lieu de "est multiple de 3", on affiche "Fizz"
  - au lieu de "est multiple de 5", on affiche "Buzz"
  - au lieu de "est multiple de 15", on affiche "FizzBuzz"

De combien de conditions avez-vous besoin ?
"""

# On peut fonctionner avec une seule condition :
n = 7
if n % 15 == 0:
    # L"ordre est capital ! Sinon on passe dans la condition 3 ou 5
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    # Cette ligne ne change pas, pourquoi ?
    print(n, " n'est multiple ni de 3 ni de 5")

# Alternative beaucoup moins élégante, avec deux "if" imbriqués :
n = 7
if n % 3 == 0:
    # Si n est multiple de 3, il peut AUSSI être multiple de 15
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif n % 5 == 0:
    # Si n est multiple de 5, il peut AUSSI être multiple de 15
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        print("Buzz")
else:
    print(n, " n'est multiple ni de 3 ni de 5")


"""
3. Écrire du code qui, pour tous les entiers de 1 à 100, affiche :
    - Fizz si le nombre est multiple de 3,
    - Buzz si le nombre est multiple de 5,
    - FizzBuzz si le nombre est multiple de 15,
    - le nombre lui-même dans les autres cas.
"""

# Notez que range(...) prend deux paramètres, sinon il commencera à 0
for i in range(1, 100):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


"""
4. écrire du code qui calcule la somme des nombres inférieurs ou égaux à 100 qui
sont multiples de 3, 5 ou 15.
"""
s = 0
for i in range(1, 100):
    # Dans les deux cas, on ajoutera le nombre au total : plus besoin de différencier !
    if i % 3 == 0 or i % 5 == 0:
        s += i
    # pas de clause else, car on ne fait rien s'il n'est pas multiple

print(s)  # => 2318
