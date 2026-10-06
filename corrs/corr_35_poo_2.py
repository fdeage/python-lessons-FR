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
#  Chap. 35     #  POO II : corrigés                                           #
#               #                                                              #
################################################################################

from dataclasses import dataclass


#####################################
#  Héritage et redéfinition         #
#####################################

# 1. Formes :
class Forme:
    def nom(self):
        return "forme"

    def decrire(self):
        return "Je suis une " + self.nom()


class Carre(Forme):
    def nom(self):
        return "carré"


class Losange(Forme):
    pass


print(Forme().decrire())    # => Je suis une forme
print(Carre().decrire())    # => Je suis une carré
print(Losange().decrire())  # => Je suis une forme
"""
decrire() est toujours celle de Forme, mais self.nom() est cherchée à partir
de la classe RÉELLE de l'objet : pour un Carre, c'est Carre.nom() qui est
trouvée en premier. Losange ne redéfinit rien : il utilise tout de Forme.
(Oui, "une carré" est mal accordé : c'est le prix d'un code trop simple !)
"""


# 2. Véhicules :
class Vehicule:
    def __init__(self, marque, vitesse_max):
        self.marque = marque
        self.vitesse_max = vitesse_max

    def decrire(self):
        return f"{self.marque}, {self.vitesse_max} km/h"


class Velo(Vehicule):
    def decrire(self):
        return super().decrire() + " (sans moteur)"


class Camion(Vehicule):
    def __init__(self, marque, vitesse_max, charge_max):
        super().__init__(marque, vitesse_max)
        self.charge_max = charge_max

    def peut_porter(self, poids):
        return poids <= self.charge_max


garage = [Vehicule("Ford", 150), Velo("BMX", 30), Camion("Volvo", 90, 18)]
for v in garage:
    print(v.decrire())
# => Ford, 150 km/h
# => BMX, 30 km/h (sans moteur)
# => Volvo, 90 km/h
print(garage[2].peut_porter(20))  # => False
"""
La boucle ne sait pas quel type de véhicule elle traite : chaque objet répond
avec SA version de decrire(). Velo réutilise la version du parent via super()
au lieu de recopier le f-string.
"""

"""
3. a) Un étudiant EST UNE personne : héritage (Etudiant hérite de Personne).
   b) Une voiture A DES roues : composition (un attribut roues, une liste de
      Roue).
   c) Une bibliothèque CONTIENT des livres : composition.
   d) Un compte épargne EST UN compte bancaire : héritage.
"""


#########################
#  super()              #
#########################

# 4. Salarié :
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age} ans."


