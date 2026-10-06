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
#  Chap. 32     #  Fonctions III : corrigés                                    #
#               #                                                              #
################################################################################

#######################
#  *args et **kwargs  #
#######################

"""
1. Sans exécuter, qu'affiche ce programme ?
"""


def f(a, *args):
    print(a, args)


f(1)           # => 1 ()
f(1, 2, 3)     # => 1 (2, 3)
f("x", [4, 5])  # => x ([4, 5],)
"""
- Le 1er argument va toujours dans a ; args ramasse le reste dans un TUPLE.
- f(1) : il ne reste rien, args est le tuple vide ().
- f("x", [4, 5]) : la liste est UN SEUL argument, donc args est un tuple
  d'un élément : ([4, 5],). La virgule finale est celle des tuples d'un
  élément (cf. chap. 17).
"""


"""
2. Une fonction produit(*nombres) :
"""


def produit(*nombres):
    resultat = 1          # élément neutre de la multiplication
    for n in nombres:
        resultat *= n
    return resultat


print(produit(2, 3, 4))  # => 24
print(produit())         # => 1
"""
On part de 1 et non de 0 : sinon le produit vaudrait toujours 0. Sans
argument, la boucle ne tourne pas et on renvoie 1.
"""


"""
3. Une fonction plus_long(*mots) :
"""


def plus_long(*mots):
    if len(mots) == 0:
        return None
    meilleur = mots[0]
    for mot in mots[1:]:
        if len(mot) > len(meilleur):   # ">" strict : le 1er gagne en cas
            meilleur = mot             # d'égalité
    return meilleur


print(plus_long("chat", "éléphant", "souris"))  # => éléphant
print(plus_long("abc", "xyz"))                  # => abc
print(plus_long())                              # => None
"""
Variante plus courte, avec ce que l'on verra plus loin dans ce chapitre :
max(mots, key=len) (max renvoie aussi le premier en cas d'égalité). Mais
max() d'un tuple vide provoque une erreur : il faut garder le test.
"""


"""
4. Une fonction decrire(nom, **infos) :
"""


def decrire(nom, **infos):
    print(nom)
    for cle, valeur in infos.items():
        print(f"  {cle} : {valeur}")


decrire("Lyon", habitants=522000, region="Auvergne-Rhône-Alpes")
# => Lyon
#      habitants : 522000
#      region : Auvergne-Rhône-Alpes
"""
infos est un dictionnaire dont les clés sont les noms des arguments nommés.
Les clés gardent l'ordre dans lequel on a passé les arguments.
"""


"""
5. Sans exécuter, qu'affiche ce programme ?
"""


def g(*args, **kwargs):
    print(len(args), len(kwargs))


g(1, 2, x=3)       # => 2 1
g()                # => 0 0
g(a=1, b=2, c=3)   # => 0 3
"""
Les arguments positionnels vont dans args (tuple), les arguments nommés dans
kwargs (dictionnaire). Sans argument, les deux sont vides.
"""


##########################
#  Ordre des paramètres  #
##########################

"""
6. Quelles définitions sont valides ?
    a) valide : obligatoire, par défaut, *args, **kwargs → l'ordre canonique.
    b) INVALIDE : un paramètre obligatoire (b) ne peut pas suivre un
       paramètre avec valeur par défaut (a=1).
    c) valide : a est après *args, il est donc keyword-only. On ne pourra
       l'appeler qu'avec f(1, 2, a=3).
    d) INVALIDE : **kwargs doit toujours être en dernier.
    e) valide : l'étoile seule rend b keyword-only.
On le vérifie avec compile(), qui analyse du code sans l'exécuter (une
erreur de syntaxe ne peut pas être interceptée autrement, cf. chap. 26) :
"""
definitions = {
    "a": "def f(a, b=2, *args, **kwargs): pass",
    "b": "def f(a=1, b): pass",
    "c": "def f(*args, a): pass",
    "d": "def f(**kwargs, *args): pass",
    "e": "def f(a, *, b): pass",
}
for lettre, code in definitions.items():
    try:
        compile(code, "<exo>", "exec")
        print(lettre, "valide")
    except SyntaxError:
        print(lettre, "INVALIDE")
# => a valide
#    b INVALIDE
#    c valide
#    d INVALIDE
#    e valide


"""
7. Valeurs de a, b, args et kwargs :
"""


def h(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)


h(1)              # => 1 10 () {}
h(1, 2, 3, 4)     # => 1 2 (3, 4) {}
h(1, c=5)         # => 1 10 () {'c': 5}
h(b=3, a=7)       # => 7 3 () {}
"""
- h(1) : b garde sa valeur par défaut, args et kwargs sont vides.
- h(1, 2, 3, 4) : 1 → a, 2 → b, le reste (3, 4) → args.
- h(1, c=5) : c ne correspond à aucun paramètre, il va dans kwargs.
- h(b=3, a=7) : les arguments nommés peuvent être dans n'importe quel ordre.
"""


