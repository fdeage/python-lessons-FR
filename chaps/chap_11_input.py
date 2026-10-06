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
#  Chap. 11     #  Saisie utilisateur                                          #
#               #                                                              #
################################################################################
#
#  - La fonction input()
#  - Convertir la saisie
#  - Nettoyer la saisie
#  - Gestion d'erreurs de conversion
#  - Vérifier une saisie avant de la convertir
#  - Exemple complet : calcul de l'IMC
#
#######################################

"""
Ce chapitre est interactif : en lançant ce fichier, le programme s'arrêtera
plusieurs fois pour vous poser des questions. Tapez votre réponse dans la
console, puis appuyez sur Entrée.
"""


# La fonction input()
######################

"""
On utilise la fonction intégrée input() pour demander à l'utilisateur de
saisir une valeur, qui sera ensuite retournée par input().
Cette valeur sera TOUJOURS une chaîne de caractères.

Fonctionnement :
    1. input() affiche le texte passé en paramètre (on l'appelle l'"invite",
       ou "prompt" en anglais),
    2. puis le programme se met en PAUSE : il attend que l'utilisateur tape
       quelque chose et appuie sur Entrée,
    3. input() retourne alors le texte tapé (sans le saut de ligne final de la
       touche Entrée), et le programme reprend.
"""

# Ici la réponse de l'utilisateur sera stockée dans la variable gout
gout = input("> Tu aimes les framboises à la moutarde ? ")
print(type(gout))  # => <class 'str'>
print(f"Tu as répondu : {gout}")  # => Tu as répondu : … (votre réponse)

"""
Note : pensez à laisser un espace à la fin de l'invite, sinon la saisie de
l'utilisateur sera collée au point d'interrogation !

Si l'utilisateur appuie directement sur Entrée sans rien taper, input()
retourne la chaîne vide "" (cf. chap. 7).

L'invite est facultative : input() tout court attend une saisie sans rien
afficher. C'est rarement une bonne idée : l'utilisateur ne sait pas ce qu'on
attend de lui !
"""


# Convertir la saisie
######################

"""
IMPT : même si l'utilisateur tape un nombre, input() retourne une STRING. Si on
tape 3, on obtient le texte "3", et non le nombre 3. On ne peut donc pas
calculer directement avec :
"""
# Simulons une saisie de l'utilisateur ("3") pour montrer le problème :
saisie = "3"
print(saisie * 2)  # => 33 (on a dupliqué la chaîne, cf. chap. 7 !)

try:
    saisie + 1  # => TypeError: can only concatenate str (not "int") to str
except TypeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# Pour travailler avec des nombres, il faudra convertir cette valeur (cf.
# chap. 6). Si un entier est attendu, on utilisera int()
print(int(saisie) * 2)  # => 6

# On peut appeler int() directement sur le résultat de input() : Python
# exécute d'abord input(), puis convertit la chaîne obtenue
nombre_oreilles = int(input("> Combien d'oreilles as-tu ? "))
print(type(nombre_oreilles))  # => <class 'int'>
print(f"Avec une oreille de plus, tu en aurais {nombre_oreilles + 1}.")

"""
Cette ligne revient à écrire, en deux étapes :
    texte = input("> Combien d'oreilles as-tu ? ")
    nombre_oreilles = int(texte)
"""

# Il faudra utiliser float() si la réponse attendue est un décimal/réel
taille = float(input("> Combien mesures-tu (en m, par ex. 1.74) ? "))
print(type(taille))  # => <class 'float'>
print(f"Tu mesures {taille * 100:.0f} cm.")  # => Tu mesures … cm. (":.0f" :
#                                              sans décimale, cf. chap. 8)

"""
Note : la fonction raw_input() ne sert que pour Python2, elle n'est plus
utilisée en Python3. Vous la croiserez peut-être dans de vieux tutoriels.
"""


# Nettoyer la saisie
#####################

"""
Les utilisateurs ne tapent pas toujours exactement ce qu'on attend : espaces
en trop, majuscules… Les méthodes du chap. 8 permettent de "nettoyer" la
saisie avant de l'utiliser.
"""
# Simulons une saisie peu soignée :
reponse = "  OUI "

# .strip() enlève les espaces autour, .lower() met en minuscules
reponse_propre = reponse.strip().lower()
print(f"[{reponse_propre}]")  # => [oui]
print(reponse_propre == "oui")  # => True

