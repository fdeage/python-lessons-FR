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
#  Chap. 50     #  Seaborn : corrigés                                          #
#               #                                                              #
################################################################################

"""
Corrigés des exercices du fichier exos_50_seaborn.py. Chaque énoncé est
rappelé, suivi d'une solution commentée. Il y a souvent plusieurs bonnes
solutions : si la vôtre est différente mais donne le même graphique, elle
est probablement juste !

Ces exercices nécessitent seaborn (qui installe aussi NumPy, pandas et
matplotlib). Comme dans le chapitre, les graphiques sont enregistrés en PNG
avec la fonction enregistrer() définie ci-dessous, puis supprimés à la fin.
Pour les regarder, passez GARDER_IMAGES à True. (Dans vos propres programmes,
vous pouvez utiliser plt.show() à la place.)

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

a) Une fonction axes-level dessine dans UN Axes matplotlib (celui qu'on lui
   passe avec ax=, ou l'Axes "courant") et renvoie cet Axes. Une fonction
   figure-level crée sa propre figure, éventuellement avec plusieurs
   graphiques (facettes), et renvoie un objet FacetGrid (ou JointGrid,
   PairGrid…) qui contient la figure (grille.figure) et les Axes
   (grille.axes).
b) relplot est figure-level : elle ne peut pas dessiner dans un Axes
   existant. seaborn ignore ax= et affiche un avertissement (UserWarning) ;
   on se retrouve avec deux figures, dont une vide. Il faut utiliser
   scatterplot(…, ax=ax) à la place.
c) clients est "tidy" : une ligne par client, une colonne par variable.
   ventes_larges ne l'est pas : la variable "magasin" est cachée dans les
   noms des colonnes Lyon, Lille, Nantes (format "large").

2. Transformez ventes_larges au format long avec melt(), dans un DataFrame
   ventes aux colonnes "mois", "magasin" et "ventes". Affichez sa forme
   (shape) et ses 3 premières lignes.
"""
ventes = ventes_larges.melt(id_vars="mois", var_name="magasin",
                            value_name="ventes")
print(ventes.shape)  # => (36, 3)
print(ventes.head(3))
# =>    mois magasin  ventes
# => 0     1    Lyon      42
# => 1     2    Lyon      40
# => 2     3    Lyon      45
# 12 mois × 3 magasins = 36 lignes. id_vars désigne la colonne gardée telle
# quelle ; les anciens noms de colonnes deviennent les valeurs de "magasin".


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

a) Qualitative : des catégories sans ordre ("colorblind", "Set2"…).
b) Séquentielle : des valeurs ordonnées, de "froid" à "chaud" ("rocket",
   "viridis"…). (Une divergente centrée sur 0 °C se défend aussi, si le
   point de référence 0 a un sens pour votre question.)
c) Divergente : on s'écarte d'un point de référence (0 %), dans un sens ou
   dans l'autre ("vlag", "coolwarm"…), avec center=0.
d) Divergente, centrée sur 0, de -1 à 1.

4. Appliquez le thème "ticks", puis créez une palette "colorblind" de 4
   couleurs. Affichez sa longueur. Pourquoi cette palette est-elle un bon
   choix par défaut ?
"""
sns.set_theme(style="ticks")
palette = sns.color_palette("colorblind", 4)
print(len(palette))  # => 4
# Ses couleurs restent distinguables par les personnes daltoniennes (les
# plus fréquentes : difficulté à distinguer rouge et vert). Elle convient à
# des catégories (palette qualitative).


#######################
#  Les distributions  #
#######################

"""
5. Tracez l'histogramme des paniers (colonne "panier") avec 25 intervalles.
   Affichez le nombre de barres dessinées, et le nom de l'axe des x.
   Enregistrez dans exo50_histo.png.
"""
fig, ax = plt.subplots()
sns.histplot(data=clients, x="panier", bins=25, ax=ax)
print(len(ax.patches))  # => 25
print(ax.get_xlabel())  # => panier
enregistrer(fig, "exo50_histo.png")
# seaborn nomme automatiquement l'axe d'après la colonne. Pour un vrai
# graphique, on préciserait l'unité : ax.set_xlabel("Panier (€)").

"""
6. Tracez sur un même graphique la densité (KDE) des paniers pour chaque
   canal (hue). Combien de courbes ont été tracées ? Enregistrez dans
   exo50_kde.png.
