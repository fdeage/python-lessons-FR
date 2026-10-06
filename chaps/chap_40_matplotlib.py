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
#  Chap. 40     #  Matplotlib                                                  #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Installer et importer matplotlib
#  - Afficher ou enregistrer ? plt.show() et savefig()
#  - Un premier graphique : plot()
#  - Titre, axes et légende
#  - Les types de graphiques
#  - Plusieurs graphiques : subplots et l'interface objet
#  - Personnaliser : couleurs, styles, annotations
#  - Tracer depuis NumPy
#  - Tracer depuis pandas
#  - Bonnes pratiques de lisibilité
#  - Nettoyage
#
##############################

# Introduction
###############

"""
"Un bon graphique vaut mieux qu'un long tableau." En Data Science, on
visualise les données à deux moments :
    1. pour EXPLORER : repérer une tendance, des valeurs aberrantes, une
       répartition inattendue… avant même de faire des calculs,
    2. pour COMMUNIQUER : présenter un résultat à quelqu'un d'autre, de
       façon claire et honnête.

matplotlib est la bibliothèque de graphiques historique de Python, et la plus
utilisée. D'autres bibliothèques (seaborn, cf. chap. 50, plotly…) existent,
mais beaucoup sont construites PAR-DESSUS matplotlib : la connaître est donc
indispensable.

Ce chapitre suppose que vous connaissez NumPy (chap. 38). La section "Tracer
depuis pandas" utilise pandas (chap. 39), mais elle est simplement sautée si
pandas n'est pas installé.

Note : ce chapitre a été vérifié avec matplotlib 3.11. Les graphiques
eux-mêmes ne peuvent pas être vérifiés par des `# =>` : ouvrez les images
produites (cf. GARDER_IMAGES ci-dessous) pour les voir.
"""


# Installer et importer matplotlib
###################################

"""
Comme NumPy et pandas, matplotlib s'installe à part (cf. chap. 22) :
    ?> pip install matplotlib
ou
    ?> conda install matplotlib

matplotlib est un gros package. On n'en importe généralement que la partie
"pyplot" (l'interface de tracé), sous l'alias conventionnel "plt" :
    import matplotlib.pyplot as plt
"""
import os
import sys

try:
    import numpy as np
    import matplotlib
except ImportError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("Ce chapitre a besoin de NumPy et de matplotlib : lancez")
    print("\"pip install numpy matplotlib\", puis relancez ce programme.")
    sys.exit(0)

"""
La ligne suivante choisit le "backend" de matplotlib, c'est-à-dire la façon
dont les graphiques sont rendus. "Agg" dessine les images en mémoire, SANS
ouvrir de fenêtre : c'est ce qu'il faut pour que ce fichier s'exécute partout
(y compris sur un serveur sans écran) et sans s'arrêter à chaque graphique.

IMPT : matplotlib.use() doit être appelé AVANT d'importer pyplot.

Dans vos propres programmes, vous n'aurez en général PAS besoin de cette
ligne : matplotlib choisit automatiquement un backend qui ouvre des fenêtres.
"""
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402 (import volontairement tardif)

print(matplotlib.__version__)  # => 3.11.2 (variable : dépend de l'installation)

"""
Ce chapitre enregistre ses graphiques sous forme d'images PNG dans le
répertoire courant (cf. chap. 28), puis les supprime à la fin pour laisser le
répertoire propre.

Pour REGARDER les images, passez GARDER_IMAGES à True, relancez le programme,
puis ouvrez les fichiers chap40_*.png qui sont apparus.
"""
GARDER_IMAGES = False
images_creees = []  # on note le nom de chaque image, pour le nettoyage final


def enregistrer(figure, nom_fichier):
    """Enregistre la figure dans un fichier PNG, puis la ferme."""
    figure.savefig(nom_fichier)
    plt.close(figure)  # libère la mémoire (cf. plus bas)
    images_creees.append(nom_fichier)
    print(f"Image enregistrée : {nom_fichier}")


# Afficher ou enregistrer ? plt.show() et savefig()
####################################################

