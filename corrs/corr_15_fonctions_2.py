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
#  Chap. 15     #  Fonctions II : corrigés                                     #
#               #                                                              #
################################################################################


############################
#  Conventions de nommage  #
############################

"""
1. Les noms de fonctions :
    a) calculer_moyenne : parfait (snake_case, recommandé par la PEP 8).
    b) CalculerMoyenne : autorisé, mais ce style (PascalCase) est réservé aux
       noms de classes (cf. chap. 34). → calculer_moyenne
    c) 2eme_essai : INTERDIT, un nom ne peut pas commencer par un chiffre.
       → deuxieme_essai (ou essai_2)
    d) calculerMoyenne : autorisé (style "camelCase" de Java ou JavaScript),
       mais pas dans les conventions Python. → calculer_moyenne
    e) f : autorisé, mais ne dit rien de ce que fait la fonction. À réserver
       aux exemples très courts. → un nom qui décrit l'action
    f) convertir_euros_en_dollars : parfait, même s'il est long : un nom
       clair vaut mieux qu'un nom court.
"""
try:
    compile("def 2eme_essai(): pass", "<exercice>", "exec")
except SyntaxError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
(compile() vérifie la syntaxe d'un bout de code écrit dans une chaîne, sans
l'exécuter : c'est le seul moyen de montrer une SyntaxError sans faire
planter tout le fichier.)
"""


#############################
#  Arguments vs paramètres  #
#############################

# 2. Paramètres et arguments :
def aire(x, y):
    return x * y


largeur = 3
print(aire(largeur, 5))  # => 15
"""
- Les PARAMÈTRES sont les noms dans la définition : x et y.
- Les ARGUMENTS sont les valeurs passées à l'appel : largeur (qui vaut 3)
  et 5.
Pendant l'appel, x vaut 3 et y vaut 5 : le paramètre x reçoit la VALEUR de
la variable largeur.
"""

# 3. Il manque un argument :
try:
    aire(2)
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
aire() attend deux arguments : Python refuse l'appel avec un seul, et le
message dit précisément lequel manque (y).
"""


################################################
#  Paramètres par défaut et arguments nommés   #
################################################

# 4. Un paramètre par défaut :
def puissance(x, n=2):
    return x ** n


print(puissance(5))          # => 25 (n vaut 2 par défaut)
print(puissance(2, 10))      # => 1024
print(puissance(n=3, x=2))   # => 8
"""
Avec des arguments NOMMÉS, l'ordre n'a plus d'importance : chaque valeur est
associée au paramètre qui porte ce nom.
"""


# 5. Défauts et arguments nommés :
def commande(plat, quantite=1, sauce="aucune"):
    print(quantite, plat, "- sauce :", sauce)


commande("frites")
# => 1 frites - sauce : aucune
commande("frites", 3)
# => 3 frites - sauce : aucune
commande("frites", sauce="ketchup")
# => 1 frites - sauce : ketchup
commande(sauce="mayo", plat="nuggets", quantite=6)
# => 6 nuggets - sauce : mayo
"""
- Dans le 3e appel, l'argument nommé permet de préciser la sauce SANS
  donner la quantité (qui garde sa valeur par défaut).
- Dans le 4e, tous les arguments sont nommés : l'ordre est libre.
"""

# 6. Un paramètre sans défaut ne peut pas suivre un paramètre avec défaut :
try:
    compile('def message(texte="Bonjour", destinataire): pass',
            "<exercice>", "exec")
except SyntaxError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")


def message(destinataire, texte="Bonjour"):
    return texte + ", " + destinataire + " !"


print(message("Ada"))           # => Bonjour, Ada !
print(message("Ada", "Salut"))  # => Salut, Ada !
"""
Sinon, lors de l'appel message("Ada"), Python ne saurait pas si "Ada" est le
texte ou le destinataire. Les paramètres avec valeur par défaut viennent
donc toujours EN DERNIER.
"""


######################
#  La valeur None    #
######################

# 7. Un chemin sans return :
def f(x):
    if x > 0:
        return "positif"


print(f(5))   # => positif
print(f(-5))  # => None
"""
Pour x = -5, la condition est fausse : on arrive à la fin de la fonction
sans rencontrer de return. La fonction retourne alors None, la valeur
spéciale qui signifie « rien ».
"""


# 8. Retourner None quand on ne trouve rien :
def trouver_lettre(texte, lettre):
    for i in range(len(texte)):
        if texte[i] == lettre:
            return i
    return None  # explicite : plus lisible que de laisser la fonction finir


print(trouver_lettre("python", "t"))  # => 2
position = trouver_lettre("python", "z")
print(position is None)  # => True
if position is None:
    print("lettre absente")  # => lettre absente
"""
Pourquoi pas -1, comme .find() ? Parce que None ne peut pas être confondu
avec une vraie position. On teste None avec "is None" (et non "== None"),
c'est la convention en Python.
"""

# 9. None comparé à d'autres valeurs :
print(None == 0)      # => False
print(None == False)  # => False
print(None == None)   # => True
"""
None n'est égal qu'à lui-même : ce n'est ni 0, ni False, ni une chaîne vide.
"""


########################################
#  Différence entre return et print()  #
########################################

