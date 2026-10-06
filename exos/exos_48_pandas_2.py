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
#  Chap. 48     #  Pandas II : exercices                                       #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", essayez de prévoir le résultat
avant de lancer le programme.

Ces exercices nécessitent pandas (cf. chap. 39 et 48, section "Installer et
importer pandas"). Les données portent sur un service de vélos en libre-service
dans une grande ville :
    - le bloc "Préparation" ci-dessous crée deux petits tableaux PROPRES
      (stations et trajets), utilisés dans la plupart des exercices,
    - il crée aussi deux fichiers CSV "SALES" (exo48_trajets.csv et
      exo48_stations.csv), tels qu'exportés par le système : ils servent aux
      sections "Nettoyer des données" et "Cas pratique".
Tous les fichiers créés sont supprimés tout à la fin ("Nettoyage").

Les corrigés sont dans le fichier corrs/corr_48_pandas_2.py.
"""

import os
import sys

try:
    import pandas as pd
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("pandas n'est pas installé : lancez \"uv add pandas\" (ou")
    print("\"pip install pandas\"), puis relancez ce programme.")
    sys.exit(0)


#################
#  Préparation  #
#################

# Ne modifiez pas ce bloc : il crée les données dont les exercices ont besoin.

# Les stations : un identifiant, un nom, un quartier.
stations = pd.DataFrame({
    "station": ["S1", "S2", "S3"],
    "nom": ["Bellecour", "Part-Dieu", "Croix-Rousse"],
    "quartier": ["Presqu'île", "Part-Dieu", "Croix-Rousse"],
})

# Les trajets : une ligne par location de vélo (durée en minutes). Remarquez
# la station S9 du trajet 7, qui n'existe pas dans la table des stations.
trajets = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "date": ["2024-06-01", "2024-06-01", "2024-06-02", "2024-06-08",
             "2024-06-09", "2024-06-12", "2024-06-15", "2024-06-16",
             "2024-06-22", "2024-06-29"],
    "station": ["S1", "S2", "S1", "S2", "S3", "S2", "S9", "S3", "S1", "S1"],
    "duree": [12, 25, 8, 45, 22, 18, 30, 35, 15, 20],
    "abonne": [True, False, True, False, True, True, False, True, False,
               True],
})

# Les fichiers "sales", exportés par les bornes (séparateur ";", dates à la
# française, doublons, valeurs manquantes ou absurdes…).
with open("exo48_trajets.csv", "w", encoding="utf-8") as f:
    f.write("id;date;station;duree;abonne\n"
            "1;01/06/2024;S1;12;oui\n"
            "2;01/06/2024; s2 ;25;non\n"
            "3;02/06/2024;S1;8;Oui\n"
            "3;02/06/2024;S1;8;Oui\n"
            "4;05/06/2024;S3;;oui\n"
            "5;08/06/2024;S2;45;non\n"
            "6;09/06/2024;S1;-5;oui\n"
            "7;12/06/2024;S2;18;OUI\n"
            "8;15/06/2024;S9;30;non\n"
            "9;16/06/2024;S3;22;oui\n"
            "10;19/06/2024;S1;15;non\n"
            "11;22/06/2024;S2;9999;oui\n"
            "12;23/06/2024;S3;35;oui\n"
            "13;29/06/2024;S1;20;non\n"
            "14;30/06/2024;s2;14;oui\n")

with open("exo48_stations.csv", "w", encoding="utf-8") as f:
    f.write("station,nom,quartier\n"
            "S1,  BELLECOUR ,Presqu'île\n"
            "S2,part-dieu,Part-Dieu\n"
            "S3,Croix-Rousse ,Croix-Rousse\n")


########################################
#  L'index : set_index et reset_index  #
########################################

"""
1. a) Créez par_station, le tableau stations indexé par la colonne station.
      Avec .loc, affichez le nom de la station S2, puis le quartier de S3.
   b) Calculez la durée totale des trajets par station (groupby, cf.
      chap. 39). Quel est l'index du résultat ? Transformez-le en un tableau
      à deux colonnes "station" et "duree" avec .reset_index().
   c) Sans exécuter : que se passe-t-il si l'on écrit par_station.loc["S9"] ?
      Vérifiez (en protégeant la ligne avec try … except).
