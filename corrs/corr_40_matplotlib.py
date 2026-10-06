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
#  Chap. 40     #  Matplotlib : corrigés                                       #
#               #                                                              #
################################################################################

"""
Ces corrigés ont été vérifiés avec matplotlib 3.11, NumPy 2.5 et pandas 3.0.

Un graphique ne peut pas être vérifié par un `# =>`. Pour regarder les
images, passez GARDER_IMAGES à True et relancez : les fichiers exo40_*.png
apparaissent dans le répertoire courant. Pour vérifier quand même nos
graphiques dans le terminal, on interroge les objets matplotlib :
    - ax.get_title(), ax.get_xlabel(), ax.get_ylabel() : les textes,
    - len(ax.lines) : le nombre de courbes tracées,
    - len(ax.patches) : le nombre de barres (ou de rectangles),
    - ax.get_ylim() : les bornes de l'axe des y.
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

    a) plt.show() AFFICHE le graphique dans une fenêtre (ou dans un notebook)
       et met le programme en pause jusqu'à ce qu'on ferme la fenêtre.
       plt.savefig("nom.png") ENREGISTRE le graphique dans un fichier image,
       sans rien afficher ; le format est déduit de l'extension.

    b) Chaque figure reste en mémoire tant qu'elle n'est pas fermée. Avec des
       dizaines de graphiques, la mémoire se remplit, et matplotlib affiche
       un avertissement au-delà de 20 figures ouvertes.

    c) "Agg" dessine les images sans ouvrir de fenêtre : le fichier peut
       ainsi s'exécuter partout (même sans écran) et d'une traite. Dans vos
       programmes, ce n'est en général PAS nécessaire : matplotlib choisit
       tout seul un backend capable d'ouvrir des fenêtres.
"""


###################################
#  Un premier graphique : plot()  #
###################################

"""
2. Tracez la courbe des températures de Paris (temp_paris) en fonction des
   mois, et enregistrez-la dans exo40_paris.png.
"""
fig = plt.figure()
plt.plot(mois, temp_paris)
enregistrer(fig, "exo40_paris.png")

"""
Les abscisses peuvent être des chaînes : matplotlib place alors les
catégories à intervalles réguliers, dans l'ordre de la liste.

3. Sans exécuter, quelles abscisses matplotlib utilise-t-il pour
   plt.plot([3, 1, 4]) ? Et que se passe-t-il avec
   plt.plot([1, 2, 3], [4, 5]) ?

Avec une seule liste, celle-ci donne les ORDONNÉES, et les abscisses sont les
indices 0, 1, 2. Avec deux listes de longueurs différentes, c'est une erreur.
"""
fig, ax = plt.subplots()
lignes = ax.plot([3, 1, 4])
print(lignes[0].get_xdata())  # => [0. 1. 2.]
try:
    ax.plot([1, 2, 3], [4, 5])
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
plt.close(fig)

"""
(plot() renvoie la liste des courbes créées : on peut leur demander leurs
coordonnées avec .get_xdata() et .get_ydata().)
"""


############################
#  Titre, axes et légende  #
############################

"""
4. Reprenez l'exercice 2 et tracez sur le MÊME graphique les températures de
   Paris et de Marseille. Ajoutez un titre, le nom des axes (avec l'unité),
   une légende et une grille. Enregistrez dans exo40_villes.png.
"""
fig = plt.figure()
plt.plot(mois, temp_paris, label="Paris")        # label= : texte de la
plt.plot(mois, temp_marseille, label="Marseille")  # légende pour chaque courbe
plt.title("Températures moyennes mensuelles")
plt.xlabel("Mois")
plt.ylabel("Température (°C)")
plt.legend()
plt.grid(True)

ax = plt.gca()  # "get current axes" : l'Axes courant, pour le vérifier
print(len(ax.lines))    # => 2 (deux courbes)
print(ax.get_ylabel())  # => Température (°C)
enregistrer(fig, "exo40_villes.png")

