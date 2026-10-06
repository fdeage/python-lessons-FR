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
#  Chap. 34     #  Programmation orientée objet I : classes et instances       #
#               #                                                              #
################################################################################
#
#  - Pourquoi la programmation orientée objet ?
#  - En Python, tout est objet
#  - Classe et instance
#  - Définir une classe : le mot-clé "class"
#  - Le constructeur __init__
#  - Le paramètre self
#  - Les attributs d'instance
#  - Les méthodes
#  - Attributs de classe et attributs d'instance
#  - Afficher un objet : __str__ et __repr__
#  - Objets mutables et références
#  - Exemple complet : un relevé de notes
#  - En bref
#
#############################################


# Pourquoi la programmation orientée objet ?
#############################################

"""
Jusqu'ici, nous avons manipulé deux sortes de choses bien séparées :
    - des DONNÉES, rangées dans des variables (int, str, list, dict…),
    - des TRAITEMENTS, écrits dans des fonctions (chap. 14-15).

Imaginons que l'on gère des comptes bancaires. Avec ce que l'on sait déjà, on
pourrait représenter chaque compte par un dictionnaire (cf. chap. 18), et
écrire des fonctions qui le manipulent :
"""
compte_ada = {"titulaire": "Ada", "solde": 100}


def deposer(compte, montant):
    compte["solde"] = compte["solde"] + montant


deposer(compte_ada, 50)
print(compte_ada["solde"])  # => 150

"""
Ça marche, mais plusieurs problèmes apparaissent quand le programme grossit :
    - rien ne garantit qu'un compte a bien les clés "titulaire" et "solde"
      (une faute de frappe, "sold", et tout plante plus loin) ;
    - la fonction deposer() est "à côté" des données : rien n'indique qu'elle
      ne sert qu'aux comptes, ni où chercher les autres fonctions liées ;
    - si l'on change la structure du dictionnaire, il faut retrouver et
      modifier toutes les fonctions qui l'utilisent.

La programmation orientée objet (POO, ou OOP en anglais pour "Object-Oriented
Programming") propose de REGROUPER données et traitements dans une même
structure : l'OBJET.

Un objet, c'est :
    - un état : des données qui le décrivent (on parle d'ATTRIBUTS) ;
    - un comportement : des fonctions qui agissent sur ces données (on parle
      de MÉTHODES).

Un compte bancaire a un titulaire et un solde (ses attributs) ; on peut y
déposer ou retirer de l'argent (ses méthodes).

La POO n'est pas obligatoire : beaucoup de scripts de Data Science s'en
passent très bien. Mais elle est partout dans les bibliothèques que vous
utiliserez (pandas, numpy, matplotlib…) : la comprendre, c'est comprendre
comment ces outils fonctionnent.
"""


# En Python, tout est objet
############################

"""
Bonne nouvelle : vous utilisez déjà des objets depuis le début du cours !

En Python, TOUTES les valeurs sont des objets : les entiers, les chaînes, les
listes, les fonctions… Chaque objet a un TYPE, que l'on obtient avec type()
(cf. chap. 6). Regardez bien ce qu'affiche type() :
"""
print(type(42))         # => <class 'int'>
print(type("bonjour"))  # => <class 'str'>
print(type([1, 2]))     # => <class 'list'>
print(type({"a": 1}))   # => <class 'dict'>

"""
Le mot "class" n'est pas là par hasard : en Python, "type" et "classe" sont
synonymes. int, str, list et dict sont des classes, et 42, "bonjour"… sont des
objets de ces classes.

Et les "méthodes" que l'on appelle avec un point depuis le chap. 7, ce sont
justement des fonctions attachées à un objet :
"""
phrase = "le python, c'est bon"
print(phrase.upper())      # => LE PYTHON, C'EST BON
print(phrase.count("o"))   # => 2

notes = [12, 8, 15]
notes.append(17)           # la méthode modifie l'objet "notes" lui-même
print(notes)               # => [12, 8, 15, 17]

