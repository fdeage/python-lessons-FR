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
#  Chap. xx     #  Pandas I                                                    #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Installer et importer pandas
#  - Les Series
#  - Les DataFrames
#  - Lire un fichier CSV
#  - Explorer un DataFrame
#  - Sélectionner des colonnes
#  - Sélectionner des lignes : loc et iloc
#  - Filtrer les lignes
#  - Les valeurs manquantes : NaN
#  - Ajouter et modifier des colonnes
#  - Trier
#  - Regrouper : groupby
#  - Exporter et nettoyer
#
##############################

# Introduction
###############

"""
pandas est LA bibliothèque Python de manipulation de données tabulaires
(c'est-à-dire de tableaux à lignes et colonnes, comme une feuille Excel ou une
table SQL). C'est l'outil de base de la Data Science en Python.

On peut voir pandas comme le TCD (Tableau Croisé Dynamique) de la donnée : il
permet de charger un tableau, d'en sélectionner une partie, de le filtrer, de
le trier, de calculer des statistiques et de regrouper des lignes… en quelques
lignes de code, et sur des millions de lignes.

pandas repose sur deux types d'objets :
    - la Series : une colonne de données (une suite de valeurs avec un index)
    - le DataFrame : un tableau de données (plusieurs Series côte à côte, qui
      partagent le même index)

Ce chapitre suppose que vous connaissez les listes (chap. 16 et 24), les
dictionnaires (chap. 18 et 27), les modules (chap. 22) et les fichiers CSV
(chap. 28).

Note : l'affichage exact des tableaux peut légèrement varier selon votre
version de pandas (notamment les types affichés par .dtypes et .info(), cf.
plus bas). Ce chapitre a été vérifié avec pandas 3.0 ; la plupart des
exemples fonctionnent à l'identique avec pandas 1.x et 2.x.
"""


# Installer et importer pandas
###############################

"""
pandas ne fait pas partie de la bibliothèque standard de Python : il faut
l'installer (une seule fois), avec un gestionnaire de packages (cf. chap. 0 et
chap. 22) :
    ?> pip install pandas
ou
    ?> conda install pandas

On l'importe ensuite, par convention, sous l'alias "pd" (cf. chap. 22). Tout le
monde utilise cet alias : vous le retrouverez dans toutes les documentations.

Ici, on protège l'import avec try … except (cf. chap. 26) : si pandas n'est pas
installé, le programme affiche un message et s'arrête proprement avec
sys.exit() (cf. chap. 22), au lieu de crasher.
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

print(pd.__version__)  # => 3.0.6 (variable : dépend de votre installation)


# Les Series
#############

"""
Une Series est une colonne de valeurs, un peu comme une liste. On la crée avec
pd.Series(), en lui passant une liste :
"""
notes = pd.Series([12, 15, 9, 17])
print(notes)
# => 0    12
#    1    15
#    2     9
#    3    17
#    dtype: int64

"""
L'affichage montre deux colonnes :
    - à gauche, l'INDEX de chaque valeur (ici 0, 1, 2, 3, comme les indices
      d'une liste),
    - à droite, les valeurs elles-mêmes.
La dernière ligne donne le type ("dtype") des valeurs : int64 est un entier
codé sur 64 bits.

IMPT : toutes les valeurs d'une Series ont le même type (contrairement à une
liste Python). C'est ce qui rend pandas si rapide.

On peut donner un index personnalisé, avec le paramètre index=… : la Series
ressemble alors à un dictionnaire.
"""
notes = pd.Series([12, 15, 9, 17], index=["Alice", "Bob", "Chloé", "David"])
print(notes)
# => Alice    12
#    Bob      15
#    Chloé     9
#    David    17
#    dtype: int64

print(notes["Bob"])  # => 15 (on accède à une valeur par son index)

"""
L'intérêt d'une Series : on peut appliquer une opération à TOUTES les valeurs
d'un coup, sans boucle ni compréhension (on dit que l'opération est
"vectorisée") :
"""
print(notes + 1)
# => Alice    13
#    Bob      16
#    Chloé    10
#    David    18
#    dtype: int64

print(notes > 10)
# => Alice     True
#    Bob       True
#    Chloé    False
#    David     True
#    dtype: bool

"""
Et on dispose de nombreuses méthodes statistiques :
"""
print(notes.mean())  # => 13.25 (la moyenne)
print(notes.max())   # => 17
print(notes.sum())   # => 53
print(notes.idxmax())  # => David (l'index de la valeur maximale)


# Les DataFrames
#################

"""
Un DataFrame est un tableau : des lignes et des colonnes. Chaque colonne est
une Series, et a un nom.

