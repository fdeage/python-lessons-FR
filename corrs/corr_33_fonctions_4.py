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
#  Chap. 33     #  Fonctions IV : corrigés                                     #
#               #                                                              #
################################################################################

import math

##############################################
#  Cas de base et appel récursif             #
##############################################

"""
1. Sans exécuter, qu'affiche ce programme ?
"""


def mystere(n):
    if n == 0:
        return
    mystere(n - 1)
    print(n)


mystere(3)
# => 1
#    2
#    3
"""
Ici, le print() est APRÈS l'appel récursif : il n'est exécuté qu'à la
REMONTÉE. mystere(3) appelle mystere(2), qui appelle mystere(1), qui appelle
mystere(0) (cas de base, ne fait rien). Puis, en remontant : mystere(1)
affiche 1, mystere(2) affiche 2, mystere(3) affiche 3.

Dans compte_a_rebours(), le print() était AVANT l'appel : il s'exécutait à
la descente, d'où l'ordre décroissant. La position du traitement par
rapport à l'appel récursif change tout !
"""


"""
2. Que renvoie f(5) ?
"""


def f(n):
    if n == 1:
        return 1
    return 2 * f(n - 1)


print(f(5))  # => 16
"""
f(5) = 2 * f(4) = 2 * 2 * f(3) = … = 2 * 2 * 2 * 2 * f(1) = 16.
La fonction calcule 2 puissance (n - 1).
"""


"""
3. Le bug : si n est IMPAIR, n diminue de 2 en 2 et "saute" par-dessus 0
   (5, 3, 1, -1, -3…) : le cas de base n'est jamais atteint. Même chose si
   n est négatif.
"""


def somme_paires_bug(n):
    if n == 0:
        return 0
    return n + somme_paires_bug(n - 2)


print(somme_paires_bug(6))  # => 12 (6 + 4 + 2 + 0 : n pair, ça marche)
try:
    somme_paires_bug(5)
except RecursionError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")


# Correction : un cas de base qui attrape tous les n <= 0
def somme_paires(n):
    if n <= 0:
        return 0
    if n % 2 == 1:                  # n impair : on part du pair en dessous
        return somme_paires(n - 1)
    return n + somme_paires(n - 2)


print(somme_paires(6))   # => 12
print(somme_paires(5))   # => 6 (4 + 2)
print(somme_paires(-3))  # => 0


"""
4. Afficher de 1 à n dans l'ordre croissant : on fait comme mystere(), en
   affichant APRÈS l'appel récursif.
"""


def compter_jusqua(n):
    if n == 0:
        return
    compter_jusqua(n - 1)
    print(n, end=" ")


compter_jusqua(5)  # => 1 2 3 4 5
print()            # retour à la ligne après les nombres


##############################################
#  La pile d'appels                          #
##############################################

"""
5. Trace de puissance(2, 3) :

    puissance(2, 3) → attend 2 * puissance(2, 2)
        puissance(2, 2) → attend 2 * puissance(2, 1)
            puissance(2, 1) → attend 2 * puissance(2, 0)
                puissance(2, 0) → cas de base : renvoie 1
            puissance(2, 1) renvoie 2 * 1 = 2
        puissance(2, 2) renvoie 2 * 2 = 4
    puissance(2, 3) renvoie 2 * 4 = 8

Au moment le plus profond, 4 appels de puissance() sont empilés (n = 3, 2,
1 et 0), au-dessus du programme principal.
"""


def puissance(x, n):
    if n == 0:
        return 1
    return x * puissance(x, n - 1)


print(puissance(2, 3))  # => 8


"""
6. La factorielle avec trace :
"""


def factorielle_tracee(n, profondeur=0):
    decalage = "    " * profondeur
    print(f"{decalage}factorielle({n})")
    if n <= 1:
        print(f"{decalage}cas de base : renvoie 1")
        return 1
    resultat = n * factorielle_tracee(n - 1, profondeur + 1)
    print(f"{decalage}renvoie {n} * factorielle({n - 1}) = {resultat}")
    return resultat


factorielle_tracee(4)
# => factorielle(4)
#        factorielle(3)
#            factorielle(2)
#                factorielle(1)
#                cas de base : renvoie 1
#            renvoie 2 * factorielle(1) = 2
#        renvoie 3 * factorielle(2) = 6
#    renvoie 4 * factorielle(3) = 24


##############################################
#  Factorielle et calculs                    #
##############################################

"""
7. Somme des chiffres :
    - cas de base : un nombre à un seul chiffre (n < 10) → c'est lui-même ;
    - sinon : dernier chiffre (n % 10) + somme des chiffres du reste (n // 10).
"""


