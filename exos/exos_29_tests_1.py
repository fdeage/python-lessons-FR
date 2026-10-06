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
#  Chap. 29     #  Tests et spécification I : exercices                        #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1).

Rappel : un assert qui échoue arrête le programme. Pour que ce fichier reste
exécutable, protégez avec try: … except AssertionError: … les assert dont vous
voulez montrer l'échec (cf. chap. 26).

Les corrigés sont dans le fichier corrs/corr_29_tests_1.py.
"""


######################################
#  Tester ses fonctions avec assert  #
######################################

"""
1. Sans exécuter, lesquels de ces assert soulèvent une AssertionError ?
   Pourquoi ? Vérifiez (en protégeant chaque ligne).
       assert 3 * 2 == 6
       assert "a" in "chat"
       assert len([]) == 1
       assert 0.1 + 0.2 == 0.3
       assert "Python".lower() == "python"
       assert [1, 2] == [2, 1]

2. Écrivez au moins 5 assert qui testent la fonction intégrée max() :
   liste "normale", nombres négatifs, liste d'un seul élément, plusieurs
   maximums égaux, liste de strings.

3. Écrivez un assert avec un message d'erreur qui vérifie que la variable
   age = -3 est positive. Affichez le message obtenu.

4. Sans exécuter : pourquoi cette ligne ne soulève-t-elle JAMAIS d'erreur, même
   si x est négatif ? (Ne la recopiez pas telle quelle : Python affiche un
   avertissement.)
       assert (x > 0, "x doit être positif")
"""


#################################
#  Les 5 effets d'une fonction  #
#################################

"""
5. Pour chacune de ces fonctions, indiquez lequel des 5 effets elle produit
   (retour, affichage, modification d'un paramètre, modification d'une
   variable globale, erreur). Laquelle est la plus facile à tester ?
       def f(a, b):
           return a * b

       def g(a, b):
           print(a * b)

       def h(liste):
           liste.append(0)

       compteur = 0
       def k():
           global compteur
           compteur += 1

       def m(x):
           if x < 0:
               raise ValueError("x doit être positif")

6. Cette fonction est difficile à tester car elle affiche au lieu de
   retourner. Réécrivez-la pour qu'elle retourne la mention, puis testez-la
   avec au moins 4 assert (pensez aux cas-limites : 10, 12, 14…).
       def afficher_mention(note):
           if note >= 16:
               print("Très bien")
           elif note >= 14:
               print("Bien")
           elif note >= 12:
               print("Assez bien")
           elif note >= 10:
               print("Passable")
           else:
               print("Insuffisant")

7. Écrivez une fonction racine(x) qui retourne x ** 0.5, et soulève une
   ValueError si x est négatif. Testez :
       a) des valeurs correctes avec assert,
       b) que racine(-4) soulève bien une ValueError (cf. l'exemple de my_pop()
          dans le chapitre).
"""


########################
#  Implémenter assert  #
########################

"""
8. Sur le modèle de my_assert() (chapitre), écrivez une fonction
   assert_egal(a, b) qui soulève une AssertionError avec le message
   "<a> != <b>" si a et b sont différents (par ex. "4 != 5"), et ne fait
   rien sinon. Testez-la dans les deux cas.
"""


####################################
#  Exemple : la fonction my_pop()  #
####################################

"""
9. Écrivez une fonction my_index(liste, x) qui fait la même chose que la
   méthode liste.index(x) : elle retourne l'indice de la première occurrence
   de x, et soulève une ValueError si x n'est pas dans la liste (sans utiliser
   .index() !).
   Écrivez ensuite une fonction test_my_index() qui compare my_index() avec
   .index() sur plusieurs cas (début, milieu, fin, doublons, absent).

10. Cette fonction contient un bug. Trouvez un test (un assert) qui le révèle,
    puis corrigez la fonction.
        def my_max(liste):
            maximum = 0
            for x in liste:
                if x > maximum:
                    maximum = x
            return maximum
"""


###########################################
#  La méthode "Think-Red-Green-Refactor"  #
###########################################

"""
11. Appliquez la méthode à une fonction compter_voyelles(s) qui retourne le
    nombre de voyelles (a, e, i, o, u, y, en minuscule ou majuscule) de s :
        - Think : quels cas-limites ? (chaîne vide, pas de voyelle,
          majuscules…)
        - Red : une version "vide" et les tests (qui échouent),
        - Green : une première version qui passe les tests,
        - Refactor : une version plus courte ou plus lisible (les tests
          doivent toujours passer).

12. Même exercice avec est_bissextile(annee). Rappel : une année est
    bissextile si elle est divisible par 4, sauf si elle est divisible par
    100… sauf si elle est divisible par 400 (2000 est bissextile, 1900 ne
    l'est pas).
"""


####################
#  Les docstrings  #
####################

"""
13. Écrivez une docstring (avec la notation "(type, type) -> type" du
    chapitre) pour la fonction suivante, puis affichez-la avec __doc__.
        def repeter(mot, n):
            return " ".join([mot] * n)
"""


#############################
#  Les annotations de type  #
#############################

"""
14. Ajoutez des annotations de type aux fonctions repeter() (exercice 13) et
    compter_voyelles() (exercice 11). Affichez leur attribut __annotations__.

15. Sans exécuter, que se passe-t-il ici ? Python refuse-t-il l'appel ?
        def double(x: int) -> int:
            return x * 2

        print(double("ab"))
"""
