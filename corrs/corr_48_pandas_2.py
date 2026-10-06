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
#  Chap. 48     #  Pandas II : corrigés                                        #
#               #                                                              #
################################################################################

"""
Les affichages ci-dessous ont été vérifiés avec pandas 3.0.6. Avec une autre
version, la présentation peut légèrement varier (types "str" affichés
"object" et dates en "[ns]" avec pandas 2.x, cf. chapitre).
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

stations = pd.DataFrame({
    "station": ["S1", "S2", "S3"],
    "nom": ["Bellecour", "Part-Dieu", "Croix-Rousse"],
    "quartier": ["Presqu'île", "Part-Dieu", "Croix-Rousse"],
})

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
"""
par_station = stations.set_index("station")
print(par_station)
# =>                   nom      quartier
#    station
#    S1          Bellecour    Presqu'île
#    S2          Part-Dieu     Part-Dieu
#    S3       Croix-Rousse  Croix-Rousse
print(par_station.loc["S2", "nom"])       # => Part-Dieu
print(par_station.loc["S3", "quartier"])  # => Croix-Rousse
"""
Une fois "station" en index, .loc[ligne, colonne] fonctionne comme une
recherche dans un dictionnaire (cf. chap. 18) : plus besoin de filtre.
"""

"""
   b) Calculez la durée totale des trajets par station. Quel est l'index du
      résultat ? Transformez-le en un tableau à deux colonnes "station" et
      "duree" avec .reset_index().
"""
total = trajets.groupby("station")["duree"].sum()
print(total)
# => station
#    S1    55
#    S2    88
#    S3    57
#    S9    30
#    Name: duree, dtype: int64
print(total.reset_index())
# =>   station  duree
#    0      S1     55
#    1      S2     88
#    2      S3     57
#    3      S9     30
"""
Le résultat du groupby est une Series dont l'INDEX est la colonne de
regroupement (station). .reset_index() la retransforme en colonne, et le nom
de la Series (duree) devient le nom de la seconde colonne.
"""

"""
   c) Sans exécuter : que se passe-t-il si l'on écrit par_station.loc["S9"] ?
"""
try:
    par_station.loc["S9"]
except KeyError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err!r})")
# => 2: (Sans ce try: … except …, cette ligne créerait : KeyError('S9'))
"""
Comme pour une clé absente d'un dictionnaire (cf. chap. 18), .loc lève une
KeyError si l'étiquette n'existe pas dans l'index.
"""


#################################
#  Empiler des tables : concat  #
#################################

"""
2. Empilez trajets et juillet dans un tableau ete de 12 lignes, avec un index
   propre (0 à 11).
"""
juillet = pd.DataFrame({"id": [11, 12], "date": ["2024-07-01", "2024-07-02"],
                        "station": ["S3", "S1"], "duree": [16, 27],
                        "abonne": [True, False]})
ete = pd.concat([trajets, juillet], ignore_index=True)
print(ete.shape)  # => (12, 5)
print(ete.tail(3))
# =>     id        date station  duree  abonne
#    9   10  2024-06-29      S1     20    True
#    10  11  2024-07-01      S3     16    True
#    11  12  2024-07-02      S1     27   False
"""
Sans ignore_index=True, les deux dernières lignes auraient les index 0 et 1
(ceux du tableau juillet) : l'index aurait des doublons.
"""

"""
3. Sans exécuter : combien de lignes et de colonnes, et combien de NaN ?
"""
a = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
b = pd.DataFrame({"y": [5], "z": [6]})
empile = pd.concat([a, b], ignore_index=True)
print(empile)
# =>      x  y    z
#    0  1.0  3  NaN
#    1  2.0  4  NaN
#    2  NaN  5  6.0
print(empile.shape)  # => (3, 3)
print(empile.isna().sum().sum())  # => 3
"""
3 lignes (2 + 1) et 3 colonnes (x, y, z : l'union des noms de colonnes).
Il y a 3 NaN : la case x de la ligne venue de b, et les deux cases z des
lignes venues de a. Remarquez que x et z sont passées en float, à cause des
NaN (cf. chap. 39).

(Pour .sum().sum() : le premier .sum() compte les NaN de chaque colonne, le
second additionne ces comptes.)
"""


################################
#  Joindre des tables : merge  #
################################