"""
"phrase.upper()" se lit : "demande à l'objet phrase d'exécuter sa méthode
upper()". La méthode connaît l'objet sur lequel elle est appelée : on n'a pas
besoin de lui redonner "phrase" en argument.

Même les nombres ont des méthodes (moins connues) :
"""
print((255).bit_length())  # => 8 (nombre de bits pour écrire 255 en binaire)
print((3.5).is_integer())  # => False
# Note : les parenthèses autour de 255 évitent que Python lise "255." comme
# un float.

"""
dir(objet) liste tout ce que l'objet sait faire (cf. chap. 22). Les noms
entourés de doubles underscores ("__add__", "__len__"…) sont des méthodes
spéciales, utilisées en coulisses par Python : on les retrouvera plus bas, et
au chap. 35.
"""
print("upper" in dir(phrase))  # => True

"""
Ce chapitre va vous apprendre à créer VOS PROPRES types d'objets.
"""


# Classe et instance
#####################

"""
IMPT : deux mots à bien distinguer.

    - Une CLASSE est un modèle, un plan de construction. Elle décrit quels
      attributs et quelles méthodes auront les objets de ce type.
    - Une INSTANCE est un objet concret, fabriqué à partir de ce modèle.

Analogie : la classe est le plan d'architecte d'une maison ; les instances sont
les maisons construites d'après ce plan. Toutes ont la même structure (des
murs, un toit, des fenêtres), mais chacune a ses propres valeurs (couleur des
volets, adresse, propriétaire…). Repeindre les volets d'une maison ne change
pas ceux des voisines.

Avec les types que l'on connaît :
    - list est une classe ;
    - [1, 2] et ["a", "b", "c"] sont deux instances de list.

On dit aussi qu'"on INSTANCIE une classe" quand on crée un objet à partir
d'elle. Pour les types intégrés, on l'a déjà fait sans le savoir :
"""
liste_vide = list()   # on instancie la classe list
print(liste_vide)     # => []
nombre = int("42")    # on instancie la classe int à partir d'une chaîne
print(nombre)         # => 42

# isinstance(objet, classe) teste si un objet est une instance d'une classe :
print(isinstance(nombre, int))  # => True
print(isinstance(nombre, str))  # => False


# Définir une classe : le mot-clé "class"
##########################################

"""
On définit une classe avec le mot-clé "class", suivi de son nom et de ":".
Tout le bloc indenté qui suit est le corps de la classe (comme pour "def").

Convention (PEP 8, cf. chap. 20) : les noms de classes s'écrivent en
"PascalCase" (ou "CamelCase") : une majuscule à chaque mot, sans underscore.
CompteBancaire, Etudiant, ReleveDeNotes… C'est ce qui permet de reconnaître une
classe au premier coup d'œil (cf. chap. 15).

La classe la plus simple possible, vide :
"""


class Chien:
    pass  # "pass" : un bloc qui ne fait rien (cf. chap. 12)


"""
Pour créer une instance, on APPELLE la classe comme une fonction, avec des
parenthèses :
"""
rex = Chien()
medor = Chien()

print(type(rex))         # => <class '__main__.Chien'>
print(rex == medor)      # => False (deux objets distincts, cf. chap. 21)
print(isinstance(rex, Chien))  # => True

"""
"__main__" est le nom du module courant, c'est-à-dire du fichier exécuté
(cf. chap. 22) : la classe Chien a été définie dans ce fichier.

Même vide, une instance peut recevoir des attributs : on y accède avec un point
"objet.attribut", comme pour les méthodes :
"""
rex.nom = "Rex"
rex.age = 3
print(rex.nom, rex.age)  # => Rex 3

# medor n'a pas reçu d'attribut "nom" : y accéder provoque une AttributeError
try:
    print(medor.nom)
except AttributeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Ajouter des attributs "à la main", objet par objet, n'est pas une bonne idée :
on retombe dans les problèmes du dictionnaire (oublis, fautes de frappe…).
La solution : le constructeur.
"""


# Le constructeur __init__
###########################

"""
Une classe peut définir une méthode spéciale nommée __init__ (deux
underscores de chaque côté, on dit "dunder init", pour "double underscore").

