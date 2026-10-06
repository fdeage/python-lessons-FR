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
#  Chap. 35     #  POO II : exercices                                          #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", demandez-vous à chaque appel de
méthode dans quelle classe Python va la trouver (l'objet, sa classe, puis les
classes parentes).

Les corrigés sont dans le fichier corr_35_poo_2.py.
"""


#####################################
#  Héritage et redéfinition         #
#####################################

"""
1. Sans exécuter, qu'affiche ce programme ?
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

       print(Forme().decrire())
       print(Carre().decrire())
       print(Losange().decrire())

2. Écrivez une classe Vehicule (attributs marque et vitesse_max, méthode
   decrire() qui retourne "<marque>, <vitesse_max> km/h"), puis deux classes
   enfants :
     - Velo, qui redéfinit decrire() pour ajouter " (sans moteur)" ;
     - Camion, qui ajoute un attribut charge_max (en tonnes) et une méthode
       peut_porter(poids).
   Créez un objet de chaque classe et parcourez-les dans une boucle en
   appelant decrire() (polymorphisme).

3. "Est un" ou "a un" ? Pour chaque paire, dites s'il faut utiliser
   l'héritage ou la composition :
       a) Etudiant / Personne        b) Voiture / Roue
       c) Bibliotheque / Livre       d) CompteEpargne / CompteBancaire
"""


#########################
#  super()              #
#########################

"""
4. Complétez la classe Salarie pour qu'elle hérite de Personne, ajoute un
   attribut salaire, et redéfinisse se_presenter() en RÉUTILISANT celle du
   parent (avec super()) pour obtenir :
   "Je suis Ada, 36 ans. Je gagne 3200 €/mois."
       class Personne:
           def __init__(self, nom, age):
               self.nom = nom
               self.age = age
           def se_presenter(self):
               return f"Je suis {self.nom}, {self.age} ans."

5. Sans exécuter, quelle erreur produit ce programme ? Pourquoi ? Corrigez-le.
       class Animal:
           def __init__(self, nom):
               self.nom = nom

       class Oiseau(Animal):
           def __init__(self, nom, envergure):
               self.envergure = envergure

       o = Oiseau("Piaf", 25)
       print(o.nom)
"""


##################################
#  isinstance() et issubclass()  #
##################################

"""
6. Avec les classes de l'exercice 2, sans exécuter, que valent :
       isinstance(Velo("BMX", 30), Vehicule)
       isinstance(Vehicule("Ford", 150), Velo)
       issubclass(Camion, Vehicule)
       type(Velo("BMX", 30)) == Vehicule

7. Sans exécuter : laquelle de ces exceptions est interceptée par
   "except LookupError" ? Vérifiez avec issubclass().
       KeyError, IndexError, ValueError, ZeroDivisionError
"""


####################################
#  Créer ses propres exceptions    #
####################################

"""
8. Créez une exception NoteInvalide (qui hérite de ValueError), et une
   fonction valider_note(note) qui la lève si la note n'est pas entre 0 et 20,
   et retourne la note sinon. Testez sur [12, 25, -1, 20] dans une boucle
   avec try/except, en affichant "OK" ou le message d'erreur.
   Vérifiez qu'un "except ValueError" intercepte aussi NoteInvalide.
"""


############################
#  Méthodes spéciales      #
############################

"""
9. Écrivez une classe Duree (heures, minutes) avec :
     - __init__ qui normalise : Duree(1, 75) doit donner 2 h 15 ;
     - __str__ : "2h15" (minutes sur deux chiffres : f"{m:02d}") ;
     - __add__ : additionne deux durées ;
     - __eq__ et __lt__ : comparent deux durées.
   Triez la liste [Duree(1, 30), Duree(0, 45), Duree(2, 0)] et affichez la
   durée totale.

10. Sans exécuter : avec la classe Fraction du chap. 35 (qui définit __eq__,
    __lt__ et __add__ mais pas __le__ ni __mul__), quelles lignes provoquent
    une erreur ?
        a = Fraction(1, 2)
        b = Fraction(2, 3)
        print(a < b)
        print(a > b)
        print(a <= b)
        print(a + b)
        print(a * b)

11. Écrivez une classe Playlist qui contient un nom et une liste de titres,
    avec __len__, __getitem__, __iter__ et __contains__. Vérifiez que len(),
    l'indexation, les slices, "in" et une boucle for fonctionnent.
"""


###################################
#  Encapsulation et propriétés    #
###################################

"""
12. Sans exécuter, qu'affiche ce programme (ou quelle erreur) ?
        class Secret:
            def __init__(self):
                self._a = 1
                self.__b = 2

        s = Secret()
        print(s._a)
        print(s._Secret__b)
        print(s.__b)

13. Écrivez une classe Rectangle dont la largeur et la hauteur sont des
    propriétés qui refusent les valeurs négatives ou nulles (ValueError),
    et qui a une propriété aire en lecture seule. Vérifiez que :
      - r = Rectangle(3, 4) ; r.aire vaut 12 ;
      - r.largeur = 5 met à jour r.aire ;
      - r.largeur = -1 lève une ValueError ;
      - r.aire = 50 lève une AttributeError.
"""


####################################
#  Bonus : classmethod, dataclass  #
####################################

"""
14. Ajoutez à la classe Duree de l'exercice 9 une @classmethod
    depuis_minutes(total) qui crée une Duree à partir d'un nombre de minutes
    (Duree.depuis_minutes(135) -> 2h15), et une @staticmethod
    est_valide(texte) qui teste si une chaîne a le format "2h15" (un "h" et
    que des chiffres de part et d'autre).

15. Réécrivez avec @dataclass une classe Etudiant (nom: str, note: float) et
    triez une liste d'étudiants par note décroissante avec sorted(…, key=…,
    reverse=True) (cf. chap. 24). Vérifiez que deux étudiants avec le même nom
    et la même note sont égaux.
"""


##############
#  Synthèse  #
##############

"""
16. Modélisez une petite bibliothèque :
      - une classe Document (titre, annee) avec __repr__ ;
      - deux classes enfants Livre (+ auteur) et Film (+ duree en minutes) ;
      - une classe Bibliotheque (composition : elle CONTIENT une liste de
        documents) avec ajouter(doc), __len__, __iter__, et une méthode
        filtrer(type_doc) qui retourne la liste des documents de ce type
        (utilisez isinstance()).
      - une exception DocumentIntrouvable, levée par une méthode
        chercher(titre) si aucun document n'a ce titre.
    Testez le tout.
"""
