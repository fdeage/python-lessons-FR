################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Félix Déage - 2026                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 26     #  Erreurs et exceptions : corrigés                            #
#               #                                                              #
################################################################################

"""
Note : ce corrigé contient un input() (exercice 13) : il faudra répondre dans
la console. Les messages d'erreur affichés peuvent varier légèrement selon
votre version de Python.
"""


########################################
#  Le mécanisme des erreurs en Python  #
########################################

# 1. Remontée d'une erreur à travers les fonctions :
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
# => A1
# => B1
# => erreur interceptée
# => suite du programme
"""
int("douze") soulève une ValueError dans etape_b(). L'erreur interrompt
etape_b() (B2 n'est pas affiché), remonte dans etape_a() qui est interrompue à
son tour (A2 n'est pas affiché), puis remonte jusqu'au try, où elle est
interceptée : "fin du try" n'est pas affiché non plus. Le programme reprend
après le bloc try/except.
"""


# 2. Soulever une erreur :
def verifier_age(age):
    if age < 0:
        raise ValueError("un âge ne peut pas être négatif")
    return age


print(verifier_age(30))  # => 30
try:
    verifier_age(-2)
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : un âge ne peut pas
#    être négatif)


##############################
#  Lire un message d'erreur  #
##############################

# 3. Premier traceback :
"""
a) Une ZeroDivisionError : le programme a divisé par zéro.
b) Dans la fonction moyenne_eleve(), ligne 3 : return sum(notes) / len(notes).
   C'est l'avant-dernière ligne de la trace (l'appel le plus récent est en
   bas).
c) Elle a été appelée par moyenne_classe() (ligne 8), elle-même appelée depuis
   le programme principal (<module>, ligne 12).
d) len(notes) vaut 0 : un des élèves de la classe n'a AUCUNE note. Le bug
   n'est pas forcément dans moyenne_eleve() : il faut se demander d'où vient
   cette liste vide (données incomplètes ?) et décider quoi faire dans ce cas
   (ignorer l'élève, soulever une erreur plus explicite…).
"""

# 4. Second traceback :
"""
Une NameError : la variable score_totl n'existe pas. C'est une faute de
frappe, et Python suggère même la correction ("Did you mean: 'score_total'?").
Il suffit d'écrire print(score_total) à la ligne 5. Les ^^^^ indiquent la
partie exacte de la ligne qui pose problème.
"""


###############################################
#  Erreurs de syntaxe et erreurs d'exécution  #
###############################################

# 5. Classement :
"""
a) SYNTAXE (SyntaxError) : la parenthèse n'est jamais fermée.
b) EXÉCUTION (ZeroDivisionError).
c) SYNTAXE (SyntaxError) : dans une condition, il faut "==" et non "=".
d) EXÉCUTION (TypeError) : on ne peut pas additionner une string et un int.
e) Pas d'erreur.
f) SYNTAXE (SyntaxError) : il manque les ":" à la fin de la ligne du for.
g) EXÉCUTION (ValueError) : "3.5" n'est pas l'écriture d'un entier (il
   faudrait int(float("3.5"))).
On le vérifie avec compile() (cf. chapitre) : seules les erreurs de syntaxe
sont détectées sans exécuter le code.
"""
codes = ['print("bonjour"', 'print(10 / 0)', 'if x = 3: print(x)',
         '"abc" + 1', 'liste = [1, 2, 3]', 'for i in range(3) print(i)',
         'int("3.5")']
for code in codes:
    try:
        compile(code, "<exercice>", "exec")
        print(f"{code!r:32} → syntaxe correcte")
    except SyntaxError:
        print(f"{code!r:32} → erreur de syntaxe")
