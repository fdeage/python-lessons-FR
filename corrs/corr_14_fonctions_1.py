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
#  Chap. 14     #  Fonctions I : corrigés                                      #
#               #                                                              #
################################################################################


##########################################
#  Définition et utilité d'une fonction  #
##########################################

"""
1. round(3.14159, 2) :
    - le nom de la fonction est round ;
    - ses arguments sont 3.14159 et 2 (les valeurs entre parenthèses) ;
    - elle retourne 3.14, la valeur arrondie à 2 décimales.
"""
print(round(3.14159, 2))  # => 3.14

"""
2. Trois avantages des fonctions (cf. chap. 14, « Pourquoi écrire des
   fonctions ? ») :
    - la concision : on écrit le code une seule fois, et on l'appelle autant
      de fois que nécessaire ;
    - une seule source de vérité : pour corriger un bug ou changer un
      calcul, on ne modifie qu'un endroit (avec du copier-coller, on risque
      d'en oublier un) ;
    - la lisibilité : un nom bien choisi (calculer_moyenne) explique ce que
      fait le code, sans avoir à le lire en détail.
"""


################################
#  Fonctions Python intégrées  #
################################

# 3. Expressions avec des fonctions intégrées :
print(abs(-7) + abs(7))                  # => 14
print(max(4, 12, 9) - min(4, 12, 9))     # => 8 (12 - 4)
print(round(2.71828, 1))                 # => 2.7
print(len("fonction"))                   # => 8
print(int("12") * 2)                     # => 24 (et non "1212")
print(type(len("abc")))                  # => <class 'int'>
"""
f) len() retourne un entier : type() s'applique à ce résultat (3), pas à
la chaîne "abc".
"""

# 4. Des appels imbriqués :
print(max(len("chat"), len("éléphant"), len("ours")))  # => 8
"""
Python évalue d'abord les arguments : max(4, 8, 4), qui vaut 8. Les appels
les plus "intérieurs" sont toujours calculés en premier.
"""


##########################################
#  Fonctions définies par l'utilisateur  #
##########################################


# 5. Définition et appels :
def dire_bonjour():
    print("Bonjour !")


print("Début")
dire_bonjour()
print("Fin")
dire_bonjour()
# => Début
# => Bonjour !
# => Fin
# => Bonjour !
"""
La définition (def) n'affiche rien : elle crée la fonction. Le code de la
fonction ne s'exécute qu'au moment de chaque APPEL, d'où « Bonjour ! » deux
fois, à l'endroit des appels.
"""


# 6. Une fonction sans paramètre :
def afficher_ligne():
    print("-" * 20)


afficher_ligne()  # => --------------------
afficher_ligne()  # => --------------------

# 7. Appeler une fonction avant de la définir :
try:
    fonction_pas_encore_la()
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


def fonction_pas_encore_la():
    print("trop tard !")


"""
Python lit le fichier de haut en bas : au moment de l'appel, la ligne "def"
n'a pas encore été exécutée, donc le nom fonction_pas_encore_la n'existe
pas encore (NameError). On définit TOUJOURS ses fonctions avant de les
appeler, en général en haut du fichier.
"""


################################
#  Où s'arrête une fonction ?  #
################################

# 8. L'indentation délimite la fonction :
def f():
    print("A")
    print("B")


print("C")
f()
# => C
# => A
# => B
"""
Seules les deux lignes INDENTÉES sous "def" font partie de la fonction.
print("C") est revenu à la marge : il est hors de la fonction, et s'exécute
en premier, avant l'appel f().
"""


#####################################
#  Pourquoi écrire des fonctions ?  #
#####################################

# 9. Factoriser une formule répétée :
def celsius_vers_fahrenheit(c):
    return c * 9 / 5 + 32


print(celsius_vers_fahrenheit(20))   # => 68.0
print(celsius_vers_fahrenheit(37))   # => 98.6
print(celsius_vers_fahrenheit(-10))  # => 14.0
"""
La formule n'est plus écrite qu'une fois : si elle était fausse, une seule
correction suffirait. Et le nom de la fonction dit ce que fait le calcul.
"""


################################
#  Fonctions avec paramètres   #
################################

# 10. Un paramètre :
def saluer(prenom):
    print("Bonjour, " + prenom + " !")


saluer("Ada")   # => Bonjour, Ada !
saluer("Alan")  # => Bonjour, Alan !


# 11. Deux paramètres et une boucle :
def afficher_rectangle(largeur, hauteur):
    for _ in range(hauteur):
        print("*" * largeur)


afficher_rectangle(4, 2)
# => ****
# => ****


# 12. L'ordre des arguments compte :
def presenter(nom, age):
    print(nom, "a", age, "ans")