"""


#################################
#  Empiler des tables : concat  #
#################################

"""
2. Les trajets de juillet arrivent dans un nouveau tableau :

       juillet = pd.DataFrame({"id": [11, 12], "date": ["2024-07-01",
                               "2024-07-02"], "station": ["S3", "S1"],
                               "duree": [16, 27], "abonne": [True, False]})

   Empilez trajets et juillet dans un tableau ete de 12 lignes, avec un index
   propre (0 à 11). Vérifiez avec .shape.

3. Sans exécuter : on empile avec pd.concat(…, ignore_index=True) les deux
   tableaux suivants. Combien de lignes et de colonnes a le résultat ? Combien
   de cases valent NaN ?

       a = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
       b = pd.DataFrame({"y": [5], "z": [6]})
"""


################################
#  Joindre des tables : merge  #
################################

"""
4. a) Joignez trajets et stations sur la colonne station, avec une jointure
      interne (inner). Combien de lignes obtenez-vous ? Quel trajet a
      disparu, et pourquoi ?
   b) Même question avec une jointure à gauche (how="left"). Que contiennent
      les colonnes nom et quartier pour le trajet disparu en a) ?

5. Avec how="outer" et indicator=True, affichez :
       a) les trajets dont la station est inconnue,
       b) les stations qui n'ont AUCUN trajet (s'il y en a).

6. Le service enregistre aussi les réparations dans une table dont la colonne
   d'identifiant s'appelle "code" (et non "station") :

       reparations = pd.DataFrame({"code": ["S1", "S3", "S1"],
                                   "piece": ["frein", "pneu", "chaîne"]})

   Joignez reparations et stations pour afficher, pour chaque réparation, la
   pièce et le nom de la station. (Cherchez les paramètres left_on et
   right_on.) Supprimez la colonne de clé en double.
"""


##############################
#  Les pièges des jointures  #
##############################

"""
7. Sans exécuter : combien de lignes donne pd.merge(g, d, on="k") ?

       g = pd.DataFrame({"k": ["a", "a", "a", "b"], "x": [1, 2, 3, 4]})
       d = pd.DataFrame({"k": ["a", "a", "b", "c"], "y": [5, 6, 7, 8]})

   Vérifiez, puis expliquez le résultat.

8. a) Joignez trajets et stations en vérifiant que la relation est bien
      "plusieurs trajets → une station" (paramètre validate).
   b) Essayez la même jointure avec validate="one_to_one" : que se passe-t-il ?
      (Protégez la ligne, et n'affichez que la 1re ligne du message.)
   c) Les notes de satisfaction des stations ont été relevées en mai et en
      juin, dans deux tableaux qui ont tous deux une colonne "note" :

          mai = pd.DataFrame({"station": ["S1", "S2"], "note": [3.8, 4.1]})
          juin = pd.DataFrame({"station": ["S1", "S2"], "note": [4.0, 3.9]})

      Joignez-les pour obtenir les colonnes station, note_mai et note_juin,
      puis ajoutez une colonne progression (note_juin - note_mai).
"""


############################################
#  Remodeler : pivot, pivot_table et melt  #
############################################

"""
9. Voici le nombre de trajets par mois et par ville, au format LARGE :

       large = pd.DataFrame({"ville": ["Lyon", "Paris"],
                             "avril": [120, 340], "mai": [150, 410],
                             "juin": [180, 390]})

   a) Passez-le au format LONG, avec les colonnes ville, mois et trajets.
   b) À partir du format long, calculez le nombre total de trajets par mois.
   c) Revenez au format large avec .pivot(). Les colonnes sont-elles dans le
      même ordre qu'au départ ? Pourquoi ?

