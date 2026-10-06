# Data Science with Python

Un cours de Python pour débutants, en français, qui part de zéro et va jusqu'à la Data Science et au Machine Learning.

Chaque leçon est un **script Python exécutable** : le texte du cours est écrit en commentaires et en chaînes `"""…"""`, entre les exemples de code. On lit le cours dans un éditeur de texte, on retape les exemples dans un shell Python, puis on exécute le fichier pour comparer.

- Version 1.0 — 2026
- Licence [CC BY-SA 4.0 FR](https://creativecommons.org/licenses/by-sa/4.0/deed.fr)
- Inspiré de [learnxinyminutes.com](https://learnxinyminutes.com)
- Auteurs : Félix Déage (chap. 00 à 31), Claude Opus 5.5 (chap. 32 à 51)

## Organisation du dépôt

```
chaps/chap_NN_<sujet>.py    le cours : un chapitre par fichier
chaps/my_module.py          modules d'exemple importés par le chap. 22
chaps/my_package/
exos/exos_NN_<sujet>.py     les énoncés d'exercices du chapitre NN
corrs/corr_NN_<sujet>.py    leurs corrigés commentés
```

Les chapitres 00 et 01 (introduction et mode d'emploi) n'ont pas d'exercices.

## Comment utiliser ce cours

1. Lisez le chap. 01, qui explique comment travailler avec ce tutoriel.
2. Pour chaque chapitre : lisez, retapez les exemples, puis exécutez le fichier.
   ```bash
   python3 chaps/chap_12_if_then.py
   ```
3. Faites les exercices dans `exos/` **avant** d'ouvrir les corrigés dans `corrs/`.

Conventions utilisées dans le code :

- `print(1 + 2)  # => 3` : ce qui suit `=>` est la sortie attendue.
- Les erreurs volontaires sont interceptées par un `try … except …`, pour que le fichier s'exécute jusqu'au bout. Leurs messages sont numérotés (`1: (Sans ce try: …`).
- `IMPT` signale un point essentiel, à connaître absolument.

## Installation

Il faut **Python 3.10 ou plus récent** (le cours est testé avec Python 3.14). Les chap. 00 à 37 et 41 à 47 n'utilisent que la bibliothèque standard.

Les chapitres de Data Science utilisent des paquets externes. Le cours recommande [uv](https://docs.astral.sh/uv/) (cf. chap. 47) :

```bash
uv run --with numpy --with pandas --with matplotlib python chaps/chap_40_matplotlib.py
```

ou, dans un environnement virtuel :

```bash
pip install numpy pandas matplotlib seaborn scikit-learn requests pytest mypy
```

Sans ces paquets, les fichiers concernés affichent un message d'installation et s'arrêtent proprement.

## Plan du cours

### Fondamentaux

| Chap. | Sujet |
|---|---|
| 00 | Introduction |
| 01 | Utiliser ce tutoriel |
| 02 | Lancer Python |
| 03 | Commentaires |
| 04 | Nombres, opérateurs et arithmétique |
| 05 | Ordre des opérations (précédence), whitespace |
| 06 | Conversions : types, binaire, décimal et hexadécimal |
| 07 | Strings I |
| 08 | Manipuler les strings |
| 09 | Booléens I : valeurs, opérateurs, expressions |
| 10 | Variables I : valeurs et types |
| 11 | Saisie utilisateur |
| 12 | Structures de contrôle I : if, then, else et elif |
| 13 | Structures de contrôle II : les boucles, range() |
| 14 | Fonctions I : built-ins, définitions, prototypes |
| 15 | Fonctions II : valeurs de retour |
| 16 | Types construits I : les listes (I) |
| 17 | Types construits II : les tuples |
| 18 | Types construits III : les dictionnaires (I) |
| 19 | Variables II : portée et namespaces |
| 20 | Formatage II |
| 21 | Booléens II |
| 22 | Modules, packages et import |
| 23 | Itérables & compréhensions |
| 24 | Types construits I : les listes (II) |
| 25 | Types construits IV : les ensembles |
| 26 | Erreurs et exceptions |
| 27 | Types construits III : les dictionnaires (II) |
| 28 | Gestion de fichiers |
| 29 | Tests et spécification I |
| 30 | Date et heure |
| 31 | Slices |

### Python avancé

| Chap. | Sujet |
|---|---|
| 32 | Fonctions III : paramètres avancés et lambda |
| 33 | Fonctions IV : la récursivité |
| 34 | Programmation orientée objet I : classes et instances |
| 35 | Programmation orientée objet II : héritage et cie |
| 36 | Générateurs (et décorateurs) |
| 37 | Tests et spécification II : pytest |

### Data Science I

| Chap. | Sujet |
|---|---|
| 38 | NumPy |
| 39 | Pandas I |
| 40 | Matplotlib |

### Outils du développeur

| Chap. | Sujet |
|---|---|
| 41 | Débogage |
| 42 | Expressions régulières |
| 43 | Collections et outils de la bibliothèque standard |
| 44 | Journaliser avec logging |
| 45 | Complexité algorithmique |
| 46 | Typing et annotations de type |
| 47 | Packaging : pip, conda, poetry et uv |

### Data Science II

| Chap. | Sujet |
|---|---|
| 48 | Pandas II |
| 49 | Récupérer des données sur le Web : requests |
| 50 | Seaborn |
| 51 | Introduction au Machine Learning |

## Vérifier que tout s'exécute

Chaque fichier doit s'exécuter jusqu'au bout. Pour tout vérifier d'un coup (les `input()` reçoivent des réponses automatiques) :

```bash
for f in chaps/chap_*.py exos/*.py corrs/*.py; do
  yes 12 | head -100 | python3 "$f" > /dev/null 2>&1 || echo "ÉCHEC $f"
done
```
