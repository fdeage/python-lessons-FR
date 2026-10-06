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
#  Chap. 36     #  Générateurs (et décorateurs) : exercices                    #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1), notez votre réponse, PUIS vérifiez avec print().

Attention aux générateurs infinis : n'appelez jamais list() dessus !

Les corrigés sont dans le fichier corr_36_generateurs.py.
"""


######################################
#  Rappel : itérables et itérateurs  #
######################################

"""
1. Sans exécuter : qu'affiche ce programme ? Quelle erreur obtient-on au
   dernier next() ?
       it = iter("abc")
       print(next(it), next(it))
       print(list(it))
       next(it)
"""


########################################
#  Les fonctions génératrices : yield  #
########################################

"""
2. Écrivez une fonction génératrice voyelles(texte) qui produit, une par une,
   les voyelles (a, e, i, o, u, y) d'un texte, en minuscules.
   list(voyelles("Data Science")) doit valoir ['a', 'a', 'i', 'e', 'e'].

3. Écrivez une fonction génératrice compte_a_rebours(n) qui produit n, n-1,
   …, 1, puis la chaîne "Décollage !".

4. Écrivez une fonction génératrice pairs(liste) qui produit les couples
   (élément, élément suivant) d'une liste.
   list(pairs([1, 2, 3, 4])) doit valoir [(1, 2), (2, 3), (3, 4)].

5. Sans exécuter : que vaut list(f()) ? Et list(g()) ?
       def f():
           for i in range(5):
               if i == 3:
                   return
               yield i

       def g():
           for i in range(5):
               if i == 3:
                   continue
               yield i
"""


#########################################
#  Pas à pas : une exécution suspendue  #
#########################################

"""
6. Sans exécuter : qu'affiche ce programme, ligne par ligne ?
       def gen():
           print("a")
           yield 1
           print("b")
           yield 2
           print("c")

       g = gen()
       print("créé")
       x = next(g)
       print(x)
       for v in g:
           print(v)
"""


############################
#  Un générateur s'épuise  #
############################

"""
7. Ce programme est censé afficher la moyenne des températures valides
   (non négatives), mais il affiche une erreur. Pourquoi ? Corrigez-le de
   deux façons différentes.
       temperatures = [21, -99, 23, 22, -99, 24]
       valides = (t for t in temperatures if t >= 0)
       print(sum(valides) / len(list(valides)))
"""


#########################
#  Générateurs infinis  #
#########################

"""
8. Écrivez un générateur infini puissances_de_2() qui produit 1, 2, 4, 8…
   Affichez les 10 premières valeurs avec itertools.islice.

9. Écrivez un générateur infini cycle_jours() qui produit "lun", "mar", …,
   "dim", puis recommence à "lun", indéfiniment. Utilisez-le avec zip() pour
   associer un jour à chacune des dates 1 à 10 d'un mois (qui commence un
   lundi).

10. Avec itertools.count et un break, trouvez le plus petit entier n tel
    que n * n dépasse 2 000.
"""


######################################
#  Évaluation paresseuse et mémoire  #
######################################

"""
11. Comparez avec sys.getsizeof() la taille de range(10), range(10_000_000),
    de la liste list(range(100_000)) et de l'expression génératrice
    (x for x in range(10_000_000)). Que remarquez-vous ? range est-il plutôt
    une liste ou un générateur ?

12. Créez un fichier "exo36_ventes.txt" contenant 1 000 lignes du type
    "vente;<numéro>;<montant>" où le montant vaut numéro % 50. Puis écrivez
    un générateur montants(chemin) qui lit le fichier LIGNE PAR LIGNE et
    produit chaque montant (en int). Calculez le total des ventes sans
    jamais charger tout le fichier. Supprimez le fichier à la fin.
"""


##############################
#  Pipelines de générateurs  #
##############################

"""
13. On reçoit des lignes de texte tapées par des humains :
        brut = ["  Paris ", "", "lyon", "MARSEILLE  ", "  ", "paris"]
    Écrivez trois générateurs, chacun avec une seule tâche :
        - nettoyer(lignes) : enlève les espaces autour,
        - non_vides(lignes) : ignore les lignes vides,
        - capitaliser(lignes) : met une majuscule initiale (.capitalize()).
    Branchez-les en pipeline, et affichez l'ensemble des villes distinctes
    (triées).

14. Écrivez un générateur par_paquets(iterable, taille) qui produit des
    listes de "taille" éléments (le dernier paquet peut être plus petit).
    list(par_paquets(range(7), 3)) doit valoir [[0, 1, 2], [3, 4, 5], [6]].
    Utile pour envoyer des données à une base de données par lots !
"""


##############################
#  Déléguer avec yield from  #
##############################

"""
15. Réécrivez cette fonction avec yield from :
        def chaine(a, b):
            for x in a:
                yield x
            for x in b:
                yield x

16. Écrivez un générateur récursif (cf. chap. 33) cles_imbriquees(d) qui
    produit toutes les clés d'un dictionnaire, y compris celles des
    dictionnaires imbriqués :
        config = {"base": {"nom": "x", "port": 5432}, "debug": True}
        list(cles_imbriquees(config)) == ['base', 'nom', 'port', 'debug']
    (isinstance(valeur, dict) teste si une valeur est un dictionnaire.)
"""


##############################
#  Expressions génératrices  #
##############################

"""
17. Avec une seule expression génératrice passée à sum(), calculez la somme
    des longueurs des mots de plus de 3 lettres de :
        phrase = "le python est un langage simple et efficace"

18. Sans exécuter : que vaut chacune de ces expressions ?
        any(x > 10 for x in [3, 8, 12])
        all(x > 10 for x in [])
        max((len(m), m) for m in ["chat", "hibou", "ours"])
"""


#############################
#  Bonus : les décorateurs  #
#############################

"""
19. Écrivez un décorateur compter_appels qui affiche, à chaque appel,
    "<nom> appelée <n> fois". Testez-le sur une fonction saluer(nom).
    (Indice : la closure peut stocker le compteur dans une liste [0], ou
    utiliser nonlocal, cf. chap. 19.) N'oubliez pas functools.wraps.

20. Écrivez un décorateur verifier_positifs qui soulève une ValueError si
    un des arguments positionnels de la fonction décorée est négatif.
    Testez-le sur une fonction aire_rectangle(largeur, hauteur).
"""


###################################################
#  Bonus : with et les gestionnaires de contexte  #
###################################################

"""
21. Avec @contextlib.contextmanager, écrivez un gestionnaire de contexte
    section(titre) qui affiche "=== titre ===" à l'entrée du bloc et
    "=== fin ===" à la sortie, même en cas d'erreur.
"""