"""
Sans label=, plt.legend() n'aurait rien à afficher (et matplotlib afficherait
un avertissement).
"""


#############################
#  Les types de graphiques  #
#############################

"""
5. Pour chacune des questions suivantes, quel type de graphique choisiriez-
   vous ?
       a) Le nombre d'habitants des 10 plus grandes villes de France.
          → Des BARRES (comparer des catégories), de préférence horizontales
            (barh) car les noms de villes sont longs, et triées.
       b) L'évolution du cours d'une action sur un an.
          → Une COURBE (une valeur qui évolue dans le temps).
       c) La relation entre la surface d'un appartement et son prix.
          → Un NUAGE DE POINTS (lien entre deux grandeurs numériques).
       d) La répartition des âges des clients d'un magasin.
          → Un HISTOGRAMME (répartition d'une variable numérique).
       e) La part de chaque parti dans une élection.
          → Des BARRES, triées. Le camembert est tentant, mais l'œil compare
            mal les angles (cf. chapitre).
       f) La comparaison des salaires de 3 services, avec les valeurs
          extrêmes.
          → Des BOÎTES À MOUSTACHES (boxplot), une par service.

6. Tracez un graphique en barres de la pluie mensuelle à Paris
   (pluie_paris). Enregistrez dans exo40_pluie.png.
"""
fig, ax = plt.subplots()
ax.bar(mois, pluie_paris)
ax.set_title("Pluie mensuelle à Paris")
ax.set_ylabel("Précipitations (mm)")
print(len(ax.patches))  # => 12 (une barre par mois)
enregistrer(fig, "exo40_pluie.png")

"""
7. Tracez l'histogramme des temps de trajet (temps_trajet) avec 15
   intervalles. Récupérez les effectifs renvoyés par plt.hist() et affichez
   le nombre de trajets dans l'intervalle le plus fréquent. Enregistrez dans
   exo40_trajets.png.
"""
fig, ax = plt.subplots()
effectifs, bornes, _ = ax.hist(temps_trajet, bins=15)
ax.set_title("Répartition des temps de trajet (200 trajets)")
ax.set_xlabel("Durée (minutes)")
ax.set_ylabel("Nombre de trajets")
print(len(effectifs), len(bornes))  # => 15 16
print(int(effectifs.max()))         # => 39
i = effectifs.argmax()  # l'indice de l'intervalle le plus fréquent
print(f"de {bornes[i]:.1f} à {bornes[i + 1]:.1f} min")  # => de 34.0 à 37.0 min
enregistrer(fig, "exo40_trajets.png")

"""
hist() renvoie trois choses : les effectifs (un tableau NumPy de 15
valeurs), les bornes des intervalles (16 valeurs : il y a toujours une borne
de plus que d'intervalles) et les rectangles dessinés (ignorés avec "_").
L'intervalle le plus fréquent est bien autour de 35 minutes, la moyenne
choisie pour générer les données.
"""

"""
8. Tracez le nuage de points (température, pluie) pour Paris : y a-t-il un
   lien visible entre la température d'un mois et la pluie ? Enregistrez
   dans exo40_nuage.png.
"""
fig, ax = plt.subplots()
ax.scatter(temp_paris, pluie_paris)
ax.set_title("Paris : pluie et température, par mois")
ax.set_xlabel("Température moyenne (°C)")
ax.set_ylabel("Précipitations (mm)")
enregistrer(fig, "exo40_nuage.png")

"""
Les points sont assez dispersés : on devine au mieux une légère tendance
(les mois chauds sont un peu plus pluvieux), mais pas de lien net. On peut
le mesurer par un calcul : le coefficient de corrélation, compris entre -1
(lien décroissant parfait) et 1 (lien croissant parfait), 0 signifiant
"aucun lien linéaire".
"""
print(np.corrcoef(temp_paris, pluie_paris)[0, 1].round(2))  # => 0.42
"""
0.42 est un lien faible à modéré. Et avec seulement 12 points (un par mois),
il serait imprudent de conclure : le nuage de points sert à EXPLORER, pas à
prouver.
"""


