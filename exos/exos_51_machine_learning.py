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
#  Chap. 51     #  Introduction au Machine Learning : exercices                #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", essayez de prévoir le résultat
avant de lancer le programme.

Ces exercices nécessitent scikit-learn et pandas. Tous les jeux de données
utilisés sont inclus dans scikit-learn ou générés ci-dessous : pas besoin
d'Internet.

IMPT : utilisez random_state=0 partout où il y a du hasard (découpage,
modèles), pour obtenir les mêmes résultats que les corrigés.

Les corrigés sont dans le fichier corrs/corr_51_machine_learning.py.
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

2. Pour le jeu de données "breast cancer" (X_cancer, y_cancer) :
       a) affichez la forme de X_cancer et de y_cancer ; que représentent
          les lignes ? les colonnes ?
       b) affichez les noms des deux classes (cancer.target_names),
       c) affichez le nombre de tumeurs de chaque classe. Les classes
          sont-elles équilibrées ?
"""


##################################
#  Séparer entraînement et test  #
##################################

"""
3. Coupez X_cancer et y_cancer en un jeu d'entraînement (80 %) et un jeu de
   test (20 %), avec random_state=0 et en gardant les proportions des
   classes. Affichez la forme des deux X, puis la proportion de tumeurs
   bénignes (classe 1) dans chacun des deux y, arrondie à 3 décimales.

4. Sans exécuter : pourquoi ne faut-il pas évaluer un modèle sur les données
   qui ont servi à l'entraîner ? Et pourquoi utilise-t-on stratify=y ?
"""


########################################
#  Baseline, kNN et arbre de décision  #
########################################

"""
5. Calculez l'exactitude (accuracy) d'un DummyClassifier qui prédit toujours
   la classe la plus fréquente, sur le jeu de test. Expliquez la valeur
   obtenue à partir de l'exercice 2 c).

6. Entraînez un KNeighborsClassifier (paramètres par défaut) sur les données
   brutes, et affichez son exactitude sur le test. Puis faites de même avec
   un pipeline StandardScaler + KNeighborsClassifier. Pourquoi une telle
   différence ? (Indice : regardez le min et le max des colonnes "mean area"
   et "smoothness error".)

7. Entraînez un arbre de décision de profondeur 3 (random_state=0).
   Affichez son exactitude sur le test, puis les 3 features les plus
   importantes (feature_importances_) avec leur importance arrondie à 2
   décimales.
"""


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


#############################################
#  Sur-apprentissage et validation croisée  #
#############################################

"""
9. Pour des arbres de décision de profondeur 1, 2, 3, 5, 8 et sans limite
   (None), affichez le score d'entraînement et le score de test. À partir de
   quelle profondeur l'arbre connaît-il le jeu d'entraînement par cœur ?
   Quelle profondeur choisiriez-vous ?

10. Comparez par validation croisée à 5 plis, sur le jeu d'ENTRAÎNEMENT,
    les trois modèles suivants, et affichez pour chacun la moyenne des
    scores (3 décimales) :
        - un DummyClassifier,
        - un arbre de décision de profondeur 3 (random_state=0),
        - le pipeline StandardScaler + KNeighborsClassifier.

11. Avec GridSearchCV (5 plis), cherchez la meilleure valeur de
    n_neighbors parmi 1, 3, 5, 7, 11, 15, 21 pour le pipeline kNN normalisé.
    Affichez la meilleure valeur, le meilleur score de validation croisée,
    puis le score du modèle final sur le jeu de test.
"""


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


################################
#  Prétraitement et pipelines  #
################################

"""
13. Encodez la colonne "carburant" des 5 premières voitures avec un
    OneHotEncoder. Affichez le tableau obtenu et les noms des nouvelles
    colonnes. Que se passe-t-il si on encode ensuite une voiture "hybride" ?
    Comment l'éviter ?

14. Reprenez l'exercice 12 en utilisant AUSSI la colonne "carburant", grâce
    à un ColumnTransformer (StandardScaler sur les colonnes numériques,
    OneHotEncoder sur "carburant") dans un pipeline. Le R² sur le test
    s'améliore-t-il ? Prédisez le prix d'une voiture électrique de 4 ans
    ayant 60 000 km.
"""


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

17. Le code ci-dessous contient une fuite de données. Corrigez-le.

        normaliseur = StandardScaler().fit(X_cancer)
        X_norm = normaliseur.transform(X_cancer)
        X_tr, X_te, y_tr, y_te = train_test_split(X_norm, y_cancer,
                                                  random_state=0)
        modele = KNeighborsClassifier().fit(X_tr, y_tr)
        print(modele.score(X_te, y_te))

18. Sans exécuter : une banque veut un modèle qui accorde ou refuse les
    crédits, entraîné sur ses décisions des 20 dernières années. Citez deux
    risques éthiques, et deux vérifications à faire avant de l'utiliser.
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
