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
#  Chap. 32     #  Fonctions III : exercices                                   #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) en notant la valeur de chaque paramètre à chaque appel.

Les corrigés sont dans le fichier corrs/corr_32_fonctions_3.py.
"""


#######################
#  *args et **kwargs  #
#######################

"""
1. Sans exécuter, qu'affiche ce programme ?
       def f(a, *args):
           print(a, args)

       f(1)
       f(1, 2, 3)
       f("x", [4, 5])

2. Écrivez une fonction produit(*nombres) qui renvoie le produit de tous ses
   arguments (et 1 si on n'en passe aucun).
       produit(2, 3, 4)  => 24
       produit()         => 1

3. Écrivez une fonction plus_long(*mots) qui renvoie le mot le plus long
   parmi ses arguments (le premier rencontré en cas d'égalité), ou None si
   aucun mot n'est passé.

4. Écrivez une fonction decrire(nom, **infos) qui affiche le nom, puis une
   ligne "  clé : valeur" par information supplémentaire.
       decrire("Lyon", habitants=522000, region="Auvergne-Rhône-Alpes")
   doit afficher :
       Lyon
         habitants : 522000
         region : Auvergne-Rhône-Alpes

5. Sans exécuter, qu'affiche ce programme ?
       def g(*args, **kwargs):
           print(len(args), len(kwargs))

       g(1, 2, x=3)
       g()
       g(a=1, b=2, c=3)
"""


##########################
#  Ordre des paramètres  #
##########################

"""
6. Parmi ces définitions, lesquelles sont valides ? Pour celles qui ne le
   sont pas, expliquez pourquoi.
       a) def f(a, b=2, *args, **kwargs): …
       b) def f(a=1, b): …
       c) def f(*args, a): …
       d) def f(**kwargs, *args): …
       e) def f(a, *, b): …

7. On définit def h(a, b=10, *args, **kwargs). Sans exécuter, que valent a,
   b, args et kwargs lors de chacun de ces appels ?
       h(1)
       h(1, 2, 3, 4)
       h(1, c=5)
       h(b=3, a=7)
"""


###############################
#  Déballage et keyword-only  #
###############################

"""
8. On dispose de def distance(x1, y1, x2, y2) qui renvoie la distance entre
   deux points : ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5.
   Avec p1 = (0, 0) et p2 = (3, 4), appelez distance() en déballant les deux
   tuples (sans écrire p1[0], p1[1]…).

9. Avec la liste valeurs = [3, 1, 4, 1, 5], affichez "3-1-4-1-5" en UNE
   instruction print(), sans boucle ni join().

10. Écrivez une fonction arrondir(valeur, *, decimales=2) qui arrondit
    valeur. Vérifiez que arrondir(3.14159, decimales=3) fonctionne, puis
    expliquez (dans un try) pourquoi arrondir(3.14159, 3) échoue.

11. On a parametres = {"valeur": 2.71828, "decimales": 1}. Appelez
    arrondir() en déballant ce dictionnaire.
"""


###################################
#  Les fonctions sont des objets  #
###################################

"""
12. Sans exécuter, qu'affiche ce programme ? Pourquoi la dernière ligne
    provoque-t-elle une erreur ?
        def bonjour():
            return "Bonjour !"

        a = bonjour
        b = bonjour()
        print(a())
        print(b)
        print(b())

13. Créez un dictionnaire conversions qui associe "km->m", "m->km" et
    "h->min" à des fonctions de conversion (écrites avec def). Écrivez une
    fonction convertir(valeur, sens) qui utilise ce dictionnaire.
        convertir(3, "km->m")    => 3000
        convertir(90, "h->min")  => 5400

14. Écrivez une fonction appliquer_deux_fois(f, x) qui renvoie f(f(x)).
    Testez-la avec une fonction qui ajoute 3, puis avec str.upper (sur une
    chaîne).