"""
Il y a deux façons de "sortir" un graphique de matplotlib :

    1. plt.show() ouvre une fenêtre (ou affiche le graphique dans un
       notebook Jupyter, cf. chap. 2). Le programme est mis en PAUSE jusqu'à
       ce qu'on ferme la fenêtre. C'est ce qu'on fait pour explorer.

    2. plt.savefig("nom.png") enregistre le graphique dans un fichier image.
       C'est ce qu'on fait pour un rapport, une présentation, un site web…
       Le format est déduit de l'extension : .png, .jpg, .svg, .pdf…

Avec le backend "Agg" choisi plus haut, plt.show() ne fait rien (il n'y a pas
de fenêtre à ouvrir) : c'est pourquoi ce chapitre utilise savefig(). Dans vos
programmes, remplacez simplement enregistrer(fig, "….png") par plt.show().

IMPT : chaque graphique créé occupe de la mémoire tant qu'il n'est pas fermé.
Après savefig(), on ferme la figure avec plt.close(). (plt.show() le fait
automatiquement quand on ferme la fenêtre.)
"""


# Un premier graphique : plot()
################################

"""
La fonction la plus simple est plt.plot(x, y) : elle relie par des segments
les points de coordonnées (x[0], y[0]), (x[1], y[1]), etc. Les abscisses x et
les ordonnées y sont deux listes (ou tableaux NumPy) de MÊME longueur.
"""
annees = [2019, 2020, 2021, 2022, 2023]
ventes = [120, 95, 140, 160, 185]

fig = plt.figure()      # 1. on crée une "figure" (la feuille blanche)
plt.plot(annees, ventes)  # 2. on trace la courbe
enregistrer(fig, "chap40_premier.png")  # 3. on enregistre (ou plt.show())
# => Image enregistrée : chap40_premier.png

"""
Si on ne donne qu'une seule liste, matplotlib l'utilise comme ordonnées, et
prend pour abscisses les indices 0, 1, 2…

Si x et y n'ont pas la même longueur, c'est une erreur :
"""
fig = plt.figure()
try:
    plt.plot([1, 2, 3], [10, 20])
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
plt.close(fig)


# Titre, axes et légende
#########################

"""
Un graphique sans titre ni légende est un graphique incompréhensible. On
ajoute :
    - plt.title() : le titre,
    - plt.xlabel() et plt.ylabel() : le nom (et l'UNITÉ !) de chaque axe,
    - plt.legend() : la légende, qui affiche le label= de chaque courbe,
    - plt.grid() : une grille, pour lire les valeurs plus facilement,
    - plt.xlim() et plt.ylim() : les bornes des axes.

Plusieurs appels à plt.plot() avant l'enregistrement tracent plusieurs
courbes sur le MÊME graphique.
"""
ventes_concurrent = [100, 110, 115, 130, 150]

fig = plt.figure()
plt.plot(annees, ventes, label="Notre entreprise")
plt.plot(annees, ventes_concurrent, label="Concurrent")
plt.title("Ventes annuelles")
plt.xlabel("Année")
plt.ylabel("Ventes (milliers d'unités)")
plt.xticks(annees)      # une graduation par année (sinon : 2019.5, etc.)
plt.ylim(0, 200)        # l'axe des y commence à 0 (cf. bonnes pratiques)
plt.legend()
plt.grid(True)
enregistrer(fig, "chap40_legende.png")
# => Image enregistrée : chap40_legende.png


# Les types de graphiques
##########################

"""
Le bon type de graphique dépend de la QUESTION qu'on pose aux données :

    | Question                                    | Graphique              |
    |---------------------------------------------|------------------------|
    | Comment une valeur évolue-t-elle ?          | courbe : plot()        |
    | Deux grandeurs sont-elles liées ?           | nuage : scatter()      |
    | Comment comparer des catégories ?           | barres : bar(), barh() |
    | Comment des valeurs se répartissent-elles ? | histogramme : hist()   |
    | Répartition + valeurs aberrantes ?          | boîte : boxplot()      |

Les données d'exemple sont générées avec NumPy, avec une graine fixe (cf.
chap. 38) pour être reproductibles.
"""
rng = np.random.default_rng(seed=0)

