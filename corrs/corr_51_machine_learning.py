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
#  Chap. 51     #  Introduction au Machine Learning : corrigés                 #
#               #                                                              #
################################################################################

"""
Corrigés des exercices du fichier exos_51_machine_learning.py. Chaque énoncé
est rappelé, suivi d'une solution commentée. Il y a souvent plusieurs bonnes
solutions !

Ces exercices nécessitent scikit-learn et pandas. Tous les jeux de données
utilisés sont inclus dans scikit-learn ou générés ci-dessous : pas besoin
d'Internet.

IMPT : utilisez random_state=0 partout où il y a du hasard (découpage,
modèles), pour obtenir les mêmes résultats que les corrigés.
"""

import sys

try:
    import numpy as np
    import pandas as pd
    import sklearn
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("Ces exercices ont besoin de scikit-learn et de pandas : lancez")
    print("\"uv add scikit-learn pandas\" (ou \"pip install scikit-learn")
    print("pandas\"), puis relancez ce programme.")
    sys.exit(0)


#################
#  Préparation  #
#################

# Ne modifiez pas ce bloc : il crée les données utilisées par les exercices.

# 1. Le jeu de données "breast cancer" (inclus dans scikit-learn) : 569
#    tumeurs décrites par 30 mesures faites sur une image, et le diagnostic :
#    0 = maligne, 1 = bénigne.
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer(as_frame=True)
X_cancer = cancer.data
y_cancer = cancer.target

# 2. Des voitures d'occasion (données inventées) : prédire le prix.
rng = np.random.default_rng(seed=3)
n = 400
voitures = pd.DataFrame({
    "kilometrage": rng.uniform(5_000, 200_000, n).round(-2),
    "age": rng.integers(1, 15, n),
    "carburant": rng.choice(["essence", "diesel", "electrique"], n),
})
voitures["prix"] = (
    25_000
    - 0.06 * voitures["kilometrage"]
    - 900 * voitures["age"]
    + voitures["carburant"].map({"essence": 0, "diesel": 1_000,
                                 "electrique": 6_000})
    + rng.normal(0, 1_500, n)
).round(-1)

from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_wine, make_blobs
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (adjusted_rand_score, classification_report,
                             confusion_matrix, mean_absolute_error)
from sklearn.model_selection import (GridSearchCV, cross_val_score,
                                     train_test_split)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

# (On regroupe ici tous les imports des corrigés, comme le recommande la
# PEP 8, cf. chap. 20. Dans le chapitre, ils étaient faits au fur et à
# mesure, pour bien voir d'où vient chaque outil.)


##########################################
#  Vocabulaire et familles de problèmes  #
##########################################

"""
1. Sans exécuter : pour chaque problème, dites s'il s'agit d'apprentissage
   supervisé (régression ou classification) ou non supervisé (clustering) :
       a) prédire la consommation électrique d'une ville demain,
       b) détecter si une transaction bancaire est frauduleuse, à partir de
          transactions passées étiquetées "fraude" / "normale",
       c) regrouper des articles de presse par sujets, sans liste de sujets
          connue à l'avance,
       d) reconnaître le chiffre (0 à 9) écrit sur une image,
       e) estimer l'âge d'une personne à partir d'une photo,
       f) découvrir des profils de clients dans un fichier de ventes.

a) Supervisé, RÉGRESSION : la cible est un nombre (des kWh).
b) Supervisé, CLASSIFICATION : deux catégories, et on a des exemples
   étiquetés.
c) NON supervisé, clustering : pas d'étiquettes, on cherche des groupes.
d) Supervisé, CLASSIFICATION : 10 catégories (les chiffres). Attention :
   même si ce sont des chiffres, ce sont des CATÉGORIES (prédire 4,5 n'a
   aucun sens).
e) Supervisé, RÉGRESSION : l'âge est un nombre.
f) NON supervisé, clustering (on parle de "segmentation" de clientèle).

2. Pour le jeu de données "breast cancer" (X_cancer, y_cancer) :
       a) affichez la forme de X_cancer et de y_cancer ; que représentent
          les lignes ? les colonnes ?
       b) affichez les noms des deux classes (cancer.target_names),
       c) affichez le nombre de tumeurs de chaque classe. Les classes
          sont-elles équilibrées ?
"""
print(X_cancer.shape)  # => (569, 30)
print(y_cancer.shape)  # => (569,)
# a) Chaque ligne est un échantillon (une tumeur), chaque colonne une
#    feature (une mesure). y contient une étiquette par tumeur.
print(cancer.target_names.tolist())  # => ['malignant', 'benign']
print(y_cancer.value_counts().sort_index().to_dict())  # => {0: 212, 1: 357}
# c) 212 malignes (0) pour 357 bénignes (1) : les classes ne sont pas
#    équilibrées (environ 37 % / 63 %), sans être très déséquilibrées.