IMPT : __init__ est appelée AUTOMATIQUEMENT à chaque création d'une instance.
Son rôle est d'INITIALISER l'objet : lui donner ses attributs de départ.
On l'appelle "le constructeur" (en toute rigueur, c'est l'"initialiseur").
"""


class Chat:
    def __init__(self, nom, age):
        print(f"(Création d'un chat nommé {nom})")
        self.nom = nom
        self.age = age


felix = Chat("Félix", 4)  # => (Création d'un chat nommé Félix)
print(felix.nom)          # => Félix
print(felix.age)          # => 4

"""
Déroulons pas à pas ce qui se passe à la ligne felix = Chat("Félix", 4) :

    1. Python crée un nouvel objet Chat, encore vide.
    2. Il appelle Chat.__init__ en lui passant : l'objet tout neuf (qui
       arrive dans le paramètre "self"), puis "Félix" (dans "nom") et 4
       (dans "age").
    3. __init__ exécute self.nom = nom et self.age = age : il attache deux
       attributs à l'objet.
    4. L'objet, maintenant initialisé, est affecté à la variable felix.

On ne passe donc PAS self à l'appel : Chat("Félix", 4) a deux arguments pour
trois paramètres (self, nom, age). Python fournit self lui-même.

Comme pour toute fonction, oublier un argument provoque une TypeError :
"""
try:
    garfield = Chat("Garfield")
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# Note : avant Python 3.10, le message dit "__init__() missing…" sans le nom
# de la classe devant.

"""
Attention aux fautes : "__init__" s'écrit avec DEUX underscores de chaque côté.
Écrire "_init_" ou "__int__" ne provoque pas d'erreur à la définition, mais la
méthode ne sera jamais appelée automatiquement !

Les paramètres de __init__ peuvent avoir des valeurs par défaut, comme toute
fonction (cf. chap. 15) :
"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


origine = Point()
p = Point(3, 4)
q = Point(y=7)            # argument nommé
print(origine.x, origine.y)  # => 0 0
print(p.x, p.y)              # => 3 4
print(q.x, q.y)              # => 0 7


# Le paramètre self
####################

"""
IMPT : "self" désigne l'instance sur laquelle on travaille. C'est TOUJOURS le
premier paramètre d'une méthode.

Pourquoi en a-t-on besoin ? Parce que le code de la classe est écrit UNE fois,
mais servira pour des milliers d'instances. Quand on écrit self.nom = nom dans
__init__, il faut bien dire à QUEL objet on attache le nom : à celui qui est
en train d'être créé, c'est-à-dire self.

    - Pendant la création de felix, self EST felix.
    - Pendant la création d'un autre chat, self est cet autre chat.

Une façon de le voir : self est une variable qui contient l'objet, exactement
comme felix. On peut le vérifier en comparant les deux avec "is", qui teste si
deux noms désignent le même objet (cf. chap. 21) :
"""


class Temoin:
    def __init__(self):
        Temoin.dernier_self = self  # on garde une trace de self (cf. plus bas)


t = Temoin()
print(Temoin.dernier_self is t)  # => True : self et t sont le même objet

"""
Le nom "self" n'est qu'une convention : Python accepterait n'importe quel nom
("moi", "this"…). Mais TOUT le monde écrit self, et les éditeurs comme les
autres programmeurs s'y attendent : respectez cette convention.

Erreur fréquente : oublier "self." devant un attribut. Dans ce cas, on crée
une simple variable locale à la fonction (cf. chap. 19), qui disparaît à la fin
de __init__ :
"""


class Oubli:
    def __init__(self, valeur):
        valeur_stockee = valeur  # oubli de "self." : variable locale !


o = Oubli(10)
try:
    print(o.valeur_stockee)
except AttributeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")


# Les attributs d'instance
###########################

"""
Les attributs créés via self.xxx dans __init__ sont des ATTRIBUTS D'INSTANCE :
chaque objet possède les siens, indépendants de ceux des autres objets.
"""


class Etudiant:
    def __init__(self, prenom, promo):
        self.prenom = prenom
        self.promo = promo
        self.notes = []  # un attribut peut avoir une valeur de départ fixe