Il peut être intéressant de créer un DataFrame basique avec des données
littérales. Cet objet pourra ensuite être manipulé à des fins de tests, ou pour
un PoC ("Proof of Concept", un prototype).

La façon la plus simple est de passer à pd.DataFrame() un dictionnaire :
    - chaque clé devient le nom d'une colonne,
    - chaque valeur (une liste) devient le contenu de la colonne.
"""
data = {
    "pokemon": ["Charmander", "Squirtle", "Bulbasaur"],
    "type": ["Fire", "Water", "Grass"],
}
df_pokemon = pd.DataFrame(data)
print(df_pokemon)
# =>       pokemon   type
#    0  Charmander   Fire
#    1    Squirtle  Water
#    2   Bulbasaur  Grass

"""
On obtient un DataFrame de deux colonnes, avec un en-tête "pokemon" et un
en-tête "type". Les deux listes sont associées par position : "Squirtle" (2e
valeur de la 1re liste) est associé à "Water" (2e valeur de la 2e liste).
Toutes les listes doivent donc avoir la même longueur.

On peut aussi utiliser la méthode pd.DataFrame.from_dict(), qui fait la même
chose :
"""
print(pd.DataFrame.from_dict(data).equals(df_pokemon))  # => True

"""
Une autre façon courante est de partir d'une liste de dictionnaires (une ligne
par dictionnaire), exactement le format obtenu avec csv.DictReader() au
chap. 28 :
"""
lignes = [
    {"pokemon": "Pikachu", "type": "Electric", "niveau": 12},
    {"pokemon": "Eevee", "type": "Normal", "niveau": 8},
]
print(pd.DataFrame(lignes))
# =>    pokemon      type  niveau
#    0  Pikachu  Electric      12
#    1    Eevee    Normal       8


# Lire un fichier CSV
######################

"""
En pratique, on crée rarement un DataFrame à la main : on charge des données
depuis un fichier. Le format le plus courant est le CSV (cf. chap. 28).

Comme au chap. 28, on commence par créer nous-mêmes un fichier CSV, pour que ce
chapitre soit exécutable. Remarquez que deux cinémas n'ont pas de note (la
valeur est vide entre deux virgules) : on y reviendra dans la section sur les
valeurs manquantes.
"""
with open("cinemas.csv", "w", encoding="utf-8") as f:
    f.write(
        "id,nom,ville,places,salles,note\n"
        "26,Gaumont Bellecour,Lyon,200,6,4.1\n"
        "12,Louxor,Paris,420,3,4.7\n"
        "35,Grand Rex,Paris,600,7,4.5\n"
        "4,Mk2 Quai de Loire,Paris,320,4,\n"
        "81,Pathé Wepler,Paris,500,14,3.9\n"
        "10,UGC George V,Paris,110,11,3.6\n"
        "7,Comoedia,Lyon,250,8,4.6\n"
        "53,Les Variétés,Marseille,180,5,\n"
    )

"""
Avec pandas, lire ce fichier tient en une ligne, avec pd.read_csv() : pas
besoin d'ouvrir le fichier, de créer un lecteur, ni de boucle !
"""
df = pd.read_csv("cinemas.csv")
print(df)
# =>    id                nom      ville  places  salles  note
#    0  26  Gaumont Bellecour       Lyon     200       6   4.1
#    1  12             Louxor      Paris     420       3   4.7
#    2  35          Grand Rex      Paris     600       7   4.5
#    3   4  Mk2 Quai de Loire      Paris     320       4   NaN
#    4  81       Pathé Wepler      Paris     500      14   3.9
#    5  10       UGC George V      Paris     110      11   3.6
#    6   7           Comoedia       Lyon     250       8   4.6
#    7  53       Les Variétés  Marseille     180       5   NaN

"""
Remarques :
    - pandas a utilisé la première ligne comme en-tête (noms des colonnes),
    - il a ajouté un index (0, 1, 2…) à gauche,
    - IMPT : contrairement au module csv, il a converti TOUT SEUL les nombres :
      "places" et "salles" sont des entiers, "note" est un float,
    - les notes manquantes sont devenues NaN (voir plus bas).

