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
#  Chap. 37     #  Tests et spécification II : pytest                          #
#               #                                                              #
################################################################################
#
#  - Les limites de "assert" tout seul
#  - Ranger ses tests dans des fonctions
#  - pytest : installation et conventions
#  - Lancer pytest et lire un rapport
#  - Tester les erreurs : pytest.raises
#  - Tester plusieurs cas : pytest.mark.parametrize
#  - Préparer des données : les fixtures
#  - pytest en action
#  - unittest, l'outil de la bibliothèque standard
#  - doctest : des exemples qui se testent tout seuls
#  - Organiser un projet testé
#  - Rappel : écrire les tests d'abord
#
###################################################

import os
import sys
import tempfile
import unittest
import doctest


"""
Au chap. 29, on a appris à tester ses fonctions avec assert, et la méthode
"Think-Red-Green-Refactor". Ce chapitre montre comment les programmeurs
testent leur code "pour de vrai" : avec un outil, ou "framework", de test.

Voici les fonctions que nous allons tester tout au long du chapitre. Elles
pourraient faire partie d'un petit programme d'analyse de notes.
"""
def moyenne(notes):
    """Retourne la moyenne d'une liste de notes (ValueError si vide)."""
    if len(notes) == 0:
        raise ValueError("impossible de calculer la moyenne d'une liste vide")
    return sum(notes) / len(notes)


def mention(note):
    """Retourne la mention correspondant à une note sur 20."""
    if not 0 <= note <= 20:
        raise ValueError(f"note invalide : {note}")
    if note >= 16:
        return "Très bien"
    if note >= 14:
        return "Bien"
    if note >= 12:
        return "Assez bien"
    if note >= 10:
        return "Passable"
    return "Insuffisant"


def nettoyer_prix(texte):
    """Convertit un prix saisi par un humain ("12,50 €") en float."""
    texte = texte.replace("€", "").replace(" ", "").replace(",", ".")
    return float(texte)


# Les limites de "assert" tout seul
####################################

"""
On pourrait tester ces fonctions avec une série d'assert, les uns après les
autres, comme au chap. 29 :

    assert moyenne([10, 20]) == 15
    assert mention(15) == "Bien"
    assert mention(12) == "Bien"        # ← ce test est FAUX
    assert nettoyer_prix("3 €") == 3.0

Cela fonctionne, mais pose plusieurs problèmes :

    1. Le PREMIER assert qui échoue arrête tout le programme : on ne sait
       pas si les tests suivants passent ou non. Avec 200 tests, on corrige
       les erreurs une par une, en relançant à chaque fois…
    2. Le message d'erreur est pauvre : "AssertionError", sans dire quelle
       valeur on a obtenue, ni laquelle on attendait.
    3. Les tests sont mélangés au code du programme : ils s'exécutent à
       chaque lancement, et alourdissent le fichier.
    4. Tester qu'une erreur est bien soulevée demande un try/except entier
       (cf. l'exemple de my_pop() au chap. 29).
    5. Pour tester 10 entrées différentes, on copie-colle 10 fois le même
       assert.

Voyons le problème n°1 et le n°2 :
"""
try:
    assert mention(12) == "Bien"
except AssertionError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err!r})")
# => 1: (Sans ce try: … except …, cette ligne créerait : AssertionError())
# → aucune information sur la valeur réellement obtenue ("Assez bien") !

"""
Un framework de test résout tous ces problèmes. Mais pour bien comprendre ce
qu'il fait, commençons par en écrire une version minuscule nous-mêmes.
"""


# Ranger ses tests dans des fonctions
######################################

"""
Première idée : chaque test devient une petite FONCTION, dont le nom
commence par "test_" et qui contient un ou quelques assert. Chaque test
vérifie UNE chose précise, et son nom dit laquelle.
"""
def test_moyenne_simple():
    assert moyenne([10, 20]) == 15


def test_moyenne_une_seule_note():
    assert moyenne([12]) == 12


