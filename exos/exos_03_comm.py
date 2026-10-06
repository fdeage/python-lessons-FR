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
#  Chap. 3      #  Commentaires : exercices                                    #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", notez d'abord votre réponse en
commentaire.

Les corrigés sont dans le fichier corrs/corr_03_comm.py.
"""


##########################
#  Commentaires simples  #
##########################

"""
1. Sans exécuter : parmi les lignes suivantes, lesquelles affichent quelque
   chose quand on exécute le fichier ? Qu'affichent-elles ?
       # print("A")
       print("B")  # print("C")
       print("D # E")
       #print("F")
   Recopiez-les sous cet énoncé et exécutez le fichier pour vérifier.

2. Écrivez un commentaire sur plusieurs lignes (avec des #) qui explique, en
   trois lignes, à quoi sert ce fichier.
"""


##################################
#  Commentaires en fin de ligne  #
##################################

"""
3. Écrivez un print() qui affiche le résultat de 6 * 7, suivi d'un commentaire
   de fin de ligne indiquant le résultat attendu, selon la convention du cours
   ("=>").

4. Le commentaire de fin de ligne suivant respecte-t-il la convention de la
   PEP 8 ? Corrigez-le si besoin.
       print(2 + 2)#=>4
"""


#######################
#  Commenter du code  #
#######################

"""
5. Les trois lignes ci-dessous (à recopier) affichent un compte à rebours.
   Commentez UNIQUEMENT la ligne du milieu, de façon à n'afficher que 3 et 1.
   Utilisez le raccourci clavier de votre éditeur.
       print(3)
       print(2)
       print(1)

6. La ligne suivante, si on la recopie telle quelle, empêche le fichier de
   s'exécuter (SyntaxError). Recopiez-la, puis commentez-la pour que le fichier
   s'exécute à nouveau :
       print("Il manque une parenthèse"
"""


######################################
#  Commentaires longs et docstrings  #
######################################

"""
7. Sans exécuter : qu'affiche le programme suivant ?
       '''print("Bonjour")'''
       print('''Au revoir''')

8. Quelle est la différence entre un commentaire avec # et une chaîne à
   triples guillemets ? Donnez deux conséquences pratiques.

9. Sans exécuter : le code suivant est-il valide ? Pourquoi ?
       print(5)  \"\"\"affiche cinq\"\"\"

10. Écrivez une docstring (sur une seule ligne) pour la fonction ci-dessous,
    puis affichez-la avec __doc__ (comme dans le cours) :
        def tripler(nombre):
            return nombre * 3
"""


###########################
#  Commentaires spéciaux  #
###########################

"""
11. À quoi sert la ligne #!/usr/bin/env python3 ? Où doit-elle se trouver ?

12. Laquelle de ces lignes est utile dans un fichier Python 3 moderne ?
        # -*- coding: utf-8 -*-
        # TODO : vérifier les arrondis
"""


#############################
#  Bien commenter son code  #
#############################

"""
13. Parmi ces commentaires, lesquels sont utiles ? Lesquels sont inutiles ?
    Pourquoi ?
        print(60 * 60 * 24)  # multiplie 60 par 60 par 24
        print(60 * 60 * 24)  # nombre de secondes dans une journée
        print(9.81 * 2)      # poids (en newtons) d'un objet de 2 kg sur Terre
        print(1 + 1)         # affiche 3

14. Ajoutez un commentaire UTILE au calcul suivant (il convertit 100 km/h en
    mètres par seconde) :
        print(100 * 1000 / 3600)
"""
