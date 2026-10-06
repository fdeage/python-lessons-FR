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
#  Chap. 14     #  Fonctions I : exercices                                     #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour chaque fonction que vous écrivez, testez-la avec plusieurs
valeurs, y compris des cas limites (0, nombre négatif, chaîne vide…).

Les corrigés sont dans le fichier corrs/corr_14_fonctions_1.py.
"""


##########################################
#  Définition et utilité d'une fonction  #
##########################################

"""
1. Dans l'appel round(3.14159, 2) : quel est le nom de la fonction ? Quels
   sont ses arguments ? Que retourne-t-elle ?

2. Citez trois avantages à écrire une fonction plutôt que de copier-coller
   le même code à plusieurs endroits.
"""


################################
#  Fonctions Python intégrées  #
################################

"""
3. Sans exécuter : que valent ces expressions ?
       a) abs(-7) + abs(7)
       b) max(4, 12, 9) - min(4, 12, 9)
       c) round(2.71828, 1)
       d) len("fonction")
       e) int("12") * 2
       f) type(len("abc"))

4. Sans exécuter : que vaut max(len("chat"), len("éléphant"), len("ours")) ?
"""


##########################################
#  Fonctions définies par l'utilisateur  #
##########################################

"""
5. Sans exécuter : qu'affiche ce programme, et dans quel ordre ?
       def dire_bonjour():
           print("Bonjour !")

       print("Début")
       dire_bonjour()
       print("Fin")
       dire_bonjour()

6. Écrivez une fonction afficher_ligne() qui affiche une ligne de 20 tirets
   ("--------------------"). Appelez-la deux fois.

7. Que se passe-t-il si l'on appelle une fonction AVANT de l'avoir définie ?
   Écrivez l'appel dans un try … except, comme dans le cours, pour voir le
   message d'erreur.
"""


################################
#  Où s'arrête une fonction ?  #
################################

"""
8. Sans exécuter : qu'affiche ce programme ? Combien de lignes font partie
   de la fonction ?
       def f():
           print("A")
           print("B")
       print("C")
       f()
"""


#####################################
#  Pourquoi écrire des fonctions ?  #
#####################################

"""
9. Le programme suivant convertit trois températures de Celsius en
   Fahrenheit (F = C × 9 / 5 + 32) en répétant la même formule. Réécrivez-le
   avec une fonction celsius_vers_fahrenheit(c) qui RETOURNE le résultat.
       print(20 * 9 / 5 + 32)
       print(37 * 9 / 5 + 32)
       print(-10 * 9 / 5 + 32)
"""


################################
#  Fonctions avec paramètres   #
################################

"""
10. Écrivez une fonction saluer(prenom) qui affiche "Bonjour, <prenom> !".

11. Écrivez une fonction afficher_rectangle(largeur, hauteur) qui affiche un
    rectangle d'étoiles. Par exemple, afficher_rectangle(4, 2) affiche :
        ****
        ****

12. Sans exécuter : qu'affiche ce programme ?
        def presenter(nom, age):
            print(nom, "a", age, "ans")

        presenter("Léa", 12)
        presenter(30, "Tom")
"""


###########################
#  Le mot-clé "return"    #
###########################

"""
13. Écrivez une fonction carre(x) qui RETOURNE x au carré. Utilisez-la pour
    calculer carre(3) + carre(4).

14. Sans exécuter : que valent a et b ?
        def double(x):
            return 2 * x

        def double_affiche(x):
            print(2 * x)

        a = double(5)
        b = double_affiche(5)

15. Écrivez une fonction est_pair(n) qui retourne True si n est pair, False
    sinon. Utilisez-la dans une boucle pour afficher les nombres pairs de 1
    à 10.

16. Écrivez une fonction valeur_absolue(x) qui retourne la valeur absolue de
    x, SANS utiliser abs(). Utilisez deux "return".

17. Sans exécuter : qu'affiche ce programme ? Pourquoi "fin" n'est-il jamais
    affiché ?
        def premier_negatif():
            for n in range(5, -5, -1):
                if n < 0:
                    return n
            print("fin")

        print(premier_negatif())

18. Écrivez une fonction compter_lettre(texte, lettre) qui retourne le nombre
    de fois où lettre apparaît dans texte, avec une boucle (sans .count()).

19. Écrivez une fonction factorielle(n) qui retourne 1 × 2 × … × n. Que doit
    retourner factorielle(0) ?
"""


################################
#  Prototype d'une fonction    #
################################

"""
20. Écrivez le prototype (la ligne "def" seule, avec une docstring qui
    explique ce que fait la fonction) d'une fonction qui calcule le prix TTC
    à partir d'un prix hors taxes et d'un taux de TVA. Complétez ensuite son
    corps, et affichez sa docstring avec __doc__.

21. Ajoutez des annotations de type à la fonction de l'exercice 20.
    Les annotations empêchent-elles d'appeler la fonction avec des
    arguments d'un autre type ? Vérifiez.
"""
