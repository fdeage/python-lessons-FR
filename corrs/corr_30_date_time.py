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
#  Chap. 30     #  Date et heure : corrigés                                    #
#               #                                                              #
################################################################################

from datetime import date, time, datetime, timedelta

###########
#  Dates  #
###########

# 1. Le 14 juillet 1789 :
prise_bastille = date(1789, 7, 14)
print(prise_bastille)            # => 1789-07-14
print(prise_bastille.year)       # => 1789
print(prise_bastille.weekday())  # => 1
"""
.weekday() compte à partir de 0 pour lundi : 1 correspond donc à un mardi.
"""

# 2. 2023 n'est pas bissextile : le 29 février 2023 n'existe pas.
try:
    date(2023, 2, 29)
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : day 29 must be in
#    range 1..28 for month 2 in year 2023)
# (Avant Python 3.14, le message était simplement "day is out of range for
# month".)
print(date(2024, 2, 29))  # => 2024-02-29 (2024 est bissextile : pas d'erreur)

# 3. Mises en forme :
d = date(2024, 1, 5)
print(d.strftime("%d/%m/%Y"))  # => 05/01/2024
print(d.strftime("%Y.%m.%d"))  # => 2024.01.05
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi",
         "dimanche"]
print(f"{jours[d.weekday()]} {d.strftime('%d/%m/%Y')}")
# => vendredi 05/01/2024
"""
.weekday() retourne un int de 0 à 6 : c'est exactement l'indice dont on a
besoin dans la liste jours (d'où l'ordre lundi → dimanche).
"""

# 4. .replace() crée une NOUVELLE date (une date ne se modifie pas) :
d_2030 = d.replace(year=2030)
print(d_2030)  # => 2030-01-05
print(d)       # => 2024-01-05 (inchangée)


############
#  Heures  #
############

# 5. 8 h 05 :
t = time(8, 5)
print(t)                       # => 08:05:00
print(t.strftime("%Hh%M"))     # => 08h05
print(t.strftime("%I:%M %p"))  # => 08:05 AM

# 6. Les heures vont de 0 à 23 :
try:
    time(25, 0)
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : hour must be in
#    0..23, not 25)  (sans ", not 25" avant Python 3.14)


###################
#  Chronométrage  #
###################

# 7. Attention : à partir d'ici, time désigne le MODULE time, et non plus
# datetime.time (cf. chapitre).
import time

avant = time.perf_counter()
total = 0
for i in range(1_000_000):
    total += i
duree_boucle = time.perf_counter() - avant

avant = time.perf_counter()
total2 = sum(range(1_000_000))
duree_sum = time.perf_counter() - avant

print(total == total2)  # => True (même résultat : 499999500000)
print(f"Boucle : {duree_boucle:.4f}s")  # => Boucle : 0.0350s (variable)
print(f"sum()  : {duree_sum:.4f}s")     # => sum()  : 0.0080s (variable)
"""
sum() est en général plusieurs fois plus rapide : la boucle est exécutée en C
à l'intérieur de l'interpréteur, au lieu d'exécuter une instruction Python
par tour de boucle. Les durées exactes dépendent de votre machine.
"""


#####################
#  Dates et heures  #
#####################

# 8. Les JO de Paris :
jo = datetime(2024, 7, 26, 19, 30)
print(jo)                                # => 2024-07-26 19:30:00
print(jo.strftime("%d/%m/%Y à %Hh%M"))   # => 26/07/2024 à 19h30
print(jo.date())                         # => 2024-07-26
print(jo.time())                         # => 19:30:00
print(jo.isoformat())                    # => 2024-07-26T19:30:00


##################################
#  Convertir une string en date  #
##################################

# 9. a) Sans heure, l'heure vaut minuit :
print(datetime.strptime("14/07/1789", "%d/%m/%Y"))  # => 1789-07-14 00:00:00
# Pour obtenir une date seule, on ajoute .date() :
print(datetime.strptime("14/07/1789", "%d/%m/%Y").date())  # => 1789-07-14

# 9. b)
print(datetime.strptime("2024-03-15 08:45", "%Y-%m-%d %H:%M"))
# => 2024-03-15 08:45:00