pd.read_csv() a de nombreux paramètres utiles, par exemple :
    - sep=";" si le séparateur est un point-virgule,
    - index_col="id" pour utiliser une colonne comme index,
    - encoding="latin-1" si le fichier n'est pas en UTF-8.
"""


# Explorer un DataFrame
########################

"""
Quand on charge un jeu de données, la première chose à faire est d'y jeter un
œil : quelle taille ? quelles colonnes ? quels types ? quelles valeurs ?
"""

# .head(n) affiche les n premières lignes (5 par défaut), .tail(n) les dernières
print(df.head(3))
# =>    id                nom  ville  places  salles  note
#    0  26  Gaumont Bellecour   Lyon     200       6   4.1
#    1  12             Louxor  Paris     420       3   4.7
#    2  35          Grand Rex  Paris     600       7   4.5

# .shape donne les dimensions du tableau : un tuple (lignes, colonnes)
print(df.shape)  # => (8, 6)

# .columns donne le nom des colonnes
print(list(df.columns))  # => ['id', 'nom', 'ville', 'places', 'salles', 'note']

# .dtypes donne le type de chaque colonne
print(df.dtypes)
# => id          int64
#    nom           str
#    ville         str
#    places      int64
#    salles      int64
#    note      float64
#    dtype: object
# (Avant pandas 3.0, les colonnes de texte sont de type "object" au lieu de
# "str".)

"""
.describe() calcule d'un coup les principales statistiques de chaque colonne
numérique : nombre de valeurs (count), moyenne (mean), écart-type (std),
minimum, quartiles (25 %, 50 % = la médiane, 75 %) et maximum.
"""
print(df[["places", "salles", "note"]].describe())
# =>            places     salles      note
#    count    8.000000   8.000000  6.000000
#    mean   322.500000   7.250000  4.233333
#    std    170.608156   3.693624  0.436654
#    min    110.000000   3.000000  3.600000
#    25%    195.000000   4.750000  3.950000
#    50%    285.000000   6.500000  4.300000
#    75%    440.000000   8.750000  4.575000
#    max    600.000000  14.000000  4.700000

"""
Remarquez que "count" vaut 6 pour la note : les valeurs manquantes ne sont pas
comptées.

