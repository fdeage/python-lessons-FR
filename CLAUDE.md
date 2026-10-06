# CLAUDE.md

Ce fichier guide Claude Code (claude.ai/code) lorsqu'il travaille sur le code de ce dépôt.

## Contenu du dépôt

Un cours pour débutants en français, « Data Science with Python » (v.1.0, 2026, CC BY-SA 4.0 FR, inspiré de learnxinyminutes.com). Auteurs : Félix Déage pour les chap. 00 à 31, Claude Opus 5.5 pour les chap. 32 à 51. Chaque leçon est un simple script Python exécutable. Les élèves le lisent dans un éditeur de texte, retapent les exemples dans un shell Python, puis exécutent le fichier pour comparer la sortie. Il n'y a ni package, ni système de build, ni fichier de dépendances, ni configuration de linter, ni suite de tests. Le `README.md` contient le plan complet du cours.

- `chaps/chap_NN_<sujet>.py` : un chapitre par fichier, numérotés dans l'ordre pédagogique (de 00 à 51). Ne jamais renuméroter un chapitre sans mettre à jour tous les renvois `cf. chap. N`, les fichiers correspondants dans `exos/` et `corrs/`, et le plan du `README.md`.
- `exos/exos_NN_<sujet>.py` : les énoncés d'exercices du chapitre NN. Chaque énoncé indique le chemin de son corrigé (`corrs/corr_NN_<sujet>.py`).
- `corrs/corr_NN_<sujet>.py` : les corrigés commentés.
- Les chap. 00 et 01 n'ont pas d'exercices. Il manque actuellement les énoncés 07, 08, 10, 11 et 13 à 17, et les corrigés 06 à 11 et 13 à 17.
- `chaps/my_module.py` et `chaps/my_package/` sont importés par le chap. 22 (et par `corrs/corr_22_modules.py`, qui ajoute `chaps/` à `sys.path` à partir de `__file__`).

## Exécution

```bash
python3 chaps/chap_12_if_then.py     # exécuter un chapitre
python3 corrs/corr_12_if_then.py     # exécuter un corrigé
```

Chaque fichier doit s'exécuter jusqu'au bout (code de sortie 0) avec un `python3` nu, depuis la racine comme depuis son dossier. Pour tous les vérifier, fournir les saisies des `input()` sur l'entrée standard (les chap. 11 à 14 et 26, ainsi que certains exercices, en demandent) :

```bash
for f in chaps/chap_*.py exos/*.py corrs/*.py; do yes 12 | head -100 | python3 -W error::SyntaxWarning "$f" >/dev/null 2>&1 || echo "FAIL $f"; done
for f in chaps/chap_3[7-9]*.py chaps/chap_4[0-9]*.py chaps/chap_5*.py; do uv run --with numpy --with pandas --with matplotlib --with seaborn --with scikit-learn --with requests --with pytest --with mypy python "$f" >/dev/null || echo "FAIL $f"; done   # paquets tiers
```

- Il faut Python 3.10 ou plus récent : le chap. 46 (typing) utilise `X | None` et `list[int]`. D'autres exemples signalent la version qu'ils demandent dans leur commentaire (`f"{x=}"` 3.8, le `|` des dictionnaires 3.9).
- Les imports de paquets tiers (numpy, pandas, matplotlib, seaborn, scikit-learn, requests, pytest, mypy) sont placés dans un `try`/`except ImportError` avec un conseil d'installation (`uv add …` puis pip) et un `sys.exit(0)` propre (ou une section sautée), pour que le fichier tourne sans le paquet. Le cours recommande uv à partir du chap. 47.
- Les chap. 40 et 50 utilisent le backend `Agg` pour s'exécuter sans affichage ; une variable `GARDER_IMAGES = False` contrôle la conservation des images produites.
- Le chap. 49 (requests) démarre un serveur HTTP local pour être déterministe hors ligne ; les appels à de vraies API sont facultatifs et protégés.
- Un fichier qui lit ou écrit des fichiers crée lui-même ses fichiers d'entrée et supprime tout ce qu'il a créé à la fin (y compris les journaux, images, caches de mypy/pytest). Après une exécution, `git status` ne doit montrer aucun fichier résiduel.
- Les sorties attendues (`# =>`) ont été vérifiées avec Python 3.14, numpy 2, pandas 3, matplotlib 3.11, seaborn 0.13 et scikit-learn 1.9. Les messages d'erreur, les temps mesurés et l'affichage des bibliothèques peuvent varier ; c'est alors signalé dans le commentaire.

## Conventions des fichiers de cours (à suivre pour modifier ou ajouter un chapitre)

- **En-tête** : chaque fichier commence par la même bannière en art ASCII (logo DS-WP, version, auteur et année du copyright, licence), puis une ligne encadrée `Chap. N  #  Titre`, puis la liste à puces des sections. Copier la bannière telle quelle depuis un fichier existant, en gardant 80 colonnes. L'auteur est `© Félix Déage - 2026` pour les chap. 00 à 31 et `© Claude Opus 5.5 - 2026` pour les chap. 32 et suivants (exercices et corrigés compris). La version et l'année figurent dans chaque fichier : un changement doit être fait partout. Les en-têtes des énoncés et des corrigés ont des titres de la forme `<sujet> : exercices` / `<sujet> : corrigés`.
- **Sections** : un commentaire `# Titre de section`, souligné par une ligne de `#` à peu près de la même longueur, qui correspond à la liste de l'en-tête.
- **La prose** est écrite en français dans des chaînes entre triples guillemets (`"""…"""`) placées entre les blocs de code. Elle suit la typographie française : espace avant `:`, `?` et `!`, `…` pour les points de suspension, et parfois l'écriture inclusive (`programmeur·se`). Les lignes font 80 colonnes au plus.
- **Les sorties attendues** sont notées en commentaire de fin de ligne après `=>`, par exemple `print(1 + 2)  # => 3`. Elles doivent rester exactes, car les élèves comparent leur propre sortie avec elles.
- **Les erreurs volontaires** sont enveloppées pour que le script continue. Chaque affichage est numéroté dans l'ordre au sein du fichier :
  ```python
  try:
      1 / 0
  except ZeroDivisionError as err:
      print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
  ```
  Le `try`/`except` n'est enseigné formellement qu'au chap. 26 ; les chapitres précédents ne l'utilisent que sous cette forme.
- **`IMPT`** signale un point que les élèves doivent absolument connaître.
- Les chapitres se renvoient les uns aux autres par numéro (`cf. chap. 9`, `voir chap. 26`). Un chapitre n'utilise que des notions déjà vues, ou renvoie explicitement au chapitre qui les détaille. En ajoutant un chapitre, ajouter aussi les renvois vers lui dans les anciens chapitres concernés.