class Salarie(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self.salaire = salaire

    def se_presenter(self):
        return f"{super().se_presenter()} Je gagne {self.salaire} €/mois."


print(Salarie("Ada", 36, 3200).se_presenter())
# => Je suis Ada, 36 ans. Je gagne 3200 €/mois.

"""
5. Oiseau définit son propre __init__, qui n'appelle pas celui d'Animal :
   l'attribut nom n'est jamais créé. print(o.nom) donne donc :
   AttributeError: 'Oiseau' object has no attribute 'nom'.
"""


class Animal:
    def __init__(self, nom):
        self.nom = nom


class OiseauBogue(Animal):
    def __init__(self, nom, envergure):
        self.envergure = envergure


try:
    print(OiseauBogue("Piaf", 25).nom)
except AttributeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


class Oiseau(Animal):  # correction
    def __init__(self, nom, envergure):
        super().__init__(nom)
        self.envergure = envergure


print(Oiseau("Piaf", 25).nom)  # => Piaf


##################################
#  isinstance() et issubclass()  #
##################################

# 6. :
print(isinstance(Velo("BMX", 30), Vehicule))   # => True (vélo EST UN véhicule)
print(isinstance(Vehicule("Ford", 150), Velo))  # => False (pas l'inverse)
print(issubclass(Camion, Vehicule))            # => True
print(type(Velo("BMX", 30)) == Vehicule)       # => False
"""
type() donne la classe exacte (Velo), sans tenir compte de l'héritage :
c'est pourquoi on préfère isinstance().
"""

# 7. LookupError :
for exc in [KeyError, IndexError, ValueError, ZeroDivisionError]:
    print(exc.__name__, issubclass(exc, LookupError))
# => KeyError True
# => IndexError True
# => ValueError False
# => ZeroDivisionError False
"""
KeyError (clé absente d'un dict) et IndexError (indice hors d'une liste)
sont deux "erreurs de recherche" : elles héritent de LookupError (cf. la
hiérarchie du chap. 26). ZeroDivisionError hérite d'ArithmeticError.
"""


####################################
#  Créer ses propres exceptions    #
####################################

# 8. NoteInvalide :
class NoteInvalide(ValueError):
    pass


def valider_note(note):
    if not 0 <= note <= 20:
        raise NoteInvalide(f"{note} n'est pas entre 0 et 20")
    return note


for note in [12, 25, -1, 20]:
    try:
        valider_note(note)
        print(note, "OK")
    except NoteInvalide as err:
        print("Erreur :", err)
# => 12 OK
# => Erreur : 25 n'est pas entre 0 et 20
# => Erreur : -1 n'est pas entre 0 et 20
# => 20 OK

try:
    valider_note(42)
except ValueError as err:  # intercepte aussi NoteInvalide (sous-classe)
    print(f"2: (Sans ce try: … except …, cette ligne créerait : "
          f"{type(err).__name__}: {err})")
"""
Hériter de ValueError plutôt que d'Exception est un bon choix : un code qui
attend des ValueError (comme int("abc")) interceptera aussi nos erreurs.
"""


############################
#  Méthodes spéciales      #
############################

# 9. Duree :
class Duree:
    def __init__(self, heures, minutes):
        total = heures * 60 + minutes  # tout en minutes…
        self.heures = total // 60      # … puis on redécoupe (cf. chap. 4)
        self.minutes = total % 60

    def en_minutes(self):
        return self.heures * 60 + self.minutes

    def __str__(self):
        return f"{self.heures}h{self.minutes:02d}"

    def __repr__(self):
        return f"Duree({self.heures}, {self.minutes})"

    def __add__(self, autre):
        return Duree(self.heures + autre.heures, self.minutes + autre.minutes)

    def __eq__(self, autre):
        return self.en_minutes() == autre.en_minutes()

    def __lt__(self, autre):
        return self.en_minutes() < autre.en_minutes()


print(Duree(1, 75))                  # => 2h15
print(Duree(1, 75) == Duree(2, 15))  # => True
durees = [Duree(1, 30), Duree(0, 45), Duree(2, 0)]
print(sorted(durees))  # => [Duree(0, 45), Duree(1, 30), Duree(2, 0)]
total = Duree(0, 0)
for d in durees:
    total = total + d
print(total)           # => 4h15
"""
Normaliser dans __init__ simplifie tout le reste : __add__ peut additionner
heures et minutes sans se soucier des retenues, le constructeur s'en charge.
Note : sum(durees) ne marcherait pas directement, car sum() commence par
0 + Duree(…), et un int ne sait pas additionner une Duree (il faudrait
__radd__).
"""

"""
10. a < b : OK (__lt__) ; a > b : OK (Python essaie b < a) ;
    a <= b : TypeError (pas de __le__) ; a + b : OK (__add__) ;
    a * b : TypeError (pas de __mul__).
"""


# 11. Playlist :
class Playlist:
    def __init__(self, nom, titres):
        self.nom = nom
        self.titres = list(titres)

    def __len__(self):
        return len(self.titres)

    def __getitem__(self, i):
        return self.titres[i]

    def __iter__(self):
        return iter(self.titres)

    def __contains__(self, titre):
        return titre in self.titres


pl = Playlist("Road trip", ["Highway Star", "Born to Run", "Roadhouse Blues"])
print(len(pl))              # => 3
print(pl[0])                # => Highway Star
print(pl[-2:])              # => ['Born to Run', 'Roadhouse Blues']
print("Born to Run" in pl)  # => True
for i, titre in enumerate(pl, start=1):
    print(i, titre)
# => 1 Highway Star
# => 2 Born to Run
# => 3 Roadhouse Blues


###################################
#  Encapsulation et propriétés    #
###################################

# 12. Secret :
class Secret:
    def __init__(self):
        self._a = 1
        self.__b = 2


s = Secret()
print(s._a)          # => 1 (convention seulement : accessible)
print(s._Secret__b)  # => 2 (le nom réel après "name mangling")
try:
    print(s.__b)
except AttributeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")


# 13. Rectangle avec propriétés :
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur  # passe par les setters
        self.hauteur = hauteur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, valeur):
        if valeur <= 0:
            raise ValueError(f"largeur invalide : {valeur}")
        self._largeur = valeur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, valeur):
        if valeur <= 0:
            raise ValueError(f"hauteur invalide : {valeur}")
        self._hauteur = valeur

    @property
    def aire(self):
        return self._largeur * self._hauteur