alice = Etudiant("Alice", 2024)
bob = Etudiant("Bob", 2025)
print(alice.prenom, alice.promo)  # => Alice 2024
print(bob.prenom, bob.promo)      # => Bob 2025

"""
On peut lire un attribut, mais aussi le MODIFIER, de l'extérieur, comme une
variable :
"""
bob.promo = 2026
print(bob.promo)    # => 2026
print(alice.promo)  # => 2024 (alice n'est pas affectée)

# Chaque étudiant a SA propre liste de notes :
alice.notes.append(15)
print(alice.notes)  # => [15]
print(bob.notes)    # => []

"""
Pour voir tous les attributs d'instance d'un objet, on peut afficher son
__dict__ : c'est un dictionnaire attribut → valeur. Pratique pour déboguer.
"""
print(alice.__dict__)  # => {'prenom': 'Alice', 'promo': 2024, 'notes': [15]}

"""
getattr(objet, "nom") et hasattr(objet, "nom") permettent de lire ou tester un
attribut dont le nom est dans une chaîne :
"""
print(hasattr(alice, "promo"))         # => True
print(hasattr(alice, "age"))           # => False
print(getattr(alice, "prenom"))        # => Alice
print(getattr(alice, "age", "inconnu"))  # => inconnu (valeur par défaut)


# Les méthodes
###############

"""
Une MÉTHODE est une fonction définie DANS une classe. Comme __init__, elle
reçoit self en premier paramètre, ce qui lui donne accès aux attributs de
l'objet.

Reprenons le compte bancaire du début, cette fois en POO :
"""


class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde = self.solde + montant

    def retirer(self, montant):
        if montant > self.solde:
            print(f"Refusé : solde insuffisant ({self.solde} €)")
            return False
        self.solde = self.solde - montant
        return True

    def afficher(self):
        print(f"Compte de {self.titulaire} : {self.solde} €")


compte = CompteBancaire("Ada", 100)
compte.afficher()          # => Compte de Ada : 100 €
compte.deposer(50)
compte.afficher()          # => Compte de Ada : 150 €
print(compte.retirer(30))  # => True
print(compte.retirer(500))
# => Refusé : solde insuffisant (120 €)
# => False
compte.afficher()          # => Compte de Ada : 120 €

"""
Remarquez :
    - Les méthodes sont indentées DANS la classe, au même niveau que
      __init__. On laisse une ligne vide entre deux méthodes (PEP 8).
    - Une méthode peut retourner une valeur (retirer() retourne un booléen),
      ou juste modifier l'objet (deposer() retourne None, cf. chap. 15).
    - À l'appel, on ne passe pas self : compte.deposer(50) a UN argument.

IMPT : compte.deposer(50) est en fait un raccourci pour
CompteBancaire.deposer(compte, 50). Python transforme l'objet placé avant le
point en premier argument : c'est lui qui arrive dans self.
"""
CompteBancaire.deposer(compte, 10)  # forme "longue", équivalente
compte.afficher()                   # => Compte de Ada : 130 €

"""
Erreur classique : oublier self dans la définition d'une méthode. Python passe
quand même l'objet en premier argument… et il y en a un de trop :
"""


class Distrait:
    def saluer():  # oubli de self !
        print("Bonjour")


d = Distrait()
try:
    d.saluer()
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Une méthode peut appeler une autre méthode du même objet, toujours via self :
"""


class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

    def est_carre(self):
        return self.largeur == self.hauteur

    def decrire(self):
        # on appelle les autres méthodes avec "self." devant
        return (f"{self.largeur}x{self.hauteur} : aire {self.aire()}, "
                f"périmètre {self.perimetre()}")


r = Rectangle(3, 4)
print(r.aire())       # => 12
print(r.est_carre())  # => False
print(r.decrire())    # => 3x4 : aire 12, périmètre 14

"""
Conseil de conception : une méthode qui CALCULE quelque chose devrait le
retourner (return) plutôt que l'afficher (print), pour que l'on puisse
réutiliser le résultat (cf. chap. 15). C'est pourquoi decrire() retourne une
chaîne au lieu d'appeler print().
"""


# Attributs de classe et attributs d'instance
##############################################

"""
On peut aussi définir des variables directement dans le corps de la classe,
en dehors de toute méthode. Ce sont des ATTRIBUTS DE CLASSE : ils sont
PARTAGÉS par toutes les instances.