##################################
#  Séparer entraînement et test  #
##################################

"""
3. Coupez X_cancer et y_cancer en un jeu d'entraînement (80 %) et un jeu de
   test (20 %), avec random_state=0 et en gardant les proportions des
   classes. Affichez la forme des deux X, puis la proportion de tumeurs
   bénignes (classe 1) dans chacun des deux y, arrondie à 3 décimales.
"""
X_train, X_test, y_train, y_test = train_test_split(
    X_cancer, y_cancer, test_size=0.2, random_state=0, stratify=y_cancer
)
print(X_train.shape, X_test.shape)  # => (455, 30) (114, 30)
print(round(y_train.mean(), 3), round(y_test.mean(), 3))  # => 0.626 0.632
# La moyenne d'une colonne de 0 et de 1 est la proportion de 1. Grâce à
# stratify, les deux jeux ont presque la même proportion de tumeurs
# bénignes que l'ensemble des données (357 / 569 = 0.627).

"""
4. Sans exécuter : pourquoi ne faut-il pas évaluer un modèle sur les données
   qui ont servi à l'entraîner ? Et pourquoi utilise-t-on stratify=y ?

Un modèle peut apprendre ses exemples "par cœur" : il aurait un excellent
score sur eux, sans rien dire de sa capacité à prédire sur de NOUVELLES
données, ce qui est le seul but. On l'évalue donc sur des données jamais
vues (le jeu de test).

stratify=y garantit que chaque classe a la même proportion dans le jeu
d'entraînement et dans le jeu de test. Sans cela, par malchance, le test
pourrait contenir trop peu de tumeurs malignes pour être représentatif.
"""


########################################
#  Baseline, kNN et arbre de décision  #
########################################

"""
5. Calculez l'exactitude (accuracy) d'un DummyClassifier qui prédit toujours
   la classe la plus fréquente, sur le jeu de test. Expliquez la valeur
   obtenue à partir de l'exercice 2 c).
"""
baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)
print(round(baseline.score(X_test, y_test), 3))  # => 0.632
# Le modèle répond toujours "bénigne" (la classe la plus fréquente). Il a
# donc raison pour toutes les tumeurs bénignes, soit environ 63 % du test.
# Et il ne détecte AUCUN cancer : un score de 63 % n'est pas bon ici.

"""
6. Entraînez un KNeighborsClassifier (paramètres par défaut) sur les données
   brutes, et affichez son exactitude sur le test. Puis faites de même avec
   un pipeline StandardScaler + KNeighborsClassifier. Pourquoi une telle
   différence ? (Indice : regardez le min et le max des colonnes "mean area"
   et "smoothness error".)
"""
knn_brut = KNeighborsClassifier().fit(X_train, y_train)
print(round(knn_brut.score(X_test, y_test), 3))  # => 0.912

knn_norm = make_pipeline(StandardScaler(), KNeighborsClassifier())
knn_norm.fit(X_train, y_train)
print(round(knn_norm.score(X_test, y_test), 3))  # => 0.956

print(X_cancer[["mean area", "smoothness error"]].agg(["min", "max"]))
# =>      mean area  smoothness error
# => min      143.5          0.001713
# => max     2501.0          0.031130
# "mean area" va de 143 à 2501, "smoothness error" reste sous 0.04. Le kNN
# calcule des distances : sans normalisation, les features aux grandes
# valeurs (comme les aires) écrasent toutes les autres. Le StandardScaler
# met toutes les features à la même échelle.

"""
7. Entraînez un arbre de décision de profondeur 3 (random_state=0).
   Affichez son exactitude sur le test, puis les 3 features les plus
   importantes (feature_importances_) avec leur importance arrondie à 2
   décimales.
"""
arbre = DecisionTreeClassifier(max_depth=3, random_state=0)
arbre.fit(X_train, y_train)
print(round(arbre.score(X_test, y_test), 3))  # => 0.921

