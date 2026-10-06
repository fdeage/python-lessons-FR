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
#  Chap. 51     #  Introduction au Machine Learning                            #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Installer et importer scikit-learn
#  - Le vocabulaire du Machine Learning
#  - Les grandes familles de problèmes
#  - Un premier jeu de données : les iris
#  - Séparer entraînement et test
#  - Le point de départ : une baseline
#  - La régression linéaire
#  - Classification : les k plus proches voisins
#  - Classification : l'arbre de décision
#  - Évaluer un classifieur
#  - Sur-apprentissage et sous-apprentissage
#  - Prétraitement : normaliser et encoder
#  - Les pipelines
#  - La validation croisée
#  - Régler les hyperparamètres
#  - Non supervisé : le clustering avec KMeans
#  - Le piège de la fuite de données
#  - Éthique et biais
#  - Pour aller plus loin
#
##############################

# Introduction
###############

"""
En programmation "classique", c'est NOUS qui écrivons les règles :

    données + règles (le programme)  ──►  réponses

Par exemple, pour classer un e-mail comme spam, on écrirait des if :
"si le message contient 'gagnant' et 'cliquez ici', alors c'est un spam"
(cf. chap. 12). Mais ces règles sont difficiles à trouver, nombreuses, et
les spammeurs s'adaptent…

En Machine Learning ("apprentissage automatique"), on renverse le problème :
on donne à l'ordinateur des EXEMPLES (des données et leurs bonnes réponses),
et c'est lui qui TROUVE les règles :

    données + réponses (des exemples)  ──►  règles (un "modèle")

Puis on utilise ce modèle pour prédire la réponse sur de NOUVELLES données,
qu'il n'a jamais vues.

Exemples d'applications : filtres anti-spam, recommandations de films,
reconnaissance d'images, détection de fraude bancaire, prévision des ventes,
diagnostic médical assisté, traduction automatique…

Ce chapitre est une INTRODUCTION : on y voit la démarche complète et les
pièges classiques, avec des modèles simples. On privilégie l'intuition : pas
besoin de mathématiques avancées pour commencer.

Prérequis : NumPy (chap. 38) et pandas (chap. 39).

Note : ce chapitre a été vérifié avec scikit-learn 1.9. Les résultats sont
reproductibles grâce au paramètre random_state (cf. plus bas), mais certains
chiffres peuvent varier légèrement avec une autre version.
"""


# Installer et importer scikit-learn
#####################################

"""
La bibliothèque de référence pour le Machine Learning "classique" en Python
est scikit-learn (souvent abrégée "sklearn"). Elle s'installe à part (cf.
chap. 22 et 47). Dans un projet géré avec uv :
    ?> uv add scikit-learn pandas
ou, avec pip :
    ?> pip install scikit-learn pandas

Attention : le paquet s'appelle "scikit-learn", mais le module qu'on importe
s'appelle "sklearn".

On n'importe jamais "tout sklearn" : on importe chaque outil depuis son
sous-module (sklearn.model_selection, sklearn.linear_model…). On les
importera au fur et à mesure du chapitre, pour bien voir d'où ils viennent.
"""
import sys

try:
    import numpy as np
    import pandas as pd
    import sklearn
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("Ce chapitre a besoin de scikit-learn et de pandas : lancez")
    print("\"uv add scikit-learn pandas\" (ou \"pip install scikit-learn")
    print("pandas\"), puis relancez ce programme.")
    sys.exit(0)

print(sklearn.__version__)  # => 1.9.1 (variable : dépend de l'installation)


# Le vocabulaire du Machine Learning
#####################################

"""
Imaginons qu'on veuille prédire le prix d'un appartement. On dispose d'un
tableau de ventes passées :

    surface   pieces   distance_centre   │  prix
    ───────────────────────────────────────┼────────
      45        2          3.0             │  210 000
      80        4          8.5             │  290 000
      …         …          …               │  …

    - Chaque LIGNE est un "échantillon" (sample), ou "observation" : ici, un
      appartement vendu.
    - Les colonnes qui servent à prédire sont les "caractéristiques"
      (features), ou "variables explicatives". On les range dans un tableau
      2D appelé X (avec un X majuscule, par convention : c'est une matrice).
    - Ce qu'on veut prédire est la "cible" (target), ou "étiquette" (label).
      On la range dans un tableau 1D appelé y (minuscule : c'est un vecteur).
    - Le "modèle" est l'objet qui apprend le lien entre X et y.
    - L'"entraînement" (training, ou "fit") est la phase où le modèle
      apprend, à partir d'exemples dont on connaît la réponse.
    - La "prédiction" (predict) est l'utilisation du modèle entraîné sur de
      nouvelles données, dont on ne connaît PAS la réponse.

IMPT : X a toujours la forme (nombre d'échantillons, nombre de features), et
y la forme (nombre d'échantillons,). Il y a autant de lignes dans X que de
valeurs dans y.
"""


# Les grandes familles de problèmes
####################################