C'est utile pour une constante commune à tous les objets, ou un compteur.
"""


class Voiture:
    nb_roues = 4         # attribut de classe : commun à toutes les voitures
    nb_voitures = 0      # compteur d'instances créées

    def __init__(self, marque):
        self.marque = marque          # attribut d'instance : propre à chacune
        Voiture.nb_voitures += 1      # on modifie l'attribut DE LA CLASSE


v1 = Voiture("Renault")
v2 = Voiture("Peugeot")
print(v1.nb_roues, v2.nb_roues)  # => 4 4
print(Voiture.nb_roues)          # => 4 (accessible via la classe aussi)
print(Voiture.nb_voitures)       # => 2

"""
Comment Python trouve-t-il v1.nb_roues ? Il cherche d'abord dans les attributs
de l'instance (v1.__dict__) ; s'il ne trouve pas, il cherche dans la classe.
"""
print(v1.__dict__)  # => {'marque': 'Renault'} (nb_roues n'y est pas !)

"""
IMPT : piège n°1. Affecter un attribut via une INSTANCE crée un attribut
d'instance qui "masque" l'attribut de classe, au lieu de le modifier :
"""
v1.nb_roues = 3                 # crée un attribut d'instance sur v1 seulement
print(v1.nb_roues)              # => 3
print(v2.nb_roues)              # => 4 (inchangé)
print(Voiture.nb_roues)         # => 4 (inchangé)
print(v1.__dict__)              # => {'marque': 'Renault', 'nb_roues': 3}

"""
C'est pour ça que, dans __init__, on a écrit Voiture.nb_voitures += 1 et non
self.nb_voitures += 1 : la seconde version créerait un attribut d'instance
valant 1, sans jamais toucher au compteur partagé.