presenter("Léa", 12)  # => Léa a 12 ans
presenter(30, "Tom")  # => 30 a Tom ans
"""
Les arguments sont associés aux paramètres DANS L'ORDRE : dans le 2e appel,
nom reçoit 30 et age reçoit "Tom". Python ne vérifie pas le sens : c'est au
programmeur de respecter le prototype. (On verra au chap. 15 les arguments
nommés, qui évitent ce piège : presenter(age=30, nom="Tom").)
"""


###########################
#  Le mot-clé "return"    #
###########################

# 13. Retourner une valeur :
def carre(x):
    return x * x


print(carre(3) + carre(4))  # => 25
"""
Chaque appel est remplacé par la valeur retournée : 9 + 16 = 25. C'est
possible uniquement parce que carre() RETOURNE son résultat (au lieu de
l'afficher).
"""


# 14. return ou print() ?
def double(x):
    return 2 * x


def double_affiche(x):
    print(2 * x)


a = double(5)
b = double_affiche(5)  # => 10 (affiché par le print de la fonction)
print(a)  # => 10
print(b)  # => None
"""
double_affiche() AFFICHE 10 mais ne retourne rien : une fonction sans
"return" retourne la valeur spéciale None (cf. chap. 15). b ne contient
donc pas 10. IMPT : afficher n'est pas retourner !
"""


# 15. Une fonction qui retourne un booléen :
def est_pair(n):
    return n % 2 == 0


for i in range(1, 11):
    if est_pair(i):
        print(i, end=" ")
print()  # => 2 4 6 8 10
"""
n % 2 == 0 est déjà un booléen : inutile d'écrire
    if n % 2 == 0:
        return True
    else:
        return False
"""


# 16. Deux return :
def valeur_absolue(x):
    if x < 0:
        return -x
    return x


print(valeur_absolue(-3))  # => 3
print(valeur_absolue(5))   # => 5
print(valeur_absolue(0))   # => 0
"""
Pas besoin de "else" : si x < 0, le premier return a déjà quitté la
fonction, et la dernière ligne n'est jamais atteinte.
"""


# 17. return interrompt la fonction (et la boucle) :
def premier_negatif():
    for n in range(5, -5, -1):
        if n < 0:
            return n
    print("fin")


print(premier_negatif())  # => -1
"""
n vaut 5, 4, 3, 2, 1, 0, puis -1 : la condition est vraie, et "return -1"
quitte IMMÉDIATEMENT la fonction, au milieu de la boucle. Le print("fin")
n'est jamais atteint (il ne le serait que si aucun nombre n'était négatif).
"""


# 18. Compter une lettre :
def compter_lettre(texte, lettre):
    compteur = 0
    for c in texte:
        if c == lettre:
            compteur = compteur + 1
    return compteur


print(compter_lettre("abracadabra", "a"))  # => 5
print(compter_lettre("abracadabra", "z"))  # => 0
print(compter_lettre("", "a"))             # => 0 (cas limite : chaîne vide)


# 19. Factorielle :
def factorielle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat = resultat * i
    return resultat


print(factorielle(5))  # => 120
print(factorielle(1))  # => 1
print(factorielle(0))  # => 1
"""
Par convention mathématique, 0! vaut 1 (le produit de "rien du tout" vaut
1, comme une somme de rien vaut 0). Notre fonction le gère sans cas
particulier : range(1, 1) est vide, et resultat reste à 1.
"""


################################
#  Prototype d'une fonction    #
################################

# 20. Prototype, docstring, puis corps :
def prix_ttc(prix_ht, taux_tva):
    """Retourne le prix TTC à partir d'un prix HT et d'un taux (0.2 = 20 %)."""
    return prix_ht * (1 + taux_tva)


print(prix_ttc(100, 0.2))  # => 120.0
print(prix_ttc.__doc__)
# => Retourne le prix TTC à partir d'un prix HT et d'un taux (0.2 = 20 %).
"""
Le prototype (nom et paramètres), documenté par la docstring, est le
"contrat" de la fonction : il suffit à quelqu'un pour l'utiliser, sans lire
son corps.
"""


# 21. Avec des annotations de type :
def prix_ttc_annote(prix_ht: float, taux_tva: float) -> float:
    """Retourne le prix TTC à partir d'un prix HT et d'un taux (0.2 = 20 %)."""
    return prix_ht * (1 + taux_tva)


print(prix_ttc_annote(50.0, 0.1))  # => 55.00000000000001
print(prix_ttc_annote(50, 1))      # => 100 (des int : aucune erreur)
"""
Les annotations ne sont PAS vérifiées par Python à l'exécution : elles
documentent le contrat et aident l'éditeur à repérer les erreurs, mais
n'empêchent rien (on le verra en détail au chap. 46). Le petit écart de
55.00000000000001 vient des arrondis des floats (cf. chap. 4).
"""