def test_mention_bien():
    assert mention(15) == "Bien"


def test_mention_limite():
    # IMPT : testez toujours les valeurs "frontières" : c'est là que se
    # cachent les bugs (">" au lieu de ">=", etc.)
    resultat = mention(12)
    # assert accepte un message (cf. chap. 29) : on y met la valeur obtenue
    assert resultat == "Bien", f"obtenu : {resultat!r}"   # ← test faux exprès


def test_nettoyer_prix_virgule():
    assert nettoyer_prix("12,50 €") == 12.5


"""
Deuxième idée : une fonction "lanceur", qui exécute chaque test dans un
try/except. Ainsi, un test qui échoue n'empêche pas les autres de tourner,
et on obtient un bilan à la fin.
"""
def lancer_tests(tests):
    nb_reussis = 0
    for test in tests:
        try:
            test()          # une fonction est une valeur : on l'appelle ici
            print(f"  OK     {test.__name__}")
            nb_reussis += 1
        except AssertionError as err:
            print(f"  ÉCHEC  {test.__name__} : {err}")
    print(f"{nb_reussis}/{len(tests)} tests réussis")


lancer_tests([test_moyenne_simple, test_moyenne_une_seule_note,
              test_mention_bien, test_mention_limite,
              test_nettoyer_prix_virgule])
# =>   OK     test_moyenne_simple
# =>   OK     test_moyenne_une_seule_note
# =>   OK     test_mention_bien
# =>   ÉCHEC  test_mention_limite : obtenu : 'Assez bien'
# =>   OK     test_nettoyer_prix_virgule
# => 4/5 tests réussis

"""
C'est EXACTEMENT ce que fait pytest… en beaucoup mieux :
    - il trouve tout seul les fonctions test_* (pas besoin de les lister),
    - il les cherche dans tous les fichiers test_*.py du projet,
    - il affiche automatiquement les valeurs obtenues et attendues, sans
      qu'on ait besoin d'écrire de message,
    - il propose des outils pour les erreurs, les cas multiples, etc.
"""


# pytest : installation et conventions
#######################################

"""
pytest est l'outil de test le plus utilisé en Python. Ce n'est pas un module
de la bibliothèque standard : il faut l'installer (cf. chap. 22), idéalement
dans un environnement virtuel :

    ?> python3 -m pip install pytest

Les conventions de pytest (IMPT) :
    - les fichiers de tests s'appellent test_<quelque_chose>.py
      (ou <quelque_chose>_test.py) ;
    - les fonctions de test s'appellent test_<ce_qui_est_testé>() ;
    - une fonction de test ne prend en général pas d'argument et ne retourne
      rien : elle contient des assert "nus", SANS message ;
    - un test qui se termine sans erreur est réussi ("passed") ; un test
      dont un assert échoue est en échec ("failed").

Typiquement, pour un fichier notes.py contenant les fonctions à tester, on
écrit un fichier test_notes.py à côté :

    # Fichier test_notes.py
    from notes import moyenne, mention

    def test_moyenne_simple():
        assert moyenne([10, 20]) == 15

    def test_mention_bien():
        assert mention(15) == "Bien"

Pas besoin d'importer pytest pour des tests aussi simples : ce sont des
fonctions Python tout à fait ordinaires !
"""


# Lancer pytest et lire un rapport
###################################

