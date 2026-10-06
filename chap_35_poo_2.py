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
#  Chap. 35     #  Programmation orientée objet II : héritage et cie           #
#               #                                                              #
################################################################################
#
#  - L'héritage
#  - Redéfinir une méthode
#  - Appeler la classe parente : super()
#  - isinstance() et issubclass()
#  - Créer ses propres exceptions
#  - Les méthodes spéciales
#  - Comparer des objets : __eq__ et __lt__
#  - Se comporter comme un conteneur : __len__, __getitem__, __iter__
#  - Les opérateurs : __add__
#  - Encapsulation : _ et __
#  - Les propriétés : @property
#  - Bonus : @classmethod et @staticmethod
#  - Composition ou héritage ?
#  - Bonus : les dataclasses
#  - En bref
#
#############################################

"""
Ce chapitre suppose que vous maîtrisez le chap. 34 : classe, instance, self,
__init__, attributs et méthodes, __str__ et __repr__.
"""


# L'héritage
#############

"""
Souvent, plusieurs classes se ressemblent : un chat et un chien sont tous les
deux des animaux, avec un nom et un âge ; un compte épargne est un compte
bancaire avec, en plus, un taux d'intérêt.

Plutôt que de copier-coller le code commun (ce qui viole le principe DRY,
cf. chap. 14), on utilise l'HÉRITAGE : une classe ENFANT (ou "sous-classe",
"classe dérivée") hérite de tout ce que contient une classe PARENTE (ou
"superclasse", "classe de base"), et peut y ajouter ou modifier des choses.

Syntaxe : on met le nom de la classe parente entre parenthèses.
"""


class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

    def crier(self):
        return "..."


class Chien(Animal):  # Chien hérite de Animal
    def rapporter(self):  # méthode supplémentaire, propre aux chiens
        return f"{self.nom} rapporte la balle !"


rex = Chien("Rex", 3)  # __init__ est hérité d'Animal
print(rex.se_presenter())  # => Je m'appelle Rex et j'ai 3 ans.
print(rex.rapporter())     # => Rex rapporte la balle !
print(rex.crier())         # => ...

"""
Chien n'a défini ni __init__, ni se_presenter(), ni crier() : il les a hérités
d'Animal. Il a seulement ajouté rapporter().

L'héritage exprime une relation "EST UN" : un chien EST UN animal. Tout ce
qu'on peut faire avec un Animal, on peut le faire avec un Chien. L'inverse est
faux : un Animal quelconque ne sait pas rapporter la balle.
"""
generique = Animal("Bestiole", 1)
try:
    generique.rapporter()
except AttributeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Comment Python trouve-t-il rex.se_presenter ? Il cherche dans l'objet, puis
dans sa classe (Chien), puis dans la classe parente (Animal), et ainsi de
suite. La première méthode trouvée gagne.

Toutes les classes héritent, au bout de la chaîne, de la classe "object" :
c'est elle qui fournit les __repr__ ou __eq__ par défaut vus au chap. 34.
"""
print(Chien.__mro__)
# => (<class '__main__.Chien'>, <class '__main__.Animal'>, <class 'object'>)
# __mro__ ("Method Resolution Order") : l'ordre dans lequel Python cherche.


# Redéfinir une méthode
########################

"""
Une classe enfant peut REDÉFINIR (on dit aussi "surcharger", en anglais
"override") une méthode de son parent : il suffit de définir une méthode du
même nom. Celle de l'enfant est trouvée en premier, et masque celle du parent.
"""


class Chat(Animal):
    def crier(self):  # redéfinit Animal.crier
        return "Miaou"


class Vache(Animal):
    def crier(self):
        return "Meuh"


felix = Chat("Félix", 4)
print(felix.crier())  # => Miaou
print(Vache("Marguerite", 6).crier())  # => Meuh

"""
C'est là que l'héritage devient puissant : on peut écrire du code qui traite
des animaux "en général", sans savoir de quelle espèce ils sont. Chaque objet
utilise SA version de la méthode. On appelle cela le POLYMORPHISME (du grec
"plusieurs formes").
"""
ferme = [rex, felix, Vache("Marguerite", 6), Animal("Inconnu", 2)]
for bete in ferme:
    print(f"{bete.nom} : {bete.crier()}")
# => Rex : ...
# => Félix : Miaou
# => Marguerite : Meuh
# => Inconnu : ...

"""
On a déjà rencontré le polymorphisme sans le nommer : len() fonctionne sur une
str, une list, un dict… et "+" additionne des nombres mais concatène des
chaînes. Chaque type a sa propre façon de répondre à la même demande.
"""


# Appeler la classe parente : super()
######################################

"""
Souvent, on ne veut pas REMPLACER complètement la méthode du parent, mais la
COMPLÉTER. Pour appeler la version du parent depuis l'enfant, on utilise
super().

