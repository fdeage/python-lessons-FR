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
#  Chap. 34     #  POO I : corrigés                                            #
#               #                                                              #
################################################################################

import math


###############################
#  En Python, tout est objet  #
###############################

# 1. Types :
print(type(3.0))              # => <class 'float'>
print(type(None))             # => <class 'NoneType'>
print(type(len))              # => <class 'builtin_function_or_method'>
print(isinstance(True, int))  # => True
"""
- None a lui aussi un type : NoneType (cf. chap. 15).
- Les fonctions sont des objets comme les autres ; len, écrite en C dans
  Python, est une "builtin_function_or_method".
- True est une instance de int : bool hérite de int (cf. chap. 21 ; on verra
  l'héritage au chap. 35). C'est pourquoi True + True vaut 2.
"""

# 2. Méthodes :
mots = ["b", "a"]
print(mots.sort())          # => None : sort() MODIFIE la liste…
print(mots)                 # => ['a', 'b'] … qui est maintenant triée
nom = "ada"
print(nom.capitalize())     # => Ada : capitalize() RETOURNE une nouvelle str…
print(nom)                  # => ada … et nom n'a pas changé
"""
- mots.sort() est appelée sur l'objet liste "mots", et le modifie en place
  (elle retourne None, cf. chap. 24).
- nom.capitalize() est appelée sur l'objet "ada". Les chaînes sont immuables
  (cf. chap. 7) : leurs méthodes ne peuvent pas les modifier, elles retournent
  toujours une nouvelle chaîne.
"""


########################
#  Classe et instance  #
########################

"""
3. a) str est la classe, "bonjour" une instance de str.
   b) list est la classe, [3, 1, 2] une instance de list.
   c) le plan est la "classe" (le modèle), la voiture réelle une "instance".
"""
print(isinstance("bonjour", str))  # => True
print(isinstance([3, 1, 2], list))  # => True


# 4. Classe vide :
class Velo:
    pass


v1 = Velo()
v2 = Velo()
v1.couleur = "rouge"
print(v1.couleur)  # => rouge
try:
    print(v2.couleur)
except AttributeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
L'attribut a été ajouté à l'OBJET v1 seulement, pas à la classe : v2 n'en a
pas, d'où l'AttributeError. C'est une bonne raison de créer tous les attributs
dans __init__.
"""


################################
#  __init__, self, attributs   #
################################

# 5. Classe Personne :
class Personne:
    def __init__(self, prenom, age):
        self.prenom = prenom
        self.age = age


p1 = Personne("Ada", 36)
p2 = Personne("Alan", 41)
print(p1.prenom, p1.age)  # => Ada 36
print(p2.prenom, p2.age)  # => Alan 41

"""
6. Les deux erreurs :
   - self manque dans "def __init__(titre, auteur)" : Python passe l'objet
     en premier argument, qui arrive dans "titre"… et il y a un argument de
     trop : TypeError: Livre.__init__() takes 2 positional arguments but 3
     were given.
   - "auteur = auteur" n'a pas de "self." : c'est une variable locale, qui
     disparaît. Même une fois self ajouté, print(l.auteur) donnerait :
     AttributeError: 'Livre' object has no attribute 'auteur'.
