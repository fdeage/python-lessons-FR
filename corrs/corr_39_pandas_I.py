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
#  Chap. 39     #  Pandas I : corrigés                                         #
#               #                                                              #
################################################################################

"""
Les affichages ci-dessous ont été vérifiés avec pandas 3.0.6. Avec une autre
version, la présentation peut légèrement varier (notamment les types affichés
par .dtypes, cf. chapitre).
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

# 1. Une Series avec un index personnalisé :
temperatures = pd.Series([18, 22, 25, 19, 21],
                         index=["lun", "mar", "mer", "jeu", "ven"])

# a) On accède à une valeur par son index, comme dans un dictionnaire :
print(temperatures["mer"])  # => 25

# b) Statistiques :
print(temperatures.mean())    # => 21.0
print(temperatures.max())     # => 25
print(temperatures.idxmax())  # => mer (l'INDEX de la valeur maximale)

# c) Les opérations s'appliquent à toutes les valeurs, sans boucle :
print(temperatures * 9 / 5 + 32)
# => lun    64.4
#    mar    71.6
#    mer    77.0
#    jeu    66.2
#    ven    69.8
#    dtype: float64

# d) Une comparaison donne une Series de booléens (un "masque")…
print(temperatures > 20)
# => lun    False
#    mar     True
#    mer     True
#    jeu    False
#    ven     True
#    dtype: bool
# … qu'on utilise entre crochets pour filtrer :
print(temperatures[temperatures > 20])
# => mar    22
#    mer    25
#    ven    21
#    dtype: int64

# 2. Une Series calcule valeur par valeur, une liste se répète :
print(pd.Series([1, 2, 3]) * 2)
# => 0    2
#    1    4
#    2    6
#    dtype: int64
print([1, 2, 3] * 2)  # => [1, 2, 3, 1, 2, 3] (cf. chap. 16)
"""
Pour une liste, "* 2" signifie "répéter la liste deux fois". Pour une Series,
c'est une opération "vectorisée" : chaque valeur est multipliée par 2. C'est
l'une des grandes différences entre pandas et les types construits de Python.
"""


####################
#  Les DataFrames  #
####################

# 3. a) Un dictionnaire de listes : une clé par COLONNE.
fruits_a = pd.DataFrame({
    "nom": ["pomme", "kiwi", "banane"],
    "prix": [2.5, 4.0, 1.8],
    "stock": [120, 35, 80],
})

# 3. b) Une liste de dictionnaires : un dictionnaire par LIGNE (le format de
# csv.DictReader, cf. chap. 28).
fruits_b = pd.DataFrame([
    {"nom": "pomme", "prix": 2.5, "stock": 120},
    {"nom": "kiwi", "prix": 4.0, "stock": 35},
    {"nom": "banane", "prix": 1.8, "stock": 80},
])

print(fruits_a)
# =>       nom  prix  stock
#    0   pomme   2.5    120
#    1    kiwi   4.0     35
#    2  banane   1.8     80
print(fruits_a.equals(fruits_b))  # => True


#########################
#  Lire un fichier CSV  #
#########################

# 4. a) Une seule ligne suffit :
df = pd.read_csv("exo_pandas_eleves.csv")
print(df)
# =>       nom classe  age  maths  physique  francais
#    0   Alice      A   16   15.0      12.0      17.0
#    1     Bob      B   17    8.0       NaN       9.0
#    2   Chloé      A   16   12.0      14.0      10.0
#    3   David      B   18    6.0       9.0      11.0
#    4    Emma      A   17   18.0      16.0       NaN
#    5   Farid      C   16   11.0      13.0      14.0
#    6  Gaëlle      C   17    NaN      10.0      15.0
#    7    Hugo      B   16   14.0      15.0      12.0

# b) (lignes, colonnes) :
print(df.shape)  # => (8, 6)

# c)
print(list(df.columns))
# => ['nom', 'classe', 'age', 'maths', 'physique', 'francais']

# d)
print(df.dtypes)
# => nom             str
#    classe          str
#    age           int64
#    maths       float64
#    physique    float64
#    francais    float64
#    dtype: object
"""
Les colonnes maths, physique et francais contiennent des cases vides, que
pandas remplace par NaN. Or NaN est un float (cf. chapitre) : pour que toute
la colonne ait le même type, pandas convertit toutes ses valeurs en float
(15 devient 15.0). La colonne age, sans case vide, reste en int64.
"""


###########################
#  Explorer un DataFrame  #
###########################

# 5. .head() pour le début, .tail() pour la fin :
print(df.head(3))
# =>      nom classe  age  maths  physique  francais
#    0  Alice      A   16   15.0      12.0      17.0
#    1    Bob      B   17    8.0       NaN       9.0
#    2  Chloé      A   16   12.0      14.0      10.0
print(df.tail(2))
# =>       nom classe  age  maths  physique  francais
#    6  Gaëlle      C   17    NaN      10.0      15.0
#    7    Hugo      B   16   14.0      15.0      12.0

# 6. Statistiques des notes :
print(df[["maths", "physique", "francais"]].describe())
# =>            maths   physique   francais
#    count   7.000000   7.000000   7.000000
#    mean   12.000000  12.714286  12.571429
#    std     4.123106   2.563480   2.878492
#    min     6.000000   9.000000   9.000000
#    25%     9.500000  11.000000  10.500000
#    50%    12.000000  13.000000  12.000000
#    75%    14.500000  14.500000  14.500000
#    max    18.000000  16.000000  17.000000
"""
"count" est le nombre de valeurs RENSEIGNÉES de chaque colonne : les NaN ne
sont pas comptés (ni dans la moyenne, ni dans les autres statistiques). Il
manque une note dans chacune des trois colonnes, d'où 7 au lieu de 8.
"""


###############################
#  Sélectionner des colonnes  #
###############################

# 7. a) Une colonne est une Series : on a accès à toutes ses méthodes.
print(round(df["maths"].mean(), 2))  # => 12.0

# 7. b)
print(list(df["classe"].unique()))  # => ['A', 'B', 'C']

# 7. c) .value_counts() compte les occurrences de chaque valeur :
print(df["classe"].value_counts())
# => classe
#    A    3
#    B    3
#    C    2
#    Name: count, dtype: int64

# 8. Avec des DOUBLES crochets, on obtient un DataFrame :
print(df[["nom", "francais"]])
# =>       nom  francais
#    0   Alice      17.0
#    1     Bob       9.0
#    2   Chloé      10.0
#    3   David      11.0
#    4    Emma       NaN
#    5   Farid      14.0
#    6  Gaëlle      15.0
#    7    Hugo      12.0
try:
    df["anglais"]
except KeyError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : 'anglais')


###########################################
#  Sélectionner des lignes : loc et iloc  #
###########################################

# 9. .iloc sélectionne par POSITION (comme les indices d'une liste) :
print(df.iloc[0])
# => nom         Alice
#    classe          A
#    age            16
#    maths        15.0
#    physique     12.0
#    francais     17.0
#    Name: 0, dtype: object
print(df.iloc[-2:])
# =>       nom classe  age  maths  physique  francais
#    6  Gaëlle      C   17    NaN      10.0      15.0
#    7    Hugo      B   16   14.0      15.0      12.0
print(df.iloc[1:4, 0:3])  # la borne de fin est EXCLUE avec .iloc
# =>      nom classe  age
#    1    Bob      B   17
#    2  Chloé      A   16
#    3  David      B   18

# 10. .loc sélectionne par ÉTIQUETTE (ici, le nom de l'élève) :
df_nom = df.set_index("nom")
print(df_nom.loc["Emma", "maths"])  # => 18.0
print(df_nom.loc["Bob":"David", ["maths", "physique"]])
# =>        maths  physique
#    nom                   
#    Bob      8.0       NaN
#    Chloé   12.0      14.0
#    David    6.0       9.0
"""
Avec .loc, la borne de fin d'une slice est INCLUSE : David fait partie du
résultat (contrairement à .iloc et aux slices de listes, cf. chap. 31).
"""


########################
#  Filtrer les lignes  #
########################

# 11. a) Les NaN ne vérifient aucune comparaison : Gaëlle n'apparaît pas.
print(df[df["maths"] >= 12]["nom"].tolist())
# => ['Alice', 'Chloé', 'Emma', 'Hugo']

# 11. b) Deux conditions : "&" (et), chacune entre parenthèses.
print(df[(df["classe"] == "A") & (df["francais"] > 12)]["nom"].tolist())
# => ['Alice']

# 11. c) .isin() teste l'appartenance à une liste de valeurs :
print(df[df["classe"].isin(["B", "C"])]["nom"].tolist())
# => ['Bob', 'David', 'Farid', 'Gaëlle', 'Hugo']

# 11. d) "|" (ou) :
print(df[(df["age"] == 16) | (df["maths"] < 10)]["nom"].tolist())
# => ['Alice', 'Bob', 'Chloé', 'David', 'Farid', 'Hugo']

# 12. "and" demande à Python de convertir chaque Series en UN SEUL booléen,
# ce qui est ambigu : pandas soulève une ValueError.
try:
    df[df["age"] > 16 and df["maths"] > 10]
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 3: (Sans ce try: … except …, cette ligne créerait : The truth value of a
#    Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().)
# Correction : "&" et des parenthèses (cf. chapitre).
print(df[(df["age"] > 16) & (df["maths"] > 10)]["nom"].tolist())  # => ['Emma']


##################################
#  Les valeurs manquantes : NaN  #
##################################

# 13. a) .isna() donne des booléens ; True compte pour 1 dans une somme.
print(df.isna().sum())
# => nom         0
#    classe      0
#    age         0
#    maths       1
#    physique    1
#    francais    1
#    dtype: int64

# 13. b)
print(df[df["physique"].isna()]["nom"].tolist())  # => ['Bob']

# 13. c) .dropna() retourne un NOUVEAU DataFrame :
print(df.dropna().shape)  # => (5, 6)
print(df.shape)           # => (8, 6) (df n'a pas été modifié)

# 14. La moyenne ignore les NaN : elle est calculée sur 7 élèves.
print(round(df["maths"].mean(), 2))            # => 12.0 (84 / 7)
print(round(df["maths"].fillna(0).mean(), 2))  # => 10.5 (84 / 8)
"""
Remplacer un NaN par 0, c'est inventer un 0 que l'élève n'a pas eu : la
moyenne de la classe baisse artificiellement. Ignorer la valeur manquante est
ici plus juste. Le bon choix dépend toujours de ce que signifie la donnée
manquante (absence justifiée, oubli de saisie…).
"""


######################################
#  Ajouter et modifier des colonnes  #
######################################

# 15. a) Le calcul se fait ligne à ligne, mais un NaN "contamine" le résultat :
df["moyenne"] = (df["maths"] + df["physique"] + df["francais"]) / 3
print(df[["nom", "moyenne"]])
# =>       nom    moyenne
#    0   Alice  14.666667
#    1     Bob        NaN
#    2   Chloé  12.000000
#    3   David   8.666667
#    4    Emma        NaN
#    5   Farid  12.666667
#    6  Gaëlle        NaN
#    7    Hugo  13.666667
"""
Bob n'a pas de note de physique : 8 + NaN + 9 vaut NaN. Toute opération avec
NaN donne NaN. Même chose pour Emma et Gaëlle.
"""

# 15. b) .mean(axis=1) calcule la moyenne de chaque ligne, sans les NaN :
df["moyenne"] = df[["maths", "physique", "francais"]].mean(axis=1).round(2)
print(df[["nom", "moyenne"]])
# =>       nom  moyenne
#    0   Alice    14.67
#    1     Bob     8.50
#    2   Chloé    12.00
#    3   David     8.67
#    4    Emma    17.00
#    5   Farid    12.67
#    6  Gaëlle    12.50
#    7    Hugo    13.67


# 16. .apply() appelle la fonction sur chaque valeur de la colonne :
def mention(moyenne):
    if moyenne >= 16:
        return "Très bien"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Insuffisant"


df["mention"] = df["moyenne"].apply(mention)
print(df[["nom", "moyenne", "mention"]])
# =>       nom  moyenne      mention
#    0   Alice    14.67         Bien
#    1     Bob     8.50  Insuffisant
#    2   Chloé    12.00   Assez bien
#    3   David     8.67  Insuffisant
#    4    Emma    17.00    Très bien
#    5   Farid    12.67   Assez bien
#    6  Gaëlle    12.50   Assez bien
#    7    Hugo    13.67   Assez bien

# 17. .rename() et .drop() retournent un nouveau DataFrame : on réaffecte df.
df = df.rename(columns={"francais": "français"})
df = df.drop(columns=["age"])
print(list(df.columns))
# => ['nom', 'classe', 'maths', 'physique', 'français', 'moyenne', 'mention']


###########
#  Trier  #
###########

# 18. a)
print(df.sort_values("moyenne", ascending=False)[["nom", "moyenne"]])
# =>       nom  moyenne
#    4    Emma    17.00
#    0   Alice    14.67
#    7    Hugo    13.67
#    5   Farid    12.67
#    6  Gaëlle    12.50
#    2   Chloé    12.00
#    3   David     8.67
#    1     Bob     8.50

# 18. b) Deux façons d'obtenir les 3 meilleurs :
print(df.sort_values("moyenne", ascending=False).head(3)["nom"].tolist())
# => ['Emma', 'Alice', 'Hugo']
print(df.nlargest(3, "moyenne")["nom"].tolist())
# => ['Emma', 'Alice', 'Hugo']

# 18. c) Plusieurs colonnes de tri, chacune avec son ordre :
print(df.sort_values(["classe", "moyenne"], ascending=[True, False])
      [["classe", "nom", "moyenne"]])
# =>   classe     nom  moyenne
#    4      A    Emma    17.00
#    0      A   Alice    14.67
#    2      A   Chloé    12.00
#    7      B    Hugo    13.67
#    3      B   David     8.67
#    1      B     Bob     8.50
#    5      C   Farid    12.67
#    6      C  Gaëlle    12.50


#########################
#  Regrouper : groupby  #
#########################

# 19. a) La moyenne par classe :
print(df.groupby("classe")["moyenne"].mean().round(2))
# => classe
#    A    14.56
#    B    10.28
#    C    12.58
#    Name: moyenne, dtype: float64

# 19. b) Le nombre d'élèves par classe (.size() compte les lignes) :
print(df.groupby("classe").size())
# => classe
#    A    3
#    B    3
#    C    2
#    dtype: int64

# 19. c) Plusieurs statistiques à la fois avec .agg() :
print(df.groupby("classe")["maths"].agg(["min", "max"]))
# =>          min   max
#    classe            
#    A       12.0  18.0
#    B        6.0  14.0
#    C       11.0  11.0
"""
La classe A a la meilleure moyenne. Remarquez que pour la classe C, le
minimum et le maximum de maths sont égaux : Gaëlle n'a pas de note, il ne
reste que celle de Farid.
"""


##########################
#  Exporter et nettoyer  #
##########################

# 20. On filtre, on trie, on garde 3 colonnes, puis on exporte sans l'index :
classe_a = df[df["classe"] == "A"].sort_values("moyenne", ascending=False)
classe_a[["nom", "moyenne", "mention"]].to_csv("exo_pandas_classe_A.csv",
                                               index=False)
print(pd.read_csv("exo_pandas_classe_A.csv"))
# =>      nom  moyenne     mention
#    0   Emma    17.00   Très bien
#    1  Alice    14.67        Bien
#    2  Chloé    12.00  Assez bien


###############
#  Nettoyage  #
###############

for nom_fichier in ["exo_pandas_eleves.csv", "exo_pandas_classe_A.csv"]:
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)
