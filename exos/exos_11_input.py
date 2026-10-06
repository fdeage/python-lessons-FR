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
#  Chap. 11     #  Saisie utilisateur : exercices                              #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier : il vous
posera vos propres questions. Testez chaque programme avec plusieurs saisies,
y compris des saisies "pièges" (espaces, majuscules, virgules…).

Contrainte : les conditions (if) et les boucles ne sont vues qu'aux chap. 12
et 13. Tous ces exercices se font donc sans elles : le programme s'exécute de
haut en bas, une seule fois.

Astuce : pour tester un calcul sans retaper la réponse à chaque fois, vous
pouvez "simuler" une saisie en rangeant directement une chaîne dans la
variable (saisie = "12" au lieu de saisie = input(…)), comme dans le cours.

Les corrigés sont dans le fichier corrs/corr_11_input.py.
"""


#########################
#  La fonction input()  #
#########################

"""
1. Sans exécuter : si l'utilisateur tape 42 puis Entrée, quel est le type de
   la valeur retournée par input() ?

2. Écrivez un programme qui demande le prénom de l'utilisateur, puis affiche
   "Bonjour <prénom> !".

3. Écrivez un programme qui demande le nom d'une ville, puis affiche
   "<ville> s'écrit avec <nombre> lettres." (cf. len() au chap. 7).
"""


#########################
#  Convertir la saisie  #
#########################

"""
4. Sans exécuter : on pose saisie = "5". Que valent saisie * 3 et
   int(saisie) * 3 ?

5. Demandez deux nombres entiers à l'utilisateur, puis affichez leur somme.

6. Demandez le prix unitaire d'un article (un nombre décimal) et une quantité
   (un entier), puis affichez le prix total avec 2 décimales, par exemple :
   "Total : 37.50 €".

7. Demandez l'année de naissance de l'utilisateur, puis affichez l'âge qu'il
   aura (ou a eu) en 2026.
"""


########################
#  Nettoyer la saisie  #
########################

"""
8. On simule une saisie peu soignée : ville = "  lyon  ". Nettoyez-la pour
   obtenir "LYON".

9. Demandez à l'utilisateur s'il aime Python (oui/non). Rangez dans une
   variable aime_python le BOOLÉEN qui vaut True s'il a répondu "oui", même
   avec des majuscules ou des espaces ("  OUI ", "Oui"…). Affichez-le.

10. On simule la saisie d'une adresse email : "  Ada.Lovelace@Example.COM ".
    Mettez-la sous une forme "normalisée" : sans espaces autour, et en
    minuscules.
"""


#####################################
#  Gestion d'erreurs de conversion  #
#####################################

"""
11. Parmi ces conversions, lesquelles provoquent une erreur ? Vérifiez en
    protégeant chaque ligne avec try: … except ValueError as err: …, comme
    dans le cours.
        int("3.0")
        float("3,0")
        int(" 12 ")
        float("douze")
        int("-5")

12. Un utilisateur français a tapé "12,75" pour un prix. Convertissez cette
    saisie en float sans erreur.
"""


###############################################
#  Vérifier une saisie avant de la convertir  #
###############################################

"""
13. Sans exécuter : que valent ces expressions ?
        "123".isdigit()
        "12.3".isdigit()
        "-7".isdigit()
        " 7".isdigit()
        " 7".strip().isdigit()
        "".isdigit()

14. Demandez un nombre de places à réserver, puis affichez
    "Saisie valide : True" ou "Saisie valide : False" selon que la saisie
    représente un entier positif. Pensez aux espaces !
"""


###################################
#  Petits programmes interactifs  #
###################################

"""
15. Convertisseur de distances : demandez une distance en kilomètres
    (l'utilisateur peut taper une virgule ou un point), et affichez-la en
    miles avec 2 décimales (1 mile = 1.609344 km). Exemple :
    "42.195 km = 26.22 miles".

16. Demandez une durée en minutes (un entier), puis affichez-la en heures et
    minutes. Exemple : 135 donne "2 h 15 min".

17. Carte de visite : demandez le prénom puis le nom de l'utilisateur, et
    affichez-les sous la forme "Ada LOVELACE", quelle que soit la façon dont
    ils ont été tapés ("  ada ", "lovelace"…).

18. Demandez trois notes (des nombres décimaux), puis affichez leur moyenne
    avec 1 décimale : "Moyenne : 13.5".
"""
