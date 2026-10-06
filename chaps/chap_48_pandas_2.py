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
#  Chap. 48     #  Pandas II                                                   #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Installer et importer pandas
#  - L'index : set_index et reset_index
#  - Empiler des tables : concat
#  - Joindre des tables : merge
#  - Les pièges des jointures
#  - Remodeler : pivot, pivot_table et melt
#  - Compter les combinaisons : crosstab
#  - groupby avancé
#  - Les dates : to_datetime et .dt
#  - Les séries temporelles : resample, rolling, shift
#  - Les textes : l'accesseur .str
#  - Nettoyer des données
#  - Créer des classes : cut et qcut
#  - apply ou vectorisation ?
#  - Enchaîner les méthodes : assign et pipe
#  - Lire et écrire d'autres formats
#  - Cas pratique : analyser des ventes
#  - Nettoyage final
#
##############################

# Introduction
###############

"""
Au chap. 39, on a appris à charger UN tableau, à le filtrer, le trier et le
regrouper. Mais dans la vraie vie, les données sont rarement aussi sages :
    - elles sont réparties dans PLUSIEURS tables, qu'il faut assembler (les
      clients dans un fichier, les commandes dans un autre…),
    - elles n'ont pas toujours la bonne forme (une colonne par mois, alors
      qu'on voudrait une ligne par mois…),
    - elles contiennent des dates, des textes mal saisis, des doublons, des
      valeurs absentes ou absurdes.

On dit souvent qu'un·e data scientist passe 80 % de son temps à préparer les
données, et 20 % à les analyser. Ce chapitre est consacré à ces 80 % !

Il suppose que vous maîtrisez le chap. 39 (Series, DataFrame, loc/iloc,
filtres, groupby). On s'appuiera aussi sur lambda (cf. chap. 32), numpy (cf.
chap. 38) et, pour une section, sur les expressions régulières (cf. chap. 42).

Note : ce chapitre a été vérifié avec pandas 3.0. Quelques affichages diffèrent
avec pandas 2.x (types "str" affichés "object", dates en "[ns]" au lieu de
"[us]"…) : c'est signalé à chaque fois.
"""


# Installer et importer pandas
###############################

"""
Comme au chap. 39, on protège l'import : si pandas n'est pas installé, le
programme affiche un message et s'arrête proprement.

Pour installer pandas dans un projet géré avec uv (cf. chap. 47) :
    ?> uv add pandas
ou, avec pip :
    ?> pip install pandas
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

print(pd.__version__)  # => 3.0.6 (variable : dépend de votre installation)

"""
On reprend le tableau des cinémas du chap. 39. Cette fois, on le crée
directement à partir d'un dictionnaire de listes (cf. chap. 39, section "Les
DataFrames") :
"""
cinemas = pd.DataFrame({
    "nom": ["Gaumont Bellecour", "Louxor", "Grand Rex", "Mk2 Quai de Loire",
            "Pathé Wepler", "UGC George V", "Comoedia", "Les Variétés"],
    "ville": ["Lyon", "Paris", "Paris", "Paris", "Paris", "Paris", "Lyon",
              "Marseille"],
    "places": [200, 420, 600, 320, 500, 110, 250, 180],
    "salles": [6, 3, 7, 4, 14, 11, 8, 5],
    "note": [4.1, 4.7, 4.5, None, 3.9, 3.6, 4.6, None],
})
print(cinemas)
# =>                  nom      ville  places  salles  note
#    0  Gaumont Bellecour       Lyon     200       6   4.1
#    1             Louxor      Paris     420       3   4.7
#    2          Grand Rex      Paris     600       7   4.5
#    3  Mk2 Quai de Loire      Paris     320       4   NaN
#    4       Pathé Wepler      Paris     500      14   3.9
#    5       UGC George V      Paris     110      11   3.6
#    6           Comoedia       Lyon     250       8   4.6
#    7       Les Variétés  Marseille     180       5   NaN


# L'index : set_index et reset_index
#####################################

"""
Jusqu'ici, l'index de nos tableaux était 0, 1, 2… (cf. chap. 39). Mais l'index
peut être n'importe quelle colonne qui identifie les lignes : un nom, un
identifiant, une date…

.set_index(colonne) transforme une colonne en index. Comme toujours en pandas,
la méthode retourne un NOUVEAU DataFrame (cf. chap. 39) :
"""
par_nom = cinemas.set_index("nom")
print(par_nom.head(3))
# =>                    ville  places  salles  note
#    nom
#    Gaumont Bellecour   Lyon     200       6   4.1
#    Louxor             Paris     420       3   4.7
#    Grand Rex          Paris     600       7   4.5

"""
Remarquez la ligne "nom" sous les noms de colonnes : c'est le nom de l'index.
On peut maintenant accéder à une ligne par son nom avec .loc, comme on le
ferait dans un dictionnaire (cf. chap. 18) :
"""
print(par_nom.loc["Louxor", "places"])  # => 420
print(par_nom.loc["Grand Rex", "ville"])  # => Paris

"""
.reset_index() fait l'inverse : l'index redevient une colonne ordinaire, et un
nouvel index 0, 1, 2… est créé. C'est très utile après un groupby, dont le
résultat a pour index la colonne de regroupement (cf. chap. 39) :
"""
places_par_ville = cinemas.groupby("ville")["places"].sum()
print(places_par_ville)
# => ville
#    Lyon          450
#    Marseille     180
#    Paris        1950
#    Name: places, dtype: int64
print(places_par_ville.reset_index())
# =>        ville  places
#    0       Lyon     450
#    1  Marseille     180
#    2      Paris    1950

"""
On peut aussi indexer par PLUSIEURS colonnes : on obtient un "MultiIndex"
(index à plusieurs niveaux). Les lignes sont alors repérées par un tuple (cf.
chap. 17) :
"""
multi = cinemas.set_index(["ville", "nom"])[["places"]].sort_index()
print(multi)
# =>                              places
#    ville     nom
#    Lyon      Comoedia              250
#              Gaumont Bellecour     200
#    Marseille Les Variétés          180
#    Paris     Grand Rex             600
#              Louxor                420
#              Mk2 Quai de Loire     320
#              Pathé Wepler          500
#              UGC George V          110

"""
L'affichage n'écrit le nom de la ville qu'une fois par groupe, pour être plus
lisible. Avec .loc, on peut sélectionner un niveau entier, ou une ligne précise
grâce à un tuple :
"""
print(multi.loc["Lyon"])
# =>                    places
#    nom
#    Comoedia              250
#    Gaumont Bellecour     200
print(multi.loc[("Paris", "Louxor"), "places"])  # => 420

"""
IMPT : le MultiIndex est puissant mais vite déroutant. En cas de doute,
.reset_index() ramène toujours à un tableau "plat", plus facile à manipuler.
"""


# Empiler des tables : concat
##############################

"""
Premier cas d'assemblage : on a plusieurs tableaux qui ont les MÊMES colonnes,
et on veut les mettre bout à bout. Par exemple, les inscriptions de janvier et
celles de février, stockées dans deux fichiers.