"""
4. a) Joignez trajets et stations avec une jointure interne. Combien de
      lignes ? Quel trajet a disparu ?
"""
joint = pd.merge(trajets, stations, on="station")
print(len(joint))  # => 9
print(joint[["id", "station", "nom", "duree"]])
# =>    id station           nom  duree
#    0   1      S1     Bellecour     12
#    1   2      S2     Part-Dieu     25
#    2   3      S1     Bellecour      8
#    3   4      S2     Part-Dieu     45
#    4   5      S3  Croix-Rousse     22
#    5   6      S2     Part-Dieu     18
#    6   8      S3  Croix-Rousse     35
#    7   9      S1     Bellecour     15
#    8  10      S1     Bellecour     20
"""
Le trajet 7 (station S9) a disparu : S9 n'existe pas dans stations, et une
jointure "inner" ne garde que les lignes qui ont une correspondance des deux
côtés.

Remarquez aussi que l'ORDRE des lignes a changé : pandas regroupe les lignes
par clé (S1, puis S2…). Si l'ordre compte, triez ensuite avec .sort_values().
"""

"""
   b) Même question avec une jointure à gauche.
"""
joint_gauche = pd.merge(trajets, stations, on="station", how="left")
print(len(joint_gauche))  # => 10
print(joint_gauche[joint_gauche["id"] == 7])
# =>    id        date station  duree  abonne  nom quartier
#    6   7  2024-06-15      S9     30   False  NaN      NaN
"""
Avec how="left", on garde TOUS les trajets : le trajet 7 est là, avec NaN
dans les colonnes venues de stations (nom et quartier).
"""

"""
5. Avec how="outer" et indicator=True, affichez :
       a) les trajets dont la station est inconnue,
       b) les stations qui n'ont AUCUN trajet.
"""
complet = pd.merge(trajets, stations, on="station", how="outer",
                   indicator=True)
print(complet["_merge"].value_counts())
# => _merge
#    both          9
#    left_only     1
#    right_only    0
#    Name: count, dtype: int64
print(complet[complet["_merge"] == "left_only"][["id", "station"]])
# =>    id station
#    9   7      S9
print(len(complet[complet["_merge"] == "right_only"]))  # => 0
"""
a) Seul le trajet 7 (S9) n'a pas de station correspondante ("left_only").
b) Aucune station n'est "right_only" : les trois stations ont au moins un
   trajet. On peut le vérifier aussi avec les ensembles (cf. chap. 25) :
"""
print(set(stations["station"]) - set(trajets["station"]))  # => set()

"""
6. Joignez reparations et stations (left_on / right_on), puis supprimez la
   colonne de clé en double.
"""
reparations = pd.DataFrame({"code": ["S1", "S3", "S1"],
                            "piece": ["frein", "pneu", "chaîne"]})
avec_noms = pd.merge(reparations, stations, left_on="code",
                     right_on="station").drop(columns="station")
print(avec_noms[["code", "piece", "nom"]])
# =>   code   piece           nom
#    0   S1   frein     Bellecour
#    1   S3    pneu  Croix-Rousse
#    2   S1  chaîne     Bellecour
"""
left_on donne le nom de la clé dans la table de gauche, right_on dans celle de
droite. Les deux colonnes sont conservées (code et station, qui contiennent
les mêmes valeurs) : on en supprime une avec .drop().
"""


##############################
#  Les pièges des jointures  #
##############################

"""
7. Sans exécuter : combien de lignes donne pd.merge(g, d, on="k") ?
"""
g = pd.DataFrame({"k": ["a", "a", "a", "b"], "x": [1, 2, 3, 4]})
d = pd.DataFrame({"k": ["a", "a", "b", "c"], "y": [5, 6, 7, 8]})
print(len(pd.merge(g, d, on="k")))  # => 7
"""
7 lignes :
    - la clé "a" apparaît 3 fois à gauche et 2 fois à droite : chaque ligne
      de gauche est associée à chaque ligne de droite, soit 3 × 2 = 6 lignes,
    - la clé "b" apparaît une fois de chaque côté : 1 × 1 = 1 ligne,
    - la clé "c" n'est qu'à droite : elle disparaît (jointure inner).
On a donc 7 lignes, alors que les tables n'en avaient que 4 chacune !
"""

"""
8. a) Joignez trajets et stations en vérifiant la relation "plusieurs trajets
      → une station".
"""
verifie = pd.merge(trajets, stations, on="station", validate="many_to_one")
print(len(verifie))  # => 9 (pas d'erreur : chaque station est unique)

