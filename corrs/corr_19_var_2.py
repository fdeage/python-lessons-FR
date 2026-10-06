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
#  Chap. 19     #  Variables II : corrigés                                     #
#               #                                                              #
################################################################################

##################################
#  Les 4 portées d'une variable  #
##################################

"""
1. Portées :
       TAUX        => Globale (définie hors de toute fonction)
       prix_ht     => Locale (paramètre de la fonction)
       montant_tva => Locale (affectée dans la fonction)
       round       => Built-in (fonction intégrée de Python)
"""


# 2. x est locale à f() : elle n'existe plus après l'appel.
def f():
    x = 10
    print(x)


f()  # => 10
try:
    print(x)
except NameError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# 3. f() lit la variable globale x AU MOMENT DE L'APPEL :
x = 1


def f():
    print(x)


f()  # => 1
x = 2
f()  # => 2


# 4. interieure() lit message dans la portée englobante, au moment de son
#    appel : message vaut alors "modifié".
def exterieure():
    message = "dehors"

    def interieure():
        print(message)

    message = "modifié"
    interieure()


exterieure()  # => modifié

# 5. Oui : une boucle ne crée pas de nouvelle portée. i est globale, et garde
#    sa dernière valeur.
for i in range(5):
    pass
print(i)  # => 4


##########################
#  Conflit de variables  #
##########################

# 6. Le x local masque le x global, sans le modifier :
x = "global"


def f():
    x = "local"
    print(x)


f()       # => local
print(x)  # => global

# 7. UnboundLocalError : comme compteur est affecté (=) dans la fonction, il
#    est local pour TOUTE la fonction. Au moment de lire compteur + 1, le
#    compteur local n'a pas encore de valeur.
compteur = 0


def incrementer():
    compteur = compteur + 1


try:
    incrementer()
except UnboundLocalError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


# Correction 1 : avec "global" (à éviter)
def incrementer_global():
    global compteur
    compteur = compteur + 1


incrementer_global()
print(compteur)  # => 1


# Correction 2 (recommandée) : paramètre et valeur de retour
def incrementer_proprement(valeur):
    return valeur + 1


compteur = incrementer_proprement(compteur)
print(compteur)  # => 2

# 8. On ne réaffecte pas la variable panier (pas de "=") : on modifie le
#    CONTENU de la liste. La liste globale est donc modifiée sans "global".
panier = []


def ajouter(article):
    panier.append(article)


ajouter("pain")
ajouter("lait")
print(panier)  # => ['pain', 'lait']

# 9. Ici, "panier = []" crée une nouvelle variable LOCALE : la liste globale
#    n'est pas touchée.
panier = ["pain"]


def vider():
    panier = []


vider()
print(panier)  # => ['pain']


# 10. liste désigne d'abord la MÊME liste que a : append(4) modifie donc a.
#     Ensuite, "liste = [0]" fait pointer liste vers une NOUVELLE liste : la
#     suite ne touche plus a.
def f(liste):
    liste.append(4)
    liste = [0]
    liste.append(5)
    return liste


a = [1, 2, 3]
b = f(a)
print(a)  # => [1, 2, 3, 4]
print(b)  # => [0, 5]


# 11. compteur() avec nonlocal :
def compteur_appels():
    nb_appels = 0

    def appeler():
        nonlocal nb_appels
        nb_appels += 1

    appeler()
    appeler()
    appeler()
    appeler()
    return nb_appels


print(compteur_appels())  # => 4


####################
#  Les namespaces  #
####################

# 12. Une variable globale dans globals() :
LANGAGE = "Python"
print("LANGAGE" in globals())  # => True
print(globals()["LANGAGE"])    # => Python


# 13. locals() dans une fonction :
def fonction_locale():
    ville = "Lyon"
    population = 520000
    print(locals())


fonction_locale()  # => {'ville': 'Lyon', 'population': 520000}

# 14. La variable list (globale) masque la fonction intégrée list() (built-in,
#     cherchée en dernier dans l'ordre LEGB) : list(range(5)) essaie
#     d'"appeler" une liste. On répare en supprimant la variable avec del.
list = [1, 2, 3]
try:
    nombres = list(range(5))
except TypeError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
del list
nombres = list(range(5))
print(nombres)  # => [0, 1, 2, 3, 4]


######################
#  Bonnes pratiques  #
######################

# 15. Sans variable globale :
def deposer(solde, montant):
    """Retourne le nouveau solde après un dépôt de montant."""
    return solde + montant


solde = 100
solde = deposer(solde, 50)
solde = deposer(solde, 20)
print(solde)  # => 170
"""
Avantages : la fonction ne dépend que de ses paramètres, on peut la tester
facilement (cf. chap. 29), et on voit clairement, à l'appel, quelle variable
est modifiée.
"""