"""
1. L'apprentissage SUPERVISÉ : on connaît la bonne réponse y pour les
   exemples d'entraînement (un "superviseur" a étiqueté les données).
       - RÉGRESSION : y est un NOMBRE (un prix, une température, une durée…)
       - CLASSIFICATION : y est une CATÉGORIE (spam / pas spam, une espèce de
         fleur, un chiffre manuscrit de 0 à 9…)

2. L'apprentissage NON SUPERVISÉ : on n'a PAS de y. On cherche une structure
   cachée dans X, par exemple des groupes d'individus qui se ressemblent
   ("clustering" : segmenter des clients, regrouper des articles…).

(Il existe d'autres familles, comme l'apprentissage par renforcement, où un
agent apprend par essais et erreurs, avec des récompenses : jeux, robotique…
Elles dépassent le cadre de ce chapitre.)

3. L'API de scikit-learn

Toute la force de scikit-learn est que TOUS ses modèles s'utilisent de la
même façon (on dit qu'ils ont la même "API", "Application Programming
Interface" : la même interface de programmation) :

    modele = UnModele(parametres)     # 1. créer le modèle (cf. chap. 34)
    modele.fit(X_train, y_train)      # 2. l'entraîner sur des exemples
    y_pred = modele.predict(X_test)   # 3. prédire sur de nouvelles données
    modele.score(X_test, y_test)      # 4. mesurer sa performance

Et les outils de préparation des données (les "transformers") ont la même
logique, avec fit() puis transform() (cf. "Prétraitement").

Changer de modèle revient donc souvent à changer UNE ligne.
"""


# Un premier jeu de données : les iris
#######################################

"""
scikit-learn fournit quelques petits jeux de données célèbres, directement
inclus dans la bibliothèque (pas besoin d'Internet). Le plus connu : les
iris de Fisher (1936). 150 fleurs de 3 espèces (setosa, versicolor,
virginica), avec 4 mesures en cm : longueur et largeur des sépales et des
pétales. Objectif : reconnaître l'espèce à partir des mesures. C'est un
problème de CLASSIFICATION.

as_frame=True demande les données sous forme de DataFrame pandas (cf.
chap. 39).
"""
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
X = iris.data      # un DataFrame : les 4 features
y = iris.target    # une Series : l'espèce, codée 0, 1 ou 2
print(X.shape)  # => (150, 4)
print(y.shape)  # => (150,)
for colonne in X.columns:
    print(colonne)
# => sepal length (cm)
# => sepal width (cm)
# => petal length (cm)
# => petal width (cm)
print(iris.target_names.tolist())  # => ['setosa', 'versicolor', 'virginica']

"""
Avant TOUT modèle, on explore les données (cf. chap. 39 et 50) : combien
d'exemples par classe ? Les features ont-elles l'air utiles ?
"""
print(y.value_counts().sort_index().to_dict())  # => {0: 50, 1: 50, 2: 50}
moyennes = X.groupby(y).mean().round(2)
moyennes.index = iris.target_names
print(moyennes[["petal length (cm)", "petal width (cm)"]])
# =>             petal length (cm)  petal width (cm)
# => setosa                   1.46              0.25
# => versicolor               4.26              1.33
# => virginica                5.55              2.03

"""
Les classes sont parfaitement équilibrées (50 fleurs chacune), et la taille
des pétales semble très différente d'une espèce à l'autre : un modèle devrait
pouvoir s'en servir.
"""


# Séparer entraînement et test
###############################

"""
Question cruciale : comment savoir si un modèle est BON ?

Mauvaise idée : le tester sur les données qui ont servi à l'entraîner. Un
modèle peut "apprendre par cœur" ses exemples, comme un élève qui connaît
les corrigés des exercices… sans avoir compris le cours. Il aurait 20/20 sur
les exercices déjà vus, et échouerait sur de nouveaux.

IMPT : on évalue TOUJOURS un modèle sur des données qu'il n'a JAMAIS vues.

On coupe donc les données en deux :
    - un jeu d'ENTRAÎNEMENT (train), en général 70 à 80 % des données,
      sur lequel le modèle apprend,
    - un jeu de TEST (test), les 20 à 30 % restants, mis de côté jusqu'à la
      fin et utilisé UNE fois pour mesurer la performance.

train_test_split() mélange les données au hasard, puis les coupe :
    - test_size=0.25 : 25 % pour le test,
    - random_state=0 : la "graine" du hasard (cf. chap. 22 et 38), pour
      obtenir le même découpage à chaque exécution,
    - stratify=y : garder les mêmes proportions de chaque classe dans les
      deux jeux (sinon, par malchance, une espèce pourrait manquer au test).
"""
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0, stratify=y
)
print(X_train.shape, X_test.shape)  # => (112, 4) (38, 4)
print(y_test.value_counts().sort_index().to_dict())  # => {0: 13, 1: 13, 2: 12}

"""
Attention à l'ordre des 4 valeurs renvoyées : X_train, X_test, y_train,
y_test. Une erreur ici fausse tout le reste !
"""


# Le point de départ : une baseline
####################################

"""
Avant de se réjouir d'un score, il faut le comparer à une référence : la
"baseline" (ligne de base). C'est le score d'un modèle "idiot", qui ne
regarde même pas les features. Par exemple, prédire toujours la classe la
plus fréquente.

Si votre modèle sophistiqué ne fait pas mieux que la baseline, il n'a rien
appris d'utile !

scikit-learn fournit ces modèles idiots : DummyClassifier (classification)
et DummyRegressor (régression). Remarquez l'API commune : fit, puis score.
Pour un classifieur, score() renvoie l'"exactitude" (accuracy) : la
proportion de bonnes réponses, entre 0 et 1.
"""
from sklearn.dummy import DummyClassifier

baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)
print(round(baseline.score(X_test, y_test), 3))  # => 0.316

"""
Avec 3 classes équilibrées, répondre toujours la même espèce donne environ
1 bonne réponse sur 3. Tout modèle sérieux devra faire beaucoup mieux.

IMPT : une exactitude de 95 % n'est PAS forcément un bon résultat. Si 95 %
des transactions bancaires sont honnêtes, un modèle qui répond toujours
"honnête" a 95 % d'exactitude… et ne détecte aucune fraude !
"""