(La syntaxe df[["places", "salles", "note"]] sélectionne trois colonnes : voir
la section suivante.)
"""


# Sélectionner des colonnes
############################

"""
On sélectionne une colonne avec des crochets et son nom, comme une clé de
dictionnaire. On obtient une Series :
"""
print(df["nom"])
# => 0    Gaumont Bellecour
#    1               Louxor
#    2            Grand Rex
#    3    Mk2 Quai de Loire
#    4         Pathé Wepler
#    5         UGC George V
#    6             Comoedia
#    7         Les Variétés
#    Name: nom, dtype: str
print(type(df["nom"]))  # => <class 'pandas.Series'>
# (Avant pandas 3.0 : <class 'pandas.core.series.Series'>)

# On peut alors utiliser toutes les méthodes des Series :
print(df["places"].sum())   # => 2580 (le nombre total de places)
print(df["ville"].unique())  # les valeurs distinctes de la colonne
# => <StringArray>
#    ['Lyon', 'Paris', 'Marseille']
#    Length: 3, dtype: str

"""
L'affichage de .unique() dépend de la version de pandas. Pour obtenir une
simple liste Python, on utilise list() :
"""
print(list(df["ville"].unique()))  # => ['Lyon', 'Paris', 'Marseille']

# .value_counts() compte le nombre d'occurrences de chaque valeur :
print(df["ville"].value_counts())
# => ville
#    Paris        5
#    Lyon         2
#    Marseille    1
#    Name: count, dtype: int64

"""
Pour sélectionner PLUSIEURS colonnes, on passe une LISTE de noms (d'où les
doubles crochets). On obtient un nouveau DataFrame :
"""
print(df[["nom", "places"]])
# =>                  nom  places
#    0  Gaumont Bellecour     200
#    1             Louxor     420
#    2          Grand Rex     600
#    3  Mk2 Quai de Loire     320
#    4       Pathé Wepler     500
#    5       UGC George V     110
#    6           Comoedia     250
#    7       Les Variétés     180

# Une colonne qui n'existe pas soulève une KeyError, comme un dictionnaire :
try:
    df["capacite"]
except KeyError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err!r})")


# Sélectionner des lignes : loc et iloc
########################################

"""
Pour sélectionner des lignes (et éventuellement des colonnes), pandas propose
deux outils, à ne pas confondre :
    - .iloc[…] ("integer location") : sélection par POSITION (0, 1, 2…),
      exactement comme les indices d'une liste,
    - .loc[…] ("location") : sélection par INDEX (l'étiquette de la ligne) et
      par NOM de colonne.

Tant que l'index est 0, 1, 2…, les deux semblent faire la même chose. Mais la
différence apparaît dès qu'on change l'index ou qu'on trie le tableau !
"""

# .iloc[n] retourne la ligne en position n (sous forme de Series)
print(df.iloc[0])
# => id                       26
#    nom       Gaumont Bellecour
#    ville                  Lyon
#    places                  200
#    salles                    6
#    note                    4.1
#    Name: 0, dtype: object

# .iloc accepte les slices (cf. chap. 31) : stop est exclu, comme d'habitude
print(df.iloc[1:3])
# =>    id        nom  ville  places  salles  note
#    1  12     Louxor  Paris     420       3   4.7
#    2  35  Grand Rex  Paris     600       7   4.5

# Avec deux paramètres : [lignes, colonnes], toujours par position
print(df.iloc[0:2, 1:3])
# =>                  nom  ville
#    0  Gaumont Bellecour   Lyon
#    1             Louxor  Paris

"""
Pour bien voir la différence avec .loc, on utilise la colonne "nom" comme
index, avec .set_index(). Cette méthode ne modifie pas df : elle retourne un
nouveau DataFrame.
"""
df_nom = df.set_index("nom")
print(df_nom.head(3))
# =>                    id  ville  places  salles  note
#    nom
#    Gaumont Bellecour  26   Lyon     200       6   4.1
#    Louxor             12  Paris     420       3   4.7
#    Grand Rex          35  Paris     600       7   4.5

# .loc sélectionne alors par nom de cinéma (l'index) et par nom de colonne :
print(df_nom.loc["Louxor", "places"])  # => 420
print(df_nom.loc["Grand Rex"]["ville"])  # => Paris

# ATTENTION : avec .loc, les slices INCLUENT la borne de fin !
print(df_nom.loc["Louxor":"Mk2 Quai de Loire", ["ville", "places"]])
# =>                    ville  places
#    nom
#    Louxor             Paris     420
#    Grand Rex          Paris     600
#    Mk2 Quai de Loire  Paris     320

# Une étiquette inconnue soulève une KeyError :
try:
    df_nom.loc["Cinéma imaginaire"]
except KeyError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err!r})")


# Filtrer les lignes
#####################

"""
IMPT : c'est l'opération la plus utilisée de pandas. Pour garder seulement les
lignes qui vérifient une condition, on procède en deux temps :
    1. on écrit une condition sur une colonne : on obtient une Series de
       booléens (un "masque"), avec True pour les lignes à garder,
    2. on passe ce masque entre crochets au DataFrame.
"""
masque = df["places"] > 300
print(list(masque))  # => [False, True, True, True, True, False, False, False]

print(df[masque])
# =>    id                nom  ville  places  salles  note
#    1  12             Louxor  Paris     420       3   4.7
#    2  35          Grand Rex  Paris     600       7   4.5
#    3   4  Mk2 Quai de Loire  Paris     320       4   NaN
#    4  81       Pathé Wepler  Paris     500      14   3.9

# On écrit généralement les deux étapes en une seule ligne :
print(df[df["ville"] == "Lyon"])
# =>    id                nom ville  places  salles  note
#    0  26  Gaumont Bellecour  Lyon     200       6   4.1
#    6   7           Comoedia  Lyon     250       8   4.6

"""
Pour combiner plusieurs conditions, ATTENTION : on n'utilise pas "and", "or" et
"not" (cf. chap. 9), mais les opérateurs bit à bit "&", "|" et "~" (cf.
chap. 21). Et chaque condition doit être entre parenthèses !

Exemple, comme au chap. 28 : les cinémas ayant plus de 4 salles ET moins de
500 places :
"""
print(df[(df["salles"] > 4) & (df["places"] < 500)])
# =>    id                nom      ville  places  salles  note
#    0  26  Gaumont Bellecour       Lyon     200       6   4.1
#    5  10       UGC George V      Paris     110      11   3.6
#    6   7           Comoedia       Lyon     250       8   4.6
#    7  53       Les Variétés  Marseille     180       5   NaN

# Avec "and", Python ne sait pas convertir une Series entière en un seul
# booléen, et soulève une erreur :
try:
    df[(df["salles"] > 4) and (df["places"] < 500)]
except ValueError as err:
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {err})")

# .isin() teste l'appartenance à une liste (équivalent de "in") :
print(df[df["ville"].isin(["Lyon", "Marseille"])]["nom"].tolist())
# => ['Gaumont Bellecour', 'Comoedia', 'Les Variétés']

"""
On peut aussi filtrer et choisir les colonnes en même temps avec .loc :
"""
print(df.loc[df["note"] > 4.4, ["nom", "note"]])
# =>          nom  note
#    1     Louxor   4.7
#    2  Grand Rex   4.5
#    6   Comoedia   4.6


# Les valeurs manquantes : NaN
###############################

"""
NaN signifie "Not a Number" (pas un nombre). C'est la valeur qu'utilise pandas
quand une valeur n'a pas été renseignée (une case vide dans le CSV, une mesure
manquante…). C'est l'équivalent de None (cf. chap. 15) pour les données.

