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
#  Chap. 44     #  Journaliser avec logging                                    #
#               #                                                              #
################################################################################
#
#  - Pourquoi pas print() ?
#  - Premiers messages
#  - Les cinq niveaux
#  - Configurer avec basicConfig()
#  - Le format des messages
#  - Les loggers nommés
#  - La hiérarchie des loggers
#  - Handlers et formatters
#  - Écrire dans un fichier
#  - Faire tourner les fichiers de log
#  - Journaliser une exception
#  - Logging dans un module ou dans le programme principal
#  - Bonus : configurer avec un dictionnaire
#  - Bonnes pratiques
#  - Nettoyage
#  - En bref
#
#############################################

import logging
import os
import sys

# Pourquoi pas print() ?
#########################

"""
Au chap. 41 (Débogage), on a utilisé print() pour suivre l'exécution d'un
programme. C'est pratique pour un bug ponctuel, mais dans un vrai programme
(un script qui tourne toutes les nuits, une application web, un pipeline de
données…), on veut garder une trace de ce qui se passe, en permanence. On
appelle cela un JOURNAL (en anglais : "log"), et l'action d'y écrire :
"journaliser" (to log).

Pourquoi ne pas simplement garder des print() ?

    - On ne peut pas les désactiver sans modifier le code. Avec logging, une
      seule ligne de configuration suffit pour afficher ou masquer les
      messages de débogage.
    - Ils n'ont pas de niveau d'importance : un message "Fichier chargé" et
      un message "Base de données injoignable" sont traités pareil.
    - Ils ne disent ni QUAND (date et heure) ni OÙ (quel module) le message a
      été produit.
    - Ils vont tous au même endroit (l'écran). Avec logging, on peut envoyer
      les messages à la fois à l'écran, dans un fichier, par e-mail…
    - Ils se mélangent avec la vraie sortie du programme (le résultat d'un
      calcul, par exemple).

Le module logging de la bibliothèque standard résout tous ces problèmes.
C'est l'outil standard en Python : toutes les bibliothèques sérieuses
(requests, pandas, scikit-learn…) l'utilisent.
"""


# Premiers messages
####################

"""
L'utilisation la plus simple : des fonctions du module, une par niveau
d'importance.

    logging.warning("Le fichier est vide")

affiche :

    WARNING:root:Le fichier est vide

c'est-à-dire : NIVEAU:NOM DU LOGGER:MESSAGE. "root" (la racine) est le nom du
logger principal (on verra les loggers nommés plus bas).

IMPT : par défaut, les messages de logging ne sont PAS écrits sur la sortie
standard (stdout, là où écrit print()), mais sur la "sortie d'erreur"
(stderr). Dans un terminal, les deux s'affichent au même endroit, mais on
peut les séparer :

    python3 mon_script.py > resultats.txt

écrit les print() dans resultats.txt, et laisse les logs à l'écran. C'est
justement ce que l'on veut : les logs ne polluent pas les résultats.

Dans ce chapitre, pour que vous puissiez comparer avec les commentaires
"# =>", on configurera logging pour écrire sur stdout (avec stream=sys.stdout,
cf. plus bas). Dans vos propres programmes, gardez le comportement par
défaut (stderr).
"""


# Les cinq niveaux
###################

"""
Chaque message a un NIVEAU, du moins grave au plus grave :

    Niveau     Valeur  Quand l'utiliser ?
    DEBUG        10    détails pour le développeur : valeurs de variables,
                       étapes intermédiaires (remplace les print() de
                       débogage)
    INFO         20    confirmation que tout se passe bien : "Fichier
                       ventes.csv chargé (1200 lignes)"
    WARNING      30    quelque chose d'inattendu, mais le programme continue :
                       "12 lignes ignorées (prix manquant)"
    ERROR        40    une opération a échoué : "Impossible d'écrire le
                       rapport"
    CRITICAL     50    une erreur grave, le programme ne peut sans doute pas
                       continuer : "Base de données injoignable"

Chaque niveau a sa fonction : logging.debug(), logging.info(),
logging.warning(), logging.error(), logging.critical().

On choisit ensuite un niveau MINIMAL d'affichage : seuls les messages de ce
niveau ou plus graves sont affichés. IMPT : par défaut, ce seuil est
WARNING. Les messages debug() et info() sont donc ignorés tant qu'on n'a
pas changé la configuration !
"""
print(logging.DEBUG, logging.INFO, logging.WARNING)  # => 10 20 30
print(logging.ERROR, logging.CRITICAL)               # => 40 50
print(logging.getLevelName(30))                      # => WARNING


