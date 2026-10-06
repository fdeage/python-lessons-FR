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
#  Chap. 10     #  Variables I : corrigés                                      #
#               #                                                              #
################################################################################

###########################
#  Déclarer une variable  #
###########################

# 1. Suivons le programme ligne à ligne :
a = 3      # a vaut 3
b = a * 2  # b vaut 6 (calculé avec la valeur de a À CE MOMENT-LÀ)
a = 10     # a vaut 10… mais b vaut toujours 6
print(a, b)  # => 10 6
"""
Piège classique : b ne "se souvient" pas qu'il a été calculé à partir de a.
Au moment de la 2e ligne, Python calcule a * 2 (soit 6) et range ce NOMBRE
dans b. Modifier a ensuite ne change rien à b.
"""

# 2. On utilise total AVANT de l'avoir créée :
try:
    print(total)  # => NameError
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# Correction : il faut affecter la variable AVANT de l'utiliser.
total = 12 + 30
print(total)  # => 42

# 3. Au cinéma :
prix_place = 9.5
prix_menu = 6
nb_places = 3
nb_menus = 2
total = prix_place * nb_places + prix_menu * nb_menus
print(total)  # => 40.5
"""
Grâce aux noms parlants, le calcul se lit presque comme une phrase. Et si le
prix d'une place change, il suffit de modifier UNE ligne.
"""


###################################
#  Variables et types de valeurs  #
###################################

# 4. Le type d'une variable est celui de la valeur qu'elle contient :
nom = "Ada"
age = 36
taille = 1.65
est_majeure = age >= 18
code_postal = "75011"
print(type(nom))          # => <class 'str'>
print(type(age))          # => <class 'int'>
print(type(taille))       # => <class 'float'>
print(type(est_majeure))  # => <class 'bool'>
print(type(code_postal))  # => <class 'str'>
"""
est_majeure contient le RÉSULTAT de la comparaison age >= 18 : un booléen
(cf. chap. 9). code_postal est entre guillemets : c'est une chaîne.
"""

# 5. Un code postal n'est pas un nombre :
print(int("01000"))  # => 1000 (le zéro du début a disparu !)
"""
- Converti en entier, "01000" (Bourg-en-Bresse) devient 1000 : le zéro de
  tête est perdu.
- Et on ne fait jamais de calcul avec un code postal : additionner deux codes
  postaux n'a aucun sens.
C'est la même chose pour un numéro de téléphone ou de sécurité sociale : ce
sont des IDENTIFIANTS composés de chiffres, pas des quantités. On les range
dans des chaînes.
"""


###################################
#  Lire et modifier une variable  #
###################################

# 6. Suivons x ligne à ligne :
x = 4
x = x + 1  # x vaut 5
x *= 3     # x vaut 15
x -= 2     # x vaut 13
x //= 4    # x vaut 3 (13 // 4 : la division entière)
print(x)   # => 3

# 7. Le compte bancaire :
solde = 100
solde += 50    # dépôt : 150
solde -= 30    # retrait : 120
solde *= 1.02  # intérêts : 122.4
print(solde)   # => 122.4
"""
Note : après la multiplication par 1.02 (un float), solde contient un float.
Selon les calculs, l'imprécision des floats peut ajouter des décimales
parasites (cf. chap. 4) : pour un affichage, on arrondirait avec round().
"""

# 8. += fonctionne aussi pour concaténer des chaînes :
phrase = "Python"
phrase += " est"
phrase += " simple"
phrase += " et puissant"
print(phrase)  # => Python est simple et puissant

# 9. On ne peut pas "additionner" une chaîne et un entier :
nb_pommes = 4
try:
    print("J'ai " + nb_pommes + " pommes")  # => TypeError
except TypeError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# Correction 1 : on convertit l'entier en chaîne avec str()
print("J'ai " + str(nb_pommes) + " pommes")  # => J'ai 4 pommes
# Correction 2 : une f-string fait la conversion toute seule
print(f"J'ai {nb_pommes} pommes")  # => J'ai 4 pommes
"""
La f-string est plus lisible, et c'est la méthode recommandée (cf. chap. 8).
"""

# 10. Incrémenter et décrémenter :
compteur = 0
compteur += 1  # 1
compteur += 1  # 2
compteur -= 1  # 1
print(compteur)  # => 1


#######################
#  Règles de nommage  #
#######################

"""
11. Noms interdits (ils provoqueraient une SyntaxError, c'est pourquoi on ne
    peut pas les montrer dans du code exécutable) :
        - 2age : commence par un chiffre ;
        - mon-age : le tiret est lu comme une soustraction (mon - age) ;
        - class : mot-clé réservé de Python (cf. chap. 34) ;
        - prix total : contient un espace ;
        - None : mot-clé réservé (cf. chap. 15).
    Noms autorisés :
        - age2, mon_age, Prix : lettres, chiffres (pas au début) et "_" ;
        - _secret : on peut commencer par un underscore ;
        - été : autorisé, mais déconseillé (caractères non ASCII).
"""
age2 = 1
mon_age = 2
_secret = 3
Prix = 4
print(age2 + mon_age + _secret + Prix)  # => 10 (ces noms fonctionnent)