# La régression linéaire
#########################

"""
Commençons par une RÉGRESSION : prédire un nombre. On génère des ventes
d'appartements fictives (cf. chap. 38) : le prix dépend de la surface, du
nombre de pièces et de la distance au centre-ville, plus une part de hasard
(le "bruit" : deux appartements identiques ne se vendent pas au même prix).
"""
rng = np.random.default_rng(seed=0)
n = 500
appartements = pd.DataFrame({
    "surface": rng.uniform(20, 120, n).round(),
    "pieces": rng.integers(1, 6, n),
    "distance_centre": rng.uniform(0, 15, n).round(1),
})
appartements["prix"] = (
    3000 * appartements["surface"]
    + 8000 * appartements["pieces"]
    - 6000 * appartements["distance_centre"]
    + 50_000
    + rng.normal(0, 20_000, n)
).round(-2)
print(appartements.head(3))
# =>    surface  pieces  distance_centre      prix
# => 0     84.0       3              3.7  277100.0
# => 1     47.0       1             11.6  134500.0
# => 2     24.0       1             11.4   49800.0

"""
La régression linéaire cherche la formule de la forme :

    prix ≈ a × surface + b × pieces + c × distance_centre + d

qui colle "au mieux" aux exemples, c'est-à-dire qui minimise les erreurs
(plus précisément, la somme des carrés des erreurs). Les nombres a, b, c
s'appellent les COEFFICIENTS, et d l'ORDONNÉE À L'ORIGINE (intercept). C'est
la même idée que la droite de régression du chap. 50, mais avec plusieurs
features.
"""
from sklearn.linear_model import LinearRegression

X_app = appartements[["surface", "pieces", "distance_centre"]]
y_app = appartements["prix"]
Xa_train, Xa_test, ya_train, ya_test = train_test_split(
    X_app, y_app, test_size=0.2, random_state=0
)  # (pas de stratify : y est un nombre, pas une catégorie)

regression = LinearRegression()
regression.fit(Xa_train, ya_train)

# Les paramètres APPRIS se terminent par un "_" dans scikit-learn :
for feature, coef in zip(X_app.columns, regression.coef_):
    print(f"{feature:>16} : {coef:>9.0f}")
# =>          surface :      2996
# =>           pieces :      9182
# =>  distance_centre :     -5800
print(int(round(regression.intercept_, -3)))  # => 46000

"""
Le modèle a retrouvé à peu près les vrais coefficients utilisés pour
générer les données (3000, 8000, -6000) ! Et on peut les INTERPRÉTER :
chaque m² ajoute environ 3000 € au prix, chaque km d'éloignement du centre
en retire environ 6000 €. C'est un grand avantage de la régression
linéaire : elle n'est pas une "boîte noire".

Prédire le prix d'un nouvel appartement (65 m², 3 pièces, à 2 km du
centre). Attention : predict() attend un tableau 2D, avec les mêmes
colonnes que pour l'entraînement, même pour UN seul appartement :
"""
nouveau = pd.DataFrame({"surface": [65], "pieces": [3],
                        "distance_centre": [2.0]})
print(int(round(regression.predict(nouveau)[0], -3)))  # => 257000

"""
Mesurer l'erreur d'une régression : on compare les prix prédits aux vrais
prix du jeu de test.
    - MAE (Mean Absolute Error) : l'erreur moyenne, en valeur absolue, dans
      l'unité de y (ici, en euros). Très facile à interpréter.
    - RMSE (Root Mean Squared Error) : la racine de la moyenne des erreurs
      au carré. Toujours dans l'unité de y, mais pénalise plus les grosses
      erreurs.
    - R² (coefficient de détermination) : la part de la variation de y que
      le modèle explique. 1 = parfait ; 0 = pas mieux que de prédire
      toujours la moyenne ; peut même être négatif pour un très mauvais
      modèle. C'est ce que renvoie regression.score().
"""
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ya_pred = regression.predict(Xa_test)
mae = mean_absolute_error(ya_test, ya_pred)
rmse = mean_squared_error(ya_test, ya_pred) ** 0.5
print(f"MAE  : {mae:.0f} €")  # => MAE  : 18953 €
print(f"RMSE : {rmse:.0f} €")  # => RMSE : 22684 €
print(round(r2_score(ya_test, ya_pred), 3))  # => 0.938
print(round(regression.score(Xa_test, ya_test), 3))  # => 0.938 (le même R²)

"""
Le modèle se trompe en moyenne d'environ 19 000 € : c'est cohérent avec le
"bruit" de 20 000 € qu'on a ajouté, et qu'aucun modèle ne peut deviner. La
baseline ferait beaucoup moins bien :
"""
from sklearn.dummy import DummyRegressor

baseline_reg = DummyRegressor(strategy="mean")  # prédit toujours la moyenne
baseline_reg.fit(Xa_train, ya_train)
mae_base = mean_absolute_error(ya_test, baseline_reg.predict(Xa_test))
print(f"MAE baseline : {mae_base:.0f} €")  # => MAE baseline : 78202 €

"""
(Le jeu de données intégré load_diabetes(), sur la progression du diabète,
permet de s'entraîner sur une vraie régression : cf. exercices.)
"""


# Classification : les k plus proches voisins
##############################################