##########################################################
#  Plusieurs graphiques : subplots et l'interface objet  #
##########################################################

"""
9. Avec fig, axes = plt.subplots(1, 2, figsize=(10, 4)), tracez côte à côte
   les températures des deux villes et la pluie à Paris. Donnez un titre à
   chaque graphique et un titre général à la figure. Affichez la forme du
   tableau axes, et le titre du graphique de gauche.
"""
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
print(axes.shape)  # => (2,)  (une seule ligne : le tableau est 1D)

axes[0].plot(mois, temp_paris, label="Paris")
axes[0].plot(mois, temp_marseille, label="Marseille")
axes[0].set_title("Températures (°C)")
axes[0].legend()

axes[1].bar(mois, pluie_paris)
axes[1].set_title("Pluie à Paris (mm)")

fig.suptitle("Le climat en un coup d'œil")
fig.tight_layout()
print(axes[0].get_title())  # => Températures (°C)
enregistrer(fig, "exo40_double.png")

"""
10. Traduisez ce code en interface objet (fig, ax = plt.subplots()).

Les fonctions de réglage prennent le préfixe "set_" ; plot() ne change pas.
"""
fig, ax = plt.subplots()
ax.plot(mois, temp_paris)
ax.set_title("Paris")
ax.set_xlabel("Mois")
ax.set_ylim(0, 30)
print(ax.get_ylim())  # => (np.float64(0.0), np.float64(30.0))
plt.close(fig)

"""
(get_ylim() renvoie un tuple de deux nombres NumPy, d'où l'affichage
"np.float64(…)" depuis NumPy 2 ; avec NumPy 1, on lirait (0.0, 30.0).)
"""


###################################################
#  Personnaliser : couleurs, styles, annotations  #
###################################################

"""
11. Tracez les températures de Marseille en rouge, avec des ronds à chaque
    point et une ligne en tirets. Ajoutez une ligne horizontale à la
    température moyenne de l'année, et une annotation avec une flèche sur le
    mois le plus chaud (le premier, s'il y en a plusieurs).
"""
fig, ax = plt.subplots()
ax.plot(mois, temp_marseille, color="red", marker="o", linestyle="--",
        label="Marseille")

moyenne = np.mean(temp_marseille)
print(round(moyenne, 1))  # => 16.6
ax.axhline(moyenne, color="gray", linestyle=":",
           label=f"Moyenne annuelle ({moyenne:.1f} °C)")

# argmax() renvoie l'indice du PREMIER maximum : juillet (indice 6).
i_max = int(np.argmax(temp_marseille))
print(mois[i_max], temp_marseille[i_max])  # => jul 26
ax.annotate("Le plus chaud", xy=(i_max, temp_marseille[i_max]),
            xytext=(i_max - 4, 27), arrowprops={"arrowstyle": "->"})

ax.set_title("Températures à Marseille")
ax.set_ylabel("Température (°C)")
ax.set_ylim(0, 30)
ax.legend()
enregistrer(fig, "exo40_marseille.png")

"""
Remarque : quand les abscisses sont des chaînes, matplotlib place la 1re
catégorie en x=0, la 2e en x=1, etc. C'est pourquoi on annote avec la
position i_max (un nombre) et non avec "jul".
"""


#########################
#  Tracer depuis NumPy  #
#########################

"""
12. Avec np.linspace(), tracez sur le même graphique les fonctions
    f(x) = x², g(x) = 2x et h(x) = x³ / 4, pour x entre -3 et 3. Combien de
    points faut-il, à peu près, pour que les courbes paraissent lisses ?
"""
x = np.linspace(-3, 3, 100)

fig, ax = plt.subplots()
ax.plot(x, x ** 2, label="f(x) = x²")      # opérations vectorisées (chap. 38)
ax.plot(x, 2 * x, label="g(x) = 2x")
ax.plot(x, x ** 3 / 4, label="h(x) = x³ / 4")
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)  # axvline : ligne verticale
ax.set_title("Trois fonctions")
ax.set_xlabel("x")
ax.legend()
print(len(ax.lines))  # => 5 (3 courbes + 2 lignes d'axes)
enregistrer(fig, "exo40_fonctions.png")