"""
   b) Essayez la même jointure avec validate="one_to_one".
"""
try:
    pd.merge(trajets, stations, on="station", validate="one_to_one")
except pd.errors.MergeError as err:
    message = str(err).splitlines()[0]
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {message})")
# => 3: (Sans ce try: … except …, cette ligne créerait : Merge keys are not
#    unique in left dataset; not a one-to-one merge)
"""
La relation n'est pas "un pour un" : plusieurs trajets partent de la même
station (S1 apparaît 4 fois dans trajets). pandas le détecte et refuse la
jointure : c'est exactement le rôle de validate=.
"""

"""
   c) Joignez mai et juin pour obtenir station, note_mai et note_juin, puis
      ajoutez une colonne progression.
"""
mai = pd.DataFrame({"station": ["S1", "S2"], "note": [3.8, 4.1]})
juin = pd.DataFrame({"station": ["S1", "S2"], "note": [4.0, 3.9]})
notes = pd.merge(mai, juin, on="station", suffixes=("_mai", "_juin"))
notes["progression"] = (notes["note_juin"] - notes["note_mai"]).round(1)
print(notes)
# =>   station  note_mai  note_juin  progression
#    0      S1       3.8        4.0          0.2
#    1      S2       4.1        3.9         -0.2
"""
Sans suffixes=…, les colonnes s'appelleraient note_x et note_y. Le .round(1)
évite des résultats comme 0.20000000000000018 (cf. chap. 4 sur les floats).
"""


############################################
#  Remodeler : pivot, pivot_table et melt  #
############################################

"""
9. a) Passez le tableau large au format long (ville, mois, trajets).
"""
large = pd.DataFrame({"ville": ["Lyon", "Paris"],
                      "avril": [120, 340], "mai": [150, 410],
                      "juin": [180, 390]})
long = large.melt(id_vars="ville", var_name="mois", value_name="trajets")
print(long)
# =>    ville   mois  trajets
#    0   Lyon  avril      120
#    1  Paris  avril      340
#    2   Lyon    mai      150
#    3  Paris    mai      410
#    4   Lyon   juin      180
#    5  Paris   juin      390

"""
   b) Le nombre total de trajets par mois :
"""
print(long.groupby("mois")["trajets"].sum())
# => mois
#    avril    460
#    juin     570
#    mai      560
#    Name: trajets, dtype: int64
"""
Au format long, c'est un simple groupby. Remarquez que les mois sont triés par
ordre ALPHABÉTIQUE (avril, juin, mai) : pour pandas, ce ne sont que des
chaînes de caractères.
"""

"""
   c) Revenez au format large avec .pivot().
"""
print(long.pivot(index="ville", columns="mois", values="trajets"))
# => mois   avril  juin  mai
#    ville
#    Lyon     120   180  150
#    Paris    340   390  410
"""
Les colonnes ne sont plus dans l'ordre de départ : .pivot() trie les noms de
colonnes, ici par ordre alphabétique. On peut rétablir l'ordre en
sélectionnant les colonnes dans l'ordre voulu :
"""
retour = long.pivot(index="ville", columns="mois", values="trajets")
print(retour[["avril", "mai", "juin"]])
# => mois   avril  mai  juin
#    ville
#    Lyon     120  150   180
#    Paris    340  410   390
"""
(Autre solution, plus robuste : convertir la colonne mois en catégorie
ORDONNÉE avant de pivoter, cf. "Créer des classes" dans le chapitre.)
"""

"""
10. Durée moyenne par quartier (lignes) et par statut d'abonné (colonnes),
    avec les moyennes générales.
"""
print(joint.pivot_table(index="quartier", columns="abonne", values="duree",
                        aggfunc="mean", margins=True,
                        margins_name="Tous").round(1))
# => abonne        False  True  Tous
#    quartier
#    Croix-Rousse    NaN  28.5  28.5
#    Part-Dieu      35.0  18.0  29.3
#    Presqu'île     15.0  13.3  13.8
#    Tous           28.3  19.2  22.2
"""
Lecture : à la Part-Dieu, les non-abonnés font des trajets de 35 min en
moyenne, contre 18 min pour les abonnés. La case NaN signifie qu'aucun
non-abonné n'a de trajet à la Croix-Rousse (on ne peut pas faire la moyenne
de zéro valeur). La ligne et la colonne "Tous" donnent les moyennes
générales.
"""