r = Rectangle(3, 4)
print(r.aire)    # => 12
r.largeur = 5
print(r.aire)    # => 20 (calculée à chaque lecture : toujours à jour)
try:
    r.largeur = -1
except ValueError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    r.aire = 50
except AttributeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
# Le texte de l'erreur 5 varie selon la version de Python.


####################################
#  Bonus : classmethod, dataclass  #
####################################

# 14. Constructeur alternatif et méthode statique :
class Duree2(Duree):  # on hérite de Duree pour ne pas tout réécrire
    @classmethod
    def depuis_minutes(cls, total):
        return cls(0, total)  # __init__ normalise tout seul

    @staticmethod
    def est_valide(texte):
        if texte.count("h") != 1:
            return False
        heures, minutes = texte.split("h")
        return heures.isdigit() and minutes.isdigit()


print(Duree2.depuis_minutes(135))  # => 2h15
print(Duree2.est_valide("2h15"))   # => True
print(Duree2.est_valide("2h"))     # => False ("".isdigit() vaut False)
print(Duree2.est_valide("deux"))   # => False
"""
Dans l'exercice, on aurait ajouté ces méthodes directement dans Duree ; ici on
les met dans une sous-classe pour garder la Duree de l'exercice 9 intacte.
cls(0, total) crée un objet de la classe sur laquelle on appelle la méthode
(Duree2 ici) : c'est l'intérêt de cls par rapport à écrire Duree en dur.
"""


# 15. Dataclass :
@dataclass
class Etudiant:
    nom: str
    note: float


promo = [Etudiant("Zoé", 14.5), Etudiant("Yan", 17.0), Etudiant("Alix", 9.5)]


def note_de(etudiant):
    return etudiant.note


for e in sorted(promo, key=note_de, reverse=True):
    print(e)
# => Etudiant(nom='Yan', note=17.0)
# => Etudiant(nom='Zoé', note=14.5)
# => Etudiant(nom='Alix', note=9.5)
print(Etudiant("Zoé", 14.5) == promo[0])  # => True
"""
@dataclass a généré __init__, __repr__ et __eq__ (qui compare le contenu).
"""


##############
#  Synthèse  #
##############

# 16. Bibliothèque :
class DocumentIntrouvable(Exception):
    pass


class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def __repr__(self):
        return f"{type(self).__name__}({self.titre!r}, {self.annee})"


class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur


class Film(Document):
    def __init__(self, titre, annee, duree):
        super().__init__(titre, annee)
        self.duree = duree


class Bibliotheque:
    def __init__(self):
        self.documents = []  # composition

    def ajouter(self, doc):
        self.documents.append(doc)

    def __len__(self):
        return len(self.documents)

    def __iter__(self):
        return iter(self.documents)

    def filtrer(self, type_doc):
        return [d for d in self.documents if isinstance(d, type_doc)]

    def chercher(self, titre):
        for d in self.documents:
            if d.titre == titre:
                return d
        raise DocumentIntrouvable(f"aucun document intitulé {titre!r}")


biblio = Bibliotheque()
biblio.ajouter(Livre("Germinal", 1885, "Zola"))
biblio.ajouter(Film("Metropolis", 1927, 153))
biblio.ajouter(Livre("Dune", 1965, "Herbert"))
print(len(biblio))              # => 3
print(biblio.filtrer(Livre))
# => [Livre('Germinal', 1885), Livre('Dune', 1965)]
print(biblio.filtrer(Document))  # => tous les documents (héritage !)
print(biblio.chercher("Dune").auteur)  # => Herbert
for doc in biblio:
    print(doc.annee, doc.titre)
# => 1885 Germinal
# => 1927 Metropolis
# => 1965 Dune
try:
    biblio.chercher("Tintin")
except DocumentIntrouvable as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- Le __repr__ de Document, hérité, affiche le bon nom de classe grâce à
  type(self).__name__.
- filtrer(Document) retourne tout : un Livre et un Film SONT des Documents.
- Bibliotheque n'hérite pas de list : elle CONTIENT une liste (composition) et
  n'expose que les opérations utiles.
"""