"""
On lance pytest depuis un terminal (cf. chap. 2), dans le dossier du
projet :

    ?> pytest                     # tous les tests du dossier (et sous-dossiers)
    ?> pytest test_notes.py       # un seul fichier
    ?> pytest test_notes.py::test_mention_bien    # un seul test
    ?> pytest -k mention          # les tests dont le nom contient "mention"
    ?> pytest -v                  # mode "verbeux" : une ligne par test
    ?> pytest -x                  # s'arrêter au premier échec

Si la commande "pytest" n'est pas trouvée, utilisez : python3 -m pytest

Voici à quoi ressemble un rapport (simplifié) avec un test en échec :

    ========================== test session starts ==========================
    collected 3 items

    test_notes.py ..F        [100%]

    =============================== FAILURES ================================
    __________________________ test_mention_limite __________________________

        def test_mention_limite():
    >       assert mention(12) == "Bien"
    E       AssertionError: assert 'Assez bien' == 'Bien'
    E         - Bien
    E         + Assez bien

    test_notes.py:10: AssertionError
    ======================== short test summary info ========================
    FAILED test_notes.py::test_mention_limite - AssertionError: assert 'Assez...
    ====================== 1 failed, 2 passed in 0.03s ======================

Comment le lire ?
    1. "collected 3 items" : pytest a trouvé 3 fonctions de test.
    2. "..F" : un caractère par test, dans l'ordre : "." = réussi,
       "F" = échec ("failed"), "E" = erreur inattendue ("error").
    3. Pour chaque échec : le code du test, avec ">" devant la ligne qui a
       échoué, et des lignes "E" qui expliquent l'erreur. IMPT : pytest
       affiche la valeur obtenue ('Assez bien') ET la valeur attendue
       ('Bien'), sans qu'on ait rien demandé : c'est sa grande force.
    4. Le nom du fichier et le numéro de ligne (test_notes.py:10).
    5. Le bilan final : 1 échec, 2 réussites.

Au bout du compte, de deux choses l'une : soit le TEST est faux (c'est le
cas ici : 12 donne bien "Assez bien"), soit la FONCTION est fausse. Il faut
réfléchir avant de "corriger" l'un ou l'autre !
"""


# Tester les erreurs : pytest.raises
#####################################

"""
Au chap. 29, pour vérifier qu'une fonction soulève bien une erreur, il
fallait un try/except et une variable booléenne. Avec pytest, on utilise le
gestionnaire de contexte pytest.raises (cf. "with", chap. 28 et 36) :

    import pytest

    def test_moyenne_liste_vide():
        with pytest.raises(ValueError):
            moyenne([])

Le test RÉUSSIT si le bloc with soulève une ValueError, et ÉCHOUE sinon (pas
d'erreur, ou une erreur d'un autre type).

On peut aussi vérifier le message d'erreur, avec le paramètre match :

    def test_mention_note_trop_grande():
        with pytest.raises(ValueError, match="note invalide"):
            mention(25)

Sans pytest, voici l'équivalent "à la main" (c'est ce que pytest.raises
fait pour nous) :
"""
def test_moyenne_liste_vide_sans_pytest():
    erreur_levee = False
    try:
        moyenne([])
    except ValueError:
        erreur_levee = True
    assert erreur_levee, "moyenne([]) aurait dû soulever ValueError"


def test_mention_note_invalide_sans_pytest():
    for note in [-1, 20.5, 25]:
        try:
            mention(note)
        except ValueError as err:
            assert "note invalide" in str(err)
        else:                            # else : exécuté si PAS d'erreur
            assert False, f"mention({note}) aurait dû échouer"


lancer_tests([test_moyenne_liste_vide_sans_pytest,
              test_mention_note_invalide_sans_pytest])
# =>   OK     test_moyenne_liste_vide_sans_pytest
# =>   OK     test_mention_note_invalide_sans_pytest
# => 2/2 tests réussis


# Tester plusieurs cas : pytest.mark.parametrize
#################################################

