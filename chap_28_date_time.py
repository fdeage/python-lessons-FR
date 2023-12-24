################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2023                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 28     #  Date et heure                                               #
#               #                                                              #
################################################################################
#
#  - Dates
#  - Heures
#  - Chronométrage
#  - Dates et heures
#  - Durée
#
##############################

"""
Python, comme la plupart des langages, a une bibliothèque (sous forme de
module) qui nous permet de travailler avec les dates et les heures (séparément
ou ensemble).
"""

# Dates
########

"""
Le module datetime contient toutes les fonctions nécessaires. Il propose
des fonctions sur les dates ("date"), les heures ("time"), et les dates et
heures ("datetime").

On travaillera d'abord avec datetime.date
"""
from datetime import date

# On obtient la date du jour avec date.today()
t = date.today()

# t est un type date…
print(type(t))  # => <class 'datetime.date'>

# …que l'on peut l'imprimer normalement avec print()
print(t)  # => 2020-11-05

# On peut affecter une date à une variable
d = date(1989, 3, 12)
print(d)  # => 1989-03-12

# d a des attributs que l'on peut imprimer un par un
print(d.day)    # => 12
print(d.month)  # => 03
print(d.year)   # => 1989

"""
On peut aussi mettre en forme cette date avec .strftime(), avec une mise
personnalisée
"""
print(d.strftime("%d-%m-%Y"))     # => 12-03-1989
print(d.strftime("%m;%d;%Y;%d"))  # => 03;12;1989;12

"""
Quelques options de .strftime() pour la date :
%y : année sur 2 chiffres
%Y : année sur 4 chiffres
%a : trois premières lettres du jour de la semaine (en anglais)
%A : jour de la semaine (en anglais)
%b : trois premières lettres du mois (en anglais)
%b : trois premières lettres du mois (en anglais)
%d : jour du mois (en chiffres)
%m : mois (en chiffres)
%B : mois (en anglais)
"""
d.strftime("%A %B %d, %Y")  # => 'Sunday March 12, 1989'


# Heures
#########

# On travaillera ici avec datetime.time
from datetime import time

# On peut affecter une heure à une variable
t = time(14, 11, 37)
print(t)  # => 02:11:37

# On peut imprimer les attributs de t un par un
print(t.hour)    # => 14
print(t.minute)  # => 11
print(t.second)  # => 37

"""
L'heure peut enregistrer une précision de l'ordre de la microseconde.
On notera qu'il s'agit de MICROsecondes et non de millisecondes : il y en a donc
un million par seconde.
"""
t2 = time(14, 11, 37, 358_144)
print(t2.microsecond)  # => 358144

# On peut aussi utiliser .strftime() pour mettre cette heure en forme
print(t.strftime("%I:%M %p"))  # => '02:11 PM'

"""
Quelques options de .strftime() pour l'heure :
%I : permet de convertir du format 24H au format 12H
%p : indique si l'heure est en AM ou PM
%H : heures sur 2 chiffres
%M : minutes (attention, %m est pour les mois)
%S : secondes
%f : microsecondes
"""
print(t2.strftime(" %H  %h  %I:%M %m %S %p %f"))
# => ' 14  Jan 02:11 01 37 PM 358144'


# Chronométrage
################

"""
Il est fréquent de vouloir chronométrer une tâche en Python : on peut utiliser
pour cela la fonction time() du module time.
"""
import time

def fonction_lente():
    # Cette fonction retourne la somme des nombres de 1 à… beaucoup
    return sum([i for i in range(10_000_000)])

avant = time.time()
_ = fonction_lente()
apres = time.time()
duree = apres - avant

print(f"Durée d'exécution : {round(duree, 3)}s")  # Durée d'exécution : 1.257s


# Dates et heures
##################

"""
On a besoin de datetime.datetime pour manipuler une combinaison de dates et
d'heures.
"""
from datetime import datetime

# On obtient l'heure courante avec datetime.now()
n = datetime.now()
print(n)  # => datetime.datetime(2020, 11, 5, 14, 7, 27, 444662)
