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
#  Chap. 50     #  Seaborn                                                     #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Installer et importer seaborn
#  - Des données "tidy" (format long)
#  - Thèmes et palettes
#  - Les distributions
#  - Les relations entre variables
#  - Les variables catégorielles
#  - Encoder plus d'informations : hue, style et size
#  - Plusieurs graphiques : les figures à facettes
#  - Les matrices : heatmap
#  - Tout voir d'un coup : pairplot et jointplot
#  - Personnaliser avec matplotlib
#  - Bonnes pratiques et graphiques trompeurs
#  - Nettoyage
#
##############################

# Introduction
###############

"""
On a vu au chap. 40 que matplotlib permet de tout dessiner… mais qu'il faut
souvent beaucoup de lignes pour obtenir un graphique statistique soigné :
calculer soi-même les moyennes par groupe, choisir les couleurs, ajouter la
légende, etc.

seaborn est une bibliothèque construite PAR-DESSUS matplotlib (cf. chap. 40)
et pandas (cf. chap. 39). Son idée : on lui donne un DataFrame et on lui dit
QUELLES COLONNES représenter, et comment. Elle se charge :
    - des calculs statistiques (moyennes, intervalles de confiance, densités,
      régressions…),
    - des couleurs et de la légende,
    - de la mise en page quand on veut un graphique par groupe.

Comparez, pour tracer la note moyenne par filière avec une couleur par
filière :

    # matplotlib "à la main"
    moyennes = df.groupby("filiere")["note"].mean()
    plt.bar(moyennes.index, moyennes.values, color=["C0", "C1", "C2"])
    plt.xlabel("filiere")
    plt.ylabel("note")

    # seaborn
    sns.barplot(data=df, x="filiere", y="note", hue="filiere")

Et seaborn ajoute en prime des barres d'erreur, que l'on expliquera plus bas.

IMPT : seaborn ne remplace PAS matplotlib, il le complète. Chaque graphique
seaborn EST un graphique matplotlib : tout ce que vous avez appris au
chap. 40 (titres, axes, savefig…) reste valable.

Note : ce chapitre a été vérifié avec seaborn 0.13, matplotlib 3.11 et
pandas 3.0. Comme au chap. 40, les graphiques eux-mêmes ne peuvent pas être
vérifiés par des `# =>` : on vérifie à la place quelques propriétés des
objets créés (titre, nombre de barres…). Pour voir les images, passez
GARDER_IMAGES à True (cf. plus bas).
"""


# Installer et importer seaborn
################################

"""
seaborn s'installe comme les autres paquets (cf. chap. 22 et 47). Dans un
projet géré avec uv :
    ?> uv add seaborn
ou, avec pip :
    ?> pip install seaborn

seaborn installe automatiquement NumPy, pandas et matplotlib s'ils manquent.

On l'importe sous l'alias conventionnel "sns" (une blague : ce sont les
initiales de Samuel Norman Seaborn, un personnage de la série "The West
Wing").
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
    print("Ce chapitre a besoin de seaborn (qui installe aussi NumPy, pandas")
    print("et matplotlib). Lancez \"uv add seaborn\" (ou \"pip install")
    print("seaborn\"), puis relancez ce programme.")
    sys.exit(0)

# Comme au chap. 40 : pas de fenêtre, on enregistre des images PNG.
# (Dans vos programmes, cette ligne est inutile, et plt.show() affiche.)
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402 (import volontairement tardif)

print(sns.__version__)  # => 0.13.2 (variable : dépend de l'installation)

"""
seaborn 0.13 utilise quelques fonctions que matplotlib 3.11 a déclarées
"obsolètes" ("deprecated") : matplotlib affiche alors des avertissements (des
"warnings"), par exemple à chaque boxplot. Ce ne sont pas des erreurs, et ce
n'est pas de notre faute : on les masque avec le module warnings de la
bibliothèque standard, pour les seuls avertissements de dépréciation émis
depuis seaborn. (Une prochaine version de seaborn corrigera cela.)
"""
warnings.filterwarnings("ignore", category=DeprecationWarning,
                        module="seaborn")
warnings.filterwarnings("ignore", category=PendingDeprecationWarning,
                        module="seaborn")

GARDER_IMAGES = False
images_creees = []  # on note le nom de chaque image, pour le nettoyage final


def enregistrer(figure, nom_fichier):
    """Enregistre la figure dans un fichier PNG, puis la ferme."""
    # bbox_inches="tight" : ne rien couper (légende, noms des axes…)
    figure.savefig(nom_fichier, bbox_inches="tight")
    plt.close(figure)  # libère la mémoire (cf. chap. 40)
    images_creees.append(nom_fichier)


"""
Les données de ce chapitre sont INVENTÉES, mais réalistes : on les génère avec
le générateur aléatoire de NumPy (cf. chap. 38), avec une graine fixe pour
obtenir toujours les mêmes valeurs.

