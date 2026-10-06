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
#  Chap. 43     #  Collections : corrigés                                      #
#               #                                                              #
################################################################################

from collections import Counter, defaultdict, namedtuple, deque
from collections import OrderedDict, ChainMap
import itertools
import heapq
import bisect
from enum import Enum


#############
#  Counter  #
#############

r"""
1. Sans exécuter, qu'affiche ce programme ?
"""
c = Counter("mississippi")
print(c["s"], c["z"])     # => 4 0
print(c.most_common(1))   # => [('i', 4)]
r"""
"mississippi" contient 4 "i", 4 "s", 2 "p" et 1 "m". Un élément absent vaut
0 (pas de KeyError). En cas d'égalité, most_common garde l'ordre de première
apparition : "i" (indice 1) apparaît avant "s" (indice 2).
"""

r"""
2. Comptez les réponses au sondage, avec un dictionnaire puis avec Counter,
   et affichez la réponse la plus fréquente et son pourcentage.
"""
reponses = ["oui", "non", "oui", "sans avis", "oui", "non"]

# a) À la main
compte = {}
for r in reponses:
    compte[r] = compte.get(r, 0) + 1
print(compte)   # => {'oui': 3, 'non': 2, 'sans avis': 1}

# b) Avec Counter
compte = Counter(reponses)
print(compte)   # => Counter({'oui': 3, 'non': 2, 'sans avis': 1})

# c) La plus fréquente
reponse, nombre = compte.most_common(1)[0]
print(f"{reponse} : {nombre / len(reponses):.0%}")   # => oui : 50%
r"""
most_common(1) renvoie une liste d'UN tuple : [0] le récupère, puis on le
déballe. Le format :.0% multiplie par 100 et ajoute le signe % (cf. chap. 8).
"""

r"""
3. Trouvez les 3 mots les plus fréquents (sans tenir compte des majuscules).
"""
texte = "Le chat voit le chien. Le chien voit le chat. Le chat dort."
mots = texte.replace(".", "").lower().split()
print(Counter(mots).most_common(3))
# => [('le', 5), ('chat', 3), ('voit', 2)]
r"""
Sans .lower(), "Le" et "le" seraient comptés séparément ; sans retirer les
points, "chien." et "chien" aussi. Nettoyer les données AVANT de compter est
indispensable (on pourrait aussi utiliser re.findall(r"\w+", …), cf. chap. 42).
"chien" apparaît aussi 2 fois, mais "voit" apparaît en premier dans le texte.
"""

r"""
4. Calculez le stock final. Pourquoi les kiwis disparaissent-ils ?
"""
stock = Counter(pommes=8, poires=5, kiwis=2)
stock.update({"pommes": 10, "kiwis": 6})
print(stock)   # => Counter({'pommes': 18, 'kiwis': 8, 'poires': 5})
stock = stock - Counter(pommes=12, kiwis=8)
print(stock)   # => Counter({'pommes': 6, 'poires': 5})
r"""
.update() AJOUTE les quantités (contrairement à dict.update, qui remplace).
La soustraction de deux Counter supprime les éléments dont le compte tombe à
0 ou moins : il reste 8 - 8 = 0 kiwi, donc la clé disparaît.
"""


#################
#  defaultdict  #
#################

r"""
5. Sans exécuter, qu'affiche ce programme ?
"""
d = defaultdict(int)
for lettre in "banane":
    d[lettre] += 1
print(dict(d))          # => {'b': 1, 'a': 2, 'n': 2, 'e': 1}
print(d["z"], len(d))   # => 0 5
r"""
Piège : lire d["z"] CRÉE la clé "z" avec la valeur int() = 0. Comme les
arguments de print() sont évalués de gauche à droite, len(d) vaut déjà 5
(b, a, n, e et z).
"""