def somme_chiffres(n):
    if n < 10:
        return n
    return n % 10 + somme_chiffres(n // 10)


print(somme_chiffres(2024))  # => 8
print(somme_chiffres(7))     # => 7
print(somme_chiffres(999))   # => 27


"""
8. Nombre de chiffres : même découpage, mais on compte 1 par chiffre.
"""


def nb_chiffres(n):
    if n < 10:
        return 1
    return 1 + nb_chiffres(n // 10)


print(nb_chiffres(7))      # => 1
print(nb_chiffres(12345))  # => 5


"""
9. L'algorithme d'Euclide (vieux de plus de 2000 ans !) :
"""


def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b, a % b)


print(pgcd(48, 18))                     # => 6
print(pgcd(17, 5))                      # => 1
print(pgcd(48, 18) == math.gcd(48, 18))  # => True
"""
Trace de pgcd(48, 18) : pgcd(18, 12) → pgcd(12, 6) → pgcd(6, 0) → 6.
Ici, on renvoie directement le résultat de l'appel récursif, sans calcul
à la remontée.
"""


##############################################
#  Listes et chaînes                         #
##############################################

"""
10. Longueur d'une liste sans len() :
"""


def longueur(liste):
    if liste == []:
        return 0
    return 1 + longueur(liste[1:])


print(longueur([4, 8, 15, 16, 23, 42]))  # => 6
print(longueur([]))                      # => 0


"""
11. Compter les occurrences d'une valeur :
"""


def compter(liste, valeur):
    if liste == []:
        return 0
    if liste[0] == valeur:
        return 1 + compter(liste[1:], valeur)
    return compter(liste[1:], valeur)


print(compter([1, 3, 1, 2, 1], 1))  # => 3
print(compter(["a", "b"], "z"))     # => 0


"""
12. Compter les voyelles d'une chaîne :
"""


def nb_voyelles(texte):
    if texte == "":
        return 0
    premiere = 1 if texte[0] in "aeiouy" else 0
    return premiere + nb_voyelles(texte[1:])


print(nb_voyelles("recursivite"))  # => 5
print(nb_voyelles("rythme"))       # => 2 (y et e)


"""
13. Une liste est triée si ses deux premiers éléments sont dans l'ordre ET
    si le reste est trié. Une liste de 0 ou 1 élément est toujours triée.
"""


def est_triee(liste):
    if len(liste) <= 1:
        return True
    if liste[0] > liste[1]:
        return False
    return est_triee(liste[1:])


print(est_triee([1, 2, 2, 5, 9]))  # => True
print(est_triee([1, 5, 3]))        # => False
print(est_triee([]))               # => True


"""
14. Renverser une liste : on renverse le reste, et on ajoute le premier
    élément À LA FIN.
"""


def renverser(liste):
    if liste == []:
        return []
    return renverser(liste[1:]) + [liste[0]]


print(renverser([1, 2, 3, 4]))  # => [4, 3, 2, 1]
"""
On écrit [liste[0]] (une liste d'un élément) car "+" concatène deux listes
(cf. chap. 16) : renverser(…) + liste[0] provoquerait une TypeError.
"""


##############################################
#  Données imbriquées                        #
##############################################

"""
15. Compter les valeurs d'une liste imbriquée :
"""


def compter_elements(donnees):
    total = 0
    for element in donnees:
        if isinstance(element, list):
            total += compter_elements(element)  # sous-liste : récursion
        else:
            total += 1                          # une valeur : on la compte
    return total


print(compter_elements([1, [2, 3], [[4], 5]]))  # => 5
print(compter_elements([[], [[]]]))             # => 0


"""
16. Maximum d'une liste imbriquée :
"""


def maximum_imbrique(donnees):
    meilleur = None
    for element in donnees:
        if isinstance(element, list):
            candidat = maximum_imbrique(element)
        else:
            candidat = element
        if candidat is not None and (meilleur is None or candidat > meilleur):
            meilleur = candidat
    return meilleur


print(maximum_imbrique([3, [8, [1, 12]], 5]))  # => 12
"""
On utilise None pour "pas encore de maximum" : cela gère aussi les
sous-listes vides (maximum_imbrique([]) renvoie None, que l'on ignore).
"""


"""
17. L'organigramme :
"""
organigramme = {"nom": "Alice", "equipe": [
    {"nom": "Bob", "equipe": [
        {"nom": "Dan", "equipe": []},
        {"nom": "Eve", "equipe": []}]},
    {"nom": "Carl", "equipe": [
        {"nom": "Fay", "equipe": []}]}]}


# a) Effectif : 1 (la personne) + l'effectif de chaque subordonné
def effectif(personne):
    total = 1
    for membre in personne["equipe"]:
        total += effectif(membre)
    return total


print(effectif(organigramme))                # => 6
print(effectif(organigramme["equipe"][0]))   # => 3 (Bob, Dan, Eve)


# b) Affichage indenté
def afficher(personne, niveau=0):
    print("    " * niveau + personne["nom"])
    for membre in personne["equipe"]:
        afficher(membre, niveau + 1)


afficher(organigramme)
# => Alice
#        Bob
#            Dan
#            Eve
#        Carl
#            Fay


# c) Recherche d'un nom
def chercher(personne, nom):
    if personne["nom"] == nom:
        return True
    for membre in personne["equipe"]:
        if chercher(membre, nom):
            return True           # trouvé dans une sous-équipe : on arrête
    return False


print(chercher(organigramme, "Fay"))   # => True
print(chercher(organigramme, "Zoé"))   # => False
"""
Ici, le cas de base est implicite : une personne sans équipe ne fait aucun
appel récursif (la boucle for ne tourne pas). C'est très fréquent avec les
structures en arbre.
"""


##############################################
#  Fibonacci et mémoïsation                  #
##############################################

"""
18. Arbre des appels de fib(4) :

                    fib(4)
            ┌─────────┴─────────┐
          fib(3)              fib(2)
       ┌────┴────┐          ┌───┴───┐
     fib(2)    fib(1)     fib(1)  fib(0)
    ┌──┴──┐
  fib(1) fib(0)

Soit 9 appels au total.
"""
nb_appels = 0


def fib(n):
    global nb_appels
    nb_appels += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


fib(4)
print(nb_appels)  # => 9


"""
19. Tribonacci :
"""


# a) Version naïve
def trib(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return trib(n - 1) + trib(n - 2) + trib(n - 3)


print([trib(i) for i in range(10)])  # => [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]

# b) Version mémoïsée
memo_trib = {0: 0, 1: 0, 2: 1}   # on peut ranger les cas de base dans le memo


def trib_memo(n):
    if n not in memo_trib:
        memo_trib[n] = trib_memo(n - 1) + trib_memo(n - 2) + trib_memo(n - 3)
    return memo_trib[n]


print(trib_memo(60))  # => 1383410902447554 (instantané)
"""
La version naïve fait TROIS appels par niveau : elle serait encore plus
lente que fib() naïf pour trib(60). Remarquez l'astuce : en mettant les cas
de base directement dans le dictionnaire, la fonction devient très courte.
"""


"""
20. L'escalier : pour monter n marches, le PREMIER pas fait 1 ou 2 marches.
    - si on fait 1 marche, il reste n - 1 marches : façons(n - 1) possibilités ;
    - si on fait 2 marches, il reste n - 2 marches : façons(n - 2).
    Donc façons(n) = façons(n - 1) + façons(n - 2)… c'est Fibonacci !
    Cas de base : façons(0) = 1 (on est arrivé : 1 façon, ne rien faire) et
    façons(1) = 1.
"""
memo_escalier = {}


def facons(n):
    if n <= 1:
        return 1
    if n not in memo_escalier:
        memo_escalier[n] = facons(n - 1) + facons(n - 2)
    return memo_escalier[n]


print(facons(3))   # => 3
print(facons(4))   # => 5
print(facons(10))  # => 89
print(facons(50))  # => 20365011074
"""
Sans mémoïsation, facons(50) demanderait des dizaines de milliards
d'appels. Avec, il en faut une centaine.
"""


##############################################
#  RecursionError, récursif ou itératif      #
##############################################

"""
21. Lesquels provoquent une RecursionError ?
    a) factorielle(500) : 500 appels imbriqués, sous la limite → OK.
    b) factorielle(5000) : 5000 appels imbriqués → RecursionError.
    c) somme_jusqua(-3) : n s'éloigne de 0 (-4, -5…) → RecursionError.
    d) fib_memo(900) : avec un memo vide, le 1er appel descend jusqu'à
       fib_memo(1) : environ 900 appels imbriqués, sous la limite → OK.
       Mais c'est juste ! fib_memo(1200) échouerait.
On le vérifie :
"""


def factorielle(n):
    if n <= 1:
        return 1
    return n * factorielle(n - 1)


def somme_jusqua(n):
    if n == 0:
        return 0
    return n + somme_jusqua(n - 1)


memo = {}


def fib_memo(n):
    if n in memo:
        return memo[n]
    resultat = n if n < 2 else fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = resultat
    return resultat


essais = {
    "a": lambda: factorielle(500),
    "b": lambda: factorielle(5000),
    "c": lambda: somme_jusqua(-3),
    "d": lambda: fib_memo(900),
}
for lettre, essai in essais.items():
    try:
        essai()
        print(lettre, "OK")
    except RecursionError:
        print(lettre, "RecursionError")
# => a OK
#    b RecursionError
#    c RecursionError
#    d OK
"""
(On range chaque appel dans une lambda, cf. chap. 32, pour ne l'exécuter
que dans le try.)
"""


"""
22. somme_chiffres() en itératif :
"""


def somme_chiffres_iteratif(n):
    total = 0
    while n > 0:
        total += n % 10   # on ajoute le dernier chiffre…
        n //= 10          # … et on l'enlève
    return total


print(somme_chiffres_iteratif(2024))  # => 8
print(somme_chiffres_iteratif(2024) == somme_chiffres(2024))  # => True


"""
23. Boucle ou récursivité ?
    a) Boucle (ou sum(notes) / len(notes)) : une liste "plate", une simple
       répétition. En récursif, 10 000 notes dépasseraient la limite !
    b) Récursivité : un dossier contient des sous-dossiers qui contiennent
       des sous-dossiers… sur une profondeur inconnue.
    c) Boucle : un million de niveaux de récursion est impossible en Python.
    d) Récursivité : un JSON est une structure imbriquée (dictionnaires et
       listes), exactement comme la fonction profondeur() du cours.
"""