importances = pd.Series(arbre.feature_importances_, index=X_cancer.columns)
for feature, importance in importances.nlargest(3).items():
    print(f"{feature:>20} : {importance:.2f}")
# => worst concave points : 0.79
# =>           worst area : 0.13
# =>           area error : 0.05
# nlargest(3) renvoie les 3 plus grandes valeurs d'une Series (cf. chap. 39).
# Les autres features ont une importance nulle ou faible : avec 3 niveaux
# de questions, l'arbre n'en utilise que quelques-unes.


############################
#  Évaluer un classifieur  #
############################

"""
8. Pour le pipeline kNN normalisé de l'exercice 6 :
       a) affichez la matrice de confusion sur le jeu de test. Combien de
          tumeurs malignes ont été classées bénignes ?
       b) affichez le rapport de classification (classification_report),
          avec les noms des classes.
       c) Sans exécuter : pour ce problème médical, quelle erreur est la
          plus grave ? Faut-il surveiller surtout la précision ou le rappel
          de la classe "malignant" ?
"""
y_pred = knn_norm.predict(X_test)
print(confusion_matrix(y_test, y_pred))
# => [[38  4]
# =>  [ 1 71]]
# a) Lignes = vraies classes (0 = maligne, 1 = bénigne), colonnes = classes
#    prédites. Les tumeurs malignes classées bénignes sont en ligne 0,
#    colonne 1 : il y en a 4 (sur 42 tumeurs malignes). C'est le rappel de
#    0.90 de la classe "malignant" dans le rapport ci-dessous.
print(classification_report(y_test, y_pred,
                            target_names=cancer.target_names))
# =>               precision    recall  f1-score   support
# =>
# =>    malignant       0.97      0.90      0.94        42
# =>       benign       0.95      0.99      0.97        72
# =>
# =>     accuracy                           0.96       114
# =>    macro avg       0.96      0.95      0.95       114
# => weighted avg       0.96      0.96      0.96       114
# c) La pire erreur est de déclarer bénigne une tumeur maligne (un cancer
#    non traité). On surveille donc le RAPPEL de la classe "malignant" :
#    parmi les vraies tumeurs malignes, combien le modèle en trouve-t-il ?
#    Une fausse alerte (une tumeur bénigne déclarée maligne) est moins
#    grave : des examens complémentaires la corrigeront.


#############################################
#  Sur-apprentissage et validation croisée  #
#############################################

"""
9. Pour des arbres de décision de profondeur 1, 2, 3, 5, 8 et sans limite
   (None), affichez le score d'entraînement et le score de test. À partir de
   quelle profondeur l'arbre connaît-il le jeu d'entraînement par cœur ?
   Quelle profondeur choisiriez-vous ?
"""
print("profondeur  train   test")
for profondeur in [1, 2, 3, 5, 8, None]:
    modele = DecisionTreeClassifier(max_depth=profondeur, random_state=0)
    modele.fit(X_train, y_train)
    print(f"{str(profondeur):>10}  {modele.score(X_train, y_train):.3f}"
          f"  {modele.score(X_test, y_test):.3f}")
# => profondeur  train   test
# =>          1  0.927  0.886
# =>          2  0.958  0.921
# =>          3  0.974  0.921
# =>          5  0.993  0.947
# =>          8  1.000  0.939
# =>       None  1.000  0.939
# Le score d'entraînement atteint 1.000 (100 %) dès la profondeur 8 : l'arbre
# connaît chaque exemple par cœur, mais le score de test n'en profite pas.
# On choisirait une profondeur modérée, qui donne un bon score de test sans
# écart énorme avec l'entraînement. ATTENTION : on ne devrait pas faire ce
# choix d'après le jeu de test (cf. chapitre) ; la bonne méthode est la
# validation croisée (exercices 10 et 11).

"""
10. Comparez par validation croisée à 5 plis, sur le jeu d'ENTRAÎNEMENT,
    les trois modèles suivants, et affichez pour chacun la moyenne des
    scores (3 décimales) :
        - un DummyClassifier,
        - un arbre de décision de profondeur 3 (random_state=0),
        - le pipeline StandardScaler + KNeighborsClassifier.
"""
modeles = {
    "baseline": DummyClassifier(),
    "arbre (3)": DecisionTreeClassifier(max_depth=3, random_state=0),
    "kNN normalisé": make_pipeline(StandardScaler(), KNeighborsClassifier()),
}
for nom, modele in modeles.items():
    scores = cross_val_score(modele, X_train, y_train, cv=5)
    print(f"{nom:>14} : {scores.mean():.3f}")