pd.concat() prend une LISTE de DataFrames et les empile verticalement :
"""
janvier = pd.DataFrame({"eleve": ["Alice", "Bob"], "note": [15, 8]})
fevrier = pd.DataFrame({"eleve": ["Chloé", "David"], "note": [12, 17]})
print(pd.concat([janvier, fevrier]))
# =>    eleve  note
#    0  Alice    15
#    1    Bob     8
#    0  Chloé    12
#    1  David    17

"""
Remarquez l'index : 0, 1, 0, 1. Chaque tableau a gardé son propre index, ce qui
crée des doublons (et .loc[0] retournerait deux lignes !). Le paramètre
ignore_index=True recrée un index propre :
"""
inscriptions = pd.concat([janvier, fevrier], ignore_index=True)
print(inscriptions)
# =>    eleve  note
#    0  Alice    15
#    1    Bob     8
#    2  Chloé    12
#    3  David    17

"""
Si les colonnes ne sont pas exactement les mêmes, pandas aligne les colonnes
par leur NOM, et remplit les cases manquantes avec NaN :
"""
mars = pd.DataFrame({"eleve": ["Emma"], "note": [14], "option": ["latin"]})
print(pd.concat([janvier, mars], ignore_index=True))
# =>    eleve  note option
#    0  Alice    15    NaN
#    1    Bob     8    NaN
#    2   Emma    14  latin

"""
Enfin, avec axis=1 (cf. chap. 38 pour le paramètre axis), concat colle les
tableaux côte à côte, en alignant les lignes par leur index :
"""
oral = pd.DataFrame({"oral": [11, 13]})
print(pd.concat([janvier, oral], axis=1))
# =>    eleve  note  oral
#    0  Alice    15    11
#    1    Bob     8    13


# Joindre des tables : merge
#############################

"""
Deuxième cas, beaucoup plus fréquent : les informations sont réparties dans
plusieurs tables qui partagent une colonne commune, appelée "clé".

Exemple : une boutique en ligne stocke ses clients dans une table, et ses
commandes dans une autre. Chaque commande contient le numéro du client
(client_id), mais pas son nom : on évite ainsi de recopier le nom dans chaque
commande (même idée que la "source unique de vérité" du chap. 14).
"""
clients = pd.DataFrame({
    "client_id": [1, 2, 3],
    "nom": ["Alice", "Bob", "Chloé"],
})
commandes = pd.DataFrame({
    "commande": [101, 102, 103, 104],
    "client_id": [1, 1, 3, 4],
    "montant": [30, 12, 50, 8],
})

"""
Observez bien ces deux tables :
    - Alice (client 1) a passé deux commandes, Chloé (client 3) une seule,
    - Bob (client 2) n'a rien commandé,
    - la commande 104 vient d'un client 4… qui n'existe pas dans la table des
      clients (une erreur de saisie, ou un client supprimé).

pd.merge(gauche, droite, on=clé) associe chaque ligne de gauche aux lignes de
droite qui ont la même valeur de clé. C'est l'équivalent du JOIN en SQL.

La question est : que faire des lignes qui n'ont PAS de correspondance (Bob et
la commande 104) ? C'est le rôle du paramètre how=…, qui a 4 valeurs.

1. how="inner" (par défaut) : on ne garde que les lignes qui ont une
correspondance des DEUX côtés. Bob et la commande 104 disparaissent.
"""
print(pd.merge(clients, commandes, on="client_id"))
# =>    client_id    nom  commande  montant
#    0          1  Alice       101       30
#    1          1  Alice       102       12
#    2          3  Chloé       103       50

"""
Remarquez qu'Alice apparaît deux fois : une fois par commande. La ligne de
gauche est dupliquée autant de fois qu'elle a de correspondances à droite.

2. how="left" : on garde TOUTES les lignes de gauche (tous les clients), même
sans commande. Les cases sans correspondance sont remplies avec NaN.
"""
print(pd.merge(clients, commandes, on="client_id", how="left"))
# =>    client_id    nom  commande  montant
#    0          1  Alice     101.0     30.0
#    1          1  Alice     102.0     12.0
#    2          2    Bob       NaN      NaN
#    3          3  Chloé     103.0     50.0

"""
Bob est bien là, avec NaN dans les colonnes de commandes. Remarquez que ces
colonnes sont passées en float (101.0…) : comme au chap. 39, NaN est un float,
et une colonne d'entiers qui contient un NaN devient une colonne de floats.

IMPT : how="left" est la jointure la plus utilisée : "je pars de ma table
principale, et je lui ajoute des informations".

3. how="right" : l'inverse, on garde toutes les lignes de droite (toutes les
commandes), même celles dont le client est inconnu.
"""
print(pd.merge(clients, commandes, on="client_id", how="right"))
# =>    client_id    nom  commande  montant
#    0          1  Alice       101       30
#    1          1  Alice       102       12
#    2          3  Chloé       103       50
#    3          4    NaN       104        8

"""
4. how="outer" : on garde tout, des deux côtés.

Le paramètre indicator=True ajoute une colonne "_merge" qui indique d'où vient
chaque ligne : "both" (les deux tables), "left_only" ou "right_only". C'est
l'outil idéal pour repérer les lignes orphelines :
"""
complet = pd.merge(clients, commandes, on="client_id", how="outer",
                   indicator=True)
print(complet)
# =>    client_id    nom  commande  montant      _merge
#    0          1  Alice     101.0     30.0        both
#    1          1  Alice     102.0     12.0        both
#    2          2    Bob       NaN      NaN   left_only
#    3          3  Chloé     103.0     50.0        both
#    4          4    NaN     104.0      8.0  right_only
orphelines = complet[complet["_merge"] == "right_only"]
print(orphelines["commande"].tolist())  # => [104.0]

"""
En résumé, si l'on représente chaque table par un cercle, et l'ensemble des
clés communes par leur intersection (cf. les ensembles, chap. 25) :

    how="inner"  →  l'intersection des clés  (G & D)
    how="left"   →  toutes les clés de gauche
    how="right"  →  toutes les clés de droite
    how="outer"  →  l'union des clés  (G | D)

Quand la clé ne porte pas le même nom dans les deux tables, on utilise
left_on=… et right_on=… :
"""
produits = pd.DataFrame({"ref": ["A1", "B2"], "libelle": ["Stylo", "Cahier"]})
lignes = pd.DataFrame({"produit": ["B2", "A1", "B2"], "quantite": [3, 1, 2]})
print(pd.merge(lignes, produits, left_on="produit", right_on="ref"))
# =>   produit  quantite ref libelle
#    0      B2         3  B2  Cahier
#    1      A1         1  A1   Stylo
#    2      B2         2  B2  Cahier

"""
Les deux colonnes de clé sont conservées : on peut supprimer la colonne en
double avec .drop(columns="ref") (cf. chap. 39).