"""
Retour aux iris. Premier classifieur, le plus intuitif qui soit : les "k
plus proches voisins" (k-Nearest Neighbors, kNN).

Pour classer une nouvelle fleur :
    1. on cherche, parmi les fleurs d'entraînement, les k fleurs dont les
       mesures sont les plus PROCHES (au sens de la distance, comme sur une
       carte),
    2. on regarde leurs espèces,
    3. on prédit l'espèce majoritaire parmi ces k voisins (un "vote").

"Dis-moi qui sont tes voisins, je te dirai qui tu es."

L'"entraînement" consiste simplement à mémoriser les exemples : tout le
travail se fait au moment de la prédiction.
"""
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
print(round(knn.score(X_test, y_test), 3))  # => 1.0

fleur = pd.DataFrame([[5.0, 3.4, 1.5, 0.2]], columns=X.columns)
print(iris.target_names[knn.predict(fleur)[0]])  # => setosa

"""
Bien mieux que la baseline ! n_neighbors (k) est un HYPERPARAMÈTRE : un
réglage choisi par NOUS avant l'entraînement (et non appris par le modèle).
    - k trop petit (k=1) : le modèle suit chaque exemple, y compris les
      erreurs ou les cas bizarres,
    - k trop grand : il "lisse" trop et ignore les détails (avec k = toutes
      les fleurs, il prédit toujours la classe majoritaire… comme la
      baseline).
On verra comment choisir k dans "Régler les hyperparamètres".

predict_proba() donne, pour chaque classe, la proportion des voisins qui
ont "voté" pour elle :
"""
print(knn.predict_proba(fleur))  # => [[1. 0. 0.]]


# Classification : l'arbre de décision
#######################################

"""
Deuxième classifieur : l'arbre de décision. Il apprend une suite de
questions du type "la largeur du pétale est-elle ≤ 0.8 cm ?", comme un
jeu des "20 questions" ou un organigramme de if/else (cf. chap. 12) :

                  largeur pétale ≤ 0.8 ?
                    /                 \\
                 oui                   non
                  |                     |
               setosa         largeur pétale ≤ 1.75 ?
                                /             \\
                             oui               non
                              |                 |
                          versicolor         virginica

À chaque étape, l'algorithme choisit la question qui SÉPARE le mieux les
classes. max_depth limite le nombre de questions successives (la
"profondeur" de l'arbre).
"""
from sklearn.tree import DecisionTreeClassifier, export_text

arbre = DecisionTreeClassifier(max_depth=2, random_state=0)
arbre.fit(X_train, y_train)
print(round(arbre.score(X_test, y_test), 3))  # => 0.947

"""
Grand avantage : on peut lire les règles apprises, avec export_text() :
"""
print(export_text(arbre, feature_names=list(X.columns)))
# => |--- petal width (cm) <= 0.80
# => |   |--- class: 0
# => |--- petal width (cm) >  0.80
# => |   |--- petal width (cm) <= 1.75
# => |   |   |--- class: 1
# => |   |--- petal width (cm) >  1.75
# => |   |   |--- class: 2

"""
(class: 0, 1, 2 correspondent à setosa, versicolor, virginica.) Ce sont
exactement les règles du dessin ci-dessus : le modèle a "découvert" tout
seul que la largeur des pétales suffit presque à distinguer les espèces.

L'arbre indique aussi l'importance de chaque feature dans ses décisions
(entre 0 et 1, total 1) :
"""
for feature, importance in zip(X.columns, arbre.feature_importances_):
    print(f"{feature:>17} : {importance:.2f}")
# => sepal length (cm) : 0.00
# =>  sepal width (cm) : 0.00
# => petal length (cm) : 0.00
# =>  petal width (cm) : 1.00

"""
Avec seulement 2 questions, l'arbre n'a utilisé qu'une feature : la largeur
des pétales a toute l'importance.
"""


# Évaluer un classifieur
#########################

"""
L'exactitude (accuracy) résume tout en un nombre… et cache les détails.
Quelles classes le modèle confond-il ?

1. La MATRICE DE CONFUSION : un tableau qui croise les vraies classes
(lignes) et les classes prédites (colonnes). La diagonale contient les
bonnes réponses, le reste les erreurs.
"""
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)

y_pred = arbre.predict(X_test)
print(round(accuracy_score(y_test, y_pred), 3))  # => 0.947
print(confusion_matrix(y_test, y_pred))
# => [[13  0  0]
# =>  [ 0 13  0]
# =>  [ 0  2 10]]

"""
Lecture : toutes les setosa (1re ligne) sont bien classées. Les erreurs ont
lieu entre versicolor et virginica, deux espèces plus proches.

2. Précision, rappel et F1, calculés pour CHAQUE classe. Prenons la classe
"virginica" :
    - PRÉCISION : parmi les fleurs que le modèle a déclarées "virginica",
      combien le sont vraiment ? ("Quand il dit virginica, a-t-il raison ?")
    - RAPPEL (recall) : parmi les vraies virginica, combien le modèle en
      a-t-il trouvé ? ("Les a-t-il toutes repérées ?")
    - F1 : une moyenne (harmonique) des deux, pour avoir un seul nombre.

Pour un test médical de dépistage, on veut un très bon RAPPEL (ne rater
aucun malade, quitte à avoir de fausses alertes). Pour un filtre anti-spam,
on veut une très bonne PRÉCISION (ne jamais jeter un vrai message).

classification_report() affiche tout cela d'un coup. ("support" est le
nombre d'exemples de chaque classe dans le jeu de test.)
"""
print(classification_report(y_test, y_pred, target_names=iris.target_names))
# =>               precision    recall  f1-score   support
# =>
# =>       setosa       1.00      1.00      1.00        13
# =>   versicolor       0.87      1.00      0.93        13
# =>    virginica       1.00      0.83      0.91        12
# =>
# =>     accuracy                           0.95        38
# =>    macro avg       0.96      0.94      0.95        38
# => weighted avg       0.95      0.95      0.95        38


