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
#  Chap. 9      #  Booléens I : corrigés                                       #
#               #                                                              #
################################################################################

########################
#  Valeurs booléennes  #
########################

# 1. Le type des booléens, et le piège des guillemets :
print(type(True))      # => <class 'bool'>
print(type("True"))    # => <class 'str'>
print(True == "True")  # => False
"""
"True" entre guillemets n'est pas un booléen, c'est du TEXTE (une str). Le
booléen True et la chaîne "True" sont donc différents.
"""

# 2. La ligne "false" (sans majuscule) provoque une NameError :
print(True)     # => True
try:
    false  # => NameError
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
print("False")  # => False (c'est une chaîne, qui s'affiche sans guillemets)
"""
Les booléens sont sensibles à la casse : seuls True et False (avec une
majuscule) existent. Python lit "false" comme le nom d'une variable… qui
n'existe pas, d'où la NameError.
"""


##############################################################
#  Expressions booléennes : égalité, inégalité, comparaison  #
##############################################################

# 3. Égalités et comparaisons :
print(1 == 1)          # => True
print(2 == 1)          # => False
print(2 != 5)          # => True
print(6 < 9)           # => True
print(5 >= 5)          # => True (5 est bien supérieur OU ÉGAL à 5)
print(32 % 2 == 1)     # => False (32 % 2 vaut 0 : 32 est pair)
print(33 % 3 > 0)      # => False (33 % 3 vaut 0 : 33 est multiple de 3)
print(7 < 9 < 15)      # => True (les deux comparaisons sont vraies)
print(85 < 32 < 127)   # => False (85 < 32 est faux, cela suffit)
print("abc" == "abc")  # => True
print("abc" == "abd")  # => False
print("2" == "2")      # => True (deux chaînes identiques)
"""
Rappel : le modulo "%" est calculé AVANT la comparaison (cf. chap. 5). Ainsi,
32 % 2 == 1 se lit (32 % 2) == 1, soit 0 == 1.
"""

# 4. Types différents :
print(2 == "2")                       # => False
print(3 == 3.0)                       # => True
print(5 == 5.1)                       # => False
print(6 == False)                     # => False
print("2" == "2.0")                   # => False
print(3 + 0.000000000001 == 3)        # => False
print(3 + 0.00000000000000001 == 3)   # => True (!)
print(True != "True")                 # => True
print(True == 1)                      # => True (!)
print(True != 2)                      # => True
"""
- Un nombre et une chaîne ne sont jamais égaux : 2 == "2" vaut False.
- Un int et un float de même valeur sont égaux : 3 == 3.0.
- "2" et "2.0" sont deux textes différents (Python ne les lit pas comme des
  nombres).
- 3 + 0.00000000000000001 == 3 vaut True : ce nombre est si petit qu'il est
  "perdu" dans l'imprécision des floats (cf. chap. 4). En revanche,
  0.000000000001 est encore assez grand pour être pris en compte.
- Curiosité : True vaut 1 et False vaut 0 quand on les compare à des
  nombres. Mais True n'est égal ni à 2, ni à la chaîne "True".
"""

# 5. Comparaisons enchaînées :
print(0 <= 47 <= 100)  # => True
# C'est équivalent à : 0 <= 47 and 47 <= 100 (cf. "and" plus bas)

# 6. Un multiple de 4 a un reste nul dans la division par 4 :
print(2024 % 4 == 0)  # => True


##########################
#  Comparer des strings  #
##########################

# 7. Ordre "lexicographique" (comme dans un dictionnaire) :
print("abc" < "abd")        # => True ("c" vient avant "d")
print("chat" < "chats")     # => True (le plus court, s'il est le "début")
print("pomme" < "poire")    # => False ("m" vient après "i")
print("Zèbre" < "abeille")  # => True (!)
print("10" < "9")           # => True (!)
print(10 < 9)               # => False
"""
- Les caractères sont comparés un par un, en commençant par le premier.
- Les majuscules ont toutes un numéro Unicode plus petit que les minuscules :
  "Z" vient donc AVANT "a" (cf. ord() au chap. 8).
- Entre guillemets, "10" et "9" sont du texte : on compare "1" et "9", et "1"
  vient avant. Entre des NOMBRES, en revanche, 10 est bien plus grand que 9.
"""


#############################
#  Pièges des comparaisons  #
#############################

# 8. On ne peut pas ORDONNER un nombre et une chaîne…
try:
    1 < "1"  # => TypeError
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# … mais on peut toujours tester leur ÉGALITÉ :
print(1 == "1")  # => False
"""
« Est-ce que 1 est plus petit que le texte "1" ? » n'a pas de sens : Python
soulève une TypeError. En revanche, « 1 et "1" sont-ils égaux ? » a une
réponse simple : non.
"""

# 9. Comparer des floats :
print(0.1 + 0.2 == 0.3)                    # => False
print(abs((0.1 + 0.2) - 0.3) < 0.000001)  # => True
"""
0.1 + 0.2 vaut en réalité 0.30000000000000004 (cf. chap. 4). Pour comparer
deux floats calculés, on teste donc si leur écart (en valeur absolue, avec
abs()) est très petit, plutôt que d'utiliser "==".
"""


########################################
#  Opérateurs booléens : not, and, or  #
########################################

# 10. Comparaisons entre booléens :
print(True == True)    # => True
print(False == False)  # => True
print(False == True)   # => False
print(False != True)   # => True