10. À partir du tableau joint de l'exercice 4 a), construisez avec
    .pivot_table() un tableau qui donne la durée MOYENNE des trajets, avec
    une ligne par quartier et une colonne par statut (abonne True/False).
    Ajoutez les moyennes générales avec margins=True.
"""


#########################################
#  Compter les combinaisons : crosstab  #
#########################################

"""
11. Avec pd.crosstab(), sur le tableau joint de l'exercice 4 a) :
       a) comptez les trajets par quartier et par statut (abonné ou non),
       b) affichez la PROPORTION d'abonnés dans chaque quartier (chaque ligne
          doit totaliser 1), arrondie à 2 chiffres.
"""


####################
#  groupby avancé  #
####################

"""
12. Pour chaque station (tableau trajets), calculez en une seule fois, avec des
    agrégations nommées : le nombre de trajets (nb), la durée totale
    (duree_totale) et la durée maximale (duree_max). Triez par durée totale
    décroissante.

13. Ajoutez au tableau trajets une colonne ecart : la différence entre la
    durée du trajet et la durée MOYENNE des trajets de sa station (utilisez
    .transform()). Quel trajet est le plus long par rapport aux habitudes de
    sa station ?

14. a) Ne gardez que les trajets des stations qui ont au moins 3 trajets
       (.filter()).
    b) Sans exécuter : quelle différence de taille y a-t-il entre
       trajets.groupby("station")["duree"].agg("mean") et
       trajets.groupby("station")["duree"].transform("mean") ?
"""


####################################
#  Les dates : to_datetime et .dt  #
####################################

"""
15. a) Convertissez la colonne date de trajets en vraies dates.
    b) Ajoutez une colonne jour contenant le nom du jour (en anglais) et une
       colonne week_end valant True pour le samedi et le dimanche (cherchez
       .dt.dayofweek).
    c) Combien de trajets ont eu lieu le week-end ? Quelle est leur durée
       moyenne, comparée à celle de la semaine ?
    d) Combien de jours séparent le premier et le dernier trajet ?

16. Sans exécuter : que donne le code suivant ? Vérifiez.

        saisies = pd.Series(["31/05/2024", "2024-06-01", "32/06/2024"])
        print(pd.to_datetime(saisies, format="%d/%m/%Y", errors="coerce"))
"""


#######################################################
#  Les séries temporelles : resample, rolling, shift  #
#######################################################

"""
17. On donne le nombre de locations par jour au mois de juin 2024 :

        jours = pd.date_range("2024-06-01", "2024-06-30", freq="D")
        locations = pd.Series([50 + (i * 13) % 40 for i in range(30)],
                              index=jours)

    a) Affichez le total des locations de la semaine du 10 au 16 juin
       (slice de dates).
    b) Calculez le total par semaine (resample), puis l'évolution d'une
       semaine sur l'autre, en pourcentage arrondi à 3 chiffres.
    c) Calculez la moyenne glissante sur 3 jours. Pourquoi les deux premières
       valeurs sont-elles NaN ?
"""


###################################
#  Les textes : l'accesseur .str  #
###################################

"""
18. a) Chargez exo48_stations.csv, puis nettoyez la colonne nom pour obtenir
       "Bellecour", "Part-Dieu" et "Croix-Rousse" (espaces, majuscules).
    b) On a les adresses des stations :

           adresses = pd.Series(["Place Bellecour, 69002 Lyon",
                                 "Rue de la Part-Dieu, 69003 Lyon",
                                 "Bd de la Croix-Rousse, 69004 Lyon"])

       Extrayez le code postal (5 chiffres) avec .str.extract() et une
       expression régulière (cf. chap. 42), puis l'arrondissement (les deux
       derniers chiffres, converti en entier).
    c) Quelles adresses contiennent le mot "Rue" ?
