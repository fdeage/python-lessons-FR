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
#  Chap. 33     #  Fonctions IV : exercices                                    #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour chaque fonction récursive, commencez TOUJOURS par vous
demander : quel est le cas de base ? comment se ramener à un problème plus
petit ? (cf. la méthode du chap. 33).

Les corrigés sont dans le fichier corr_33_fonctions_4.py.
"""


##############################################
#  Cas de base et appel récursif             #
##############################################

"""
1. Sans exécuter, qu'affiche ce programme ?
       def mystere(n):
           if n == 0:
               return
           mystere(n - 1)
           print(n)

       mystere(3)
   Comparez avec le compte_a_rebours() du cours : qu'est-ce qui change, et
   pourquoi ?

2. Sans exécuter, que renvoie f(5) ? Que calcule cette fonction ?
       def f(n):
           if n == 1:
               return 1
           return 2 * f(n - 1)

3. Cette fonction contient un bug. Lequel ? Pour quelles valeurs de n
   provoque-t-elle une RecursionError ? Corrigez-la.
       def somme_paires(n):
           # somme des entiers pairs de 0 à n (n pair)
           if n == 0:
               return 0
           return n + somme_paires(n - 2)

4. Écrivez une fonction récursive compter_jusqua(n) qui affiche les nombres
   de 1 à n DANS L'ORDRE croissant (indice : regardez l'exercice 1).
"""


##############################################
#  La pile d'appels                          #
##############################################

"""
5. Sans exécuter, écrivez la trace complète (descente et remontée) de
   l'appel puissance(2, 3) avec :
       def puissance(x, n):
           if n == 0:
               return 1
           return x * puissance(x, n - 1)
   Combien d'appels sont empilés au moment le plus profond ?

6. Ajoutez un paramètre profondeur à la factorielle (comme somme_tracee()
   dans le cours) pour afficher la trace de factorielle(4).
"""


##############################################
#  Factorielle et calculs                    #
##############################################

"""
7. Écrivez une fonction récursive somme_chiffres(n) qui renvoie la somme des
   chiffres d'un entier positif (indice : n % 10 donne le dernier chiffre,
   n // 10 enlève le dernier chiffre).
       somme_chiffres(2024) => 8

8. Écrivez une fonction récursive nb_chiffres(n) qui renvoie le nombre de
   chiffres d'un entier positif.
       nb_chiffres(7) => 1 ; nb_chiffres(12345) => 5

9. Écrivez une fonction récursive pgcd(a, b) en utilisant l'algorithme
   d'Euclide : pgcd(a, 0) = a, et sinon pgcd(a, b) = pgcd(b, a % b).
   Vérifiez avec math.gcd().
"""


##############################################
#  Listes et chaînes                         #
##############################################

"""
10. Écrivez une fonction récursive longueur(liste) qui renvoie le nombre
    d'éléments d'une liste, SANS utiliser len().
    (Indice : comparez la liste à [] pour le cas de base.)

11. Écrivez une fonction récursive compter(liste, valeur) qui renvoie le
    nombre d'occurrences de valeur dans la liste.

12. Écrivez une fonction récursive nb_voyelles(texte) qui compte les voyelles
    (aeiouy) d'une chaîne en minuscules.

13. Écrivez une fonction récursive est_triee(liste) qui renvoie True si la
    liste est triée par ordre croissant.

14. Écrivez une fonction récursive renverser(liste) qui renvoie une NOUVELLE
    liste avec les éléments dans l'ordre inverse.
"""


##############################################
#  Données imbriquées                        #
##############################################

"""
15. Écrivez une fonction compter_elements(donnees) qui renvoie le nombre de
    valeurs (non-listes) contenues dans une liste imbriquée.
        compter_elements([1, [2, 3], [[4], 5]]) => 5

16. Écrivez une fonction maximum_imbrique(donnees) qui renvoie le plus grand
    nombre d'une liste imbriquée (non vide).
        maximum_imbrique([3, [8, [1, 12]], 5]) => 12

17. Voici un organigramme : chaque personne est un dictionnaire avec un nom
    et la liste de ses subordonnés (eux-mêmes des dictionnaires).
        organigramme = {"nom": "Alice", "equipe": [
            {"nom": "Bob", "equipe": [
                {"nom": "Dan", "equipe": []},
                {"nom": "Eve", "equipe": []}]},
            {"nom": "Carl", "equipe": [
                {"nom": "Fay", "equipe": []}]}]}
    a) Écrivez effectif(personne) qui renvoie le nombre total de personnes
       (la personne elle-même comprise).
    b) Écrivez afficher(personne) qui affiche l'organigramme avec une
       indentation de 4 espaces par niveau.
    c) Écrivez chercher(personne, nom) qui renvoie True si quelqu'un porte ce
       nom dans l'organigramme.
"""


##############################################
#  Fibonacci et mémoïsation                  #
##############################################

"""
18. Combien d'appels à fib() fait le calcul de fib(4) avec la version naïve
    du cours ? Dessinez l'arbre des appels, puis vérifiez avec un compteur.

19. La suite de "Tribonacci" est comme Fibonacci, mais chaque terme est la
    somme des TROIS précédents : trib(0) = 0, trib(1) = 0, trib(2) = 1,
    trib(n) = trib(n-1) + trib(n-2) + trib(n-3).
    a) Écrivez-la de façon récursive naïve et affichez les 10 premiers
       termes.
    b) Écrivez une version mémoïsée avec un dictionnaire, et calculez
       trib(60).

20. (Problème) On monte un escalier de n marches, en faisant à chaque pas une
    OU deux marches. De combien de façons peut-on monter l'escalier ?
    (Pour 3 marches : 1+1+1, 1+2, 2+1 → 3 façons.)
    Écrivez une fonction récursive façons(n) (sans cédille dans le nom !),
    mémoïsée, et calculez-la pour n = 4, 10 et 50.
"""


##############################################
#  RecursionError, récursif ou itératif      #
##############################################

"""
21. Sans exécuter, lesquels de ces appels provoquent une RecursionError
    (avec la limite par défaut de 1000) ?
        a) factorielle(500)
        b) factorielle(5000)
        c) somme_jusqua(-3)       (version du cours, cas de base n == 0)
        d) fib_memo(900)          (avec un memo vide au départ)

22. Réécrivez somme_chiffres() (exercice 7) de façon itérative, avec une
    boucle while.

23. Pour chacun de ces problèmes, choisiriez-vous plutôt une boucle ou la
    récursivité ? Pourquoi ?
        a) calculer la moyenne d'une liste de 10 000 notes,
        b) lister tous les fichiers d'un dossier et de ses sous-dossiers,
        c) afficher les nombres de 1 à 1 000 000,
        d) calculer la profondeur maximale d'un fichier JSON.
"""
