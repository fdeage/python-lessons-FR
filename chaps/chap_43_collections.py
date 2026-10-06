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
#  Chap. 43     #  Collections et outils de la bibliothèque standard           #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Compter : Counter
#  - Des valeurs par défaut : defaultdict
#  - Des tuples avec des noms : namedtuple
#  - Une file à deux bouts : deque
#  - OrderedDict : un dictionnaire ordonné (historique)
#  - Bonus : ChainMap
#  - Combiner des itérables : itertools
#  - Les plus grands, les plus petits : heapq
#  - Bonus : chercher dans une liste triée avec bisect
#  - Rappel : les dataclasses
#  - Des constantes nommées : Enum
#  - Quel conteneur pour quel besoin ?
#  - En bref
#
#############################################

from collections import Counter, defaultdict, namedtuple, deque
from collections import OrderedDict, ChainMap
import itertools
import heapq
import bisect
import timeit
from dataclasses import dataclass
from enum import Enum


# Introduction
###############

r"""
On connaît déjà les quatre conteneurs de base de Python : les listes (chap. 16
et 24), les tuples (chap. 17), les dictionnaires (chap. 18 et 27) et les
ensembles (chap. 25). Ils suffisent pour presque tout.

Mais certaines tâches reviennent si souvent (compter des éléments, regrouper
des valeurs par catégorie, garder les N derniers éléments…) que la
bibliothèque standard propose des conteneurs spécialisés, dans le module
"collections". Ils sont plus courts à écrire, plus lisibles et souvent plus
rapides que leur équivalent "fait main".

On verra aussi quelques modules voisins très utiles : itertools, heapq,
bisect et enum.

Tout cela fait partie de la bibliothèque standard : rien à installer
(cf. chap. 22).
"""


# Compter : Counter
####################

r"""
Compter les occurrences des éléments d'une liste est une tâche très
fréquente. Au chap. 27, on l'a fait à la main avec un dictionnaire :
"""
fruits = ["pomme", "kiwi", "pomme", "poire", "kiwi", "pomme"]

compteur = {}
for fruit in fruits:
    compteur[fruit] = compteur.get(fruit, 0) + 1
print(compteur)   # => {'pomme': 3, 'kiwi': 2, 'poire': 1}

r"""
Counter fait exactement cela, en une ligne. Un Counter est un dictionnaire
spécialisé : les clés sont les éléments, les valeurs leur nombre
d'occurrences.
"""
c = Counter(fruits)
print(c)            # => Counter({'pomme': 3, 'kiwi': 2, 'poire': 1})
print(c["pomme"])   # => 3

# IMPT : un élément absent vaut 0 (pas de KeyError, contrairement à un dict)
print(c["banane"])  # => 0

r"""
Counter accepte n'importe quel itérable (cf. chap. 23), par exemple une
chaîne de caractères :
"""
lettres = Counter("abracadabra")
print(lettres)   # => Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

r"""
.most_common(n) renvoie les n éléments les plus fréquents, sous forme de
liste de tuples (élément, nombre), du plus fréquent au moins fréquent :
"""
print(lettres.most_common(2))   # => [('a', 5), ('b', 2)]
print(lettres.most_common(1)[0][0])  # => a : la lettre la plus fréquente

r"""
Un exemple typique d'analyse de texte : les mots les plus fréquents.
"""
texte = "le chat et le chien et le poisson"
print(Counter(texte.split()).most_common(2))   # => [('le', 3), ('et', 2)]

r"""
On peut mettre à jour un Counter avec .update(), et additionner ou
soustraire deux Counter :
"""
stock = Counter(pommes=10, poires=4)
stock.update({"pommes": 5, "kiwis": 3})   # AJOUTE (ne remplace pas)
print(stock)   # => Counter({'pommes': 15, 'poires': 4, 'kiwis': 3})

ventes = Counter(pommes=12, poires=4)
print(stock - ventes)   # => Counter({'pommes': 3, 'kiwis': 3})
print(stock + ventes)   # => Counter({'pommes': 27, 'poires': 8, 'kiwis': 3})