Cas le plus fréquent : l'enfant a besoin d'attributs en plus. Son __init__
doit alors faire tout ce que fait celui du parent, PLUS l'initialisation des
nouveaux attributs.
"""


class ChienGuide(Chien):
    def __init__(self, nom, age, maitre):
        super().__init__(nom, age)  # Animal.__init__ fait son travail…
        self.maitre = maitre        # … puis on ajoute l'attribut propre

    def se_presenter(self):
        debut = super().se_presenter()  # la version du parent…
        return f"{debut} Je guide {self.maitre}."  # … complétée


guide = ChienGuide("Pollux", 5, "M. Martin")
print(guide.se_presenter())
# => Je m'appelle Pollux et j'ai 5 ans. Je guide M. Martin.
print(guide.rapporter())  # => Pollux rapporte la balle ! (hérité de Chien)

"""
IMPT : si l'enfant définit son propre __init__, celui du parent n'est PLUS
appelé automatiquement. Oublier super().__init__(…) est une erreur classique :
les attributs du parent ne sont alors jamais créés.
"""


class ChienOublieux(Chien):
    def __init__(self, nom, age, couleur):
        self.couleur = couleur  # oubli de super().__init__(nom, age) !


oublieux = ChienOublieux("Médor", 2, "noir")
try:
    print(oublieux.se_presenter())
except AttributeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Un exemple plus concret, avec le compte bancaire du chap. 34 :
"""


class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def __repr__(self):
        return f"{type(self).__name__}({self.titulaire!r}, {self.solde})"


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde=0, taux=0.03):
        super().__init__(titulaire, solde)
        self.taux = taux

    def appliquer_interets(self):
        self.deposer(round(self.solde * self.taux, 2))  # méthode héritée


livret = CompteEpargne("Ada", 1000)
livret.appliquer_interets()
print(livret)  # => CompteEpargne('Ada', 1030.0)

"""
Astuce : dans __repr__, type(self).__name__ donne le nom de la classe RÉELLE
de l'objet. Le même __repr__, hérité, affiche donc "CompteEpargne" pour un
livret et "CompteBancaire" pour un compte simple.
"""
print(CompteBancaire("Bob", 20))  # => CompteBancaire('Bob', 20)


# isinstance() et issubclass()
###############################

"""
isinstance(objet, Classe) (cf. chap. 34) tient compte de l'héritage : un
objet est une instance de sa classe, mais aussi de toutes ses classes
parentes.
"""
print(isinstance(guide, ChienGuide))  # => True
print(isinstance(guide, Chien))       # => True (un ChienGuide EST UN Chien)
print(isinstance(guide, Animal))      # => True
print(isinstance(guide, Chat))        # => False
print(isinstance(felix, Chien))       # => False

# type() donne la classe exacte, sans tenir compte de l'héritage :
print(type(guide) == Chien)  # => False
print(type(guide).__name__)  # => ChienGuide

"""
issubclass(Enfant, Parent) teste la relation entre deux CLASSES :
"""
print(issubclass(ChienGuide, Animal))  # => True
print(issubclass(Animal, Chien))       # => False

# On peut tester plusieurs classes d'un coup avec un tuple :
print(isinstance(felix, (Chien, Chat)))  # => True

"""
Ça vous rappelle quelque chose ? Au chap. 26, on a vu que les exceptions
forment une hiérarchie : ZeroDivisionError hérite d'ArithmeticError, qui
hérite d'Exception… C'était déjà de l'héritage de classes !
"""
print(issubclass(ZeroDivisionError, ArithmeticError))  # => True
print(issubclass(ZeroDivisionError, Exception))        # => True
print(ZeroDivisionError.__mro__)
# => (<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)