r"""
6. Regroupez ces villes par département dans un defaultdict(list), puis
   affichez le nombre de villes par département.
"""
villes = [("Lyon", "69"), ("Nice", "06"), ("Villeurbanne", "69"),
          ("Cannes", "06"), ("Lille", "59")]
par_dep = defaultdict(list)
for ville, dep in villes:
    par_dep[dep].append(ville)

for dep, liste in par_dep.items():
    print(dep, len(liste), liste)
# => 69 2 ['Lyon', 'Villeurbanne']
# => 06 2 ['Nice', 'Cannes']
# => 59 1 ['Lille']
r"""
Grâce à defaultdict(list), la première fois qu'on voit un département, sa
liste vide est créée automatiquement : pas besoin de tester "if dep in…".
"""

r"""
7. Construisez pour chaque client l'ensemble des produits qu'il a achetés.
"""
achats = [("Ada", "pain"), ("Alan", "lait"), ("Ada", "beurre"),
          ("Ada", "pain"), ("Alan", "pain")]
produits = defaultdict(set)
for client, produit in achats:
    produits[client].add(produit)
for client in produits:
    print(client, sorted(produits[client]))
# => Ada ['beurre', 'pain']
# => Alan ['lait', 'pain']
r"""
Avec set, le "pain" acheté deux fois par Ada n'apparaît qu'une fois. On trie
à l'affichage, car l'ordre d'un ensemble n'est pas garanti (cf. chap. 25).
"""

r"""
8. Regroupez les mots selon leur première lettre.
"""
mots = ["avion", "bateau", "arbre", "balle", "camion", "abricot"]
par_lettre = defaultdict(list)
for mot in mots:
    par_lettre[mot[0]].append(mot)
print(dict(par_lettre))
# => {'a': ['avion', 'arbre', 'abricot'], 'b': ['bateau', 'balle'],
#     'c': ['camion']}


################
#  namedtuple  #
################

r"""
9. Créez un namedtuple Produit, trois produits, puis calculez la valeur
   totale du stock.
"""
Produit = namedtuple("Produit", ["nom", "prix", "quantite"])
produits = [Produit("stylo", 1.5, 100), Produit("cahier", 3.2, 40),
            Produit("cartable", 25.0, 5)]
total = sum(p.prix * p.quantite for p in produits)
print(total)   # => 403.0
r"""
p.prix est bien plus lisible que p[1] : c'est tout l'intérêt de namedtuple.
150 + 128 + 125 = 403.
"""

r"""
10. Sans exécuter, qu'affiche ce programme ? Lequel provoque une erreur ?
"""
Point = namedtuple("Point", "x y")
p = Point(1, 2)
q = p._replace(y=5)
print(p, q)          # => Point(x=1, y=2) Point(x=1, y=5)
print(q._asdict())   # => {'x': 1, 'y': 5}
try:
    p.x = 3
except AttributeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
r"""
Un namedtuple est immuable, comme un tuple : on ne peut pas modifier un
champ. ._replace() ne modifie pas p, il renvoie un NOUVEAU Point.
"""

r"""
11. Trouvez le produit le plus cher, puis triez les produits par quantité
    décroissante.
"""
print(max(produits, key=lambda p: p.prix).nom)   # => cartable
tries = sorted(produits, key=lambda p: p.quantite, reverse=True)
print([p.nom for p in tries])   # => ['stylo', 'cahier', 'cartable']


###########
#  deque  #
###########

r"""
12. Sans exécuter, qu'affiche ce programme ?
"""
d = deque([1, 2, 3])
d.append(4)        # [1, 2, 3, 4]
d.appendleft(0)    # [0, 1, 2, 3, 4]
d.pop()            # retire 4 à droite
d.popleft()        # retire 0 à gauche
print(d)           # => deque([1, 2, 3])

r"""
13. Simulez une file d'attente à un guichet.
"""
file = deque(["Ada", "Alan", "Grace"])
ordre = []
ordre.append(file.popleft())   # Ada est servie
file.append("Linus")           # Linus arrive en bout de file
while file:
    ordre.append(file.popleft())