Enfin, la méthode .join() est un raccourci pour joindre deux tables sur leur
INDEX (au lieu d'une colonne). Elle fait une jointure "left" par défaut :
"""
infos = pd.DataFrame({"region": ["ARA", "IDF"]}, index=["Lyon", "Paris"])
print(cinemas.set_index("ville")[["nom"]].join(infos).head(4))
# =>                      nom region
#    ville
#    Lyon   Gaumont Bellecour    ARA
#    Paris             Louxor    IDF
#    Paris          Grand Rex    IDF
#    Paris  Mk2 Quai de Loire    IDF

"""
Marseille n'a pas de région dans "infos" : avec la jointure left, la ligne est
gardée avec NaN (elle n'apparaît pas ici car on n'affiche que 4 lignes).
"""


# Les pièges des jointures
###########################

"""
Les jointures sont la première source de bugs silencieux en analyse de
données. Trois pièges à connaître.

Piège 1 : les noms de colonnes en double. Si les deux tables ont une colonne
de même nom qui n'est pas la clé, pandas ajoute les suffixes _x et _y. On peut
choisir des suffixes plus parlants avec suffixes=(…, …) :
"""
notes_2023 = pd.DataFrame({"ville": ["Lyon", "Paris"], "note": [4.1, 4.3]})
notes_2024 = pd.DataFrame({"ville": ["Lyon", "Paris"], "note": [4.4, 4.2]})
print(pd.merge(notes_2023, notes_2024, on="ville"))
# =>    ville  note_x  note_y
#    0   Lyon     4.1     4.4
#    1  Paris     4.3     4.2
print(pd.merge(notes_2023, notes_2024, on="ville",
               suffixes=("_2023", "_2024")))
# =>    ville  note_2023  note_2024
#    0   Lyon        4.1        4.4
#    1  Paris        4.3        4.2

"""
Piège 2 : les clés en double des DEUX côtés. Si une clé apparaît 2 fois à
gauche et 2 fois à droite, chaque ligne de gauche est associée à chaque ligne
de droite : on obtient 2 × 2 = 4 lignes ! Avec de vraies données, le nombre de
lignes peut exploser sans prévenir.
"""
gauche = pd.DataFrame({"ville": ["Paris", "Paris"], "cinema": ["Louxor",
                                                              "Grand Rex"]})
droite = pd.DataFrame({"ville": ["Paris", "Paris"], "musee": ["Louvre",
                                                             "Orsay"]})
print(pd.merge(gauche, droite, on="ville"))
# =>    ville     cinema   musee
#    0  Paris     Louxor  Louvre
#    1  Paris     Louxor   Orsay
#    2  Paris  Grand Rex  Louvre
#    3  Paris  Grand Rex   Orsay

"""
IMPT : après une jointure, vérifiez TOUJOURS le nombre de lignes (len() ou
.shape). S'il a augmenté alors que vous ne vous y attendiez pas, c'est qu'une
clé est en double.

Piège 3 (le remède) : le paramètre validate=… demande à pandas de vérifier la
relation entre les deux tables, et de lever une erreur si elle n'est pas
respectée :
    - "one_to_one" : chaque clé est unique des deux côtés,
    - "one_to_many" : unique à gauche (ex. : un client → plusieurs commandes),
    - "many_to_one" : unique à droite (ex. : plusieurs commandes → un client).
"""
try:
    pd.merge(clients, commandes, on="client_id", validate="one_to_one")
except pd.errors.MergeError as err:
    # On n'affiche que la 1re ligne du message, qui est assez long
    message = str(err).splitlines()[0]
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {message})")
# => 2: (Sans ce try: … except …, cette ligne créerait : Merge keys are not
#    unique in right dataset; not a one-to-one merge)

# Avec la bonne relation, tout se passe bien :
ok = pd.merge(clients, commandes, on="client_id", validate="one_to_many")
print(len(ok))  # => 3


# Remodeler : pivot, pivot_table et melt
#########################################

"""
Un même jeu de données peut être rangé de deux façons :

    - au format LARGE ("wide") : une ligne par élève, une colonne par matière.
      C'est le format agréable à lire pour un humain, comme un bulletin.

          eleve  maths  physique
          Alice     15        12
          Bob        8        11

    - au format LONG ("long") : une ligne par MESURE (un élève, une matière,
      une note). C'est le format préféré des outils d'analyse et de
      visualisation (groupby, seaborn au chap. 50…).

          eleve  matiere   note
          Alice  maths       15
          Bob    maths        8
          Alice  physique    12
          Bob    physique    11

.melt() passe du format large au format long. On lui indique :
    - id_vars : les colonnes qui identifient la ligne (à garder telles quelles),
    - var_name : le nom de la nouvelle colonne qui contiendra les anciens noms
      de colonnes,
    - value_name : le nom de la nouvelle colonne qui contiendra les valeurs.
"""
bulletin = pd.DataFrame({
    "eleve": ["Alice", "Bob"],
    "maths": [15, 8],
    "physique": [12, 11],
})
long = bulletin.melt(id_vars="eleve", var_name="matiere", value_name="note")
print(long)
# =>    eleve   matiere  note
#    0  Alice     maths    15
#    1    Bob     maths     8
#    2  Alice  physique    12
#    3    Bob  physique    11

# Au format long, la moyenne par matière est un simple groupby :
print(long.groupby("matiere")["note"].mean())
# => matiere
#    maths       11.5
#    physique    11.5
#    Name: note, dtype: float64

"""
.pivot() fait le chemin inverse (format long → format large). On indique :
    - index : ce qui devient les lignes,
    - columns : la colonne dont les VALEURS deviennent des noms de colonnes,
    - values : la colonne qui remplit le tableau.
"""
print(long.pivot(index="eleve", columns="matiere", values="note"))
# => matiere  maths  physique
#    eleve
#    Alice       15        12
#    Bob          8        11

"""
.pivot() exige que chaque couple (ligne, colonne) soit unique : il ne sait pas
quoi faire si deux valeurs tombent dans la même case.
"""
ventes = pd.DataFrame({
    "mois": ["2024-01", "2024-01", "2024-02", "2024-02", "2024-01"],
    "magasin": ["Lyon", "Paris", "Lyon", "Paris", "Lyon"],
    "ca": [100, 250, 120, 230, 30],
})
try:
    # Lyon a DEUX lignes pour 2024-01 (100 et 30) : quelle valeur choisir ?
    ventes.pivot(index="magasin", columns="mois", values="ca")
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 3: (Sans ce try: … except …, cette ligne créerait : Index contains
#    duplicate entries, cannot reshape)

"""
C'est là qu'intervient .pivot_table() : c'est un pivot qui AGRÈGE les valeurs
qui tombent dans la même case, avec la fonction donnée dans aggfunc ("sum",
"mean", "count", "max"…). C'est exactement le Tableau Croisé Dynamique
d'Excel.
"""
print(ventes.pivot_table(index="magasin", columns="mois", values="ca",
                         aggfunc="sum"))
# => mois     2024-01  2024-02
#    magasin
#    Lyon         130      120
#    Paris        250      230

"""
Les 100 + 30 de Lyon en janvier ont bien été additionnés. Avec margins=True,
on ajoute les totaux des lignes et des colonnes :
"""
print(ventes.pivot_table(index="magasin", columns="mois", values="ca",
                         aggfunc="sum", margins=True, margins_name="Total"))
# => mois     2024-01  2024-02  Total
#    magasin
#    Lyon         130      120    250
#    Paris        250      230    480
#    Total        380      350    730

"""
Bonus : .stack() et .unstack() font passer un niveau d'index des colonnes aux
lignes (stack, "empiler") et inversement (unstack, "dépiler"). Le résultat de
.stack() est une Series à MultiIndex :
"""
empile = bulletin.set_index("eleve").stack()
print(empile)
# => eleve
#    Alice  maths       15
#           physique    12
#    Bob    maths        8
#           physique    11
#    dtype: int64
print(empile.unstack())
# =>        maths  physique
#    eleve
#    Alice     15        12
#    Bob        8        11


# Compter les combinaisons : crosstab
######################################

"""
pd.crosstab(colonne1, colonne2) compte le nombre de lignes pour chaque
combinaison de valeurs : c'est un "tableau de contingence", très utilisé en
statistiques. Ici, combien de lignes de ventes par magasin et par mois ?
"""
print(pd.crosstab(ventes["magasin"], ventes["mois"]))
# => mois     2024-01  2024-02
#    magasin
#    Lyon           2        1
#    Paris          1        1

"""
Avec normalize="index", on obtient des proportions par ligne plutôt que des
comptes (chaque ligne totalise 1) :
"""
print(pd.crosstab(ventes["magasin"], ventes["mois"],
                  normalize="index").round(2))
# => mois     2024-01  2024-02
#    magasin
#    Lyon        0.67     0.33
#    Paris       0.50     0.50

"""
C'est équivalent à un pivot_table avec aggfunc="count", mais plus court à
écrire.
"""


# groupby avancé
#################

"""
On a vu au chap. 39 le groupby sur une colonne, et .agg() avec des
agrégations nommées. Voici les autres usages courants.

1. Regrouper selon PLUSIEURS colonnes : on passe une liste. Le résultat a un
MultiIndex (cf. plus haut).
"""
cinemas["taille"] = ["petit" if p < 300 else "grand"
                     for p in cinemas["places"]]
print(cinemas.groupby(["ville", "taille"])["places"].sum())
# => ville      taille
#    Lyon       petit      450
#    Marseille  petit      180
#    Paris      grand     1840
#               petit      110
#    Name: places, dtype: int64

"""
Avec as_index=False, les colonnes de regroupement restent des colonnes
ordinaires : le résultat est un tableau "plat", souvent plus pratique (c'est
l'équivalent d'un .reset_index()).
"""
print(cinemas.groupby(["ville", "taille"], as_index=False)["places"].sum())
# =>        ville taille  places
#    0       Lyon  petit     450
#    1  Marseille  petit     180
#    2      Paris  grand    1840
#    3      Paris  petit     110

"""
2. Des agrégations différentes selon les colonnes : on passe à .agg() un
dictionnaire {colonne: fonction ou liste de fonctions}. Les colonnes du
résultat ont alors deux niveaux (colonne, fonction) :
"""
print(cinemas.groupby("ville").agg({"places": "sum",
                                    "note": ["mean", "max"]}))
# =>           places   note
#                 sum   mean  max
#    ville
#    Lyon         450  4.350  4.6
#    Marseille    180    NaN  NaN
#    Paris       1950  4.175  4.7

"""
Les agrégations nommées du chap. 39 (nom=(colonne, fonction)) donnent un
résultat plus lisible, avec un seul niveau de colonnes : préférez-les.

3. .transform() : calculer une valeur PAR GROUPE, mais la renvoyer pour CHAQUE
LIGNE. Le résultat a la même taille que le tableau de départ, ce qui permet de
l'ajouter comme nouvelle colonne.

Exemple : quelle part des places de sa ville représente chaque cinéma ?
"""
total_ville = cinemas.groupby("ville")["places"].transform("sum")
print(total_ville.tolist())  # => [450, 1950, 1950, 1950, 1950, 1950, 450, 180]
cinemas["part_ville"] = (cinemas["places"] / total_ville).round(2)
print(cinemas[["nom", "ville", "places", "part_ville"]])
# =>                  nom      ville  places  part_ville
#    0  Gaumont Bellecour       Lyon     200        0.44
#    1             Louxor      Paris     420        0.22
#    2          Grand Rex      Paris     600        0.31
#    3  Mk2 Quai de Loire      Paris     320        0.16
#    4       Pathé Wepler      Paris     500        0.26
#    5       UGC George V      Paris     110        0.06
#    6           Comoedia       Lyon     250        0.56
#    7       Les Variétés  Marseille     180        1.00

"""
Les Variétés est le seul cinéma de Marseille : il représente 100 % (1.0) des
places de sa ville.

Comparez :
    - .agg("sum") → UNE valeur par groupe (3 lignes ici),
    - .transform("sum") → la valeur du groupe, répétée sur CHAQUE ligne (8).

4. .filter() : garder ou éliminer des groupes ENTIERS, selon une condition sur
le groupe. La fonction (souvent une lambda, cf. chap. 32) reçoit chaque groupe
sous forme de DataFrame, et retourne True (on garde) ou False.

Exemple : ne garder que les villes qui ont au moins 2 cinémas.
"""
grandes_villes = cinemas.groupby("ville").filter(lambda g: len(g) >= 2)
print(len(grandes_villes))  # => 7 (Marseille et son unique cinéma ont disparu)
print(grandes_villes["ville"].unique().tolist())  # => ['Lyon', 'Paris']


# Les dates : to_datetime et .dt
#################################

"""
Dans un fichier CSV, une date n'est qu'une chaîne de caractères : "2024-03-15"
ou "15/03/2024". Pour pouvoir calculer avec (trier, extraire le mois, calculer
une durée…), il faut la convertir en vraie date, comme avec strptime au
chap. 30.

pd.to_datetime() convertit une Series de chaînes en Series de dates :
"""
dates = pd.to_datetime(pd.Series(["2024-03-01", "2024-03-15", "2024-04-02"]))
print(dates)
# => 0   2024-03-01
#    1   2024-03-15
#    2   2024-04-02
#    dtype: datetime64[us]

"""
Le type est maintenant datetime64 (avec pandas 2.x, l'affichage est
"datetime64[ns]" : la précision de stockage est la nanoseconde au lieu de la
microseconde, ça ne change rien pour nous).

IMPT : pour les dates à la française (jour/mois/année), précisez TOUJOURS le
format, avec les mêmes codes que strftime/strptime (cf. chap. 30). Sinon, "01/
03/2024" risque d'être lu comme le 3 janvier (format américain) !
"""
fr = pd.to_datetime(pd.Series(["01/03/2024", "15/03/2024"]),
                    format="%d/%m/%Y")
print(fr.dt.month.tolist())  # => [3, 3] : c'est bien le mois de mars

"""
(On peut aussi écrire dayfirst=True au lieu du format, mais le format explicite
est plus sûr.)

Si une valeur ne peut pas être convertie, to_datetime lève une erreur :
"""
saisies = pd.Series(["2024-03-01", "pas une date", "2024-03-20"])
try:
    pd.to_datetime(saisies)
except ValueError as err:
    message = str(err).split(". ")[0]  # la 1re phrase du message
    print(f"4: (Sans ce try: … except …, cette ligne créerait : {message})")
# => 4: (Sans ce try: … except …, cette ligne créerait : time data "pas une
#    date" doesn't match format "%Y-%m-%d")

"""
Avec errors="coerce" ("forcer"), les valeurs invalides sont remplacées par NaT
("Not a Time"), l'équivalent de NaN pour les dates. On peut ensuite les
repérer avec .isna() (cf. chap. 39) :
"""
converties = pd.to_datetime(saisies, errors="coerce")
print(converties.isna().tolist())  # => [False, True, False]

"""
Une fois converties, les dates donnent accès à l'accesseur .dt, qui permet
d'extraire leurs composantes (comme .str pour les textes, cf. plus bas) :
"""
print(dates.dt.year.tolist())        # => [2024, 2024, 2024]
print(dates.dt.month.tolist())       # => [3, 3, 4]
print(dates.dt.day.tolist())         # => [1, 15, 2]
print(dates.dt.dayofweek.tolist())   # => [4, 4, 1] (0 = lundi, 6 = dimanche)
print(dates.dt.day_name().tolist())  # => ['Friday', 'Friday', 'Tuesday']
# .dt.strftime() formate les dates en texte (codes du chap. 30) :
print(dates.dt.strftime("%d/%m").tolist())  # => ['01/03', '15/03', '02/04']

"""
La différence entre deux dates est une durée (un Timedelta, l'équivalent du
timedelta du chap. 30) :
"""
duree = dates.max() - dates.min()
print(duree)       # => 32 days 00:00:00
print(duree.days)  # => 32

"""
Attention : .dt ne marche QUE sur une colonne de dates. Sur des chaînes, il
lève une erreur (c'est le signe qu'on a oublié to_datetime) :
"""
try:
    pd.Series(["2024-03-01"]).dt.year
except AttributeError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 5: (Sans ce try: … except …, cette ligne créerait : Can only use .dt
#    accessor with datetimelike values)

"""
Enfin, pd.date_range() crée une suite de dates régulières (un peu comme
range() pour les entiers, cf. chap. 13). freq="D" signifie "chaque jour" :
"""
print(pd.date_range("2024-02-27", periods=4, freq="D").strftime("%d/%m")
      .tolist())
# => ['27/02', '28/02', '29/02', '01/03']

"""
Remarquez que pandas connaît le calendrier : 2024 est bissextile, le 29
février existe bien.
"""


# Les séries temporelles : resample, rolling, shift
####################################################

"""
Une "série temporelle" est une suite de mesures dans le temps : le nombre
d'entrées d'un cinéma chaque jour, la température chaque heure, un cours de
bourse… pandas excelle dans ce domaine (il a été créé dans une banque, pour
analyser des données financières).

La clé est de mettre les dates en INDEX. Créons le nombre d'entrées journalier
d'un cinéma sur le 1er trimestre 2024. (Les nombres sont fabriqués par un
calcul pour que le résultat soit le même à chaque exécution.)
"""
jours = pd.date_range("2024-01-01", "2024-03-31", freq="D")
entrees = pd.Series([100 + (i * 37) % 50 for i in range(len(jours))],
                    index=jours, name="entrees")
print(entrees.head())
# => 2024-01-01    100
#    2024-01-02    137
#    2024-01-03    124
#    2024-01-04    111
#    2024-01-05    148
#    Freq: D, Name: entrees, dtype: int64
print(len(entrees))  # => 91 (91 jours : 31 + 29 + 31)

"""
Avec un index de dates, .loc accepte des dates partielles : "2024-02" désigne
tout le mois de février. Et on peut faire des slices de dates (cf. chap. 31),
où, contrairement aux slices habituelles, la date de fin est INCLUSE :
"""
print(entrees.loc["2024-02"].sum())  # => 3635 (total de février)
print(entrees.loc["2024-02-10":"2024-02-12"])
# => 2024-02-10    130
#    2024-02-11    117
#    2024-02-12    104
#    Freq: D, Name: entrees, dtype: int64

"""
1. .resample(fréquence) : c'est un groupby sur des périodes de temps. On
choisit la période, puis l'agrégation :
    - "W" : par semaine (qui se termine le dimanche),
    - "ME" : par mois ("Month End" : chaque période est étiquetée par le
      dernier jour du mois),
    - "YE" : par année, "h" : par heure…
