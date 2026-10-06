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
#  Chap. 39     #  Pandas I : exercices                                        #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", essayez de prévoir le résultat
avant de lancer le programme.

Ces exercices nécessitent pandas (cf. chapitre, section "Installer et importer
pandas"). Le fichier exo_pandas_eleves.csv est créé juste en dessous
("Préparation"), et tous les fichiers créés sont supprimés tout à la fin
("Nettoyage").

Les corrigés sont dans le fichier corrs/corr_39_pandas_I.py.
"""

import os
import sys

try:
    import pandas as pd
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("pandas n'est pas installé : lancez \"pip install pandas\" (ou")
    print("\"conda install pandas\"), puis relancez ce programme.")
    sys.exit(0)


#################
#  Préparation  #
#################

# Ne modifiez pas ce bloc : il crée le fichier dont les exercices ont besoin.
# Remarquez les cases vides : certaines notes n'ont pas été saisies.
with open("exo_pandas_eleves.csv", "w", encoding="utf-8") as f:
    f.write("nom,classe,age,maths,physique,francais\n")
    f.write("Alice,A,16,15,12,17\n")
    f.write("Bob,B,17,8,,9\n")
    f.write("Chloé,A,16,12,14,10\n")
    f.write("David,B,18,6,9,11\n")
    f.write("Emma,A,17,18,16,\n")
    f.write("Farid,C,16,11,13,14\n")
    f.write("Gaëlle,C,17,,10,15\n")
    f.write("Hugo,B,16,14,15,12\n")


################
#  Les Series  #
################

"""
1. Créez une Series temperatures contenant les valeurs 18, 22, 25, 19 et 21,
   avec pour index "lun", "mar", "mer", "jeu" et "ven". Affichez :
       a) la température de mercredi,
       b) la moyenne, le maximum, et le jour le plus chaud,
       c) les températures converties en degrés Fahrenheit (F = C * 9 / 5 +
          32), sans boucle,
       d) la Series de booléens "température > 20", puis seulement les jours
          où il a fait plus de 20 degrés.

2. Sans exécuter, que vaut pd.Series([1, 2, 3]) * 2 ? Et [1, 2, 3] * 2 ?
   Pourquoi est-ce différent ?
"""


####################
#  Les DataFrames  #
####################

"""
3. Créez un DataFrame fruits de deux façons, et vérifiez avec .equals()
   qu'elles donnent le même résultat :
       a) à partir d'un dictionnaire de listes (une liste par colonne),
       b) à partir d'une liste de dictionnaires (un dictionnaire par ligne),
   avec les colonnes nom ("pomme", "kiwi", "banane"), prix (2.5, 4.0, 1.8) et
   stock (120, 35, 80).
"""


#########################
#  Lire un fichier CSV  #
#########################

"""
4. Chargez exo_pandas_eleves.csv dans un DataFrame df. Affichez :
       a) le DataFrame complet,
       b) ses dimensions (nombre de lignes et de colonnes),
       c) la liste de ses colonnes,
       d) le type de chaque colonne. Pourquoi la colonne maths est-elle de
          type float, alors que les notes du fichier sont des entiers ?
"""


###########################
#  Explorer un DataFrame  #
###########################

"""
5. Affichez les 3 premières lignes, puis les 2 dernières (cherchez la méthode
   "inverse" de .head()).

6. Affichez les statistiques (.describe()) des trois colonnes de notes. Que
   représente la ligne "count", et pourquoi n'est-elle pas égale à 8 partout ?
"""


###############################
#  Sélectionner des colonnes  #
###############################

"""
7. Affichez :
       a) la moyenne en maths,
       b) la liste des classes distinctes,
       c) le nombre d'élèves par classe.

8. Affichez un DataFrame avec seulement les colonnes nom et francais. Que se
   passe-t-il si on demande la colonne "anglais" ? (Protégez la ligne.)
"""


###########################################
#  Sélectionner des lignes : loc et iloc  #
###########################################

"""
9. Avec .iloc, affichez :
       a) la première ligne,
       b) les deux dernières lignes,
       c) les lignes 1 à 3 (incluses) et les colonnes 0 à 2 (incluses).

10. Créez df_nom, une copie de df indexée par la colonne nom. Avec .loc,
    affichez :
        a) la note de maths d'Emma,
        b) les notes de maths et de physique de "Bob" à "David" (le dernier
           est-il inclus ?).
"""


########################
#  Filtrer les lignes  #
########################

"""
11. Affichez le nom des élèves (sous forme de liste) :
        a) qui ont au moins 12 en maths,
        b) de la classe A qui ont plus de 12 en français,
        c) des classes B ou C (avec .isin()),
        d) qui ont 16 ans ou qui ont moins de 10 en maths.

12. Sans exécuter, pourquoi cette ligne provoque-t-elle une erreur ?
        df[df["age"] > 16 and df["maths"] > 10]
    Corrigez-la.
"""


##################################
#  Les valeurs manquantes : NaN  #
##################################

"""
13. a) Comptez les valeurs manquantes de chaque colonne.
    b) Affichez le nom des élèves qui n'ont pas de note de physique.
    c) Combien de lignes reste-t-il si on supprime toutes les lignes
       incomplètes ? Le DataFrame df a-t-il été modifié ?

14. Sans exécuter : la moyenne de la colonne maths est-elle calculée sur 8
    élèves ou sur 7 ? Vérifiez en la comparant avec la moyenne obtenue en
    remplaçant les NaN par 0. Laquelle des deux vous semble la plus juste ?
"""


######################################
#  Ajouter et modifier des colonnes  #
######################################

"""
15. Ajoutez à df une colonne moyenne, égale à la moyenne des trois notes :
        a) d'abord avec (maths + physique + francais) / 3. Que vaut la moyenne
           de Bob ? Pourquoi ?
        b) puis avec la méthode .mean(axis=1) appliquée aux trois colonnes de
           notes (axis=1 : on calcule la moyenne de chaque LIGNE, en ignorant
           les NaN). Arrondissez à 2 décimales.

16. Avec .apply() et une fonction mention(moyenne) (cf. chap. 29), ajoutez
    une colonne mention ("Très bien" si >= 16, "Bien" si >= 14, "Assez bien"
    si >= 12, "Passable" si >= 10, "Insuffisant" sinon).

17. Renommez la colonne francais en français, puis supprimez la colonne age.
    Affichez la liste des colonnes.
"""


###########
#  Trier  #
###########

"""
18. a) Affichez le nom et la moyenne des élèves, du meilleur au moins bon.
    b) Affichez les noms des 3 meilleurs élèves (de deux façons : avec
       .sort_values() puis .head(), et avec .nlargest()).
    c) Triez par classe (ordre alphabétique), puis par moyenne décroissante
       dans chaque classe.
"""


#########################
#  Regrouper : groupby  #
#########################

"""
19. Pour chaque classe, affichez :
        a) la moyenne générale (colonne moyenne), arrondie à 2 décimales,
        b) le nombre d'élèves,
        c) la note de maths minimale et maximale (avec .agg()).
    Quelle classe a la meilleure moyenne ?
"""


##########################
#  Exporter et nettoyer  #
##########################

"""
20. Enregistrez dans exo_pandas_classe_A.csv les élèves de la classe A,
    triés par moyenne décroissante, avec seulement les colonnes nom, moyenne
    et mention (sans l'index). Relisez le fichier avec pd.read_csv() pour
    vérifier.
"""


###############
#  Nettoyage  #
###############

for nom_fichier in ["exo_pandas_eleves.csv", "exo_pandas_classe_A.csv"]:
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)