r"""
Notez que la soustraction supprime les éléments dont le compte tombe à 0 ou
en dessous (ici, les poires).

.total() (Python 3.10+) renvoie la somme de tous les comptes :
"""
print(sum(stock.values()))   # => 22 : fonctionne dans toutes les versions


# Des valeurs par défaut : defaultdict
#######################################

r"""
Autre tâche très fréquente : REGROUPER des valeurs par catégorie. À la main,
il faut vérifier si la clé existe avant d'ajouter :
"""
eleves = [("Ada", "A"), ("Alan", "B"), ("Grace", "A"), ("Linus", "B"),
          ("Guido", "A")]

par_groupe = {}
for nom, groupe in eleves:
    if groupe not in par_groupe:
        par_groupe[groupe] = []      # 1re fois : on crée la liste vide
    par_groupe[groupe].append(nom)
print(par_groupe)
# => {'A': ['Ada', 'Grace', 'Guido'], 'B': ['Alan', 'Linus']}

r"""
Un defaultdict est un dictionnaire qui crée AUTOMATIQUEMENT une valeur par
défaut quand on accède à une clé absente. On lui donne, à la création, une
FONCTION sans paramètre qui fabrique cette valeur (cf. chap. 32 : les
fonctions sont des objets) :
    defaultdict(list)   : une clé absente vaut [] (car list() renvoie [])
    defaultdict(int)    : une clé absente vaut 0  (car int() renvoie 0)
    defaultdict(set)    : une clé absente vaut set()
"""
par_groupe = defaultdict(list)
for nom, groupe in eleves:
    par_groupe[groupe].append(nom)   # plus besoin du if !
print(par_groupe)
# => defaultdict(<class 'list'>, {'A': ['Ada', 'Grace', 'Guido'],
#                                 'B': ['Alan', 'Linus']})
print(dict(par_groupe))   # pour un affichage plus lisible
# => {'A': ['Ada', 'Grace', 'Guido'], 'B': ['Alan', 'Linus']}

r"""
Avec int, on obtient un compteur (mais Counter est plus adapté pour compter) :
"""
longueurs = defaultdict(int)
for mot in ["chat", "kiwi", "pomme", "lit"]:
    longueurs[len(mot)] += 1   # une clé absente vaut 0 : 0 + 1
print(dict(longueurs))   # => {4: 2, 5: 1, 3: 1}

r"""
Avec set, on regroupe sans doublons :
"""
achats = [("Ada", "pain"), ("Alan", "lait"), ("Ada", "pain"), ("Ada", "lait")]
produits_par_client = defaultdict(set)
for client, produit in achats:
    produits_par_client[client].add(produit)
print(sorted(produits_par_client["Ada"]))   # => ['lait', 'pain']

r"""
Attention : la simple LECTURE d'une clé absente la crée ! C'est parfois
surprenant :
"""
d = defaultdict(list)
print("x" in d)   # => False
d["x"]            # une simple lecture…
print("x" in d)   # => True : … a créé la clé "x" avec la valeur []

r"""
Pour juste tester la présence d'une clé, utilisez "in" ou .get(), qui ne
créent rien.
"""


# Des tuples avec des noms : namedtuple
########################################

r"""
Un tuple (cf. chap. 17) est pratique pour regrouper quelques valeurs, mais
on y accède par des indices peu parlants :
"""
point = (2.5, 4.0)
print(point[0])   # => 2.5 : est-ce x ? la latitude ? on ne sait pas…

r"""
namedtuple crée un nouveau TYPE de tuple dont les éléments ont des noms. On
lui donne le nom du type et la liste des noms des champs :
"""
Point = namedtuple("Point", ["x", "y"])