Les données réelles ont presque toujours des valeurs manquantes : il faut
savoir les repérer et décider quoi en faire.
"""

# .isna() retourne un masque : True là où la valeur est manquante
print(df["note"].isna().tolist())
# => [False, False, False, True, False, False, False, True]

# Combien de valeurs manquantes par colonne ? (True compte pour 1, cf. chap. 21)
print(df.isna().sum())
# => id        0
#    nom       0
#    ville     0
#    places    0
#    salles    0
#    note      2
#    dtype: int64

# Quels cinémas n'ont pas de note ?
print(df[df["note"].isna()]["nom"].tolist())  # => ['Mk2 Quai de Loire', 'Les Variétés']

"""
Attention : NaN n'est égal à rien, même pas à lui-même ! On ne peut donc pas
tester "== NaN" : on utilise toujours .isna() (ou .notna() pour l'inverse).
"""
nan = float("nan")
print(nan == nan)  # => False (!)

"""
Les fonctions statistiques de pandas ignorent les NaN : la moyenne est
calculée sur les 6 notes connues.
"""
print(round(df["note"].mean(), 2))  # => 4.23

"""
Deux stratégies principales pour traiter les NaN :
    1. supprimer les lignes concernées, avec .dropna(),
    2. remplacer les NaN par une valeur, avec .fillna(valeur).
Ces méthodes retournent un nouveau DataFrame (ou une nouvelle Series) : df
n'est pas modifié.
"""
print(df.dropna().shape)  # => (6, 6) (il reste 6 lignes)

notes_completees = df["note"].fillna(0)
print(notes_completees.tolist())  # => [4.1, 4.7, 4.5, 0.0, 3.9, 3.6, 4.6, 0.0]

"""
Remplacer par 0 fausse la moyenne ! On préfère souvent remplacer par la
moyenne ou la médiane de la colonne :
"""
notes_completees = df["note"].fillna(df["note"].median())
print(notes_completees.tolist())  # => [4.1, 4.7, 4.5, 4.3, 3.9, 3.6, 4.6, 4.3]

print(df.shape)  # => (8, 6) (df n'a pas été modifié)


# Ajouter et modifier des colonnes
###################################

"""
On crée une nouvelle colonne en lui affectant une valeur, comme pour une clé de
dictionnaire (cf. chap. 18). Les calculs entre colonnes se font ligne à ligne,
sans boucle :
"""
df["places_par_salle"] = df["places"] / df["salles"]
print(df[["nom", "places", "salles", "places_par_salle"]].head(3))
# =>                  nom  places  salles  places_par_salle
#    0  Gaumont Bellecour     200       6         33.333333
#    1             Louxor     420       3        140.000000
#    2          Grand Rex     600       7         85.714286

# On peut arrondir une colonne avec .round() :
df["places_par_salle"] = df["places_par_salle"].round(1)
print(df["places_par_salle"].tolist())
# => [33.3, 140.0, 85.7, 80.0, 35.7, 10.0, 31.2, 36.0]

# Une colonne à partir d'une condition (une colonne de booléens) :
df["grand"] = df["places"] >= 400
print(df[["nom", "grand"]].head(3))
# =>                  nom  grand
#    0  Gaumont Bellecour  False
#    1             Louxor   True
#    2          Grand Rex   True

"""
Les strings d'une colonne de texte ont des méthodes accessibles via ".str",
qui s'appliquent à toutes les valeurs (cf. chap. 8 pour les méthodes de
strings) :
"""
print(df["ville"].str.upper().tolist())
# => ['LYON', 'PARIS', 'PARIS', 'PARIS', 'PARIS', 'PARIS', 'LYON', 'MARSEILLE']

"""
Pour appliquer sa propre fonction (cf. chap. 14) à chaque valeur d'une
colonne, on utilise .apply() :
"""
def categorie(nb_places):
    if nb_places < 200:
        return "petit"
    elif nb_places < 450:
        return "moyen"
    else:
        return "grand"


df["categorie"] = df["places"].apply(categorie)
print(df[["nom", "places", "categorie"]])
# =>                  nom  places categorie
#    0  Gaumont Bellecour     200     moyen
#    1             Louxor     420     moyen
#    2          Grand Rex     600     grand
#    3  Mk2 Quai de Loire     320     moyen
#    4       Pathé Wepler     500     grand
#    5       UGC George V     110     petit
#    6           Comoedia     250     moyen
#    7       Les Variétés     180     petit

# Pour renommer des colonnes, on passe un dictionnaire {ancien: nouveau} :
df = df.rename(columns={"salles": "nb_salles"})

# Pour supprimer des colonnes, on utilise .drop(columns=[…]) :
df = df.drop(columns=["grand", "places_par_salle"])
print(list(df.columns))
# => ['id', 'nom', 'ville', 'places', 'nb_salles', 'note', 'categorie']

"""
Remarquez le "df = df.rename(…)" : comme la plupart des méthodes de pandas,
.rename() et .drop() retournent un NOUVEAU DataFrame. Sans réaffectation, df
ne serait pas modifié.
"""


# Trier
########

"""
.sort_values(colonne) trie les lignes selon une colonne (par ordre croissant
par défaut, ou décroissant avec ascending=False). Comme sorted() (cf.
chap. 24), elle retourne un nouveau DataFrame trié.
"""
print(df.sort_values("places", ascending=False)[["nom", "places"]])
# =>                  nom  places
#    2          Grand Rex     600
#    4       Pathé Wepler     500
#    1             Louxor     420
#    3  Mk2 Quai de Loire     320
#    6           Comoedia     250
#    0  Gaumont Bellecour     200
#    7       Les Variétés     180
#    5       UGC George V     110

"""
Remarquez que l'index suit les lignes : il n'est plus dans l'ordre. C'est
justement là que .loc et .iloc diffèrent (cf. plus haut) :
"""
df_trie = df.sort_values("places", ascending=False)
print(df_trie.iloc[0]["nom"])  # => Grand Rex (la 1re ligne en POSITION)
print(df_trie.loc[0]["nom"])   # => Gaumont Bellecour (la ligne d'INDEX 0)

# On peut trier sur plusieurs colonnes : d'abord par ville, puis par note
# décroissante au sein de chaque ville. Les NaN sont placés à la fin.
print(df.sort_values(["ville", "note"], ascending=[True, False])[["ville", "nom", "note"]])
# =>        ville                nom  note
#    6       Lyon           Comoedia   4.6
#    0       Lyon  Gaumont Bellecour   4.1
#    7  Marseille       Les Variétés   NaN
#    1      Paris             Louxor   4.7
#    2      Paris          Grand Rex   4.5
#    4      Paris       Pathé Wepler   3.9
#    5      Paris       UGC George V   3.6
#    3      Paris  Mk2 Quai de Loire   NaN

# .nlargest(n, colonne) est un raccourci pour obtenir les n plus grandes valeurs
print(df.nlargest(2, "nb_salles")["nom"].tolist())  # => ['Pathé Wepler', 'UGC George V']


# Regrouper : groupby
######################

"""
IMPT : .groupby() est la fonction "Tableau Croisé Dynamique" de pandas. Elle
permet de répondre à des questions comme : "quel est le nombre total de places
PAR ville ?"