(Avant pandas 2.2, on écrivait "M" et "Y" au lieu de "ME" et "YE".)
"""
par_mois = entrees.resample("ME").sum()
print(par_mois)
# => 2024-01-31    3855
#    2024-02-29    3635
#    2024-03-31    3875
#    Freq: ME, Name: entrees, dtype: int64
print(entrees.resample("W").mean().round(1).head(3))
# => 2024-01-07    125.3
#    2024-01-14    127.1
#    2024-01-21    121.9
#    Freq: W-SUN, Name: entrees, dtype: float64

"""
2. .rolling(n) : la "moyenne glissante" (ou mobile). Pour chaque jour, on
calcule la moyenne des n derniers jours. C'est l'outil de base pour lisser
une courbe trop irrégulière et faire apparaître une tendance (vous l'avez déjà
vu dans les courbes d'épidémies, "moyenne sur 7 jours").
"""
lisse = entrees.rolling(7).mean().round(1)
print(lisse.head(9))
# => 2024-01-01      NaN
#    2024-01-02      NaN
#    2024-01-03      NaN
#    2024-01-04      NaN
#    2024-01-05      NaN
#    2024-01-06      NaN
#    2024-01-07    125.3
#    2024-01-08    126.6
#    2024-01-09    127.9
#    Freq: D, Name: entrees, dtype: float64

"""
Les 6 premiers jours valent NaN : il n'y a pas encore 7 jours de données pour
calculer la moyenne. Le 7 janvier, la valeur est la moyenne du 1er au 7.

3. .shift(n) décale les valeurs de n lignes (vers le bas), et .pct_change()
calcule la variation en pourcentage par rapport à la ligne précédente. Idéal
pour comparer un mois au mois précédent :
"""
evolution = pd.DataFrame({
    "total": par_mois,
    "mois_precedent": par_mois.shift(1),
    "evolution": par_mois.pct_change().round(3),
})
print(evolution)
# =>             total  mois_precedent  evolution
#    2024-01-31   3855             NaN        NaN
#    2024-02-29   3635          3855.0     -0.057
#    2024-03-31   3875          3635.0      0.066

"""
Les entrées ont baissé de 5,7 % en février, puis augmenté de 6,6 % en mars.
(Février a deux jours de moins que janvier : il faudrait comparer des moyennes
journalières pour être honnête ! cf. les bonnes pratiques du chap. 40.)

Attention, resample() exige un index de dates :
"""
try:
    pd.Series([1, 2, 3]).resample("ME").sum()
except TypeError as err:
    print(f"6: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 6: (Sans ce try: … except …, cette ligne créerait : Only valid with
#    DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of
#    'RangeIndex')


# Les textes : l'accesseur .str
################################

"""
Les colonnes de texte saisies par des humains sont rarement propres : espaces
en trop, majuscules incohérentes, fautes de frappe… L'accesseur .str donne
accès à presque toutes les méthodes des chaînes (cf. chap. 7 et 8), appliquées
à TOUTE la colonne d'un coup :
"""
villes = pd.Series(["  Paris ", "LYON", "lyon", "Saint-Étienne", None])
print(villes.str.strip().str.lower())
# => 0            paris
#    1             lyon
#    2             lyon
#    3    saint-étienne
#    4              NaN
#    dtype: str

"""
Remarquez :
    - on peut enchaîner les .str : .str.strip().str.lower(),
    - la valeur manquante (None) reste manquante (NaN), sans provoquer
      d'erreur. C'est un gros avantage sur une boucle avec .lower(), qui
      planterait sur None (cf. chap. 26).

D'autres méthodes utiles :
"""
print(villes.str.len().tolist())  # => [8.0, 4.0, 4.0, 13.0, nan]
print(villes.str.contains("on", case=False).tolist())
# => [False, True, True, False, False]
print(villes.str.strip().str.title().tolist())
# => ['Paris', 'Lyon', 'Lyon', 'Saint-Étienne', nan]

"""
.str.contains() retourne une Series de booléens : on peut donc s'en servir
comme filtre (cf. chap. 39, "Filtrer les lignes"). (Avec pandas 2.x, la valeur
manquante donne NaN au lieu de False : ajoutez na=False pour être sûr.)

.str.split() découpe chaque chaîne ; avec expand=True, les morceaux deviennent
des colonnes. Le paramètre n limite le nombre de découpes :
"""
personnes = pd.Series(["Mme Alice Martin", "M. Bob Durand"])
print(personnes.str.split(" ", n=1, expand=True))
# =>      0             1
#    0  Mme  Alice Martin
#    1   M.    Bob Durand

"""
.str.replace() remplace un morceau de texte. Exemple classique : des nombres
écrits à la française, avec une virgule, que Python ne sait pas convertir
(cf. chap. 6). On remplace la virgule par un point, puis on convertit avec
.astype(float) :
"""
prix_texte = pd.Series(["12,50", "3,99", "100"])
prix = prix_texte.str.replace(",", ".").astype(float)
print(prix.tolist())  # => [12.5, 3.99, 100.0]

"""
Enfin, avec les expressions régulières (cf. chap. 42), .str.extract() extrait
des morceaux de texte qui suivent un motif. Chaque groupe entre parenthèses du
motif devient une colonne :
"""
references = pd.Series(["Réf. A-123 (2023)", "Réf. B-7 (2024)"])
print(references.str.extract(r"([A-Z])-(\d+)"))
# =>    0    1
#    0  A  123
#    1  B    7

# Et .str.replace(…, regex=True) remplace selon un motif :
print(references.str.replace(r" \(\d{4}\)", "", regex=True).tolist())
# => ['Réf. A-123', 'Réf. B-7']


# Nettoyer des données
#######################

"""
Voici un extrait de registre d'adhérents d'une médiathèque, tel qu'on le
reçoit parfois : rempli à la main, par plusieurs personnes. Tous les
problèmes classiques y sont.
"""
brut = pd.DataFrame({
    "Nom ": ["alice martin", "Bob Durand", "Bob Durand", "CHLOÉ PETIT",
             "david roux", "Emma Blanc"],
    "Age": ["34", "17", "17", "200", None, "41"],
    "ville": ["lyon", "Paris ", "Paris ", "PARIS", "Lyon", "paris"],
    "abonne": ["oui", "non", "non", "Oui", "oui", "NON"],
})
print(brut)
# =>            Nom   Age   ville abonne
#    0  alice martin   34    lyon    oui
#    1    Bob Durand   17  Paris     non
#    2    Bob Durand   17  Paris     non
#    3   CHLOÉ PETIT  200   PARIS    Oui
#    4    david roux  NaN    Lyon    oui
#    5    Emma Blanc   41   paris    NON

"""
Étape 1 : des noms de colonnes propres. "Nom " a un espace en trop, ce qui
rendrait brut["Nom"] impossible. On peut nettoyer TOUS les noms de colonnes
d'un coup, car .columns accepte aussi l'accesseur .str :
"""
propre = brut.copy()  # on garde l'original intact (cf. chap. 24 sur les copies)
propre.columns = propre.columns.str.strip().str.lower()
print(list(propre.columns))  # => ['nom', 'age', 'ville', 'abonne']

"""
Étape 2 : les doublons. .duplicated() indique les lignes qui sont la copie
EXACTE d'une ligne précédente, et .drop_duplicates() les supprime :
"""
print(propre.duplicated().tolist())
# => [False, False, True, False, False, False]
propre = propre.drop_duplicates()
print(len(propre))  # => 5

"""
(Avec subset=["nom"], on ne compare que certaines colonnes. Attention : ici,
les doublons sont identiques, mais souvent ils diffèrent d'un espace ou d'une
majuscule… d'où l'intérêt de nettoyer les textes AVANT de chercher les
doublons !)

Étape 3 : des textes homogènes, avec .str (cf. plus haut) :
"""
propre["nom"] = propre["nom"].str.title()
propre["ville"] = propre["ville"].str.strip().str.title()
print(propre["ville"].value_counts())
# => ville
#    Paris    3
#    Lyon     2
#    Name: count, dtype: int64

"""
.value_counts() (cf. chap. 39) est le meilleur moyen de vérifier qu'une
colonne de catégories est propre : avant nettoyage, on aurait eu 5 villes
différentes au lieu de 2 !

Étape 4 : remplacer des valeurs avec .map() ou .replace().
    - .map(dictionnaire) remplace CHAQUE valeur par celle du dictionnaire ;
      les valeurs absentes du dictionnaire deviennent NaN,
    - .replace(dictionnaire) ne remplace que les valeurs présentes dans le
      dictionnaire, et laisse les autres intactes.
"""
propre["abonne"] = propre["abonne"].str.lower().map({"oui": True,
                                                     "non": False})
print(propre["abonne"].tolist())  # => [True, False, True, True, False]

"""
Étape 5 : les bons types. L'âge a été lu comme du texte : impossible de
calculer une moyenne. On convertit avec .astype() (l'équivalent d'int() et
float() du chap. 6, sur toute une colonne).

Problème : il y a une valeur manquante, et un entier ne peut pas être NaN :
"""
try:
    propre["age"].astype(int)
except (ValueError, TypeError) as err:
    print(f"7: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 7: (Sans ce try: … except …, cette ligne créerait : cannot convert float
#    NaN to integer)

"""
Deux solutions :
    - convertir en float (qui accepte NaN),
    - ou utiliser pd.to_numeric(…, errors="coerce"), qui convertit aussi les
      textes invalides en NaN (comme pour les dates, cf. plus haut).
"""
propre["age"] = pd.to_numeric(propre["age"], errors="coerce")
print(propre["age"].tolist())  # => [34.0, 17.0, 200.0, nan, 41.0]

"""
Étape 6 : les valeurs aberrantes ("outliers"). 200 ans, c'est sûrement une
faute de frappe. Pour les repérer, on peut :
    - utiliser son bon sens et des règles métier (un âge est entre 0 et 120),
    - regarder .describe() (cf. chap. 39) : un max anormal saute aux yeux,
    - utiliser une règle statistique : on considère comme suspecte toute
      valeur éloignée de plus de 1,5 fois l'écart interquartile (Q3 - Q1) des
      quartiles (c'est la règle utilisée par les boîtes à moustaches, cf.
      chap. 40).
"""
# .between(a, b) teste si chaque valeur est entre a et b (NaN donne False) :
print(propre["age"].between(0, 120).tolist())
# => [True, True, False, False, True]

# On remplace les âges impossibles par NaN avec .where(condition) : les valeurs
# qui ne respectent pas la condition deviennent NaN.
propre["age"] = propre["age"].where(propre["age"].between(0, 120))
print(propre["age"].tolist())  # => [34.0, 17.0, nan, nan, 41.0]

"""
IMPT : ne supprimez jamais une valeur "parce qu'elle dérange". Une valeur
extrême peut être vraie (un adhérent de 99 ans existe !). Supprimez seulement
ce qui est IMPOSSIBLE, et notez toujours ce que vous avez fait.

Étape 7 : les valeurs manquantes. Au chap. 39, on a vu .isna(), .dropna() et
.fillna(). Il existe d'autres stratégies de remplissage :
    - .fillna(valeur) : une valeur fixe (0, la moyenne, la médiane…),
    - .ffill() ("forward fill") : la dernière valeur connue, recopiée vers le
      bas (utile pour une série temporelle : "rien n'a changé depuis"),
    - .interpolate() : une valeur intermédiaire, calculée entre la valeur
      précédente et la suivante.
"""
mesures = pd.Series([10.0, None, None, 16.0])
print(mesures.fillna(0).tolist())   # => [10.0, 0.0, 0.0, 16.0]
print(mesures.ffill().tolist())     # => [10.0, 10.0, 10.0, 16.0]
print(mesures.interpolate().tolist())  # => [10.0, 12.0, 14.0, 16.0]

# Pour l'âge, on remplace les âges inconnus par la médiane des âges connus
# (la médiane est moins sensible aux valeurs extrêmes que la moyenne) :
propre["age"] = propre["age"].fillna(propre["age"].median())
print(propre)
# =>             nom   age  ville  abonne
#    0  Alice Martin  34.0   Lyon    True
#    1    Bob Durand  17.0  Paris   False
#    3   Chloé Petit  34.0  Paris    True
#    4    David Roux  34.0   Lyon    True
#    5    Emma Blanc  41.0  Paris   False

"""
Il n'y a pas de "bonne" stratégie universelle : tout dépend de ce que l'on
veut faire des données. Supprimer les lignes incomplètes (dropna) est simple,
mais on perd de l'information ; les remplir introduit des valeurs "inventées".

Étape 8 (bonus) : le type "category". Une colonne qui ne contient que
quelques valeurs différentes, répétées des milliers de fois (une ville, un
statut…), occupe beaucoup moins de mémoire si on la convertit en "category" :
pandas stocke chaque valeur différente une seule fois, et un simple numéro
pour chaque ligne.
"""
grosse = pd.Series(["Paris", "Lyon"] * 50_000)  # 100 000 lignes
avant = grosse.memory_usage(deep=True)
apres = grosse.astype("category").memory_usage(deep=True)
print(round(avant / apres))  # => 53 (environ ; dépend de la version)
print(grosse.astype("category").cat.categories.tolist())  # => ['Lyon', 'Paris']


# Créer des classes : cut et qcut
##################################

"""
On a souvent besoin de transformer une valeur numérique en catégorie : un âge
en tranche d'âge, une note en mention… Au chap. 39, on l'a fait avec une
fonction et .apply(). pd.cut() le fait directement : on lui donne les bornes
des classes (bins) et leurs noms (labels).

Avec bins=[0, 17, 64, 120], les classes sont ]0, 17], ]17, 64] et ]64, 120] :
la borne de gauche est exclue, celle de droite incluse.
"""
ages = pd.Series([5, 17, 18, 34, 70])
tranches = pd.cut(ages, bins=[0, 17, 64, 120],
                  labels=["mineur", "adulte", "senior"])
print(tranches)
# => 0    mineur
#    1    mineur
#    2    adulte
#    3    adulte
#    4    senior
#    dtype: category
#    Categories (3, str): ['mineur' < 'adulte' < 'senior']

"""
Le résultat est de type "category" (cf. plus haut). Remarquez le "<" entre les
catégories : elles sont ORDONNÉES (mineur < adulte < senior), ce qui permet de
les trier dans un ordre logique, et pas alphabétique.