p = Point(2.5, 4.0)
print(p)          # => Point(x=2.5, y=4.0)
print(p.x, p.y)   # => 2.5 4.0 : accès par nom…
print(p[0])       # => 2.5 : … mais aussi par indice, c'est toujours un tuple
x, y = p          # et on peut le déballer (cf. chap. 17)
print(x + y)      # => 6.5

r"""
Comme un tuple, un namedtuple est immuable :
"""
try:
    p.x = 10
except AttributeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

r"""
Pour "modifier" un champ, ._replace() renvoie une NOUVELLE instance, et
._asdict() convertit en dictionnaire (pratique pour l'export JSON, cf.
chap. 28, ou pour créer un DataFrame pandas, cf. chap. 39) :
"""
p2 = p._replace(x=10)
print(p2)           # => Point(x=10, y=4.0)
print(p)            # => Point(x=2.5, y=4.0) : l'original est inchangé
print(p._asdict())  # => {'x': 2.5, 'y': 4.0}

r"""
Un usage typique : représenter les lignes d'un fichier de données.
"""
Ville = namedtuple("Ville", "nom population departement")  # noms séparés
villes = [Ville("Lyon", 522_000, "69"), Ville("Lille", 236_000, "59"),
          Ville("Nice", 342_000, "06")]
plus_grande = max(villes, key=lambda v: v.population)   # cf. chap. 32
print(plus_grande.nom)   # => Lyon

r"""
namedtuple, tuple ou classe ?
    - tuple       : 2 ou 3 valeurs, utilisées localement ;
    - namedtuple  : des "enregistrements" immuables et légers, avec des noms ;
    - dataclass   : des enregistrements MODIFIABLES, avec des méthodes et des
                    valeurs par défaut (cf. chap. 35 et plus bas) ;
    - classe      : des objets avec un vrai comportement (cf. chap. 34).
"""


# Une file à deux bouts : deque
################################

r"""
Une deque (prononcer "dèque", pour "double-ended queue", file à deux bouts)
ressemble à une liste, mais elle permet d'ajouter et de retirer des éléments
RAPIDEMENT aux DEUX extrémités :
    .append(x) / .pop()          à droite (comme une liste)
    .appendleft(x) / .popleft()  à gauche
"""
file = deque(["Ada", "Alan"])
file.append("Grace")       # arrive en fin de file
file.appendleft("Guido")   # passe devant tout le monde
print(file)                # => deque(['Guido', 'Ada', 'Alan', 'Grace'])
print(file.popleft())      # => Guido : le premier sort
print(file)                # => deque(['Ada', 'Alan', 'Grace'])

r"""
Une deque peut servir :
    - de FILE (FIFO, "premier arrivé, premier servi") : append + popleft ;
    - de PILE (LIFO, "dernier arrivé, premier servi") : append + pop.

Pourquoi ne pas utiliser une liste, avec liste.pop(0) ? Parce que retirer le
PREMIER élément d'une liste oblige Python à décaler tous les autres d'une
case : c'est lent quand la liste est longue. La deque, elle, est conçue pour
cela. Mesurons-le avec timeit (cf. chap. 22) :
"""
def vider_liste():
    l = list(range(50_000))
    while l:
        l.pop(0)

def vider_deque():
    d = deque(range(50_000))
    while d:
        d.popleft()

t_liste = timeit.timeit(vider_liste, number=1)
t_deque = timeit.timeit(vider_deque, number=1)
print(t_liste > t_deque)   # => True
# Les temps exacts varient selon la machine ; chez nous, la deque est
# plusieurs dizaines de fois plus rapide. On expliquera pourquoi au chap. 45
# (complexité algorithmique).

r"""
maxlen : une deque peut avoir une taille maximale. Quand elle est pleine,
ajouter un élément d'un côté en fait sortir un de l'autre côté. Idéal pour
garder un "historique glissant" (les N dernières valeurs) :
"""
dernieres_mesures = deque(maxlen=3)
for mesure in [12, 15, 11, 18, 20]:
    dernieres_mesures.append(mesure)
    print(list(dernieres_mesures))