# Configurer avec basicConfig()
################################

"""
La fonction logging.basicConfig() configure le logger principal en une
ligne. Ses paramètres les plus utiles :

    level=…      le niveau minimal affiché (logging.DEBUG, logging.INFO…)
    format=…     le format des messages (cf. section suivante)
    stream=…     où écrire (sys.stderr par défaut ; ici sys.stdout)
    filename=…   OU un fichier où écrire (à la place de l'écran)
    force=True   (Python 3.8+) remplace une configuration existante

IMPT : basicConfig() ne fait RIEN si le logger principal est déjà
configuré. Appelez-la une seule fois, tout au début du programme. (Dans ce
chapitre, on la rappelle plusieurs fois pour les besoins de l'exemple, avec
force=True.)
"""
logging.basicConfig(level=logging.WARNING, stream=sys.stdout, force=True)

logging.debug("Valeur de x : 42")          # ignoré : DEBUG < WARNING
logging.info("Chargement terminé")         # ignoré : INFO < WARNING
logging.warning("3 lignes incomplètes")
# => WARNING:root:3 lignes incomplètes
logging.error("Fichier introuvable")       # => ERROR:root:Fichier introuvable

# On abaisse le seuil à DEBUG : tout s'affiche.
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, force=True)
logging.debug("Valeur de x : 42")          # => DEBUG:root:Valeur de x : 42
logging.info("Chargement terminé")         # => INFO:root:Chargement terminé

"""
En pratique : on met level=logging.DEBUG pendant le développement, et
level=logging.INFO (ou WARNING) en production. Les messages de débogage
restent dans le code, prêts à resservir, sans encombrer l'affichage.
"""


# Le format des messages
#########################

"""
Le paramètre format est une chaîne contenant des "champs" de la forme
%(nom)s, qui seront remplacés par les informations du message. (C'est
l'ancienne syntaxe de formatage de Python, avec %, encore utilisée par
logging.) Les champs les plus utiles :

    %(asctime)s     la date et l'heure du message
    %(levelname)s   le niveau (DEBUG, INFO…)
    %(name)s        le nom du logger
    %(message)s     le message lui-même
    %(funcName)s    la fonction qui a produit le message
    %(lineno)d      le numéro de ligne (d pour un entier)
    %(module)s      le nom du module (le fichier, sans .py)

Le paramètre datefmt choisit le format de la date, avec les mêmes codes que
strftime() (cf. chap. 30).
"""
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="[%(levelname)s] %(funcName)s() : %(message)s",
    force=True,
)


def charger(nom_fichier):
    logging.info("Lecture de %s", nom_fichier)


charger("ventes.csv")  # => [INFO] charger() : Lecture de ventes.csv

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    force=True,
)
logging.warning("Disque presque plein")
# => 06/10/2026 18:42:07 WARNING  Disque presque plein
#    (la date et l'heure varient, bien sûr)

"""
Notes :
    - %(levelname)-8s : le "-8" aligne le niveau à gauche sur 8 caractères,
      pour que les messages soient bien alignés en colonne (comme :<8 dans
      une f-string, cf. chap. 8).
    - Le format standard des dates en informatique est l'ISO 8601
      ("%Y-%m-%d %H:%M:%S", c'est-à-dire 2026-10-06 18:42:07) : il se trie
      dans l'ordre chronologique. C'est le format par défaut de asctime.

Pour la suite du chapitre, on revient à un format sans date, pour que les
"# =>" restent identiques à chaque exécution :
"""
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="%(levelname)s:%(name)s:%(message)s",
    force=True,
)


# Les loggers nommés
#####################