"""
1. Le nuage de points (scatter) : un point par individu. Ici, 50 élèves, avec
leur temps de révision et leur note. On voit tout de suite si les deux sont
liés (une "corrélation").
"""
heures_revision = rng.uniform(0, 10, size=50)
notes = (6 + 1.2 * heures_revision + rng.normal(0, 2, size=50)).clip(0, 20)
# (.clip(0, 20) ramène les notes entre 0 et 20)

fig = plt.figure()
plt.scatter(heures_revision, notes)
plt.title("Note en fonction du temps de révision")
plt.xlabel("Temps de révision (heures)")
plt.ylabel("Note (/20)")
enregistrer(fig, "chap40_nuage.png")
# => Image enregistrée : chap40_nuage.png

"""
2. Les barres (bar) : une barre par catégorie. Idéal pour comparer des
quantités. plt.barh() trace des barres horizontales, plus lisibles quand les
noms des catégories sont longs.
"""
fruits = ["Pommes", "Bananes", "Kiwis", "Oranges"]
quantites = [45, 30, 12, 25]

fig = plt.figure()
plt.bar(fruits, quantites)
plt.title("Ventes de fruits (lundi)")
plt.ylabel("Quantité vendue (kg)")
enregistrer(fig, "chap40_barres.png")
# => Image enregistrée : chap40_barres.png

"""
3. L'histogramme (hist) : on découpe les valeurs en intervalles ("bins") et
on compte combien de valeurs tombent dans chacun. Il montre la RÉPARTITION
des données : sont-elles regroupées ? étalées ? symétriques ?

Attention à ne pas confondre avec un graphique en barres : un histogramme
porte sur UNE variable numérique, et ses barres se touchent.
"""
tailles = rng.normal(loc=170, scale=8, size=500)  # 500 tailles, en cm

fig = plt.figure()
effectifs, bornes, _ = plt.hist(tailles, bins=20)
plt.title("Répartition des tailles (500 personnes)")
plt.xlabel("Taille (cm)")
plt.ylabel("Nombre de personnes")
enregistrer(fig, "chap40_histogramme.png")
# => Image enregistrée : chap40_histogramme.png

"""
plt.hist() renvoie aussi ses calculs : les effectifs de chaque intervalle et
les bornes des intervalles (20 intervalles, donc 21 bornes). Le "_" ignore la
3e valeur renvoyée (cf. chap. 17).
"""
print(len(effectifs), len(bornes))  # => 20 21
print(int(effectifs.sum()))         # => 500 (personne n'est oublié)

"""
4. La boîte à moustaches (boxplot) résume une répartition en 5 nombres : la
"boîte" va du 1er au 3e quartile (la moitié centrale des valeurs), le trait
dans la boîte est la médiane (cf. chap. 38), et les "moustaches" s'étendent
jusqu'aux valeurs extrêmes "normales". Les points isolés au-delà sont des
valeurs ABERRANTES potentielles.

Elle est surtout utile pour COMPARER plusieurs groupes côte à côte :
"""
classe_a = rng.normal(12, 2, size=30)
classe_b = rng.normal(10, 4, size=30)
classe_c = np.append(rng.normal(13, 1.5, size=29), 2)  # un 2/20 isolé

fig = plt.figure()
plt.boxplot([classe_a, classe_b, classe_c])
plt.xticks([1, 2, 3], ["Classe A", "Classe B", "Classe C"])
plt.title("Notes par classe")
plt.ylabel("Note (/20)")
enregistrer(fig, "chap40_boxplot.png")
# => Image enregistrée : chap40_boxplot.png

"""
Lecture : la classe B a une boîte plus haute (notes plus dispersées) ; la
classe C a un point isolé tout en bas (la note de 2, aberrante pour ce
groupe).

5. Le camembert (pie) : à ÉVITER dans la plupart des cas. L'œil humain compare
très mal des angles et des surfaces : sur un camembert, 25 % et 30 % se
ressemblent beaucoup, alors que sur un graphique en barres la différence
saute aux yeux. Le voici quand même, pour que vous le reconnaissiez :
"""
fig = plt.figure()
plt.pie(quantites, labels=fruits, autopct="%1.0f%%")  # autopct : les %
plt.title("Ventes de fruits (à éviter : préférez les barres)")
enregistrer(fig, "chap40_camembert.png")
# => Image enregistrée : chap40_camembert.png

