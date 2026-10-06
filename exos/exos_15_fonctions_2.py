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
#  Chap. 15     #  Fonctions II : exercices                                    #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les questions « sans exécuter », remplacez mentalement chaque
appel de fonction par la valeur qu'il retourne (cf. chap. 1).

Les corrigés sont dans le fichier corrs/corr_15_fonctions_2.py.
"""


############################
#  Conventions de nommage  #
############################

"""
1. Parmi ces noms de fonctions, lesquels respectent les conventions de
   Python (PEP 8) ? Lesquels sont interdits ? Renommez les autres.
       a) calculer_moyenne
       b) CalculerMoyenne
       c) 2eme_essai
       d) calculerMoyenne
       e) f
       f) convertir_euros_en_dollars
"""


#############################
#  Arguments vs paramètres  #
#############################

"""
2. Dans le code suivant, quels sont les paramètres ? Quels sont les
   arguments ? Que vaut x pendant l'exécution de l'appel ?
       def aire(x, y):
           return x * y

       largeur = 3
       print(aire(largeur, 5))

3. Sans exécuter : que se passe-t-il lors de l'appel aire(2) ? Vérifiez avec
   un try … except.
"""


################################################
#  Paramètres par défaut et arguments nommés   #
################################################

"""
4. Écrivez une fonction puissance(x, n=2) qui retourne x à la puissance n
   (2 par défaut). Testez puissance(5), puissance(2, 10) et
   puissance(n=3, x=2).

5. Sans exécuter : qu'affichent ces appels ?
       def commande(plat, quantite=1, sauce="aucune"):
           print(quantite, plat, "- sauce :", sauce)

       commande("frites")
       commande("frites", 3)
       commande("frites", sauce="ketchup")
       commande(sauce="mayo", plat="nuggets", quantite=6)

6. Pourquoi la définition suivante est-elle refusée par Python ? Corrigez-la.
       def message(texte="Bonjour", destinataire):
           ...
"""


######################
#  La valeur None    #
######################

"""
7. Sans exécuter : qu'affiche ce programme ?
       def f(x):
           if x > 0:
               return "positif"

       print(f(5))
       print(f(-5))

8. Écrivez une fonction trouver_lettre(texte, lettre) qui retourne la
   position (l'indice) de la première occurrence de lettre dans texte, ou
   None si elle n'y est pas (sans utiliser .find()). Testez le résultat avec
   "is None".

9. Sans exécuter : que valent None == 0, None == False et None == None ?
"""


########################################
#  Différence entre return et print()  #
########################################

"""
10. La fonction suivante devait calculer une moyenne, mais le programme
    plante. Pourquoi ? Corrigez la fonction.
        def moyenne(a, b):
            print((a + b) / 2)

        m = moyenne(12, 16)
        print(m + 1)

11. Écrivez deux versions d'une fonction qui calcule le périmètre d'un
    cercle (2 × 3.14159 × r) : l'une qui l'affiche, l'autre qui le
    retourne. Laquelle peut-on utiliser pour calculer la somme des périmètres
    de deux cercles ?
"""


###############################
#  Imbrication de fonctions   #
###############################

"""
12. Sans exécuter : qu'affiche ce programme ? Écrivez la suite des appels.
        def ajouter_un(x):
            return x + 1

        def doubler(x):
            return 2 * x

        print(doubler(ajouter_un(3)))
        print(ajouter_un(doubler(3)))
        print(doubler(doubler(doubler(1))))

13. Écrivez une fonction est_voyelle(c), puis une fonction
    compter_voyelles(texte) qui l'utilise.

14. Écrivez une fonction hypotenuse(a, b) qui retourne la longueur de
    l'hypoténuse d'un triangle rectangle (racine de a² + b²), en vous
    servant d'une fonction carre(x). Indice : la racine carrée de y s'écrit
    y ** 0.5.
"""


######################
#  Retour multiple   #
######################

"""
15. Écrivez une fonction min_max(a, b, c) qui retourne à la fois le plus
    petit et le plus grand des trois nombres. Récupérez les deux résultats
    dans deux variables.

16. Écrivez une fonction convertir_secondes(total) qui retourne le nombre
    d'heures, de minutes et de secondes contenues dans total secondes.
    Testez avec 3725 (1 h 2 min 5 s).

17. Sans exécuter : que se passe-t-il ?
        def deux_valeurs():
            return 1, 2

        a, b, c = deux_valeurs()
"""


#################################
#  L'adresse d'une fonction     #
#################################

"""
18. Sans exécuter : quelle est la différence entre ces deux lignes ?
        print(len)
        print(len("abc"))

19. Écrivez une fonction appliquer(fonction, a, b) qui retourne
    fonction(a, b). Utilisez-la avec une fonction addition(x, y) et une
    fonction multiplication(x, y).

20. Le programme suivant devait afficher "Bonjour", mais il affiche autre
    chose. Pourquoi ? Corrigez-le.
        def salutation():
            return "Bonjour"

        print(salutation)
"""