# 11. not, and, or :
print(not True)                  # => False
print(not False)                 # => True
print(True and True)             # => True
print(False and False)           # => False
print(False or False)            # => False
print(True and not False)        # => True (not False vaut True)
print(False != (not False))      # => True (False != True)
print(False or True)             # => True
print(1 == 1 and 2 == 1)         # => False (la 2e condition est fausse)
print(not "test" == "test")      # => False
print(2 == 1 or 2 != 1)          # => True (la 2e condition est vraie)
"""
Dans not "test" == "test", la comparaison est évaluée AVANT le not : on
calcule d'abord "test" == "test" (True), puis not True (False).
"""

# 12. L'opérateur in :
print(1 in [1, 2, 3, 4])       # => True
print(1 in [2, 3, 4, 5])       # => False
print(2.0 in [1, 2, 3])        # => True (2.0 == 2)
print("n" in "anne")           # => True
print("test" == "testing")     # => False
print("test" in "testing")     # => True ("test" est un morceau de "testing")
print("testing" in "test")     # => False (l'inverse n'est pas vrai)
"""
- 2.0 in [1, 2, 3] vaut True : "in" teste l'égalité "==", et 2.0 == 2.
- Pour les chaînes, "in" teste si le texte de gauche est un MORCEAU du texte
  de droite. "==" teste l'égalité complète, ce qui est bien plus strict.
"""

# 13. Le "coupe-circuit" de and :
print(0 != 0 and 1 / 0 > 1)  # => False
"""
Pas d'erreur ! La 1re condition (0 != 0) est fausse : toute l'expression est
donc forcément fausse, et Python n'évalue même pas la 2e condition (où se
trouve la division par zéro).
"""


#############################
#  Combinaisons booléennes  #
#############################

# 14. Priorités : not, puis and, puis or :
print(True or False and False)    # => True
print((True or False) and False)  # => False
print(not True or True)           # => True
print(not (True or True))         # => False
"""
- True or False and False se lit True or (False and False), soit
  True or False : True.
- Avec des parenthèses, on calcule d'abord True or False (True), puis
  True and False : False.
- not True or True se lit (not True) or True, soit False or True : True.
- not (True or True) se lit not True : False.
"""

# 15. Avec des variables booléennes :
A = True
B = False
print(B or A)                         # => True
print(B and A)                        # => False
print(A and 1 == 1)                   # => True
print(B or 0 != 1)                    # => True
print(A or 1 == 2)                    # => True
print((A and B) or ((not B) and A))   # => True
"""
Détail du dernier exemple (avec A = True et B = False) :
    - (A and B)          => True and False => False
    - (not B)            => not False      => True
    - ((not B) and A)    => True and True  => True
    - False or True      => True
"""

"""
16. Les 4 combinaisons de (A and B) or ((not B) and A) :

        A      | B      | A and B | (not B) and A | résultat
        -------+--------+---------+---------------+---------
        True   | True   | True    | False         | True
        True   | False  | False   | True          | True
        False  | True   | False   | False         | False
        False  | False  | False   | False         | False

    Le résultat est toujours égal à A : B ne change rien ! L'expression peut
    donc s'écrire simplement… A. En effet, elle dit "A et B, ou A et pas B" :
    dans les deux cas il faut A, et B peut valoir n'importe quoi.
    (On verra au chap. 21 comment construire ces "tables de vérité".)
"""
print((True and True) or ((not True) and True))    # => True
print((True and False) or ((not False) and True))  # => True
print((False and True) or ((not True) and False))  # => False
print((False and False) or ((not False) and False))  # => False


##########################################
#  Stocker un booléen dans une variable  #
##########################################

# 17. Le manège :
age = 15
accompagne = True
peut_monter = age >= 12 or accompagne
print(peut_monter)  # => True
age = 8
accompagne = False
peut_monter = age >= 12 or accompagne
print(peut_monter)  # => False
"""
Il suffit qu'UNE des deux conditions soit vraie : c'est un "or". À 15 ans, on
peut monter (accompagné ou non) ; à 8 ans, seulement si on est accompagné.
"""

# 18. Les années bissextiles :
annee = 2024
est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
print(est_bissextile)  # => True
annee = 2023
est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
print(est_bissextile)  # => False
annee = 1900
est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
print(est_bissextile)  # => False
annee = 2000
est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
print(est_bissextile)  # => True
"""
On traduit la règle mot à mot :
    - "divisible par 4 SAUF les années divisibles par 100" :
      annee % 4 == 0 and annee % 100 != 0
    - "… OU divisible par 400" : … or annee % 400 == 0
1900 est divisible par 4 et par 100, mais pas par 400 : elle n'est pas
bissextile. 2000 est divisible par 400 : elle l'est.
Les parenthèses ne sont pas obligatoires (and passe avant or), mais elles
rendent l'expression bien plus lisible.
(Il faut ici répéter l'expression pour chaque année : on verra au chap. 14
comment l'écrire une seule fois, dans une fonction.)
"""

# 19. Le mot de passe :
mdp = "azerty123"
print(len(mdp) >= 8 and mdp != "password")  # => True
mdp = "password"
print(len(mdp) >= 8 and mdp != "password")  # => False
"""
"password" contient bien 8 caractères, mais c'est justement le mot de passe
interdit : la 2e condition est fausse, donc toute l'expression aussi.
"""