"""
fig, ax = plt.subplots()
sns.kdeplot(data=clients, x="panier", hue="canal", ax=ax)
print(len(ax.lines))  # => 2
enregistrer(fig, "exo50_kde.png")
# Une courbe par valeur de "canal" (web, boutique). La courbe "web" est
# décalée vers la droite : les paniers en ligne sont plus élevés.

"""
7. Tracez la fonction de répartition (ecdfplot) des paniers. Puis calculez
   avec pandas la proportion de clients dont le panier est inférieur ou égal
   à 60 € : c'est la hauteur de la courbe en x = 60. Enregistrez dans
   exo50_ecdf.png.
"""
fig, ax = plt.subplots()
sns.ecdfplot(data=clients, x="panier", ax=ax)
ax.axvline(60, color="gray", linestyle="--")  # repère en x = 60
enregistrer(fig, "exo50_ecdf.png")

proportion = (clients["panier"] <= 60).mean()
print(round(proportion, 3))  # => 0.448
# (clients["panier"] <= 60) est une Series de booléens (cf. chap. 39) ; sa
# moyenne est la proportion de True, car True vaut 1 et False vaut 0.


###################################
#  Les relations entre variables  #
###################################

"""
8. Tracez le nuage de points (âge, panier), avec une couleur par canal.
   Vérifiez que le graphique contient bien 250 points. Enregistrez dans
   exo50_nuage.png.
"""
fig, ax = plt.subplots()
sns.scatterplot(data=clients, x="age", y="panier", hue="canal", ax=ax)
print(len(ax.collections[0].get_offsets()))  # => 250
enregistrer(fig, "exo50_nuage.png")
# Tous les points sont dans une seule "collection" matplotlib, même avec
# deux couleurs : seaborn colore chaque point individuellement.

"""
9. Tracez le même nuage avec regplot (sans hue), puis calculez la pente de
   la droite de régression avec np.polyfit. Interprétez-la en une phrase.
   Enregistrez dans exo50_reg.png.
"""
fig, ax = plt.subplots()
sns.regplot(data=clients, x="age", y="panier", ax=ax,
            scatter_kws={"alpha": 0.4})
enregistrer(fig, "exo50_reg.png")

pente, ordonnee = np.polyfit(clients["age"], clients["panier"], 1)
print(round(pente, 2))  # => 0.73
# En moyenne, chaque année d'âge supplémentaire s'accompagne d'environ
# 0,73 € de panier en plus. (On a généré les données avec 0.8 : la
# régression s'en approche, malgré le bruit et l'effet du canal.)
# Attention : c'est une corrélation, pas une cause !

"""
10. Tracez l'évolution des ventes mois par mois, une courbe par magasin, à
    partir du DataFrame ventes de l'exercice 2. Combien d'entrées la légende
    contient-elle ? Enregistrez dans exo50_ventes.png.
"""
fig, ax = plt.subplots()
sns.lineplot(data=ventes, x="mois", y="ventes", hue="magasin", marker="o",
             ax=ax)
ax.set_ylabel("Ventes (milliers d'€)")
ax.set_xticks(range(1, 13))  # un repère par mois
print(len(ax.get_legend().get_texts()))  # => 3
enregistrer(fig, "exo50_ventes.png")
# C'est tout l'intérêt du format long : hue="magasin" suffit pour avoir une
# courbe et une entrée de légende par magasin.


#################################
#  Les variables catégorielles  #
#################################

"""
11. Tracez un barplot du panier moyen par région (ordre : Nord, Sud,
    Ouest). Récupérez la hauteur des barres et comparez-la au résultat d'un
    groupby. Que représentent les petits traits au sommet des barres ?
    Enregistrez dans exo50_barres.png.
"""
ordre = ["Nord", "Sud", "Ouest"]
fig, ax = plt.subplots()
sns.barplot(data=clients, x="region", y="panier", order=ordre, ax=ax)
hauteurs = [round(float(barre.get_height()), 2) for barre in ax.patches]
print(hauteurs)  # => [62.85, 62.68, 64.73]
enregistrer(fig, "exo50_barres.png")

moyennes = clients.groupby("region")["panier"].mean().round(2)
print(moyennes[ordre].tolist())  # => [62.85, 62.68, 64.73]
# Les hauteurs sont bien les moyennes par région. Les traits sont les barres
# d'erreur : par défaut, l'intervalle de confiance à 95 % de la moyenne. Ici
# ils se chevauchent largement : les différences entre régions peuvent
# n'être dues qu'au hasard (on a d'ailleurs tiré les régions au hasard).

"""
12. Avec countplot, tracez le nombre de clients pour chaque note de
    satisfaction (1 à 5). Affichez la liste des effectifs. Enregistrez dans
    exo50_satisfaction.png.