(seaborn propose aussi des jeux de données d'exemple avec sns.load_dataset(),
mais ils sont téléchargés depuis Internet : on ne les utilise pas ici, pour
que ce fichier fonctionne même hors ligne.)

Le jeu de données : 300 étudiants, avec leur filière, leur année d'études,
leurs heures de révision par semaine, leur temps d'écran par jour, et leur
note à l'examen.
"""
rng = np.random.default_rng(seed=42)
n = 300
filieres = rng.choice(["Info", "Maths", "Bio"], size=n, p=[0.4, 0.35, 0.25])
annees = rng.choice(["L1", "L2", "L3"], size=n)
heures = rng.uniform(0, 15, size=n).round(1)
ecran = rng.uniform(1, 8, size=n).round(1)
bonus = np.select([filieres == "Info", filieres == "Maths"], [1.0, 0.0], -1.0)
notes = 6 + 0.7 * heures - 0.4 * ecran + bonus + rng.normal(0, 2, size=n)
notes = notes.clip(0, 20).round(1)  # une note est entre 0 et 20

etudiants = pd.DataFrame({
    "filiere": filieres,
    "annee": annees,
    "heures": heures,
    "ecran": ecran,
    "note": notes,
})
print(etudiants.shape)  # => (300, 5)
print(etudiants.head(3))
# =>   filiere annee  heures  ecran  note
# => 0     Bio    L2     0.6    2.8   2.3
# => 1   Maths    L3    13.3    3.3  14.1
# => 2     Bio    L3    10.6    2.7  10.8


# Des données "tidy" (format long)
###################################

"""
seaborn attend des données "tidy" ("rangées") :
    - une LIGNE par observation (ici : un étudiant),
    - une COLONNE par variable (filière, note…).

C'est le cas de notre DataFrame etudiants. Mais on rencontre souvent des
tableaux au format "large" ("wide"), plus agréables à lire pour un humain.
Par exemple, des températures moyennes mensuelles, une colonne par ville :
"""
mois = list(range(1, 13))
temperatures_larges = pd.DataFrame({
    "mois": mois,
    "Paris": [5, 6, 10, 13, 16, 20, 22, 22, 18, 14, 9, 6],
    "Lyon": [3, 5, 9, 12, 16, 20, 23, 22, 18, 13, 8, 4],
    "Marseille": [8, 9, 12, 15, 19, 23, 26, 26, 22, 18, 12, 9],
})
print(temperatures_larges.shape)  # => (12, 4)

"""
Ici, la variable "ville" est cachée dans les NOMS des colonnes. Pour seaborn,
il faut la transformer en une vraie colonne : c'est le passage au format
"long", avec la méthode melt() de pandas (détaillée au chap. 48) :
"""
temperatures = temperatures_larges.melt(
    id_vars="mois",          # la colonne à garder telle quelle
    var_name="ville",        # nom de la nouvelle colonne (anciens en-têtes)
    value_name="temperature",  # nom de la colonne des valeurs
)
print(temperatures.shape)  # => (36, 3)
print(temperatures.head(3))
# =>    mois  ville  temperature
# => 0     1  Paris            5
# => 1     2  Paris            6
# => 2     3  Paris           10

"""
On a maintenant 36 lignes (12 mois × 3 villes) et 3 colonnes : "mois",
"ville", "temperature". C'est ce format que seaborn sait exploiter : on
pourra écrire hue="ville" pour avoir une couleur par ville.

IMPT : si un graphique seaborn est difficile à écrire, c'est très souvent que
les données ne sont pas au format long. Commencez par melt() !
"""


# Thèmes et palettes
#####################

"""
1. Les thèmes

