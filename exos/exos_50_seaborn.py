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
#  Chap. 50     #  Seaborn : exercices                                         #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", essayez de prévoir le résultat
avant de lancer le programme.

Ces exercices nécessitent seaborn (qui installe aussi NumPy, pandas et
matplotlib). Comme dans le chapitre, les graphiques sont enregistrés en PNG
avec la fonction enregistrer() définie ci-dessous, puis supprimés à la fin.
Pour les regarder, passez GARDER_IMAGES à True. (Dans vos propres programmes,
vous pouvez utiliser plt.show() à la place.)

Les corrigés sont dans le fichier corrs/corr_50_seaborn.py.
"""

import os
import sys
import warnings

try:
    import numpy as np
    import pandas as pd
    import matplotlib
    import seaborn as sns
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("Ces exercices ont besoin de seaborn : lancez \"uv add seaborn\"")
    print("(ou \"pip install seaborn\"), puis relancez ce programme.")
    sys.exit(0)

matplotlib.use("Agg")  # pas de fenêtre (cf. chap. 40)
import matplotlib.pyplot as plt  # noqa: E402

# Masque les avertissements de dépréciation de seaborn 0.13 (cf. chapitre)
warnings.filterwarnings("ignore", category=DeprecationWarning,
                        module="seaborn")
warnings.filterwarnings("ignore", category=PendingDeprecationWarning,
                        module="seaborn")

GARDER_IMAGES = False
images_creees = []


def enregistrer(figure, nom_fichier):
    """Enregistre la figure dans un fichier PNG, puis la ferme."""
    figure.savefig(nom_fichier, bbox_inches="tight")
    plt.close(figure)
    images_creees.append(nom_fichier)


#################
#  Préparation  #
#################

# Ne modifiez pas ce bloc : il crée les données utilisées par les exercices.
# 250 clients d'une boutique en ligne et physique (données inventées).
rng = np.random.default_rng(seed=7)
n = 250
canal = rng.choice(["web", "boutique"], size=n, p=[0.6, 0.4])
age = rng.integers(18, 76, size=n)
panier = 20 + 0.8 * age + np.where(canal == "web", 15, 0)
panier = (panier + rng.normal(0, 12, size=n)).round(2)  # montant en euros
clients = pd.DataFrame({
    "canal": canal,
    "region": rng.choice(["Nord", "Sud", "Ouest"], size=n),
    "age": age,
    "panier": panier,
    "satisfaction": rng.integers(1, 6, size=n),  # note de 1 à 5
})

# Ventes mensuelles (en milliers d'euros) de trois magasins, format "large"
ventes_larges = pd.DataFrame({
    "mois": range(1, 13),
    "Lyon": [42, 40, 45, 47, 50, 52, 48, 39, 51, 55, 60, 75],
    "Lille": [35, 33, 36, 38, 40, 41, 37, 30, 42, 44, 50, 66],
    "Nantes": [28, 27, 30, 33, 35, 37, 36, 31, 34, 37, 41, 55],
})


################################################
#  Des données "tidy" et fonctions de seaborn  #
################################################

"""
1. Sans exécuter :
       a) Quelle est la différence entre une fonction "axes-level" (comme
          histplot) et une fonction "figure-level" (comme displot) ? Que
          renvoie chacune ?
       b) Que se passe-t-il si on écrit sns.relplot(…, ax=ax) ?
       c) Le DataFrame clients est-il au format "tidy" ? Et ventes_larges ?

2. Transformez ventes_larges au format long avec melt(), dans un DataFrame
   ventes aux colonnes "mois", "magasin" et "ventes". Affichez sa forme
   (shape) et ses 3 premières lignes.
"""


########################
#  Thèmes et palettes  #
########################

"""
3. Sans exécuter : quelle famille de palette (qualitative, séquentielle ou
   divergente) choisiriez-vous pour colorer :
       a) les régions (Nord, Sud, Ouest) ?
       b) une température en °C sur une carte ?
       c) l'écart des ventes par rapport à l'objectif (en %, positif ou
          négatif) ?
       d) une matrice de corrélation ?

4. Appliquez le thème "ticks", puis créez une palette "colorblind" de 4
   couleurs. Affichez sa longueur. Pourquoi cette palette est-elle un bon
   choix par défaut ?
"""


#######################
#  Les distributions  #
#######################

"""
5. Tracez l'histogramme des paniers (colonne "panier") avec 25 intervalles.
   Affichez le nombre de barres dessinées, et le nom de l'axe des x.
   Enregistrez dans exo50_histo.png.