pd.qcut() ("quantile cut") découpe autrement : au lieu de donner des bornes,
on donne un nombre de classes, et pandas choisit les bornes pour que chaque
classe contienne le MÊME nombre de valeurs. Avec q=4, on obtient les quartiles :
"""
scores = pd.Series([3, 8, 12, 15, 21, 30, 44, 90])
print(pd.qcut(scores, q=4, labels=["Q1", "Q2", "Q3", "Q4"]).tolist())
# => ['Q1', 'Q1', 'Q2', 'Q2', 'Q3', 'Q3', 'Q4', 'Q4']


# apply ou vectorisation ?
###########################

"""
.apply() (cf. chap. 39) applique une fonction Python à chaque valeur (ou,
avec axis=1, à chaque ligne). C'est très souple… mais LENT : pandas doit
appeler votre fonction une fois par ligne, comme une boucle for.

Les opérations "vectorisées" (cf. chap. 38) sont calculées en une seule fois,
en C, sur toute la colonne : elles sont souvent 10 à 100 fois plus rapides.
"""
panier = pd.DataFrame({"prix": [10.0, 20.0, 5.0], "quantite": [3, 1, 2]})

# Version apply, ligne par ligne (axis=1) : à éviter
print(panier.apply(lambda ligne: ligne["prix"] * ligne["quantite"],
                   axis=1).tolist())
# => [30.0, 20.0, 10.0]

# Version vectorisée : à préférer
print((panier["prix"] * panier["quantite"]).tolist())  # => [30.0, 20.0, 10.0]

"""
Mesurons la différence sur 100 000 lignes, avec timeit (cf. chap. 22) :
"""
import timeit

grand = pd.DataFrame({"prix": [10.0] * 100_000, "quantite": [3] * 100_000})
t_apply = timeit.timeit(
    lambda: grand.apply(lambda l: l["prix"] * l["quantite"], axis=1),
    number=1)
t_vecto = timeit.timeit(lambda: grand["prix"] * grand["quantite"], number=1)
print(t_apply > 10 * t_vecto)  # => True (le rapport exact dépend de la machine)

"""
Règle pratique :
    1. cherchez d'abord une opération vectorisée (+, *, comparaisons, .str,
       .dt, np.where (cf. chap. 38), pd.cut, .map…),
    2. utilisez .apply() seulement quand c'est impossible autrement (une
       logique compliquée, une fonction d'une autre bibliothèque…),
    3. n'écrivez jamais de boucle for sur les lignes d'un DataFrame (avec
       .iterrows() par exemple) sans y être obligé.
