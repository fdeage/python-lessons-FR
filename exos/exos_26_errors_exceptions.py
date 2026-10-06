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
#  Chap. 26     #  Erreurs et exceptions : exercices                           #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier.

Attention : dans ce chapitre, vous allez provoquer des erreurs exprès.
Protégez-les avec try: … except …: pour que votre fichier reste exécutable
jusqu'au bout.

Le corrigé contient un input() : il faudra répondre dans la console.

Les corrigés sont dans le fichier corr_26_errors_exceptions.py.
"""


########################################
#  Le mécanisme des erreurs en Python  #
########################################

"""
1. Sans exécuter, qu'affiche ce programme ? Quelles lignes ne sont jamais
   exécutées ?
       def etape_b():
           print("B1")
           x = int("douze")
           print("B2")

       def etape_a():
           print("A1")
           etape_b()
           print("A2")

       try:
           etape_a()
           print("fin du try")
       except ValueError:
           print("erreur interceptée")
       print("suite du programme")

2. Écrivez une fonction verifier_age(age) qui soulève une ValueError avec le
   message "un âge ne peut pas être négatif" si age < 0, et qui retourne age
   sinon. Appelez-la avec 30, puis avec -2 (protégé par un try).
"""


##############################
#  Lire un message d'erreur  #
##############################

"""
3. Un camarade vous montre ce traceback :

   Traceback (most recent call last):
     File "notes.py", line 12, in <module>
       print(moyenne_classe(classe))
     File "notes.py", line 8, in moyenne_classe
       total += moyenne_eleve(eleve)
     File "notes.py", line 3, in moyenne_eleve
       return sum(notes) / len(notes)
   ZeroDivisionError: division by zero

   Répondez (dans une string) :
       a) Quel est le type de l'erreur ? Que signifie le message ?
       b) Dans quelle fonction et à quelle ligne l'erreur a-t-elle lieu ?
       c) Quelle fonction a appelé cette fonction ?
       d) Quelle est la cause probable du problème (pensez aux données) ?

4. Même question pour celui-ci. Quelle est la faute, et comment la corriger ?

   Traceback (most recent call last):
     File "jeu.py", line 5, in <module>
       print(score_totl)
             ^^^^^^^^^^
   NameError: name 'score_totl' is not defined. Did you mean: 'score_total'?
"""


###############################################
#  Erreurs de syntaxe et erreurs d'exécution  #
###############################################

"""
5. Sans exécuter, classez chaque ligne : erreur de SYNTAXE, erreur
   d'EXÉCUTION, ou pas d'erreur ? Donnez le type d'erreur.
       a) print("bonjour"
       b) print(10 / 0)
       c) if x = 3: print(x)
       d) "abc" + 1
       e) liste = [1, 2, 3]
       f) for i in range(3) print(i)
       g) int("3.5")

