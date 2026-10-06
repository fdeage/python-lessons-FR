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
#  Chap. 6      #  Conversions : corrigés                                      #
#               #                                                              #
################################################################################

###################################
#  La fonction intégrée `type()`  #
###################################

"""
1. Sans exécuter : qu'affichent ces lignes ?
"""
print(type(7))       # => <class 'int'>
print(type(7.0))     # => <class 'float'> (le ".0" suffit à faire un float)
print(type("7"))     # => <class 'str'> (des guillemets : c'est du texte)
print(type(7 / 7))   # => <class 'float'>
print(type(7 // 7))  # => <class 'int'>
print(type(True))    # => <class 'bool'>
"""
- La division "/" retourne TOUJOURS un float, même quand le résultat tombe
  juste (7 / 7 vaut 1.0, et non 1). C'est la division entière "//" qui
  retourne un int quand on lui donne deux int (cf. chap. 4).
- True n'est ni un nombre ni du texte : c'est un booléen (cf. chap. 9).
"""

"""
2. True ou False ?
"""
print(3 == 3.0)               # => True
print(type(3) == type(3.0))   # => False
print(type(2 + 3.0) == float)  # => True
print(type("3") == int)       # => False
"""
- 3 et 3.0 ont la même VALEUR (l'égalité "==" compare les valeurs)…
- … mais pas le même TYPE : int d'un côté, float de l'autre.
- Quand on mélange un int et un float dans un calcul, le résultat est un float
  (2 + 3.0 vaut 5.0).
- "3" est une chaîne, son type est str.
"""


#####################################################
#  Conversions entre types : int(), float(), str()  #
#####################################################

"""
3. Que valent ces expressions ?
"""
print(int(9.99))          # => 9
print(int(-9.99))         # => -9
print(float(4))           # => 4.0
print(int("12") + 1)      # => 13
print(float("2.5") * 2)   # => 5.0
print(str(12) == "12")    # => True
print("12" == 12)         # => False
"""
- int() TRONQUE : il supprime la partie décimale, sans arrondir. 9.99 donne 9
  (et pas 10) ; -9.99 donne -9 (la troncature se fait vers 0).
- int("12") convertit le texte "12" en nombre 12 : on peut alors calculer.
- str(12) donne le texte "12", égal à la chaîne "12".
- Mais le texte "12" n'est pas égal au nombre 12 : types différents.
"""

"""
4. Lesquelles provoquent une erreur ?
"""
try:
    int("12.5")  # => ValueError : int() n'accepte pas de partie décimale
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    float("12,5")  # => ValueError : la virgule n'est pas un séparateur décimal
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

print(int("  7 "))   # => 7 (les espaces autour sont tolérés)
print(float("1e2"))  # => 100.0 (la notation scientifique est acceptée)

try:
    int("douze")  # => ValueError : Python ne lit pas les nombres en lettres
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
Trois conversions échouent : "12.5" pour int(), "12,5" pour float() (il faut
un POINT), et "douze". Les deux autres fonctionnent.
"""

"""
5. "7.9" en entier, en une seule expression :
"""
print(int(float("7.9")))  # => 7
"""
int("7.9") échouerait (cf. exercice 4). On convertit donc d'abord en float
(7.9), puis en int : la partie décimale est supprimée, on obtient 7.
Python exécute les fonctions de l'intérieur vers l'extérieur : d'abord
float("7.9"), puis int() sur le résultat.
"""

"""
6. int(-7.5) et -7.5 // 1 :
"""
print(int(-7.5))   # => -7
print(-7.5 // 1)   # => -8.0
"""
- int() tronque "vers 0" : on enlève simplement la partie décimale, -7.5
  devient -7.
- La division entière "//" arrondit toujours vers le BAS (vers moins
  l'infini) : -7.5 devient -8. Et comme -7.5 est un float, le résultat est un
  float : -8.0.
Pour les nombres positifs, les deux donnent le même résultat ; c'est avec les
nombres négatifs qu'il faut être prudent.
"""


##################################
#  Arrondir un nombre : round()  #
##################################

"""
7. Que valent ces expressions ?
"""
print(round(4.6))         # => 5
print(round(4.4))         # => 4
print(round(-2.7))        # => -3
print(round(2.71828, 3))  # => 2.718
print(round(1.5))         # => 2
print(round(2.5))         # => 2
"""
- round() arrondit à l'entier le PLUS PROCHE : 4.6 donne 5, -2.7 donne -3.
- Avec un 2e paramètre, on garde ce nombre de décimales.
- Le piège : pour un nombre exactement "au milieu" (x.5), Python arrondit vers
  l'entier PAIR le plus proche (l'"arrondi bancaire") : 1.5 donne 2, mais 2.5
  donne aussi 2 !
"""

"""
8. Prix TTC de 19.99 € HT, arrondi au centime :
"""
print(19.99 * 1.2)            # => 23.987999999999996 (imprécision des floats)
print(round(19.99 * 1.2, 2))  # => 23.99
"""
Le calcul brut donne un nombre avec beaucoup de décimales, à cause de
l'imprécision des floats (cf. chap. 4). Arrondir à 2 décimales donne un prix
présentable : 23.99 €.
"""

"""
9. int(x) et round(x) :
"""
print(int(3.7), round(3.7))  # => 3 4 : différents
print(int(3.2), round(3.2))  # => 3 3 : identiques
"""
int() tronque, round() arrondit. Ils donnent donc le même résultat quand la
partie décimale est inférieure à 0.5 (3.2), et des résultats différents quand
elle est supérieure à 0.5 (3.7).
"""


#############################
#  Les bases de numération  #
#############################

"""
10. Le binaire 1011 :
        1 * 2**3 + 0 * 2**2 + 1 * 2**1 + 1 * 2**0
      =    8     +    0     +    2     +    1     = 11
"""
print(1 * 2**3 + 0 * 2**2 + 1 * 2**1 + 1 * 2**0)  # => 11
print(0b1011)                                     # => 11 (vérification)

"""
11. L'hexadécimal 1F :
        1 * 16**1 + 15 * 16**0 = 16 + 15 = 31
"""
print(1 * 16**1 + 15 * 16**0)  # => 31
print(0x1F)                    # => 31 (vérification)

"""
12. Chiffres de chaque base :
    - base 2 : 2 chiffres (0 et 1), le plus grand est 1 ;
    - base 8 : 8 chiffres (0 à 7), le plus grand est 7 ;
    - base 16 : 16 chiffres (0 à 9, puis A à F), le plus grand est F (15).
    Règle générale : en base b, on utilise b chiffres, de 0 à b - 1.
"""


#################################
#  Conversions vers le décimal  #
#################################

# 13. Le préfixe 0b indique du binaire : Python convertit tout seul.
print(0b110110)  # => 54
# À la main : 32 + 16 + 0 + 4 + 2 + 0 = 54

# 14. Le préfixe 0x indique de l'hexadécimal :
print(0x1A7)  # => 423
# À la main : 1 * 256 + 10 * 16 + 7 = 256 + 160 + 7 = 423

# 15. Le préfixe 0o indique de l'octal :
print(0o777)  # => 511
# À la main : 7 * 64 + 7 * 8 + 7 = 448 + 56 + 7 = 511

# 16. 0b1111 vaut 15 et 0x10 vaut 16 :
print(0b1111 + 0x10)        # => 31
print(type(0b1111 + 0x10))  # => <class 'int'>
"""
Les écritures 0b… et 0x… sont juste d'autres façons d'ÉCRIRE un entier : le
résultat est un int ordinaire, que Python affiche en décimal.
"""


###################################
#  Conversions depuis le décimal  #
###################################

# 17. bin() convertit un entier en binaire :
print(bin(45))  # => 0b101101
# À la main : 45 = 32 + 8 + 4 + 1, soit 101101

# 18. On peut passer directement un nombre écrit en hexadécimal à bin() :
print(bin(0xF3))  # => 0b11110011
# Astuce : chaque chiffre hexa donne 4 bits : F = 1111 et 3 = 0011

# 19. hex() convertit en hexadécimal :
print(hex(255))  # => 0xff (255 = 15 * 16 + 15, soit "ff")

# 20. De même, hex() accepte un nombre écrit en binaire :
print(hex(0b110101110))  # => 0x1ae
# Astuce : on découpe en paquets de 4 bits depuis la droite :
# 1 | 1010 | 1110, soit 1 | a | e

# 21. format() permet d'enlever le préfixe et d'imposer une largeur :
print(format(200, "b"))  # => 11001000
print(format(5, "08b"))  # => 00000101
"""
"08b" signifie : en binaire ("b"), sur 8 caractères ("8"), en complétant à
gauche par des zéros ("0").
"""

# 22. hex(bin(5)) :
try:
    hex(bin(5))  # => TypeError
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
bin(5) retourne la CHAÎNE "0b101", et non un nombre. Or hex() n'accepte que
des entiers (int) : on ne peut pas enchaîner ces deux fonctions.
"""


############################################
#  Conversions depuis une base arbitraire  #
############################################

"""
23. On utilise int(chaine, base). Le nombre est donné sous forme de CHAÎNE,
    puisqu'il n'existe pas de préfixe pour les bases 3 ou 5.
    a) à la main, en base 3 (les puissances de 3 sont 1, 3, 9, 27, 81, 243) :
       1 * 243 + 0 * 81 + 1 * 27 + 1 * 9 + 0 * 3 + 1 * 1 = 280
"""
print(int("101101", 3))  # => 280
print(int("21012", 3))   # => 194 (2 * 81 + 1 * 27 + 0 * 9 + 1 * 3 + 2)
print(int("1243", 5))    # => 198 (1 * 125 + 2 * 25 + 4 * 5 + 3)
print(int("ABCDEF", 16))  # => 11259375
# Pour la base 16, le préfixe fonctionne aussi : 0xABCDEF
print(0xABCDEF)  # => 11259375

# 24. Les composantes de la couleur #FF8000 :
print(int("FF", 16))  # => 255 (le rouge est au maximum)
print(int("80", 16))  # => 128 (le vert est à moitié)
print(int("00", 16))  # => 0 (pas de bleu)
"""
Chaque composante va de 00 (0) à FF (255) : un orange, c'est beaucoup de
rouge, un peu de vert, et pas de bleu.
"""

# 25. Le chiffre 2 n'existe pas en base 2 (seuls 0 et 1 existent) :
try:
    int("2", 2)  # => ValueError
except ValueError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

print(int("2", 3))  # => 2
"""
En base 3, les chiffres sont 0, 1 et 2 : "2" est un nombre valide, qui vaut
simplement 2.
"""
