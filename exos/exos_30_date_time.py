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
#  Chap. 30     #  Date et heure : exercices                                   #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1).

Pour que vos résultats soient reproductibles, utilisez des dates FIXES (par ex.
date(2024, 3, 12)) plutôt que date.today(), sauf si l'énoncé dit le contraire.

Attention au conflit de noms vu dans le chapitre : si vous faites
"import time", le nom time ne désigne plus datetime.time. Importez par exemple
"from datetime import time as heure".

Les corrigés sont dans le fichier corr_30_date_time.py.
"""


###########
#  Dates  #
###########

"""
1. Créez la date du 14 juillet 1789. Affichez-la, puis affichez son année et
   le numéro du jour de la semaine (avec .weekday()). Quel jour de la semaine
   était-ce ?

2. Sans exécuter, que se passe-t-il avec date(2023, 2, 29) ? Et avec
   date(2024, 2, 29) ? Vérifiez (en protégeant la ligne qui pose problème).

3. Avec d = date(2024, 1, 5), affichez avec .strftime() :
       a) 05/01/2024
       b) 2024.01.05
       c) vendredi 05/01/2024 (le nom du jour en français, avec une liste)

4. À partir de d, créez (sans retaper l'année, le mois et le jour) la même
   date en 2030. d doit rester inchangée.
"""


############
#  Heures  #
############

"""
5. Créez l'heure 8 h 05 (8 heures, 5 minutes) et affichez-la :
       a) telle quelle,
       b) sous la forme 08h05,
       c) au format anglais 08:05 AM.

6. Sans exécuter, que se passe-t-il avec time(25, 0) ? Vérifiez.
"""


###################
#  Chronométrage  #
###################

"""
7. Avec time.perf_counter(), comparez la durée de ces deux calculs de la
   somme des entiers de 0 à 999 999 :
       a) avec une boucle for et un accumulateur (cf. chap. 13),
       b) avec sum(range(1_000_000)).
   Lequel est le plus rapide ? (Les durées varient d'une exécution à l'autre.)
"""


#####################
#  Dates et heures  #
#####################

"""
8. La cérémonie d'ouverture des JO de Paris a commencé le 26 juillet 2024 à
   19 h 30. Créez ce datetime, puis affichez :
       a) le datetime lui-même,
       b) 26/07/2024 à 19h30,
       c) la date seule, puis l'heure seule,
       d) son format ISO.
"""


##################################
#  Convertir une string en date  #
##################################

"""
9. Convertissez ces strings en datetime avec datetime.strptime(), et
   affichez le résultat :
       a) "14/07/1789"
       b) "2024-03-15 08:45"
       c) "15 mars 2024" (indice : le mois est en toutes lettres et en
          français… strptime() ne le comprend pas avec une locale anglaise.
          Que proposez-vous ?)

10. On a la liste dates = ["05/01/2024", "28/12/2023", "14/02/2024",
    "01/01/2024"]. Triez ces dates dans l'ordre chronologique et affichez-les
    au format jj/mm/aaaa. Pourquoi ne peut-on pas simplement trier les
    strings ?
"""


###########
#  Durée  #
###########

"""
11. Quelle date serons-nous 100 jours après le 1er janvier 2024 ? Et 100
    jours AVANT ?

12. Combien de jours se sont écoulés entre le 14 juillet 1789 et le 14
    juillet 1989 ?

13. Une personne est née le 12 mars 1989. Le 12 mars 2024 :
        a) depuis combien de jours est-elle née ?
        b) quel âge a-t-elle (en années) ? Pourquoi ne pas simplement diviser
           le nombre de jours par 365 ?

14. Un film commence à 20 h 45 et finit à 23 h 12 le même jour. Calculez sa
    durée (un timedelta), puis sa durée en minutes.

15. Sans exécuter, que se passe-t-il avec timedelta(months=1) ? Pourquoi ?
"""


########################
#  Comparer des dates  #
########################

"""
16. Avec la liste naissances = [date(1989, 3, 12), date(2001, 9, 9),
    date(1975, 12, 1), date(2010, 6, 30)] :
        a) affichez la date la plus ancienne et la plus récente,
        b) comptez les personnes nées avant l'an 2000.

17. Écrivez une fonction est_majeur(naissance, jour) qui retourne True si une
    personne née à la date naissance a au moins 18 ans à la date jour.
    Testez-la avec des assert (cf. chap. 29), en pensant au cas-limite du
    jour de l'anniversaire.
"""