# => 'print("bonjour"'                → erreur de syntaxe
# => 'print(10 / 0)'                  → syntaxe correcte
# => 'if x = 3: print(x)'             → erreur de syntaxe
# => '"abc" + 1'                      → syntaxe correcte
# => 'liste = [1, 2, 3]'              → syntaxe correcte
# => 'for i in range(3) print(i)'     → erreur de syntaxe
# => 'int("3.5")'                     → syntaxe correcte
"""
"syntaxe correcte" ne veut pas dire "pas d'erreur" : b, d et g sont du Python
valide, mais échoueront À L'EXÉCUTION.
(Note : {code!r:32} affiche le repr() de code sur 32 caractères, pour aligner
les colonnes, cf. chap. 8.)
"""

# 6. Pourquoi ce try est inutile :
"""
Python lit (compile) le fichier EN ENTIER avant d'en exécuter la moindre
ligne. La parenthèse manquante est détectée à ce moment-là : le try n'a
encore jamais été exécuté, et ne peut donc rien intercepter. Le fichier
entier refuse de se lancer. La seule solution : corriger la faute.
"""
try:
    compile('print("oups"', "<exercice>", "exec")
except SyntaxError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
Ici, ça fonctionne car le code fautif est dans une STRING : il n'est compilé
qu'au moment où compile() est exécutée, donc à l'intérieur du try.
"""


#################################
#  Causes fréquentes d'erreurs  #
#################################

# 7. Le bon type d'erreur pour chaque ligne :
try:
    [1, 2, 3][3]
except IndexError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    {"a": 1}["b"]
except KeyError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    "texte".append("!")
except AttributeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    len(42)
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    int("quarante-deux")
except ValueError as err:
    print(f"7: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    import module_qui_n_existe_pas
except ModuleNotFoundError as err:
    print(f"8: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    open("fichier_absent.txt")
except FileNotFoundError as err:
    print(f"9: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    variable_inconnue + 1
except NameError as err:
    print(f"10: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    2.5 ** 10000
except OverflowError as err:
    print(f"11: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- [1, 2, 3][3] : IndexError (les indices vont de 0 à 2).
- {"a": 1}["b"] : KeyError (la clé n'existe pas). Le message est la clé
  elle-même : 'b'.
- "texte".append("!") : AttributeError (les strings n'ont pas de méthode
  .append(), c'est une méthode de liste).
- len(42) : TypeError (un int n'a pas de longueur).
- int("quarante-deux") : ValueError (le TYPE est bon, une string, mais sa
  VALEUR ne peut pas être convertie).
- import … : ModuleNotFoundError (une ImportError particulière).
- open(…) : FileNotFoundError (une OSError particulière).
- variable_inconnue : NameError.
- 2.5 ** 10000 : OverflowError (le résultat dépasse la capacité d'un float ;
  avec des int, Python n'aurait pas eu de limite).
"""


# 8. Recherche sécurisée :
def recherche_securisee(collection, cle):
    try:
        return collection[cle]
    except LookupError:
        return None


print(recherche_securisee([10, 20], 1))       # => 20
print(recherche_securisee([10, 20], 5))       # => None
print(recherche_securisee({"a": 1}, "a"))     # => 1
print(recherche_securisee({"a": 1}, "z"))     # => None
"""
IndexError (liste) et KeyError (dictionnaire) descendent toutes les deux de
LookupError : un seul "except LookupError" intercepte les deux.
"""


##################################
#  La hiérarchie des exceptions  #
##################################

# 9. Parentés :
print(issubclass(IndexError, LookupError))          # => True
print(issubclass(ZeroDivisionError, Exception))     # => True
print(issubclass(ValueError, TypeError))            # => False
print(issubclass(ModuleNotFoundError, ImportError))  # => True
print(issubclass(KeyboardInterrupt, Exception))     # => False
"""
- ZeroDivisionError descend de ArithmeticError, qui descend de Exception :
  issubclass() remonte toute la lignée.
- ValueError et TypeError sont "cousines" : aucune ne descend de l'autre.
- KeyboardInterrupt descend directement de BaseException, PAS de Exception :
  c'est voulu, pour que Ctrl+C fonctionne même avec un "except Exception".
"""