# 12. Les noms sont sensibles à la casse :
note = 12
Note = 15
print(note)  # => 12
"""
note et Note sont deux variables DIFFÉRENTES. Pour éviter toute confusion,
n'utilisez jamais deux noms qui ne diffèrent que par les majuscules.
"""

"""
13. str est le nom de la fonction intégrée str(). Si on écrit str = "abc", la
    variable str "cache" la fonction : tout appel à str() (par exemple
    str(5)) provoquera ensuite une TypeError ("'str' object is not
    callable"), jusqu'à la fin du programme. Il en va de même pour print,
    int, float, len, type, list, input…
"""


############################
#  Conventions de nommage  #
############################

# 14. Des noms en snake case, parlants :
nb_eleves = 28
prix_ht = 12.5
moyenne_generale = 13.2
print(nb_eleves, prix_ht, moyenne_generale)  # => 28 12.5 13.2
"""
- NbEleves est en CamelCase : en Python, on écrit nb_eleves.
- x ne dit rien de son contenu : prix_ht est bien plus clair.
- MOYENNEgenerale mélange les styles : moyenne_generale.
"""

# 15. Une valeur qui ne change jamais s'écrit en MAJUSCULES :
TAUX_TVA = 0.2
print(TAUX_TVA)  # => 0.2
"""
Par convention, les noms entièrement en majuscules signalent une
"constante" : une valeur fixée une fois pour toutes, qu'on ne modifie pas
(cf. chap. 19). Python ne l'interdit pas, mais tout le monde comprend qu'il ne
faut pas y toucher.
"""


##########################################
#  Quelques fonctions sur les variables  #
##########################################

# 16. Types et comparaisons :
a = 7
b = "7"
c = 7.0
print(type(a))  # => <class 'int'>
print(type(b))  # => <class 'str'>
print(type(c))  # => <class 'float'>
print(a == b)   # => False (un nombre n'est jamais égal à une chaîne)
print(a == c)   # => True (même valeur, même si les types diffèrent)

# 17. dir() liste les méthodes disponibles :
print("upper" in dir("abc"))  # => True
print("upper" in dir(42))     # => False
"""
dir() retourne la liste des noms disponibles sur une valeur. On teste ensuite
avec "in" si "upper" en fait partie : c'est le cas pour une chaîne (on peut
écrire "abc".upper()), mais pas pour un entier (mettre un nombre en
majuscules n'a pas de sens).
"""


##########################
#  Affectation multiple  #
##########################

# 18. Trois variables en une ligne :
nom, prenom, age = "Lovelace", "Ada", 36
print(prenom, nom, age)  # => Ada Lovelace 36

# 19. Échanger deux variables :
gauche = "pomme"
droite = "poire"
# a) avec une variable temporaire :
temporaire = gauche  # on met "pomme" de côté
gauche = droite      # gauche vaut "poire"
droite = temporaire  # droite récupère "pomme"
print(gauche, droite)  # => poire pomme
# b) en une seule ligne (on échange à nouveau, pour revenir au départ) :
gauche, droite = droite, gauche
print(gauche, droite)  # => pomme poire
"""
Python calcule d'abord TOUTES les valeurs de droite (droite, gauche), puis
les range dans les variables de gauche : il n'y a donc pas besoin de variable
temporaire.
"""

# 20. Une même valeur pour plusieurs variables :
x = y = 0
x += 1
print(x, y)  # => 1 0
"""
x et y reçoivent toutes les deux la valeur 0 au départ, mais ce sont deux
variables distinctes : modifier x ne change pas y.
"""

# 21. Trop de valeurs pour le nombre de variables :
try:
    a, b = 1, 2, 3  # => ValueError
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
Il faut exactement autant de variables à gauche que de valeurs à droite. Ici,
Python ne sait pas où ranger le 3.
"""


######################
#  Petits problèmes  #
######################

# 22. Conversion de température :
celsius = 37.5
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} °C = {fahrenheit} °F")  # => 37.5 °C = 99.5 °F

# 23. Durée d'une vidéo :
duree = 3725
heures = duree // 3600            # 3600 secondes dans une heure : 1
reste = duree % 3600              # il reste 125 secondes
minutes = reste // 60             # 2 minutes…
secondes = reste % 60             # … et 5 secondes
print(f"{heures} h {minutes} min {secondes} s")  # => 1 h 2 min 5 s
"""
La division entière "//" donne le nombre d'heures complètes, et le modulo "%"
ce qu'il reste. On recommence avec ce reste pour les minutes. Des variables
bien nommées rendent chaque étape facile à suivre.
"""

# 24. Moyenne pondérée :
note1, coef1 = 12, 2
note2, coef2 = 15, 3
note3, coef3 = 8, 1
somme = note1 * coef1 + note2 * coef2 + note3 * coef3  # 24 + 45 + 8 = 77
total_coefs = coef1 + coef2 + coef3                    # 6
moyenne = somme / total_coefs
print(round(moyenne, 2))  # => 12.83
"""
Chaque note compte autant de fois que son coefficient : on divise donc la
somme pondérée (77) par la somme des coefficients (6), et non par le nombre
de notes (3).
"""