"""


class LivreFaux:
    def __init__(titre, auteur):
        self.titre = titre
        auteur = auteur


try:
    l = LivreFaux("Germinal", "Zola")
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


class Livre:  # version corrigée
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur


l = Livre("Germinal", "Zola")
print(l.auteur)  # => Zola


# 7. Point3D avec valeurs par défaut :
class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


origine = Point3D()
p = Point3D(1, 2, 3)
haut = Point3D(z=5)  # argument nommé : x et y gardent leur valeur par défaut
print(origine.x, origine.y, origine.z)  # => 0 0 0
print(p.x, p.y, p.z)                    # => 1 2 3
print(haut.x, haut.y, haut.z)           # => 0 0 5


# 8. Boîtes :
class Boite:
    def __init__(self, contenu):
        self.contenu = contenu


b1 = Boite("pommes")
b2 = Boite("poires")
b1.contenu = "cerises"
print(b1.contenu, b2.contenu)  # => cerises poires
print(b1.__dict__)             # => {'contenu': 'cerises'}
"""
Chaque instance a ses propres attributs : modifier b1.contenu ne touche pas
b2. __dict__ montre les attributs d'instance de b1 et leurs valeurs.
"""


##################
#  Les méthodes  #
##################

# 9. Personne avec méthodes :
class Personne:
    def __init__(self, prenom, age):
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        return f"Bonjour, je suis {self.prenom}."

    def est_majeur(self):
        return self.age >= 18

    def feter_anniversaire(self):
        self.age += 1


lea = Personne("Léa", 17)
print(lea.se_presenter())  # => Bonjour, je suis Léa.
print(lea.est_majeur())    # => False
lea.feter_anniversaire()
print(lea.age)             # => 18
print(lea.est_majeur())    # => True
"""
est_majeur() retourne directement le résultat de la comparaison : inutile
d'écrire "if self.age >= 18: return True else: return False" (cf. chap. 12).
feter_anniversaire() modifie l'objet et ne retourne rien (None).
"""


# 10. Cercle :
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def agrandir(self, facteur):
        self.rayon *= facteur


c = Cercle(2)
print(round(c.aire(), 2))       # => 12.57
print(round(c.perimetre(), 2))  # => 12.57 (pour r = 2, aire = périmètre !)
c.agrandir(3)
print(c.rayon)                  # => 6
print(round(c.aire(), 2))       # => 113.1

# 11. Forme longue :
print(Cercle.aire(c) == c.aire())  # => True
"""
c.aire() est un raccourci pour Cercle.aire(c) : Python passe l'objet placé
avant le point comme premier argument, qui arrive dans self.
"""


# 12. Compteur :
class Compteur:
    def __init__(self):
        self.valeur = 0

    def incrementer(self):
        self.valeur += 1

    def decrementer(self):
        if self.valeur > 0:
            self.valeur -= 1

    def reinitialiser(self):
        self.valeur = 0


cpt = Compteur()
for lettre in "anticonstitutionnellement":
    if lettre in "aeiouy":
        cpt.incrementer()
print(cpt.valeur)  # => 10
cpt.reinitialiser()
cpt.decrementer()  # ne descend pas sous 0
print(cpt.valeur)  # => 0


###################################################
#  Attributs de classe et attributs d'instance    #
###################################################

# 13. Robots :
class Robot:
    nb_robots = 0

    def __init__(self, nom):
        self.nom = nom
        Robot.nb_robots += 1


r1 = Robot("R2")
r2 = Robot("C3")
print(Robot.nb_robots)                               # => 2
r1.nb_robots = 100
print(Robot.nb_robots, r1.nb_robots, r2.nb_robots)  # => 2 100 2
"""
"r1.nb_robots = 100" ne modifie PAS l'attribut de classe : il crée un
attribut d'instance sur r1, qui masque celui de la classe pour r1 seulement.
Robot.nb_robots et r2.nb_robots (qui va le chercher dans la classe) valent
toujours 2.
"""

"""
14. La liste articles est un attribut de CLASSE : une seule liste, partagée
    par tous les paniers. p1.ajouter("pain") la modifie, et p2 la voit aussi :
    print(p2.articles) affiche ['pain'].