sns.set_theme() change l'apparence de TOUS les graphiques suivants (y compris
ceux faits directement avec matplotlib) : fond, grille, polices…

    - style : "darkgrid" (par défaut), "whitegrid", "dark", "white", "ticks"
    - context : la taille des éléments selon l'usage : "paper", "notebook"
      (par défaut), "talk" (présentation), "poster"
"""
sns.set_theme(style="whitegrid", context="notebook")

"""
2. Les palettes de couleurs

Une palette est une liste de couleurs. Il en existe trois grandes familles,
et le choix dépend de la NATURE de la variable représentée :

    - QUALITATIVE : des couleurs bien distinctes, sans ordre, pour des
      catégories (filières, villes…). Ex. : "deep", "Set2", "colorblind".
    - SÉQUENTIELLE : du clair au foncé, pour des valeurs ordonnées qui vont
      de "peu" à "beaucoup" (une note, une population…). Ex. : "Blues",
      "viridis", "rocket".
    - DIVERGENTE : deux couleurs opposées autour d'un centre neutre, pour des
      valeurs qui s'écartent d'un point de référence (une corrélation entre
      -1 et 1, un écart à la moyenne…). Ex. : "coolwarm", "vlag", "RdBu".

sns.color_palette() renvoie une palette, sous forme de liste de couleurs
(chaque couleur est un tuple (rouge, vert, bleu) de floats entre 0 et 1) :
"""
palette = sns.color_palette("colorblind", 3)
print(len(palette))  # => 3
print(tuple(round(c, 2) for c in palette[0]))  # => (0.0, 0.45, 0.7)

"""
IMPT : environ 8 % des hommes et 0,5 % des femmes ont une forme de
daltonisme, le plus souvent une difficulté à distinguer le rouge et le vert.
Préférez la palette "colorblind" (ou "viridis" pour du séquentiel), et
n'utilisez jamais la couleur comme SEULE information : on peut la doubler
par une forme ou un style de ligne (cf. "style" plus bas).
"""
sns.set_palette("colorblind")  # palette par défaut pour la suite


# Les distributions
####################

"""
Première question à se poser face à une variable numérique : comment ses
valeurs sont-elles RÉPARTIES ? Sont-elles regroupées autour d'une valeur ?
Étalées ? Y a-t-il des valeurs extrêmes ?

1. histplot() : l'histogramme (cf. chap. 40), en une ligne.

On passe le DataFrame avec data=, puis le NOM de la colonne avec x=. C'est la
signature commune à presque toutes les fonctions de seaborn.

Les fonctions comme histplot() renvoient l'objet Axes de matplotlib dans
lequel elles ont dessiné (cf. chap. 40) : on peut donc le personnaliser.
"""
fig, ax = plt.subplots()
ax = sns.histplot(data=etudiants, x="note", bins=20, ax=ax)
ax.set_title("Répartition des notes")
print(len(ax.patches))  # => 20 : une barre (un "patch") par intervalle
print(ax.get_xlabel())  # => note : seaborn nomme l'axe d'après la colonne
enregistrer(fig, "chap50_histplot.png")

"""
2. kdeplot() : l'estimation de densité ("Kernel Density Estimate")

Un histogramme dépend du nombre d'intervalles choisi. La KDE trace à la place
une courbe lisse, comme si on "lissait" l'histogramme : l'aire sous la courbe
vaut 1. On l'utilise souvent pour COMPARER des distributions, avec hue= :
une courbe par groupe.
"""
fig, ax = plt.subplots()
sns.kdeplot(data=etudiants, x="note", hue="filiere", ax=ax)
ax.set_title("Distribution des notes par filière")
print(len(ax.lines))  # => 3 : une courbe par filière
enregistrer(fig, "chap50_kdeplot.png")

"""
Attention : la courbe KDE "déborde" parfois au-delà des valeurs possibles (une
note négative, par exemple) : c'est un effet du lissage, pas une donnée.

3. ecdfplot() : la fonction de répartition empirique