print(ordre)   # => ['Ada', 'Alan', 'Grace', 'Linus']
r"""
Une file d'attente est "premier arrivé, premier servi" (FIFO) : on ajoute à
droite avec append et on sert à gauche avec popleft.
"""

r"""
14. Calculez la moyenne mobile sur 3 jours des températures.
"""
temperatures = [10, 12, 14, 13, 9, 8, 11]
fenetre = deque(maxlen=3)
for t in temperatures:
    fenetre.append(t)
    if len(fenetre) == 3:
        print(round(sum(fenetre) / 3, 2))
# => 12.0
# => 13.0
# => 12.0
# => 10.0
# => 9.33
r"""
Avec maxlen=3, chaque nouvel append fait sortir automatiquement la valeur la
plus ancienne : la deque contient toujours les 3 derniers jours.
"""


###################################
#  OrderedDict, ChainMap et Enum  #
###################################

r"""
15. Sans exécuter, que valent ces deux expressions ?
"""
print({"a": 1, "b": 2} == {"b": 2, "a": 1})               # => True
print(OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1))     # => False
r"""
Deux dict sont égaux s'ils ont les mêmes couples clé-valeur, quel que soit
l'ordre. Deux OrderedDict doivent en plus avoir le même ordre.
"""

r"""
16. Avec un ChainMap, combinez les paramètres par ordre de priorité.
"""
ligne_de_commande = {"verbeux": True}
utilisateur = {"langue": "fr", "verbeux": False}
defaut = {"langue": "en", "verbeux": False, "theme": "clair"}

config = ChainMap(ligne_de_commande, utilisateur, defaut)
print(config["langue"], config["theme"], config["verbeux"])
# => fr clair True
r"""
Pour chaque clé, ChainMap cherche d'abord dans ligne_de_commande, puis dans
utilisateur, puis dans defaut : le premier dictionnaire qui a la clé gagne.
"""

r"""
17. Créez une énumération Couleur et une fonction peut_passer(feu).
"""
class Couleur(Enum):
    ROUGE = 1
    ORANGE = 2
    VERT = 3

def peut_passer(feu):
    return feu == Couleur.VERT

print(peut_passer(Couleur.VERT))    # => True
print(peut_passer(Couleur.ROUGE))   # => False
try:
    Couleur.BLEU
except AttributeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
r"""
Avec des strings ("vert", "rouge"), une faute de frappe passerait inaperçue.
Avec une Enum, un membre qui n'existe pas lève immédiatement une erreur.
"""


###############
#  itertools  #
###############

r"""
18. Calculez le solde d'un compte jour après jour.
"""
operations = [-20, 50, -30, -10]
print(list(itertools.accumulate([100] + operations)))
# => [100, 80, 130, 100, 90]
r"""
accumulate fait la somme cumulée : 100, 100-20, 100-20+50, etc. On place le
solde initial en tête de la liste.
"""

r"""
19. Combien de menus différents ? Combien de façons de choisir 2 entrées ?
"""
entrees = ["soupe", "salade", "terrine"]
plats = ["poulet", "poisson"]
desserts = ["tarte", "glace"]

menus = list(itertools.product(entrees, plats, desserts))
print(len(menus))   # => 12
print(menus[0])     # => ('soupe', 'poulet', 'tarte')
print(len(list(itertools.combinations(entrees, 2))))   # => 3
r"""
    a) product forme toutes les combinaisons : 3 × 2 × 2 = 12 menus.
    b) combinations ne tient pas compte de l'ordre : (soupe, salade) et
       (salade, soupe) comptent pour un. Il y a 3 paires. Avec
       permutations, on en aurait 6.
"""

r"""
20. Sans exécuter, qu'affiche ce programme ? Comment le corriger pour obtenir
    un seul groupe par parité ?
"""
nombres = [2, 4, 1, 3, 6, 5]
def est_pair(n):
    return n % 2 == 0