IMPT : piège n°2, plus sournois. Un attribut de classe MUTABLE (une liste, un
dictionnaire) est partagé : si une instance le modifie en place (append…),
toutes les instances voient la modification.
"""


class Equipe:
    membres = []  # ERREUR : une seule liste, partagée par TOUTES les équipes

    def __init__(self, nom):
        self.nom = nom

    def recruter(self, personne):
        self.membres.append(personne)  # modifie la liste de la CLASSE


rouge = Equipe("Rouge")
bleue = Equipe("Bleue")
rouge.recruter("Alice")
print(bleue.membres)  # => ['Alice'] (!!! Alice est aussi chez les bleus)

"""
Ici, self.membres.append() ne crée pas d'attribut d'instance (on ne fait pas
d'affectation "self.membres = …") : Python trouve la liste dans la classe et
la modifie. Correction : créer la liste dans __init__, une par instance.
"""


class EquipeCorrigee:
    def __init__(self, nom):
        self.nom = nom
        self.membres = []  # une NOUVELLE liste pour chaque équipe

    def recruter(self, personne):
        self.membres.append(personne)


rouge = EquipeCorrigee("Rouge")
bleue = EquipeCorrigee("Bleue")
rouge.recruter("Alice")
print(rouge.membres)  # => ['Alice']
print(bleue.membres)  # => []

"""
Règle simple : les attributs de classe pour les constantes (nombres, chaînes,
tuples) partagées ; tout le reste dans __init__.
"""


# Afficher un objet : __str__ et __repr__
##########################################

"""
Que se passe-t-il si l'on affiche directement un objet ?
"""
print(r)  # => <__main__.Rectangle object at 0x7f…> (l'adresse varie)

"""
Python affiche le nom de la classe et l'adresse mémoire de l'objet (comme pour
les fonctions, cf. chap. 15) : pas très utile.

Pour choisir ce qu'affiche print(), on définit la méthode spéciale __str__.
Elle doit RETOURNER une chaîne (pas l'afficher) :
"""


class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def __str__(self):
        return f"« {self.titre} », {self.auteur} ({self.annee})"

    def __repr__(self):
        return f"Livre({self.titre!r}, {self.auteur!r}, {self.annee!r})"


livre = Livre("Les Misérables", "Victor Hugo", 1862)
print(livre)       # => « Les Misérables », Victor Hugo (1862)
print(str(livre))  # => « Les Misérables », Victor Hugo (1862)
print(f"Je lis {livre}.")  # => Je lis « Les Misérables », Victor Hugo (1862).

"""
print(), str() et les f-strings appellent tous __str__ en coulisses.

__repr__ est l'autre méthode d'affichage. La différence :
    - __str__ : une représentation LISIBLE, pour l'utilisateur final ;
    - __repr__ : une représentation NON AMBIGUË, pour le programmeur. Par
      convention, elle ressemble si possible au code qui recrée l'objet.

On voit __repr__ quand on tape l'objet seul dans la console Python, quand on
appelle repr(), et quand l'objet est DANS un conteneur (liste, dict…) :
"""
print(repr(livre))  # => Livre('Les Misérables', 'Victor Hugo', 1862)
bibliotheque = [livre, Livre("Germinal", "Émile Zola", 1885)]
print(bibliotheque)
# => [Livre('Les Misérables', 'Victor Hugo', 1862), Livre('Germinal', 'Émile Zola', 1885)]

"""
Le "!r" dans la f-string de __repr__ applique repr() à la valeur : c'est ce
qui ajoute les guillemets autour des chaînes. On connaît déjà cette différence
pour les types intégrés :
"""
print(str("abc"))   # => abc
print(repr("abc"))  # => 'abc'

"""
Conseil : définissez au moins __repr__ dans vos classes. Si __str__ n'existe
pas, Python utilise __repr__ à sa place ; l'inverse n'est pas vrai.
"""


class Temperature:
    def __init__(self, degres):
        self.degres = degres

    def __repr__(self):
        return f"Temperature({self.degres})"


print(Temperature(21.5))    # => Temperature(21.5) (pas de __str__ : __repr__)


# Objets mutables et références
################################

"""
Les objets que l'on crée avec nos classes sont MUTABLES : on peut modifier
leurs attributs après création. Ils se comportent donc comme les listes et les
dictionnaires vis-à-vis de l'affectation (cf. chap. 19 et 24).

IMPT : une variable ne contient pas l'objet, mais une RÉFÉRENCE vers lui.
"autre = compte" ne copie pas le compte : les deux noms désignent le MÊME
objet.
"""
c1 = CompteBancaire("Bob", 100)
c2 = c1              # pas de copie ! c2 et c1 désignent le même compte
c2.deposer(50)
print(c1.solde)      # => 150 (c1 "voit" le dépôt fait via c2)
print(c1 is c2)      # => True

"""
Même chose quand on passe un objet à une fonction : la fonction reçoit une
référence vers l'objet, et peut donc le modifier (comme une liste, cf.
chap. 24).
"""


def offrir_bonus(un_compte):
    un_compte.deposer(10)


offrir_bonus(c1)
print(c1.solde)      # => 160

"""
Pour obtenir une vraie copie indépendante, on utilise le module copy
(cf. chap. 24) : copy.copy() pour une copie superficielle, copy.deepcopy() si
l'objet contient lui-même des objets mutables (des listes, par exemple).
"""
import copy

c3 = copy.copy(c1)
c3.deposer(1000)
print(c1.solde, c3.solde)  # => 160 1160 (c1 n'a pas bougé)
print(c1 is c3)            # => False

"""
Par défaut, "==" entre deux objets de nos classes compare les IDENTITÉS (comme
"is"), et non le contenu : deux comptes identiques mais distincts ne sont pas
"égaux". On verra au chap. 35 comment définir sa propre égalité avec __eq__.
"""
a = Point(1, 2)
b = Point(1, 2)
print(a == b)  # => False (deux objets distincts, même contenu)
print(a == a)  # => True


# Exemple complet : un relevé de notes
#######################################

"""
Rassemblons tout ce que l'on a vu dans une classe un peu plus réaliste, comme
on pourrait en écrire pour analyser les résultats d'une classe d'élèves.
"""


class Releve:
    """Relevé des notes d'un élève, sur 20."""

    note_max = 20  # attribut de classe : constante commune à tous les relevés

    def __init__(self, eleve):
        self.eleve = eleve
        self.notes = {}  # matière -> liste de notes (une par instance !)

    def ajouter(self, matiere, note):
        """Ajoute une note, après vérification."""
        if not 0 <= note <= Releve.note_max:
            raise ValueError(f"Note invalide : {note}")  # cf. chap. 26
        if matiere not in self.notes:
            self.notes[matiere] = []
        self.notes[matiere].append(note)

    def moyenne(self, matiere):
        """Moyenne d'une matière (None si aucune note)."""
        liste = self.notes.get(matiere, [])
        if not liste:
            return None
        return sum(liste) / len(liste)

    def moyenne_generale(self):
        """Moyenne des moyennes de chaque matière."""
        moyennes = [self.moyenne(m) for m in self.notes]  # cf. chap. 23
        if not moyennes:
            return None
        return sum(moyennes) / len(moyennes)

    def meilleure_matiere(self):
        return max(self.notes, key=self.moyenne)  # cf. chap. 27

    def __str__(self):
        lignes = [f"Relevé de {self.eleve}"]
        for matiere in sorted(self.notes):
            lignes.append(f"  {matiere:<10} {self.moyenne(matiere):5.2f}")
        lignes.append(f"  {'Général':<10} {self.moyenne_generale():5.2f}")
        return "\n".join(lignes)

    def __repr__(self):
        return f"Releve({self.eleve!r})"


releve = Releve("Camille")
releve.ajouter("maths", 14)
releve.ajouter("maths", 17)
releve.ajouter("histoire", 12)
releve.ajouter("anglais", 16)
releve.ajouter("anglais", 13)

print(releve.moyenne("maths"))     # => 15.5
print(releve.moyenne("physique"))  # => None
print(releve.meilleure_matiere())  # => maths
print(releve)
# => Relevé de Camille
# =>   anglais    14.50
# =>   histoire   12.00
# =>   maths      15.50
# =>   Général    14.00

# La vérification de ajouter() protège l'objet contre les données absurdes :
try:
    releve.ajouter("maths", 25)
except ValueError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Remarquez :
    - la docstring de la classe et des méthodes (cf. chap. 14), que l'on
      retrouve avec help(Releve) ;
    - key=self.moyenne : une méthode passée en argument, SANS parenthèses
      (on donne la méthode elle-même, max() l'appellera pour chaque matière) ;
    - l'objet garantit sa propre cohérence : on ne peut pas ajouter de note
      hors de [0, 20] en passant par ajouter().

On peut maintenant gérer toute une classe d'élèves, en mettant les relevés
dans une liste :
"""
classe = [Releve("Camille"), Releve("Dominique")]
classe[0].ajouter("maths", 15)
classe[1].ajouter("maths", 9)
classe[1].ajouter("maths", 13)
for r in classe:
    print(r.eleve, r.moyenne_generale())
# => Camille 15.0
# => Dominique 11.0
print(classe)  # => [Releve('Camille'), Releve('Dominique')]


# En bref
##########

"""
    class NomDeClasse:                 # PascalCase
        attribut_de_classe = valeur    # partagé par toutes les instances

        def __init__(self, a, b):      # appelée à la création
            self.a = a                 # attributs d'instance
            self.b = b

        def methode(self, x):          # self en 1er paramètre, toujours
            return self.a + x

        def __str__(self):             # pour print() et str()
            return "..."

        def __repr__(self):            # pour repr(), la console, les listes
            return "NomDeClasse(...)"

    objet = NomDeClasse(1, 2)          # instanciation (pas de self à passer)
    objet.methode(10)                  # = NomDeClasse.methode(objet, 10)

À retenir :
    - classe = modèle ; instance = objet concret créé à partir du modèle ;
    - self = l'instance en cours ; oublier "self." crée une variable locale ;
    - les attributs mutables se créent dans __init__, jamais au niveau de la
      classe ;
    - une variable contient une référence : "=" ne copie pas un objet.

Au chap. 35, on verra comment des classes peuvent hériter les unes des
autres, et comment rendre nos objets compatibles avec ==, <, len(), +, for…
"""
