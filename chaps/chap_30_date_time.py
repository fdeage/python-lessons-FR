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
#  Chap. 30     #  Date et heure                                               #
#               #                                                              #
################################################################################
#
#  - Dates
#  - Heures
#  - Chronométrage
#  - Dates et heures
#  - Convertir une string en date
#  - Durée
#  - Comparer des dates
#
########################

"""
Python, comme la plupart des langages, a une bibliothèque (sous forme de
module, cf. chap. 22) qui nous permet de travailler avec les dates et les
heures (séparément ou ensemble).

Manipuler des dates "à la main" est un piège : années bissextiles, mois de 28
à 31 jours, changements d'heure… Utilisez toujours le module datetime plutôt
que de recoder ces calculs vous-même !

Note : plusieurs résultats de ce chapitre dépendent du moment où vous lancez
le programme (date du jour, heure courante, durée d'exécution). Ils sont
signalés "(variable)" dans les commentaires.
"""

# Dates
########

"""
Le module datetime contient toutes les fonctions nécessaires. Il propose
des types pour les dates ("date"), les heures ("time"), les dates et
heures ("datetime") et les durées ("timedelta").

On travaillera d'abord avec datetime.date
"""
from datetime import date

# On obtient la date du jour avec date.today()
t = date.today()

# t est un type date…
print(type(t))  # => <class 'datetime.date'>

# …que l'on peut imprimer normalement avec print()
print(t)  # => 2020-11-05 (variable : la date du jour)

"""
Note : la date est affichée au format international (norme ISO 8601) :
année-mois-jour. Ce format a l'avantage de pouvoir être trié dans l'ordre
alphabétique comme dans l'ordre chronologique.
"""

# On peut créer une date précise en donnant l'année, le mois et le jour, dans
# cet ordre, et l'affecter à une variable
d = date(1989, 3, 12)
print(d)  # => 1989-03-12

# d a des attributs que l'on peut imprimer un par un. Ce sont des ints :
print(d.day)    # => 12
print(d.month)  # => 3 (un int, donc pas de 0 devant)
print(d.year)   # => 1989

"""
On peut aussi connaître le jour de la semaine avec .weekday(), qui retourne un
int de 0 (lundi) à 6 (dimanche). Le 12 mars 1989 était un dimanche :
"""
print(d.weekday())  # => 6