Le fonctionnement se fait en trois étapes ("split-apply-combine") :
    1. on découpe le tableau en groupes, selon les valeurs d'une colonne (ici,
       un groupe par ville),
    2. on applique un calcul à chaque groupe (somme, moyenne, comptage…),
    3. on rassemble les résultats dans un nouveau tableau.
"""
print(df.groupby("ville")["places"].sum())
# => ville
#    Lyon          450
#    Marseille     180
#    Paris        1950
#    Name: places, dtype: int64

# La note moyenne par ville (les NaN sont ignorés) :
print(df.groupby("ville")["note"].mean().round(2))
# => ville
#    Lyon         4.35
#    Marseille     NaN
#    Paris        4.18
#    Name: note, dtype: float64

"""
Pour Marseille, la seule note est manquante : la moyenne est donc NaN.

Avec .agg(), on peut calculer plusieurs statistiques d'un coup, sur une ou
plusieurs colonnes :
"""
print(df.groupby("ville").agg(
    nb_cinemas=("nom", "count"),
    places_totales=("places", "sum"),
    salles_max=("nb_salles", "max"),
))
# =>            nb_cinemas  places_totales  salles_max
#    ville
#    Lyon                2             450           8
#    Marseille           1             180           5
#    Paris               5            1950          14
# (Cette syntaxe d'.agg() nécessite pandas 0.25+.)

# On peut regrouper selon une colonne calculée, comme notre "categorie" :
print(df.groupby("categorie")["nb_salles"].sum())
# => categorie
#    grand    21
#    moyen    21
#    petit    16
#    Name: nb_salles, dtype: int64


# Exporter et nettoyer
#######################

"""
Une fois les données traitées, on peut les sauvegarder dans un fichier CSV avec
.to_csv(). Le paramètre index=False évite d'écrire l'index (0, 1, 2…) comme
une colonne supplémentaire.