"""
Règle simple : si vous hésitez avec un camembert, faites un graphique en
barres, trié par ordre décroissant.
"""


# Plusieurs graphiques : subplots et l'interface objet
#######################################################

"""
Jusqu'ici, on a utilisé l'interface "plt.…" : matplotlib se souvient du
graphique "courant", et chaque appel à plt.title(), plt.plot()… le modifie.
C'est pratique pour un graphique rapide, mais cela devient confus dès qu'il y
a plusieurs graphiques.

La méthode recommandée est l'interface OBJET (cf. chap. 34 pour la notion
d'objet et de méthode) :
    fig, ax = plt.subplots()
renvoie deux objets :
    - fig : la Figure (toute l'image),
    - ax : un Axes, c'est-à-dire UN graphique à l'intérieur de la figure
      (attention, "Axes" ne veut pas dire "axes" : c'est le graphique entier).

On appelle alors les méthodes de ax. Leurs noms sont presque les mêmes, avec
"set_" devant pour les réglages :
    plt.title()  → ax.set_title()
    plt.xlabel() → ax.set_xlabel()
    plt.ylim()   → ax.set_ylim()
    plt.plot()   → ax.plot()  (identique)
"""
fig, ax = plt.subplots()
print(type(fig).__name__)  # => Figure
print(type(ax).__name__)   # => Axes

ax.plot(annees, ventes, label="Notre entreprise")
ax.set_title("Ventes annuelles (interface objet)")
ax.set_xlabel("Année")
ax.set_ylabel("Ventes (milliers d'unités)")
ax.legend()
print(ax.get_title())  # => Ventes annuelles (interface objet)
enregistrer(fig, "chap40_objet.png")
# => Image enregistrée : chap40_objet.png

"""
Pour plusieurs graphiques dans la même figure, on donne le nombre de lignes
et de colonnes de la "grille" : plt.subplots(2, 2) renvoie un tableau NumPy
2 × 2 d'objets Axes, qu'on indexe comme au chap. 38 : axes[ligne, colonne].

figsize=(largeur, hauteur) fixe la taille de l'image, en pouces (1 pouce =
2,54 cm).
"""
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
print(axes.shape)  # => (2, 2)

axes[0, 0].plot(annees, ventes)
axes[0, 0].set_title("Courbe")

axes[0, 1].bar(fruits, quantites)
axes[0, 1].set_title("Barres")

axes[1, 0].hist(tailles, bins=20)
axes[1, 0].set_title("Histogramme")

axes[1, 1].scatter(heures_revision, notes)
axes[1, 1].set_title("Nuage de points")

fig.suptitle("Quatre graphiques dans une figure")  # titre de la figure
fig.tight_layout()  # ajuste les espacements pour que rien ne se chevauche
print(len(fig.axes))  # => 4
enregistrer(fig, "chap40_subplots.png")
# => Image enregistrée : chap40_subplots.png

"""
Avec une seule ligne (ou une seule colonne), le tableau est 1D :
plt.subplots(1, 3) → axes[0], axes[1], axes[2].

IMPT : dès qu'un programme fait plus d'un graphique, utilisez l'interface
objet. C'est aussi celle de la plupart des exemples de la documentation.
"""


# Personnaliser : couleurs, styles, annotations
################################################

"""
plot() accepte de nombreux paramètres nommés (cf. chap. 15) :
    - color= : une couleur ("red", "tab:blue", "#1f77b4"…),
    - linestyle= : "-" (plein), "--" (tirets), ":" (pointillés)…,
    - linewidth= : l'épaisseur du trait,
    - marker= : un symbole à chaque point ("o" rond, "s" carré, "^"
      triangle…).

ax.axhline() trace une ligne horizontale (un seuil, une moyenne…), et
ax.annotate() ajoute un texte avec une flèche pointant vers un point.
"""
fig, ax = plt.subplots()
ax.plot(annees, ventes, color="tab:blue", marker="o", linewidth=2,
        label="Notre entreprise")
