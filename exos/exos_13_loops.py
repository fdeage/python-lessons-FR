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
#  Chap. 13     #  Les boucles : exercices                                     #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les questions « sans exécuter », faites d'abord tourner le
programme DANS VOTRE TÊTE (cf. chap. 1), en notant la valeur de chaque
variable à chaque tour de boucle, puis vérifiez.

Rappel : print(x, end=" ") affiche x suivi d'un espace au lieu d'un saut de
ligne, ce qui permet d'afficher plusieurs valeurs sur une même ligne.

Les corrigés sont dans le fichier corrs/corr_13_loops.py.

N'oubliez pas les parties 3 et 4 de l'exercice FizzBuzz, à la fin du fichier
exos/exos_12_if_then.py : vous avez maintenant tout ce qu'il faut !
"""


#########################
#  La boucle "while"    #
#########################

"""
1. Sans exécuter : qu'affiche ce programme ? Remplissez un tableau de trace
   avec une colonne par variable (x et y) et une ligne par tour de boucle.
       x = 1
       y = 0
       while x < 5:
           y = y + x
           x = x + 1
       print(x, y)

2. Sans exécuter : combien de fois "coucou" est-il affiché ?
       n = 10
       while n > 0:
           print("coucou")
           n = n - 3

3. Sans exécuter : que se passe-t-il avec ce programme ? Corrigez-le pour
   qu'il affiche 0 1 2 3 4.
       i = 0
       while i < 5:
           print(i, end=" ")

4. Avec une boucle while, affichez les puissances de 2 inférieures à 1000 :
   1 2 4 8 16 … 512.

5. Un capital de 1000 € est placé à 3 % par an (chaque année, il est multiplié
   par 1.03). Avec une boucle while, calculez au bout de combien d'années il
   dépasse 2000 €.
"""


#########################################
#  La boucle "for" avec une collection  #
#########################################

"""
6. Avec une boucle for, affichez chaque lettre du mot "Python", une par ligne.

7. Comptez le nombre de voyelles (a, e, i, o, u, y) dans la phrase
   "les boucles sont partout en programmation". Indice : l'opérateur "in"
   teste si un caractère fait partie d'une chaîne : "a" in "aeiouy".

8. Avec une boucle for sur la liste ["Paris", "Lyon", "Marseille"],
   affichez "J'aime Paris", "J'aime Lyon", etc.

9. Écrivez une boucle qui construit l'inverse de la chaîne "bonjour"
   ("ruojnob"), sans utiliser de slice.
"""


################################################
#  La boucle "for" avec la fonction range()    #
################################################

"""
10. Sans exécuter : que contiennent ces range() ? (Écrivez la liste des
    valeurs, puis vérifiez avec list().)
        a) range(6)
        b) range(2, 9)
        c) range(1, 20, 4)
        d) range(10, 0, -2)
        e) range(5, 5)

11. Affichez la table de multiplication de 7, sous la forme
        7 x 1 = 7
        7 x 2 = 14
        …
        7 x 10 = 70

12. Calculez la somme des nombres pairs de 2 à 100 (inclus), de deux façons :
    avec un "if" dans la boucle, puis avec le pas de range().

13. Sans exécuter : que vaut i après cette boucle ?
        for i in range(3):
            pass
        print(i)
"""


##########################################
#  Équivalence entre "while" et "for"    #
##########################################

"""
14. Réécrivez cette boucle while avec une boucle for et range() :
        i = 10
        while i <= 50:
            print(i, end=" ")
            i = i + 10

15. Peut-on toujours remplacer un while par un for ? Pourquoi la boucle de
    l'exercice 5 (le capital qui double) s'écrit-elle plus naturellement avec
    un while ?
"""


#########################################
#  Les mots-clés "break" et "continue"  #
#########################################

"""
16. Sans exécuter : qu'affichent ces deux boucles ?
        for i in range(10):
            if i == 4:
                break
            print(i, end=" ")
        print()
        for i in range(10):
            if i % 3 == 0:
                continue
            print(i, end=" ")

17. Avec une boucle for et break, trouvez le plus petit entier n supérieur
    ou égal à 1 tel que n * n dépasse 500.

18. Avec continue, affichez les nombres de 1 à 20 qui ne sont multiples ni de
    2 ni de 3.
"""


#################################
#  Compteurs et accumulateurs   #
#################################

"""
19. Calculez 2 à la puissance 10 SANS utiliser l'opérateur ** : partez de 1,
    et multipliez par 2 dix fois.

20. Comptez combien de nombres entre 1 et 1000 sont divisibles par 7.

21. Dans la chaîne "3, 7, 1, 9, 4", chaque chiffre est un nombre. Avec une
    boucle, calculez leur somme (24) et le plus grand (9), sans utiliser
    sum() ni max(). Indice : "7".isdigit() vaut True, ", ".isdigit() vaut
    False.

22. Un nombre est "parfait" s'il est égal à la somme de ses diviseurs autres
    que lui-même (6 = 1 + 2 + 3). Vérifiez que 28 est parfait.
"""


#########################
#  Boucles imbriquées   #
#########################

"""
23. Sans exécuter : combien de fois "x" est-il affiché ?
        for i in range(3):
            for j in range(4):
                print("x", end="")
        print()

24. Affichez ce triangle avec deux boucles imbriquées (ou une seule boucle
    et l'opérateur * sur les chaînes, cf. chap. 7) :
        *
        **
        ***
        ****
        *****

25. Affichez toutes les tables de multiplication de 1 à 5, une table par
    ligne :
        1 2 3 4 5 6 7 8 9 10
        2 4 6 8 10 12 14 16 18 20
        …
"""