# Sur-apprentissage et sous-apprentissage
##########################################

"""
Deux défauts opposés guettent tout modèle :

    - le SOUS-apprentissage (underfitting) : le modèle est trop simple pour
      capturer la structure des données. Il est mauvais partout, à
      l'entraînement comme au test.
    - le SUR-apprentissage (overfitting) : le modèle est trop complexe. Il
      apprend "par cœur" les exemples, y compris leur bruit et leurs
      exceptions. Il est excellent à l'entraînement… et décevant au test.

L'objectif : un modèle qui GÉNÉRALISE, c'est-à-dire qui fonctionne bien sur
des données nouvelles.

Démonstration avec un jeu de données plus difficile, généré par
make_classification() : 400 exemples, 2 classes, 10 features dont 5
utiles, et 20 % d'étiquettes tirées au hasard (flip_y) pour simuler des
erreurs de saisie.
"""
from sklearn.datasets import make_classification

X_diff, y_diff = make_classification(
    n_samples=400, n_features=10, n_informative=5, flip_y=0.2,
    random_state=2,
)
Xd_train, Xd_test, yd_train, yd_test = train_test_split(
    X_diff, y_diff, test_size=0.3, random_state=0, stratify=y_diff
)

print("profondeur  train   test")
for profondeur in [1, 2, 3, 5, 8, 12, None]:
    modele = DecisionTreeClassifier(max_depth=profondeur, random_state=0)
    modele.fit(Xd_train, yd_train)
    score_train = modele.score(Xd_train, yd_train)
    score_test = modele.score(Xd_test, yd_test)
    print(f"{str(profondeur):>10}  {score_train:.3f}  {score_test:.3f}")
# => profondeur  train   test
# =>          1  0.714  0.775
# =>          2  0.821  0.800
# =>          3  0.857  0.825
# =>          5  0.900  0.792
# =>          8  0.964  0.750
# =>         12  1.000  0.700
# =>       None  1.000  0.700

"""
(max_depth=None : l'arbre grandit sans limite.) Lecture du tableau :
    - à faible profondeur, les deux scores sont moyens : SOUS-apprentissage,
    - plus l'arbre est profond, plus le score d'entraînement monte, jusqu'à
      1.000 (100 % : il connaît chaque exemple par cœur, même les
      étiquettes fausses !),
    - mais le score de test, lui, monte puis redescend : au-delà d'une
      certaine profondeur, c'est du SUR-apprentissage. Ici, le meilleur
      compromis est une profondeur de 3 (0.825 au test), alors que l'arbre
      sans limite tombe à 0.700 malgré son 100 % à l'entraînement.

IMPT : un grand écart entre le score d'entraînement et le score de test est
le signe d'un sur-apprentissage. Le bon modèle est celui qui a le meilleur
score sur des données NON vues.
"""


# Prétraitement : normaliser et encoder
########################################

"""
Les modèles ne travaillent qu'avec des NOMBRES, et certains sont sensibles à
l'ÉCHELLE de ces nombres. Il faut souvent préparer les données : c'est le
"prétraitement" (preprocessing).

1. Normaliser les features numériques

Le kNN calcule des distances. Si une feature va de 0 à 1000 et une autre de
0 à 1, la première écrase complètement la seconde dans le calcul ! Exemple
avec le jeu de données intégré "wine" : 178 vins, 13 mesures chimiques aux
échelles très différentes, 3 cépages à reconnaître.
"""
from sklearn.datasets import load_wine

vins = load_wine(as_frame=True)
X_vin, y_vin = vins.data, vins.target
print(X_vin[["proline", "hue"]].describe().loc[["min", "max"]])
# =>      proline   hue
# => min    278.0  0.48
# => max   1680.0  1.71

Xv_train, Xv_test, yv_train, yv_test = train_test_split(
    X_vin, y_vin, test_size=0.3, random_state=0, stratify=y_vin
)
knn_brut = KNeighborsClassifier().fit(Xv_train, yv_train)
print(round(knn_brut.score(Xv_test, yv_test), 3))  # => 0.722

"""
(fit() renvoie le modèle lui-même : on peut enchaîner .fit(…) dès la
création.)

La solution : le StandardScaler, qui transforme chaque feature pour qu'elle
ait une moyenne de 0 et un écart-type de 1 (on soustrait la moyenne, puis on
divise par l'écart-type). Toutes les features ont alors la même échelle.

C'est un "transformer" : il a la même API que les modèles, avec transform()
au lieu de predict() :
    - fit(X_train) : APPRENDRE la moyenne et l'écart-type de chaque feature,
      sur le jeu d'entraînement SEULEMENT,
    - transform(X) : appliquer la transformation (à X_train ET à X_test,
      avec les moyennes apprises sur X_train).
"""
from sklearn.preprocessing import StandardScaler

normaliseur = StandardScaler()
normaliseur.fit(Xv_train)
Xv_train_norm = normaliseur.transform(Xv_train)
Xv_test_norm = normaliseur.transform(Xv_test)
print(Xv_train_norm.mean(axis=0).round(2)[:3])  # => [0. 0. 0.]
print(Xv_train_norm.std(axis=0).round(2)[:3])  # => [1. 1. 1.]

knn_norm = KNeighborsClassifier().fit(Xv_train_norm, yv_train)
print(round(knn_norm.score(Xv_test_norm, yv_test), 3))  # => 0.963