###############################
#  Déballage et keyword-only  #
###############################

"""
8. Appeler distance() en déballant deux tuples :
"""


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


p1 = (0, 0)
p2 = (3, 4)
print(distance(*p1, *p2))  # => 5.0
"""
*p1 donne 0, 0 et *p2 donne 3, 4 : l'appel équivaut à distance(0, 0, 3, 4).
On peut utiliser plusieurs étoiles dans un même appel.
"""


"""
9. Afficher "3-1-4-1-5" en une instruction :
"""
valeurs = [3, 1, 4, 1, 5]
print(*valeurs, sep="-")  # => 3-1-4-1-5
"""
*valeurs passe chaque nombre comme un argument séparé à print(), et
sep="-" remplace l'espace habituel par un tiret.
"""


"""
10. Une fonction avec un paramètre keyword-only :
"""


def arrondir(valeur, *, decimales=2):
    return round(valeur, decimales)


print(arrondir(3.14159))               # => 3.14
print(arrondir(3.14159, decimales=3))  # => 3.142
try:
    arrondir(3.14159, 3)
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
L'étoile seule rend decimales keyword-only : la fonction n'accepte qu'UN
argument positionnel (valeur). Le 3 passé sans son nom est refusé.
"""


"""
11. Appeler arrondir() en déballant un dictionnaire :
"""
parametres = {"valeur": 2.71828, "decimales": 1}
print(arrondir(**parametres))  # => 2.7
"""
**parametres équivaut à arrondir(valeur=2.71828, decimales=1). Les clés
doivent correspondre exactement aux noms des paramètres.
"""


###################################
#  Les fonctions sont des objets  #
###################################

"""
12. Sans exécuter, qu'affiche ce programme ?
"""


def bonjour():
    return "Bonjour !"


a = bonjour      # a désigne la FONCTION (pas de parenthèses)
b = bonjour()    # b contient le RÉSULTAT de l'appel : la chaîne "Bonjour !"
print(a())       # => Bonjour !
print(b)         # => Bonjour !
try:
    print(b())
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
b est une chaîne, pas une fonction : on ne peut pas l'appeler avec ().
"""


"""
13. Un dictionnaire de fonctions de conversion :
"""


def km_vers_m(x):
    return x * 1000


def m_vers_km(x):
    return x / 1000


def h_vers_min(x):
    return x * 60


conversions = {"km->m": km_vers_m, "m->km": m_vers_km, "h->min": h_vers_min}


def convertir(valeur, sens):
    fonction = conversions[sens]   # on récupère la fonction…
    return fonction(valeur)        # … puis on l'appelle


print(convertir(3, "km->m"))    # => 3000
print(convertir(90, "h->min"))  # => 5400
print(convertir(1500, "m->km"))  # => 1.5
"""
Pour ajouter une conversion, il suffit d'ajouter une entrée au dictionnaire,
sans toucher à convertir() : pas de longue suite de if/elif.
"""


"""
14. appliquer_deux_fois(f, x) :
"""


def appliquer_deux_fois(fonction, x):
    return fonction(fonction(x))


def ajouter_3(n):
    return n + 3


print(appliquer_deux_fois(ajouter_3, 10))       # => 16
print(appliquer_deux_fois(str.upper, "salut"))  # => SALUT
"""
str.upper est la méthode upper() vue comme une fonction ordinaire :
str.upper("salut") équivaut à "salut".upper(). La passer deux fois ne
change rien après la 1re (c'est déjà en majuscules).
"""


############
#  lambda  #
############

"""
15. Les mêmes fonctions en lambda (pour l'exercice seulement : la PEP 8
    préfère def pour une fonction que l'on nomme, cf. chap. 20) :
"""
moitie = lambda x: x / 2                               # noqa: E731
est_pair = lambda n: n % 2 == 0                        # noqa: E731
initiales = lambda prenom, nom: prenom[0] + nom[0]     # noqa: E731
print(moitie(9))                        # => 4.5
print(est_pair(4), est_pair(7))         # => True False
print(initiales("Ada", "Lovelace"))     # => AL


"""
16. Sans exécuter, que vaut chaque expression ?
"""
print((lambda x: x * 2)(5))          # => 10
print((lambda a, b=1: a - b)(10))    # => 9
print((lambda s: s[::-1])("abc"))    # => cba
"""
On crée la lambda (entre parenthèses) et on l'appelle immédiatement avec
(…). Dans le 2e cas, b vaut 1 par défaut.
"""


