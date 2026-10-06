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
#  Chap. 16     #  Les listes (I) : exercices                                  #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier.

Les corrigés sont dans le fichier corrs/corr_16_listes_1.py.

Ces exercices n'utilisent que les notions du chap. 16 et des chapitres
précédents. Les autres méthodes des listes (.sort(), .insert()…), enumerate()
et zip() sont au programme des exercices du chap. 24.
"""


########################
#  Déclarer une liste  #
########################

"""
1. Sans exécuter : combien d'éléments contient chacune de ces listes ?
       []
       [[]]
       [1, [2, 3], "abc"]
       ["a", "b", "c", ""]
       [[], [], []]

2. Créez une liste courses qui contient "pain", "lait" et "œufs", puis
   affichez la liste et son type.

3. Un programme utilise ces quatre variables :
       ville_1 = "Lyon"
       ville_2 = "Lille"
       ville_3 = "Nantes"
       ville_4 = "Brest"
   Remplacez-les par une seule liste villes, écrite sur plusieurs lignes (un
   élément par ligne), puis affichez-la.
"""


######################################
#  Accéder à une valeur de la liste  #
######################################

"""
4. Sans exécuter : avec notes = [12, 15, 8, 17, 10, 14], que vaut chaque
   expression ?
       notes[0]
       notes[3]
       notes[-1]
       notes[-2]
       notes[len(notes) - 1]
       notes[1] + notes[2]

5. Sans exécuter : avec m = [[1, 2, 3], [4, 5, 6]], que vaut chaque
   expression ?
       m[1]
       m[1][2]
       m[0][-1]
       len(m)
       len(m[0])

6. Sans exécuter : avec notes = [12, 15, 8, 17, 10, 14], lesquelles de ces
   expressions soulèvent une erreur ? Laquelle ? Vérifiez en protégeant
   chaque ligne avec try: … except …: (vu au chap. 1, détaillé au chap. 26).
       notes[6]
       notes[-6]
       notes[-7]
       [][0]

7. Sans exécuter : avec courses = ["pain", "lait", "œufs"], que vaut chaque
   expression ?
       "lait" in courses
       "Lait" in courses
       "pain" not in courses
       3 in [1, [3]]
       [3] in [1, [3]]

8. Écrivez un "if" qui affiche "Pensez au beurre !" si "beurre" n'est pas dans
   la liste courses.
"""


#####################################
#  Modifier une valeur de la liste  #
#####################################

"""
9. Sans exécuter : qu'affiche ce programme ?
       nombres = [1, 2, 3]
       nombres[0] = nombres[2]
       nombres[2] = 0
       print(nombres)

10. Échangez le premier et le dernier élément de la liste
        couleurs = ["rouge", "vert", "bleu", "jaune"]
    en utilisant les indices 0 et -1 (votre code doit fonctionner quelle que
    soit la longueur de la liste).

11. Sans exécuter : avec lettres = ["a", "b", "c"], lesquelles de ces lignes
    soulèvent une erreur ? Pourquoi ?
        lettres[-1] = "z"
        lettres[3] = "d"
        "abc"[0] = "z"
"""


##################################
#  Longueur d'une liste : len()  #
##################################

"""
12. Sans exécuter : que vaut chaque expression ?
        len([1, [2, 3], []])
        len([[]])
        len([""])
        len("abc")
        len(["abc"])

13. Avec animaux = ["chat", "chien", "lapin", "hamster"], affichez le dernier
    élément de deux façons différentes, puis l'avant-dernier.
"""


########################################################
#  .append(), .extend(), .pop(), del et l'opérateur +  #
########################################################

"""
14. Sans exécuter : qu'affiche ce programme ?
        a = [1]
        a.append(2)
        a.append([3, 4])
        a.extend([5])
        print(a, len(a))

15. Sans exécuter : qu'affiche ce programme ?
        x = [1, 2, 3]
        y = x.pop()
        z = x.append(9)
        print(x, y, z)

16. Sans exécuter : qu'affiche ce programme ?
        l = [10, 20, 30, 40]
        del l[1]
        print(l.pop(1))
        print(l)

17. Sans exécuter : qu'affiche ce programme ? Quelle est la différence entre
    "+" et .extend() ?
        a = [1, 2]
        b = a + [3]
        print(a, b)
        a.extend([3])
        print(a)

18. Une pile d'assiettes : partez d'une liste vide pile, posez les assiettes
    "bleue", "verte" puis "rouge" (chacune sur la précédente), puis retirez
    l'assiette du dessus. Affichez l'assiette retirée et la pile restante.

19. Ajoutez le nombre 0 AU DÉBUT de la liste nombres = [1, 2, 3], sans utiliser
    de méthode (indice : la concaténation, cf. "En bref" du chap. 16).
"""


####################################
#  Parcourir une liste avec "for"  #
####################################

"""
20. Affichez la liste de courses (exercice 2) sous cette forme :
        - pain
        - lait
        - œufs

21. Avec notes = [12, 15, 8, 17, 10, 14, 6], comptez le nombre de notes
    supérieures ou égales à 10.

22. Trouvez la plus grande note de la liste notes de l'exercice 21 SANS
    utiliser max() : parcourez la liste en gardant en mémoire la plus grande
    valeur rencontrée jusqu'ici.

23. Construisez la liste des carrés des entiers de 1 à 10 avec une boucle et
    .append(), puis affichez-la.

24. Écrivez une fonction moyenne(nombres) qui retourne la moyenne d'une liste
    de nombres, ou 0 si la liste est vide (cf. chap. 12 et 14). Testez-la
    avec [12, 15, 8] et [].

25. Écrivez une fonction mots_longs(mots, n) qui retourne une NOUVELLE liste
    contenant seulement les mots de plus de n lettres. Testez-la avec
    ["chat", "éléphant", "rat", "girafe"] et n = 4.

26. Écrivez une fonction inverser(liste) qui retourne une nouvelle liste avec
    les éléments dans l'ordre inverse, sans modifier la liste de départ.
    Indice : ajoutez chaque élément AU DÉBUT du résultat (exercice 19).
"""
