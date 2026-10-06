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
#  Chap. 17     #  Les tuples : exercices                                      #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier.

Les corrigés sont dans le fichier corrs/corr_17_tuples.py.
"""


############################
#  Définition et création  #
############################

"""
1. Sans exécuter : quel est le type de chaque valeur ?
       (5)
       (5,)
       ()
       ("a")
       ("a",)
       tuple("ab")
   Et que vaut x après l'instruction x = 5, ?

2. Ce programme devait afficher 25.0, mais il affiche autre chose. Sans
   exécuter, qu'affiche-t-il ? Trouvez le bug et corrigez-le.
       prix = 12.5,
       total = prix * 2
       print(total)

3. Créez un tuple point qui représente le point de coordonnées x = 3 et
   y = -2, puis affichez "x = 3, y = -2" en accédant à ses éléments.
"""


########################
#  Intérêt des tuples  #
########################

"""
4. Pour chacune de ces données, choisiriez-vous une liste ou un tuple ?
   Pourquoi ?
       a) les notes d'un élève, qui s'ajoutent au fil de l'année
       b) les coordonnées GPS d'une ville (latitude, longitude)
       c) une date de naissance (jour, mois, année)
       d) le contenu d'un panier sur un site marchand
       e) une couleur au format (rouge, vert, bleu)

5. Écrivez une fonction min_max(nombres) qui parcourt une liste de nombres
   avec une boucle (sans utiliser min() ni max()) et retourne À LA FOIS le
   plus petit et le plus grand nombre. Récupérez le résultat dans deux
   variables, puis affichez-les.

6. Écrivez une fonction division(a, b) qui retourne le quotient et le reste
   de la division euclidienne de a par b (cf. chap. 4). Testez-la avec 17
   et 5, en récupérant le résultat dans deux variables q et r.
"""


########################
#  Opérations de base  #
########################

"""
7. Sans exécuter : avec t = (4, 8, 15, 16, 23, 42), que vaut chaque
   expression ?
       t[2]
       t[-1]
       len(t)
       15 in t
       t.index(16)
       t.count(4)
       sum(t)
       max(t)

8. Sans exécuter : que vaut chaque expression ?
       (1, 2) + (3,)
       ("ab",) * 3
       (0,) * 0
       ((1, 2),) + (3, 4)

9. Sans exécuter : avec t = (4, 8, 15, 16, 23, 42), lesquelles de ces
   expressions soulèvent une erreur ? Laquelle ? Vérifiez en protégeant
   chaque ligne avec try: … except …: (vu au chap. 1, détaillé au chap. 26).
       t + (5,)
       t + 5
       t[10]
       t.index(99)

10. Sans exécuter : qu'affiche ce programme ?
        a, b, c = 1, 2, 3
        a, b, c = b, c, a
        print(a, b, c)
"""


########################
#  Parcourir un tuple  #
########################

"""
11. Avec etapes = ("Paris", "Lyon", "Marseille"), affichez :
        Étape 1 : Paris
        Étape 2 : Lyon
        Étape 3 : Marseille

12. Un panier est une liste de tuples (nom, prix unitaire, quantité) :
        panier = [("stylo", 1.5, 4), ("cahier", 2.5, 2), ("sac", 24.0, 1)]
    Affichez le prix de chaque ligne ("stylo : 6.0 €"…), puis le total du
    panier.

13. Avec eleves = [("Alice", 15), ("Bob", 12), ("Chloé", 18), ("Dan", 9)],
    trouvez et affichez le nom de l'élève qui a la meilleure note.
"""


#############################
#  Déballage ("unpacking")  #
#############################

"""
14. Sans exécuter : que valent les variables après chaque ligne ?
        a, *b = "hello"
        *debut, fin = (1, 2, 3)
        x, (y, z) = 1, (2, 3)
        _, milieu, _ = (7, 8, 9)

15. Sans exécuter : lesquelles de ces lignes soulèvent une erreur ?
        a, b = (1, 2, 3)
        a, b, c = "ab"
        a, b = "ab"

16. Écrivez une fonction premier_et_dernier(sequence) qui retourne le premier
    et le dernier élément d'une liste, d'un tuple ou d'une string. Testez-la
    sur [3, 1, 4, 1, 5] et sur "Python", en déballant le résultat.
"""


#########################
#  Comparer des tuples  #
#########################

"""
17. Sans exécuter : que vaut chaque comparaison ?
        (1, 2) == (2, 1)
        (3, 1) < (2, 9)
        ("Dupont", "Marie") < ("Dupont", "Paul")
        (1, 2) < (1, 2)
        (0,) < (0, 0)
        (5, 2) == [5, 2]

18. Des dates sont stockées sous la forme (année, mois, jour) :
        dates = [(2024, 3, 15), (2023, 12, 1), (2024, 1, 30)]
    Trouvez la date la plus ancienne avec une boucle et "<", puis vérifiez
    votre résultat avec min(dates). Pourquoi min() fonctionne-t-il ?
"""


#######################
#  Modifier un tuple  #
#######################

"""
19. Sans exécuter : qu'affiche ce programme ? La dernière ligne provoque-t-elle
    une erreur ?
        t = (1, [2, 3])
        t[1].append(4)
        print(t)
        t = t + (5,)
        print(t)
        t[0] = 0

20. On a la couleur orange = (255, 128, 0). "Modifiez" sa 2e composante
    (128) en 64, de deux façons :
        a) en construisant directement un nouveau tuple avec les indices,
        b) en passant par une liste (list() puis tuple()).
"""


########################################
#  Conversions entre listes et tuples  #
########################################

"""
21. Sans exécuter : que vaut chaque expression ?
        list((1, 2))
        tuple([3])
        tuple("hey")
        list(tuple("ab"))
        tuple(range(3))

22. Écrivez une fonction ajouter_note(notes, note) qui reçoit un TUPLE de
    notes et retourne un nouveau tuple avec la note ajoutée à la fin. Vérifiez
    que le tuple de départ n'a pas changé.
"""