# =>       baseline : 0.626
# =>      arbre (3) : 0.941
# =>  kNN normalisé : 0.958
# Le kNN normalisé est le meilleur des trois, et les deux "vrais" modèles
# font bien mieux que la baseline.

"""
11. Avec GridSearchCV (5 plis), cherchez la meilleure valeur de
    n_neighbors parmi 1, 3, 5, 7, 11, 15, 21 pour le pipeline kNN normalisé.
    Affichez la meilleure valeur, le meilleur score de validation croisée,
    puis le score du modèle final sur le jeu de test.
"""
grille = {"kneighborsclassifier__n_neighbors": [1, 3, 5, 7, 11, 15, 21]}
recherche = GridSearchCV(knn_norm, grille, cv=5)
recherche.fit(X_train, y_train)
print(recherche.best_params_)
# => {'kneighborsclassifier__n_neighbors': 3}
print(round(recherche.best_score_, 3))  # => 0.963
print(round(recherche.score(X_test, y_test), 3))  # => 0.956
# Le nom du paramètre est "nomdeletape__parametre" : make_pipeline nomme
# l'étape d'après la classe, en minuscules. Le score de test n'est calculé
# qu'une fois, à la toute fin.


############################
#  La régression linéaire  #
############################

"""
12. Prédire le prix des voitures (DataFrame voitures) à partir du
    kilométrage et de l'âge seulement :
        a) coupez les données (test 25 %, random_state=0),
        b) entraînez une LinearRegression et affichez ses coefficients
           (arrondis à 2 décimales) ; interprétez-les,
        c) affichez la MAE et le R² sur le test,
        d) comparez la MAE à celle d'un DummyRegressor.
"""
X_v = voitures[["kilometrage", "age"]]
y_v = voitures["prix"]
Xv_train, Xv_test, yv_train, yv_test = train_test_split(
    X_v, y_v, test_size=0.25, random_state=0
)
regression = LinearRegression().fit(Xv_train, yv_train)
for feature, coef in zip(X_v.columns, regression.coef_):
    print(f"{feature:>12} : {coef:.2f}")
# =>  kilometrage : -0.06
# =>          age : -902.06
# b) Chaque km parcouru fait perdre environ 6 centimes, chaque année
#    d'âge environ 900 € (les vraies valeurs utilisées pour générer les
#    données : -0.06 et -900).

mae = mean_absolute_error(yv_test, regression.predict(Xv_test))
print(f"MAE : {mae:.0f} €")  # => MAE : 2612 €
print(round(regression.score(Xv_test, yv_test), 3))  # => 0.725

baseline_reg = DummyRegressor().fit(Xv_train, yv_train)
mae_base = mean_absolute_error(yv_test, baseline_reg.predict(Xv_test))
print(f"MAE baseline : {mae_base:.0f} €")  # => MAE baseline : 4973 €
# d) Le modèle fait bien mieux que la baseline (qui prédit toujours le prix
#    moyen). Il lui manque l'information du carburant (exercice 14).


################################
#  Prétraitement et pipelines  #
################################

"""
13. Encodez la colonne "carburant" des 5 premières voitures avec un
    OneHotEncoder. Affichez le tableau obtenu et les noms des nouvelles
    colonnes. Que se passe-t-il si on encode ensuite une voiture "hybride" ?
    Comment l'éviter ?
"""
cinq = voitures[["carburant"]].head(5)  # double crochet : un DataFrame (2D)
print(cinq["carburant"].tolist())
# => ['essence', 'diesel', 'electrique', 'diesel', 'diesel']
encodeur = OneHotEncoder()
print(encodeur.fit_transform(cinq).toarray())
# => [[0. 0. 1.]
# =>  [1. 0. 0.]
# =>  [0. 1. 0.]
# =>  [1. 0. 0.]
# =>  [1. 0. 0.]]
print(encodeur.get_feature_names_out().tolist())
# => ['carburant_diesel', 'carburant_electrique', 'carburant_essence']

hybride = pd.DataFrame({"carburant": ["hybride"]})
try:
    encodeur.transform(hybride)
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

encodeur_souple = OneHotEncoder(handle_unknown="ignore").fit(cinq)
print(encodeur_souple.transform(hybride).toarray())  # => [[0. 0. 0.]]
# Avec handle_unknown="ignore", une catégorie inconnue donne une ligne de 0
# au lieu d'une erreur.