#########################################
#  Compter les combinaisons : crosstab  #
#########################################

"""
11. a) Les trajets par quartier et par statut :
"""
print(pd.crosstab(joint["quartier"], joint["abonne"]))
# => abonne        False  True
#    quartier
#    Croix-Rousse      0      2
#    Part-Dieu         2      1
#    Presqu'île        1      3

"""
    b) La proportion d'abonnés dans chaque quartier :
"""
print(pd.crosstab(joint["quartier"], joint["abonne"],
                  normalize="index").round(2))
# => abonne        False  True
#    quartier
#    Croix-Rousse   0.00   1.00
#    Part-Dieu      0.67   0.33
#    Presqu'île     0.25   0.75
"""
Avec normalize="index", chaque LIGNE totalise 1 : à la Presqu'île, 75 % des
trajets sont faits par des abonnés (3 sur 4).
"""


####################
#  groupby avancé  #
####################

"""
12. Par station : nombre de trajets, durée totale, durée maximale, triés par
    durée totale décroissante.
"""
resume = (
    trajets.groupby("station")
    .agg(nb=("id", "count"), duree_totale=("duree", "sum"),
         duree_max=("duree", "max"))
    .sort_values("duree_totale", ascending=False)
)
print(resume)
# =>          nb  duree_totale  duree_max
#    station
#    S2        3            88         45
#    S3        2            57         35
#    S1        4            55         20
#    S9        1            30         30

"""
13. Une colonne ecart : durée du trajet - durée moyenne de sa station.
"""
moyenne_station = trajets.groupby("station")["duree"].transform("mean")
trajets["ecart"] = (trajets["duree"] - moyenne_station).round(1)
print(trajets[["id", "station", "duree", "ecart"]])
# =>    id station  duree  ecart
#    0   1      S1     12   -1.8
#    1   2      S2     25   -4.3
#    2   3      S1      8   -5.8
#    3   4      S2     45   15.7
#    4   5      S3     22   -6.5
#    5   6      S2     18  -11.3
#    6   7      S9     30    0.0
#    7   8      S3     35    6.5
#    8   9      S1     15    1.2
#    9  10      S1     20    6.2
print(trajets.loc[trajets["ecart"].idxmax(), "id"])  # => 4
"""
.transform("mean") renvoie, pour CHAQUE trajet, la moyenne de sa station : on
peut donc soustraire les deux colonnes ligne à ligne. Le trajet 4 dure 15,7
minutes de plus que la moyenne de la station S2 : c'est le plus "inhabituel".

(Le trajet 7, seul de sa station S9, a un écart de 0 : il est égal à sa propre
moyenne.)
"""

"""
14. a) Les trajets des stations qui ont au moins 3 trajets :
"""
frequentes = trajets.groupby("station").filter(lambda grp: len(grp) >= 3)
print(frequentes["station"].value_counts())
# => station
#    S1    4
#    S2    3
#    Name: count, dtype: int64
"""
S3 (2 trajets) et S9 (1 trajet) ont été éliminées en entier.

    b) Sans exécuter : .agg("mean") retourne UNE valeur par groupe, soit 4
       valeurs ici (S1, S2, S3, S9), avec les stations en index.
       .transform("mean") retourne une valeur par LIGNE du tableau de départ,
       soit 10 valeurs, avec le même index que trajets.
"""
print(len(trajets.groupby("station")["duree"].agg("mean")))        # => 4
print(len(trajets.groupby("station")["duree"].transform("mean")))  # => 10


####################################
#  Les dates : to_datetime et .dt  #
####################################