Pour chaque valeur x, la courbe donne la PROPORTION d'observations
inférieures ou égales à x. Elle se lit facilement : "à quelle note se trouve
la moitié des étudiants ?" → on cherche où la courbe atteint 0.5 (la
médiane). Pas d'intervalle à choisir, pas de lissage : rien n'est caché.
"""
fig, ax = plt.subplots()
sns.ecdfplot(data=etudiants, x="note", hue="filiere", ax=ax)
ax.axhline(0.5, color="gray", linestyle="--")  # repère de la médiane
enregistrer(fig, "chap50_ecdfplot.png")

mediane = etudiants["note"].median()
print(mediane)  # => 9.7 : la courbe "toutes filières" passerait 0.5 ici

"""
4. displot() : la version "figure"

seaborn distingue deux sortes de fonctions :
    - les fonctions "axes-level" (histplot, kdeplot, scatterplot…) dessinent
      dans UN Axes et renvoient cet Axes,
    - les fonctions "figure-level" (displot, relplot, catplot…) créent
      elles-mêmes une figure ENTIÈRE, éventuellement avec plusieurs
      graphiques, et renvoient un objet FacetGrid (cf. plus bas).

displot() est la version figure-level de histplot/kdeplot/ecdfplot : on
choisit le type avec kind=. Son intérêt apparaîtra avec les facettes.
"""
grille = sns.displot(data=etudiants, x="heures", kind="hist", bins=15)
print(type(grille).__name__)  # => FacetGrid
enregistrer(grille.figure, "chap50_displot.png")


# Les relations entre variables
################################

"""
Deuxième grande question : deux variables numériques sont-elles LIÉES ?
Quand l'une augmente, l'autre augmente-t-elle aussi ?

1. scatterplot() : le nuage de points, un point par étudiant.
"""
fig, ax = plt.subplots()
sns.scatterplot(data=etudiants, x="heures", y="note", ax=ax)
ax.set_title("Plus on révise, meilleure est la note ?")
# Un nuage de points est un seul objet "collection" de 300 points :
print(len(ax.collections))  # => 1
print(len(ax.collections[0].get_offsets()))  # => 300
enregistrer(fig, "chap50_scatterplot.png")

"""
2. regplot() : le nuage + une droite de régression

regplot() ajoute la droite qui "passe au mieux" au milieu des points (la
régression linéaire, détaillée au chap. 51), entourée d'une bande colorée :
l'INTERVALLE DE CONFIANCE à 95 %.

Intuition : si on refaisait l'étude avec 300 AUTRES étudiants, on
n'obtiendrait pas exactement la même droite. La bande montre où la "vraie"
droite a de bonnes chances de se trouver. Elle est étroite là où il y a
beaucoup de points, plus large aux extrémités.
"""
fig, ax = plt.subplots()
sns.regplot(data=etudiants, x="heures", y="note", ax=ax,
            scatter_kws={"alpha": 0.4})  # points semi-transparents
print(len(ax.lines))  # => 1 : la droite de régression
enregistrer(fig, "chap50_regplot.png")

"""
La pente de la droite peut se calculer avec NumPy (np.polyfit, polynôme de
degré 1) : c'est ce que fait seaborn en interne.
"""
pente, ordonnee = np.polyfit(etudiants["heures"], etudiants["note"], 1)
print(round(pente, 2))  # => 0.79 : +0,79 point par heure de révision

"""
(On a généré les données avec un coefficient de 0.7 : la régression s'en
approche, malgré le "bruit" aléatoire ajouté aux notes.)

3. lineplot() : une courbe, pour des données ORDONNÉES (le temps, souvent).

Avec nos températures au format long, une ligne de code suffit pour avoir une
courbe par ville, avec légende :
"""
fig, ax = plt.subplots()
sns.lineplot(data=temperatures, x="mois", y="temperature", hue="ville",
             marker="o", ax=ax)
ax.set_title("Températures moyennes mensuelles")
print(len(ax.get_legend().get_texts()))  # => 3 : une entrée par ville
enregistrer(fig, "chap50_lineplot.png")

"""
Si plusieurs lignes ont la même valeur de x, lineplot() trace leur MOYENNE,
entourée d'une bande d'intervalle de confiance (comme regplot). Par exemple,
la note moyenne selon le nombre d'heures arrondi :
"""
etudiants["heures_arrondies"] = etudiants["heures"].round()
fig, ax = plt.subplots()
sns.lineplot(data=etudiants, x="heures_arrondies", y="note", ax=ax)
print(len(ax.collections))  # => 1 : la bande de l'intervalle de confiance
enregistrer(fig, "chap50_lineplot_ic.png")

"""
4. relplot() : la version figure-level de scatterplot (kind="scatter", par
défaut) et de lineplot (kind="line"). On la retrouve avec les facettes.
"""


# Les variables catégorielles
##############################

"""
Troisième situation : comparer une variable numérique (la note) entre des
CATÉGORIES (les filières). seaborn propose trois familles de graphiques.