"""
g est une droite : 2 points suffiraient. Pour les courbes de f et h, une
cinquantaine de points donnent déjà un rendu lisse à l'écran ; 100 est une
valeur confortable. Avec 5 points, on verrait nettement des segments.

Remarque : axhline() et axvline() créent aussi des "lignes", d'où les 5
éléments de ax.lines.
"""


##########################
#  Tracer depuis pandas  #
##########################

"""
13. (Nécessite pandas.) Créez un DataFrame avec les colonnes paris et
    marseille (les températures), et les mois pour index. En une ligne avec
    .plot(), tracez les deux courbes ; puis, avec kind="bar", les barres
    groupées. Nommez l'axe des y.
"""
try:
    import pandas as pd
except ImportError as err:
    pd = None
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("pandas n'est pas installé : exercice 13 sauté")

if pd is not None:
    df = pd.DataFrame({"paris": temp_paris, "marseille": temp_marseille},
                      index=mois)

    ax = df.plot(title="Températures (tracé par pandas)")
    ax.set_ylabel("Température (°C)")
    print(len(ax.lines))  # une courbe par colonne
    enregistrer(ax.figure, "exo40_pandas_courbes.png")

    ax = df.plot(kind="bar", title="Températures par mois")
    ax.set_ylabel("Température (°C)")
    print(len(ax.patches))  # 12 mois × 2 villes
    enregistrer(ax.figure, "exo40_pandas_barres.png")
# => 2
#    24

"""
pandas utilise automatiquement l'index pour les abscisses et les noms des
colonnes pour la légende. df.plot() renvoie un Axes : on le personnalise
ensuite comme d'habitude, et on retrouve la figure avec ax.figure.
"""


####################################
#  Bonnes pratiques de lisibilité  #
####################################

"""
14. Trouvez au moins 4 problèmes dans ces deux graphiques (qui montrent les
    mêmes données), puis remplacez-les par un seul graphique correct, en
    interface objet. Enregistrez-le dans exo40_corrige.png.

Les problèmes :
    1. Un camembert : les trois parts (1520, 1480, 1610) sont presque égales,
       et l'œil ne voit pas quelle est la plus grande.
    2. Un titre qui ne dit rien ("graphique"), et aucun titre sur le 2e.
    3. Une COURBE pour des catégories sans ordre (des produits) : relier
       "Produit A" à "Produit B" par un segment n'a pas de sens.
    4. Un axe des y qui commence à 1450 : les écarts paraissent énormes
       alors qu'ils sont d'environ 8 %.
    5. Aucun nom d'axe, aucune unité (des euros ? des unités vendues ?).

La correction : des barres, triées, avec un axe des y qui part de 0, un titre
informatif et des axes nommés.
"""
ventes_produits = {"Produit A": 1520, "Produit B": 1480, "Produit C": 1610}

# On trie les produits par ventes décroissantes (cf. chap. 24 et 27) :
produits_tries = sorted(ventes_produits, key=ventes_produits.get,
                        reverse=True)
valeurs_triees = [ventes_produits[p] for p in produits_tries]
print(produits_tries)  # => ['Produit C', 'Produit A', 'Produit B']

fig, ax = plt.subplots()
ax.bar(produits_tries, valeurs_triees, color="tab:blue")
ax.set_title("Ventes par produit : des résultats très proches")
ax.set_ylabel("Ventes (unités)")
ax.set_ylim(0, 1800)
print(ax.get_ylim()[0])  # => 0.0 (l'axe part bien de 0)
enregistrer(fig, "exo40_corrige.png")


###############
#  Nettoyage  #
###############

if GARDER_IMAGES:
    print(f"{len(images_creees)} images gardées dans {os.getcwd()}")
else:
    for nom_fichier in images_creees:
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