pandas sait aussi écrire et lire bien d'autres formats : Excel (.to_excel(),
pd.read_excel()), JSON (.to_json(), pd.read_json()), SQL…
"""
resultat = df[df["ville"] == "Paris"].sort_values("note", ascending=False)
resultat.to_csv("cinemas_paris.csv", index=False)

# On vérifie le contenu du fichier en le relisant comme du texte (cf. chap. 28)
with open("cinemas_paris.csv", "r", encoding="utf-8") as f:
    print(f.read(), end="")
# => id,nom,ville,places,nb_salles,note,categorie
#    12,Louxor,Paris,420,3,4.7,moyen
#    35,Grand Rex,Paris,600,7,4.5,grand
#    81,Pathé Wepler,Paris,500,14,3.9,grand
#    10,UGC George V,Paris,110,11,3.6,petit
#    4,Mk2 Quai de Loire,Paris,320,4,,moyen

"""
Remarquez que le NaN est réécrit comme une case vide.

Enfin, comme au chap. 28, on supprime les fichiers créés par ce chapitre pour
laisser le répertoire propre :
"""
for nom_fichier in ["cinemas.csv", "cinemas_paris.csv"]:
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)

"""
Pour aller plus loin :
    - la documentation officielle, et son tutoriel "10 minutes to pandas" :
      https://pandas.pydata.org/docs/user_guide/10min.html
    - pandas fonctionne main dans la main avec NumPy (calcul numérique) et
      matplotlib (graphiques) : df["places"].plot() trace directement un
      graphique, si matplotlib est installé.
"""
