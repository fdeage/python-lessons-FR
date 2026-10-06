################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2024                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 24     #  Les listes (II) : exercices                                 #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier.

Les corrigés sont dans le fichier corr_24_listes_2.py.
"""


#########################
#  Fonctions intégrées  #
#########################

"""
1. Sans exécuter, que vaut chaque expression ?
       len([3, [1, 2], "abc"])
       max([4, 18, 7])
       min(["kiwi", "abricot", "pomme"])
       sum([0.5, 1.5, 2])
       sum([])
       list(enumerate("ab"))
       list(zip([1, 2, 3], "xy"))

2. Sans exécuter, lesquelles de ces lignes soulèvent une erreur ? Laquelle ?
   Vérifiez en protégeant chaque ligne avec try: … except …: (cf. chap. 26
   pour les détails, mais vous connaissez déjà la syntaxe).
       max([])
       sum(["1", "2"])
       min([3, "3"])

3. Les températures d'une semaine sont :
       temperatures = [14, 17, 21, 19, 12, 9, 15]
   Affichez la température minimale, maximale, l'amplitude (max - min) et la
   moyenne (arrondie à 1 décimale, cf. chap. 6).

4. Avec enumerate(), affichez les jours de la semaine numérotés à partir de 1 :
       1. lundi
       2. mardi
       …
   (jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi",
   "dimanche"])

5. Avec zip(), affichez chaque jour avec sa température (exercice 3) :
       lundi : 14°C
       …
"""


######################################
#  Autres façons de créer une liste  #
######################################

"""
6. Sans exécuter, que vaut chaque expression ?
       ["-"] * 3
       [0, 1] * 2
       list(range(10, 0, -3))
       list("2024")
       list((True, False))
       "a,b,,c".split(",")

7. Créez une liste de 26 compteurs à zéro (un par lettre de l'alphabet), puis
   affichez sa longueur.
"""


#########################
#  Parcourir une liste  #
#########################

"""
8. Sans exécuter, que vaut prix à la fin ? Pourquoi ?
       prix = [10, 20, 30]
       for p in prix:
           p = p * 2

9. Doublez réellement chaque élément de prix = [10, 20, 30] "sur place"
   (la liste elle-même doit être modifiée).

10. On a les ventes de 6 mois consécutifs :
        ventes = [120, 135, 128, 150, 149, 170]
    Affichez, pour chaque mois à partir du 2e, s'il est en "hausse" ou en
    "baisse" par rapport au mois précédent.

11. Avec une boucle while, trouvez l'indice du premier mot de plus de 6
    lettres de ["chat", "lapin", "hippopotame", "crocodile"]. Votre programme
    ne doit pas planter si aucun mot ne convient : testez-le aussi avec
    ["a", "b"].

12. Le programme suivant veut supprimer toutes les notes inférieures à 10,
    mais il est faux. Pourquoi ? Corrigez-le.
        notes = [8, 9, 14, 7, 12]
        for n in notes:
            if n < 10:
                notes.remove(n)
        print(notes)
"""


##############
#  Matrices  #
##############

"""
On représente une grille de morpion par une matrice 3 × 3 :
    grille = [["X", "O", "X"],
              [" ", "X", "O"],
              ["O", " ", "X"]]

13. Sans exécuter, que valent grille[1][2], grille[2][0], len(grille) et
    len(grille[0]) ?

14. Affichez la grille ligne par ligne, avec les cases séparées par "|" :
        X|O|X
         |X|O
        O| |X

15. Comptez le nombre de cases vides (" "), puis affichez les coordonnées
    (ligne, colonne) de chacune.

16. Vérifiez si le joueur "X" a gagné sur la diagonale principale (cases
    [0][0], [1][1] et [2][2]).

17. Sans exécuter, qu'affiche ce programme ? Pourquoi ? Corrigez la création
    de la matrice.
        m = [[0] * 2] * 2
        m[0][1] = 5
        print(m)
"""


###################
#  Tri de listes  #
###################

"""
18. Sans exécuter, qu'affiche ce programme ?
        l = [3, 1, 2]
        print(sorted(l))
        print(l)
        print(l.sort())
        print(l)

19. Triez la liste ["Zoé", "adam", "Léa", "bob"] :
        a) dans l'ordre par défaut (pourquoi ce résultat ?),
        b) sans tenir compte des majuscules,
        c) par longueur de prénom, de la plus longue à la plus courte.

20. On a une liste d'élèves sous forme de tuples (nom, âge, moyenne) :
        classe = [("Ana", 17, 14.5), ("Bob", 16, 12.0), ("Chloé", 17, 16.0)]
    Triez-la par moyenne décroissante, en écrivant une fonction qui sera
    passée au paramètre key. Affichez ensuite le nom du premier.

21. Écrivez une fonction mediane(nombres) qui retourne la médiane d'une liste
    de nombres (la valeur "du milieu" une fois la liste triée ; si la liste a
    un nombre pair d'éléments, la moyenne des deux valeurs du milieu). La
    liste passée en argument ne doit PAS être modifiée.
        mediane([3, 1, 2])     → 2
        mediane([4, 1, 3, 2])  → 2.5
"""


######################################
#  D'autres méthodes sur les listes  #
######################################

"""
22. Sans exécuter, que vaut l après chaque ligne, et qu'affiche chaque
    print() ?
        l = ["a", "b", "c", "b"]
        l.insert(1, "z")
        l.remove("b")
        print(l.pop(0))
        print(l.index("b"))
        print(l.count("b"))
        print(l.append("d"))

23. Écrivez une fonction retirer_tout(liste, valeur) qui supprime TOUTES les
    occurrences de valeur dans liste (en modifiant la liste), en utilisant
    .count() et .remove().

24. Une file d'attente : on part de file = ["Ana", "Bob"]. Simulez :
        - "Chloé" arrive (en fin de file),
        - "Djamel" a un coupe-file et se place en tête,
        - la première personne est servie (affichez son nom),
        - "Bob" quitte la file,
    puis affichez la file.
"""


##########################
#  Bonus sur les listes  #
##########################

"""
25. Sans exécuter, qu'affiche ce programme ?
        a = [1, 2]
        b = a
        c = a.copy()
        b.append(3)
        print(a, b, c)
        print(a is b, a is c, a == b)

26. Sans exécuter, que valent ces comparaisons ?
        [1, 2] == [2, 1]
        [2, 1] > [1, 9, 9]
        ["b"] < ["a", "z"]

27. Sans exécuter, que valent premier, milieu et dernier ?
        premier, *milieu, dernier = [5, 10, 15, 20, 25]

28. Transformez la liste [2024, 3, 15] en la string "2024-3-15".
"""
