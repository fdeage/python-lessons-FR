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
#  Chap. 37     #  Tests et spécification II : corrigés                        #
#               #                                                              #
################################################################################

import os
import sys
import tempfile
import unittest
import doctest


def est_bissextile(annee):
    """Retourne True si l'année est bissextile."""
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)


def normaliser_email(email):
    """Met un e-mail en minuscules et enlève les espaces autour.
    Soulève ValueError si l'e-mail ne contient pas exactement un "@"."""
    email = email.strip().lower()
    if email.count("@") != 1:
        raise ValueError(f"e-mail invalide : {email!r}")
    return email


def taux_de_remplissage(valeurs):
    """Retourne la proportion (entre 0 et 1) de valeurs qui ne sont pas None.

    >>> taux_de_remplissage([1, None, 3, None])
    0.5
    >>> taux_de_remplissage([])
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return sum(1 for v in valeurs if v is not None) / len(valeurs)


#####################################
#  Les limites de assert tout seul  #
#####################################

# 1. Deux assert sont exécutés : le 1er passe (2024 est bissextile), le 2e
#    échoue (1900 ne l'est pas : divisible par 100 mais pas par 400). Le
#    programme s'arrête alors, et les deux derniers ne sont jamais testés.
assert est_bissextile(2024)
try:
    assert est_bissextile(1900)
except AssertionError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err!r})")
# => 1: (Sans ce try: … except …, cette ligne créerait : AssertionError())
"""
Le message est vide : on ne sait ni quelle valeur a été obtenue (False), ni
laquelle était attendue. Et on ne sait pas si 2000 et 2023 sont bien gérés.

2. Avantages d'un framework de test (au choix) :
   - un échec n'arrête pas les autres tests : on voit TOUS les problèmes ;
   - le rapport montre la valeur obtenue et la valeur attendue ;
   - les tests sont séparés du code du programme (fichiers test_*.py) ;
   - les tests sont trouvés automatiquement, sans les lister ;
   - des outils dédiés : erreurs (raises), cas multiples (parametrize),
     données partagées (fixtures).
"""


#########################################
#  Ranger ses tests dans des fonctions  #
#########################################

# 3. Un test = une règle précise, et un nom qui la décrit :
def test_annee_divisible_par_4_est_bissextile():
    assert est_bissextile(2024)


def test_annee_non_divisible_par_4_ne_l_est_pas():
    assert not est_bissextile(2023)


def test_annee_seculaire_non_divisible_par_400_ne_l_est_pas():
    assert not est_bissextile(1900)


def test_annee_divisible_par_400_est_bissextile():
    assert est_bissextile(2000)


# 4.
def lancer(tests):
    nb_echecs = 0
    for test in tests:
        try:
            test()
            print("OK    ", test.__name__)
        except AssertionError:
            print("ÉCHEC ", test.__name__)
            nb_echecs += 1
    return nb_echecs


echecs = lancer([test_annee_divisible_par_4_est_bissextile,
                 test_annee_non_divisible_par_4_ne_l_est_pas,
                 test_annee_seculaire_non_divisible_par_400_ne_l_est_pas,
                 test_annee_divisible_par_400_est_bissextile])
print(echecs, "échec(s)")
# => OK     test_annee_divisible_par_4_est_bissextile
# => OK     test_annee_non_divisible_par_4_ne_l_est_pas
# => OK     test_annee_seculaire_non_divisible_par_400_ne_l_est_pas
# => OK     test_annee_divisible_par_400_est_bissextile
# => 0 échec(s)


##########################################
#  pytest : installation et conventions  #
##########################################

"""
5. Fichiers trouvés : test_calculs.py (test_*.py) et calculs_test.py
   (*_test.py). Pas tests_calculs.py ("tests_" ≠ "test_"), ni calculs.py, ni
   mes_tests.py.
   Fonctions trouvées : test_moyenne(), test_() ET tester_moyenne() !
   Par défaut, pytest collecte toute fonction dont le nom COMMENCE par
   "test" (pas forcément "test_") : tester_moyenne() est donc un piège.
   Ne sont pas trouvées : moyenne_test() (le préfixe compte, pas le
   suffixe) et Test_moyenne() (la casse compte).

   Retenez la règle simple : nommez TOUJOURS vos tests test_quelque_chose(),
   et rien d'autre ne doit commencer par "test".
"""


######################################
#  Lancer pytest et lire un rapport  #
######################################

"""
6. a) 5 tests (un caractère par test : . F . F .). Le 2e et le 4e ont
      échoué ("2 failed, 3 passed").
   b) Obtenu : 1. Attendu : 2.
   c) La médiane de [3, 1, 2] est 2 (la valeur du milieu une fois la liste
      TRIÉE : [1, 2, 3]). La fonction a renvoyé 1, l'élément du milieu de
      la liste NON triée : elle oublie probablement de trier la liste.

