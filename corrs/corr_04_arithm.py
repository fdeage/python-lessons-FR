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
#  Chap. 4      #  Arithmétique : corrigés                                     #
#               #                                                              #
################################################################################

################################
#  Calculs simples             #
################################

# 1. Somme de deux entiers positifs :
print(12 + 30)  # => 42

# 2. Moyenne de trois entiers : on additionne, PUIS on divise. Les parenthèses
# sont indispensables (cf. chap. 5 : la division passe avant l'addition).
print((12 + 15 + 18) / 3)  # => 15.0
print(12 + 15 + 18 / 3)    # => 33.0 (faux : seul 18 est divisé par 3 !)
# Note : le résultat est un float, car "/" retourne toujours un float.

# 3. Somme des entiers de 1 à 5 :
print(1 + 2 + 3 + 4 + 5)  # => 15
# (Avec les boucles du chap. 13, on saura le faire pour 1 à 1000 sans tout
# écrire.)

# 4. Différence de deux décimaux :
print(10.5 - 2.25)  # => 8.25
print(1.1 - 1.0)    # => 0.10000000000000009 (les floats sont des valeurs
#                      approchées : cf. exercice 17)

# 5. Produit d'un nombre immense et d'un décimal :
print(123_456_789_123_456_789 * 0.5)  # => 6.172839456172839e+16
"""
Le résultat est un float (on multiplie par un float) : Python l'affiche en
notation scientifique, car il est très grand. Il a aussi perdu de la
précision : un float ne garde qu'environ 16 chiffres significatifs.
"""

# 6. Conversion de 212 °F en °C : C = (F - 32) * 5/9
print((212 - 32) * 5 / 9)  # => 100.0 (l'eau bout à 100 °C, soit 212 °F)
print((32 - 32) * 5 / 9)   # => 0.0 (et gèle à 0 °C, soit 32 °F)

# 7. 2 à la puissance 16 moins 4 à la puissance 3 :
print(2 ** 16 - 4 ** 3)  # => 65472 (65536 - 64)
# La puissance est calculée avant la soustraction : pas besoin de parenthèses.

# 8. Distance Terre-Soleil en notation scientifique :
print(1.5e8)  # => 150000000.0 (1,5 × 10^8 km)
# Remarque : la notation scientifique retourne toujours un float.

