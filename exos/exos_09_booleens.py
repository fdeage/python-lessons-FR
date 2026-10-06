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
#  Chap. 9      #  Booléens I : exercices                                      #
#               #                                                              #
################################################################################

"""
Pour la plupart de ces exercices, il faut déterminer la valeur d'expressions
SANS les exécuter : notez votre réponse (True ou False) à côté de chaque
ligne, puis vérifiez avec print().

Les corrigés sont dans le fichier corrs/corr_09_booleens.py.
"""


########################
#  Valeurs booléennes  #
########################

"""
1. Sans exécuter : qu'affichent ces lignes ?
       print(type(True))
       print(type("True"))
       print(True == "True")

2. Parmi ces lignes, laquelle provoque une erreur ? Pourquoi ? Vérifiez en la
   protégeant avec try: … except NameError as err: …
       True
       false
       "False"
"""


##############################################################
#  Expressions booléennes : égalité, inégalité, comparaison  #
##############################################################

"""
3. Tests basiques d'égalité et de comparaison :
       1 == 1
       2 == 1
       2 != 5
       6 < 9
       5 >= 5
       32 % 2 == 1
       33 % 3 > 0
       7 < 9 < 15
       85 < 32 < 127
       "abc" == "abc"
       "abc" == "abd"
       "2" == "2"

4. Tests avec des valeurs de types différents :
       2 == "2"
       3 == 3.0
       5 == 5.1
       6 == False
       "2" == "2.0"
       3 + 0.000000000001 == 3
       3 + 0.00000000000000001 == 3
       True != "True"
       True == 1
       True != 2

5. Écrivez une expression qui vaut True si le nombre 47 est compris entre 0 et
   100 (bornes incluses), en enchaînant les comparaisons.

6. Écrivez une expression qui vaut True si le nombre 2024 est un multiple de 4.
"""


##########################
#  Comparer des strings  #
##########################

"""
7. Sans exécuter :
       "abc" < "abd"
       "chat" < "chats"
       "pomme" < "poire"
       "Zèbre" < "abeille"
       "10" < "9"
       10 < 9
"""


#############################
#  Pièges des comparaisons  #
#############################

"""
8. Que se passe-t-il avec 1 < "1" ? Et avec 1 == "1" ? Vérifiez (protégez la
   ligne qui provoque une erreur avec try: … except TypeError as err: …).

9. Sans exécuter : que vaut 0.1 + 0.2 == 0.3 ? Écrivez ensuite une expression
   qui compare correctement ces deux nombres (cf. le cours).
"""


########################################
#  Opérateurs booléens : not, and, or  #
########################################

"""
10. Tests entre valeurs booléennes :
        True == True
        False == False
        False == True
        False != True

11. Expressions avec not, and et or :
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

12. L'opérateur "in" (pour les chaînes, cf. le cours ; les listes, entre
    crochets, seront vues au chap. 16 : "in" teste si la valeur figure dans
    la liste) :
        1 in [1, 2, 3, 4]
        1 in [2, 3, 4, 5]
        2.0 in [1, 2, 3]
        "n" in "anne"
        "test" == "testing"
        "test" in "testing"
        "testing" in "test"

13. Sans exécuter : l'expression suivante provoque-t-elle une erreur de
    division par zéro ? Pourquoi ?
        0 != 0 and 1 / 0 > 1
"""


#############################
#  Combinaisons booléennes  #
#############################

"""
14. Sans exécuter, en tenant compte des priorités (not, puis and, puis or) :
        True or False and False
        (True or False) and False
        not True or True
        not (True or True)

15. Tests avec des variables booléennes. On pose : A = True et B = False.
        B or A
        B and A
        A and 1 == 1
        B or 0 != 1
        A or 1 == 2
        (A and B) or ((not B) and A)

16. Faites (à la main) la liste des valeurs de la dernière expression de
    l'exercice 15 pour les 4 combinaisons possibles de A et B (True/True,
    True/False, False/True, False/False). De quelle variable dépend-elle
    vraiment ? Comment pourrait-on la réécrire plus simplement ?
"""


##########################################
#  Stocker un booléen dans une variable  #
##########################################

"""
17. On pose : age = 15 et accompagne = True. Un manège est autorisé aux
    personnes de 12 ans ou plus, ou aux plus jeunes s'ils sont accompagnés.
    Rangez dans une variable peut_monter l'expression correspondante, puis
    affichez-la. Testez avec d'autres valeurs.

18. Une année est bissextile si elle est divisible par 4, SAUF les années
    divisibles par 100, qui ne le sont que si elles sont aussi divisibles par
    400. Rangez dans une variable est_bissextile l'expression qui teste une
    année annee. Vérifiez avec 2024 (oui), 2023 (non), 1900 (non) et
    2000 (oui).

19. Un mot de passe est "acceptable" s'il contient au moins 8 caractères
    (len(), cf. chap. 7) ET s'il est différent de "password". Écrivez
    l'expression pour mdp = "azerty123", puis pour mdp = "password".
"""