"""
fig, ax = plt.subplots()
sns.countplot(data=clients, x="satisfaction", ax=ax)
effectifs = [int(barre.get_height()) for barre in ax.patches]
print(effectifs)  # => [41, 59, 51, 50, 49]
print(sum(effectifs))  # => 250 : tous les clients sont comptés
enregistrer(fig, "exo50_satisfaction.png")

"""
13. Comparez la distribution des paniers selon le canal : un boxplot, avec
    les points des clients superposés (stripplot). Enregistrez dans
    exo50_box.png.
"""
fig, ax = plt.subplots()
sns.boxplot(data=clients, x="canal", y="panier", color="white", ax=ax)
sns.stripplot(data=clients, x="canal", y="panier", alpha=0.5, ax=ax)
ax.set_ylabel("Panier (€)")
enregistrer(fig, "exo50_box.png")
# color="white" rend les boîtes discrètes, pour que les points restent
# visibles. Ici, swarmplot serait déconseillé : 250 points, c'est beaucoup
# pour un "essaim" sans chevauchement.


#############################################
#  Encoder plus d'informations et facettes  #
#############################################

"""
14. Tracez le nuage (âge, panier) en encodant le canal par la couleur ET la
    forme des points, et la satisfaction par la taille. Pourquoi est-il
    utile de doubler la couleur par la forme ? Enregistrez dans
    exo50_encodage.png.
"""
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=clients, x="age", y="panier", hue="canal",
                style="canal", size="satisfaction", sizes=(15, 120),
                alpha=0.7, ax=ax)
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
enregistrer(fig, "exo50_encodage.png")
# La forme rend le graphique lisible par les personnes daltoniennes, et
# même imprimé en noir et blanc.

"""
15. Avec relplot, faites un nuage (âge, panier) par région, côte à côte
    (col=), dans l'ordre Nord, Sud, Ouest. Affichez la forme de grille.axes,
    puis changez les titres en "Région Nord", etc. Enregistrez dans
    exo50_facettes.png.
"""
grille = sns.relplot(data=clients, x="age", y="panier", col="region",
                     col_order=ordre, hue="canal", height=3.5)
print(grille.axes.shape)  # => (1, 3)
grille.set_titles("Région {col_name}")
print([ax.get_title() for ax in grille.axes[0]])
# => ['Région Nord', 'Région Sud', 'Région Ouest']
enregistrer(grille.figure, "exo50_facettes.png")
# {col_name} est remplacé par la valeur de la colonne pour chaque facette.


############################################
#  Matrices, pairplot et personnalisation  #
############################################

"""
16. Calculez la matrice de corrélation (arrondie à 2 décimales) entre "age",
    "panier" et "satisfaction". Affichez-la, puis tracez-la avec une heatmap
    annotée, une palette divergente centrée sur 0, entre -1 et 1. Quelle
    variable n'est liée à aucune autre ? Enregistrez dans exo50_corr.png.
"""
correlations = clients[["age", "panier", "satisfaction"]].corr().round(2)
print(correlations)
# =>                age  panier  satisfaction
# => age           1.00    0.68         -0.02
# => panier        0.68    1.00          0.03
# => satisfaction -0.02    0.03          1.00
fig, ax = plt.subplots()
sns.heatmap(correlations, annot=True, cmap="vlag", center=0, vmin=-1,
            vmax=1, square=True, ax=ax)
print(len(ax.texts))  # => 9 : une annotation par case
enregistrer(fig, "exo50_corr.png")
# L'âge et le panier sont fortement corrélés. La satisfaction n'est liée à
# rien : ses corrélations sont proches de 0 (elle a été tirée au hasard).

"""
17. Avec pivot_table, calculez le panier moyen par région (lignes) et par
    canal (colonnes), arrondi à 1 décimale. Affichez-le, puis tracez-le en
    heatmap annotée. Enregistrez dans exo50_pivot.png.