"""
Pour tester mention() correctement, il faudrait tester chaque mention, ET
chaque frontière (9.99, 10, 11.99, 12…). Plutôt que d'écrire 10 fonctions
presque identiques, on utilise le décorateur (cf. chap. 36)
pytest.mark.parametrize :

    import pytest

    @pytest.mark.parametrize("note, attendu", [
        (0, "Insuffisant"),
        (9.99, "Insuffisant"),
        (10, "Passable"),
        (12, "Assez bien"),
        (14, "Bien"),
        (16, "Très bien"),
        (20, "Très bien"),
    ])
    def test_mention(note, attendu):
        assert mention(note) == attendu

    1. Le premier argument est une chaîne qui donne le nom des paramètres,
       séparés par des virgules.
    2. Le second est une liste de tuples : un tuple par cas à tester.
    3. pytest exécute test_mention() une fois PAR TUPLE, et compte chaque
       exécution comme un test séparé : ici, 7 tests. Si un cas échoue, les
       autres sont quand même exécutés, et le rapport indique lequel a
       échoué (ex. : test_mention[12-Assez bien]).

Sans pytest, on obtient une partie de cet effet avec une simple boucle (mais
la boucle s'arrête au premier cas en échec) :
"""
CAS_MENTION = [
    (0, "Insuffisant"),
    (9.99, "Insuffisant"),
    (10, "Passable"),
    (12, "Assez bien"),
    (14, "Bien"),
    (16, "Très bien"),
    (20, "Très bien"),
]


def test_mention_tous_les_cas():
    for note, attendu in CAS_MENTION:
        obtenu = mention(note)
        assert obtenu == attendu, f"mention({note}) : {obtenu!r} ≠ {attendu!r}"


lancer_tests([test_mention_tous_les_cas])
# =>   OK     test_mention_tous_les_cas
# => 1/1 tests réussis


# Préparer des données : les fixtures
######################################

"""
Souvent, plusieurs tests ont besoin des mêmes données de départ : une liste
de notes, un dictionnaire d'élèves, un fichier CSV… Plutôt que de les
recréer dans chaque test, pytest propose les "fixtures" (en anglais :
"installation", "équipement").

Une fixture est une fonction décorée par @pytest.fixture, qui RETOURNE des
données. Pour l'utiliser, un test met simplement le NOM de la fixture dans
ses paramètres : pytest appelle la fixture et passe le résultat au test.

    import pytest

    @pytest.fixture
    def notes_classe():
        return {"Ada": [15, 18, 12], "Alan": [9, 11, 10], "Grace": [17, 19]}

    def test_moyenne_ada(notes_classe):
        assert moyenne(notes_classe["Ada"]) == 15

    def test_mention_grace(notes_classe):
        assert mention(moyenne(notes_classe["Grace"])) == "Très bien"

IMPT : la fixture est rappelée pour CHAQUE test. Chaque test reçoit donc
des données toutes neuves : si un test modifie la liste (avec .append()…),
cela n'affecte pas les autres. Les tests restent indépendants les uns des
autres : on peut les lancer dans n'importe quel ordre.

pytest fournit aussi des fixtures toutes faites. La plus utile est tmp_path :
un dossier temporaire, propre à chaque test, et supprimé automatiquement.
Idéal pour tester des fonctions qui lisent ou écrivent des fichiers
(cf. chap. 28) :

    def test_ecriture(tmp_path):
        chemin = tmp_path / "notes.txt"    # (un objet pathlib, cf. chap. 22)
        chemin.write_text("15\n18\n")
        assert chemin.read_text().split() == ["15", "18"]
"""


# pytest en action
###################

"""
Si pytest est installé, ce programme va maintenant l'utiliser pour de vrai :
    1. on crée un dossier temporaire avec le module tempfile (bibliothèque
       standard) : il sera supprimé automatiquement à la fin du bloc with ;
    2. on y écrit un fichier de tests, test_demo.py, qui utilise tout ce qui
       précède : raises, parametrize, fixture ;
    3. on lance pytest sur ce fichier avec pytest.main(), qui fait la même
       chose que la commande "pytest" du terminal.
"""
CODE_TESTS = '''
import pytest


def moyenne(notes):
    if len(notes) == 0:
        raise ValueError("liste vide")
    return sum(notes) / len(notes)


@pytest.fixture
def notes():
    return [12, 15, 18]


def test_moyenne(notes):
    assert moyenne(notes) == 15


def test_moyenne_vide():
    with pytest.raises(ValueError, match="vide"):
        moyenne([])


@pytest.mark.parametrize("liste, attendu", [([10], 10), ([0, 20], 10),
                                            ([1, 2], 2)])  # dernier cas faux
def test_moyenne_cas(liste, attendu):
    assert moyenne(liste) == attendu
'''

