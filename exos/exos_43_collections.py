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
#  Chap. 43     #  Collections : exercices                                     #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) en notant le contenu de chaque conteneur ligne à ligne.

Les corrigés sont dans le fichier corrs/corr_43_collections.py.
"""

from collections import Counter, defaultdict, namedtuple, deque
from collections import OrderedDict, ChainMap
import itertools
import heapq
import bisect
from enum import Enum


#############
#  Counter  #
#############

"""
1. Sans exécuter, qu'affiche ce programme ?
       c = Counter("mississippi")
       print(c["s"], c["z"])
       print(c.most_common(1))

2. Voici les réponses à un sondage :
       reponses = ["oui", "non", "oui", "sans avis", "oui", "non"]
   a) Comptez-les avec un dictionnaire et une boucle (comme au chap. 27).
   b) Comptez-les avec Counter.
   c) Affichez la réponse la plus fréquente et son pourcentage.

3. Trouvez les 3 mots les plus fréquents (sans tenir compte des majuscules)
   dans :
       texte = "Le chat voit le chien. Le chien voit le chat. Le chat dort."
   (Indice : retirez les points et passez en minuscules avant de découper.)

4. Un magasin a le stock Counter(pommes=8, poires=5, kiwis=2). Il reçoit une
   livraison {"pommes": 10, "kiwis": 6} puis vend Counter(pommes=12,
   kiwis=8). Calculez le stock final. Pourquoi les kiwis disparaissent-ils ?
"""


#################
#  defaultdict  #
#################

"""
5. Sans exécuter, qu'affiche ce programme ?
       d = defaultdict(int)
       for lettre in "banane":
           d[lettre] += 1
       print(dict(d))
       print(d["z"], len(d))

6. Regroupez ces villes par département dans un defaultdict(list) :
       villes = [("Lyon", "69"), ("Nice", "06"), ("Villeurbanne", "69"),
                 ("Cannes", "06"), ("Lille", "59")]
   Puis affichez, pour chaque département, le nombre de villes.

7. À partir de cette liste d'achats, construisez pour chaque client
   l'ensemble (sans doublon) des produits qu'il a achetés :
       achats = [("Ada", "pain"), ("Alan", "lait"), ("Ada", "beurre"),
                 ("Ada", "pain"), ("Alan", "pain")]

8. Regroupez les mots suivants selon leur première lettre :
       mots = ["avion", "bateau", "arbre", "balle", "camion", "abricot"]
   Résultat attendu : {'a': ['avion', 'arbre', 'abricot'],
                       'b': ['bateau', 'balle'], 'c': ['camion']}
"""


################
#  namedtuple  #
################

"""
9. Créez un namedtuple Produit avec les champs nom, prix et quantite.
   Créez-en trois, puis calculez la valeur totale du stock
   (somme de prix * quantite).

10. Sans exécuter, qu'affiche ce programme ? Lequel des print() provoque une
    erreur ?
        Point = namedtuple("Point", "x y")
        p = Point(1, 2)
        q = p._replace(y=5)
        print(p, q)
        print(q._asdict())
        p.x = 3

11. Avec max() et un paramètre key (cf. chap. 32), trouvez le produit le plus
    cher de l'exercice 9, puis triez les produits par quantité décroissante.
"""


###########
#  deque  #
###########

"""
12. Sans exécuter, qu'affiche ce programme ?
        d = deque([1, 2, 3])
        d.append(4)
        d.appendleft(0)
        d.pop()
        d.popleft()
        print(d)

13. Simulez une file d'attente à un guichet : les clients "Ada", "Alan" et
    "Grace" arrivent dans cet ordre, puis "Linus" arrive après que le premier
    client a été servi. Affichez l'ordre de passage.

14. Avec une deque(maxlen=3), calculez la moyenne mobile sur 3 jours des
    températures [10, 12, 14, 13, 9, 8, 11] : affichez la moyenne après
    chaque jour où la deque est pleine (à partir du 3e jour).
"""


###################################
#  OrderedDict, ChainMap et Enum  #
###################################

"""
15. Sans exécuter, que valent ces deux expressions ?
        {"a": 1, "b": 2} == {"b": 2, "a": 1}
        OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1)
    (Pensez à importer OrderedDict.)

16. Avec un ChainMap, combinez des paramètres en ligne de commande, des
    paramètres de l'utilisateur et des valeurs par défaut, par ordre de
    priorité décroissante :
        ligne_de_commande = {"verbeux": True}
        utilisateur = {"langue": "fr", "verbeux": False}
        defaut = {"langue": "en", "verbeux": False, "theme": "clair"}
    Affichez la langue, le thème et la valeur de "verbeux".

17. Créez une énumération Couleur avec ROUGE, ORANGE et VERT (valeurs 1, 2,
    3). Écrivez une fonction peut_passer(feu) qui renvoie True seulement pour
    Couleur.VERT. Que se passe-t-il si on écrit Couleur.BLEU ?
"""


###############
#  itertools  #
###############

"""
18. Avec itertools.accumulate, calculez le solde d'un compte jour après jour,
    à partir d'un solde initial de 100 et des opérations [-20, 50, -30, -10].
    (Indice : accumulate([100, -20, …]).)

19. Un restaurant propose 3 entrées, 2 plats et 2 desserts :
        entrees = ["soupe", "salade", "terrine"]
        plats = ["poulet", "poisson"]
        desserts = ["tarte", "glace"]
    a) Combien de menus différents (entrée + plat + dessert) existe-t-il ?
       Utilisez itertools.product.
    b) Combien de façons de choisir 2 entrées différentes (sans ordre) ?
       Utilisez itertools.combinations.

20. Sans exécuter, qu'affiche ce programme ? Comment le corriger pour obtenir
    un seul groupe par parité ?
        nombres = [2, 4, 1, 3, 6, 5]
        def est_pair(n):
            return n % 2 == 0

        for pair, groupe in itertools.groupby(nombres, key=est_pair):
            print(pair, list(groupe))
"""


#####################
#  heapq et bisect  #
#####################

"""
21. Avec heapq, affichez les 2 notes les plus hautes et les 2 plus basses de
    [14, 8, 19, 12, 5, 17].

22. Avec heapq.nsmallest et key, trouvez les 2 villes les moins peuplées :
        villes = [("Lyon", 522_000), ("Lille", 236_000), ("Nice", 342_000),
                  ("Brest", 139_000)]

23. Gérez une file de priorité de tickets d'assistance avec heappush et
    heappop : (2, "imprimante"), (1, "serveur en panne"), (3, "souris"),
    (1, "pas d'internet"). Dans quel ordre sont-ils traités ? Que se passe-t-il
    quand deux tickets ont la même priorité ?

24. Avec bisect, écrivez une fonction tranche_age(age) qui renvoie
    "enfant" (moins de 12 ans), "ado" (12 à 17), "adulte" (18 à 64) ou
    "senior" (65 et plus).
"""


##########################
#  Choisir le bon outil  #
##########################

"""
25. Pour chaque besoin, quel conteneur ou outil choisiriez-vous ?
    a) compter le nombre de visites par page d'un site
    b) garder les 10 dernières commandes tapées par l'utilisateur
    c) représenter un pixel (r, g, b) qui ne doit pas changer
    d) regrouper des étudiants par promotion
    e) les 5 produits les plus vendus parmi 100 000
    f) les jours de la semaine
"""