On reparlera du coût des algorithmes au chap. 45 (complexité).
"""


# Enchaîner les méthodes : assign et pipe
##########################################

"""
Comme la plupart des méthodes pandas retournent un nouveau DataFrame, on peut
les enchaîner les unes derrière les autres : c'est le "method chaining". Le
code se lit alors de haut en bas, comme une recette.

Pour ajouter une colonne au milieu d'une chaîne, on utilise .assign(nom=…).
Si la valeur dépend du tableau en cours de construction, on passe une lambda
qui reçoit ce tableau (ici "t") :
"""
resultat = (
    panier
    .assign(total=lambda t: t["prix"] * t["quantite"])
    .query("total > 15")
    .sort_values("total", ascending=False)
)
print(resultat)
# =>    prix  quantite  total
#    0  10.0         3   30.0
#    1  20.0         1   20.0

"""
Notez :
    - les parenthèses autour de toute l'expression, qui permettent de couper
      la chaîne sur plusieurs lignes (cf. chap. 5),
    - .query("total > 15") : une autre façon d'écrire un filtre, sous forme de
      chaîne, équivalente à t[t["total"] > 15].

.pipe(fonction, arguments…) insère VOTRE fonction dans la chaîne : elle reçoit
le DataFrame en premier argument, et doit en retourner un. Pratique pour
réutiliser une étape de nettoyage :
"""
def ajouter_ttc(table, taux=0.2):
    """Ajoute une colonne "ttc" (prix toutes taxes comprises)."""
    return table.assign(ttc=(table["prix"] * (1 + taux)).round(2))


print(panier.pipe(ajouter_ttc, taux=0.055))
# =>    prix  quantite    ttc
#    0  10.0         3  10.55
#    1  20.0         1  21.10
#    2   5.0         2   5.28


# Lire et écrire d'autres formats
##################################

"""
pd.read_csv() a de nombreux paramètres pour lire les CSV "à la française",
exportés par Excel :
    - sep=";" : le séparateur est un point-virgule (et non une virgule),
    - decimal="," : les nombres ont une virgule décimale,
    - encoding="latin-1" : l'ancien encodage de Windows (cf. chap. 28),
    - parse_dates=[…] : convertit directement des colonnes en dates,
    - usecols=[…] : ne charge que certaines colonnes,
    - dtype={…} : impose le type de certaines colonnes.