# 9. c) %B attend le nom ANGLAIS du mois ("March") : "mars" provoque une
# ValueError. Une solution simple : remplacer le mois par son numéro grâce à
# un dictionnaire (cf. chap. 18), puis utiliser %m.
try:
    datetime.strptime("15 mars 2024", "%d %B %Y")
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 3: (Sans ce try: … except …, cette ligne créerait : time data '15 mars
#    2024' does not match format '%d %B %Y')

mois = {"janvier": 1, "février": 2, "mars": 3, "avril": 4, "mai": 5,
        "juin": 6, "juillet": 7, "août": 8, "septembre": 9, "octobre": 10,
        "novembre": 11, "décembre": 12}
jour, nom_mois, annee = "15 mars 2024".split()
print(date(int(annee), mois[nom_mois], int(jour)))  # => 2024-03-15

# 10. Les strings "jj/mm/aaaa" se trient caractère par caractère : on
# comparerait d'abord les JOURS ("01" < "05" < "14" < "28"), quelle que soit
# l'année. Il faut donc convertir en dates avant de trier.
dates = ["05/01/2024", "28/12/2023", "14/02/2024", "01/01/2024"]
print(sorted(dates))
# => ['01/01/2024', '05/01/2024', '14/02/2024', '28/12/2023'] (FAUX !)
vraies_dates = [datetime.strptime(s, "%d/%m/%Y").date() for s in dates]
for d in sorted(vraies_dates):
    print(d.strftime("%d/%m/%Y"))
# => 28/12/2023
# => 01/01/2024
# => 05/01/2024
# => 14/02/2024
"""
Remarque : le format ISO "aaaa-mm-jj" n'a pas ce problème, il se trie dans
l'ordre chronologique même sous forme de string (cf. chapitre).
"""


###########
#  Durée  #
###########

# 11. On ajoute ou on retire un timedelta :
print(date(2024, 1, 1) + timedelta(days=100))  # => 2024-04-10
print(date(2024, 1, 1) - timedelta(days=100))  # => 2023-09-23

# 12. La soustraction de deux dates donne un timedelta :
ecart = date(1989, 7, 14) - date(1789, 7, 14)
print(ecart.days)  # => 73048

# 13. a) Nombre de jours :
naissance = date(1989, 3, 12)
jour = date(2024, 3, 12)
print((jour - naissance).days)  # => 12784


# 13. b) Âge en années : on soustrait les années, puis on retire 1 si
# l'anniversaire n'est pas encore passé cette année-là.
def age(naissance, jour):
    resultat = jour.year - naissance.year
    if (jour.month, jour.day) < (naissance.month, naissance.day):
        resultat -= 1
    return resultat


print(age(naissance, jour))  # => 35
"""
On compare des tuples (mois, jour) : la comparaison se fait élément par
élément (cf. chap. 17), ce qui est exactement ce qu'on veut ici.

Diviser par 365 ne marche pas toujours, à cause des années bissextiles. Par
exemple, pour une personne née le 1er mars 2000, la veille de ses 18 ans :
"""
veille = date(2018, 2, 28)
print((veille - date(2000, 3, 1)).days // 365)  # => 18 (FAUX)
print(age(date(2000, 3, 1), veille))            # => 17 (juste)

# 14. Durée d'un film : il faut des datetime (on ne peut pas soustraire deux
# datetime.time), donc on fixe une date quelconque.
debut = datetime(2024, 1, 1, 20, 45)
fin = datetime(2024, 1, 1, 23, 12)
duree = fin - debut
print(duree)                        # => 2:27:00
print(duree.total_seconds() / 60)   # => 147.0

# 15. Un mois n'a pas une durée fixe (28 à 31 jours) : timedelta ne connaît
# donc pas de paramètre months.
try:
    timedelta(months=1)
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 4: (Sans ce try: … except …, cette ligne créerait :
#    __new__() got an unexpected keyword argument 'months')
# (Le texte exact du message peut varier selon la version de Python.)


########################
#  Comparer des dates  #
########################

# 16. Les dates se comparent avec <, >, ==… donc min(), max() et sorted()
# fonctionnent directement :
naissances = [date(1989, 3, 12), date(2001, 9, 9), date(1975, 12, 1),
              date(2010, 6, 30)]
print(min(naissances))  # => 1975-12-01
print(max(naissances))  # => 2010-06-30
avant_2000 = [d for d in naissances if d < date(2000, 1, 1)]
print(len(avant_2000))  # => 2


# 17. On réutilise la fonction age() de l'exercice 13 :
def est_majeur(naissance, jour):
    return age(naissance, jour) >= 18


assert est_majeur(date(2000, 3, 1), date(2018, 3, 1)) is True    # le jour J
assert est_majeur(date(2000, 3, 1), date(2018, 2, 28)) is False  # la veille
assert est_majeur(date(1989, 3, 12), date(2024, 3, 12)) is True
assert est_majeur(date(2010, 6, 30), date(2024, 3, 12)) is False
print("Tous les tests de est_majeur() passent")
# => Tous les tests de est_majeur() passent