"""
15. a) Convertir la colonne date :
"""
trajets["date"] = pd.to_datetime(trajets["date"])
print(trajets["date"].dtype)  # => datetime64[us] ([ns] avec pandas 2.x)
"""
Les dates sont au format ISO (année-mois-jour) : pas besoin de format, pandas
les reconnaît sans ambiguïté.

    b) Les colonnes jour et week_end :
"""
trajets["jour"] = trajets["date"].dt.day_name()
trajets["week_end"] = trajets["date"].dt.dayofweek >= 5
print(trajets[["id", "date", "jour", "week_end"]])
# =>    id       date       jour  week_end
#    0   1 2024-06-01   Saturday      True
#    1   2 2024-06-01   Saturday      True
#    2   3 2024-06-02     Sunday      True
#    3   4 2024-06-08   Saturday      True
#    4   5 2024-06-09     Sunday      True
#    5   6 2024-06-12  Wednesday     False
#    6   7 2024-06-15   Saturday      True
#    7   8 2024-06-16     Sunday      True
#    8   9 2024-06-22   Saturday      True
#    9  10 2024-06-29   Saturday      True
"""
.dt.dayofweek vaut 0 pour lundi… et 5 et 6 pour samedi et dimanche : le test
">= 5" donne directement la colonne de booléens, sans boucle ni apply.

    c) Le nombre de trajets du week-end, et les durées moyennes :
"""
print(trajets["week_end"].sum())  # => 9 (True vaut 1, cf. chap. 21)
print(trajets.groupby("week_end")["duree"].mean().round(1))
# => week_end
#    False    18.0
#    True     23.6
#    Name: duree, dtype: float64
"""
9 trajets sur 10 ont eu lieu le week-end. Ils durent en moyenne 23,6 min,
contre 18 min en semaine. Mais attention : il n'y a qu'UN trajet en semaine
(le mercredi 12 juin) ! Une moyenne calculée sur une seule valeur ne permet
aucune conclusion : vérifiez toujours les effectifs (avec .agg(["mean",
"count"]) par exemple) avant de comparer des moyennes.

    d) L'écart entre le premier et le dernier trajet :
"""
print((trajets["date"].max() - trajets["date"].min()).days)  # => 28

"""
16. Sans exécuter : que donne ce code ?
"""
saisies = pd.Series(["31/05/2024", "2024-06-01", "32/06/2024"])
print(pd.to_datetime(saisies, format="%d/%m/%Y", errors="coerce"))
# => 0   2024-05-31
#    1          NaT
#    2          NaT
#    dtype: datetime64[us]
"""
    - "31/05/2024" respecte le format : c'est le 31 mai,
    - "2024-06-01" ne respecte PAS le format imposé (jour/mois/année) : NaT,
    - "32/06/2024" respecte le format… mais le 32 juin n'existe pas : NaT.
Avec errors="coerce", aucune erreur n'est levée : les valeurs invalides
deviennent NaT. Pensez toujours à les compter (.isna().sum()) après coup !
"""


######################################################
#  Les séries temporelles : resample, rolling, shift  #
######################################################

jours = pd.date_range("2024-06-01", "2024-06-30", freq="D")
locations = pd.Series([50 + (i * 13) % 40 for i in range(30)], index=jours)

"""
17. a) Total des locations du 10 au 16 juin :
"""
print(locations.loc["2024-06-10":"2024-06-16"].sum())  # => 522
"""
Avec un index de dates, la slice INCLUT la date de fin (contrairement aux
slices de listes, cf. chap. 31) : on a bien 7 jours.

    b) Total par semaine, et évolution d'une semaine sur l'autre :
"""
semaines = locations.resample("W").sum()
print(pd.DataFrame({"total": semaines,
                    "evolution": semaines.pct_change().round(3)}))
# =>             total  evolution
#    2024-06-02    113        NaN
#    2024-06-09    525      3.646
#    2024-06-16    522     -0.006
#    2024-06-23    479     -0.082
#    2024-06-30    476     -0.006
"""
Attention à la lecture : les semaines se terminent le dimanche, et chaque
ligne est étiquetée par ce dimanche. La première "semaine" ne compte que 2
jours (samedi 1er et dimanche 2 juin) : d'où l'évolution énorme de la semaine
suivante (3.646, soit + 365 %). Comparer des périodes de longueurs différentes
n'a pas de sens : on pourrait comparer des moyennes par jour
(.resample("W").mean()), ou ne garder que les semaines complètes.

    c) Moyenne glissante sur 3 jours :
"""
print(locations.rolling(3).mean().round(1).head(5))
# => 2024-06-01     NaN
#    2024-06-02     NaN
#    2024-06-03    63.0
#    2024-06-04    76.0
#    2024-06-05    75.7
#    Freq: D, dtype: float64
"""
Les 1er et 2 juin, il n'y a pas encore 3 jours de données : la moyenne
glissante vaut NaN. Le 3 juin, c'est la moyenne des 1er, 2 et 3 juin.
"""


###################################
#  Les textes : l'accesseur .str  #
###################################