# 10. L'ordre des except :
try:
    {"a": 1}["z"]
except LookupError:
    print("problème de recherche")
except KeyError:
    print("clé absente")
# => problème de recherche
"""
Python teste les clauses except DANS L'ORDRE, et s'arrête à la première qui
convient. Une KeyError EST une LookupError : la 1re clause l'intercepte
toujours, et la 2e ne sera jamais utilisée. Il faut placer les erreurs les
plus PRÉCISES en premier :
"""
try:
    {"a": 1}["z"]
except KeyError:
    print("clé absente")
except LookupError:
    print("problème de recherche")
# => clé absente


#############################################
#  Gérer les erreurs avec try: … except: …  #
#############################################

# 11. Division sûre :
def division_sure(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erreur : division par zéro")
        return None
    except TypeError:
        print("Erreur : a et b doivent être des nombres")
        return None


print(division_sure(10, 4))    # => 2.5
print(division_sure(10, 0))
# => Erreur : division par zéro
# => None
print(division_sure(10, "2"))
# => Erreur : a et b doivent être des nombres
# => None


# 12. Convertir en ignorant les valeurs invalides :
def convertir_tous(textes):
    entiers = []
    nb_ignorees = 0
    for texte in textes:
        try:
            entiers.append(int(texte))
        except ValueError:
            nb_ignorees += 1
    print(f"{nb_ignorees} valeur(s) ignorée(s)")
    return entiers


print(convertir_tous(["12", "abc", "7", "", "-3"]))
# => 2 valeur(s) ignorée(s)
# => [12, 7, -3]
"""
Le try est À L'INTÉRIEUR de la boucle : une valeur invalide ne fait sauter
que son tour de boucle, et on passe à la suivante. Si le try entourait toute
la boucle, la première erreur arrêterait la conversion de toute la liste.
"""


# 13. Saisie avec 3 essais :
def demander_entier(question):
    for essai in range(3):
        saisie = input(question)
        try:
            return int(saisie)
        except ValueError:
            restants = 2 - essai
            print(f"'{saisie}' n'est pas un entier "
                  f"({restants} essai(s) restant(s))")
    return None


nombre = demander_entier("Entrez un entier : ")
print("Vous avez saisi :", nombre)
# => (dépend de votre saisie)
"""
Si int(saisie) réussit, return sort immédiatement de la fonction (et donc de
la boucle). Sinon, on affiche un message et la boucle passe à l'essai suivant.
Après 3 échecs, la boucle se termine et la fonction retourne None.
"""

# 14. Le "except:" nu :
diviseur_correct = 4
try:
    resultat = 10 / diviseur_corect  # faute de frappe volontaire !
except:
    resultat = 0
print(resultat)  # => 0
"""
Un "except:" sans type intercepte TOUTES les erreurs, y compris celles qu'on
n'avait pas prévues. Ici, la faute de frappe (diviseur_corect) produit une
NameError… qui est silencieusement transformée en résultat 0 ! Le bug est
caché, et le programme continue avec une valeur fausse.

Il faut intercepter uniquement l'erreur que l'on sait gérer :
"""
try:
    resultat = 10 / diviseur_corect
except ZeroDivisionError:
    resultat = 0
except NameError as err:
    print(f"12: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
Avec "except ZeroDivisionError", la NameError n'aurait pas été interceptée :
le programme aurait crashé avec un message clair, et on aurait corrigé la
faute (le 2e except n'est là que pour garder ce fichier exécutable).
"""


#################################
#  Les clauses else et finally  #
#################################

# 15. Ordre d'exécution :
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
# => début
# => résultat : 2.0
# => fin
test(0)
# => début
# => division par zéro
# => fin
"""
- else n'est exécuté que s'il n'y a PAS eu d'erreur dans le try.
- finally est exécuté DANS TOUS LES CAS.
"""


# 16. return et finally :
def f():
    try:
        return "try"
    finally:
        print("finally")


print(f())
# => finally
# => try
"""
Piège : même un return ne court-circuite pas finally ! Python prépare la
valeur à retourner ("try"), exécute le bloc finally (qui affiche "finally"),
PUIS sort de la fonction. Le print() extérieur affiche donc "try" en
dernier.
"""


#############################################
#  Soulever ses propres erreurs avec raise  #
#############################################

# 17. Créer un compte :
def creer_compte(pseudo, age):
    if type(pseudo) != str:
        raise TypeError("le pseudo doit être une string")
    if len(pseudo) < 3:
        raise ValueError(f"le pseudo {pseudo!r} est trop court "
                         "(3 caractères min.)")
    if not 13 <= age <= 120:
        raise ValueError(f"l'âge {age} n'est pas entre 13 et 120")
    return {"pseudo": pseudo, "age": age}


print(creer_compte("ada", 36))  # => {'pseudo': 'ada', 'age': 36}
try:
    creer_compte(42, 36)
except TypeError as err:
    print(f"13: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    creer_compte("al", 36)
except ValueError as err:
    print(f"14: (Sans ce try: … except …, cette ligne créerait : {err})")
try:
    creer_compte("ada", 8)
except ValueError as err:
    print(f"15: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
- TypeError : le paramètre n'a pas le bon TYPE.
- ValueError : le type est bon, mais la VALEUR est inacceptable.
L'ordre des tests compte : on vérifie le type AVANT d'appeler len(pseudo),
sinon len(42) soulèverait une TypeError beaucoup moins claire.
"""


# 18. Re-soulever une erreur :
def lire_temperature(texte):
    try:
        return float(texte)
    except ValueError:
        print(f"Valeur illisible : {texte!r}")
        raise


print(lire_temperature("21.5"))  # => 21.5
try:
    lire_temperature("chaud")
except ValueError as err:
    print(f"16: (Sans ce try: … except …, cette ligne créerait : {err})")
# => Valeur illisible : 'chaud'
# => 16: (Sans ce try: … except …, cette ligne créerait : could not convert
#    string to float: 'chaud')
"""
"raise" seul, dans un except, re-soulève l'erreur en cours. La fonction a
signalé le problème (affichage), mais laisse l'appelant décider quoi faire.
"""


################################################
#  Live and let die : quand laisser crasher ?  #
################################################

catalogue = {"pain": 1.2, "lait": 0.9}


# 19. a) Style LBYL ("regarde avant de sauter") :
def prix_lbyl(catalogue, produit):
    if produit in catalogue:
        return catalogue[produit]
    return 0


# 19. b) Style EAFP ("demande pardon plutôt que la permission") :
def prix_eafp(catalogue, produit):
    try:
        return catalogue[produit]
    except KeyError:
        return 0


print(prix_lbyl(catalogue, "pain"), prix_lbyl(catalogue, "beurre"))  # => 1.2 0
print(prix_eafp(catalogue, "pain"), prix_eafp(catalogue, "beurre"))  # => 1.2 0
"""
Les deux sont correctes. Pour un dictionnaire, le plus simple reste
catalogue.get(produit, 0) (cf. chap. 27).
"""

# 20. Intercepter ou laisser crasher ?
"""
a) INTERCEPTER : c'est une erreur prévisible de l'utilisateur, et on sait
   quoi faire (afficher un message et redemander, cf. exercice 13).
b) LAISSER CRASHER (ou soulever une erreur explicite) : la situation est
   "impossible", c'est donc le signe d'un BUG ailleurs dans le programme.
   Renvoyer une valeur arbitraire (0 ?) cacherait le problème et fausserait
   les résultats.
c) INTERCEPTER : on ignore (et on compte, ou on enregistre) les lignes mal
   formées, comme à l'exercice 12. Perdre 3 lignes sur 10 000 est souvent
   acceptable… à condition de le savoir !
d) LAISSER CRASHER : c'est un bug du programmeur, il faut le corriger. Le
   traceback indique exactement où.
"""