"""
C'est pour cela que "except ArithmeticError" intercepte aussi les
ZeroDivisionError : Python utilise isinstance() pour choisir le bloc except.

Conseil : en général, préférez isinstance() à type() == …, justement parce
qu'il respecte l'héritage. Et si vous écrivez beaucoup de
"if isinstance(…) … elif isinstance(…)", c'est souvent le signe qu'une méthode
redéfinie dans chaque classe (polymorphisme) serait plus élégante.
"""


# Créer ses propres exceptions
###############################

"""
Puisque les exceptions sont des classes, on peut créer les siennes en héritant
d'Exception (ou d'une de ses sous-classes). C'est la pratique recommandée pour
signaler les erreurs propres à votre programme : elles ont un nom parlant, et
l'appelant peut les intercepter précisément.

La classe peut être vide : tout est hérité d'Exception.
"""


class SoldeInsuffisant(Exception):
    pass


class CompteBloque(Exception):
    """Levée quand on opère sur un compte bloqué."""


class CompteSecurise(CompteBancaire):
    def __init__(self, titulaire, solde=0):
        super().__init__(titulaire, solde)
        self.bloque = False

    def retirer(self, montant):
        if self.bloque:
            raise CompteBloque(f"le compte de {self.titulaire} est bloqué")
        if montant > self.solde:
            raise SoldeInsuffisant(
                f"retrait de {montant} € refusé, solde : {self.solde} €")
        self.solde -= montant


cs = CompteSecurise("Chloé", 50)
try:
    cs.retirer(80)
except SoldeInsuffisant as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

cs.bloque = True
try:
    cs.retirer(10)
except (SoldeInsuffisant, CompteBloque) as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : "
          f"{type(err).__name__}: {err})")

"""
On peut aussi créer sa propre hiérarchie d'exceptions, pour intercepter
toutes les erreurs d'un même domaine d'un coup :
"""


class ErreurDonnees(Exception):
    """Classe de base pour toutes les erreurs de données de notre programme."""


class ValeurManquante(ErreurDonnees):
    pass


class ValeurAberrante(ErreurDonnees):
    def __init__(self, colonne, valeur):
        super().__init__(f"valeur aberrante dans {colonne!r} : {valeur}")
        self.colonne = colonne  # on peut stocker des infos utiles
        self.valeur = valeur


def verifier_age(age):
    if age is None:
        raise ValeurManquante("âge non renseigné")
    if not 0 <= age <= 130:
        raise ValeurAberrante("age", age)
    return age


for age in [34, None, 212]:
    try:
        verifier_age(age)
        print(f"{age} : OK")
    except ErreurDonnees as err:  # intercepte les DEUX sous-classes
        print(f"{age} : problème ({type(err).__name__}) : {err}")
# => 34 : OK
# => None : problème (ValeurManquante) : âge non renseigné
# => 212 : problème (ValeurAberrante) : valeur aberrante dans 'age' : 212

"""
Convention : le nom d'une classe d'exception se termine souvent par "Error"
(en anglais) ou commence par "Erreur" : ValueError, KeyError…
"""


# Les méthodes spéciales
#########################

"""
On a vu au chap. 34 que __init__, __str__ et __repr__ sont appelées
"automatiquement" par Python. Ce sont des MÉTHODES SPÉCIALES (ou "méthodes
magiques", ou "dunder methods"). Il en existe des dizaines : chacune permet à
nos objets de réagir à une syntaxe ou une fonction intégrée de Python.

    Ce qu'on écrit      Ce que Python appelle
    --------------      ---------------------
    print(obj)          obj.__str__()
    a == b              a.__eq__(b)
    a < b               a.__lt__(b)
    len(obj)            obj.__len__()
    obj[i]              obj.__getitem__(i)
    for x in obj        obj.__iter__()
    a + b               a.__add__(b)
    x in obj            obj.__contains__(x)

C'est ainsi que les types intégrés fonctionnent : "abc" + "d" appelle en fait
"abc".__add__("d").
"""
print("abc".__add__("d"))  # => abcd
print([1, 2, 3].__len__())  # => 3

"""
On n'appelle quasiment jamais ces méthodes directement : on les DÉFINIT dans
nos classes, et on utilise la syntaxe normale (+, len(), ==…).
"""


