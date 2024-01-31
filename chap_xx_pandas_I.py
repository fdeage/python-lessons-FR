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
#  Chap. 30     #  Pandas I                                                    #
#               #                                                              #
################################################################################
#
#  -
#
##############################

"""
NaN : "Not a Number". Quand une valeur n'a pas

pandas est le TCD (Tableau Croisé Dynamique) de la donnée
"""
import sys
site_packages = next(p for p in sys.path if 'site-packages' in p)
print(site_packages)


"""
Il peut être intéressant de créer un DataFrame basique avec des données
littérales. Cet objet pourra ensuite être manipulé à des fins de tests, ou pour
un PoC.

Il suffit d'utiliser la méthode .from_dict() :
"""
# import pandas as pd

# data = {'pokemon': ['Charmander', 'Squirtle', 'Bulbasaur'], 'type': ['Fire', 'Water', 'Grass']}
# pd.DataFrame.from_dict(data)

"""
This creates a two column DataFrame with a pokemon header and a type header. The two lists of value will be matched up positionally, so squirtle will be paired with water.
"""