try:
    import pytest
except ImportError:
    pytest = None
    print("pytest n'est pas installé : la démonstration est ignorée.")
    print("Pour l'installer : python3 -m pip install pytest")

if pytest is not None:
    with tempfile.TemporaryDirectory() as dossier:
        chemin_test = os.path.join(dossier, "test_demo.py")
        with open(chemin_test, "w", encoding="utf-8") as f:
            f.write(CODE_TESTS)
        # -q : rapport court ; -p no:cacheprovider : ne pas créer de dossier
        # .pytest_cache ; sys.dont_write_bytecode : pas de __pycache__
        sys.dont_write_bytecode = True
        code_retour = pytest.main(["-q", "-p", "no:cacheprovider",
                                   chemin_test])
        sys.dont_write_bytecode = False
    print("code de retour de pytest :", int(code_retour))
# => (si pytest est installé, quelque chose comme :)
#    ...F                                                          [100%]
#    =================================== FAILURES ===========================
#    ________________________ test_moyenne_cas[liste2-2] ____________________
#    ...
#    E       assert 1.5 == 2
#    E        +  where 1.5 = moyenne([1, 2])
#    ...
#    FAILED .../test_demo.py::test_moyenne_cas[liste2-2] - assert 1.5 == 2
#    1 failed, 4 passed in 0.02s
#    code de retour de pytest : 1
# => (sinon :)
#    pytest n'est pas installé : la démonstration est ignorée.
#    Pour l'installer : python3 -m pip install pytest

"""
Remarquez :
    - 5 tests ont été trouvés : 2 fonctions + 3 cas de parametrize ;
    - le cas en échec est identifié précisément : [liste2-2] = 3e cas
      (on compte à partir de 0, cf. chap. 16), valeur attendue 2 ;
    - "where 1.5 = moyenne([1, 2])" : pytest détaille même le calcul ;
    - le code de retour vaut 0 si tout passe, 1 s'il y a des échecs. Les
      outils d'intégration continue (cf. chap. 20) s'en servent pour
      refuser du code qui casse les tests.
"""


# unittest, l'outil de la bibliothèque standard
################################################

"""
Python fournit son propre framework de test, sans rien installer : le
module unittest. Il est plus ancien et plus "verbeux" que pytest, mais vous
le rencontrerez dans beaucoup de projets (et pytest sait aussi lancer les
tests unittest).

Différences principales :
    - les tests sont des méthodes d'une CLASSE qui hérite de
      unittest.TestCase (classes et héritage : cf. chap. 34 et 35) ;
    - au lieu de assert, on utilise des méthodes : self.assertEqual(a, b),
      self.assertTrue(x), self.assertIn(a, b), self.assertRaises(Erreur)…
    - la méthode spéciale setUp() joue le rôle d'une fixture : elle est
      appelée avant chaque test.
"""
class TestNotes(unittest.TestCase):

    def setUp(self):
        # appelée avant CHAQUE test : données toutes neuves
        self.notes = [12, 15, 18]

    def test_moyenne(self):
        self.assertEqual(moyenne(self.notes), 15)

    def test_moyenne_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])

    def test_mention(self):
        self.assertEqual(mention(17), "Très bien")
        self.assertIn(mention(11), ["Passable", "Assez bien"])


