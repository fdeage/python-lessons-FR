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
#  Chap. 4      #  Arithmétique : exercices                                    #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", notez d'abord votre réponse en
commentaire.

Les variables ne sont vues qu'au chap. 10 : écrivez donc directement vos
calculs dans des print(), par exemple print(3 + 4).

Les corrigés sont dans le fichier corrs/corr_04_arithm.py.
"""


################################
#  Calculs simples             #
################################

"""
Écrivez un programme qui…

1. affiche la somme de deux nombres entiers positifs
2. calcule la moyenne de trois nombres entiers
3. calcule la somme des entiers de 1 à 5
4. affiche la différence de deux nombres décimaux
5. affiche le produit d'un nombre immense et d'un décimal
6. calcule la température en degrés Celsius depuis une valeur en Fahrenheit
   (formule : F = (9/5) * C + 32, donc C = (F - 32) * 5/9), par exemple pour
   212 °F
7. calcule 2 à la puissance 16 moins 4 à la puissance 3
8. utilise la notation scientifique pour représenter la distance Terre-Soleil
   en km (distance : cent cinquante millions de km)
9. calcule la division entière de 15 par 2 et affiche son type
10. affiche le type du produit de 5.0 par 14
11. affiche les valeurs absolues de 4.3, -14.8, et 4.3 - 14.8 (dans le même
    print)
12. affiche la valeur absolue d'un entier négatif
13. détermine si un nombre est pair ou impair (indice : que vaut le reste de
    la division par 2 ?)
14. convertit un nombre de minutes (par exemple 135) en heures et minutes
"""


################################
#  Ints et floats              #
################################

"""
15. Sans exécuter : quel est le type (int ou float) de chacun de ces nombres ?
        42      42.0      -3      .5      4e2      1_000_000

16. Écrivez un milliard de deux façons : avec des underscores, puis en
    notation scientifique. Les deux valeurs sont-elles du même type ?

17. Sans exécuter : que vaut 0.1 + 0.2 ? Et 0.1 + 0.2 == 0.3 ? Comment
    vérifier correctement que 0.1 + 0.2 « vaut » 0.3 ?

18. Calculez 2 ** 1000. Combien de chiffres le résultat a-t-il environ ?
    Pourquoi Python n'a-t-il aucun problème, alors que 2.0 ** 10000 en a
    un ? (protégez cette deuxième ligne avec try: … except OverflowError: …)
"""


################################
#  Division entière et modulo  #
################################

"""
19. Sans exécuter, que valent :
        17 // 5      17 % 5      -17 // 5      -17 % 5      7.5 // 2

20. Utilisez divmod() pour obtenir en une fois le quotient et le reste de la
    division de 100 par 7.

21. 1000 secondes, c'est combien de minutes et de secondes ?

22. Quel est le chiffre des unités de 98765 ? Et le nombre formé par les deux
    derniers chiffres ? (Utilisez le modulo.)
"""


################################
#  Division par zéro           #
################################

"""
23. Sans exécuter : que se passe-t-il pour 1 / 0, 1 // 0 et 1 % 0 ? Vérifiez
    chaque cas en le protégeant avec try: … except ZeroDivisionError: …

24. Et pour 1.0 / 0.0 ? Le fait d'utiliser des floats change-t-il quelque
    chose ?
"""


################################
#  Arrondis, min() et max()    #
################################

"""
25. Sans exécuter, que valent :
        round(4.6)     round(-4.6)     round(4.5)     round(5.5)
        round(3.14159, 3)     round(1234.5678, -1)

26. Affichez 2 / 3 arrondi à deux décimales.

27. Affichez le plus grand et le plus petit des nombres suivants :
        12, -4, 7.5, 0, 33, -4.5

28. Un sac de ciment pèse 35 kg. Une brouette ne supporte pas plus de 80 kg.
    Combien de sacs entiers peut-on mettre dans la brouette ? Quel poids
    reste-t-il de libre ?
"""
