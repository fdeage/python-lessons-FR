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
#  Chap. 19     #  Variables II : exercices                                    #
#               #                                                              #
################################################################################

"""
La plupart de ces exercices sont des exercices de "simulation" : sans
exécuter le code, déterminez ce qu'il affiche (ou quelle erreur il
provoque), en appliquant la règle LEGB. Vérifiez ensuite en le recopiant
dans un fichier ou dans l'interpréteur.

Les corrigés sont dans le fichier corrs/corr_19_var_2.py.
"""


##################################
#  Les 4 portées d'une variable  #
##################################

"""
1. Pour chaque variable de ce programme, indiquez sa portée (Locale,
   Englobante, Globale ou Built-in) :
       TAUX = 0.2
       def prix_ttc(prix_ht):
           montant_tva = prix_ht * TAUX
           return round(prix_ht + montant_tva, 2)
   (TAUX, prix_ht, montant_tva, round)

2. Qu'affiche ce programme ?
       def f():
           x = 10
           print(x)
       f()
       print(x)

3. Qu'affiche ce programme ?
       x = 1
       def f():
           print(x)
       f()
       x = 2
       f()

4. Qu'affiche ce programme ?
       def exterieure():
           message = "dehors"
           def interieure():
               print(message)
           message = "modifié"
           interieure()
       exterieure()

5. Après cette boucle (hors de toute fonction), la variable i existe-t-elle ?
   Que vaut-elle ?
       for i in range(5):
           pass
"""


##########################
#  Conflit de variables  #
##########################

"""
6. Qu'affiche ce programme ?
       x = "global"
       def f():
           x = "local"
           print(x)
       f()
       print(x)

7. Ce programme provoque une erreur. Laquelle, et pourquoi ? Corrigez-le de
   deux façons : avec le mot-clé global, puis (mieux) sans.
       compteur = 0
       def incrementer():
           compteur = compteur + 1
       incrementer()

8. Qu'affiche ce programme ? Pourquoi n'a-t-on pas besoin de "global" ?
       panier = []
       def ajouter(article):
           panier.append(article)
       ajouter("pain")
       ajouter("lait")
       print(panier)

9. Qu'affiche ce programme ? Expliquez la différence avec l'exercice 8.
       panier = ["pain"]
       def vider():
           panier = []
       vider()
       print(panier)

10. Qu'affiche ce programme ?
        def f(liste):
            liste.append(4)
            liste = [0]
            liste.append(5)
            return liste
        a = [1, 2, 3]
        b = f(a)
        print(a)
        print(b)

11. Écrivez une fonction compteur_appels() qui utilise nonlocal pour compter le
    nombre d'appels à une fonction imbriquée, comme dans le cours.
"""


####################
#  Les namespaces  #
####################

"""
12. Créez une variable globale LANGAGE = "Python", puis vérifiez avec
    globals() qu'elle fait bien partie du namespace global.

13. Écrivez une fonction qui crée deux variables locales et affiche locals().

14. Qu'affiche ce programme, et pourquoi ? Comment réparer le problème ?
        list = [1, 2, 3]
        nombres = list(range(5))
"""


######################
#  Bonnes pratiques  #
######################

"""
15. Ce programme utilise des variables globales. Réécrivez-le pour que la
    fonction reçoive tout ce dont elle a besoin en paramètres et RETOURNE son
    résultat :
        solde = 100
        def deposer(montant):
            global solde
            solde = solde + montant
        deposer(50)
        deposer(20)
        print(solde)
"""