"""
Jusqu'ici, on a utilisé le logger principal ("root"), via les fonctions
logging.info(), logging.warning()… Dans un vrai programme, on crée plutôt
un logger PAR MODULE, avec un nom :

    logger = logging.getLogger(__name__)

__name__ vaut le nom du module (cf. chap. 22) : "__main__" pour le
programme principal, "my_package.module1" pour un module importé, etc. On
sait donc immédiatement de quel fichier vient chaque message.

On utilise ensuite les MÉTHODES du logger (cf. chap. 34) : logger.debug(),
logger.info(), logger.warning(), logger.error(), logger.critical().
"""
logger = logging.getLogger(__name__)
print(logger.name)   # => __main__
logger.info("Démarrage de l'analyse")
# => INFO:__main__:Démarrage de l'analyse

ventes_log = logging.getLogger("ventes")
ventes_log.warning("Prix manquant ligne 12")
# => WARNING:ventes:Prix manquant ligne 12

# getLogger() renvoie TOUJOURS le même objet pour un même nom : pas besoin
# de passer le logger d'une fonction à l'autre, il suffit de le redemander.
print(logging.getLogger("ventes") is ventes_log)  # => True


# La hiérarchie des loggers
############################

"""
Les noms de loggers forment une HIÉRARCHIE, avec le point comme séparateur
(comme les packages, cf. chap. 22) : le logger "app.db" est l'"enfant" du
logger "app", lui-même enfant du logger principal "root".

    root
     └── app
          ├── app.db
          └── app.web

Deux règles importantes :

    1. PROPAGATION : un message envoyé à "app.db" est transmis à ses
       parents ("app", puis "root"). C'est pour cela que nos loggers nommés
       ci-dessus s'affichaient : leur message remontait jusqu'au logger
       principal, configuré par basicConfig().

    2. NIVEAU : si un logger n'a pas de niveau propre, il utilise celui de
       son parent. On peut donc régler le niveau de toute une branche d'un
       coup, ou au contraire rendre une partie du programme plus (ou moins)
       bavarde.
"""
app = logging.getLogger("app")
app_db = logging.getLogger("app.db")
print(app_db.parent.name)          # => app
print(app.parent.name)             # => root

app_db.debug("Requête : SELECT * FROM ventes")
# => DEBUG:app.db:Requête : SELECT * FROM ventes

# On rend la base de données moins bavarde : seulement WARNING et plus.
app_db.setLevel(logging.WARNING)
app_db.debug("Requête : SELECT * FROM clients")   # ignoré
app_db.warning("Requête lente (3.2 s)")
# => WARNING:app.db:Requête lente (3.2 s)
logging.getLogger("app.web").debug("GET /accueil")
# => DEBUG:app.web:GET /accueil   ("app.web" n'est pas concerné)

print(app_db.getEffectiveLevel())  # => 30 (son propre niveau : WARNING)
print(app.getEffectiveLevel())     # => 10 (hérité de root : DEBUG)

"""
Application courante : les bibliothèques que vous utilisez ont leurs propres
loggers (par exemple "urllib3" pour requests, cf. chap. 49). Si elles sont
trop bavardes, on les fait taire sans toucher à vos propres messages :

    logging.getLogger("urllib3").setLevel(logging.WARNING)
"""


# Handlers et formatters
#########################

"""
basicConfig() cache en réalité trois types d'objets, que l'on peut
manipuler soi-même pour un contrôle total :

    - le LOGGER : l'objet à qui on envoie les messages (logger.info(…)) ;
    - le(s) HANDLER(S) ("gestionnaire") : décide OÙ envoyer le message
      (écran, fichier…). Un logger peut avoir plusieurs handlers ;
    - le FORMATTER : décide de la FORME du message (le format vu plus haut).
      Chaque handler a son formatter.

Le trajet d'un message :

    logger.info("…")
       │  le niveau du message ≥ niveau du logger ? sinon : ignoré
       ▼
    handler 1 (écran)        handler 2 (fichier)
       │ niveau ≥ niveau        │ niveau ≥ niveau
       │ du handler ?           │ du handler ?
       ▼                        ▼
    formatter 1              formatter 2
       ▼                        ▼
    affichage                écriture dans le fichier

Chaque handler a donc AUSSI un niveau : on peut, par exemple, tout écrire
dans un fichier (DEBUG) mais n'afficher à l'écran que les problèmes
(WARNING).

Construisons un logger "rapport" qui affiche ses messages à l'écran, avec
son propre format :
"""
rapport = logging.getLogger("rapport")
rapport.setLevel(logging.DEBUG)
# On coupe la propagation vers root, sinon chaque message s'afficherait
# deux fois (une fois par notre handler, une fois par celui de root) :
rapport.propagate = False

