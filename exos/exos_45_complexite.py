################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Claude Opus 5.5 - 2026                #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 45     #  Complexité algorithmique : exercices                        #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", comptez les opérations dans
votre tête (ou sur papier) avant de lancer le code.

Les corrigés sont dans le fichier corrs/corr_45_complexite.py.
"""


#######################################
#  Compter les opérations, notation O  #
#######################################

"""
1. Sans exécuter : simplifiez ces coûts avec la notation O.
       a) 5n + 3
       b) n² + 1000n
       c) 42
       d) 2n³ + n²
       e) n/2 + log₂(n)
       f) 3 × 2^n + n¹⁰

2. Vrai ou faux ?
       a) Un algorithme O(n) est toujours plus rapide qu'un algorithme O(n²).
       b) Si un algorithme O(n²) met 1 seconde pour n = 1000, il mettra
          environ 4 secondes pour n = 2000.
       c) O(2n) et O(n) désignent la même complexité.
       d) log₂(1 milliard) est environ égal à 30.

3. Un programme O(n) met 2 secondes pour traiter 1 million de lignes.
   Combien de temps environ pour 10 millions de lignes ? Et si le programme
   était O(n²) (avec les mêmes 2 secondes pour 1 million) ?
"""


##########################
#  Analyser une boucle   #
##########################

"""
4. Sans exécuter : combien de fois la ligne "compteur += 1" est-elle
   exécutée, en fonction de n ? Donnez la complexité de chaque fonction.

       def a(n):
           compteur = 0
           for i in range(n):
               for j in range(10):
                   compteur += 1
           return compteur

       def b(n):
           compteur = 0
           for i in range(n):
               compteur += 1
           for j in range(n):
               for k in range(n):
                   compteur += 1
           return compteur

       def c(n):
           compteur = 0
           i = 1
           while i < n:
               compteur += 1
               i = i * 2
           return compteur

       def d(n):
           compteur = 0
           for i in range(n):
               j = n
               while j > 1:
                   compteur += 1
                   j = j // 2
           return compteur

   Vérifiez ensuite en appelant chaque fonction avec n = 16 et n = 1024.

5. Quelle est la complexité de cette fonction ? Où se cache la boucle
   "invisible" ? Réécrivez-la pour qu'elle soit en O(n).

       def sans_doublons(valeurs):
           resultat = []
           for v in valeurs:
               if v not in resultat:
                   resultat.append(v)
           return resultat

   (Conseil : gardez l'ordre d'apparition des valeurs, en utilisant un set
   en plus de la liste.)
"""


#####################################
#  Complexité des opérations Python  #
#####################################

"""
6. Pour chaque opération, donnez sa complexité (n = taille de la
   structure) :
       a) liste[500]
       b) liste.append(x)
       c) liste.insert(0, x)
       d) x in liste
       e) x in un_set
       f) d["cle"]
       g) sorted(liste)
       h) liste[10:20]
       i) len(liste)

7. On reçoit chaque jour une liste de 100 000 identifiants de clients, et
   on veut savoir lesquels sont des clients "premium" (une liste de 50 000
   identifiants). Écrivez une fonction clients_premium(clients, premium) qui
   renvoie la liste des clients premium, en O(n + m). Testez-la sur de
   petites listes.

8. Écrivez une fonction construire_csv(lignes) qui reçoit une liste de
   listes de nombres et renvoie le texte CSV correspondant (valeurs
   séparées par des virgules, lignes séparées par "\n"), SANS concaténer de
   chaîne dans une boucle avec "+".
       construire_csv([[1, 2], [3, 4]])  => "1,2\n3,4"
"""


####################################################
#  Recherche linéaire et recherche dichotomique   #
####################################################

"""
9. Sans exécuter : combien d'étapes, au maximum, faut-il à une recherche
   dichotomique dans une liste triée de :
       a) 16 éléments ?   b) 1000 éléments ?   c) 1 million d'éléments ?
       d) 1 milliard d'éléments ?

10. Écrivez une fonction recherche_dichotomique(liste, cible) qui renvoie
    l'indice de la cible dans la liste triée, ou -1 si elle est absente.
    Testez-la sur [3, 8, 15, 21, 42, 57, 60] avec 42, 3, 60 et 10.

11. Modifiez votre fonction pour qu'elle AFFICHE la zone de recherche
    (gauche, droite) à chaque étape. Faites-la tourner sur l'exemple
    précédent avec la cible 10.

12. On doit chercher 1000 valeurs dans une liste de 1 million d'éléments
    non triée. Que vaut-il mieux faire :
        a) 1000 recherches linéaires ?
        b) trier la liste, puis faire 1000 recherches dichotomiques ?
        c) construire un set, puis faire 1000 tests "in" ?
    Estimez le nombre d'opérations de chaque solution.
"""


#########################
#  Algorithmes de tri   #
#########################

"""
13. Le tri à bulles : on parcourt la liste en échangeant chaque paire
    d'éléments voisins mal ordonnés ; après un passage, le plus grand
    élément est à la fin. On recommence n - 1 fois.
    Écrivez une fonction tri_bulles(liste) qui renvoie (liste_triée,
    nombre_de_comparaisons), sans modifier la liste d'origine.
    Testez-la sur [5, 1, 4, 2, 8]. Quelle est sa complexité ?

14. Améliorez tri_bulles : si un passage complet ne fait AUCUN échange, la
    liste est triée et on peut s'arrêter. Combien de comparaisons sur une
    liste déjà triée de 1000 éléments ? Quelle est la complexité dans le
    meilleur cas ?

15. Sans exécuter : pour trier 1 million d'éléments, combien de comparaisons
    environ font :
        a) un tri par sélection (n(n-1)/2) ?
        b) sorted() (environ n × log₂(n)) ?
"""


################################
#  Récursivité et complexité   #
################################

"""
16. Sans exécuter : quelle est la complexité de ces fonctions récursives ?

        def somme(liste):
            if not liste:
                return 0
            return liste[0] + somme(liste[1:])

        def puissance_rapide(x, n):
            if n == 0:
                return 1
            moitie = puissance_rapide(x, n // 2)
            if n % 2 == 0:
                return moitie * moitie
            return moitie * moitie * x

    (Attention, pour somme() : que coûte liste[1:] ?)

17. Écrivez une version de puissance_rapide qui compte ses appels (avec
    une variable globale, cf. chap. 19), et comparez avec le nombre de
    multiplications d'une boucle naïve, pour x = 2 et n = 1000.
"""


#############################
#  Mémoire et mesures       #
#############################

"""
18. Quelle est la complexité en MÉMOIRE de :
        a) sum([x ** 2 for x in range(n)])
        b) sum(x ** 2 for x in range(n))
        c) a_des_doublons_rapide du chapitre (avec un set)

19. Avec timeit, mesurez le temps de "x in liste" et de "x in un_set" pour
    des structures de 1 000, 10 000 et 100 000 éléments (x étant le dernier
    élément). Comment évoluent les temps quand n est multiplié par 10 ?

20. Problème : on a une liste de températures journalières et on veut, pour
    chaque jour, la moyenne des 7 derniers jours (moyenne "glissante").
        a) Écrivez une version simple qui recalcule la somme des 7 valeurs
           à chaque jour. Quelle est sa complexité si la fenêtre fait k
           jours ?
        b) Écrivez une version en O(n) qui met à jour la somme : on ajoute
           la nouvelle valeur et on retire celle qui sort de la fenêtre.
    Testez sur [10, 12, 11, 13, 15, 14, 16, 18, 17] avec une fenêtre de 3
    jours (les deux premiers jours n'ont pas de moyenne).
"""
