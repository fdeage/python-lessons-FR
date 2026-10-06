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
#  Chap. 10     #  Variables I : exercices                                     #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices « sans exécuter », suivez le programme ligne à
ligne dans votre tête, en notant la valeur de chaque variable après chaque
ligne (cf. chap. 1).

Les corrigés sont dans le fichier corrs/corr_10_variables.py.
"""


###########################
#  Déclarer une variable  #
###########################

"""
1. Sans exécuter : qu'affiche ce programme ?
       a = 3
       b = a * 2
       a = 10
       print(a, b)

2. Ce programme provoque une erreur. Laquelle, et pourquoi ? Corrigez-le.
       print(total)
       total = 12 + 30

3. Un cinéma vend des places à 9.5 € et des menus pop-corn à 6 €. Créez les
   variables prix_place, prix_menu, nb_places et nb_menus (3 places et
   2 menus), puis une variable total qui contient le prix à payer.
   Affichez-la.
"""


###################################
#  Variables et types de valeurs  #
###################################

"""
4. Sans exécuter : quel est le type de chacune de ces variables ?
       nom = "Ada"
       age = 36
       taille = 1.65
       est_majeure = age >= 18
       code_postal = "75011"

5. Pourquoi est-il préférable de ranger un code postal dans une chaîne plutôt
   que dans un entier ? (Indice : pensez au code postal "01000".)
"""


###################################
#  Lire et modifier une variable  #
###################################

"""
6. Sans exécuter : que vaut x à la fin de ce programme ?
       x = 4
       x = x + 1
       x *= 3
       x -= 2
       x //= 4

7. Un compte bancaire contient 100 €. On dépose 50 €, puis on retire 30 €,
   puis la banque verse 2 % d'intérêts (le solde est multiplié par 1.02).
   Écrivez ces opérations avec les raccourcis +=, -= et *=, puis affichez le
   solde final.

8. Construisez la phrase "Python est simple et puissant" en partant de
   phrase = "Python" et en utilisant uniquement l'opérateur +=.

9. Ce programme provoque une erreur. Pourquoi ? Corrigez-le de deux façons :
   avec str(), puis avec une f-string (cf. chap. 8).
       nb_pommes = 4
       print("J'ai " + nb_pommes + " pommes")

10. Sans exécuter : qu'affiche ce programme ?
        compteur = 0
        compteur += 1
        compteur += 1
        compteur -= 1
        print(compteur)
"""


#######################
#  Règles de nommage  #
#######################

"""
11. Parmi ces noms de variables, lesquels sont interdits par Python ? Pour
    chacun, dites pourquoi.
        age2        2age        mon-age     mon_age     _secret
        class       Prix        prix total  été         None

12. Sans exécuter : qu'affiche ce programme ?
        note = 12
        Note = 15
        print(note)

13. Pourquoi ne faut-il jamais écrire str = "abc" dans un programme ?
"""


############################
#  Conventions de nommage  #
############################

"""
14. Renommez ces variables en respectant la convention de Python (snake case)
    et en choisissant des noms parlants :
        NbEleves = 28        # le nombre d'élèves d'une classe
        x = 12.5             # un prix hors taxes, en euros
        MOYENNEgenerale = 13.2

15. Le taux de TVA (20 %) ne change jamais dans un programme de facturation.
    Comment nommer la variable qui le contient, selon les conventions vues
    dans le cours ?
"""


##########################################
#  Quelques fonctions sur les variables  #
##########################################

"""
16. On pose : a = 7, b = "7" et c = 7.0. Affichez le type de chaque variable,
    puis testez a == b et a == c.

17. Utilisez dir() et l'opérateur "in" (cf. chap. 9) pour vérifier qu'on peut
    appeler la méthode "upper" sur une chaîne, mais pas sur un entier.
"""


##########################
#  Affectation multiple  #
##########################

"""
18. En une seule ligne, créez les variables nom, prenom et age avec les
    valeurs "Lovelace", "Ada" et 36. Affichez-les.

19. On pose : gauche = "pomme" et droite = "poire". Échangez le contenu des
    deux variables, d'abord avec une variable temporaire, puis en une seule
    ligne.

20. Sans exécuter : qu'affiche ce programme ?
        x = y = 0
        x += 1
        print(x, y)

21. Que se passe-t-il avec a, b = 1, 2, 3 ? Vérifiez en protégeant la ligne
    avec try: … except ValueError as err: …
"""


######################
#  Petits problèmes  #
######################

"""
22. Convertissez une température : rangez 37.5 dans une variable celsius,
    calculez la température en degrés Fahrenheit (F = C × 9 / 5 + 32), et
    affichez "37.5 °C = 99.5 °F" avec une f-string.

23. Une vidéo dure 3725 secondes. Calculez le nombre d'heures, de minutes et
    de secondes restantes (avec // et %, cf. chap. 4), et affichez
    "1 h 2 min 5 s".

24. Un élève a obtenu 12 (coefficient 2), 15 (coefficient 3) et 8
    (coefficient 1). Calculez sa moyenne pondérée, arrondie à 2 décimales.
"""