# 10. La moyenne qui plantait :
def moyenne_fausse(a, b):
    print((a + b) / 2)


m = moyenne_fausse(12, 16)  # => 14.0 (affiché, mais pas retourné)
try:
    print(m + 1)
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
La fonction AFFICHE la moyenne mais ne la retourne pas : m vaut None, et
None + 1 n'a pas de sens. Il faut remplacer le print par un return :
"""


def moyenne(a, b):
    return (a + b) / 2


m = moyenne(12, 16)
print(m + 1)  # => 15.0


# 11. Afficher ou retourner :
def afficher_perimetre(r):
    print(2 * 3.14159 * r)


def perimetre(r):
    return 2 * 3.14159 * r


afficher_perimetre(1)  # => 6.28318
print(perimetre(1) + perimetre(2))  # => 18.849539999999998
"""
(Le 8 final vient des arrondis des floats, cf. chap. 4 : on aurait pu
afficher round(…, 5), qui vaut 18.84954.)

Seule la version avec return permet de RÉUTILISER le résultat dans un
calcul. Règle pratique : une fonction calcule et retourne ; c'est le
programme principal qui décide d'afficher.
"""


###############################
#  Imbrication de fonctions   #
###############################

# 12. Appels imbriqués :
def ajouter_un(x):
    return x + 1


def doubler(x):
    return 2 * x


print(doubler(ajouter_un(3)))         # => 8
print(ajouter_un(doubler(3)))         # => 7
print(doubler(doubler(doubler(1))))   # => 8
"""
On calcule de l'intérieur vers l'extérieur :
    - doubler(ajouter_un(3)) → doubler(4) → 8
    - ajouter_un(doubler(3)) → ajouter_un(6) → 7 : l'ordre compte !
    - doubler(doubler(doubler(1))) → doubler(doubler(2)) → doubler(4) → 8
"""


# 13. Une fonction qui en utilise une autre :
def est_voyelle(c):
    return c in "aeiouy"


def compter_voyelles(texte):
    compteur = 0
    for c in texte:
        if est_voyelle(c):
            compteur = compteur + 1
    return compteur


print(compter_voyelles("fonctions imbriquees"))  # => 8
"""
Chaque fonction fait UNE chose : est_voyelle() décide, compter_voyelles()
compte. Pour gérer les voyelles accentuées, il suffirait de modifier
est_voyelle() : une seule source de vérité (cf. chap. 14).
"""


# 14. L'hypoténuse :
def carre(x):
    return x * x


def hypotenuse(a, b):
    return (carre(a) + carre(b)) ** 0.5


print(hypotenuse(3, 4))  # => 5.0
print(hypotenuse(5, 12))  # => 13.0


######################
#  Retour multiple   #
######################

# 15. Retourner deux valeurs :
def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)


petit, grand = min_max(7, 2, 9)
print(petit, grand)  # => 2 9
"""
"return x, y" retourne en fait un tuple (cf. chap. 17), que l'on "déballe"
dans deux variables, dans l'ordre.
"""


# 16. Heures, minutes, secondes :
def convertir_secondes(total):
    heures = total // 3600
    reste = total % 3600
    minutes = reste // 60
    secondes = reste % 60
    return heures, minutes, secondes


h, m, s = convertir_secondes(3725)
print(h, "h", m, "min", s, "s")  # => 1 h 2 min 5 s
"""
// donne la division entière, % le reste (cf. chap. 4) : 3725 s = 1 × 3600 s
+ 125 s, et 125 s = 2 × 60 s + 5 s.
"""


# 17. Trop de variables pour les valeurs retournées :
def deux_valeurs():
    return 1, 2


try:
    a, b, c = deux_valeurs()
except ValueError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
La fonction retourne 2 valeurs, mais on veut en ranger 3 : Python refuse
(ValueError). Il faut autant de variables que de valeurs retournées.
"""


#################################
#  L'adresse d'une fonction     #
#################################

# 18. La fonction elle-même, ou son résultat :
print(len)         # => <built-in function len>
print(len("abc"))  # => 3
"""
- Sans parenthèses, len désigne la fonction ELLE-MÊME : print affiche une
  description de l'objet fonction.
- Avec parenthèses, len("abc") APPELLE la fonction : print affiche le
  résultat, 3.
"""


# 19. Passer une fonction en argument :
def appliquer(fonction, a, b):
    return fonction(a, b)


def addition(x, y):
    return x + y


def multiplication(x, y):
    return x * y


print(appliquer(addition, 3, 4))        # => 7
print(appliquer(multiplication, 3, 4))  # => 12
"""
On passe addition SANS parenthèses : on donne la fonction elle-même, et
c'est appliquer() qui l'appelle. (On verra au chap. 32 d'autres usages de
cette idée très puissante.)
"""


# 20. Les parenthèses oubliées :
def salutation():
    return "Bonjour"


print(salutation)    # => <function salutation at 0x…> (adresse variable)
print(salutation())  # => Bonjour
"""
Sans parenthèses, on affiche la fonction (son "adresse" en mémoire, qui
change à chaque exécution), pas le résultat de son appel. C'est une erreur
très fréquente : la correction est d'ajouter les parenthèses.
"""