"""
Dans un fichier de tests, on écrit en général à la fin :

    if __name__ == "__main__":      # cf. chap. 22
        unittest.main()

ou on lance depuis le terminal : python3 -m unittest test_notes.py

Mais unittest.main() termine le programme quand les tests sont finis (il
appelle sys.exit). Ici, on veut continuer le chapitre : on charge donc les
tests nous-mêmes, et on les lance avec un TextTestRunner qui écrit dans la
sortie standard (sys.stdout).
"""
suite = unittest.TestLoader().loadTestsFromTestCase(TestNotes)
resultat = unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)
# => test_mention (__main__.TestNotes.test_mention) ... ok
# => test_moyenne (__main__.TestNotes.test_moyenne) ... ok
# => test_moyenne_vide (__main__.TestNotes.test_moyenne_vide) ... ok
# =>
# => ----------------------------------------------------------------------
# => Ran 3 tests in 0.000s
# =>
# => OK
# (La présentation exacte varie selon la version de Python, et la durée
# selon la machine.)
print(resultat.wasSuccessful())  # => True

"""
Équivalences pytest ↔ unittest :

    pytest                              unittest
    ----------------------------------  ----------------------------------
    assert a == b                       self.assertEqual(a, b)
    assert x                            self.assertTrue(x)
    assert a in b                       self.assertIn(a, b)
    with pytest.raises(ValueError):     with self.assertRaises(ValueError):
    @pytest.fixture                     def setUp(self):
    @pytest.mark.parametrize(…)         with self.subTest(…): dans une boucle

Conseil : pour un nouveau projet, préférez pytest, plus simple et plus
lisible. Mais savoir lire unittest est indispensable.
"""


# doctest : des exemples qui se testent tout seuls
###################################################

"""
On a vu les docstrings au chap. 29. Une bonne docstring contient souvent des
exemples d'utilisation, écrits comme dans l'interpréteur interactif
(cf. chap. 2) : ">>>" devant l'appel, et le résultat attendu à la ligne
suivante.

Le module doctest (bibliothèque standard) cherche ces exemples, les exécute,
et vérifie que le résultat affiché est bien celui écrit dans la docstring.
La documentation devient un test : elle ne peut donc plus mentir !
"""
def pourcentage(partie, total):
    """Retourne partie / total, en pourcentage arrondi à 1 décimale.

    >>> pourcentage(1, 4)
    25.0
    >>> pourcentage(1, 3)
    33.3
    >>> pourcentage(5, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return round(partie / total * 100, 1)


# doctest.testmod() teste toutes les docstrings du fichier courant. Elle
# n'affiche rien si tout va bien, et retourne un bilan :
print(doctest.testmod())  # => TestResults(failed=0, attempted=3)

"""
Les 3 exemples de pourcentage() ont été exécutés ("attempted=3"), et aucun
n'a échoué. Notez qu'on peut même tester une erreur : on écrit la première
ligne du traceback, "...", puis la dernière ligne.

Si un exemple est faux, doctest affiche un rapport détaillé. Exemple avec
une docstring volontairement fausse (testée seule, avec
run_docstring_examples) :
"""
def double(x):
    """
    >>> double(4)
    9
    """
    return x * 2


doctest.run_docstring_examples(double, {"double": double}, name="double")
# => **********************************************************************
# => File "…", line ?, in double
# => Failed example:
# =>     double(4)
# => Expected:
# =>     9
# => Got:
# =>     8

"""
Depuis le terminal : python3 -m doctest mon_fichier.py -v

Limites : doctest compare du TEXTE affiché. Il convient bien pour des
exemples courts et lisibles, mais pas pour des tests nombreux ou complexes
(ordre d'affichage d'un ensemble, floats, dates…) : pour ceux-là, pytest
reste le bon outil.
"""


# Organiser un projet testé
############################

"""
Dans un vrai projet, les tests sont dans des fichiers séparés, en général
dans un dossier tests/ :

    mon_projet/
    ├── notes/                  # le package (cf. chap. 22)
    │   ├── __init__.py
    │   ├── calculs.py          # moyenne(), mention()…
    │   └── import_csv.py       # lecture des fichiers de notes
    ├── tests/
    │   ├── test_calculs.py     # tests de calculs.py
    │   └── test_import_csv.py  # tests de import_csv.py
    ├── requirements.txt        # dépendances, dont pytest (cf. chap. 22)
    └── pyproject.toml          # configuration (cf. chap. 20)