"""
with open("chap48_mesures.csv", "w", encoding="utf-8") as f:
    f.write("date;station;temperature\n"
            "2024-07-01;Lyon;28,5\n"
            "2024-07-02;Lyon;31,2\n")

mesures = pd.read_csv("chap48_mesures.csv", sep=";", decimal=",",
                      parse_dates=["date"])
print(mesures)
# =>         date station  temperature
#    0 2024-07-01    Lyon         28.5
#    1 2024-07-02    Lyon         31.2
print(mesures.dtypes)
# => date           datetime64[us]
#    station                   str
#    temperature           float64
#    dtype: object

"""
De la même façon, .to_csv() accepte sep=";" et decimal="," pour produire un
fichier qu'Excel en français ouvrira correctement.

pandas sait lire et écrire beaucoup d'autres formats (il faut parfois installer
une bibliothèque supplémentaire) :
    - Excel : pd.read_excel("fichier.xlsx", sheet_name=…) et .to_excel()
      (nécessite openpyxl : uv add openpyxl),
    - JSON : pd.read_json() et .to_json() (cf. chap. 27 et 49),
    - Parquet : pd.read_parquet() et .to_parquet() (nécessite pyarrow). C'est
      le format de référence en Data Science : compact, rapide, et il
      conserve les types (dates, catégories…), contrairement au CSV,
    - SQL : pd.read_sql() lit le résultat d'une requête dans une base de
      données.