ax.plot(annees, ventes_concurrent, color="tab:gray", linestyle="--",
        marker="s", label="Concurrent")

moyenne = np.mean(ventes)
ax.axhline(moyenne, color="tab:red", linestyle=":",
           label=f"Notre moyenne ({moyenne:.0f})")

ax.annotate("Covid", xy=(2020, 95), xytext=(2020.3, 60),
            arrowprops={"arrowstyle": "->"})

ax.set_title("Ventes annuelles, personnalisées")
ax.set_xticks(annees)
ax.set_ylim(0, 200)
ax.legend()
enregistrer(fig, "chap40_personnalise.png")
# => Image enregistrée : chap40_personnalise.png

"""
On peut aussi changer l'apparence générale avec un "style" prédéfini :
plt.style.use("ggplot"), plt.style.use("seaborn-v0_8")… La liste est dans
plt.style.available.
"""
print("ggplot" in plt.style.available)  # => True


# Tracer depuis NumPy
######################

"""
Pour tracer une fonction mathématique, on génère beaucoup d'abscisses
régulièrement espacées avec np.linspace() (cf. chap. 38), puis on calcule les
ordonnées de façon vectorisée. Avec assez de points, les segments sont si
courts que la courbe paraît lisse.
"""
x = np.linspace(0, 2 * np.pi, 200)  # 200 points entre 0 et 2π
print(x.shape)  # => (200,)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)")
ax.axhline(0, color="black", linewidth=0.5)  # l'axe des abscisses
ax.set_title("Fonctions trigonométriques")
ax.set_xlabel("x (radians)")
ax.legend()
enregistrer(fig, "chap40_numpy.png")
# => Image enregistrée : chap40_numpy.png

"""
Essayez de remplacer 200 par 5 dans np.linspace() : la "courbe" devient une
ligne brisée, car matplotlib ne fait que relier des points.

Un tableau 2D peut aussi être affiché comme une image, chaque valeur devenant
une couleur, avec ax.imshow(). C'est une "carte de chaleur" (heatmap) :
"""
temperatures = rng.normal(15, 5, size=(7, 24))  # 7 jours × 24 heures

fig, ax = plt.subplots()
image = ax.imshow(temperatures, cmap="coolwarm", aspect="auto")
fig.colorbar(image, ax=ax, label="Température (°C)")  # l'échelle de couleurs
ax.set_title("Températures par jour et par heure")
ax.set_xlabel("Heure")
ax.set_ylabel("Jour")
enregistrer(fig, "chap40_heatmap.png")
# => Image enregistrée : chap40_heatmap.png


# Tracer depuis pandas
#######################

"""
pandas (cf. chap. 39) sait tracer directement ses Series et DataFrames avec
la méthode .plot(), qui appelle matplotlib en coulisses. Le paramètre kind=
choisit le type : "line" (par défaut), "bar", "barh", "hist", "box",
"scatter"…

Les noms des colonnes et de l'index servent automatiquement d'étiquettes et
de légende : c'est très rapide pour explorer.

pandas est facultatif pour ce chapitre : si l'import échoue, on saute
simplement cette section.
"""
try:
    import pandas as pd
except ImportError as err:
    pd = None
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")
    print("pandas n'est pas installé : section \"Tracer depuis pandas\" sautée")

if pd is not None:
    df = pd.DataFrame({"annee": annees,
                       "nous": ventes,
                       "concurrent": ventes_concurrent})
    df = df.set_index("annee")  # l'année devient l'index (les abscisses)

    # Toutes les colonnes, une courbe par colonne, en une seule ligne :
    ax = df.plot(title="Ventes (tracé par pandas)", marker="o")
    ax.set_ylabel("Ventes (milliers d'unités)")  # on récupère un Axes normal
    enregistrer(ax.figure, "chap40_pandas_courbes.png")

    # Des barres groupées :
    ax = df.plot(kind="bar", title="Ventes par année")
    enregistrer(ax.figure, "chap40_pandas_barres.png")

    # On peut aussi tracer DANS un Axes existant, avec le paramètre ax= :
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    df["nous"].plot(ax=axes[0], title="Nous")
    df["concurrent"].plot(ax=axes[1], title="Concurrent", color="tab:gray")
    fig.tight_layout()
    enregistrer(fig, "chap40_pandas_subplots.png")
