# CLAUDE.md

Ce fichier guide Claude Code (claude.ai/code) lorsqu'il travaille sur le code de ce dépôt.

## Contenu du dépôt

Un cours pour débutants en français, « Data Science with Python » (v.0.9, © Félix Déage, CC BY-SA 4.0 FR, inspiré de learnxinyminutes.com). Chaque leçon est un simple script Python exécutable. Les élèves le lisent dans un éditeur de texte, retapent les exemples dans un shell Python, puis exécutent le fichier pour comparer la sortie. Il n'y a ni package, ni système de build, ni fichier de dépendances, ni configuration de linter, ni suite de tests.

- `chap_NN_<sujet>.py` : un chapitre par fichier, numérotés dans l'ordre pédagogique (de 00 intro à 40). Ne jamais renuméroter un chapitre sans mettre à jour tous les renvois `cf. chap. N` et les fichiers correspondants dans `exos/`.
- `exos/exos_NN_<sujet>.py` : les exercices du chapitre NN. `exos/corr_NN_<sujet>.py` : leurs corrigés. Les chapitres 02 à 40 ont chacun un énoncé et un corrigé (00 et 01 n'en ont pas).

## Exécution

```bash
python3 chap_12_if_then.py        # exécuter un chapitre
python3 exos/corr_12_if_then.py   # exécuter un corrigé
```

Chaque fichier doit s'exécuter jusqu'au bout (code de sortie 0) avec un `python3` nu. Pour tous les vérifier, fournir les saisies des `input()` sur l'entrée standard (les chap. 11 à 14 et 26, ainsi que certains exercices, en demandent) :

```bash
for f in chap_*.py exos/*.py; do yes 12 | head -100 | python3 -W error::SyntaxWarning "$f" >/dev/null 2>&1 || echo "FAIL $f"; done
for f in chap_3[7-9]*.py chap_40*.py; do uv run --with numpy --with pandas --with matplotlib --with pytest python "$f" >/dev/null || echo "FAIL $f"; done   # paquets tiers
```

- Le cours cible Python 3.6+. Quelques exemples demandent une version plus récente, ce qu'indique le commentaire à côté (`f"{x=}"` 3.8, `list[int]` et le `|` des dictionnaires 3.9).
- Les imports de paquets tiers (numpy aux chap. 00 et 38, pytest au 37, pandas au 39, matplotlib au 40) sont placés dans un `try`/`except ImportError` avec un conseil d'installation et un `sys.exit(0)` propre (ou une section sautée), pour que le fichier tourne sans le paquet. Le chap. 40 utilise le backend `Agg` pour s'exécuter sans affichage.
- Un fichier qui lit ou écrit des fichiers (chap. 23, 28, 36, 37, 39, 40 et leurs exercices) crée lui-même ses fichiers d'entrée et supprime tout ce qu'il a créé à la fin. Après une exécution, `git status` ne doit montrer aucun fichier résiduel.
- `my_module.py` et `my_package/`, à la racine, sont importés par le chap. 22.
- Les sorties attendues (`# =>`) ont été vérifiées avec Python 3.14, numpy 2 et pandas 3. Les messages d'erreur et l'affichage de pandas/numpy peuvent varier légèrement selon les versions.

## Conventions des fichiers de cours (à suivre pour modifier ou ajouter un chapitre)

- **En-tête** : chaque fichier commence par la même bannière en art ASCII (logo DS-WP, version, année du copyright, licence), puis une ligne encadrée `Chap. N  #  Titre`, puis la liste à puces des sections. Copier la bannière telle quelle depuis un fichier existant. La version et l'année figurent dans chaque fichier : un changement doit être fait partout. Les en-têtes des énoncés et des corrigés ont des titres de la forme `<sujet> : exercices` / `<sujet> : corrigés`.
- **Sections** : un commentaire `# Titre de section`, souligné par une ligne de `#` à peu près de la même longueur, qui correspond à la liste de l'en-tête.
- **La prose** est écrite en français dans des chaînes entre triples guillemets (`"""…"""`) placées entre les blocs de code. Elle suit la typographie française : espace avant `:`, `?` et `!`, `…` pour les points de suspension, et parfois l'écriture inclusive (`programmeur·se`).
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
- Les chapitres se renvoient les uns aux autres par numéro (`cf. chap. 9`, `voir chap. 26`). En cas de renumérotation ou de réorganisation, mettre à jour ces renvois et les noms de fichiers (l'historique git montre que des chapitres ont déjà été scindés et réordonnés).
