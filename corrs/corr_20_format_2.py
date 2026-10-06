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
#  Chap. 20     #  Formatage II : corrigés                                     #
#               #                                                              #
################################################################################

##################################
#  Pourquoi formater son code ?  #
##################################

"""
1. Trois raisons (parmi d'autres) :
     - le code est lu beaucoup plus souvent qu'il n'est écrit : un style
       régulier se lit plus vite, même par soi-même dans six mois ;
     - en équipe, tout le monde écrit pareil : on lit le fond, pas la forme,
       et les différences entre deux versions (git diff) ne montrent que les
       vraies modifications ;
     - un code bien présenté rend certaines erreurs visibles (indentation,
       opérateurs collés, noms trompeurs).

2. Oui, les deux fonctions font exactement le même calcul :
"""
def f(a, b):
    return a * b / 2


def aire_triangle(base, hauteur):
    return base * hauteur / 2


print(f(6, 4))              # => 12.0
print(aire_triangle(6, 4))  # => 12.0
"""
La version b) est bien plus facile à relire : son nom dit ce qu'elle calcule,
ses paramètres disent ce qu'ils représentent, et la PEP 8 interdit de mettre
le corps d'une fonction sur la même ligne que "def".
"""


########################
#  La PEP 8 : nommage  #
########################

# 3. Constante en MAJUSCULES, fonction et paramètres en snake_case, noms
#    parlants :
TAUX_TVA = 0.2


def calculer_prix_ttc(prix_unitaire, quantite):
    prix_hors_taxes = prix_unitaire * quantite
    return prix_hors_taxes * (1 + TAUX_TVA)


print(calculer_prix_ttc(10, 3))  # => 36.0
"""
Note : un nom de fonction commence souvent par un verbe (calculer, afficher,
lire…), puisqu'une fonction FAIT quelque chose.

4. Revue des noms :
     - nombreEleves : camelCase, autorisé par Python mais contraire à la PEP 8
       (→ nombre_eleves) ;
     - nombre_eleves, note_moyenne : corrects ;
     - NOMBRE_MAX : correct pour une constante ;
     - 2eme_note : INTERDIT, un nom ne peut pas commencer par un chiffre
       (SyntaxError) → deuxieme_note ;
     - l : autorisé, mais la PEP 8 le déconseille explicitement (on le
       confond avec 1 et I) ;
     - list : autorisé, mais DANGEREUX : on masque la fonction intégrée list()
       (cf. chap. 19) ;
     - class : INTERDIT, c'est un mot-clé de Python (SyntaxError) ;
     - _total : correct ; le "_" initial signale par convention une variable
       "interne", à ne pas utiliser depuis l'extérieur ;
     - Prix_TTC : ni snake_case ni constante → prix_ttc.
"""
# On peut vérifier les deux noms interdits avec compile(), qui analyse une
# chaîne comme du code Python, sans l'exécuter (cf. chap. 26) :
try:
    compile("2eme_note = 12", "<exercice>", "exec")
except SyntaxError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    compile("class = 3", "<exercice>", "exec")
except SyntaxError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


########################################
#  La PEP 8 : espaces et lignes vides  #
########################################

# 5. Un espace autour des opérateurs et du "=" d'affectation, un espace après
#    les virgules, aucun espace juste à l'intérieur des parenthèses et des
#    crochets, et PAS d'espace autour du "=" d'un argument nommé :
def aire(longueur, largeur):
    return longueur * largeur


resultat = aire(3, 4)
print(resultat)            # => 12
print("a", "b", sep="-")   # => a-b
liste = [1, 2, 3]


# 6. Deux lignes vides avant et après chaque fonction "de premier niveau" ;
#    les imports en haut du fichier, suivis eux aussi de deux lignes vides
#    (ici, l'import est placé en milieu de fichier pour suivre l'énoncé ;
#    dans un vrai fichier, il serait tout en haut) :
import math


def perimetre_cercle(rayon):
    return 2 * math.pi * rayon


def aire_cercle(rayon):
    return math.pi * rayon ** 2


print(perimetre_cercle(1))  # => 6.283185307179586
print(aire_cercle(1))       # => 3.141592653589793
"""
Note : dans le corps d'une fonction, on peut aussi utiliser UNE ligne vide
pour séparer des étapes logiques, mais avec modération.
"""


####################################
#  La PEP 8 : longueur des lignes  #
####################################