"""


##########################
#  Nettoyer des données  #
##########################

"""
19. Chargez exo48_trajets.csv (attention au séparateur !) et nettoyez-le
    étape par étape, en affichant le nombre de lignes après chaque étape :
       a) supprimez les doublons,
       b) uniformisez la colonne station (S1, S2, S3…, sans espaces),
       c) transformez la colonne abonne en booléens (True/False), quelle que
          soit la façon dont "oui" et "non" ont été écrits,
       d) supprimez les trajets sans durée,
       e) remplacez par NaN les durées impossibles (négatives, ou supérieures
          à 12 heures), puis supprimez ces lignes,
       f) convertissez les dates (format jour/mois/année) et la durée (en
          entier).
    Combien de lignes reste-t-il au final ?
"""


#####################################
#  Créer des classes : cut et qcut  #
#####################################

"""
20. Sur le tableau trajets :
       a) ajoutez une colonne categorie qui classe chaque trajet en "court"
          (jusqu'à 15 min incluses), "moyen" (jusqu'à 30 min incluses) ou
          "long" (au-delà), avec pd.cut(),
       b) comptez les trajets de chaque catégorie, dans l'ordre court, moyen,
          long,
       c) découpez les durées en 2 classes de même effectif avec pd.qcut().
          Quelle est la durée qui sépare les deux classes (la médiane) ?
"""


##############################
#  apply ou vectorisation ?  #
##############################

"""
21. Le tarif d'un trajet est de 1 € pour les abonnés, et de 1 € + 0,10 € par
    minute pour les autres. Un collègue a écrit :

        trajets["prix"] = trajets.apply(
            lambda l: 1.0 if l["abonne"] else 1.0 + 0.1 * l["duree"], axis=1)

    Réécrivez ce calcul SANS apply, de façon vectorisée (indice : un booléen
    vaut 0 ou 1, cf. chap. 21 ; ou cherchez la méthode .where()). Vérifiez
    que les deux colonnes sont égales avec .equals(). Arrondissez à 2
    chiffres.
"""


#############################################
#  Enchaîner les méthodes : assign et pipe  #
#############################################

"""
22. a) Écrivez une fonction nettoyer_stations(table) qui reçoit le tableau
       brut des stations (lu depuis exo48_stations.csv) et retourne un
       tableau nettoyé (noms propres, comme à l'exercice 18 a).
    b) En UNE SEULE chaîne de méthodes, entre parenthèses : lisez
       exo48_stations.csv, appliquez nettoyer_stations avec .pipe(), ajoutez
       une colonne longueur_nom avec .assign(), et ne gardez que les stations
       dont le nom fait plus de 9 caractères avec .query().
"""


#####################################
#  Lire et écrire d'autres formats  #
#####################################

"""
23. a) Écrivez le tableau trajets dans exo48_export.csv "à la française" :
       séparateur ";", virgule décimale, sans l'index. Ajoutez avant une
       colonne km = duree * 0.25 (vitesse moyenne de 15 km/h) pour avoir des
       nombres à virgule.
    b) Affichez les 3 premières lignes du fichier comme du texte (cf.
       chap. 28).
    c) Relisez-le avec pd.read_csv() et les bons paramètres, et vérifiez que
       la colonne km est bien de type float.
"""


##########################
#  Cas pratique : bilan  #
##########################

"""
24. Bilan du mois de juin, à partir des fichiers SALES :
       a) reprenez le nettoyage de l'exercice 19 (si possible en une chaîne
          de méthodes),
       b) joignez-le aux stations nettoyées (exercice 22), en écartant les
          stations inconnues (vérifiez lesquelles avec indicator=True),
       c) calculez, pour chaque quartier : le nombre de trajets, la durée
          moyenne et la part des trajets faits par des abonnés,
       d) construisez un tableau avec une ligne par quartier, une colonne par
          SEMAINE (numéro de semaine : .dt.isocalendar().week), et le nombre
          de trajets dans chaque case (0 s'il n'y en a pas).
"""


###############
#  Nettoyage  #
###############

for nom_fichier in ["exo48_trajets.csv", "exo48_stations.csv",
                    "exo48_export.csv"]:
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)