"""
18. a) Nettoyer les noms de stations du fichier :
"""
stations_brutes = pd.read_csv("exo48_stations.csv")
print(stations_brutes["nom"].tolist())
# => ['  BELLECOUR ', 'part-dieu', 'Croix-Rousse ']
noms = stations_brutes["nom"].str.strip().str.title()
print(noms.tolist())  # => ['Bellecour', 'Part-Dieu', 'Croix-Rousse']
"""
.str.strip() enlève les espaces au début et à la fin, et .str.title() met
une majuscule au début de chaque mot (y compris après le tiret : Part-Dieu).

    b) Code postal et arrondissement :
"""
adresses = pd.Series(["Place Bellecour, 69002 Lyon",
                      "Rue de la Part-Dieu, 69003 Lyon",
                      "Bd de la Croix-Rousse, 69004 Lyon"])
codes = adresses.str.extract(r"(\d{5})")
print(codes)
# =>        0
#    0  69002
#    1  69003
#    2  69004
arrondissement = codes[0].str[-2:].astype(int)
print(arrondissement.tolist())  # => [2, 3, 4]
r"""
- r"(\d{5})" : exactement 5 chiffres consécutifs (cf. chap. 42). Les
  parenthèses délimitent le GROUPE à extraire, qui devient la colonne 0.
- .str[-2:] applique une slice (cf. chap. 31) à chaque chaîne : les deux
  derniers caractères ("02"). .astype(int) les convertit en entiers (2).

    c) Les adresses qui contiennent "Rue" :
"""
print(adresses[adresses.str.contains("Rue")].tolist())
# => ['Rue de la Part-Dieu, 69003 Lyon']
"""
Attention, .str.contains() est sensible à la casse par défaut : avec
case=False, "rue" écrit en minuscules serait aussi trouvé.
"""


##########################
#  Nettoyer des données  #
##########################

"""
19. Nettoyer exo48_trajets.csv étape par étape :
"""
brut = pd.read_csv("exo48_trajets.csv", sep=";")
print(len(brut))  # => 15 (lignes au départ)

# a) Les doublons (la ligne du trajet 3 a été enregistrée deux fois)
propre = brut.drop_duplicates()
print(len(propre))  # => 14

# b) Les stations : sans espaces, en majuscules
propre["station"] = propre["station"].str.strip().str.upper()
print(propre["station"].value_counts().sort_index().to_dict())
# => {'S1': 5, 'S2': 5, 'S3': 3, 'S9': 1}

# c) "oui"/"Oui"/"OUI" → True, "non" → False : on passe en minuscules
# AVANT d'appliquer le dictionnaire, pour couvrir toutes les variantes.
propre["abonne"] = propre["abonne"].str.lower().map({"oui": True,
                                                     "non": False})
print(propre["abonne"].isna().sum())  # => 0 (aucune valeur non reconnue)

# d) Les trajets sans durée
propre = propre.dropna(subset=["duree"])
print(len(propre))  # => 13

# e) Les durées impossibles : négatives, ou plus de 12 h (720 min)
propre["duree"] = propre["duree"].where(propre["duree"].between(0, 720))
print(propre["duree"].isna().sum())  # => 2 (durées impossibles)
propre = propre.dropna(subset=["duree"])
print(len(propre))  # => 11

# f) Les types : dates à la française, durée entière
propre["date"] = pd.to_datetime(propre["date"], format="%d/%m/%Y")
propre["duree"] = propre["duree"].astype(int)
print(propre.dtypes)
# => id                  int64
#    date       datetime64[us]
#    station               str
#    duree               int64
#    abonne               bool
#    dtype: object
"""
Il reste 11 lignes sur 15 : on a supprimé un doublon (étape a), un trajet
sans durée (d) et deux durées impossibles, -5 et 9999 minutes (e).

Remarques :
    - la colonne duree a été lue comme des float, à cause de la case vide
      (NaN est un float, cf. chap. 39) : on ne peut la convertir en entiers
      qu'APRÈS avoir supprimé les NaN,
    - on a gardé le trajet de la station S9 : elle est inconnue, mais le
      trajet en lui-même est valide. C'est la jointure (exercice 24) qui
      décidera quoi en faire.
"""


#####################################
#  Créer des classes : cut et qcut  #
#####################################