# => [12]
# => [12, 15]
# => [12, 15, 11]
# => [15, 11, 18]
# => [11, 18, 20]

# Une moyenne mobile sur les 3 dernières valeurs :
print(sum(dernieres_mesures) / len(dernieres_mesures))   # => 16.333333333333332

r"""
Contrepartie : l'accès par indice au MILIEU d'une deque (d[i]) est plus lent
que pour une liste, et les deques n'acceptent pas les slices.
"""
try:
    dernieres_mesures[0:2]
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


# OrderedDict : un dictionnaire ordonné (historique)
#####################################################

r"""
Avant Python 3.7, les dictionnaires ne garantissaient pas l'ordre de leurs
clés. OrderedDict était alors LE moyen d'avoir un dictionnaire ordonné.

Depuis Python 3.7, les dict normaux conservent l'ordre d'insertion (cf.
chap. 27) : OrderedDict est donc beaucoup moins utile. Vous le croiserez
surtout dans du code ancien.

Il garde deux petites particularités :
    - .move_to_end(cle) déplace une clé à la fin (ou au début avec
      last=False) ;
    - l'égalité entre deux OrderedDict tient compte de l'ordre.
"""
od = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")
print(list(od))   # => ['b', 'c', 'a']

print({"a": 1, "b": 2} == {"b": 2, "a": 1})   # => True
print(OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1))   # => False


# Bonus : ChainMap
###################

r"""
Un ChainMap regroupe plusieurs dictionnaires en une seule "vue" : quand on
cherche une clé, il regarde dans le premier dictionnaire, puis dans le
deuxième, etc. C'est pratique pour des configurations superposées : les
choix de l'utilisateur ont priorité sur les valeurs par défaut.
"""
defaut = {"couleur": "bleu", "taille": 12, "police": "Arial"}
choix_utilisateur = {"taille": 16}

config = ChainMap(choix_utilisateur, defaut)
print(config["taille"])    # => 16 : trouvé dans choix_utilisateur
print(config["couleur"])   # => bleu : pas dans choix_utilisateur -> defaut
print(dict(config))
# => {'couleur': 'bleu', 'taille': 16, 'police': 'Arial'}

r"""
Rien n'est copié : si on modifie "defaut", la vue est mise à jour.
(Pour un simple fusionnement, {**defaut, **choix_utilisateur} suffit,
cf. chap. 27.)
"""


# Combiner des itérables : itertools
#####################################

r"""
Le module itertools contient des fonctions qui fabriquent des ITÉRATEURS
(cf. chap. 23 et 36) à partir d'autres itérables. Comme ce sont des
itérateurs, on les convertit souvent en liste pour les afficher.

1. chain : enchaîner plusieurs itérables, sans créer de liste intermédiaire.
"""
janvier = [12, 15]
fevrier = [11, 18, 20]
print(list(itertools.chain(janvier, fevrier)))   # => [12, 15, 11, 18, 20]

r"""
2. accumulate : les totaux cumulés (ou autre opération cumulée).
"""
ventes_par_jour = [3, 5, 2, 8]
print(list(itertools.accumulate(ventes_par_jour)))   # => [3, 8, 10, 18]
print(list(itertools.accumulate(ventes_par_jour, max)))  # => [3, 5, 5, 8]

r"""
3. product, combinations, permutations : la combinatoire.
    - product(a, b)          : tous les couples (x, y), x dans a et y dans b
                               (comme deux boucles for imbriquées)
    - combinations(l, k)     : les groupes de k éléments, SANS tenir compte
                               de l'ordre
    - permutations(l, k)     : les arrangements de k éléments, EN tenant
                               compte de l'ordre
"""
tailles = ["S", "M"]
couleurs = ["rouge", "noir"]
print(list(itertools.product(tailles, couleurs)))
# => [('S', 'rouge'), ('S', 'noir'), ('M', 'rouge'), ('M', 'noir')]