"""
14. Reprenez l'exercice 12 en utilisant AUSSI la colonne "carburant", grâce
    à un ColumnTransformer (StandardScaler sur les colonnes numériques,
    OneHotEncoder sur "carburant") dans un pipeline. Le R² sur le test
    s'améliore-t-il ? Prédisez le prix d'une voiture électrique de 4 ans
    ayant 60 000 km.
"""
preparation = ColumnTransformer([
    ("num", StandardScaler(), ["kilometrage", "age"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["carburant"]),
])
pipeline = make_pipeline(preparation, LinearRegression())

X_v2 = voitures[["kilometrage", "age", "carburant"]]
Xv2_train, Xv2_test, yv2_train, yv2_test = train_test_split(
    X_v2, y_v, test_size=0.25, random_state=0
)  # même random_state : mêmes voitures dans le test qu'à l'exercice 12
pipeline.fit(Xv2_train, yv2_train)
print(round(pipeline.score(Xv2_test, yv2_test), 3))  # => 0.924

voiture = pd.DataFrame({"kilometrage": [60_000], "age": [4],
                        "carburant": ["electrique"]})
print(int(round(pipeline.predict(voiture)[0], -2)))  # => 23600
# Le R² s'améliore nettement : le carburant explique une bonne partie du
# prix (+6000 € pour une électrique dans nos données).


###############################################
#  Non supervisé : le clustering avec KMeans  #
###############################################

"""
15. Générez 400 points en 2D répartis en 4 groupes avec
    make_blobs(n_samples=400, centers=4, random_state=0). Appliquez un
    KMeans à 4 clusters (n_init=10, random_state=0) :
        a) affichez le nombre de points de chaque cluster,
        b) comparez les clusters trouvés aux vrais groupes avec
           adjusted_rand_score,
        c) recommencez avec 2 clusters : que devient le score ? KMeans
           pouvait-il "savoir" qu'il y avait 4 groupes ?
"""
X_blobs, vrais_groupes = make_blobs(n_samples=400, centers=4, random_state=0)
kmeans = KMeans(n_clusters=4, n_init=10, random_state=0).fit(X_blobs)
print(np.bincount(kmeans.labels_))  # => [ 99 107  92 102]
print(round(adjusted_rand_score(vrais_groupes, kmeans.labels_), 3))  # => 0.806
# b) Un score de 0.806, et pas 1 : avec random_state=0, deux des groupes de
#    make_blobs se chevauchent un peu, et les points de la zone commune
#    sont parfois attribués "au mauvais" groupe. C'est tout de même très
#    proche des vrais groupes.

kmeans2 = KMeans(n_clusters=2, n_init=10, random_state=0).fit(X_blobs)
print(round(adjusted_rand_score(vrais_groupes, kmeans2.labels_), 3))  # => 0.296
# c) Avec 2 clusters, KMeans fusionne des groupes et le score chute. Il
#    trouve TOUJOURS le nombre de groupes qu'on lui demande : c'est à nous
#    de choisir k (méthode du coude, score de silhouette, connaissance du
#    domaine…).


#################################
#  Fuite de données et éthique  #
#################################

"""
16. Sans exécuter : dans chacun des cas suivants, y a-t-il une fuite de
    données ? Pourquoi ?
        a) On normalise X avec un StandardScaler, puis on coupe en
           train/test.
        b) Pour prédire si un patient sera hospitalisé, on utilise la
           colonne "nombre de jours d'hospitalisation".
        c) On coupe en train/test, puis on met StandardScaler et le modèle
           dans un pipeline qu'on entraîne sur le train.
        d) Les données contiennent plusieurs radios de chaque patient, et
           on coupe en train/test au hasard, radio par radio.

a) OUI : les moyennes et écarts-types utilisés pour normaliser ont été
   calculés en incluant le jeu de test. (L'effet est souvent faible pour un
   StandardScaler, mais c'est une mauvaise habitude, et l'effet peut être
   énorme pour d'autres étapes, comme la sélection de features.)
b) OUI : cette information n'existe qu'APRÈS l'hospitalisation. Au moment
   de prédire, on ne l'a pas. Le modèle aurait un score parfait… et
   inutilisable.
c) NON : c'est la bonne méthode.
d) OUI : des radios du même patient se retrouvent dans le train et dans le
   test. Le modèle peut "reconnaître le patient" plutôt que la maladie. Il
   faut couper par patient (cf. GroupShuffleSplit dans scikit-learn).

17. Le code ci-dessous contient une fuite de données. Corrigez-le.

        normaliseur = StandardScaler().fit(X_cancer)
        X_norm = normaliseur.transform(X_cancer)
        X_tr, X_te, y_tr, y_te = train_test_split(X_norm, y_cancer,
                                                  random_state=0)
        modele = KNeighborsClassifier().fit(X_tr, y_tr)
        print(modele.score(X_te, y_te))

Le normaliseur est entraîné sur TOUTES les données, test compris. On coupe
d'abord, puis on met la normalisation dans un pipeline, entraîné sur le
train seulement :
"""
X_tr, X_te, y_tr, y_te = train_test_split(X_cancer, y_cancer,
                                          random_state=0)
modele = make_pipeline(StandardScaler(), KNeighborsClassifier())
modele.fit(X_tr, y_tr)
print(round(modele.score(X_te, y_te), 3))  # => 0.951

"""
18. Sans exécuter : une banque veut un modèle qui accorde ou refuse les
    crédits, entraîné sur ses décisions des 20 dernières années. Citez deux
    risques éthiques, et deux vérifications à faire avant de l'utiliser.

Risques :
    - le modèle reproduit les biais des décisions passées : si certains
      groupes (femmes, quartiers, origines…) ont été défavorisés, il
      apprendra à les défavoriser, en paraissant "objectif",
    - des variables innocentes en apparence (code postal, prénom…) peuvent
      servir de substitut à des informations sensibles,
    - les clients refusés n'ont jamais pu montrer qu'ils auraient remboursé :
      les données ne disent rien d'eux,
    - une décision automatique et inexplicable est difficile à contester.
Vérifications :
    - comparer les performances et les taux d'acceptation entre groupes,
    - vérifier quelles variables sont utilisées, et retirer celles qui sont
      sensibles ou qui les révèlent indirectement,
    - pouvoir expliquer chaque décision au client, et garder un contrôle
      humain (c'est une exigence du RGPD et de l'AI Act pour le crédit).
"""


#################
#  Mini-projet  #
#################

"""
19. Sur le jeu de données load_wine() (cf. chapitre), menez la démarche
    complète :
        1. découpage train/test (25 %, stratifié, random_state=0),
        2. baseline,
        3. comparaison par validation croisée d'un arbre de décision et
           d'un RandomForestClassifier (from sklearn.ensemble ; une
           "forêt" de nombreux arbres, random_state=0), et d'un kNN
           normalisé,
        4. évaluation UNE seule fois du meilleur modèle sur le test, avec
           sa matrice de confusion.
"""
vins = load_wine(as_frame=True)
X_vin, y_vin = vins.data, vins.target

# 1. Découpage, en tout premier
Xw_train, Xw_test, yw_train, yw_test = train_test_split(
    X_vin, y_vin, test_size=0.25, random_state=0, stratify=y_vin
)

# 2. et 3. Baseline et comparaison, par validation croisée sur le train
candidats = {
    "baseline": DummyClassifier(),
    "arbre": DecisionTreeClassifier(random_state=0),
    "forêt": RandomForestClassifier(random_state=0),
    "kNN normalisé": make_pipeline(StandardScaler(), KNeighborsClassifier()),
}
for nom, modele in candidats.items():
    scores = cross_val_score(modele, Xw_train, yw_train, cv=5)
    print(f"{nom:>14} : {scores.mean():.3f}")
# =>       baseline : 0.399
# =>          arbre : 0.896
# =>          forêt : 0.955
# =>  kNN normalisé : 0.940

# 4. Le meilleur (la forêt), évalué une seule fois sur le test
meilleur = RandomForestClassifier(random_state=0).fit(Xw_train, yw_train)
print(round(meilleur.score(Xw_test, yw_test), 3))  # => 1.0
print(confusion_matrix(yw_test, meilleur.predict(Xw_test)))
# => [[15  0  0]
# =>  [ 0 18  0]
# =>  [ 0  0 12]]
# Une forêt combine les votes de nombreux arbres, chacun entraîné sur une
# partie des données : elle sur-apprend beaucoup moins qu'un arbre seul.
# Elle n'a pas besoin de normalisation (comme les arbres).