# Une date invalide soulève une erreur ValueError (cf. chap. 26) :
try:
    date(2023, 2, 29)  # 2023 n'est pas bissextile : pas de 29 février !
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Une date ne peut pas être modifiée (comme un tuple, cf. chap. 17) : on ne peut
pas écrire d.day = 13. On crée plutôt une nouvelle date avec .replace() :
"""
d2 = d.replace(day=13)
print(d2)  # => 1989-03-13
print(d)   # => 1989-03-12 (d n'a pas changé)

"""
On peut aussi mettre en forme cette date avec .strftime() ("string format
time"), avec une mise en forme personnalisée. On lui passe une string
contenant des codes commençant par "%", qui seront remplacés par la valeur
correspondante ; le reste du texte est recopié tel quel.
"""
print(d.strftime("%d-%m-%Y"))     # => 12-03-1989
print(d.strftime("%m;%d;%Y;%d"))  # => 03;12;1989;12
print(d.strftime("%d/%m/%Y"))     # => 12/03/1989 (le format français)

"""
Quelques options de .strftime() pour la date :
%y : année sur 2 chiffres
%Y : année sur 4 chiffres
%a : trois premières lettres du jour de la semaine (en anglais)
%A : jour de la semaine (en anglais)
%b : trois premières lettres du mois (en anglais)
%B : mois (en anglais)
%d : jour du mois (en chiffres, sur 2 chiffres)
%m : mois (en chiffres, sur 2 chiffres)
%j : numéro du jour dans l'année (de 001 à 366)

La liste complète est dans la documentation :
https://docs.python.org/fr/3/library/datetime.html#strftime-and-strptime-format-codes
"""
print(d.strftime("%A %B %d, %Y"))  # => Sunday March 12, 1989
print(d.strftime("%a %b %y"))      # => Sun Mar 89
print(d.strftime("%j"))            # => 071 (le 71e jour de l'année)

"""
Remarque : les noms de jours et de mois sont en anglais par défaut. On peut
les obtenir en français en changeant la "locale" (avec le module locale), mais
cela dépend des langues installées sur votre système. Le plus simple et le plus
sûr reste souvent d'utiliser une liste :
"""
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi",
         "dimanche"]
print(f"Le {d.strftime('%d/%m/%Y')} était un {jours[d.weekday()]}.")
# => Le 12/03/1989 était un dimanche.

"""
Enfin, .isoformat() retourne la date sous forme de string au format ISO (le
même que celui de print()) :
"""
print(d.isoformat())        # => 1989-03-12
print(type(d.isoformat()))  # => <class 'str'>


# Heures
#########

# On travaillera ici avec datetime.time
from datetime import time

# On peut affecter une heure à une variable (heures, minutes, secondes)
t = time(14, 11, 37)
print(t)  # => 14:11:37 (l'heure est affichée au format 24 h)

# On peut imprimer les attributs de t un par un
print(t.hour)    # => 14
print(t.minute)  # => 11
print(t.second)  # => 37

# Les paramètres non précisés valent 0 :
print(time(9))  # => 09:00:00

"""
L'heure peut enregistrer une précision de l'ordre de la microseconde.
On notera qu'il s'agit de MICROsecondes et non de millisecondes : il y en a donc
un million par seconde.

(Rappel : le "_" dans 358_144 sert juste à rendre le nombre plus lisible,
cf. chap. 4. Il nécessite Python 3.6+.)
"""
t2 = time(14, 11, 37, 358_144)
print(t2.microsecond)  # => 358144
print(t2)              # => 14:11:37.358144

# On peut aussi utiliser .strftime() pour mettre cette heure en forme
print(t.strftime("%I:%M %p"))  # => 02:11 PM
print(t.strftime("%Hh%M"))     # => 14h11

"""
Quelques options de .strftime() pour l'heure :
%I : permet de convertir du format 24H au format 12H
%p : indique si l'heure est en AM ou PM
%H : heures sur 2 chiffres (format 24 h)
%M : minutes (attention, %m est pour les mois)
%S : secondes
%f : microsecondes
"""
print(t2.strftime("%H:%M:%S.%f"))  # => 14:11:37.358144

"""
Attention : un objet time ne contient AUCUNE information de date. Si on lui
demande un code de date comme %m (mois) ou %b, Python utilise une date par
défaut (le 1er janvier 1900), ce qui n'a pas de sens :
"""
print(t2.strftime("%H %m %b"))  # => 14 01 Jan

# Une heure invalide soulève aussi une ValueError :
try:
    time(25, 0)
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


# Chronométrage
################

"""
Il est fréquent de vouloir chronométrer une tâche en Python : on peut utiliser
pour cela la fonction time() du module time.

time.time() retourne le nombre de secondes écoulées depuis le 1er janvier 1970
à minuit (UTC), une date de référence appelée "epoch" ou "temps Unix". C'est un
float, très grand :
"""
import time

print(time.time())  # => 1700000000.123456 (variable)

"""
ATTENTION : en écrivant "import time", on vient de remplacer le nom "time" !
Juste au-dessus, avec "from datetime import time", time désignait le type
datetime.time ; désormais, time désigne le module time (cf. chap. 19 sur les
conflits de noms, et chap. 22 sur les imports).
"""
print(type(time))  # => <class 'module'>

"""
C'est une source de bugs classique : évitez de donner le même nom à deux
choses différentes. Ici, on aurait pu écrire "import datetime" puis
"datetime.time(…)", ce qui lève toute ambiguïté.

Pour chronométrer, on prend l'heure avant et après la tâche, puis on fait la
différence :
"""
def fonction_lente():
    # Cette fonction retourne la somme des nombres de 0 à… beaucoup
    return sum([i for i in range(10_000_000)])

avant = time.time()
_ = fonction_lente()
apres = time.time()
duree = apres - avant

print(f"Durée d'exécution : {round(duree, 3)}s")
# => Durée d'exécution : 1.257s (variable : dépend de votre ordinateur)

"""
Notes :
    - Pour mesurer précisément une durée, la documentation recommande plutôt
      time.perf_counter(), qui fonctionne de la même façon mais avec un
      chronomètre plus précis (sa valeur seule n'a pas de sens, seule la
      différence entre deux appels en a une).
    - Pour comparer la vitesse de petits bouts de code, le module timeit les
      exécute de nombreuses fois et donne un résultat plus fiable (cf. chap. 22).
"""
avant = time.perf_counter()
_ = sum([i for i in range(1_000_000)])
duree = time.perf_counter() - avant
print(f"Durée d'exécution : {duree:.4f}s")  # => Durée d'exécution : 0.0412s (variable)

"""
La fonction time.sleep(n) met le programme en pause pendant n secondes (n peut
être un float). C'est utile pour attendre entre deux actions :
"""
avant = time.perf_counter()
time.sleep(0.2)  # pause de 0,2 seconde
print(round(time.perf_counter() - avant, 1))  # => 0.2


# Dates et heures
##################

"""
On a besoin de datetime.datetime pour manipuler une combinaison de dates et
d'heures. (Oui : le module datetime contient un type qui s'appelle lui aussi
datetime…)
"""
from datetime import datetime

# On obtient la date et l'heure courantes avec datetime.now()
n = datetime.now()
print(n)  # => 2020-11-05 14:07:27.444662 (variable)

# Dans la console (sans print()), on verrait plutôt la représentation suivante :
# datetime.datetime(2020, 11, 5, 14, 7, 27, 444662)

# On peut créer une date et heure précise (année, mois, jour, heure, minute,
# seconde) :
dt = datetime(1989, 3, 12, 14, 11, 37)
print(dt)  # => 1989-03-12 14:11:37

# On retrouve tous les attributs de date et de time :
print(dt.year, dt.month, dt.day)       # => 1989 3 12
print(dt.hour, dt.minute, dt.second)   # => 14 11 37

# On peut séparer la date et l'heure…
print(dt.date())  # => 1989-03-12
print(dt.time())  # => 14:11:37

# … ou les combiner avec datetime.combine() :
print(datetime.combine(date(2000, 1, 1), dt.time()))  # => 2000-01-01 14:11:37

# Et bien sûr, mettre en forme avec .strftime() :
print(dt.strftime("%d/%m/%Y à %Hh%M"))  # => 12/03/1989 à 14h11
print(dt.isoformat())                  # => 1989-03-12T14:11:37

"""
HP : ces objets datetime sont dits "naïfs" : ils ne contiennent pas de fuseau
horaire. Pour des applications internationales, on utilisera des datetime
"conscients" de leur fuseau horaire (avec datetime.timezone, ou le module
zoneinfo à partir de Python 3.9).
"""


# Convertir une string en date
###############################

"""
Inversement, on a souvent des dates sous forme de texte (saisie utilisateur,
fichier CSV, cf. chap. 28…), que l'on veut convertir en vraie date pour pouvoir
faire des calculs.

