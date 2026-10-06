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
#  Chap. 12     #  if, then, else et elif : exercices                          #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Changez les valeurs des variables pour tester TOUS les cas de vos
conditions (chaque branche "if", "elif" et "else").

Les corrigés sont dans le fichier corrs/corr_12_if_then.py.
"""


##############
#  FizzBuzz  #
##############

"""
Cet exercice se compose de cinq parties.

0. Écrire du code qui affiche si un nombre est pair, et sinon ne fait rien.

1. Écrire du code qui teste si un nombre est un multiple de 3 ou de 5, et
   affiche le texte correspondant ("... est multiple de ...").

2. Écrire du code qui teste si un nombre est un multiple de 3, de 5 ou de 15.
   Concernant le texte affiché :
     - au lieu de "est multiple de 3", on affiche "Fizz"
     - au lieu de "est multiple de 5", on affiche "Buzz"
     - au lieu de "est multiple de 15", on affiche "FizzBuzz"

   De combien de conditions avez-vous besoin ?

Les parties 3 et 4 nécessitent une boucle : revenez-y après le chap. 13.

3. Écrire du code qui teste les entiers de 1 à 100, et affiche :
    - Fizz si le nombre est multiple de 3,
    - Buzz si le nombre est multiple de 5,
    - FizzBuzz si le nombre est multiple de 15,
    - le nombre lui-même dans les autres cas.

4. Écrire du code qui calcule la somme des nombres inférieurs ou égaux à 100
   qui sont multiples de 3, 5 ou 15.
"""


#########################
#  La structure "if"    #
#########################

"""
5. Sans exécuter : qu'affiche ce programme ?
       temperature = 25
       if temperature > 30:
           print("Il fait très chaud")
       print("Bonne journée")

6. On pose : mot = "python". Écrivez un "if" qui affiche "Mot court" si le mot
   contient moins de 5 lettres. Qu'affiche votre programme ? Testez avec
   mot = "go".

7. Écrivez un "if" qui affiche "Âge valide" si une variable age est comprise
   entre 0 et 120 (bornes incluses). Utilisez une comparaison "encadrée".

8. Sans exécuter : lesquels de ces "if" affichent quelque chose ?
       if 0: print("A")
       if 42: print("B")
       if "": print("C")
       if "False": print("D")
       if 0.0: print("E")
"""


#######################
#  Le mot-clé "else"  #
#######################

"""
9. Écrivez un programme qui affiche "majeur" ou "mineur" selon la valeur d'une
   variable age.

10. Un magasin offre la livraison pour toute commande d'au moins 50 €. Selon
    la valeur d'une variable montant, affichez "Livraison offerte" ou
    "Il manque … € pour la livraison offerte" (avec la somme manquante).

11. Écrivez un programme qui affiche la valeur absolue d'un nombre x, SANS
    utiliser abs().
"""


#######################
#  Le mot-clé "elif"  #
#######################

"""
12. Selon la valeur d'une variable temperature (en °C), affichez :
       - "glace" en dessous de 0 (exclu),
       - "eau" entre 0 et 100 (exclu),
       - "vapeur" à partir de 100.

13. Le programme suivant est censé afficher la mention d'une note sur 20, mais
    il affiche "passable" pour une note de 17. Pourquoi ? Corrigez-le.
        note = 17
        if note >= 10:
            print("passable")
        elif note >= 12:
            print("assez bien")
        elif note >= 14:
            print("bien")
        elif note >= 16:
            print("très bien")
        else:
            print("recalé")

14. Sans exécuter : que vaut x à la fin de chacun de ces deux programmes ?
        x = 5                        x = 5
        if x > 3:                    if x > 3:
            x = x + 10                   x = x + 10
        elif x > 10:                 if x > 10:
            x = x * 2                    x = x * 2
"""


#####################################
#  Indentation et "if" imbriqués    #
#####################################

"""
15. Sans exécuter : qu'affiche ce programme pour a = 5 ? Et pour a = -5 ?
        a = 5
        if a > 0:
            print("positif")
            if a > 10:
                print("grand")
        print("fin")

16. Une année est bissextile si elle est divisible par 4, SAUF si elle est
    divisible par 100, À MOINS qu'elle soit divisible par 400. Écrivez un
    programme qui affiche si une année est bissextile, d'abord avec des "if"
    imbriqués, puis avec une seule condition (and, or, not).
    Testez avec 2024 (oui), 1900 (non), 2000 (oui) et 2023 (non).

17. Récrivez ce code SANS "if" imbriqué, avec une seule condition :
        if age >= 18:
            if pays == "France":
                print("Vous pouvez voter en France")
"""


########################################
#  Le mot-clé "pass" et pièges         #
########################################

"""
18. Vous voulez écrire la structure d'un programme, mais vous ne savez pas
    encore quoi faire quand la commande est vide. Écrivez le "if" avec "pass",
    pour que le code s'exécute sans erreur.

19. Trouvez les erreurs dans chacun de ces "if" (sans les exécuter : ils
    empêcheraient le fichier de se lancer, ou donneraient un résultat faux) :
        if x == 3            # a.
            print("trois")
        if x = 3:            # b.
            print("trois")
        if fruit == "pomme" or "poire":   # c.
            print("fruit à pépins")
        saisie = input("Âge ? ")          # d.
        if saisie >= 18:
            print("majeur")
"""


################################
#  Les "one-liner" avec if     #
################################

"""
20. Récrivez ces quatre lignes en une seule, avec une expression
    conditionnelle :
        if note >= 10:
            resultat = "admis"
        else:
            resultat = "ajourné"

21. Sans exécuter : que vaut y ?
        x = 7
        y = "pair" if x % 2 == 0 else "impair"

22. Affichez "1 chat" ou "N chats" selon la valeur d'une variable nb_chats,
    avec un seul print() et une expression conditionnelle.
"""
