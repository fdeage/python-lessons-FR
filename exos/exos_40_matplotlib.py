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
#  Chap. 40     #  Matplotlib : exercices                                      #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", essayez de prévoir le résultat
avant de lancer le programme.

Ces exercices nécessitent NumPy et matplotlib (pandas pour l'exercice 13).
Comme dans le chapitre, les graphiques sont enregistrés en PNG avec la
fonction enregistrer() définie ci-dessous, puis supprimés à la fin. Pour les
regarder, passez GARDER_IMAGES à True. (Dans vos propres programmes, vous
pouvez utiliser plt.show() à la place.)

Les corrigés sont dans le fichier corr_40_matplotlib.py.
"""

import os
import sys

try:
    import numpy as np
    import matplotlib
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("Ces exercices ont besoin de NumPy et de matplotlib : lancez")
    print("\"pip install numpy matplotlib\", puis relancez ce programme.")
    sys.exit(0)

matplotlib.use("Agg")  # pas de fenêtre (cf. chapitre)
import matplotlib.pyplot as plt  # noqa: E402

GARDER_IMAGES = False
images_creees = []


def enregistrer(figure, nom_fichier):
    """Enregistre la figure dans un fichier PNG, puis la ferme."""
    figure.savefig(nom_fichier)
    plt.close(figure)
    images_creees.append(nom_fichier)


#################
#  Préparation  #
#################

# Ne modifiez pas ce bloc : il crée les données utilisées par les exercices.
mois = ["jan", "fév", "mar", "avr", "mai", "jun",
        "jul", "aoû", "sep", "oct", "nov", "déc"]
temp_paris = [5, 6, 10, 13, 16, 20, 22, 22, 18, 14, 9, 6]
temp_marseille = [8, 9, 12, 15, 19, 23, 26, 26, 22, 18, 12, 9]
pluie_paris = [50, 40, 48, 52, 63, 50, 62, 52, 48, 61, 50, 55]  # en mm

rng = np.random.default_rng(seed=1)
temps_trajet = rng.normal(35, 8, size=200).round()  # 200 trajets, en minutes


#######################################################
#  Afficher ou enregistrer ? plt.show() et savefig()  #
#######################################################

"""
1. Sans exécuter :
       a) Quelle est la différence entre plt.show() et plt.savefig() ?
       b) Pourquoi faut-il fermer une figure (plt.close()) après savefig()
          quand on crée beaucoup de graphiques ?
       c) Pourquoi le chapitre appelle-t-il matplotlib.use("Agg") ? Faut-il
          le faire dans vos propres programmes ?
"""


###################################
#  Un premier graphique : plot()  #
###################################

"""
2. Tracez la courbe des températures de Paris (temp_paris) en fonction des
   mois, et enregistrez-la dans exo40_paris.png.

3. Sans exécuter, quelles abscisses matplotlib utilise-t-il pour
   plt.plot([3, 1, 4]) ? Et que se passe-t-il avec
   plt.plot([1, 2, 3], [4, 5]) ?
"""


############################
#  Titre, axes et légende  #
############################

"""
4. Reprenez l'exercice 2 et tracez sur le MÊME graphique les températures de
   Paris et de Marseille. Ajoutez un titre, le nom des axes (avec l'unité),
   une légende et une grille. Enregistrez dans exo40_villes.png.
"""


#############################
#  Les types de graphiques  #
#############################

"""
5. Pour chacune des questions suivantes, quel type de graphique choisiriez-
   vous ?
       a) Le nombre d'habitants des 10 plus grandes villes de France.
       b) L'évolution du cours d'une action sur un an.
       c) La relation entre la surface d'un appartement et son prix.
       d) La répartition des âges des clients d'un magasin.
       e) La part de chaque parti dans une élection.
       f) La comparaison des salaires de 3 services, avec les valeurs
          extrêmes.

6. Tracez un graphique en barres de la pluie mensuelle à Paris
   (pluie_paris). Enregistrez dans exo40_pluie.png.

7. Tracez l'histogramme des temps de trajet (temps_trajet) avec 15
   intervalles. Récupérez les effectifs renvoyés par plt.hist() et affichez
   le nombre de trajets dans l'intervalle le plus fréquent. Enregistrez dans
   exo40_trajets.png.

8. Tracez le nuage de points (température, pluie) pour Paris : y a-t-il un
   lien visible entre la température d'un mois et la pluie ? Enregistrez
   dans exo40_nuage.png.
"""


##########################################################
#  Plusieurs graphiques : subplots et l'interface objet  #
##########################################################

"""
9. Avec fig, axes = plt.subplots(1, 2, figsize=(10, 4)), tracez côte à côte :
       - à gauche, les températures des deux villes (courbes),
       - à droite, la pluie à Paris (barres).
   Donnez un titre à chaque graphique et un titre général à la figure.
   Affichez la forme du tableau axes, et le titre du graphique de gauche
   (avec .get_title()). Enregistrez dans exo40_double.png.

10. Traduisez ce code en interface objet (fig, ax = plt.subplots()) :
        fig = plt.figure()
        plt.plot(mois, temp_paris)
        plt.title("Paris")
        plt.xlabel("Mois")
        plt.ylim(0, 30)
"""


###################################################
#  Personnaliser : couleurs, styles, annotations  #
###################################################

"""
11. Tracez les températures de Marseille en rouge, avec des ronds à chaque
    point et une ligne en tirets. Ajoutez une ligne horizontale à la
    température moyenne de l'année, et une annotation avec une flèche sur le
    mois le plus chaud (le premier, s'il y en a plusieurs). Enregistrez dans
    exo40_marseille.png.
"""


#########################
#  Tracer depuis NumPy  #
#########################

"""
12. Avec np.linspace(), tracez sur le même graphique les fonctions
    f(x) = x², g(x) = 2x et h(x) = x³ / 4, pour x entre -3 et 3. Combien de
    points faut-il, à peu près, pour que les courbes paraissent lisses ?
    Enregistrez dans exo40_fonctions.png.
"""


##########################
#  Tracer depuis pandas  #
##########################

"""
13. (Nécessite pandas.) Créez un DataFrame avec les colonnes paris et
    marseille (les températures), et les mois pour index. En une ligne avec
    .plot(), tracez les deux courbes ; puis, avec kind="bar", les barres
    groupées. Nommez l'axe des y. Enregistrez dans exo40_pandas_*.png.
"""


####################################
#  Bonnes pratiques de lisibilité  #
####################################

"""
14. Trouvez au moins 4 problèmes dans ces deux graphiques (qui montrent les
    mêmes données), puis remplacez-les par un seul graphique correct, en
    interface objet. Enregistrez-le dans exo40_corrige.png.
"""
ventes_produits = {"Produit A": 1520, "Produit B": 1480, "Produit C": 1610}

fig = plt.figure()
plt.pie(list(ventes_produits.values()), labels=list(ventes_produits))
plt.title("graphique")
enregistrer(fig, "exo40_mauvais.png")

fig = plt.figure()
plt.plot(list(ventes_produits), list(ventes_produits.values()))
plt.ylim(1450, 1650)
enregistrer(fig, "exo40_mauvais_2.png")


###############
#  Nettoyage  #
###############

if not GARDER_IMAGES:
    for nom_fichier in images_creees:
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