6. Pourquoi ne peut-on pas écrire ceci pour se protéger d'une faute de
   frappe ?
       try:
           print("oups"
       except SyntaxError:
           print("parenthèse oubliée")
   Vérifiez qu'on peut, en revanche, détecter l'erreur avec compile() sur une
   string, comme dans le chapitre.
"""


#################################
#  Causes fréquentes d'erreurs  #
#################################

"""
7. Pour chaque ligne, quel type d'erreur est soulevé ? Écrivez chaque ligne
   dans un try avec le BON type dans le except (pas "Exception" !).
       [1, 2, 3][3]
       {"a": 1}["b"]
       "texte".append("!")
       len(42)
       int("quarante-deux")
       import module_qui_n_existe_pas
       open("fichier_absent.txt")
       variable_inconnue + 1
       2.5 ** 10000

8. Écrivez une fonction recherche_securisee(collection, cle) qui retourne
   collection[cle], ou None si la clé ou l'indice n'existe pas. Elle doit
   fonctionner aussi bien avec une liste qu'avec un dictionnaire, avec UN SEUL
   except.
"""


##################################
#  La hiérarchie des exceptions  #
##################################

"""
9. Sans exécuter, que vaut chaque expression ?
       issubclass(IndexError, LookupError)
       issubclass(ZeroDivisionError, Exception)
       issubclass(ValueError, TypeError)
       issubclass(ModuleNotFoundError, ImportError)
       issubclass(KeyboardInterrupt, Exception)

10. Sans exécuter, qu'affiche ce programme ? Pourquoi le 2e except est-il
    inutile ? Corrigez l'ordre des clauses.
        try:
            {"a": 1}["z"]
        except LookupError:
            print("problème de recherche")
        except KeyError:
            print("clé absente")
"""


#############################################
#  Gérer les erreurs avec try: … except: …  #
#############################################

"""
11. Écrivez une fonction division_sure(a, b) qui retourne a / b, ou :
        - None si b vaut 0 (ZeroDivisionError),
        - None si a ou b n'est pas un nombre (TypeError),
    en affichant un message différent dans chaque cas.

12. Écrivez une fonction convertir_tous(textes) qui convertit une liste de
    strings en entiers, en ignorant (et en comptant) celles qui ne sont pas
    des entiers valides. Elle retourne la liste des entiers obtenus.
        convertir_tous(["12", "abc", "7", "", "-3"])  → [12, 7, -3]
    et affiche "2 valeur(s) ignorée(s)".

13. Écrivez une fonction demander_entier(question) qui demande un entier à
    l'utilisateur avec input(). Si la saisie n'est pas un entier, elle affiche
    un message et redemande, au maximum 3 fois. Après 3 échecs, elle retourne
    None. Appelez-la une fois.

14. Pourquoi est-ce une mauvaise idée d'écrire ceci ? Que se passe-t-il si
    l'on fait une faute de frappe dans le nom de la variable ?
        try:
            resultat = 10 / diviseur
        except:
            resultat = 0
"""


#################################
#  Les clauses else et finally  #
#################################

"""
15. Sans exécuter, qu'affichent ces deux appels ?
        def test(x):
            try:
                print("début")
                r = 10 / x
            except ZeroDivisionError:
                print("division par zéro")
            else:
                print("résultat :", r)
            finally:
                print("fin")

        test(5)
        test(0)

16. Sans exécuter, que retourne f() ? (Piège !)
        def f():
            try:
                return "try"
            finally:
                print("finally")
"""


#############################################
#  Soulever ses propres erreurs avec raise  #
#############################################

"""
17. Écrivez une fonction creer_compte(pseudo, age) qui soulève :
        - une TypeError si pseudo n'est pas une string,
        - une ValueError si pseudo fait moins de 3 caractères,
        - une ValueError si age n'est pas entre 13 et 120,
    avec à chaque fois un message explicatif, et retourne le dictionnaire
    {"pseudo": pseudo, "age": age} sinon. Testez-la avec des valeurs valides,
    puis avec trois appels invalides protégés.

18. Écrivez une fonction lire_temperature(texte) qui convertit texte en float.
    En cas d'échec, elle affiche "Valeur illisible : …" puis RE-SOULÈVE la
    même erreur (pour que l'appelant sache que ça a échoué). Appelez-la avec
    "21.5", puis avec "chaud" (protégé).
"""


################################################
#  Live and let die : quand laisser crasher ?  #
################################################

"""
19. Écrivez deux versions d'une fonction prix(catalogue, produit) qui retourne
    le prix d'un produit dans un dictionnaire, ou 0 s'il est absent :
        a) dans le style LBYL (avec if),
        b) dans le style EAFP (avec try).
    catalogue = {"pain": 1.2, "lait": 0.9}

20. Pour chaque situation, faut-il intercepter l'erreur ou laisser le
    programme crasher ? Justifiez (dans une string).
        a) L'utilisateur tape "douze" au lieu de 12 dans un formulaire.
        b) Une fonction de calcul reçoit une liste de notes vide alors que le
           programme garantit qu'elle ne l'est jamais.
        c) Un fichier de 10 000 lignes de données contient 3 lignes mal
           formées.
        d) Le code appelle une fonction qui n'existe pas (faute de frappe).
"""