On utilise datetime.strptime() ("string parse time") : on lui donne la string,
puis le format dans lequel elle est écrite, avec les mêmes codes "%" que
.strftime(). (Pour convertir toute une colonne avec pandas : pd.to_datetime(),
cf. chap. 48.)
"""
s = "25/12/2023 18:30"
noel = datetime.strptime(s, "%d/%m/%Y %H:%M")
print(noel)        # => 2023-12-25 18:30:00
print(type(noel))  # => <class 'datetime.datetime'>

"""
Moyen mnémotechnique :
    - strFtime : de la date vers la string (F comme "format")
    - strPtime : de la string vers la date (P comme "parse", analyser)

Si la string ne correspond pas au format, on obtient une ValueError :
"""
try:
    datetime.strptime("2023-12-25", "%d/%m/%Y")
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Pour les dates au format ISO (année-mois-jour), il existe un raccourci,
.fromisoformat() (Python 3.7+) :
"""
print(date.fromisoformat("2023-12-25"))  # => 2023-12-25


# Durée
########

"""
Une durée (un intervalle de temps) est représentée par le type
datetime.timedelta.

On peut créer une durée en précisant le nombre de jours (days), d'heures
(hours), de minutes (minutes), de secondes (seconds), de semaines (weeks)…
"""
from datetime import timedelta