"""
20. a) Une colonne categorie (court / moyen / long) :
"""
trajets["categorie"] = pd.cut(trajets["duree"], bins=[0, 15, 30, 1000],
                              labels=["court", "moyen", "long"])
print(trajets[["id", "duree", "categorie"]].head(4))
# =>    id  duree categorie
#    0   1     12     court
#    1   2     25     moyen
#    2   3      8     court
#    3   4     45      long
"""
Les intervalles sont ]0, 15], ]15, 30] et ]30, 1000] : la borne de droite est
INCLUSE, donc un trajet de 15 min est "court" et un trajet de 30 min est
"moyen", comme demandé. (1000 est une borne "assez grande" pour tout couvrir ;
on peut aussi utiliser float("inf"), cf. chap. 4.)

    b) Le nombre de trajets par catégorie :
"""
print(trajets["categorie"].value_counts(sort=False))
# => categorie
#    court    3
#    moyen    5
#    long     2
#    Name: count, dtype: int64
"""
Avec sort=False, value_counts() respecte l'ordre des catégories (court, moyen,
long) au lieu de trier par effectif.

    c) Deux classes de même effectif :
"""
deux = pd.qcut(trajets["duree"], q=2)
print(deux.value_counts(sort=False))
# => duree
#    (7.999, 21.0]    5
#    (21.0, 45.0]     5
#    Name: count, dtype: int64
print(trajets["duree"].median())  # => 21.0
"""
Sans labels=…, qcut nomme les classes par leurs intervalles. La borne qui
sépare les deux classes est 21.0 minutes : c'est la médiane des durées
(5 trajets en dessous, 5 au-dessus). (Le 7.999 au lieu de 8 vient de ce que
qcut élargit très légèrement la première classe pour inclure le minimum.)
"""


##############################
#  apply ou vectorisation ?  #
##############################

"""
21. Le prix, sans apply.
"""
trajets["prix"] = trajets.apply(
    lambda l: 1.0 if l["abonne"] else 1.0 + 0.1 * l["duree"], axis=1).round(2)

# Solution 1 : "not abonne" vaut 1 pour les non-abonnés, 0 pour les abonnés
prix_1 = (1.0 + 0.1 * trajets["duree"] * ~trajets["abonne"]).round(2)

# Solution 2 : .where(condition, autre) garde la valeur là où la condition
# est vraie, et prend "autre" ailleurs
prix_2 = (1.0 + 0.1 * trajets["duree"]).where(~trajets["abonne"], 1.0)
prix_2 = prix_2.round(2)

print(prix_1.tolist())  # => [1.0, 3.5, 1.0, 5.5, 1.0, 1.0, 4.0, 1.0, 2.5, 1.0]
print(trajets["prix"].equals(prix_1))  # => True
print(trajets["prix"].equals(prix_2))  # => True
"""
- ~ inverse une Series de booléens (comme "not", cf. chap. 21 et 38) :
  ~trajets["abonne"] vaut True pour les NON-abonnés,
- multiplié par un nombre, True vaut 1 et False vaut 0 : le supplément à la
  minute est annulé pour les abonnés.
Les deux versions vectorisées donnent exactement le même résultat que apply,
en étant bien plus rapides sur de gros volumes (cf. chapitre).
"""


#############################################
#  Enchaîner les méthodes : assign et pipe  #
#############################################

"""
22. a) La fonction nettoyer_stations :
"""
def nettoyer_stations(table):
    """Retourne une copie de table avec des noms de stations propres."""
    return table.assign(nom=table["nom"].str.strip().str.title())


"""
    b) Une seule chaîne de méthodes :
"""
longues = (
    pd.read_csv("exo48_stations.csv")
    .pipe(nettoyer_stations)
    .assign(longueur_nom=lambda t: t["nom"].str.len())
    .query("longueur_nom > 9")
)
print(longues)
# =>   station           nom      quartier  longueur_nom
#    2      S3  Croix-Rousse  Croix-Rousse            12
"""
- .pipe(nettoyer_stations) appelle nettoyer_stations(tableau_en_cours),
- la lambda de .assign() reçoit le tableau DÉJÀ nettoyé : la longueur est
  calculée sur les noms sans espaces (sinon "  BELLECOUR " compterait 12
  caractères !),
- "Bellecour" et "Part-Dieu" (9 caractères chacun) ne sont pas strictement
  plus longs que 9 : ils sont écartés.
"""