7. pytest -k email -x
"""


########################################
#  Tester les erreurs : pytest.raises  #
########################################

# 8. Version pytest (à mettre dans un fichier test_*.py) :
TEST_PYTEST_8 = '''
def test_email_sans_arobase():
    with pytest.raises(ValueError, match="invalide"):
        normaliser_email("pas-d-arobase")
'''


# Version sans pytest :
def test_email_sans_arobase():
    try:
        normaliser_email("pas-d-arobase")
    except ValueError as err:
        assert "invalide" in str(err)
    else:
        assert False, "aucune erreur soulevée"


lancer([test_email_sans_arobase])   # => OK     test_email_sans_arobase


####################################################
#  Tester plusieurs cas : pytest.mark.parametrize  #
####################################################

# 9. Version pytest :
TEST_PYTEST_9 = '''
@pytest.mark.parametrize("brut, attendu", [
    ("Ada@Exemple.FR", "ada@exemple.fr"),
    ("  ada@exemple.fr  ", "ada@exemple.fr"),
    ("ada@exemple.fr", "ada@exemple.fr"),
    ("  ADA@EXEMPLE.FR ", "ada@exemple.fr"),
])
def test_normaliser_email(brut, attendu):
    assert normaliser_email(brut) == attendu
'''

# Version sans pytest :
CAS_EMAIL = [
    ("Ada@Exemple.FR", "ada@exemple.fr"),        # majuscules
    ("  ada@exemple.fr  ", "ada@exemple.fr"),    # espaces
    ("ada@exemple.fr", "ada@exemple.fr"),        # déjà correct
    ("  ADA@EXEMPLE.FR ", "ada@exemple.fr"),     # les deux
]


def test_normaliser_email_cas():
    for brut, attendu in CAS_EMAIL:
        obtenu = normaliser_email(brut)
        assert obtenu == attendu, f"{brut!r} → {obtenu!r}"


lancer([test_normaliser_email_cas])   # => OK     test_normaliser_email_cas

"""
10. 4 tests : test_somme est exécuté 3 fois (un par tuple), plus test_autre.
"""


#########################################
#  Préparer des données : les fixtures  #
#########################################

# 11. Version pytest :
TEST_PYTEST_11 = '''
@pytest.fixture
def releves():
    return [12.5, None, 13.0, None, 14.5]


def test_taux(releves):
    assert taux_de_remplissage(releves) == 0.6


def test_nombre_de_releves(releves):
    assert len(releves) == 5
'''

"""
12. Si les données étaient partagées, un test qui fait releves.append(10)
    modifierait la liste pour tous les tests suivants : test_nombre_de_releves
    trouverait 6 valeurs et échouerait… ou pas, selon l'ORDRE d'exécution des
    tests ! Les tests ne seraient plus indépendants, et leurs résultats
    deviendraient imprévisibles. En recréant les données pour chaque test, la
    fixture évite ce piège.
