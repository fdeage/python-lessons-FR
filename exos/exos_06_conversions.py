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
#  Chap. 6      #  Conversions : exercices                                     #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Les variables ne seront vues qu'au chap. 10 : écrivez directement
les calculs dans des print().

Pour les conversions entre bases, faites d'abord le calcul À LA MAIN (sur
papier), puis vérifiez avec Python.

Les corrigés sont dans le fichier corrs/corr_06_conversions.py.
"""


###################################
#  La fonction intégrée `type()`  #
###################################

"""
1. Sans exécuter : qu'affichent ces lignes ? Vérifiez ensuite.
       print(type(7))
       print(type(7.0))
       print(type("7"))
       print(type(7 / 7))
       print(type(7 // 7))
       print(type(True))

2. Sans exécuter : que valent ces expressions (True ou False) ?
       3 == 3.0
       type(3) == type(3.0)
       type(2 + 3.0) == float
       type("3") == int
"""


########################################
#  Conversions entre types : int(), …  #
########################################

"""
3. Sans exécuter : que valent ces expressions ?
       int(9.99)
       int(-9.99)
       float(4)
       int("12") + 1
       float("2.5") * 2
       str(12) == "12"
       "12" == 12

4. Parmi ces conversions, lesquelles provoquent une erreur ? Vérifiez en
   protégeant chaque ligne avec try: … except ValueError as err: …, comme dans
   le cours.
       int("12.5")
       float("12,5")
       int("  7 ")
       float("1e2")
       int("douze")

5. Convertissez la chaîne "7.9" en entier, en UNE seule expression. Quelle
   valeur obtenez-vous ?

6. Sans exécuter : que valent int(-7.5) et -7.5 // 1 ? Pourquoi sont-ils
   différents ?
"""


##################################
#  Arrondir un nombre : round()  #
##################################

"""
7. Sans exécuter : que valent ces expressions ?
       round(4.6)
       round(4.4)
       round(-2.7)
       round(2.71828, 3)
       round(1.5)
       round(2.5)

8. Un article coûte 19.99 € hors taxes. Calculez son prix toutes taxes
   comprises (TVA de 20 %, soit un prix multiplié par 1.2), arrondi au
   centime.

9. Trouvez un nombre x pour lequel int(x) et round(x) donnent des résultats
   différents, et un nombre pour lequel ils donnent le même résultat.
"""


#############################
#  Les bases de numération  #
#############################

"""
10. Écrivez la décomposition du nombre binaire 1011 en puissances de 2 (comme
    dans le cours), puis faites calculer cette somme par Python.

11. Même question pour le nombre hexadécimal 1F, en puissances de 16
    (rappel : F vaut 15).

12. Combien de chiffres différents utilise-t-on en base 2 ? En base 8 ? En
    base 16 ? Quel est le plus grand chiffre de chacune de ces bases ?
"""


#################################
#  Conversions vers le décimal  #
#################################

"""
13. Convertissez le nombre binaire 0b110110 en décimal.

14. Convertissez le nombre hexadécimal 0x1A7 en décimal.

15. Convertissez le nombre octal 0o777 en décimal.

16. Sans exécuter : que vaut 0b1111 + 0x10 ? Quel est le type du résultat ?
"""


###################################
#  Conversions depuis le décimal  #
###################################

"""
17. Convertissez le nombre décimal 45 en binaire.

18. Convertissez le nombre hexadécimal 0xF3 en binaire.

19. Convertissez le nombre décimal 255 en hexadécimal.

20. Convertissez le nombre binaire 0b110101110 en hexadécimal.

21. Affichez le nombre 200 en binaire, sans le préfixe "0b". Affichez ensuite
    le nombre 5 en binaire sur 8 chiffres exactement (un "octet").

22. Pourquoi hex(bin(5)) provoque-t-il une erreur ? Vérifiez en protégeant la
    ligne avec try: … except TypeError as err: …
"""


############################################
#  Conversions depuis une base arbitraire  #
############################################

"""
23. Convertissez en décimal :
        a) le nombre 101101 écrit en base 3,
        b) le nombre 21012 écrit en base 3,
        c) le nombre 1243 écrit en base 5,
        d) le nombre ABCDEF écrit en base 16.
    Faites au moins le a) à la main.

24. La couleur Web #FF8000 (un orange) est composée de trois nombres
    hexadécimaux de 2 chiffres : FF pour le rouge, 80 pour le vert et 00 pour
    le bleu. Convertissez ces trois composantes en décimal.

25. Pourquoi int("2", 2) provoque-t-il une erreur, alors que int("2", 3)
    fonctionne ? Que vaut int("2", 3) ?
"""
