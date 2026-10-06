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
#  Chap. 5      #  Précédence et whitespace : exercices                        #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", notez d'abord votre réponse en
commentaire, puis vérifiez avec print().

Les corrigés sont dans le fichier corrs/corr_05_precedence.py.
"""


#################################
#  Précédence des opérateurs    #
#################################

"""
1. Sans l'exécuter, comment s'évalue l'expression suivante ?
       3 + 5 * 2

2. Ajoutez des parenthèses pour rendre cette expression plus lisible (sans
   changer son résultat) :
       10 - 2 * 3 / 4

3. Que renvoient les deux expressions suivantes ? Quel est le type du
   résultat ?
       5 - 1 * 7 + 1 / 3 - 1
       ((5 - 1) * ((7 + 1) / (3 - 1)))

4. Le formatage des expressions suivantes est-il correct (selon la PEP 8) ?
       2*  (5 + 3)
       (7-3)//2

5. Expliquez pourquoi ces deux expressions donnent des résultats différents :
       8 / 2 * 2
       8 / (2 * 2)

6. Quelle est la valeur de cette expression ?
       2 ** 3 * 4

7. Expliquez pourquoi ces deux expressions sont équivalentes (les booléens
   seront détaillés au chap. 9) :
       not True or False
       (not True) or False

8. Quelle est la valeur de cette expression ? Pourquoi ?
       True and 2 > 3

9. Ajoutez des parenthèses à l'expression suivante pour qu'elle vaille 20 :
       2 + 3 * 4
   Puis pour qu'elle vaille… 14 (sans parenthèses inutiles !).

10. Sans exécuter : que vaut 10 - 4 % 3 ? Et (10 - 4) % 3 ?
"""


################################################
#  Associativité : de gauche à droite… sauf…   #
################################################

"""
11. Sans exécuter : que valent 100 / 10 / 5 et 100 / (10 / 5) ? Laquelle des
    deux s'écrit sans parenthèses ?

12. Sans exécuter : que vaut 2 ** 3 ** 2 ? Pourquoi ce n'est pas 64 ?

13. Sans exécuter : que valent -3 ** 2 et (-3) ** 2 ?
"""


##########################################
#  Whitespace et erreurs d'indentation   #
##########################################

"""
14. Ces trois expressions donnent-elles le même résultat ? Laquelle est la
    mieux présentée ?
        7 * 3-1
        7*3 - 1
        7   *   3   -   1

15. Sans exécuter : pourquoi le code suivant provoque-t-il une erreur ?
    Laquelle ?
            print("Bonjour")
        print("Au revoir")

16. Pourquoi est-il déconseillé de mélanger espaces et tabulations en début
    de ligne ? Combien d'espaces la PEP 8 recommande-t-elle pour un niveau
    d'indentation ?
"""


##################################
#  Couper une ligne trop longue  #
##################################

"""
17. Le calcul suivant est trop long pour tenir sur une ligne de 79
    caractères. Récrivez-le sur trois lignes, de deux façons : avec des
    parenthèses (recommandé), puis avec des backslashs.
        print(1000 + 2000 + 3000 + 4000 + 5000 + 6000 + 7000 + 8000 + 9000)

18. Pourquoi la méthode avec les parenthèses est-elle recommandée ?
"""


#######################################
#  Le whitespace recommandé (PEP 8)   #
#######################################

"""
19. Récrivez les lignes suivantes selon les recommandations de la PEP 8 :
        x=4
        y = x*x+2*x+1
        print (x , y)
        print( x+y )
"""