# 7. On crée d'abord des valeurs pour pouvoir exécuter le code :
prix_unitaire_hors_taxes = 25
quantite_commandee = 4
taux_de_tva = 0.2
remise_fidelite = 10

# a) Avec des parenthèses : à l'intérieur, on peut passer à la ligne librement.
#    On coupe AVANT les opérateurs, pour les voir en début de ligne :
prix_total = (
    prix_unitaire_hors_taxes * quantite_commandee * (1 + taux_de_tva)
    - remise_fidelite
)
print(prix_total)  # => 110.0

# b) Avec des variables intermédiaires : souvent plus lisible, car chaque
#    étape a un nom.
prix_hors_taxes = prix_unitaire_hors_taxes * quantite_commandee
prix_ttc = prix_hors_taxes * (1 + taux_de_tva)
prix_total = prix_ttc - remise_fidelite
print(prix_total)  # => 110.0


# 8. La fonction, puis l'appel avec un argument par ligne. On laisse une
#    virgule après le dernier argument ("trailing comma") : ajouter un
#    argument ne modifiera qu'une seule ligne.
def construire_message(debut, nom, objet, etat, ponctuation="."):
    return debut + " " + nom + " " + objet + " " + etat + ponctuation


message = construire_message(
    "Bonjour",
    "Ada Lovelace",
    "votre commande n°1042",
    "est prête",
    ponctuation="!",
)
print(message)  # => Bonjour Ada Lovelace votre commande n°1042 est prête!

# 9. Deux chaînes écrites côte à côte sont collées automatiquement par Python.
#    Les parenthèses permettent de les répartir sur plusieurs lignes (attention
#    à ne pas oublier l'espace à la fin du premier morceau) :
avertissement = (
    "Attention : ce programme supprime définitivement les fichiers "
    "temporaires du dossier courant."
)
print(avertissement)
# => Attention : ce programme supprime définitivement les fichiers temporaires
#    du dossier courant.  (sur une seule ligne)


######################################################
#  La PEP 8 : imports, comparaisons et commentaires  #
######################################################

# 10. Les imports vont TOUT EN HAUT du fichier (ici, on les place au début de
#     l'exercice), un module par ligne, par ordre alphabétique. On importe
#     seulement ce dont on a besoin, au lieu de "from math import *" qui
#     cache l'origine des noms (cf. chap. 22). Les modules os, sys et random
#     n'étant pas utilisés, la meilleure correction est même de les supprimer.
from math import sqrt

print("Début")   # => Début
print(sqrt(16))  # => 4.0

# 11. Valeurs de test :
est_connecte = True
resultat = None
mot = "python"
liste = [1, 2]

if est_connecte:          # et non "== True" : est_connecte est déjà un booléen
    print("ok")           # => ok
if resultat is None:      # None se teste avec "is" (cf. chap. 21)
    print("rien")         # => rien
if "x" not in mot:        # "not in" se lit comme de l'anglais
    print("pas de x")     # => pas de x
if len(liste) != 0:       # ou, encore plus court : "if liste:" (cf. chap. 21)
    print("liste non vide")  # => liste non vide

# 12. Valeurs de test :
i = 0
prix = 100
x = 50

i = i + 1  # (aucun commentaire : le code se suffit à lui-même)
# Calcul de la TVA à 5,5 % (taux réduit)
tva = prix * 0.055
x = x * 1.1  # Majoration de 10 % demandée par le client en 2023
print(i, tva, round(x, 2))  # => 1 5.5 55.0
"""
- "# ajoute 1 à i" répète le code : inutile, on le supprime (et il manquait
  le 2e espace avant le "#") ;
- "#calcul" : il faut un espace après le "#" ;
- "# TVA à 20 %" est FAUX : le code calcule 5,5 %. Un commentaire faux est
  pire que pas de commentaire : on le corrige ;
- le dernier commentaire est utile : il explique POURQUOI (on le garde, avec
  juste une majuscule).
"""


####################################
#  La PEP 20 : le "Zen of Python"  #
####################################