"""


class PanierBogue:
    articles = []

    def ajouter(self, article):
        self.articles.append(article)


p1 = PanierBogue()
p2 = PanierBogue()
p1.ajouter("pain")
print(p2.articles)  # => ['pain'] (bug !)


class Panier:  # correction : une liste par instance, créée dans __init__
    def __init__(self):
        self.articles = []

    def ajouter(self, article):
        self.articles.append(article)


p1 = Panier()
p2 = Panier()
p1.ajouter("pain")
print(p1.articles, p2.articles)  # => ['pain'] []


##############################
#  __str__ et __repr__       #
##############################

# 15. Cercle affichable :
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def __str__(self):
        return f"Cercle de rayon {self.rayon}"

    def __repr__(self):
        return f"Cercle({self.rayon})"


c = Cercle(2)
print(c)                 # => Cercle de rayon 2
print([c, Cercle(5)])    # => [Cercle(2), Cercle(5)]
"""
print(objet) utilise __str__ ; mais une liste affiche ses éléments avec
__repr__.
"""


# 16. Mot (seulement __repr__) :
class Mot:
    def __init__(self, texte):
        self.texte = texte

    def __repr__(self):
        return f"Mot({self.texte!r})"


m = Mot("python")
print(m)                  # => Mot('python')
print([m, Mot("java")])   # => [Mot('python'), Mot('java')]
"""
Sans __str__, print() se rabat sur __repr__. Le !r ajoute les guillemets
autour du texte, comme repr("python").
"""


####################################
#  Objets mutables et références   #
####################################

# 17. Jauges :
class Jauge:
    def __init__(self):
        self.niveau = 0


def remplir(j):
    j.niveau = 10


a = Jauge()
b = a
remplir(b)
c = Jauge()
print(a.niveau, b.niveau, c.niveau)  # => 10 10 0
print(a is b, a == c)                # => True False
"""
b = a ne copie pas la jauge : a et b désignent le MÊME objet. remplir() reçoit
une référence vers cet objet et le modifie : a.niveau vaut donc 10 aussi.
c est une autre jauge, distincte : elle reste à 0, et a == c vaut False (par
défaut, == compare les identités pour nos objets).
"""


##############
#  Synthèse  #
##############

# 18. Inventaire :
class Inventaire:
    def __init__(self):
        self.stock = {}

    def ajouter(self, produit, quantite):
        self.stock[produit] = self.stock.get(produit, 0) + quantite

    def retirer(self, produit, quantite):
        disponible = self.stock.get(produit, 0)
        if quantite > disponible:
            raise ValueError(f"stock insuffisant de {produit} "
                             f"({disponible} disponibles)")
        self.stock[produit] = disponible - quantite

    def total(self):
        return sum(self.stock.values())

    def __str__(self):
        lignes = [f"{produit} : {qte}" for produit, qte in
                  sorted(self.stock.items())]
        return "\n".join(lignes)


inv = Inventaire()
inv.ajouter("pommes", 12)
inv.ajouter("bananes", 6)
inv.ajouter("pommes", 3)
inv.retirer("bananes", 2)
print(inv.total())  # => 19
print(inv)
# => bananes : 4
# => pommes : 15
try:
    inv.retirer("kiwis", 1)
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- self.stock.get(produit, 0) (cf. chap. 27) évite de tester si le produit
  existe déjà.
- __str__ construit la liste des lignes avec une compréhension (chap. 23),
  triée grâce à sorted() sur les couples (produit, quantité), puis les relie
  avec "\n".join() (chap. 8).
"""


# 19. Statistiques :
class Statistiques:
    def __init__(self, valeurs):
        self.valeurs = list(valeurs)  # copie de la liste reçue

    def moyenne(self):
        return sum(self.valeurs) / len(self.valeurs)

    def minimum(self):
        return min(self.valeurs)

    def maximum(self):
        return max(self.valeurs)

    def etendue(self):
        return self.maximum() - self.minimum()

    def ecart_type(self):
        m = self.moyenne()
        carres = [(x - m) ** 2 for x in self.valeurs]
        return math.sqrt(sum(carres) / len(carres))


s = Statistiques([12.5, 14.0, 9.5, 11.0, 13.0])
print(s.moyenne())               # => 12.0
print(s.minimum(), s.maximum())  # => 9.5 14.0
print(s.etendue())               # => 4.5
print(round(s.ecart_type(), 3))  # => 1.581
"""
etendue() et ecart_type() réutilisent les autres méthodes via self : on
n'écrit le calcul de la moyenne qu'une fois (principe DRY, cf. chap. 14).
Écarts à la moyenne : 0.5, 2, -2.5, -1, 1 ; carrés : 0.25, 4, 6.25, 1, 1 ;
moyenne des carrés : 12.5 / 5 = 2.5 ; racine : environ 1.581.
"""