"""


############
#  lambda  #
############

"""
15. Réécrivez ces fonctions sous forme de lambda (rangées dans une variable,
    juste pour l'exercice) :
        def moitie(x): return x / 2
        def est_pair(n): return n % 2 == 0
        def initiales(prenom, nom): return prenom[0] + nom[0]

16. Sans exécuter, que vaut chaque expression ?
        (lambda x: x * 2)(5)
        (lambda a, b=1: a - b)(10)
        (lambda s: s[::-1])("abc")

17. Pourquoi ce code ne fonctionne-t-il pas ? Corrigez-le avec def.
        verifier = lambda n: if n > 0: "positif"
"""


################
#  key=lambda  #
################

"""
18. Avec produits = [("stylo", 1.5, 120), ("cahier", 3.2, 45),
    ("gomme", 0.8, 200), ("classeur", 4.9, 30)]
    (nom, prix unitaire, quantité en stock) :
        a) triez les produits par prix croissant ;
        b) triez-les par valeur du stock (prix × quantité) décroissante ;
        c) trouvez (avec max) le produit dont la quantité est la plus grande ;
        d) trouvez (avec min) le nom le plus court.

19. Avec la liste de dictionnaires
        pays = [{"nom": "France", "pop": 68, "pib": 3.0},
                {"nom": "Allemagne", "pop": 84, "pib": 4.5},
                {"nom": "Espagne", "pop": 48, "pib": 1.6},
                {"nom": "Italie", "pop": 59, "pib": 2.3}]
    (population en millions, PIB en milliers de milliards de dollars),
    affichez les noms des pays triés par PIB par habitant décroissant.

20. Triez les mots ["Banane", "abricot", "Cerise", "avocat"] par ordre
    alphabétique en ignorant les majuscules, puis par longueur et, à
    longueur égale, par ordre alphabétique (insensible à la casse).
"""


#######################
#  map() et filter()  #
#######################

"""
21. Sans exécuter, que vaut chaque expression ?
        list(map(len, ["a", "bb", "ccc"]))
        list(filter(lambda x: x > 2, [1, 5, 2, 8]))
        list(map(str.upper, "abc"))

22. La ligne saisie = "12.5;13;11.75;14" contient des mesures séparées par
    des ";". Avec map(), obtenez la liste de floats correspondante, puis sa
    moyenne.

23. Avec filter(), gardez seulement les adresses e-mail contenant "@" dans
    ["ada@mail.fr", "pas-un-mail", "alan@ex.com", ""].

24. Réécrivez chaque expression sous forme de compréhension de liste :
        list(map(lambda x: x * 10, nombres))
        list(filter(lambda m: m.startswith("a"), mots))
        list(map(lambda x: x ** 2, filter(lambda x: x < 0, nombres)))

25. Sans exécuter, qu'affiche ce programme ? Pourquoi ?
        doubles = map(lambda x: 2 * x, [1, 2, 3])
        print(sum(doubles))
        print(sum(doubles))
"""


######################################
#  Fonctions imbriquées et closures  #
######################################

"""
26. Écrivez une fonction fabrique_salutation(formule) qui renvoie une
    fonction prenant un prénom et renvoyant "<formule>, <prénom> !".
        bonjour = fabrique_salutation("Bonjour")
        bonjour("Ada")   => "Bonjour, Ada !"

27. Écrivez une fonction fabrique_seuil(seuil) qui renvoie une fonction
    testant si une valeur dépasse le seuil. Utilisez-la avec filter() pour
    garder les températures supérieures à 25 dans
    [18.2, 26.5, 31.0, 24.9, 25.1].

28. Sans exécuter, qu'affiche ce programme ?
        def f(n):
            return lambda x: x + n

        g = f(1)
        h = f(10)
        print(g(5), h(5), f(100)(5))

29. (Problème) Écrivez une fonction fabrique_compteur_mots() qui renvoie une
    fonction ajouter(mot). Chaque appel à ajouter(mot) compte le mot (dans un
    dictionnaire gardé par la closure) et renvoie le nombre de fois où ce mot
    a été vu jusqu'ici.
        compter = fabrique_compteur_mots()
        compter("chat") => 1 ; compter("chien") => 1 ; compter("chat") => 2
"""