# 13. Affiche les 19 aphorismes du Zen (il suffit de l'importer) :
import this  # => The Zen of Python, by Tim Peters …
"""
Exemples d'explications :
  - "Readability counts." : un programme est lu bien plus souvent qu'il n'est
    écrit, donc sa lisibilité compte autant que son bon fonctionnement ;
  - "Explicit is better than implicit." : on préfère écrire clairement ce
    qu'on fait (ex. "import math" puis "math.sqrt") plutôt que de le cacher
    (ex. "from math import *") ;
  - "Errors should never pass silently." : on ne doit pas cacher une erreur
    (par exemple avec un "except" vide, cf. chap. 26).
"""

# 14. La version b) : "Readability counts", "Sparse is better than dense" et
#     "Flat is better than nested". La version a) tient sur une ligne, mais il
#     faut la relire trois fois pour la comprendre. Les deux affichent bien la
#     même chose :
for x in range(10):
    est_pair_non_multiple_de_3 = x % 2 == 0 and x % 3 != 0
    if est_pair_non_multiple_de_3 or x == 9:
        print(x)  # => 2, 4, 8 et 9 (sur 4 lignes)


#########################
#  Outils de formatage  #
#########################

"""
15. Un linter ANALYSE le code et signale les problèmes (style, mais aussi
    erreurs probables), sans forcément les corriger. Un formatteur RÉÉCRIT la
    présentation du code, sans en changer le sens.
      a) variable importée mais inutilisée : le linter (ruff check, flake8) ;
      b) espaces autour des opérateurs : le formatteur (black, ruff format) ;
      c) lignes vides avant une fonction : le formatteur ;
      d) "== None" : le linter (le formatteur ne change jamais le sens du
         code, or "==" et "is" ne font pas la même chose).

16. "--diff" affiche les modifications que ruff FERAIT, sans toucher au
    fichier : les lignes précédées de "-" seraient supprimées, celles
    précédées de "+" ajoutées. Sans cette option, "ruff format brouillon.py"
    réécrit directement le fichier.

17. Les outils accepteront des lignes jusqu'à 100 caractères au lieu de 88
    (valeur par défaut de ruff et black). Ce réglage est mis dans le projet
    pour que TOUTE l'équipe (et les outils automatiques, cf. ci-dessous)
    applique les mêmes règles, quel que soit l'éditeur de chacun.
"""


############################
#  Configurer son éditeur  #
############################

"""
18. Les réglages dépendent de l'éditeur. Par exemple, dans VS Code
    (Préférences > Paramètres, ou le fichier settings.json) :
        "editor.rulers": [79],
        "editor.renderWhitespace": "all",
        "editor.insertSpaces": true,
        "editor.tabSize": 4,
        "editor.formatOnSave": true
    (le dernier réglage nécessite une extension de formatage, comme Ruff ou
    Black Formatter). Dans Sublime Text, les réglages équivalents sont
    "rulers", "draw_white_space", "translate_tabs_to_spaces" et "tab_size".

19. Contenu du fichier .editorconfig :

        root = true

        [*.py]
        charset = utf-8
        indent_style = space
        indent_size = 4
        insert_final_newline = true
"""


##########################
#  Automatiser avec git  #
##########################

"""
20. Un hook git est un programme que git lance automatiquement à un moment
    précis, par exemple juste avant d'enregistrer un commit. Lancer le
    formatteur à ce moment-là garantit qu'AUCUN code mal formaté n'entre dans
    le dépôt : on ne dépend plus de la mémoire ni de la discipline de chacun.

21. L'ordre est : b) installer pre-commit, c) créer le fichier de
    configuration, a) activer le hook dans le dépôt, puis d) commiter.
    Au moment de d), si un fichier est mal formaté, ruff le reformate et le
    commit est ANNULÉ : on relit les modifications, on les ajoute
    (?> git add …) et on relance le commit.
"""


#####################################
#  Synthèse : un programme complet  #
#####################################

# 22. Version reformatée. Changements : imports inutiles supprimés (math et
#     sys ne servent à rien), espaces, lignes vides, une instruction par ligne
#     (pas de ";"), noms parlants en snake_case, "is not None", et une
#     f-string à la place de la concaténation (cf. chap. 8).
SEUIL = 10


def calculer_moyenne(notes, seuil=SEUIL):
    total = 0
    nombre = 0
    for note in notes:
        if note >= seuil:
            total += note
            nombre += 1
    if nombre == 0:
        return None
    return total / nombre


notes = [12, 8, 15, 9, 18]
moyenne = calculer_moyenne(notes)
if moyenne is not None:
    print(f"Moyenne : {round(moyenne, 2)}")  # => Moyenne : 15.0