"""

# Si pytest est installé, on exécute pour de vrai les tests des exercices
# 8, 9 et 11, dans un dossier temporaire (cf. chap. 37) :
try:
    import pytest
except ImportError:
    pytest = None
    print("pytest n'est pas installé : python3 -m pip install pytest")

if pytest is not None:
    entete = "import pytest\n" + "\n".join(
        [__import__("inspect").getsource(f)
         for f in (normaliser_email, taux_de_remplissage)])
    with tempfile.TemporaryDirectory() as dossier:
        chemin = os.path.join(dossier, "test_exo37.py")
        with open(chemin, "w", encoding="utf-8") as fichier:
            fichier.write(entete + TEST_PYTEST_8 + TEST_PYTEST_9
                          + TEST_PYTEST_11)
        sys.dont_write_bytecode = True
        pytest.main(["-q", "-p", "no:cacheprovider", chemin])
        sys.dont_write_bytecode = False
# => (avec pytest) .......                                    [100%]
#                  7 passed in 0.01s
# => (sans pytest) pytest n'est pas installé : python3 -m pip install pytest
"""
(On utilise le module inspect pour recopier le code source des fonctions à
tester dans le fichier temporaire : c'est un détail technique, normalement
on écrirait "from mon_module import normaliser_email" dans test_exo37.py.)
"""


###################################################
#  unittest, l'outil de la bibliothèque standard  #
###################################################

# 13. et 14.
class TestBissextile(unittest.TestCase):

    def test_divisible_par_4(self):
        self.assertTrue(est_bissextile(2024))

    def test_seculaire(self):
        self.assertFalse(est_bissextile(1900))

    def test_divisible_par_400(self):
        self.assertTrue(est_bissextile(2000))


class TestEmail(unittest.TestCase):

    def test_email_vide(self):            # exercice 14
        with self.assertRaises(ValueError):
            normaliser_email("")


chargeur = unittest.TestLoader()
suite = unittest.TestSuite([chargeur.loadTestsFromTestCase(TestBissextile),
                            chargeur.loadTestsFromTestCase(TestEmail)])
resultat = unittest.TextTestRunner(stream=sys.stdout, verbosity=1).run(suite)
print(resultat.wasSuccessful())
# => ....
# => ----------------------------------------------------------------------
# => Ran 4 tests in 0.000s
# =>
# => OK
# => True
"""
TextTestRunner (et non unittest.main()) permet de lancer les tests SANS
quitter le programme. verbosity=1 affiche un "." par test réussi.
"""


######################################################
#  doctest : des exemples qui se testent tout seuls  #
######################################################

# 15.
def initiales(nom_complet):
    """Retourne les initiales d'un nom, en majuscules, suivies d'un point.

    >>> initiales("ada lovelace")
    'A.L.'
    >>> initiales("Grace Brewster Hopper")
    'G.B.H.'
    >>> initiales("")
    ''
    """
    return "".join(mot[0].upper() + "." for mot in nom_complet.split())


# 16. taux_de_remplissage([]) divise par len([]) = 0 : ZeroDivisionError.
#     Le doctest est dans la docstring de taux_de_remplissage, plus haut.
#     testmod() vérifie les docstrings de tout le fichier :
print(doctest.testmod())  # => TestResults(failed=0, attempted=5)
"""
5 exemples : 2 pour taux_de_remplissage() et 3 pour initiales(). Pour tester
une erreur, on écrit "Traceback (most recent call last):", puis "...", puis
la dernière ligne du message d'erreur.
"""


###############################
#  Organiser un projet testé  #
###############################

"""
17. Une arborescence possible :

    projet_meteo/
    ├── meteo/
    │   ├── __init__.py
    │   ├── lecture.py
    │   └── stats.py
    ├── tests/
    │   ├── test_lecture.py      # tests de meteo/lecture.py
    │   └── test_stats.py        # tests de meteo/stats.py
    └── requirements.txt         # avec pytest

    Un fichier de test par module, avec le même nom précédé de "test_".
"""


#######################################
#  Rappel : écrire les tests d'abord  #
#######################################

"""
18. a) THINK : cas à tester
       - texte plus court que n : retourné tel quel ("abc", 10 → "abc") ;
       - texte de longueur exactement n : retourné tel quel (cas limite !) ;
       - texte plus long : n caractères au total, dont "…" à la fin
         ("abcdefgh", 5 → "abcd…") ;
       - texte vide : "" ;
       - le résultat ne dépasse jamais n caractères.
"""
CAS_TRONQUER = [
    ("abc", 10, "abc"),
    ("abcde", 5, "abcde"),
    ("abcdefgh", 5, "abcd…"),
    ("", 3, ""),
]


def verifier_tronquer(fonction):
    nb_echecs = 0
    for texte, n, attendu in CAS_TRONQUER:
        obtenu = fonction(texte, n)
        if obtenu != attendu or len(obtenu) > n:
            print(f"  ÉCHEC {texte!r}, {n} → {obtenu!r} (attendu {attendu!r})")
            nb_echecs += 1
    print(f"  {nb_echecs} échec(s)")


# b) RED : avec une version vide, les tests échouent (c'est normal !).
def tronquer_vide(texte, n):
    pass


verifier_tronquer(tronquer_vide)
# =>   ÉCHEC 'abc', 10 → None (attendu 'abc')
# =>   ÉCHEC 'abcde', 5 → None (attendu 'abcde')
# =>   ÉCHEC 'abcdefgh', 5 → None (attendu 'abcd…')
# =>   ÉCHEC '', 3 → None (attendu '')
# =>   4 échec(s)
"""
Tous les tests échouent : c'est rassurant, cela prouve que nos tests
vérifient réellement quelque chose. (Notez que len(obtenu) n'est jamais
appelé sur None : "or" s'arrête dès que la première condition est vraie,
cf. chap. 9.)
"""


# c) GREEN :
def tronquer(texte, n):
    if len(texte) <= n:
        return texte
    return texte[:n - 1] + "…"     # n - 1 caractères + "…" = n caractères


verifier_tronquer(tronquer)   # =>   0 échec(s)
"""
Tous les tests passent. On pourrait maintenant améliorer la fonction
(REFACTOR), par exemple pour couper sur un espace plutôt qu'au milieu d'un
mot, en relançant les tests après chaque modification.
"""