"""
17. Une lambda ne peut contenir qu'une EXPRESSION, pas une instruction comme
    un bloc "if … :". On le vérifie avec compile() :
"""
try:
    compile('verifier = lambda n: if n > 0: "positif"', "<exo>", "exec")
except SyntaxError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")


# Correction avec def (et un cas "sinon", pour toujours renvoyer une valeur) :
def verifier(n):
    if n > 0:
        return "positif"
    return "négatif ou nul"


print(verifier(5), verifier(-2))  # => positif négatif ou nul
"""
Une lambda resterait possible avec l'expression conditionnelle (cf. chap.
12) : lambda n: "positif" if n > 0 else "négatif ou nul".
"""


################
#  key=lambda  #
################

"""
18. Trier et chercher dans une liste de produits :
"""
produits = [("stylo", 1.5, 120), ("cahier", 3.2, 45),
            ("gomme", 0.8, 200), ("classeur", 4.9, 30)]

# a) par prix croissant (élément d'indice 1)
print(sorted(produits, key=lambda p: p[1]))
# => [('gomme', 0.8, 200), ('stylo', 1.5, 120), ('cahier', 3.2, 45),
#     ('classeur', 4.9, 30)]

# b) par valeur du stock décroissante
for nom, prix, qte in sorted(produits, key=lambda p: p[1] * p[2],
                             reverse=True):
    print(nom, round(prix * qte, 2))
# => stylo 180.0
#    gomme 160.0
#    classeur 147.0
#    cahier 144.0

# c) le produit avec la plus grande quantité
print(max(produits, key=lambda p: p[2]))  # => ('gomme', 0.8, 200)

# d) le nom le plus court
print(min(produits, key=lambda p: len(p[0]))[0])  # => stylo
"""
- max() et min() renvoient l'élément ENTIER (le tuple), d'où le [0] pour
  n'avoir que le nom en d).
- En d), "stylo" et "gomme" ont 5 lettres : min() renvoie le premier
  rencontré, "stylo".
- round(…, 2) en b) évite d'afficher des valeurs comme 180.00000000000003
  (cf. chap. 4).
"""


"""
19. Pays triés par PIB par habitant décroissant :
"""
pays = [{"nom": "France", "pop": 68, "pib": 3.0},
        {"nom": "Allemagne", "pop": 84, "pib": 4.5},
        {"nom": "Espagne", "pop": 48, "pib": 1.6},
        {"nom": "Italie", "pop": 59, "pib": 2.3}]
classement = sorted(pays, key=lambda p: p["pib"] / p["pop"], reverse=True)
print([p["nom"] for p in classement])
# => ['Allemagne', 'France', 'Italie', 'Espagne']
"""
PIB par habitant (en unités arbitraires) : Allemagne 0.054, France 0.044,
Italie 0.039, Espagne 0.033. La clé est calculée pour chaque pays, et le
tri se fait sur ces valeurs.
"""


"""
20. Trier des mots en ignorant la casse, puis par longueur :
"""
mots = ["Banane", "abricot", "Cerise", "avocat"]
print(sorted(mots))
# => ['Banane', 'Cerise', 'abricot', 'avocat']  (majuscules d'abord !)
print(sorted(mots, key=lambda m: m.lower()))
# => ['abricot', 'avocat', 'Banane', 'Cerise']
print(sorted(mots, key=lambda m: (len(m), m.lower())))
# => ['avocat', 'Banane', 'Cerise', 'abricot']
"""
- Sans key, les majuscules passent avant les minuscules (ordre Unicode, cf.
  chap. 9). m.lower() compare tout en minuscules. On aurait pu écrire
  key=str.lower directement.
- Avec un tuple (longueur, mot en minuscules), on trie d'abord par longueur,
  puis par ordre alphabétique pour départager. "avocat", "Banane" et
  "Cerise" ont 6 lettres (et "avocat" < "banane" < "cerise" en minuscules),
  "abricot" en a 7, il arrive en dernier.
"""


#######################
#  map() et filter()  #
#######################

"""
21. Sans exécuter, que vaut chaque expression ?
"""
print(list(map(len, ["a", "bb", "ccc"])))          # => [1, 2, 3]
print(list(filter(lambda x: x > 2, [1, 5, 2, 8])))  # => [5, 8]
print(list(map(str.upper, "abc")))                  # => ['A', 'B', 'C']
"""
Le 3e cas : une chaîne est itérable, map() applique str.upper à chaque
caractère et renvoie une liste de 3 chaînes.
"""