# 9. Division entière de 15 par 2, et son type :
print(15 // 2)        # => 7
print(type(15 // 2))  # => <class 'int'> (type() sera détaillé au chap. 6)

# 10. Type du produit de 5.0 par 14 :
print(type(5.0 * 14))  # => <class 'float'> (un seul float suffit pour que
#                         le résultat soit un float)

# 11. Valeurs absolues dans le même print() :
print(abs(4.3), abs(-14.8), abs(4.3 - 14.8))  # => 4.3 14.8 10.5
# Note : print() accepte plusieurs valeurs séparées par des virgules, et les
# affiche séparées par une espace.

# 12. Valeur absolue d'un entier négatif :
print(abs(-42))  # => 42

# 13. Pair ou impair : le reste de la division par 2 vaut 0 pour un nombre
# pair, 1 pour un nombre impair.
print(14 % 2)  # => 0 (14 est pair)
print(15 % 2)  # => 1 (15 est impair)
# (Pour afficher "pair" ou "impair", il faudra un "if" : cf. chap. 12.)

# 14. 135 minutes en heures et minutes :
print(135 // 60, "h", 135 % 60, "min")  # => 2 h 15 min
# La division entière donne le nombre d'heures COMPLÈTES, le modulo donne les
# minutes restantes.


################################
#  Ints et floats              #
################################

"""
15. Types :
        42 => int       42.0 => float     -3 => int
        .5 => float     4e2 => float (la notation scientifique donne un float)
        1_000_000 => int (les underscores ne changent rien au type)
"""
print(type(42), type(42.0), type(-3))
# => <class 'int'> <class 'float'> <class 'int'>
print(type(.5), type(4e2), type(1_000_000))
# => <class 'float'> <class 'float'> <class 'int'>

# 16. Un milliard, de deux façons :
print(1_000_000_000)  # => 1000000000 (un int)
print(1e9)            # => 1000000000.0 (un float)
# Même valeur, mais pas le même type !

# 17. 0.1 + 0.2 ne vaut pas exactement 0.3 :
print(0.1 + 0.2)         # => 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # => False
# On compare plutôt des valeurs arrondies :
print(round(0.1 + 0.2, 2) == 0.3)  # => True
# (Le test d'égalité "==" sera détaillé au chap. 9.)

# 18. Les ints sont arbitrairement grands, pas les floats :
print(2 ** 1000)
# => 10715086071862673209484250490… (302 chiffres : on ne l'écrit pas en
#    entier ici !)
try:
    2.0 ** 10000  # le résultat dépasse la limite des floats (environ 1.8e308)
except OverflowError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
2 ** 1000 est un calcul entre ints : Python utilise autant de mémoire que
nécessaire. 2.0 ** 10000 est un calcul entre floats, limités à environ
1.8e308 : Python lève une erreur OverflowError ("débordement").
"""


################################
#  Division entière et modulo  #
################################

# 19. Divisions entières et modulos :
print(17 // 5)   # => 3
print(17 % 5)    # => 2 (17 = 3 × 5 + 2)
print(-17 // 5)  # => -4 (arrondi à l'entier INFÉRIEUR : -3.4 donne -4)
print(-17 % 5)   # => 3 (-17 = -4 × 5 + 3 : le reste a le signe du diviseur)
print(7.5 // 2)  # => 3.0 (avec un float, le résultat est un float)

# 20. Quotient et reste en une fois :
print(divmod(100, 7))  # => (14, 2) (100 = 14 × 7 + 2)

# 21. 1000 secondes en minutes et secondes :
print(1000 // 60, "min", 1000 % 60, "s")  # => 16 min 40 s

# 22. Chiffre des unités et deux derniers chiffres :
print(98765 % 10)   # => 5 (le reste de la division par 10)
print(98765 % 100)  # => 65 (le reste de la division par 100)
# Astuce : n // 10 "enlève" le dernier chiffre, n % 10 le "récupère".
print(98765 // 10)  # => 9876


################################
#  Division par zéro           #
################################

# 23. Les trois opérations lèvent une ZeroDivisionError :
try:
    1 / 0
except ZeroDivisionError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    1 // 0
except ZeroDivisionError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    1 % 0
except ZeroDivisionError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# (Le texte exact de l'erreur peut varier selon la version de Python.)

# 24. Avec des floats, c'est la même chose :
try:
    1.0 / 0.0
except ZeroDivisionError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
# Python ne retourne pas "inf" ici : diviser par zéro est toujours une erreur,
# que les nombres soient des ints ou des floats.


################################
#  Arrondis, min() et max()    #
################################

# 25. Arrondis :
print(round(4.6))   # => 5
print(round(-4.6))  # => -5
print(round(4.5))   # => 4 (!)
print(round(5.5))   # => 6
"""
Piège : quand un nombre est EXACTEMENT à mi-chemin entre deux entiers, round()
choisit l'entier PAIR (c'est l'"arrondi bancaire") : 4.5 donne 4, et 5.5
donne 6.
"""
print(round(3.14159, 3))     # => 3.142
print(round(1234.5678, -1))  # => 1230.0 (arrondi à la dizaine)

# 26. 2 / 3 arrondi à deux décimales :
print(round(2 / 3, 2))  # => 0.67

# 27. Le plus grand et le plus petit :
print(max(12, -4, 7.5, 0, 33, -4.5))  # => 33
print(min(12, -4, 7.5, 0, 33, -4.5))  # => -4.5
# min() et max() acceptent des ints et des floats mélangés.

# 28. Sacs de 35 kg dans une brouette de 80 kg maximum :
print(80 // 35)  # => 2 (on ne peut mettre que 2 sacs entiers)
print(80 % 35)   # => 10 (il reste 10 kg de libre : 80 - 2 × 35)
print(divmod(80, 35))  # => (2, 10) (les deux en une fois)