# Comparer des objets : __eq__ et __lt__
#########################################

"""
Par défaut, a == b compare les identités (cf. chap. 34) : deux objets
distincts ne sont jamais égaux, même s'ils ont le même contenu. On change ce
comportement en définissant __eq__(self, autre), qui doit retourner un
booléen.
"""


class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError("dénominateur nul")
        self.num = num
        self.den = den

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __eq__(self, autre):
        # a/b == c/d  <=>  a*d == c*b (produit en croix)
        return self.num * autre.den == autre.num * self.den

    def __lt__(self, autre):
        # a/b < c/d  <=>  a*d < c*b (si b et d sont positifs)
        return self.num * autre.den < autre.num * self.den

    def __add__(self, autre):
        # a/b + c/d = (a*d + c*b) / (b*d)
        return Fraction(self.num * autre.den + autre.num * self.den,
                        self.den * autre.den)


un_demi = Fraction(1, 2)
deux_quarts = Fraction(2, 4)
un_tiers = Fraction(1, 3)

print(un_demi == deux_quarts)  # => True (grâce à __eq__)
print(un_demi != un_tiers)     # => True (Python déduit != de __eq__)
print(un_tiers < un_demi)      # => True (grâce à __lt__)
print(un_demi > un_tiers)      # => True (Python essaie un_tiers < un_demi)

"""
Avec __lt__, nos objets deviennent TRIABLES : sorted(), min() et max()
utilisent "<" pour comparer (cf. chap. 24).
"""
fractions = [Fraction(3, 4), un_tiers, un_demi, Fraction(1, 10)]
print(sorted(fractions))
# => [Fraction(1, 10), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)]
print(max(fractions))  # => 3/4 (print() utilise __str__)

"""
En revanche, on n'a pas défini __le__ ("<=") : Python ne peut pas le deviner.
"""
try:
    print(un_tiers <= un_demi)
except TypeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Pour obtenir toutes les comparaisons à partir de __eq__ et __lt__, le module
functools fournit le décorateur @total_ordering (on reparlera des décorateurs
au chap. 36). Les dataclasses (fin de ce chapitre) le font aussi.