une_semaine = timedelta(weeks=1)
print(une_semaine)  # => 7 days, 0:00:00

duree = timedelta(days=1, hours=2, minutes=30)
print(duree)  # => 1 day, 2:30:00

"""
IMPT : l'intérêt principal des durées est de faire des calculs avec les dates :
    - date + durée => date
    - date - durée => date
    - date - date  => durée
"""
# Quelle date serons-nous dans 100 jours après le 12 mars 1989 ?
print(d + timedelta(days=100))  # => 1989-06-20

# Python gère tout seul les fins de mois et les années bissextiles :
print(date(2024, 2, 28) + timedelta(days=1))  # => 2024-02-29
print(date(2023, 2, 28) + timedelta(days=1))  # => 2023-03-01

# Combien de jours entre deux dates ? On soustrait :
ecart = date(2023, 12, 25) - date(2023, 1, 1)
print(ecart)            # => 358 days, 0:00:00
print(type(ecart))      # => <class 'datetime.timedelta'>
print(ecart.days)       # => 358 (le nombre de jours, sous forme d'int)

# Avec des datetime, l'écart contient aussi les heures :
ecart = datetime(2023, 12, 25, 18, 30) - datetime(2023, 12, 24, 12, 0)
print(ecart)                  # => 1 day, 6:30:00
print(ecart.total_seconds())  # => 109800.0 (la durée totale en secondes)

"""
Attention : timedelta ne connaît pas les mois ni les années, car leur durée
varie (28 à 31 jours, 365 ou 366 jours). On ne peut donc pas écrire
timedelta(months=1) :
"""
try:
    timedelta(months=1)
except TypeError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

"""
Exemple : combien de jours avant le prochain Noël ? (le résultat dépend du
jour où vous lancez le programme)
"""
aujourdhui = date.today()
prochain_noel = date(aujourdhui.year, 12, 25)
if prochain_noel < aujourdhui:  # Noël est passé cette année…
    prochain_noel = date(aujourdhui.year + 1, 12, 25)
print(f"Noël est dans {(prochain_noel - aujourdhui).days} jours.")
# => Noël est dans 81 jours. (variable)


# Comparer des dates
#####################

"""
Les dates, heures et datetime se comparent avec les opérateurs habituels
(cf. chap. 9) : une date "plus petite" est une date plus ancienne.
"""
print(date(1989, 3, 12) < date(2000, 1, 1))   # => True
print(date(1989, 3, 12) == date(1989, 3, 12))  # => True

# Rappel : depuis "import time", le nom time désigne le module time (cf. section
# "Chronométrage"). Pour comparer des heures, on réimporte donc le type
# datetime.time, en lui donnant cette fois un alias (cf. chap. 22) pour éviter
# le conflit de noms :
from datetime import time as heure

print(heure(9, 30) > heure(14, 0))  # => False

"""
On peut donc trier une liste de dates avec sorted() (cf. chap. 24), ou trouver
la plus ancienne avec min() :
"""
dates = [date(2021, 5, 3), date(1999, 12, 31), date(2010, 7, 14)]
print(min(dates))  # => 1999-12-31
print([str(x) for x in sorted(dates)])
# => ['1999-12-31', '2010-07-14', '2021-05-03']

"""
Attention : on ne peut pas comparer une date avec un datetime (ou avec une
string !) : il faut d'abord convertir l'un des deux.
"""
try:
    print(date(2000, 1, 1) < datetime(2000, 1, 1, 12, 0))
except TypeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")

# On convertit le datetime en date avec .date() :
print(date(2000, 1, 1) < datetime(2000, 1, 2, 12, 0).date())  # => True