"""
Spectaculaire ! Même modèle, mêmes données, mais normalisées.
(Les arbres de décision, eux, ne sont pas sensibles à l'échelle : une
question "proline ≤ 755 ?" marche quelle que soit l'unité.)

2. Encoder les features catégorielles

Une colonne de texte comme "quartier" ("nord", "sud", "centre") ne peut pas
être donnée telle quelle à un modèle. La solution classique est
l'encodage "one-hot" : une colonne de 0/1 par catégorie possible.

    quartier            quartier_centre  quartier_nord  quartier_sud
    ────────            ───────────────  ─────────────  ────────────
    nord        ──►            0               1              0
    centre                     1               0              0
    sud                        0               0              1

(Pourquoi pas simplement nord=0, centre=1, sud=2 ? Parce que le modèle en
déduirait un ORDRE et des distances qui n'existent pas : "sud" serait
"2 fois plus" que "centre".)
"""
from sklearn.preprocessing import OneHotEncoder

quartiers = pd.DataFrame({"quartier": ["nord", "centre", "sud", "nord"]})
encodeur = OneHotEncoder()
print(encodeur.fit_transform(quartiers).toarray())
# => [[0. 1. 0.]
# =>  [1. 0. 0.]
# =>  [0. 0. 1.]
# =>  [0. 1. 0.]]
print(list(encodeur.get_feature_names_out()))
# => ['quartier_centre', 'quartier_nord', 'quartier_sud']

"""
fit_transform() fait fit() puis transform() en une fois. (toarray()
convertit le résultat, stocké sous une forme compacte dite "creuse", en
tableau NumPy normal.)

Erreur classique : une catégorie jamais vue pendant l'entraînement.
"""
try:
    encodeur.transform(pd.DataFrame({"quartier": ["est"]}))
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
"""
La solution : OneHotEncoder(handle_unknown="ignore"), qui encode une
catégorie inconnue par une ligne de 0.
"""


# Les pipelines
################

"""
Normaliser à la main, puis entraîner, puis penser à normaliser AUSSI le jeu
de test… c'est fastidieux, et source d'erreurs. Un Pipeline enchaîne les
étapes dans un seul objet, qui s'utilise ensuite comme un modèle :
    - pipeline.fit(X_train, y_train) : fit + transform de chaque étape de
      prétraitement, puis fit du modèle final,
    - pipeline.predict(X_test) : transform de chaque étape (avec ce qui a été
      appris sur X_train), puis predict.

make_pipeline() crée un pipeline en nommant les étapes automatiquement.
"""
from sklearn.pipeline import make_pipeline

pipeline_vin = make_pipeline(StandardScaler(), KNeighborsClassifier())
pipeline_vin.fit(Xv_train, yv_train)
print(round(pipeline_vin.score(Xv_test, yv_test), 3))  # => 0.963
print(list(pipeline_vin.named_steps))
# => ['standardscaler', 'kneighborsclassifier']

"""
Même score qu'à la main, en 2 lignes, et sans risque d'oublier une étape.

Pour des données MIXTES (des colonnes numériques et des colonnes de texte),
on applique un traitement différent selon les colonnes avec un
ColumnTransformer. Ajoutons un quartier à nos appartements :
"""
from sklearn.compose import ColumnTransformer

appartements["quartier"] = rng.choice(["nord", "centre", "sud"], n)
bonus_quartier = appartements["quartier"].map(
    {"nord": 0, "centre": 40_000, "sud": 10_000}
)
appartements["prix"] = appartements["prix"] + bonus_quartier

colonnes_num = ["surface", "pieces", "distance_centre"]
colonnes_cat = ["quartier"]
preparation = ColumnTransformer([
    ("num", StandardScaler(), colonnes_num),
    ("cat", OneHotEncoder(handle_unknown="ignore"), colonnes_cat),
])
pipeline_app = make_pipeline(preparation, LinearRegression())

X_app2 = appartements[colonnes_num + colonnes_cat]
y_app2 = appartements["prix"]
Xa2_train, Xa2_test, ya2_train, ya2_test = train_test_split(
    X_app2, y_app2, test_size=0.2, random_state=0
)
pipeline_app.fit(Xa2_train, ya2_train)
print(round(pipeline_app.score(Xa2_test, ya2_test), 3))  # => 0.935

nouveau = pd.DataFrame({"surface": [65], "pieces": [3],
                        "distance_centre": [2.0], "quartier": ["centre"]})
print(int(round(pipeline_app.predict(nouveau)[0], -3)))  # => 298000

"""
IMPT : en pratique, on met TOUJOURS le prétraitement dans un pipeline. On
verra plus bas que c'est aussi ce qui protège de la "fuite de données".
"""


# La validation croisée
########################

"""
Un seul découpage train/test, c'est un peu de la chance : avec un autre
random_state, le score aurait été un peu différent. Surtout avec peu de
données (30 % de 178 vins = 54 vins de test seulement).

La VALIDATION CROISÉE (cross-validation) répète l'expérience :
    1. on coupe les données en k parts égales ("folds"), par ex. k = 5,
    2. on entraîne sur 4 parts et on teste sur la 5e,
    3. on recommence 5 fois, en changeant à chaque fois la part de test,
    4. on obtient 5 scores, dont on regarde la moyenne et la dispersion.

    tour 1 : [TEST] [ ent ] [ ent ] [ ent ] [ ent ]
    tour 2 : [ ent ] [TEST] [ ent ] [ ent ] [ ent ]
    …
    tour 5 : [ ent ] [ ent ] [ ent ] [ ent ] [TEST]

Chaque exemple sert une fois au test. cross_val_score() fait tout cela :
"""
from sklearn.model_selection import cross_val_score