"""
tableau = clients.pivot_table(index="region", columns="canal",
                              values="panier", aggfunc="mean").round(1)
print(tableau)
# => canal   boutique   web
# => region
# => Nord        52.3  69.4
# => Ouest       59.4  69.2
# => Sud         56.4  67.2
fig, ax = plt.subplots()
sns.heatmap(tableau, annot=True, fmt=".1f", cmap="rocket_r", ax=ax)
enregistrer(fig, "exo50_pivot.png")
# Des valeurs (des euros) de "peu" à "beaucoup" : une palette séquentielle
# convient. fmt=".1f" affiche une décimale dans chaque case (cf. chap. 8).

"""
18. Tracez un pairplot des colonnes "age", "panier" et "satisfaction", avec
    une couleur par canal. Quelle est la forme de grille.axes ? Enregistrez
    dans exo50_pairplot.png.
"""
grille = sns.pairplot(clients[["age", "panier", "satisfaction", "canal"]],
                      hue="canal", height=2)
print(grille.axes.shape)  # => (3, 3)
enregistrer(grille.figure, "exo50_pairplot.png")
# 3 variables numériques → une grille 3 × 3. "canal" sert de couleur : il
# n'a pas sa propre ligne.


##############################################
#  Bonnes pratiques et graphiques trompeurs  #
##############################################

"""
19. Le graphique ci-dessous est trompeur et peu lisible. Trouvez au moins
    4 défauts, puis refaites-le correctement dans exo50_corrige.png.

    fig, ax = plt.subplots()
    sns.barplot(data=clients, x="region", y="panier", hue="region",
                palette="rainbow", errorbar=None, ax=ax)
    ax.set_ylim(55, 65)
    ax.set_xlabel("")
    ax.set_ylabel("")

Défauts :
    - l'axe des y commence à 55 : pour des BARRES, il faut partir de 0,
      sinon les différences paraissent énormes,
    - pas de barres d'erreur : on ne voit pas que les différences sont
      dans la marge d'incertitude,
    - la palette "rainbow" n'est pas adaptée aux daltoniens, et les couleurs
      n'apportent aucune information (elles répètent l'axe des x),
    - pas de titre, pas de nom d'axe, pas d'unité.
"""
fig, ax = plt.subplots()
sns.barplot(data=clients, x="region", y="panier", order=ordre,
            color="C0", ax=ax)  # une seule couleur ; barres d'erreur (IC)
ax.set_ylim(0, None)  # None : la limite haute reste automatique
ax.set_title("Panier moyen par région (IC à 95 %)")
ax.set_xlabel("Région")
ax.set_ylabel("Panier moyen (€)")
print(ax.get_ylim()[0])  # => 0.0
enregistrer(fig, "exo50_corrige.png")

"""
20. Mini-projet : en une seule figure de 2 × 2 graphiques (plt.subplots(2,
    2) et ax=…), présentez les clients : la distribution des âges, le
    nombre de clients par canal, le panier selon le canal (boxplot), et le
    lien entre âge et panier. Donnez un titre à chaque graphique et un titre
    général (fig.suptitle). Enregistrez dans exo50_tableau_de_bord.png.
"""
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
sns.histplot(data=clients, x="age", bins=15, ax=axes[0, 0])
axes[0, 0].set_title("Âge des clients")
sns.countplot(data=clients, x="canal", ax=axes[0, 1])
axes[0, 1].set_title("Clients par canal")
sns.boxplot(data=clients, x="canal", y="panier", ax=axes[1, 0])
axes[1, 0].set_title("Panier selon le canal")
sns.scatterplot(data=clients, x="age", y="panier", hue="canal",
                alpha=0.6, ax=axes[1, 1])
axes[1, 1].set_title("Âge et panier")
fig.suptitle("Nos clients en un coup d'œil", fontsize=16)
fig.tight_layout()  # évite que les titres se chevauchent
print(len(fig.axes))  # => 4
enregistrer(fig, "exo50_tableau_de_bord.png")
# Les fonctions axes-level acceptent ax= : c'est ce qui permet de les placer
# dans une grille de subplots (cf. chap. 40). Une fonction figure-level
# (displot, catplot…) ne le pourrait pas.


###############
#  Nettoyage  #
###############

plt.close("all")
if not GARDER_IMAGES:
    for nom_fichier in images_creees:
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
    print("Images supprimées")  # => Images supprimées