equipe = ["Ada", "Alan", "Grace"]
print(list(itertools.combinations(equipe, 2)))
# => [('Ada', 'Alan'), ('Ada', 'Grace'), ('Alan', 'Grace')]
print(len(list(itertools.permutations(equipe, 2))))   # => 6
# (Ada, Alan) et (Alan, Ada) sont deux permutations différentes,
# mais une seule combinaison.

r"""
4. groupby : regrouper des éléments CONSÉCUTIFS qui ont la même clé. Il
renvoie des couples (clé, groupe), où groupe est lui-même un itérateur.

IMPT : groupby ne regroupe que des éléments qui se SUIVENT. Il faut donc
presque toujours TRIER les données selon la même clé avant !
"""
mots = ["kiwi", "ananas", "noix", "fraise", "lit"]

# Sans tri préalable : les groupes sont "cassés"
for longueur, groupe in itertools.groupby(mots, key=len):
    print(longueur, list(groupe))
# => 4 ['kiwi']
# => 6 ['ananas']
# => 4 ['noix']
# => 6 ['fraise']
# => 3 ['lit']

# Avec tri préalable selon la même clé : on obtient bien un groupe par clé
for longueur, groupe in itertools.groupby(sorted(mots, key=len), key=len):
    print(longueur, list(groupe))
# => 3 ['lit']
# => 4 ['kiwi', 'noix']
# => 6 ['ananas', 'fraise']

r"""
(Pour regrouper des données sans les trier, un defaultdict(list) est souvent
plus simple. Et sur des tableaux de données, on utilisera le groupby de
pandas, cf. chap. 39.)
"""


# Les plus grands, les plus petits : heapq
###########################################

r"""
Pour obtenir les n plus grandes (ou plus petites) valeurs d'une collection,
on peut trier puis prendre une slice. heapq.nlargest et heapq.nsmallest le
font directement, et plus efficacement quand n est petit devant la taille
des données :
"""
notes = [12, 18, 7, 15, 9, 20, 11]
print(heapq.nlargest(3, notes))    # => [20, 18, 15]
print(heapq.nsmallest(2, notes))   # => [7, 9]
print(sorted(notes, reverse=True)[:3])   # => [20, 18, 15] : même résultat

# Avec un paramètre key, comme sorted (cf. chap. 32) :
print([v.nom for v in heapq.nlargest(2, villes, key=lambda v: v.population)])
# => ['Lyon', 'Nice']

r"""
heapq permet aussi de gérer une "file de priorité" : une liste dans laquelle
on peut ajouter des éléments n'importe quand, et toujours retirer rapidement
le PLUS PETIT. On y met souvent des tuples (priorité, tâche) : les tuples se
comparent élément par élément (cf. chap. 17), donc la priorité compte en
premier.
"""
taches = []
heapq.heappush(taches, (3, "ranger le bureau"))
heapq.heappush(taches, (1, "réparer le serveur"))
heapq.heappush(taches, (2, "répondre aux emails"))

while taches:
    priorite, tache = heapq.heappop(taches)   # retire la plus petite priorité
    print(priorite, tache)
# => 1 réparer le serveur
# => 2 répondre aux emails
# => 3 ranger le bureau


# Bonus : chercher dans une liste triée avec bisect
####################################################

r"""
Le module bisect travaille sur des listes DÉJÀ TRIÉES. Il trouve très
rapidement à quel indice un élément devrait être inséré pour que la liste
reste triée (par "dichotomie", cf. chap. 45).

Un usage classique : attribuer une catégorie selon des seuils.
"""
seuils = [10, 12, 14, 16]                       # triés !
mentions = ["Insuffisant", "Passable", "Assez bien", "Bien", "Très bien"]

def mention(note):
    return mentions[bisect.bisect_right(seuils, note)]

print(mention(8))    # => Insuffisant
print(mention(12))   # => Assez bien
print(mention(17))   # => Très bien

r"""
bisect.insort(liste, x) insère x à la bonne place dans une liste triée :
"""
scores = [10, 20, 30]
bisect.insort(scores, 25)
print(scores)   # => [10, 20, 25, 30]