ecran = logging.StreamHandler(sys.stdout)   # handler vers l'écran
ecran.setLevel(logging.INFO)                # n'affiche que INFO et plus
ecran.setFormatter(logging.Formatter(">> %(levelname)s - %(message)s"))
rapport.addHandler(ecran)

rapport.debug("Détail technique")    # ignoré par le handler (DEBUG < INFO)
rapport.info("Rapport généré")       # => >> INFO - Rapport généré
rapport.error("Graphique manquant")  # => >> ERROR - Graphique manquant


# Écrire dans un fichier
#########################

"""
Le handler FileHandler écrit les messages dans un fichier (en mode ajout
"a" par défaut, cf. chap. 28 : le fichier grossit à chaque exécution).

Ajoutons au logger "rapport" un 2e handler, qui écrit TOUT (dès DEBUG) dans
un fichier, avec un format plus détaillé :
"""
fichier = logging.FileHandler("rapport.log", mode="w", encoding="utf-8")
fichier.setLevel(logging.DEBUG)
fichier.setFormatter(
    logging.Formatter("%(levelname)-8s %(name)s:%(funcName)s : %(message)s")
)
rapport.addHandler(fichier)


def generer_rapport(nb_lignes):
    rapport.debug("Début, %d lignes à traiter", nb_lignes)
    rapport.info("Rapport généré")
    if nb_lignes == 0:
        rapport.warning("Rapport vide")


generer_rapport(0)
# À l'écran (handler "ecran", niveau INFO) :
# => >> INFO - Rapport généré
# => >> WARNING - Rapport vide

# Dans le fichier (handler "fichier", niveau DEBUG) : on le relit.
fichier.flush()   # force l'écriture sur le disque (cf. chap. 28)
with open("rapport.log", encoding="utf-8") as f:
    print(f.read(), end="")
# => DEBUG    rapport:generer_rapport : Début, 0 lignes à traiter
# => INFO     rapport:generer_rapport : Rapport généré
# => WARNING  rapport:generer_rapport : Rapport vide

"""
Le fichier contient le message DEBUG, que l'écran n'a pas affiché : c'est
tout l'intérêt d'avoir plusieurs handlers.
"""


# Faire tourner les fichiers de log
####################################

"""
Un programme qui tourne pendant des mois produit un fichier de log énorme.
Le module logging.handlers propose des handlers qui font "tourner" les
fichiers ("log rotation") :

    - RotatingFileHandler : quand le fichier dépasse maxBytes octets, il est
      renommé en .log.1 (l'ancien .log.1 devient .log.2, etc.) et un nouveau
      fichier vide est créé. On garde au plus backupCount anciens fichiers :
      les plus vieux sont supprimés.
    - TimedRotatingFileHandler : même principe, mais selon le temps (un
      fichier par jour, par semaine…).
"""
from logging.handlers import RotatingFileHandler

tournant = logging.getLogger("capteur")
tournant.setLevel(logging.INFO)
tournant.propagate = False
rotation = RotatingFileHandler(
    "capteur.log", maxBytes=200, backupCount=2, encoding="utf-8"
)
tournant.addHandler(rotation)

for i in range(30):
    tournant.info("Mesure n°%d : température = %.1f °C", i, 20 + i / 10)

print(sorted(f for f in os.listdir(".") if f.startswith("capteur.log")))
# => ['capteur.log', 'capteur.log.1', 'capteur.log.2']
# Les mesures les plus anciennes ont été supprimées : on n'a jamais plus de
# 3 fichiers d'environ 200 octets.
with open("capteur.log", encoding="utf-8") as f:
    print(f.readlines()[-1], end="")
# => Mesure n°29 : température = 22.9 °C