6. Tracez sur un même graphique la densité (KDE) des paniers pour chaque
   canal (hue). Combien de courbes ont été tracées ? Enregistrez dans
   exo50_kde.png.

7. Tracez la fonction de répartition (ecdfplot) des paniers. Puis calculez
   avec pandas la proportion de clients dont le panier est inférieur ou égal
   à 60 € : c'est la hauteur de la courbe en x = 60. Enregistrez dans
   exo50_ecdf.png.
"""


###################################
#  Les relations entre variables  #
###################################

"""
8. Tracez le nuage de points (âge, panier), avec une couleur par canal.
   Vérifiez que le graphique contient bien 250 points. Enregistrez dans
   exo50_nuage.png.

9. Tracez le même nuage avec regplot (sans hue), puis calculez la pente de
   la droite de régression avec np.polyfit. Interprétez-la en une phrase.
   Enregistrez dans exo50_reg.png.

10. Tracez l'évolution des ventes mois par mois, une courbe par magasin, à
    partir du DataFrame ventes de l'exercice 2. Combien d'entrées la légende
    contient-elle ? Enregistrez dans exo50_ventes.png.
"""


#################################
#  Les variables catégorielles  #
#################################

"""
11. Tracez un barplot du panier moyen par région (ordre : Nord, Sud,
    Ouest). Récupérez la hauteur des barres et comparez-la au résultat d'un
    groupby. Que représentent les petits traits au sommet des barres ?
    Enregistrez dans exo50_barres.png.

12. Avec countplot, tracez le nombre de clients pour chaque note de
    satisfaction (1 à 5). Affichez la liste des effectifs. Enregistrez dans
    exo50_satisfaction.png.

13. Comparez la distribution des paniers selon le canal : un boxplot, avec
    les points des clients superposés (stripplot). Enregistrez dans
    exo50_box.png.
"""


#############################################
#  Encoder plus d'informations et facettes  #
#############################################

"""
14. Tracez le nuage (âge, panier) en encodant le canal par la couleur ET la
    forme des points, et la satisfaction par la taille. Pourquoi est-il
    utile de doubler la couleur par la forme ? Enregistrez dans
    exo50_encodage.png.

15. Avec relplot, faites un nuage (âge, panier) par région, côte à côte
    (col=), dans l'ordre Nord, Sud, Ouest. Affichez la forme de grille.axes,
    puis changez les titres en "Région Nord", etc. Enregistrez dans
    exo50_facettes.png.
"""


############################################
#  Matrices, pairplot et personnalisation  #
############################################

"""
16. Calculez la matrice de corrélation (arrondie à 2 décimales) entre "age",
    "panier" et "satisfaction". Affichez-la, puis tracez-la avec une heatmap
    annotée, une palette divergente centrée sur 0, entre -1 et 1. Quelle
    variable n'est liée à aucune autre ? Enregistrez dans exo50_corr.png.

17. Avec pivot_table, calculez le panier moyen par région (lignes) et par
    canal (colonnes), arrondi à 1 décimale. Affichez-le, puis tracez-le en
    heatmap annotée. Enregistrez dans exo50_pivot.png.

18. Tracez un pairplot des colonnes "age", "panier" et "satisfaction", avec
    une couleur par canal. Quelle est la forme de grille.axes ? Enregistrez
    dans exo50_pairplot.png.
"""


##############################################
#  Bonnes pratiques et graphiques trompeurs  #
##############################################

"""
19. Le graphique ci-dessous est trompeur et peu lisible. Trouvez au moins
    4 défauts, puis refaites-le correctement dans exo50_corrige.png.
"""
fig, ax = plt.subplots()
sns.barplot(data=clients, x="region", y="panier", hue="region",
            palette="rainbow", errorbar=None, ax=ax)
ax.set_ylim(55, 65)
ax.set_xlabel("")
ax.set_ylabel("")
enregistrer(fig, "exo50_mauvais.png")

"""
20. Mini-projet : en une seule figure de 2 × 2 graphiques (plt.subplots(2,
    2) et ax=…), présentez les clients : la distribution des âges, le
    nombre de clients par canal, le panier selon le canal (boxplot), et le
    lien entre âge et panier. Donnez un titre à chaque graphique et un titre
    général (fig.suptitle). Enregistrez dans exo50_tableau_de_bord.png.
"""


###############
#  Nettoyage  #
###############

plt.close("all")
if not GARDER_IMAGES:
    for nom_fichier in images_creees:
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