for pair, groupe in itertools.groupby(nombres, key=est_pair):
    print(pair, list(groupe))
# => True [2, 4]
# => False [1, 3]
# => True [6]
# => False [5]
r"""
groupby ne regroupe que les éléments CONSÉCUTIFS de même clé. Il faut trier
d'abord, selon la même clé :
"""
for pair, groupe in itertools.groupby(sorted(nombres, key=est_pair),
                                      key=est_pair):
    print(pair, list(groupe))
# => False [1, 3, 5]
# => True [2, 4, 6]
r"""
(False < True, donc les impairs viennent en premier. Le tri est stable : à
l'intérieur de chaque groupe, l'ordre d'origine est conservé.)
"""


#####################
#  heapq et bisect  #
#####################

r"""
21. Affichez les 2 notes les plus hautes et les 2 plus basses.
"""
notes = [14, 8, 19, 12, 5, 17]
print(heapq.nlargest(2, notes))    # => [19, 17]
print(heapq.nsmallest(2, notes))   # => [5, 8]

r"""
22. Trouvez les 2 villes les moins peuplées.
"""
villes = [("Lyon", 522_000), ("Lille", 236_000), ("Nice", 342_000),
          ("Brest", 139_000)]
print(heapq.nsmallest(2, villes, key=lambda v: v[1]))
# => [('Brest', 139000), ('Lille', 236000)]

r"""
23. Gérez une file de priorité de tickets d'assistance.
"""
tickets = []
for ticket in [(2, "imprimante"), (1, "serveur en panne"), (3, "souris"),
               (1, "pas d'internet")]:
    heapq.heappush(tickets, ticket)
while tickets:
    print(heapq.heappop(tickets))
# => (1, "pas d'internet")
# => (1, 'serveur en panne')
# => (2, 'imprimante')
# => (3, 'souris')
r"""
heappop renvoie toujours le plus PETIT tuple. Les tuples se comparent élément
par élément (cf. chap. 17) : à priorité égale, c'est le texte qui départage,
par ordre alphabétique ("p" < "s"). Si l'on veut respecter l'ordre
d'arrivée, on ajoute un compteur : (priorite, numero_arrivee, texte).
"""

r"""
24. Avec bisect, écrivez une fonction tranche_age(age).
"""
SEUILS = [12, 18, 65]
TRANCHES = ["enfant", "ado", "adulte", "senior"]

def tranche_age(age):
    return TRANCHES[bisect.bisect_right(SEUILS, age)]

for age in [5, 12, 17, 18, 64, 65, 90]:
    print(age, tranche_age(age))
# => 5 enfant
# => 12 ado
# => 17 ado
# => 18 adulte
# => 64 adulte
# => 65 senior
# => 90 senior
r"""
bisect_right(SEUILS, age) compte combien de seuils sont inférieurs ou égaux à
age : 0 pour 5, 1 pour 12 (12 <= 12), 2 pour 18, 3 pour 65. Ce nombre est
directement l'indice de la tranche. Testez toujours les valeurs AUX seuils
(12, 18, 65) : c'est là que se cachent les erreurs.
"""


##########################
#  Choisir le bon outil  #
##########################

r"""
25. Pour chaque besoin, quel conteneur ou outil choisiriez-vous ?
    a) compter le nombre de visites par page d'un site
       -> Counter
    b) garder les 10 dernières commandes tapées par l'utilisateur
       -> deque(maxlen=10)
    c) représenter un pixel (r, g, b) qui ne doit pas changer
       -> un tuple, ou un namedtuple("Pixel", "r g b") pour plus de clarté
    d) regrouper des étudiants par promotion
       -> defaultdict(list)
    e) les 5 produits les plus vendus parmi 100 000
       -> Counter(...).most_common(5), ou heapq.nlargest(5, ...)
    f) les jours de la semaine
       -> une Enum
"""