"""
(Dans la réalité, on choisit plutôt maxBytes=10_000_000, soit 10 Mo, et
backupCount=5. On a pris 200 octets pour voir la rotation en action.)
"""


# Journaliser une exception
############################

"""
IMPT : dans un bloc except (cf. chap. 26), utilisez logger.exception(). Il
journalise le message au niveau ERROR, AVEC le traceback complet (cf.
chap. 41), sans arrêter le programme.
"""


def moyenne(valeurs):
    return sum(valeurs) / len(valeurs)


try:
    moyenne([])
except ZeroDivisionError:
    logger.exception("Calcul de la moyenne impossible")
# => ERROR:__main__:Calcul de la moyenne impossible
# => Traceback (most recent call last):
# =>   File "…/chap_44_logging.py", line …, in <module>
# =>     moyenne([])
# =>     ~~~~~~~^^^^
# =>   File "…/chap_44_logging.py", line …, in moyenne
# =>     return sum(valeurs) / len(valeurs)
# =>            ~~~~~~~~~~~~~^~~~~~~~~~~~~~
# => ZeroDivisionError: division by zero
# (les chemins et numéros de ligne dépendent de votre ordinateur)

"""
Comparez avec logger.error("…") : le message seul, sans traceback. Quand on
relit un log après un incident, le traceback est souvent ce qui permet de
comprendre ce qui s'est passé : ne le perdez pas !

Bonne pratique : journaliser ET relancer l'exception si on ne sait pas la
traiter (cf. chap. 26) :

    except ValueError:
        logger.exception("Ligne %d illisible", numero)
        raise
"""


# Logging dans un module ou dans le programme principal
########################################################

"""
IMPT : la règle d'or est de séparer :

    - l'ÉMISSION des messages, partout dans le code : chaque module crée son
      logger en haut du fichier et l'utilise ;
    - la CONFIGURATION (niveaux, handlers, formats), UNE SEULE FOIS, dans le
      programme principal. Un module ne doit jamais appeler basicConfig() :
      c'est au programme qui l'utilise de décider quoi afficher.

Un module "nettoyage.py" ressemble donc à ceci :

    import logging

    logger = logging.getLogger(__name__)    # "nettoyage"

    def supprimer_doublons(lignes):
        resultat = list(dict.fromkeys(lignes))
        logger.info("%d doublons supprimés", len(lignes) - len(resultat))
        return resultat

et le programme principal "main.py" :

    import logging
    import nettoyage

    if __name__ == "__main__":              # cf. chap. 22
        logging.basicConfig(level=logging.INFO)
        nettoyage.supprimer_doublons(["a", "b", "a"])

    # => INFO:nettoyage:1 doublons supprimés

Si le programme principal ne configure rien, les messages INFO du module ne
s'affichent pas (seuil par défaut : WARNING). Le module n'impose rien à
personne : c'est exactement ce que l'on veut d'une bibliothèque.

(Les auteurs de bibliothèques ajoutent parfois
logging.getLogger(__name__).addHandler(logging.NullHandler()), un handler
qui ne fait rien, pour être sûrs de ne jamais rien afficher d'eux-mêmes.)
"""


# Bonus : configurer avec un dictionnaire
##########################################

"""
Pour une configuration complexe (plusieurs loggers, handlers et formatters),
on peut tout décrire dans un dictionnaire (cf. chap. 18) et le passer à
logging.config.dictConfig(). Ce dictionnaire peut même être lu depuis un
fichier JSON ou YAML : on change alors la configuration des logs sans
toucher au code.
"""
import logging.config

CONFIG_LOGS = {
    "version": 1,                        # obligatoire, toujours 1
    "disable_existing_loggers": False,   # ne pas couper les loggers créés
    "formatters": {
        "court": {"format": "{levelname} | {name} | {message}", "style": "{"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",   # syntaxe spéciale pour sys.stdout
            "formatter": "court",
            "level": "INFO",
        },
    },
    "loggers": {
        "pipeline": {"handlers": ["console"], "level": "DEBUG",
                     "propagate": False},
    },
}
logging.config.dictConfig(CONFIG_LOGS)

pipeline = logging.getLogger("pipeline")
pipeline.debug("Ignoré : le handler console est au niveau INFO")
pipeline.info("Étape 1/3 : extraction")
# => INFO | pipeline | Étape 1/3 : extraction