scores = cross_val_score(pipeline_vin, Xv_train, yv_train, cv=5)
print(scores.round(3))  # => [0.96 0.92 0.92 0.92 1.  ]
print(f"{scores.mean():.3f} ± {scores.std():.3f}")  # => 0.944 ± 0.032

"""
On fait la validation croisée sur le jeu d'ENTRAÎNEMENT : le jeu de test
reste caché jusqu'à la toute fin (cf. section suivante).

C'est l'outil idéal pour COMPARER des modèles de façon fiable :
"""
for nom, modele in [
    ("baseline", DummyClassifier()),
    ("arbre", DecisionTreeClassifier(random_state=0)),
    ("kNN normalisé", make_pipeline(StandardScaler(),
                                    KNeighborsClassifier())),
]:
    scores = cross_val_score(modele, Xv_train, yv_train, cv=5)
    print(f"{nom:>14} : {scores.mean():.3f}")
# =>       baseline : 0.403
# =>          arbre : 0.872
# =>  kNN normalisé : 0.944


# Régler les hyperparamètres
#############################

"""
Quelle valeur de k pour le kNN ? Quelle profondeur pour l'arbre ? Plutôt que
de deviner, on les essaie toutes, et on garde la meilleure… selon la
VALIDATION CROISÉE.

IMPT : ne choisissez JAMAIS un hyperparamètre d'après le score sur le jeu de
test ! Sinon, le test a servi à faire un choix, et il n'est plus une mesure
honnête sur des données "jamais vues".

GridSearchCV essaie toutes les combinaisons d'une "grille" de valeurs, avec
une validation croisée pour chacune. Dans un pipeline, on désigne un
paramètre par "nomdeletape__parametre" (deux "_").
"""
from sklearn.model_selection import GridSearchCV

grille = {"kneighborsclassifier__n_neighbors": [1, 5, 15, 25, 35, 50, 75]}
recherche = GridSearchCV(pipeline_vin, grille, cv=5)
recherche.fit(Xv_train, yv_train)

# Le score moyen de validation croisée pour chaque valeur essayée :
for k, score in zip(grille["kneighborsclassifier__n_neighbors"],
                    recherche.cv_results_["mean_test_score"]):
    print(f"k = {k:>2} : {score:.3f}")
# => k =  1 : 0.920
# => k =  5 : 0.944
# => k = 15 : 0.944
# => k = 25 : 0.976
# => k = 35 : 0.960
# => k = 50 : 0.952
# => k = 75 : 0.581
print(recherche.best_params_)
# => {'kneighborsclassifier__n_neighbors': 25}
print(round(recherche.best_score_, 3))  # => 0.976

"""
Le meilleur k est un compromis : ni 1 (trop sensible à chaque exemple), ni
75 (avec 124 vins d'entraînement, chaque vote mélange presque tous les
cépages : sous-apprentissage). Si le meilleur score avait été au BORD de la
grille, il aurait fallu essayer des valeurs plus loin.

GridSearchCV ré-entraîne automatiquement le meilleur modèle sur tout le jeu
d'entraînement. C'est seulement MAINTENANT, une fois tous les choix faits,
qu'on l'évalue UNE fois sur le jeu de test :
"""
print(round(recherche.score(Xv_test, yv_test), 3))  # => 0.981

"""
La démarche complète d'un projet de ML supervisé :
    1. explorer les données,
    2. mettre de côté un jeu de test,
    3. établir une baseline,
    4. comparer des modèles (dans des pipelines) par validation croisée,
    5. régler les hyperparamètres du meilleur, par validation croisée,
    6. évaluer UNE fois le modèle final sur le jeu de test.
"""


# Non supervisé : le clustering avec KMeans
############################################

"""
Sans étiquettes y, peut-on trouver des groupes ? C'est le CLUSTERING.
Exemple : une entreprise veut segmenter ses clients selon leur
comportement, sans savoir à l'avance quels groupes existent.

L'algorithme KMeans cherche k groupes ("clusters") :
    1. il place k centres au hasard,
    2. il affecte chaque point au centre le plus proche,
    3. il déplace chaque centre au milieu (la moyenne) de ses points,
    4. il recommence les étapes 2 et 3 jusqu'à ce que plus rien ne bouge.

Testons-le sur des données générées avec make_blobs() : 300 points en 2D,
répartis en 3 "tas". On connaît les vrais groupes, mais on ne les donne PAS
à KMeans (pas de y dans fit !).
"""
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X_blobs, vrais_groupes = make_blobs(n_samples=300, centers=3,
                                    cluster_std=1.0, random_state=1)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0)
kmeans.fit(X_blobs)          # pas de y : apprentissage non supervisé
groupes = kmeans.labels_     # le numéro de groupe trouvé pour chaque point
print(np.bincount(groupes))  # => [100 100 100] : nombre de points par groupe
print(kmeans.cluster_centers_.round(1))
# => [[ -1.5   4.4]
# =>  [-10.1  -3.9]
# =>  [ -7.1  -8. ]]

"""
Les numéros de groupes sont arbitraires (le "groupe 0" de KMeans n'a aucune
raison d'être le "groupe 0" de make_blobs). Pour comparer, on utilise un
score qui ne dépend pas des numéros, l'"Adjusted Rand Index" (1 = groupes
identiques, 0 = groupes faits au hasard) :
"""
from sklearn.metrics import adjusted_rand_score

print(round(adjusted_rand_score(vrais_groupes, groupes), 3))  # => 0.98