#####################################
#  Lire et écrire d'autres formats  #
#####################################

"""
23. a) Écrire trajets "à la française" :
"""
export = trajets[["id", "date", "station", "duree"]].assign(
    km=lambda t: t["duree"] * 0.25)
export.to_csv("exo48_export.csv", sep=";", decimal=",", index=False)

"""
    b) Les 3 premières lignes du fichier :
"""
with open("exo48_export.csv", "r", encoding="utf-8") as f:
    for numero, ligne in enumerate(f):
        if numero == 3:
            break
        print(ligne, end="")
# => id;date;station;duree;km
#    1;2024-06-01;S1;12;3,0
#    2;2024-06-01;S2;25;6,25
"""
Les km sont écrits avec une virgule (3,0), comme le veut un tableur réglé en
français. Le point-virgule sépare les colonnes, pour éviter la confusion avec
la virgule décimale.

    c) Relire le fichier :
"""
relu = pd.read_csv("exo48_export.csv", sep=";", decimal=",",
                   parse_dates=["date"])
print(relu["km"].dtype)  # => float64
print(relu["km"].sum())  # => 57.5
"""
Sans decimal=",", la colonne km serait lue comme du texte ("3,0" n'est pas un
nombre pour Python, cf. chap. 6).
"""


##########################
#  Cas pratique : bilan  #
##########################

"""
24. a) Le nettoyage en une chaîne de méthodes :
"""
trajets_juin = (
    pd.read_csv("exo48_trajets.csv", sep=";")
    .drop_duplicates()
    .assign(
        station=lambda t: t["station"].str.strip().str.upper(),
        abonne=lambda t: t["abonne"].str.lower().map({"oui": True,
                                                      "non": False}),
        date=lambda t: pd.to_datetime(t["date"], format="%d/%m/%Y"),
    )
    .dropna(subset=["duree"])
    .query("0 <= duree <= 720")
    .astype({"duree": int})
)
print(len(trajets_juin))  # => 11
"""
.query("0 <= duree <= 720") remplace les étapes e) de l'exercice 19 : les
comparaisons enchaînées fonctionnent comme en Python (cf. chap. 9).

    b) La jointure avec les stations nettoyées :
"""
stations_propres = pd.read_csv("exo48_stations.csv").pipe(nettoyer_stations)
verif = pd.merge(trajets_juin, stations_propres, on="station", how="left",
                 validate="many_to_one", indicator=True)
print(verif[verif["_merge"] == "left_only"][["id", "station"]])
# =>    id station
#    5   8      S9
bilan = verif.query("_merge == 'both'").drop(columns="_merge")
print(len(bilan))  # => 10
"""
On écarte le trajet 8 (station S9 inconnue) : il en reste 10.

    c) Par quartier : nombre de trajets, durée moyenne, part d'abonnés.
"""
par_quartier = bilan.groupby("quartier").agg(
    nb=("id", "count"),
    duree_moy=("duree", "mean"),
    part_abonnes=("abonne", "mean"),
).round(2)
print(par_quartier)
# =>               nb  duree_moy  part_abonnes
#    quartier
#    Croix-Rousse   2      28.50           1.0
#    Part-Dieu      4      25.50           0.5
#    Presqu'île     4      13.75           0.5
"""
La moyenne d'une colonne de booléens est la PROPORTION de True (True vaut 1,
False vaut 0) : à la Croix-Rousse, tous les trajets (1.00) ont été faits par
des abonnés.

    d) Le nombre de trajets par quartier et par semaine :
"""
semaine = bilan.assign(semaine=lambda t: t["date"].dt.isocalendar().week)
print(semaine.pivot_table(index="quartier", columns="semaine", values="id",
                          aggfunc="count", fill_value=0))
# => semaine       22  23  24  25  26
#    quartier
#    Croix-Rousse   0   0   1   1   0
#    Part-Dieu      1   1   1   0   1
#    Presqu'île     2   0   0   1   1
"""
.dt.isocalendar().week donne le numéro de semaine de la norme ISO (les
semaines commencent le lundi). Le 1er juin 2024 étant un samedi, il appartient
à la semaine 22. fill_value=0 remplace les cases vides (aucun trajet) par 0.
"""


###############
#  Nettoyage  #
###############

for nom_fichier in ["exo48_trajets.csv", "exo48_stations.csv",
                    "exo48_export.csv"]:
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)