# Rappel : les dataclasses
###########################

r"""
Au chap. 35, on a vu le décorateur @dataclass (Python 3.7+), qui génère
automatiquement __init__, __repr__ et __eq__ d'une classe. C'est l'outil de
choix pour des "enregistrements" modifiables, là où namedtuple les rend
immuables :
"""
@dataclass
class Mesure:
    capteur: str
    valeur: float
    unite: str = "°C"   # valeur par défaut

m = Mesure("salon", 21.5)
print(m)          # => Mesure(capteur='salon', valeur=21.5, unite='°C')
m.valeur = 22.0   # modifiable, contrairement à un namedtuple
print(m.valeur)   # => 22.0


# Des constantes nommées : Enum
################################

r"""
Quand une variable ne peut prendre que quelques valeurs fixes (des jours, des
niveaux de gravité, des statuts de commande…), on est tenté d'utiliser des
strings : "en_cours", "livree"… Mais une faute de frappe ("livre") ne
provoque aucune erreur, et le bug passe inaperçu.

Le module enum permet de définir une ÉNUMÉRATION : un ensemble fini de
constantes nommées. On l'écrit comme une classe (cf. chap. 34) qui hérite de
Enum (cf. chap. 35) :
"""
class Statut(Enum):
    EN_ATTENTE = 1
    EXPEDIEE = 2
    LIVREE = 3

commande = Statut.EXPEDIEE
print(commande)         # => Statut.EXPEDIEE
print(commande.name)    # => EXPEDIEE
print(commande.value)   # => 2
print(commande == Statut.EXPEDIEE)   # => True

# Une faute de frappe est détectée immédiatement :
try:
    Statut.LIVRE
except AttributeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# On peut parcourir une énumération, et retrouver un membre par sa valeur :
print([s.name for s in Statut])   # => ['EN_ATTENTE', 'EXPEDIEE', 'LIVREE']
print(Statut(3))                  # => Statut.LIVREE


# Quel conteneur pour quel besoin ?
####################################

r"""
    Besoin                                         Outil
    ---------------------------------------------  ------------------------
    une séquence modifiable                        list           (chap. 16)
    une séquence fixe, petite                      tuple          (chap. 17)
    associer des clés à des valeurs                dict           (chap. 18)
    des éléments uniques, tester l'appartenance    set            (chap. 25)
    compter des occurrences                        Counter
    regrouper des valeurs par clé                  defaultdict(list)
    un enregistrement immuable avec des noms       namedtuple
    un enregistrement modifiable                   @dataclass     (chap. 35)
    une file / ajouter-retirer aux deux bouts      deque
    garder les N dernières valeurs                 deque(maxlen=N)
    superposer plusieurs dictionnaires             ChainMap
    les N plus grands / plus petits                heapq.nlargest/nsmallest
    une file de priorité                           heapq.heappush/heappop
    chercher/insérer dans une liste triée          bisect
    un ensemble fini de constantes                 Enum
    des tableaux de nombres                        numpy          (chap. 38)
    des tableaux de données                        pandas         (chap. 39)
"""


# En bref
##########

r"""
    from collections import Counter, defaultdict, namedtuple, deque

    Counter(iterable)          compte les éléments ; .most_common(n)
    defaultdict(list)          une clé absente est créée avec list() -> []
    namedtuple("P", ["x","y"]) tuple aux champs nommés ; ._replace, ._asdict
    deque(maxlen=n)            append/appendleft, pop/popleft rapides
    OrderedDict                utile surtout avant Python 3.7
    ChainMap(d1, d2)           cherche dans d1, puis dans d2

    itertools.chain/accumulate/product/combinations/permutations
    itertools.groupby          TRIER d'abord selon la même clé !
    heapq.nlargest(n, l)       les n plus grands ; heappush/heappop
    bisect.bisect_right(l, x)  position de x dans une liste triée
    class C(Enum): A = 1       constantes nommées
"""