"""
Remarquez "style": "{" : le format utilise alors la syntaxe des accolades
de str.format() (cf. chap. 8) au lieu des %(…)s.
"""


# Bonnes pratiques
###################

"""
1. Formatage "paresseux" : passez les valeurs en ARGUMENTS du logger, avec
   %s (texte), %d (entier), %.2f (float à 2 décimales)…

       logger.debug("Total : %s, lignes : %d", total, nb)     # OUI
       logger.debug(f"Total : {total}, lignes : {nb}")        # à éviter

   Avec la 1re forme, le message n'est construit QUE s'il est vraiment
   affiché. Avec une f-string, il est construit à chaque fois, même si le
   niveau DEBUG est désactivé : c'est du travail inutile (et parfois
   coûteux).
"""


class Statistiques:
    """Un objet dont la conversion en texte est longue à calculer."""

    def __str__(self):
        print("   (calcul coûteux du résumé…)")
        return "résumé des statistiques"


stats = Statistiques()
pipeline.debug("Stats : %s", stats)      # DEBUG désactivé : __str__ n'est
#                                          même pas appelée, rien ne s'affiche
pipeline.info("Stats : %s", stats)
# =>    (calcul coûteux du résumé…)
# => INFO | pipeline | Stats : résumé des statistiques

"""
2. IMPT : ne journalisez JAMAIS de données sensibles : mots de passe, clés
   d'API (cf. chap. 49), numéros de carte bancaire, données de santé… Les
   fichiers de log sont souvent lus par beaucoup de monde, copiés, archivés
   pendant des années. Le RGPD s'applique aussi à eux.

       logger.info("Connexion de %s avec le mot de passe %s", nom, mdp) # NON
       logger.info("Connexion de %s", nom)                              # OUI

3. Des messages UTILES : "Erreur" ne sert à rien. "Impossible de lire
   ventes_2024.csv : colonne 'prix' absente" permet d'agir.

4. Le bon niveau : un log rempli de WARNING que personne ne lit finit par
   être ignoré, y compris le jour où un vrai problème survient.

5. Un logger par module : logger = logging.getLogger(__name__), et la
   configuration dans le programme principal seulement.

6. logging remplace les print() de DÉBOGAGE, pas les print() qui font
   partie du programme (afficher un résultat à l'utilisateur, par exemple).
"""


# Nettoyage
############

"""
Pour supprimer les fichiers de log créés par ce chapitre, il faut d'abord
FERMER les handlers qui les tiennent ouverts (sinon, sous Windows, la
suppression échoue).
"""
for log, handler in [(rapport, fichier), (tournant, rotation)]:
    log.removeHandler(handler)
    handler.close()

for nom in os.listdir("."):
    if nom == "rapport.log" or nom.startswith("capteur.log"):
        os.remove(nom)
print("Fichiers de log supprimés")  # => Fichiers de log supprimés

"""
(logging.shutdown(), appelée automatiquement à la fin du programme, ferme
tous les handlers restants.)
"""


# En bref
##########

"""
    import logging
    logging.basicConfig(level=logging.INFO)   # une fois, dans le programme
                                              # principal
    logger = logging.getLogger(__name__)      # en haut de chaque module
    logger.debug / info / warning / error / critical("… %s", valeur)
    logger.exception("…")                     # dans un except : + traceback

    Niveaux :  DEBUG 10 < INFO 20 < WARNING 30 (défaut) < ERROR 40
               < CRITICAL 50
    format :   "%(asctime)s %(levelname)s %(name)s %(message)s"
    Sortie :   stderr par défaut ; stream=sys.stdout ou filename="app.log"
    Hiérarchie "app" > "app.db" : propagation vers les parents, niveau
               hérité ; logging.getLogger("bavard").setLevel(logging.WARNING)
    Handlers : StreamHandler (écran), FileHandler (fichier),
               RotatingFileHandler (rotation), chacun avec son niveau et
               son Formatter
    Configuration complexe : logging.config.dictConfig({…})
    Jamais de mot de passe ni de donnée personnelle dans un log !
"""