Bonnes pratiques (IMPT) :
    - un fichier de test par module, avec un nom qui y correspond ;
    - un test = un comportement précis, avec un nom explicite :
      test_moyenne_liste_vide_souleve_erreur() vaut mieux que test_3() ;
    - des tests courts, indépendants, et RAPIDES (on doit pouvoir les lancer
      des dizaines de fois par jour) ;
    - tester les cas normaux, les cas limites (liste vide, 0, valeurs
      frontières, très grands nombres…) et les cas d'erreur ;
    - lancer TOUS les tests avant chaque commit (un hook git peut le faire
      automatiquement, cf. chap. 20) ;
    - quand on trouve un bug : on écrit d'abord un test qui le reproduit
      (il échoue), PUIS on corrige (il passe). Le bug ne reviendra jamais
      sans qu'on le sache : c'est un "test de non-régression".

La "couverture de code" ("coverage") mesure quel pourcentage des lignes de
votre programme est exécuté par les tests. Le plugin pytest-cov l'affiche :

    ?> python3 -m pip install pytest-cov
    ?> pytest --cov=notes
"""


# Rappel : écrire les tests d'abord
####################################

"""
Au chap. 29, on a vu la méthode "Think-Red-Green-Refactor". Avec pytest, elle
devient très concrète. On appelle cela le "TDD" (Test-Driven Development,
développement piloté par les tests) :

    1. THINK    : réfléchir à ce que la fonction doit faire, et à ses cas
                  limites. Écrire sa signature et sa docstring.
    2. RED      : écrire les tests (dans test_*.py). Lancer pytest : ils
                  échouent forcément (en rouge), puisque la fonction n'est
                  pas encore écrite. C'est normal, et même rassurant : cela
                  prouve que les tests testent quelque chose !
    3. GREEN    : écrire le code le plus simple possible qui fait passer les
                  tests (en vert).
    4. REFACTOR : améliorer le code (lisibilité, performance…) en relançant
                  les tests à chaque modification : s'ils restent verts, on
                  n'a rien cassé.

Exemple : on veut une fonction qui nettoie des prix saisis à la main. Avant
d'écrire nettoyer_prix() (tout en haut de ce fichier), on aurait écrit :

    @pytest.mark.parametrize("texte, attendu", [
        ("12", 12.0),
        ("12,50", 12.5),
        ("12.50 €", 12.5),
        (" 3 € ", 3.0),
    ])
    def test_nettoyer_prix(texte, attendu):
        assert nettoyer_prix(texte) == attendu

    def test_nettoyer_prix_invalide():
        with pytest.raises(ValueError):
            nettoyer_prix("gratuit")

Vérifions que notre version passe bien ces tests :
"""
def test_nettoyer_prix_tous_les_cas():
    for texte, attendu in [("12", 12.0), ("12,50", 12.5),
                           ("12.50 €", 12.5), (" 3 € ", 3.0)]:
        assert nettoyer_prix(texte) == attendu, texte


def test_nettoyer_prix_invalide():
    try:
        nettoyer_prix("gratuit")
    except ValueError:
        return              # c'est l'erreur attendue : le test réussit
    assert False, "nettoyer_prix('gratuit') aurait dû échouer"


lancer_tests([test_nettoyer_prix_tous_les_cas, test_nettoyer_prix_invalide])
# =>   OK     test_nettoyer_prix_tous_les_cas
# =>   OK     test_nettoyer_prix_invalide
# => 2/2 tests réussis

"""
En résumé :
    - rangez vos tests dans des fonctions test_*, dans des fichiers test_*.py ;
    - lancez-les avec pytest, qui les trouve tout seul et explique chaque
      échec en détail ;
    - pytest.raises pour les erreurs, @pytest.mark.parametrize pour les cas
      multiples, @pytest.fixture pour les données partagées ;
    - unittest (standard) et doctest (exemples dans les docstrings) sont des
      alternatives sans installation ;
    - écrivez les tests AVANT le code, et lancez-les souvent.
"""
