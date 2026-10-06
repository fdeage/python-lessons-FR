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
#  Chap. 5      #  Précédence et whitespace : corrigés                         #
#               #                                                              #
################################################################################

#################################
#  Précédence des opérateurs    #
#################################

# 1. La multiplication passe avant l'addition : 3 + (5 * 2) = 3 + 10
print(3 + 5 * 2)  # => 13

# 2. Avec des parenthèses qui montrent l'ordre réel des calculs :
print(10 - 2 * 3 / 4)        # => 8.5
print(10 - ((2 * 3) / 4))    # => 8.5 (même résultat, plus lisible)
# * et / ont la même priorité : on les calcule de gauche à droite, donc
# 2 * 3 = 6 d'abord, puis 6 / 4 = 1.5, puis 10 - 1.5 = 8.5.

# 3. Les deux expressions :
print(5 - 1 * 7 + 1 / 3 - 1)
# => -2.666666666666667
# Calcul : 1 * 7 = 7 et 1 / 3 = 0.333…, puis 5 - 7 + 0.333… - 1
print(((5 - 1) * ((7 + 1) / (3 - 1))))  # => 16.0
# Calcul : 4 * (8 / 2) = 4 * 4.0 = 16.0
# Dans les deux cas, le résultat est un float, car il contient une division
# avec "/".
print(type(((5 - 1) * ((7 + 1) / (3 - 1)))))  # => <class 'float'>

# 4. Le formatage n'est pas correct : il faut une espace de chaque côté des
# opérateurs (on peut au plus coller les opérateurs les plus prioritaires),
# jamais d'espaces "déséquilibrées" comme dans `2*  (`.
print(2 * (5 + 3))  # => 16
print((7 - 3) // 2)  # => 2

# 5. / et * ont la même priorité et se calculent de GAUCHE À DROITE :
print(8 / 2 * 2)    # => 8.0 (8 / 2 = 4.0, puis 4.0 * 2 = 8.0)
print(8 / (2 * 2))  # => 2.0 (les parenthèses forcent 2 * 2 = 4 d'abord)

# 6. La puissance passe avant la multiplication : (2 ** 3) * 4 = 8 * 4
print(2 ** 3 * 4)  # => 32

# 7. "not" est prioritaire sur "or" : la première expression se lit donc
# comme la seconde. not True vaut False, et False or False vaut False.
print(not True or False)    # => False
print((not True) or False)  # => False

# 8. Les comparaisons passent avant "and" : on calcule d'abord 2 > 3 (False),
# puis True and False, qui vaut False.
print(True and 2 > 3)  # => False

# 9. Pour obtenir 20, on force l'addition d'abord :
print((2 + 3) * 4)  # => 20
# Pour obtenir 14, c'est l'ordre normal : les parenthèses seraient inutiles
# (on peut toutefois les ajouter pour la lisibilité : 2 + (3 * 4)).
print(2 + 3 * 4)  # => 14

# 10. Le modulo a la même priorité que * et / : il passe avant la soustraction
print(10 - 4 % 3)    # => 9 (4 % 3 = 1, puis 10 - 1)
print((10 - 4) % 3)  # => 0 (6 % 3 = 0)


################################################
#  Associativité : de gauche à droite… sauf…   #
################################################

# 11. La division est associative à gauche :
print(100 / 10 / 5)    # => 2.0 (= (100 / 10) / 5 = 10.0 / 5)
print(100 / (10 / 5))  # => 50.0 (= 100 / 2.0)
# C'est la première qui s'écrit sans parenthèses.

# 12. La puissance est associative à DROITE : on calcule 3 ** 2 = 9 d'abord,
# puis 2 ** 9 = 512. Pour obtenir 64, il faut écrire (2 ** 3) ** 2.
print(2 ** 3 ** 2)    # => 512
print((2 ** 3) ** 2)  # => 64

# 13. La puissance passe avant le moins "unaire" (le signe -) :
print(-3 ** 2)    # => -9 (= -(3 ** 2))
print((-3) ** 2)  # => 9


##########################################
#  Whitespace et erreurs d'indentation   #
##########################################

# 14. Les espaces en milieu de ligne ne changent pas le résultat :
print(7 * 3-1)          # => 20
print(7*3 - 1)          # => 20
print(7   *   3   -   1)  # => 20
"""
La deuxième présentation est la meilleure : en collant les opérateurs
prioritaires, elle montre visuellement l'ordre des calculs. La première est
trompeuse : elle suggère qu'on calcule 3 - 1 d'abord, ce qui est faux !

15. La première ligne est indentée alors qu'elle n'est dans aucun bloc (pas
    de "if", cf. chap. 12) : Python lève une IndentationError ("unexpected
    indent"). Comme c'est une erreur de syntaxe, le fichier ne se lancerait
    même pas. On la démontre ici avec exec(), comme dans le cours :
"""
try:
    exec("    print('Bonjour')\nprint('Au revoir')")
except IndentationError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
16. Une tabulation et des espaces peuvent paraître identiques à l'écran, mais
    Python les distingue : un mélange produit des erreurs (TabError) ou un code
    qui ne fait pas ce qu'il semble faire. La PEP 8 recommande 4 ESPACES par
    niveau d'indentation (configurez votre éditeur pour que la touche Tab
    insère 4 espaces).
"""


##################################
#  Couper une ligne trop longue  #
##################################

# 17. Avec des parenthèses : à l'intérieur, on peut revenir à la ligne
# librement.
print(1000 + 2000 + 3000
      + 4000 + 5000 + 6000
      + 7000 + 8000 + 9000)  # => 45000

# Avec des backslashs : le \ doit être le TOUT DERNIER caractère de la ligne.
print(1000 + 2000 + 3000 + \
      4000 + 5000 + 6000 + \
      7000 + 8000 + 9000)  # => 45000

"""
18. Les parenthèses sont recommandées car :
    - un simple espace oublié après le \\ provoque une erreur de syntaxe,
      invisible à l'œil nu ;
    - on ne peut pas mettre de commentaire après un \\ ;
    - les parenthèses délimitent clairement le début et la fin de l'expression.
"""


#######################################
#  Le whitespace recommandé (PEP 8)   #
#######################################

# 19. Version conforme à la PEP 8 (les variables seront vues au chap. 10) :
x = 4
y = x*x + 2*x + 1  # on colle les opérateurs prioritaires (ou : x * x + …)
print(x, y)  # => 4 25
print(x + y)  # => 29