"""


# Cas pratique : analyser des ventes
#####################################

"""
Mettons tout ensemble. Une chaîne de librairies nous envoie deux fichiers :
    - ventes.csv : une ligne par vente, exportée par les caisses (avec les
      défauts habituels),
    - produits.csv : le catalogue (référence, titre, rayon, prix).
Question : quel est le chiffre d'affaires par mois et par rayon ?
"""
with open("chap48_ventes.csv", "w", encoding="utf-8") as f:
    f.write("date;magasin;ref;quantite\n"
            "05/01/2024; lyon;L01;2\n"
            "05/01/2024;Paris;L02;1\n"
            "05/01/2024;Paris;L02;1\n"
            "17/01/2024;LYON;L03;3\n"
            "29/01/2024;Paris;L01;\n"
            "02/02/2024;Paris;L03;999\n"
            "14/02/2024;Lyon;L02;4\n"
            "20/02/2024;paris;L01;1\n"
            "03/03/2024;Lyon;L04;2\n")

with open("chap48_produits.csv", "w", encoding="utf-8") as f:
    f.write("ref,titre,rayon,prix\n"
            "L01,Le Petit Prince,Jeunesse,8.5\n"
            "L02,Python pour les nuls,Informatique,24.9\n"
            "L03,Astérix,BD,10.9\n")

# 1. Chargement : séparateur ";" pour les ventes
ventes = pd.read_csv("chap48_ventes.csv", sep=";")
produits = pd.read_csv("chap48_produits.csv")
print(ventes.shape, produits.shape)  # => (9, 4) (3, 4)

"""
2. Nettoyage, en une seule chaîne de méthodes :
    - dates à la française → vraies dates,
    - noms de magasins homogènes,
    - suppression des doublons (le ticket du 05/01 a été enregistré deux
      fois),
    - suppression des ventes sans quantité,
    - suppression de la quantité absurde (999 livres d'un coup : une erreur
      de saisie, après vérification auprès du magasin).
"""
ventes_propres = (
    ventes
    .assign(
        date=lambda t: pd.to_datetime(t["date"], format="%d/%m/%Y"),
        magasin=lambda t: t["magasin"].str.strip().str.title(),
    )
    .drop_duplicates()
    .dropna(subset=["quantite"])
    .query("quantite < 100")
    .astype({"quantite": int})
)
print(ventes_propres)
# =>         date magasin  ref  quantite
#    0 2024-01-05    Lyon  L01         2
#    1 2024-01-05   Paris  L02         1
#    3 2024-01-17    Lyon  L03         3
#    6 2024-02-14    Lyon  L02         4
#    7 2024-02-20   Paris  L01         1
#    8 2024-03-03    Lyon  L04         2

"""
On est passé de 9 à 6 lignes. Vérifions toujours ce qu'on a supprimé, et
pourquoi : ici, un doublon, une quantité vide, une quantité absurde.

3. Jointure avec le catalogue. Chaque vente concerne UN produit : c'est une
relation "many_to_one". On fait une jointure left avec indicator=True, pour
repérer les références inconnues du catalogue :
"""
detail = pd.merge(ventes_propres, produits, on="ref", how="left",
                  validate="many_to_one", indicator=True)
print(detail[detail["_merge"] == "left_only"][["date", "ref"]])
# =>         date  ref
#    5 2024-03-03  L04

"""
La référence L04 n'existe pas dans le catalogue ! Dans la vraie vie, on
demanderait le catalogue à jour. Ici, on écarte cette vente (en le notant
dans notre rapport), puis on calcule le chiffre d'affaires de chaque ligne :
"""
detail = (
    detail
    .query("_merge == 'both'")
    .drop(columns="_merge")
    .assign(ca=lambda t: t["quantite"] * t["prix"])
)
print(detail[["date", "magasin", "titre", "quantite", "ca"]])
# =>         date magasin                 titre  quantite    ca
#    0 2024-01-05    Lyon       Le Petit Prince         2  17.0
#    1 2024-01-05   Paris  Python pour les nuls         1  24.9
#    2 2024-01-17    Lyon               Astérix         3  32.7
#    3 2024-02-14    Lyon  Python pour les nuls         4  99.6
#    4 2024-02-20   Paris       Le Petit Prince         1   8.5

"""
4. Agrégation : chiffre d'affaires par mois et par rayon, avec un
pivot_table. On crée d'abord une colonne "mois" à partir de la date
(.dt.strftime, cf. plus haut) :
"""
bilan = (
    detail
    .assign(mois=lambda t: t["date"].dt.strftime("%Y-%m"))
    .pivot_table(index="rayon", columns="mois", values="ca", aggfunc="sum",
                 fill_value=0, margins=True, margins_name="Total")
)
print(bilan)
# => mois          2024-01  2024-02  Total
#    rayon
#    BD               32.7      0.0   32.7
#    Informatique     24.9     99.6  124.5
#    Jeunesse         17.0      8.5   25.5
#    Total            74.6    108.1  182.7

"""
(fill_value=0 remplace les cases vides par 0 : aucune vente de BD en février,
par exemple.)

5. Une dernière question : quel magasin vend le plus, en moyenne par vente ?
"""
print(detail.groupby("magasin")["ca"].agg(["count", "sum", "mean"]).round(2))
# =>          count    sum   mean
#    magasin
#    Lyon         3  149.3  49.77
#    Paris        2   33.4  16.70

# Lyon fait près de 50 € par vente en moyenne, contre 16,70 € à Paris.

"""
En une quarantaine de lignes, on a chargé, nettoyé, joint, agrégé et résumé
les données. Avec quelques milliers ou millions de lignes, le code serait
EXACTEMENT le même : c'est toute la force de pandas.

Pour présenter ces résultats, on pourra tracer un graphique (cf. chap. 40 et
chap. 50 pour seaborn).
"""


# Nettoyage final
##################

"""
Comme d'habitude (cf. chap. 28 et 39), on supprime les fichiers créés par ce
chapitre :
"""
for nom_fichier in ["chap48_mesures.csv", "chap48_ventes.csv",
                    "chap48_produits.csv"]:
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)

"""
Pour aller plus loin :
    - le guide de l'utilisateur de pandas, en particulier les pages "Merge,
      join, concatenate and compare", "Reshaping and pivot tables" et "Time
      series / date functionality" :
      https://pandas.pydata.org/docs/user_guide/
    - le livre "Python for Data Analysis" de Wes McKinney, le créateur de
      pandas, lisible gratuitement en ligne : https://wesmckinney.com/book/
"""