1. Les ESTIMATIONS : barplot() et countplot()

barplot() ne trace PAS les valeurs elles-mêmes, mais un RÉSUMÉ par catégorie :
par défaut, la moyenne (le paramètre "estimator", qu'on peut changer).
"""
fig, ax = plt.subplots()
sns.barplot(data=etudiants, x="filiere", y="note",
            order=["Bio", "Info", "Maths"], ax=ax)
print(len(ax.patches))  # => 3 : une barre par filière
hauteurs = [round(float(barre.get_height()), 2) for barre in ax.patches]
print(hauteurs)  # => [8.07, 10.41, 9.63]
enregistrer(fig, "chap50_barplot.png")

# Les hauteurs sont bien les moyennes par filière (cf. groupby, chap. 39) :
print(etudiants.groupby("filiere")["note"].mean().round(2).to_dict())
# => {'Bio': 8.07, 'Info': 10.41, 'Maths': 9.63}

"""
Et les petits traits noirs au sommet des barres ? Ce sont des BARRES
D'ERREUR. Par défaut, elles montrent l'intervalle de confiance à 95 % de la
moyenne : la moyenne "réelle" (celle qu'on obtiendrait avec une infinité
d'étudiants) a de bonnes chances d'être dans cet intervalle.

IMPT : si les barres d'erreur de deux groupes se chevauchent largement, la
différence entre les deux moyennes n'est peut-être qu'un effet du hasard.

On peut changer ce qu'elles représentent avec errorbar= :
    - ("ci", 95) : intervalle de confiance à 95 % (par défaut),
    - "sd" : l'écart-type, c'est-à-dire la DISPERSION des données,
    - None : pas de barre d'erreur.
L'intervalle de confiance est calculé par "bootstrap" (des tirages au hasard) :
ses bornes exactes peuvent varier très légèrement d'une exécution à l'autre.

On peut aussi changer l'estimateur, par exemple pour la médiane :
"""
fig, ax = plt.subplots()
sns.barplot(data=etudiants, x="filiere", y="note", estimator="median",
            errorbar="sd", order=["Bio", "Info", "Maths"], ax=ax)
enregistrer(fig, "chap50_barplot_mediane.png")

"""
countplot() compte simplement le NOMBRE de lignes par catégorie (pas besoin
de y) :
"""
fig, ax = plt.subplots()
sns.countplot(data=etudiants, x="filiere", order=["Info", "Maths", "Bio"],
              ax=ax)
print([int(barre.get_height()) for barre in ax.patches])  # => [123, 102, 75]
enregistrer(fig, "chap50_countplot.png")

"""
2. Les DISTRIBUTIONS par catégorie : boxplot() et violinplot()

Une moyenne ne dit rien de la dispersion. Le boxplot ("boîte à moustaches",
cf. chap. 40) montre la médiane, les quartiles et les valeurs extrêmes. Le
violinplot dessine en plus la forme de la distribution (une KDE symétrique,
cf. plus haut).
"""
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
sns.boxplot(data=etudiants, x="filiere", y="note", ax=ax1)
sns.violinplot(data=etudiants, x="filiere", y="note", ax=ax2)
ax1.set_title("boxplot")
ax2.set_title("violinplot")
enregistrer(fig, "chap50_box_violon.png")

"""
3. Les POINTS eux-mêmes : stripplot() et swarmplot()

Pour de petits jeux de données, rien ne vaut l'affichage de TOUTES les
valeurs. stripplot() les aligne en ajoutant un léger décalage horizontal
aléatoire ("jitter") pour qu'ils ne se superposent pas ; swarmplot() les
range en "essaim", sans aucun chevauchement (mais il devient illisible, et
lent, au-delà de quelques centaines de points).

On peut superposer les points à un boxplot : on voit à la fois le résumé et
les données.
"""
echantillon = etudiants.sample(60, random_state=0)  # 60 étudiants au hasard
fig, ax = plt.subplots()
sns.boxplot(data=echantillon, x="filiere", y="note", color="white", ax=ax)
sns.swarmplot(data=echantillon, x="filiere", y="note", ax=ax, size=4)
enregistrer(fig, "chap50_swarmplot.png")

"""
4. catplot() est la version figure-level de tout ce qui précède : kind="bar",
"count", "box", "violin", "strip", "swarm"…
"""


# Encoder plus d'informations : hue, style et size
###################################################

"""
Un graphique a deux axes… mais on peut représenter plus de deux variables, en
les "encodant" dans l'apparence des points ou des lignes :
    - hue : la COULEUR (catégories, ou valeurs numériques en dégradé),
    - style : la FORME des points / le type de trait (catégories seulement),
    - size : la TAILLE des points (plutôt des valeurs numériques).

Ici, 4 variables sur un seul graphique : heures (x), note (y), filière
(couleur ET forme, pour les daltoniens) et temps d'écran (taille).
"""
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=etudiants, x="heures", y="note", hue="filiere",
                style="filiere", size="ecran", sizes=(10, 120), alpha=0.7,
                ax=ax)
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))  # légende à droite
fig.tight_layout()
enregistrer(fig, "chap50_hue_style_size.png")

"""
IMPT : ne pas en abuser. Au-delà de 3 ou 4 variables, un graphique devient
illisible : mieux vaut faire plusieurs graphiques (cf. section suivante).
"""


# Plusieurs graphiques : les figures à facettes
################################################

"""
Les fonctions figure-level (relplot, displot, catplot) savent découper les
données en sous-groupes et faire UN GRAPHIQUE PAR GROUPE, côte à côte, avec
les mêmes axes : ce sont les "facettes" ("small multiples").
    - col="annee" : une colonne de graphiques par année,
    - row="filiere" : une ligne de graphiques par filière.

C'est souvent plus lisible que tout superposer avec hue.
"""
grille = sns.relplot(data=etudiants, x="heures", y="note", col="annee",
                     col_order=["L1", "L2", "L3"], hue="filiere",
                     height=3.5, aspect=0.9)
print(grille.axes.shape)  # => (1, 3) : 1 ligne, 3 colonnes de graphiques
print(grille.axes[0, 0].get_title())  # => annee = L1
grille.set_axis_labels("Heures de révision", "Note")
grille.set_titles("Année {col_name}")  # personnaliser le titre de chaque case
print(grille.axes[0, 0].get_title())  # => Année L1
enregistrer(grille.figure, "chap50_facettes.png")

"""
Lignes ET colonnes : une grille de 3 × 3 histogrammes.
"""
grille = sns.displot(data=etudiants, x="note", row="filiere", col="annee",
                     col_order=["L1", "L2", "L3"], height=2, bins=10)
print(grille.axes.shape)  # => (3, 3)
enregistrer(grille.figure, "chap50_facettes_grille.png")

"""
L'objet renvoyé est un FacetGrid. Ses attributs utiles :
    - grille.figure : la figure matplotlib (pour savefig),
    - grille.axes : un tableau NumPy des Axes (cf. chap. 38),
    - grille.set_titles(), grille.set_axis_labels() : personnaliser.

Erreur fréquente : passer ax= à une fonction figure-level. Elle crée sa
propre figure, elle ne peut pas dessiner dans un Axes existant. seaborn ne
plante pas : il IGNORE ax= et affiche un avertissement (un "warning"). On
l'intercepte ici avec warnings.catch_warnings(), pour l'afficher proprement :
"""
fig, ax = plt.subplots()
with warnings.catch_warnings(record=True) as avertissements:
    warnings.simplefilter("always")  # enregistrer tous les avertissements
    sns.relplot(data=etudiants, x="heures", y="note", ax=ax)
message = str(avertissements[0].message)
print(message[:59])
# => relplot is a figure-level function and does not accept the
print(len(plt.get_fignums()))  # => 2 : notre figure (vide) + celle de relplot
plt.close("all")
"""
Retenez la règle : ax= seulement avec les fonctions axes-level (histplot,
scatterplot, boxplot…).
"""


# Les matrices : heatmap
#########################

"""
Une "heatmap" (carte de chaleur) représente un tableau 2D de nombres par des
couleurs. Son usage le plus courant : la MATRICE DE CORRÉLATION.

La corrélation entre deux variables est un nombre entre -1 et 1 :
    -  1 : quand l'une augmente, l'autre augmente (lien parfait),
    -  0 : pas de lien LINÉAIRE,
    - -1 : quand l'une augmente, l'autre diminue (lien parfait).

DataFrame.corr() calcule toutes les corrélations deux à deux (cf. chap. 39) :
"""
correlations = etudiants[["heures", "ecran", "note"]].corr().round(2)
print(correlations)
# =>         heures  ecran  note
# => heures    1.00  -0.12  0.83
# => ecran    -0.12   1.00 -0.28
# => note      0.83  -0.28  1.00

"""
Lecture : la note est fortement liée aux heures de révision (0.83), un peu
liée NÉGATIVEMENT au temps d'écran (-0.28). C'est ce qu'on a mis dans les
données générées !

Et les heures de révision et le temps d'écran (-0.12) ? On les a tirés au
hasard INDÉPENDAMMENT l'un de l'autre : leur "vraie" corrélation est 0. Les
-0.12 viennent uniquement du hasard de l'échantillon. Avec 300 observations,
une corrélation aussi faible ne veut rien dire.

Pour une corrélation, on choisit une palette DIVERGENTE centrée sur 0
(center=0), avec vmin=-1 et vmax=1 pour que les couleurs aient toujours le
même sens. annot=True écrit la valeur dans chaque case.
"""
fig, ax = plt.subplots()
sns.heatmap(correlations, annot=True, cmap="vlag", center=0, vmin=-1,
            vmax=1, square=True, ax=ax)
ax.set_title("Matrice de corrélation")
print(len(ax.texts))  # => 9 : une annotation par case (3 × 3)
enregistrer(fig, "chap50_heatmap.png")

"""
IMPT : corrélation n'est pas causalité ! Deux variables peuvent être
corrélées parce qu'une troisième les influence toutes les deux. (Le nombre
de glaces vendues et le nombre de coups de soleil sont corrélés… à cause du
beau temps.)

Une heatmap sert aussi pour un tableau croisé : par exemple la note moyenne
par filière et par année, obtenue avec pivot_table() (cf. chap. 48).
"""
tableau = etudiants.pivot_table(index="filiere", columns="annee",
                                values="note", aggfunc="mean").round(1)
print(tableau.shape)  # => (3, 3)
fig, ax = plt.subplots()
sns.heatmap(tableau, annot=True, fmt=".1f", cmap="rocket_r", ax=ax)
enregistrer(fig, "chap50_heatmap_pivot.png")


# Tout voir d'un coup : pairplot et jointplot
##############################################

"""
1. pairplot() : en exploration, on veut souvent voir TOUTES les relations
entre les variables numériques d'un coup. pairplot() fait une grille :
    - hors de la diagonale : le nuage de points de chaque paire,
    - sur la diagonale : la distribution de chaque variable.
"""
grille = sns.pairplot(etudiants[["heures", "ecran", "note", "filiere"]],
                      hue="filiere", height=2)
print(grille.axes.shape)  # => (3, 3) : 3 variables numériques
enregistrer(grille.figure, "chap50_pairplot.png")

"""
Attention : avec 10 variables, cela fait 100 graphiques… et un calcul long.
Choisissez les colonnes intéressantes.

2. jointplot() : un nuage de points avec, dans les marges, la distribution
de chaque variable. kind= peut valoir "scatter", "reg", "hex" (des hexagones
colorés selon le nombre de points, utile quand il y en a beaucoup), "kde"…
"""
grille = sns.jointplot(data=etudiants, x="heures", y="note", kind="reg",
                       height=5)
print(type(grille).__name__)  # => JointGrid
enregistrer(grille.figure, "chap50_jointplot.png")


# Personnaliser avec matplotlib
################################

"""
Puisque seaborn dessine dans des objets matplotlib, on personnalise avec les
méthodes vues au chap. 40 :
    - axes-level : la fonction renvoie un Axes → ax.set_title(), etc.
    - figure-level : on passe par grille.ax (un seul graphique), grille.axes,
      ou grille.figure.
"""
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=etudiants, x="annee", y="note", hue="filiere",
            order=["L1", "L2", "L3"], ax=ax)
ax.set_title("Notes par année et par filière", fontsize=14)
ax.set_xlabel("Année d'études")
ax.set_ylabel("Note à l'examen (/20)")
ax.set_ylim(0, 20)  # une note est sur 20 : on montre toute l'échelle
ax.axhline(10, color="red", linestyle="--", linewidth=1)  # la moyenne
ax.legend(title="Filière", loc="upper left", bbox_to_anchor=(1, 1))
sns.despine(ax=ax)  # retire les bordures haute et droite, plus épuré
print(ax.get_ylim())  # => (np.float64(0.0), np.float64(20.0))
enregistrer(fig, "chap50_personnalise.png")

"""
(L'affichage np.float64(…) vient de NumPy 2 ; avec NumPy 1, on voit
simplement (0.0, 20.0).)

Sauvegarder :
    - axes-level : fig.savefig("graphique.png", dpi=150) (cf. chap. 40),
    - figure-level : grille.savefig("graphique.png") ou
      grille.figure.savefig(…).
dpi= ("points par pouce") règle la résolution ; bbox_inches="tight" évite
qu'une légende placée hors du graphique soit coupée.

Pour revenir au style par défaut de matplotlib : sns.reset_defaults().
"""


# Bonnes pratiques et graphiques trompeurs
###########################################

"""
seaborn rend les graphiques faciles… y compris les graphiques trompeurs.
Quelques règles (complétant celles du chap. 40) :

1. Un graphique en BARRES doit partir de 0 : la longueur de la barre EST
   l'information. Couper l'axe exagère les différences. (Pour un boxplot ou
   une courbe, ce n'est pas obligatoire.)

2. Une moyenne seule cache la dispersion. Deux groupes peuvent avoir la même
   moyenne et des distributions très différentes : montrez la distribution
   (boxplot, violin, points) ou au moins les barres d'erreur.

3. Indiquez ce que représentent les barres d'erreur (intervalle de
   confiance ? écart-type ?) : ce n'est pas du tout la même chose.

4. Choisissez la palette selon la nature de la variable (qualitative,
   séquentielle, divergente) et pensez aux daltoniens.

5. Un graphique doit répondre à UNE question : donnez-lui un titre qui la
   pose (ou qui donne la réponse !), nommez les axes avec leurs unités.

Exemple : deux groupes avec la MÊME moyenne (10) mais des distributions très
différentes. Le barplot les montre identiques, le stripplot révèle tout.
"""
groupe_a = rng.normal(10, 0.5, size=40)          # notes très regroupées
groupe_b = np.concatenate([rng.normal(5, 1, 20),  # deux sous-groupes :
                           rng.normal(15, 1, 20)])  # les faibles et les forts
groupe_b = groupe_b - groupe_b.mean() + groupe_a.mean()  # même moyenne
deux_groupes = pd.DataFrame({
    "groupe": ["A"] * 40 + ["B"] * 40,
    "note": np.concatenate([groupe_a, groupe_b]),
})
moyennes = deux_groupes.groupby("groupe")["note"].mean().round(2)
print(moyennes["A"] == moyennes["B"])  # => True

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4), sharey=True)
sns.barplot(data=deux_groupes, x="groupe", y="note", errorbar=None, ax=ax1)
ax1.set_title("Moyennes : identiques…")
sns.stripplot(data=deux_groupes, x="groupe", y="note", ax=ax2)
ax2.set_title("…mais des réalités très différentes")
enregistrer(fig, "chap50_trompeur.png")

"""
Pour aller plus loin :
    - le tutoriel officiel, très bien fait :
      https://seaborn.pydata.org/tutorial.html
    - la galerie d'exemples : https://seaborn.pydata.org/examples/
    - "Fundamentals of Data Visualization" (Claus O. Wilke), en ligne et
      gratuit : https://clauswilke.com/dataviz/
"""


# Nettoyage
############

"""
Comme au chap. 40, on supprime les images créées par ce chapitre… sauf si vous
avez demandé à les garder (GARDER_IMAGES = True, cf. plus haut).
"""
print(len(images_creees))  # => 22
plt.close("all")

if GARDER_IMAGES:
    print(f"{len(images_creees)} images gardées dans {os.getcwd()}")
else:
    for nom_fichier in images_creees:
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
    print("Images supprimées (passez GARDER_IMAGES à True pour les garder)")
# => Images supprimées (passez GARDER_IMAGES à True pour les garder)
