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
#  Chap. 37     #  Tests et spécification II : exercices                       #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier.

Ce fichier doit rester exécutable SANS pytest. Pour les exercices qui
demandent du code pytest, deux possibilités :
    - écrivez-le dans un fichier séparé test_exo37.py, et lancez
      "python3 -m pytest test_exo37.py" dans un terminal (après avoir
      installé pytest, cf. chap. 22 et 37) ;
    - ou écrivez-le ici en commentaire, ou dans une chaîne de caractères.

Les corrigés sont dans le fichier corr_37_tests_2.py.

Voici les fonctions à tester dans les exercices :
"""
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
    """
    return sum(1 for v in valeurs if v is not None) / len(valeurs)


#####################################
#  Les limites de assert tout seul  #
#####################################

"""
1. Sans exécuter : combien de ces assert sont exécutés avant que le
   programme ne s'arrête ? Quelle information manque dans le message
   d'erreur ?
       assert est_bissextile(2024)
       assert est_bissextile(1900)
       assert est_bissextile(2000)
       assert not est_bissextile(2023)

2. Citez trois avantages d'un framework de test (comme pytest) par rapport
   à une liste d'assert placée à la fin du programme.
"""


#########################################
#  Ranger ses tests dans des fonctions  #
#########################################

"""
3. Écrivez 4 fonctions de test (nommées test_…) pour est_bissextile() :
   une année divisible par 4, une année non divisible par 4, une année
   séculaire non bissextile (1900), une année séculaire bissextile (2000).
   Choisissez des noms qui expliquent ce que chaque test vérifie.

4. Écrivez une fonction lancer(tests) qui exécute une liste de fonctions de
   test, affiche "OK" ou "ÉCHEC" pour chacune, et retourne le nombre
   d'échecs. Utilisez-la sur vos 4 tests.
"""


##########################################
#  pytest : installation et conventions  #
##########################################

"""
5. Parmi ces noms, lesquels seront trouvés automatiquement par pytest ?
       fichiers : test_calculs.py, calculs_test.py, tests_calculs.py,
                  calculs.py, mes_tests.py
       fonctions : test_moyenne(), moyenne_test(), tester_moyenne(),
                   test_(), Test_moyenne()
"""


######################################
#  Lancer pytest et lire un rapport  #
######################################

"""
6. Voici un extrait de rapport pytest. Répondez aux questions.
       test_stats.py .F.F.                                       [100%]
       ...
       >       assert mediane([3, 1, 2]) == 2
       E       assert 1 == 2
       E        +  where 1 = mediane([3, 1, 2])
       ...
       2 failed, 3 passed in 0.04s
   a) Combien de tests ont été exécutés ? Lesquels (n° d'ordre) ont échoué ?
   b) Quelle valeur a été obtenue, et laquelle était attendue ?
   c) D'après vous, quelle erreur la fonction mediane() contient-elle
      probablement ?

7. Quelle commande lance uniquement les tests dont le nom contient
   "email", en s'arrêtant au premier échec ?
"""


########################################
#  Tester les erreurs : pytest.raises  #
########################################

"""
8. Écrivez (en pytest) un test qui vérifie que normaliser_email("pas-d-arobase")
   soulève une ValueError dont le message contient "invalide".
   Puis écrivez le même test SANS pytest (avec try/except/else), et
   exécutez-le.
"""


####################################################
#  Tester plusieurs cas : pytest.mark.parametrize  #
####################################################

"""
9. Écrivez (en pytest) un test paramétré de normaliser_email() avec au
   moins 4 cas : majuscules, espaces autour, e-mail déjà correct, mélange
   des deux.
   Puis faites la même chose sans pytest, avec une liste de cas et une
   boucle.

10. Sans exécuter : combien de tests pytest compte-t-il pour ce code ?
        @pytest.mark.parametrize("a, b", [(1, 2), (3, 4), (5, 6)])
        def test_somme(a, b):
            assert a + b > 0

        def test_autre():
            assert True
"""


#########################################
#  Préparer des données : les fixtures  #
#########################################

"""
11. Écrivez une fixture releves qui retourne la liste
    [12.5, None, 13.0, None, 14.5], puis deux tests qui l'utilisent :
    l'un vérifie taux_de_remplissage(releves) == 0.6, l'autre vérifie que
    releves contient 5 valeurs.

12. Pourquoi est-il important que chaque test reçoive des données "toutes
    neuves" ? Imaginez un test qui fait releves.append(10) : que se
    passerait-il pour les autres tests si les données étaient partagées ?
"""


###################################################
#  unittest, l'outil de la bibliothèque standard  #
###################################################

"""
13. Écrivez une classe TestBissextile(unittest.TestCase) avec trois
    méthodes de test pour est_bissextile() (utilisez assertTrue et
    assertFalse). Lancez-la avec unittest.TextTestRunner, sans quitter le
    programme.

14. Traduisez ce test pytest en unittest :
        def test_email_vide():
            with pytest.raises(ValueError):
                normaliser_email("")
"""


######################################################
#  doctest : des exemples qui se testent tout seuls  #
######################################################

"""
15. Ajoutez une docstring avec 3 exemples doctest (">>>") à une fonction
    initiales(nom_complet) qui retourne les initiales en majuscules :
    initiales("ada lovelace") == "A.L.". Vérifiez avec doctest.

16. taux_de_remplissage([]) soulève une erreur. Laquelle ? Écrivez un
    doctest qui documente ce comportement.
"""


###############################
#  Organiser un projet testé  #
###############################

"""
17. Vous avez un projet avec deux modules : meteo/lecture.py (lit des CSV
    de relevés) et meteo/stats.py (calcule moyennes et extrêmes). Proposez
    une arborescence, avec les noms des fichiers de tests.
"""


#######################################
#  Rappel : écrire les tests d'abord  #
#######################################

"""
18. TDD : on veut une fonction tronquer(texte, n) qui coupe un texte trop
    long à n caractères, en terminant par "…" (le "…" compte dans les n
    caractères) ; un texte assez court est retourné tel quel.
    a) THINK : listez au moins 4 cas à tester, dont des cas limites.
    b) RED : écrivez les tests (sans pytest), et constatez qu'ils échouent
       avec une version vide de la fonction (qui retourne None).
    c) GREEN : écrivez la fonction pour que tous les tests passent.
"""