"""
22. Convertir une ligne de mesures avec map() :
"""
saisie = "12.5;13;11.75;14"
mesures = list(map(float, saisie.split(";")))
print(mesures)                       # => [12.5, 13.0, 11.75, 14.0]
print(sum(mesures) / len(mesures))   # => 12.8125
"""
split(";") donne une liste de chaînes, et map(float, …) convertit chacune.
Le list() est indispensable pour pouvoir utiliser len() (un objet map n'a
pas de longueur).
"""


"""
23. Garder les e-mails valides avec filter() :
"""
adresses = ["ada@mail.fr", "pas-un-mail", "alan@ex.com", ""]
print(list(filter(lambda a: "@" in a, adresses)))
# => ['ada@mail.fr', 'alan@ex.com']


"""
24. Les mêmes calculs en compréhensions :
"""
nombres = [3, -1, 4, -5]
mots = ["ananas", "kiwi", "abricot"]
print(list(map(lambda x: x * 10, nombres)))      # => [30, -10, 40, -50]
print([x * 10 for x in nombres])                 # => [30, -10, 40, -50]

print(list(filter(lambda m: m.startswith("a"), mots)))
# => ['ananas', 'abricot']
print([m for m in mots if m.startswith("a")])  # => ['ananas', 'abricot']

print(list(map(lambda x: x ** 2, filter(lambda x: x < 0, nombres))))
# => [1, 25]
print([x ** 2 for x in nombres if x < 0])      # => [1, 25]
"""
Les compréhensions sont plus courtes et se lisent comme une phrase : c'est
pour cela qu'on les préfère en Python dès qu'il faut écrire une lambda.
"""


"""
25. Sans exécuter, qu'affiche ce programme ?
"""
doubles = map(lambda x: 2 * x, [1, 2, 3])
print(sum(doubles))  # => 12
print(sum(doubles))  # => 0
"""
map() renvoie un itérateur, qui s'ÉPUISE après un parcours (cf. chap. 23).
Le 1er sum() consomme toutes les valeurs ; le 2e ne trouve plus rien et
renvoie 0 (la somme de "rien"). Pour réutiliser les valeurs, il faut les
ranger dans une liste : doubles = list(map(…)).
"""


######################################
#  Fonctions imbriquées et closures  #
######################################

"""
26. Une fabrique de salutations :
"""


def fabrique_salutation(formule):
    def saluer(prenom):
        return f"{formule}, {prenom} !"
    return saluer


bonjour = fabrique_salutation("Bonjour")
salut = fabrique_salutation("Salut")
print(bonjour("Ada"))   # => Bonjour, Ada !
print(salut("Alan"))    # => Salut, Alan !
"""
Chaque appel à fabrique_salutation() crée une nouvelle fonction saluer, qui
se souvient de SA formule. On aurait aussi pu renvoyer
lambda prenom: f"{formule}, {prenom} !".
"""


"""
27. Une fabrique de tests de seuil, utilisée avec filter() :
"""


def fabrique_seuil(seuil):
    return lambda valeur: valeur > seuil


depasse_25 = fabrique_seuil(25)
temperatures = [18.2, 26.5, 31.0, 24.9, 25.1]
print(list(filter(depasse_25, temperatures)))  # => [26.5, 31.0, 25.1]
print(depasse_25(25))                          # => False (25 n'est pas > 25)


"""
28. Sans exécuter, qu'affiche ce programme ?
"""


def f_ajout(n):
    return lambda x: x + n


g_1 = f_ajout(1)
h_10 = f_ajout(10)
print(g_1(5), h_10(5), f_ajout(100)(5))  # => 6 15 105
"""
(Les fonctions sont renommées ici pour ne pas écraser f, g et h, définies
plus haut.) g_1 ajoute 1, h_10 ajoute 10. f_ajout(100)(5) crée une fonction
qui ajoute 100 et l'appelle immédiatement avec 5.
"""


"""
29. Un compteur de mots gardé par une closure :
"""


def fabrique_compteur_mots():
    compteurs = {}                  # dictionnaire "mémorisé" par la closure

    def ajouter(mot):
        compteurs[mot] = compteurs.get(mot, 0) + 1
        return compteurs[mot]
    return ajouter


compter = fabrique_compteur_mots()
print(compter("chat"))   # => 1
print(compter("chien"))  # => 1
print(compter("chat"))   # => 2
"""
Pas besoin de nonlocal ici : on ne RÉAFFECTE pas compteurs (pas de
"compteurs = …"), on MODIFIE le dictionnaire existant. C'est la même règle
que pour une liste globale modifiée dans une fonction (cf. chap. 19).
Chaque appel à fabrique_compteur_mots() crée un compteur indépendant.
"""