# Sans nettoyage, la comparaison échouerait :
print(reponse == "oui")  # => False

"""
Note : on peut enchaîner les méthodes, comme dans reponse.strip().lower() : on
appelle .lower() sur le résultat de .strip(). Python les exécute de gauche à
droite.

On peut donc aussi les appliquer directement sur input() :
    reponse = input("> Continuer ? (oui/non) ").strip().lower()
"""


# Gestion d'erreurs de conversion
##################################

# Attention, tenter une conversion avec int() ou float() peut créer une erreur
# si la chaîne ne représente pas un nombre valide.

# Si l'utilisateur saisit un nombre décimal d'oreilles (par exemple "4.3"), on
# aura une erreur :
saisie = "4.3"
try:
    int(saisie)  # => ValueError: invalid literal for int() with base 10: '4.3'
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

# Un Français tapera souvent une virgule au lieu d'un point :
a = "3,25"
try:
    float(a)  # => ValueError: could not convert string to float: '3,25'
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

# Et bien sûr, du texte ne peut pas être converti en nombre :
b = "douze"
try:
    int(b)  # => ValueError: invalid literal for int() with base 10: 'douze'
except ValueError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Une ValueError arrête immédiatement le programme : c'est ce qui arrivera dans
la section précédente si vous répondez "deux" au nombre d'oreilles. Essayez !

Quelques parades simples :
    - pour les virgules, on peut les remplacer par des points avant de
      convertir (cf. .replace() au chap. 8),
    - pour les entiers, on peut tester la saisie avant de la convertir (voir
      la section suivante),
    - plus tard, on apprendra à intercepter proprement ces erreurs avec
      try: … except: … (cf. chap. 26), comme on le fait dans ce cours.
"""
print(float(a.replace(",", ".")))  # => 3.25


# Vérifier une saisie avant de la convertir
############################################

"""
La méthode .isdigit() (cf. chap. 8) retourne True si la chaîne ne contient QUE
des chiffres. C'est donc un bon moyen de savoir si int() va fonctionner sur une
saisie représentant un entier positif :
"""
print("42".isdigit())     # => True  : int("42") fonctionnera
print("4.3".isdigit())    # => False : int("4.3") échouerait
print("douze".isdigit())  # => False : int("douze") échouerait
print("".isdigit())       # => False : l'utilisateur n'a rien tapé

"""
Attention aux limites de .isdigit() :
    - un nombre négatif ("-4") donne False, car "-" n'est pas un chiffre,
    - des espaces autour (" 42 ") donnent False : pensez à .strip() d'abord !
"""
print("-4".isdigit())          # => False
print(" 42 ".strip().isdigit())  # => True

"""
Pour l'instant, on sait seulement OBTENIR ce booléen. Au chapitre suivant
(chap. 12), on verra comment s'en servir pour décider quoi faire : convertir
si la saisie est valide, ou afficher un message d'erreur sinon. Et au chap. 13,
on verra comment reposer la question tant que la saisie n'est pas valide.
"""
age_saisi = input("> Quel âge as-tu ? ").strip()
saisie_valide = age_saisi.isdigit()
print(f"Ta saisie est-elle un entier positif ? {saisie_valide}")


# Exemple complet : calcul de l'IMC
####################################

"""
Rassemblons tout ce que l'on a vu dans un petit programme : le calcul de
l'Indice de Masse Corporelle (IMC), qui vaut le poids (en kg) divisé par le
carré de la taille (en m).

Étapes :
    1. demander les valeurs à l'utilisateur (input),
    2. les nettoyer et les convertir (strip, replace, float),
    3. faire le calcul,
    4. afficher le résultat proprement (f-string avec 1 décimale, cf. chap. 8).
"""
poids = float(input("> Ton poids (en kg) ? ").strip().replace(",", "."))
taille = float(input("> Ta taille (en m) ? ").strip().replace(",", "."))

imc = poids / taille ** 2  # la puissance passe avant la division (chap. 5)
print(f"Ton IMC est de {imc:.1f}.")  # => Ton IMC est de … (ex. : 22.9 pour
#                                       70 kg et 1.75 m)

"""
Remarque : grâce au .replace(",", "."), l'utilisateur peut taper "1,75" ou
"1.75" : les deux fonctionneront.
"""