"""
KMeans a retrouvé les groupes sans jamais voir les étiquettes. Limites :
    - il faut choisir k soi-même (des méthodes aident : "méthode du coude",
      score de silhouette),
    - il trouve des groupes "ronds" et de tailles comparables,
    - il est sensible à l'échelle : normalisez d'abord (StandardScaler) !
    - il trouve TOUJOURS k groupes, même s'il n'y a aucune structure dans
      les données : c'est à vous de vérifier que les groupes ont un sens.
"""


# Le piège de la fuite de données
##################################

"""
La "fuite de données" (data leakage) est l'erreur la plus dangereuse du ML :
une information du jeu de test (ou du futur) "fuit" dans l'entraînement. Le
score est alors excellent… et complètement faux. Le modèle s'effondre une
fois en production.

Exemples :
    - normaliser ou sélectionner des features sur TOUTES les données AVANT
      de couper train/test (le modèle a "vu" le test à travers les moyennes
      ou la sélection),
    - utiliser une feature qui n'existe qu'APRÈS coup (prédire si un client
      va résilier son contrat… avec la colonne "date de résiliation"),
    - avoir des doublons, ou plusieurs lignes d'un même patient, à la fois
      dans le train et dans le test.

Démonstration spectaculaire : des données PUREMENT aléatoires (100
exemples, 5000 features de bruit, des étiquettes tirées à pile ou face).
Aucun modèle ne peut faire mieux que 50 % : il n'y a RIEN à apprendre.
"""
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import LogisticRegression

rng_bruit = np.random.default_rng(seed=0)
X_bruit = rng_bruit.normal(size=(100, 5000))
y_bruit = rng_bruit.integers(0, 2, size=100)

"""
MAUVAISE méthode : on sélectionne d'abord les 20 features "les plus liées"
à y, sur TOUTES les données, puis on fait une validation croisée.
(LogisticRegression est, malgré son nom, un classifieur linéaire classique.)
"""
selection = SelectKBest(k=20).fit(X_bruit, y_bruit)  # fuite : voit tout y !
X_selection = selection.transform(X_bruit)
scores_faux = cross_val_score(LogisticRegression(), X_selection, y_bruit,
                              cv=5)
print(round(scores_faux.mean(), 2))  # => 0.85 : trop beau pour être vrai !

"""
BONNE méthode : la sélection fait partie du pipeline. À chaque tour de
validation croisée, elle n'est apprise QUE sur la partie entraînement.
"""
pipeline_propre = make_pipeline(SelectKBest(k=20), LogisticRegression())
scores_justes = cross_val_score(pipeline_propre, X_bruit, y_bruit, cv=5)
print(round(scores_justes.mean(), 2))  # => 0.48 : le hasard, comme attendu

"""
Parmi 5000 features aléatoires, certaines sont liées à y PAR HASARD. En les
choisissant sur toutes les données, on a "triché" sans le vouloir.

Bonnes pratiques :
    - couper train/test en TOUT PREMIER, avant toute préparation,
    - mettre tout le prétraitement dans un pipeline,
    - se méfier d'un score "trop beau",
    - se demander, pour chaque feature : "aurai-je vraiment cette information
      au moment de faire la prédiction ?"
"""


# Éthique et biais
###################

"""
Un modèle apprend à partir des données qu'on lui donne… y compris leurs
biais. Quelques exemples réels :
    - un outil de recrutement entraîné sur dix ans de CV d'une entreprise
      tech, où la plupart des recrues étaient des hommes, a appris à
      pénaliser les CV mentionnant des activités féminines (Amazon, 2018),
    - des systèmes de reconnaissance faciale bien moins précis sur les
      visages à peau foncée, sous-représentés dans les données
      d'entraînement (étude "Gender Shades", 2018).

Questions à se poser :
    - Les données d'entraînement sont-elles REPRÉSENTATIVES de la population
      sur laquelle le modèle sera utilisé ?
    - Le modèle est-il aussi performant pour TOUS les groupes ? (Calculez les
      scores par groupe, pas seulement le score global.)
    - Utilise-t-il, directement ou indirectement, des informations
      sensibles (origine, sexe, âge…) ? Supprimer la colonne ne suffit pas :
      le code postal, par exemple, peut révéler l'origine sociale.
    - Ses décisions peuvent-elles être expliquées et contestées ?
    - Les données personnelles sont-elles protégées ? En Europe, le RGPD
      encadre leur utilisation, et l'AI Act (2024) réglemente les systèmes
      d'IA à haut risque (recrutement, crédit, santé…).

IMPT : un modèle n'est pas "objectif" parce qu'il est mathématique. Il
reproduit, et parfois amplifie, les biais de ses données.
"""


# Pour aller plus loin
#######################

"""
Ce chapitre n'est qu'un début. Pour continuer :
    - d'autres modèles de scikit-learn, qui s'utilisent EXACTEMENT de la même
      façon : RandomForestClassifier (une "forêt" de nombreux arbres, très
      robuste), GradientBoostingClassifier, LogisticRegression, SVC…
    - la documentation de scikit-learn, avec un excellent guide utilisateur
      et des exemples : https://scikit-learn.org/stable/user_guide.html
    - le MOOC gratuit "Machine learning in Python with scikit-learn",
      créé par l'Inria (les développeurs de scikit-learn) :
      https://inria.github.io/scikit-learn-mooc/
    - le Deep Learning (réseaux de neurones : images, texte, son), avec
      PyTorch ou Keras, une fois les bases de ce chapitre maîtrisées,
    - Kaggle (https://www.kaggle.com) : des jeux de données réels et des
      compétitions pour pratiquer.
"""