# => Image enregistrée : chap40_pandas_courbes.png
#    Image enregistrée : chap40_pandas_barres.png
#    Image enregistrée : chap40_pandas_subplots.png

"""
df.plot() renvoie un objet Axes : on peut donc le personnaliser ensuite avec
toutes les méthodes vues plus haut (set_ylabel, set_ylim, legend…).
"""


# Bonnes pratiques de lisibilité
#################################

"""
Un graphique doit pouvoir être compris SANS explication orale. Quelques
règles :

    1. Un titre qui dit ce qu'on regarde (voire ce qu'il faut en retenir :
       "Les ventes ont doublé depuis 2020").
    2. Des axes nommés, AVEC leurs unités (€, kg, °C, heures…).
    3. Une légende dès qu'il y a plusieurs séries, et seulement dans ce cas.
    4. IMPT : pour un graphique en barres, l'axe des y commence à 0. Sinon,
       la hauteur des barres ne représente plus les quantités, et une petite
       différence paraît énorme (c'est une technique de manipulation
       classique !).
    5. Le bon type de graphique (cf. le tableau plus haut) : pas de camembert,
       pas de courbe pour des catégories sans ordre.
    6. Peu de couleurs, et qui ont un sens : une couleur par série, la même
       série de la même couleur d'un graphique à l'autre. Pensez aux
       daltoniens : les palettes par défaut de matplotlib ("tab:…") sont
       conçues pour rester distinguables.
    7. Pas de décoration inutile : pas d'effet 3D, pas d'ombre, pas de fond
       chargé. Chaque élément doit transmettre une information.
    8. Des graduations lisibles : pas de "2019.5" pour des années (cf.
       set_xticks), et des textes assez gros (paramètre fontsize=).

Exemple de la règle 4 : les deux graphiques ci-dessous montrent EXACTEMENT
les mêmes données.
"""
equipes = ["Équipe A", "Équipe B"]
scores = [96, 98]

fig, (ax_trompeur, ax_honnete) = plt.subplots(1, 2, figsize=(9, 4))
ax_trompeur.bar(equipes, scores, color=["tab:gray", "tab:blue"])
ax_trompeur.set_ylim(95, 98.5)  # l'axe commence à 95 : B semble 3 fois mieux
ax_trompeur.set_title("Trompeur : l'axe commence à 95")

ax_honnete.bar(equipes, scores, color=["tab:gray", "tab:blue"])
ax_honnete.set_ylim(0, 100)     # l'axe commence à 0 : la différence est minime
ax_honnete.set_title("Honnête : l'axe commence à 0")

for ax in (ax_trompeur, ax_honnete):
    ax.set_ylabel("Score (/100)")
fig.tight_layout()
enregistrer(fig, "chap40_trompeur.png")
# => Image enregistrée : chap40_trompeur.png

"""
Remarquez le déballage (cf. chap. 17) : plt.subplots(1, 2) renvoie un tableau
de 2 Axes, qu'on peut directement répartir dans deux variables entre
parenthèses.

Pour aller plus loin :
    - la galerie de matplotlib, pleine d'exemples à copier et adapter :
      https://matplotlib.org/stable/gallery/
    - le "Data Visualisation Catalogue", pour choisir le bon graphique :
      https://datavizcatalogue.com
    - seaborn, une bibliothèque construite sur matplotlib, spécialisée dans
      les graphiques statistiques (cf. chap. 50) : https://seaborn.pydata.org
"""


# Nettoyage
############

"""
Comme au chap. 28, on supprime les fichiers créés par ce chapitre… sauf si
vous avez demandé à les garder (GARDER_IMAGES = True, cf. plus haut).
"""
print(len(images_creees) >= 13)  # => True (13 images, 16 avec pandas)

if GARDER_IMAGES:
    print(f"{len(images_creees)} images gardées dans {os.getcwd()}")
else:
    for nom_fichier in images_creees:
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
    print("Images supprimées (passez GARDER_IMAGES à True pour les garder)")
# => Images supprimées (passez GARDER_IMAGES à True pour les garder)