Note : définir __eq__ rend les objets "non hashables" : on ne peut plus les
utiliser comme clés de dictionnaire ou dans un set (cf. chap. 18 et 25), sauf
à définir aussi __hash__. Ne vous en souciez que si vous en avez besoin.
"""


# Se comporter comme un conteneur : __len__, __getitem__, __iter__
###################################################################

"""
Créons une classe qui représente une série de mesures (par exemple des
températures relevées chaque jour). On aimerait l'utiliser comme une liste :
len(serie), serie[0], for t in serie…
"""


class Serie:
    def __init__(self, nom, valeurs):
        self.nom = nom
        self.valeurs = list(valeurs)  # copie : la série a sa propre liste

    def __repr__(self):
        return f"Serie({self.nom!r}, {self.valeurs})"

    def __len__(self):            # len(serie)
        return len(self.valeurs)

    def __getitem__(self, i):     # serie[i] et serie[a:b]
        return self.valeurs[i]

    def __iter__(self):           # for x in serie
        return iter(self.valeurs)  # on délègue à la liste (cf. chap. 23)

    def __contains__(self, x):    # x in serie
        return x in self.valeurs

    def moyenne(self):
        return sum(self.valeurs) / len(self)  # len(self) appelle __len__


temp = Serie("Lyon", [12.5, 14.0, 9.5, 11.0])
print(len(temp))       # => 4
print(temp[0])         # => 12.5
print(temp[-1])        # => 11.0
print(temp[1:3])       # => [14.0, 9.5] (les slices passent par __getitem__)
print(14.0 in temp)    # => True
for t in temp:
    print(t, end=" ")  # => 12.5 14.0 9.5 11.0
print()
print(temp.moyenne())  # => 11.75
print(max(temp))       # => 14.0 (max() parcourt l'objet grâce à __iter__)
print(sorted(temp))    # => [9.5, 11.0, 12.5, 14.0]

"""
Avec __len__, l'objet a aussi une valeur de vérité : une Serie vide est
"fausse" dans un if (comme une liste vide, cf. chap. 21).
"""
vide = Serie("Vide", [])
print(bool(vide))  # => False
print(bool(temp))  # => True

"""
C'est exactement ainsi que fonctionnent les Series et DataFrames de pandas
(cf. chap. 39) : des classes qui définissent __len__, __getitem__, __iter__,
__add__… pour se comporter "comme" des listes ou des tableaux.
"""


# Les opérateurs : __add__
###########################

"""
Notre Fraction plus haut définit __add__ : on peut donc les additionner avec
"+". __add__ doit RETOURNER un nouvel objet (sans modifier self ni autre),
comme 2 + 3 ne modifie ni 2 ni 3.
"""
total = un_demi + un_tiers
print(total)            # => 5/6
print(un_demi)          # => 1/2 (inchangé)
print(un_demi + un_demi + un_demi)  # => 12/8 (pas simplifiée : à vous !)

"""
Les autres opérateurs suivent le même modèle :
    __sub__ (-), __mul__ (*), __truediv__ (/), __floordiv__ (//),
    __mod__ (%), __pow__ (**), __neg__ (- unaire)…

Si l'opération n'a pas de sens, Python lève une TypeError :
"""
try:
    print(un_demi * un_tiers)  # __mul__ n'est pas défini
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Un exemple très courant en sciences : les vecteurs.
"""


class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"

    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __mul__(self, k):  # vecteur * nombre
        return Vecteur(self.x * k, self.y * k)

    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y

    def norme(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


u = Vecteur(1, 2)
v = Vecteur(3, -1)
print(u + v)                   # => Vecteur(4, 1)
print(u * 3)                   # => Vecteur(3, 6)
print(Vecteur(3, 4).norme())   # => 5.0
print(u + v == Vecteur(4, 1))  # => True

"""
Attention : u * 3 marche, mais 3 * u non ! Python appelle d'abord
(3).__mul__(u), que les int ne savent pas faire. Il faudrait définir aussi
__rmul__ (le "r" pour "right", l'opérande de droite).
"""
try:
    print(3 * u)
except TypeError as err:
    print(f"7: (Sans ce try: … except …, cette ligne créerait : {err})")


# Encapsulation : _ et __
##########################

"""
L'ENCAPSULATION consiste à cacher les détails internes d'un objet, pour que
l'extérieur ne les utilise qu'à travers ses méthodes. Exemple : on ne devrait
pas pouvoir écrire compte.solde = -1000000 sans passer par retirer().

Beaucoup de langages (Java, C++…) ont des mots-clés "private" ou "public".
Python, non : TOUT est accessible. À la place, il y a des CONVENTIONS :

    - un nom qui commence par UN underscore (_solde) signifie "interne :
      ne touchez pas à ça depuis l'extérieur". Rien ne l'empêche, mais c'est
      un avertissement clair entre programmeurs. ("Nous sommes entre adultes
      consentants", dit la communauté Python.)

    - un nom qui commence par DEUX underscores (__solde), sans en finir par
      deux, déclenche le "name mangling" : Python renomme l'attribut en
      _NomDeClasse__solde. Le but est surtout d'éviter les conflits de noms
      avec les classes enfants, pas de "sécuriser" la donnée.
"""


class Coffre:
    def __init__(self, contenu, code):
        self.contenu = contenu  # public
        self._code = code       # "interne" (convention)
        self.__secret = 42      # "name mangling"

    def ouvrir(self, code):
        if code == self._code:
            return self.contenu
        return "Code incorrect"


coffre = Coffre("lingots", "1234")
print(coffre.ouvrir("0000"))  # => Code incorrect
print(coffre.ouvrir("1234"))  # => lingots
print(coffre._code)           # => 1234 (possible… mais déconseillé !)

try:
    print(coffre.__secret)
except AttributeError as err:
    print(f"8: (Sans ce try: … except …, cette ligne créerait : {err})")

print(coffre._Coffre__secret)  # => 42 (le nom a juste été modifié)

"""
En pratique : utilisez "_" pour tout ce qui est interne (attributs ET
méthodes d'aide), et réservez "__" aux rares cas de conflits d'héritage.
Ne confondez pas avec les méthodes spéciales __xxx__, qui ont deux
underscores des DEUX côtés et ne sont pas concernées.
"""


# Les propriétés : @property
#############################

"""
Problème : on veut que les utilisateurs de notre classe écrivent simplement
compte.solde (sans parenthèses), mais on voudrait quand même CONTRÔLER les
modifications (refuser un solde négatif, par exemple).

La solution pythonique est la PROPRIÉTÉ : une méthode déguisée en attribut.
On la crée avec @property placé au-dessus de la méthode. (La syntaxe "@…" est
un "décorateur" : on les étudiera au chap. 36. Pour l'instant, retenez-la
comme une formule.)
"""


class Thermometre:
    def __init__(self, celsius):
        self.celsius = celsius  # passe déjà par le "setter" ci-dessous !

    @property
    def celsius(self):  # le "getter" : appelé quand on LIT t.celsius
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):  # le "setter" : appelé quand on ÉCRIT
        if valeur < -273.15:
            raise ValueError(f"{valeur} °C est sous le zéro absolu")
        self._celsius = valeur

    @property
    def fahrenheit(self):  # propriété calculée, en lecture seule
        return self._celsius * 9 / 5 + 32


t = Thermometre(20)
print(t.celsius)     # => 20 (pas de parenthèses : on lit comme un attribut)
print(t.fahrenheit)  # => 68.0
t.celsius = 100      # appelle le setter
print(t.fahrenheit)  # => 212.0

try:
    t.celsius = -300
except ValueError as err:
    print(f"9: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    t.fahrenheit = 50  # pas de setter : lecture seule
except AttributeError as err:
    print(f"10: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Déroulons :
    - t.celsius (lecture) appelle la première méthode celsius(), qui retourne
      l'attribut interne self._celsius ;
    - t.celsius = 100 (écriture) appelle la méthode marquée @celsius.setter,
      qui vérifie la valeur puis la stocke dans self._celsius ;
    - même __init__ passe par le setter : la vérification s'applique dès la
      création de l'objet.

Note : le texte exact de l'erreur 10 varie selon la version de Python.

Conseil : commencez toujours avec de simples attributs publics. Si un jour
vous avez besoin de contrôler l'accès, transformez-les en propriétés : le code
qui utilise la classe (t.celsius) n'aura pas à changer. C'est pour cela qu'en
Python, on n'écrit pas de méthodes get_celsius()/set_celsius() comme en Java.
"""


# Bonus : @classmethod et @staticmethod
########################################

"""
Deux autres décorateurs changent la nature d'une méthode.

@classmethod : la méthode reçoit la CLASSE (nommée "cls" par convention) au
lieu de l'instance. Usage principal : des constructeurs alternatifs, pour
créer un objet à partir d'un autre format de données.

@staticmethod : la méthode ne reçoit ni self ni cls. C'est une simple
fonction rangée dans la classe parce qu'elle s'y rapporte logiquement.
"""


class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __repr__(self):
        return f"Date({self.jour}, {self.mois}, {self.annee})"

    @classmethod
    def depuis_texte(cls, texte):  # "25/12/2024" -> Date(25, 12, 2024)
        jour, mois, annee = texte.split("/")  # cf. chap. 8 et 17
        return cls(int(jour), int(mois), int(annee))  # cls() = Date()

    @staticmethod
    def est_bissextile(annee):
        return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)


noel = Date.depuis_texte("25/12/2024")  # appelée sur la classe
print(noel)                          # => Date(25, 12, 2024)
print(Date.est_bissextile(2024))     # => True
print(Date.est_bissextile(1900))     # => False

"""
Vous croiserez ce motif partout en Data Science : pd.DataFrame.from_dict(…),
datetime.fromisoformat(…) (cf. chap. 30)… sont des @classmethod.
(Pour de vraies dates, utilisez bien sûr le module datetime !)
"""


# Composition ou héritage ?
############################

"""
L'héritage n'est pas la seule façon de réutiliser du code. La COMPOSITION
consiste à mettre un objet DANS un autre, comme attribut. Elle exprime une
relation "A UN" (ou "EST COMPOSÉ DE") :
    - une voiture A UN moteur (composition) ;
    - une voiture EST UN véhicule (héritage).
"""


class Moteur:
    def __init__(self, puissance):
        self.puissance = puissance
        self.allume = False

    def demarrer(self):
        self.allume = True


class Voiture:
    def __init__(self, marque, puissance):
        self.marque = marque
        self.moteur = Moteur(puissance)  # composition : la voiture A UN moteur

    def demarrer(self):
        self.moteur.demarrer()  # la voiture "délègue" au moteur
        return f"{self.marque} démarre ({self.moteur.puissance} ch)"


clio = Voiture("Renault", 90)
print(clio.demarrer())        # => Renault démarre (90 ch)
print(clio.moteur.allume)     # => True

"""
Faire hériter Voiture de Moteur serait absurde : une voiture n'EST PAS un
moteur. Testez toujours la phrase "un X est un Y" avant d'utiliser l'héritage.

Le Releve du chap. 34 utilisait déjà la composition : il contenait un
dictionnaire de listes. Et notre Serie ci-dessus CONTIENT une liste au lieu
d'hériter de list.

Conseil souvent donné : "préférez la composition à l'héritage". L'héritage
crée un lien fort entre deux classes (modifier le parent peut casser tous les
enfants), et les hiérarchies profondes deviennent vite difficiles à suivre.
Réservez-le aux vraies relations "est un", sur un ou deux niveaux.
"""


# Bonus : les dataclasses
##########################

"""
Écrire __init__, __repr__ et __eq__ pour une classe qui sert surtout à stocker
des données est répétitif. Depuis Python 3.7, le module dataclasses le fait
pour nous : on déclare simplement les attributs, avec leur type (cf. les
annotations, chap. 14 et 29).
"""
from dataclasses import dataclass, field


@dataclass
class Produit:
    nom: str
    prix: float
    stock: int = 0  # valeur par défaut

    def valeur_stock(self):  # on peut ajouter des méthodes normalement
        return self.prix * self.stock


stylo = Produit("Stylo", 1.5, 100)
print(stylo)                 # => Produit(nom='Stylo', prix=1.5, stock=100)
print(stylo.valeur_stock())          # => 150.0
print(stylo == Produit("Stylo", 1.5, 100))  # => True (__eq__ généré)
print(Produit("Gomme", 0.8))  # => Produit(nom='Gomme', prix=0.8, stock=0)

"""
@dataclass a écrit pour nous __init__ (dans l'ordre des attributs), un
__repr__ lisible et un __eq__ qui compare le contenu.

Avec @dataclass(order=True), on obtient aussi <, <=, >, >= (qui comparent les
attributs dans l'ordre, comme des tuples, cf. chap. 17).

Attention au piège des attributs mutables (chap. 34) : pour une liste par
défaut, on utilise field(default_factory=list), qui crée une NOUVELLE liste
pour chaque instance.
"""


@dataclass(order=True)
class Joueur:
    score: int
    nom: str
    badges: list = field(default_factory=list)


joueurs = [Joueur(12, "Zoé"), Joueur(30, "Yan"), Joueur(12, "Alix")]
print(max(joueurs).nom)  # => Yan
print([j.nom for j in sorted(joueurs)])  # => ['Alix', 'Zoé', 'Yan']
joueurs[0].badges.append("débutant")
print(joueurs[1].badges)  # => [] (chacun sa liste)


# En bref
##########

"""
    class Enfant(Parent):                  # héritage : "Enfant EST UN Parent"
        def __init__(self, a, b, c):
            super().__init__(a, b)         # on initialise la partie "Parent"
            self.c = c

        def methode(self):                 # redéfinition (polymorphisme)
            base = super().methode()       # réutiliser la version du parent
            return base + "…"

    class MonErreur(Exception):            # ses propres exceptions
        pass

Méthodes spéciales principales :
    __init__  création           __str__  print(), str()
    __repr__  console, repr()    __eq__   ==        __lt__  <, sorted()
    __len__   len()              __getitem__  obj[i]
    __iter__  for … in …         __contains__ in    __add__ +

Encapsulation : _interne (convention), __mangle (rare), @property pour
contrôler l'accès à un attribut.

À retenir :
    - héritage = "est un" ; composition = "a un" : préférez la composition
      en cas de doute ;
    - si l'enfant a son propre __init__, appelez super().__init__(…) ;
    - isinstance() respecte l'héritage : c'est ainsi que "except" choisit
      son bloc ;
    - pour des classes qui stockent surtout des données : @dataclass.
"""
