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
#  Chap. 9      #  Booléens : exercices                                        #
#               #                                                              #
################################################################################

# Sans les exécuter, déterminer la valeur de ces expressions :

# 1. tests basiques d'égalité et de comparaison :

1 == 1
2 == 1
2 != 5
6 < 9
5 >= 5
32 % 2 == 1
33 % 3 > 0


# 2. tests avec des variables de type distinct :

2 == "2"
3 == 3.0
5 == 5.1
6 == False
"2" == "2.0"
3 + 0.000000000001 == 3
3 + 0.00000000000000001 == 3
True != "True"


# 3. tests entre littéraux booléens (True et False) :

True == True
False == False
False == True
False != True


# 4. expressions avec opérateurs not, and et or :
not True
not False
True and True
False and False
False or False
True and not False
False != (not False)
False or True

1 == 1 and 2 == 1
not "test" == "test"
2 == 1 or 2 != 1


# 5. expressions avec l'opérateur booléen `in`
1 in [1, 2, 3, 4]
1 in [2, 3, 4, 5]
"n" in "anne"
"test" == "testing"
"test" in "testing"


# 6. tests avec des variables booléennes
A = True
B = False

B or A
B and A
A and 1 == 1
B or 0 != 1
A or 1 == 2
(A and B) or ((not B) and A)

# Faites une table de vérité de l'expression précédente : de quelle variable
# dépend-elle ? Comment pourrait-on la réécrire ?
