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
#  Chap. 23     #  Itérables & compréhensions : exercices                      #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier.

Les corrigés sont dans le fichier corrs/corr_23_iter_compr.py.

Comme dans le chapitre, certains exercices utilisent un fichier : on le crée
ci-dessous (ne vous souciez pas de ce code, cf. chap. 28), et on le supprime à
la toute fin du fichier.
"""
with open("courses.txt", "w") as fichier:
    fichier.write("pain\nlait\noeufs\nchocolat\nlait\npommes\n")


###################
#  Les itérables  #
###################

"""
1. Sans exécuter, qu'affiche chacune de ces boucles ?
       for x in (1, 2):
           print(x * 3)

       for c in "oui":
           print(c + c)

       for cle in {"a": 1, "b": 2}:
           print(cle)

2. Sans exécuter, que valent ces expressions ?
       "ch" in "chat"
       "ac" in "chat"
       3 in range(3)
       "b" in {"a": "b"}
       "a" in {"a": "b"}
       sum(range(5))
       list("123")
       max("abricot")

3. Le fichier "courses.txt" (créé en haut de ce fichier) contient une liste de
   courses, un article par ligne. Avec une boucle for sur open("courses.txt"),
   affichez chaque article SANS ligne vide entre deux articles (deux méthodes
   possibles : le paramètre end de print(), ou la méthode .strip()).

4. Toujours avec une boucle for sur le fichier, comptez le nombre de lignes de
   "courses.txt" (sans utiliser len()).
"""


#########################################
#  Bonus : comment fonctionne "for" ?  #
#########################################

"""
5. Sans exécuter, qu'affiche ce programme ?
       it = iter("abc")
       print(next(it))
       print(next(it))
       print(list(it))
       print(list(it))

6. Réécrivez la boucle suivante SANS "for", avec iter(), next(), while et
   try: … except StopIteration: … (cf. le chapitre) :
       for nombre in [10, 20, 30]:
           print(nombre + 1)
"""


###################################
#  Compréhensions sur des listes  #
###################################

"""
7. Avec une compréhension, créez :
       a) la liste des 10 premiers multiples de 7 : [0, 7, 14, …, 63],
       b) la liste des longueurs des mots de ["un", "deux", "trois"],
       c) la liste des mots de ["Paris", "lyon", "NICE"] écrits en minuscules,
       d) la liste des nombres de ["3", "14", "15"] convertis en entiers,
       e) la liste des carrés de 1 à 10, en utilisant une fonction carre(x)
          que vous définirez.

8. Traduisez cette boucle en compréhension, puis vérifiez que les deux listes
   sont égales avec "==" :
       resultat = []
       for i in range(1, 6):
           resultat.append(i * 10 + 1)

9. Traduisez cette compréhension en boucle for avec .append() :
       initiales = [prenom[0] for prenom in ["Ada", "Grace", "Alan"]]

10. Avec une compréhension sur open("courses.txt"), créez la liste des
    articles sans leur "\n" final.
"""


########################################
#  Conditions sur les compréhensions  #
########################################

"""
11. Sans exécuter, que valent ces listes ?
        [x for x in range(10) if x % 3 == 0]
        [x * 2 for x in [1, -2, 3, -4] if x > 0]
        ["+" if x > 0 else "-" for x in [1, -2, 3, -4]]
        [c for c in "programmation" if c not in "aeiouy"]

12. Avec une compréhension et une condition, créez :
        a) la liste des nombres impairs entre 1 et 20,
        b) la liste des mots de plus de 4 lettres de
           ["chat", "éléphant", "rat", "girafe", "ours"],
        c) la liste des notes au-dessus de la moyenne de
           [12, 8, 15, 9, 17, 11] (calculez d'abord la moyenne).

13. À partir de temperatures = [3, -2, 0, 7, -5, 12], créez une nouvelle liste
    de même longueur où les températures négatives sont remplacées par 0.
    Faut-il un "if" à droite ou un "if … else …" à gauche ? Pourquoi ?

14. Corrigez cette compréhension, qui crée une SyntaxError (ne la décommentez
    pas telle quelle, sinon tout le fichier refuserait de s'exécuter) :
        # [x for x in range(5) if x > 2 else 0]
"""


#####################################
#  Compréhensions sur des matrices  #
#####################################

"""
On utilise la matrice suivante :
    notes = [[12, 15, 9], [8, 11, 14], [17, 13, 16]]
Chaque ligne contient les trois notes d'un élève.

15. Avec une compréhension, créez :
        a) la liste des premières notes de chaque élève : [12, 8, 17],
        b) la liste des moyennes de chaque élève,
        c) la liste des meilleures notes de chaque élève (avec max()).

16. Avec une compréhension imbriquée, créez la matrice des notes augmentées
    d'un point (en gardant la forme de la matrice).

17. Avec une compréhension imbriquée, créez la table de multiplication de 1 à
    5 sous forme de matrice : [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], …].
"""


#############################
#  Compréhensions chaînées  #
#############################

"""
18. Sans exécuter, que vaut cette liste ? Combien a-t-elle d'éléments ?
        [a + b for a in "xy" for b in "123"]

19. Avec des for chaînés, "aplatissez" la matrice notes de l'exercice 15 en une
    seule liste de 9 notes, puis calculez la moyenne de la classe.

20. Un dé a 6 faces. Avec une compréhension à deux for et une condition,
    créez la liste des couples (d1, d2) de deux dés dont la somme vaut 7.
    Combien y en a-t-il ?
"""


#############################
#  Compréhensions avancées  #
#############################

"""
21. Avec une compréhension de dictionnaire, créez un dictionnaire qui associe
    à chaque nombre de 1 à 5 son cube : {1: 1, 2: 8, …}.

22. À partir de la liste fruits = ["pomme", "kiwi", "banane"], créez avec une
    compréhension de dictionnaire le dictionnaire {fruit: nombre de lettres}.

23. Avec une expression génératrice passée à sum(), calculez la somme des
    carrés des nombres pairs de 0 à 100.

24. Sans exécuter, que vaut chaque ligne ?
        gen = (x + 1 for x in range(3))
        print(list(gen))
        print(list(gen))
"""


################################################
#  Quand (ne pas) utiliser une compréhension ?  #
################################################

"""
25. Pour chacune de ces tâches, utiliseriez-vous une compréhension ou une
    boucle for classique ? Pourquoi ?
        a) afficher chaque élément d'une liste avec print(),
        b) créer la liste des prix TTC à partir de la liste des prix HT,
        c) lire un fichier, et pour chaque ligne : la découper, convertir
           plusieurs valeurs, vérifier qu'elles sont valides, et les ajouter à
           trois listes différentes,
        d) garder uniquement les adresses e-mail qui contiennent "@".
"""


# Nettoyage : on supprime le fichier créé au début (cf. chap. 22 et 28)
import os
os.remove("courses.txt")
