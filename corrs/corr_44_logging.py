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
#  Chap. 44     #  Journaliser avec logging : corrigés                         #
#               #                                                              #
################################################################################

import logging
import os
import sys
from logging.handlers import RotatingFileHandler

#################################
#  Pourquoi logging ? Niveaux   #
#################################

"""
1. Citez trois avantages du module logging par rapport à des print() pour
   suivre le fonctionnement d'un programme.
"""
"""
    - On peut afficher ou masquer les messages selon leur NIVEAU
      d'importance, en changeant une seule ligne de configuration, sans
      supprimer les messages du code.
    - Chaque message peut indiquer automatiquement sa date, son niveau, le
      module et la fonction qui l'ont produit.
    - On peut envoyer les messages à plusieurs endroits à la fois (écran,
      fichier, fichiers tournants…), chacun avec son propre filtre.
    - Les logs vont sur stderr par défaut : ils ne se mélangent pas avec les
      résultats du programme (stdout).
    - Chaque module a son logger : on peut régler finement ce qu'affiche
      chaque partie du programme, et faire taire une bibliothèque bavarde.
"""

"""
2. Sans exécuter, et sans aucune configuration de logging au préalable,
   qu'affiche ce programme ? Sur quelle sortie (stdout ou stderr) ?

       import logging
       logging.debug("Connexion à la base")
       logging.info("12 lignes chargées")
       logging.warning("3 lignes ignorées")
       logging.error("Rapport non généré")
"""
logging.debug("Connexion à la base")
logging.info("12 lignes chargées")
logging.warning("3 lignes ignorées")
logging.error("Rapport non généré")
# => (sur stderr) WARNING:root:3 lignes ignorées
# => (sur stderr) ERROR:root:Rapport non généré
"""
Sans configuration, le seuil est WARNING : debug() et info() sont ignorés.
Les messages vont sur la sortie d'erreur (stderr), au format
NIVEAU:NOM_DU_LOGGER:MESSAGE. Dans un terminal, ils s'affichent comme des
print(), mais "python3 corr_44_logging.py > sortie.txt" les laisserait à
l'écran au lieu de les écrire dans sortie.txt.

(Pour la suite, on configure logging sur stdout, pour que l'ordre des
affichages soit le même que celui des print().)
"""

"""
3. Quel niveau (DEBUG, INFO, WARNING, ERROR, CRITICAL) choisiriez-vous pour
   chacun de ces messages ?
       a) "Valeur de la variable seuil : 0.75"
       b) "Plus d'espace disque : arrêt du programme"
       c) "Fichier ventes.csv chargé (1200 lignes)"
       d) "Colonne 'date' absente, on utilise la date du jour"
       e) "Impossible d'envoyer l'e-mail de rapport"
"""
"""
a) DEBUG : un détail interne, utile seulement pour déboguer.
b) CRITICAL : le programme ne peut pas continuer.
c) INFO : tout se passe normalement, on le confirme.
d) WARNING : situation inattendue, mais le programme s'adapte et continue.
e) ERROR : une opération a échoué (mais le reste du programme peut
   continuer).
"""

"""
4. Sans exécuter : que vaut logging.WARNING ? Et
   logging.ERROR > logging.INFO ? Vérifiez ensuite en exécutant.
"""
print(logging.WARNING)                # => 30
print(logging.ERROR > logging.INFO)   # => True  (40 > 20)
"""
Les niveaux sont de simples entiers (DEBUG 10, INFO 20, WARNING 30, ERROR 40,
CRITICAL 50) : "afficher à partir de INFO" revient à "afficher si
niveau >= 20".
"""


###############################
#  basicConfig() et format    #
###############################

"""
5. Configurez logging pour afficher sur stdout tous les messages à partir du
   niveau INFO, au format "NIVEAU - message", par exemple :
       INFO - Démarrage
   Puis envoyez un message de chaque niveau (debug, info, warning, error,
   critical). Lesquels s'affichent ?
"""
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(levelname)s - %(message)s",
    force=True,   # remplace la configuration automatique de l'exercice 2
)
logging.debug("Détail")      # ignoré : DEBUG < INFO
logging.info("Démarrage")    # => INFO - Démarrage
logging.warning("Attention")  # => WARNING - Attention
logging.error("Erreur")      # => ERROR - Erreur
logging.critical("Panne")    # => CRITICAL - Panne
"""
Tous les messages s'affichent, sauf celui de niveau DEBUG.
"""

"""
6. Écrivez une fonction charger_csv(nom) qui journalise (niveau INFO, avec
   le logger principal) le message "Chargement de <nom>". Configurez le
   format pour obtenir exactement :
       [INFO] charger_csv : Chargement de clients.csv
   (Indice : %(funcName)s.)
"""
logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="[%(levelname)s] %(funcName)s : %(message)s",
    force=True,
)


def charger_csv(nom):
    logging.info("Chargement de %s", nom)


charger_csv("clients.csv")  # => [INFO] charger_csv : Chargement de clients.csv
"""
%(funcName)s est remplacé par le nom de la fonction qui a émis le message.
On passe nom en argument du logger (formatage "paresseux", cf. le cours)
plutôt que d'utiliser une f-string.
"""

"""
7. Sans exécuter, qu'affiche ce programme ? Pourquoi ? Comment le corriger ?

       import logging, sys
       logging.basicConfig(level=logging.WARNING, stream=sys.stdout)
       logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
       logging.debug("Message de débogage")
"""
"""
Il n'affiche RIEN. basicConfig() ne fait rien si le logger principal est
déjà configuré : le 2e appel est ignoré, le seuil reste WARNING, et le
message DEBUG est filtré.

Pour le vérifier ici (où logging est déjà configuré par les exercices
précédents), on simule un "premier" appel avec force=True :
"""
logging.basicConfig(level=logging.WARNING, stream=sys.stdout, force=True)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)  # ignoré !
logging.debug("Message de débogage")                         # rien
print(logging.getLogger().level)                             # => 30
"""
Corrections possibles :
    - n'appeler basicConfig() qu'une seule fois (la bonne pratique) ;
    - ou ajouter force=True au 2e appel (Python 3.8+) ;
    - ou changer seulement le niveau : logging.getLogger().setLevel(…).
"""
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, force=True)
logging.debug("Message de débogage")  # => DEBUG:root:Message de débogage

"""
8. a) Quel format de date (paramètre datefmt) produit des dates de la forme
      2026-10-06 18:42:07 ? Pourquoi ce format est-il conseillé ?
   b) Dans le format "%(levelname)-8s %(message)s", à quoi sert le "-8" ?
"""
"""
a) datefmt="%Y-%m-%d %H:%M:%S" (mêmes codes que strftime(), cf. chap. 30).
   C'est le format international ISO 8601 : sans ambiguïté (le 06/10 est-il
   le 6 octobre ou le 10 juin ?), et l'ordre alphabétique des lignes est
   aussi l'ordre chronologique.
b) Il aligne le nom du niveau à gauche sur 8 caractères (en complétant avec
   des espaces). Les messages commencent ainsi tous à la même colonne, ce
   qui rend le journal plus lisible :
"""
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, force=True,
                    format="%(levelname)-8s %(message)s")
logging.info("Aligné")      # => INFO     Aligné
logging.warning("Aligné")   # => WARNING  Aligné
logging.debug("Aligné")     # => DEBUG    Aligné


####################################
#  Loggers nommés et hiérarchie    #
####################################

# On revient à un format qui montre le nom du logger :
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, force=True,
                    format="%(levelname)s:%(name)s:%(message)s")

"""
9. Sans exécuter, que valent :
       a) logging.getLogger("ventes") is logging.getLogger("ventes")
       b) logging.getLogger("app.db.requetes").parent.name, sachant que le
          logger "app.db" a déjà été créé avec logging.getLogger("app.db")
       c) logging.getLogger("solo").parent.name
"""
print(logging.getLogger("ventes") is logging.getLogger("ventes"))  # => True
logging.getLogger("app.db")
print(logging.getLogger("app.db.requetes").parent.name)            # => app.db
print(logging.getLogger("solo").parent.name)                       # => root
"""
a) True : getLogger() renvoie toujours le même objet pour un même nom.
b) Le parent est le logger EXISTANT dont le nom est le "préfixe" le plus
   proche : app.db (qui aura lui-même pour parent app, puis root).
c) Un nom sans point a pour parent le logger principal, root.

Détail curieux : si le logger intermédiaire n'existe pas encore, le parent
est provisoirement l'ancêtre existant le plus proche… puis logging corrige
automatiquement la hiérarchie quand le logger intermédiaire est créé :
"""
print(logging.getLogger("x.y.z").parent.name)  # => root ("x.y" n'existe pas)
logging.getLogger("x.y")                       # on crée "x.y"…
print(logging.getLogger("x.y.z").parent.name)  # => x.y  (… corrigé !)

"""
10. Avec la configuration suivante, quels messages s'affichent ? (sans
    exécuter, puis vérifiez)

        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout,
                            format="%(levelname)s:%(name)s:%(message)s",
                            force=True)
        logging.getLogger("app.db").setLevel(logging.WARNING)

        logging.getLogger("app").debug("A")
        logging.getLogger("app.db").info("B")
        logging.getLogger("app.db").error("C")
        logging.getLogger("app.db.cache").debug("D")
        logging.getLogger("app.web").info("E")
"""
logging.getLogger("app.db").setLevel(logging.WARNING)

logging.getLogger("app").debug("A")         # => DEBUG:app:A
logging.getLogger("app.db").info("B")       # ignoré
logging.getLogger("app.db").error("C")      # => ERROR:app.db:C
logging.getLogger("app.db.cache").debug("D")  # ignoré
logging.getLogger("app.web").info("E")      # => INFO:app.web:E
"""
    A : "app" n'a pas de niveau propre, il hérite de root (DEBUG) : affiché.
    B : "app.db" est au niveau WARNING, INFO < WARNING : ignoré.
    C : ERROR ≥ WARNING : affiché.
    D : "app.db.cache" n'a pas de niveau propre : il hérite de son parent
        "app.db" (WARNING), donc DEBUG est ignoré. Le réglage s'applique à
        toute la branche !
    E : "app.web" hérite de "app", qui hérite de root (DEBUG) : affiché.
"""

"""
11. Vous écrivez un module "statistiques.py", destiné à être importé par
    d'autres programmes.
    a) Comment y créer le logger ? Quel sera son nom ?
    b) Faut-il appeler basicConfig() dans ce module ? Pourquoi ?
"""
"""
a) En haut du fichier :
       import logging
       logger = logging.getLogger(__name__)
   Quand le module est importé, __name__ vaut "statistiques" (cf. chap. 22) :
   c'est le nom du logger. (Si on lançait statistiques.py directement, il
   vaudrait "__main__".)
b) Non ! La configuration (niveau, format, destination) appartient au
   PROGRAMME PRINCIPAL, qui est le seul à savoir ce qu'il veut afficher. Un
   module qui appelle basicConfig() impose ses choix à tous ceux qui
   l'importent (et empêche leur propre basicConfig() de fonctionner, puisque
   seul le 1er appel compte).
"""
print(__name__)  # => __main__  (ce fichier est lancé directement)

"""
12. La bibliothèque que vous utilisez écrit des dizaines de messages INFO
    avec un logger nommé "bavard". Écrivez la ligne qui n'affiche plus que
    ses messages WARNING et plus graves, sans toucher à vos propres
    messages. Vérifiez avec un exemple.
"""
bavard = logging.getLogger("bavard")
bavard.info("Je raconte ma vie")      # => INFO:bavard:Je raconte ma vie

logging.getLogger("bavard").setLevel(logging.WARNING)   # la réponse

bavard.info("Je raconte ma vie")      # ignoré désormais
bavard.warning("Problème réel")       # => WARNING:bavard:Problème réel
logging.getLogger("moi").info("Mes messages s'affichent toujours")
# => INFO:moi:Mes messages s'affichent toujours


###############################
#  Handlers et formatters     #
###############################

"""
13. Créez un logger "import_csv" qui :
       - affiche à l'écran (stdout) les messages à partir de WARNING, au
         format "!! message" ;
       - écrit TOUS les messages (dès DEBUG) dans le fichier import.log, au
         format "NIVEAU:message".
    Envoyez-lui un message debug, un info et un warning. Puis relisez et
    affichez le contenu de import.log. Enfin, fermez le handler de fichier
    et supprimez import.log.
"""
import_csv = logging.getLogger("import_csv")
import_csv.setLevel(logging.DEBUG)   # le logger laisse tout passer : ce sont
import_csv.propagate = False         # les handlers qui filtrent. Et pas de
#                                      propagation vers root (sinon doublons)

ecran = logging.StreamHandler(sys.stdout)
ecran.setLevel(logging.WARNING)
ecran.setFormatter(logging.Formatter("!! %(message)s"))
import_csv.addHandler(ecran)

fichier = logging.FileHandler("import.log", mode="w", encoding="utf-8")
fichier.setLevel(logging.DEBUG)
fichier.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
import_csv.addHandler(fichier)

import_csv.debug("Ouverture du fichier")
import_csv.info("250 lignes lues")
import_csv.warning("2 lignes vides")   # => !! 2 lignes vides

fichier.flush()
with open("import.log", encoding="utf-8") as f:
    print(f.read(), end="")
# => DEBUG:Ouverture du fichier
# => INFO:250 lignes lues
# => WARNING:2 lignes vides

import_csv.removeHandler(fichier)
fichier.close()          # IMPT : fermer avant de supprimer
os.remove("import.log")
print(os.path.exists("import.log"))  # => False

"""
Le logger est réglé sur DEBUG pour laisser passer tous les messages vers ses
handlers ; c'est ensuite chaque handler qui applique son propre seuil.
Si le logger était réglé sur WARNING, le fichier ne recevrait jamais les
messages DEBUG et INFO.
"""

"""
14. Sans exécuter, combien de fois le message s'affiche-t-il ? Pourquoi ?
    Comment l'afficher une seule fois ?

        logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                            format="%(message)s", force=True)
        log = logging.getLogger("double")
        log.addHandler(logging.StreamHandler(sys.stdout))
        log.info("Bonjour")
"""
logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                    format="%(message)s", force=True)
log = logging.getLogger("double")
log.addHandler(logging.StreamHandler(sys.stdout))
log.info("Bonjour")
# => Bonjour
# => Bonjour
"""
Deux fois : une fois par le handler du logger "double", puis une 2e fois
parce que le message se PROPAGE au logger principal (root), qui a son propre
handler (créé par basicConfig). Solutions : log.propagate = False, ou ne
pas ajouter de handler à "double" (et laisser root tout afficher).
"""
log.propagate = False
log.info("Bonjour")  # => Bonjour

"""
15. a) Un RotatingFileHandler est créé avec maxBytes=1_000_000 et
       backupCount=3. Combien de fichiers de log, au maximum, existeront sur
       le disque ? Quelle place occuperont-ils, au maximum, environ ?
    b) Créez un tel handler (avec maxBytes=100 et backupCount=1) pour un
       logger "mesures", écrivez 20 messages, et affichez la liste des
       fichiers créés. Nettoyez ensuite.
"""
"""
a) 4 fichiers : le fichier courant (app.log) et 3 anciens (app.log.1,
   app.log.2, app.log.3). Chacun fait au plus environ 1 Mo, soit environ
   4 Mo au total, quelle que soit la durée de fonctionnement du programme.
b)
"""
mesures = logging.getLogger("mesures")
mesures.setLevel(logging.INFO)
mesures.propagate = False
rotation = RotatingFileHandler("mesures.log", maxBytes=100, backupCount=1,
                               encoding="utf-8")
mesures.addHandler(rotation)

for i in range(20):
    mesures.info("Mesure %d", i)

print(sorted(f for f in os.listdir(".") if f.startswith("mesures.log")))
# => ['mesures.log', 'mesures.log.1']

mesures.removeHandler(rotation)
rotation.close()
for nom in os.listdir("."):
    if nom.startswith("mesures.log"):
        os.remove(nom)

"""
16. Écrivez une fonction lire_prix(texte) qui renvoie float(texte). Si la
    conversion échoue (ValueError), elle doit journaliser l'erreur AVEC son
    traceback, au niveau ERROR, avec le message "Prix illisible : <texte>",
    puis renvoyer None. Écrivez le log dans un fichier, et affichez
    seulement la 1re et la dernière ligne du fichier (le traceback dépend de
    votre ordinateur). Nettoyez ensuite.
"""
prix_log = logging.getLogger("prix")
prix_log.propagate = False
fichier_prix = logging.FileHandler("prix.log", mode="w", encoding="utf-8")
fichier_prix.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
prix_log.addHandler(fichier_prix)


def lire_prix(texte):
    try:
        return float(texte)
    except ValueError:
        prix_log.exception("Prix illisible : %s", texte)
        return None


print(lire_prix("12.5"))   # => 12.5
print(lire_prix("12,5"))   # => None

fichier_prix.flush()
with open("prix.log", encoding="utf-8") as f:
    lignes = f.read().splitlines()
print(lignes[0])   # => ERROR:Prix illisible : 12,5
print(lignes[-1])  # => ValueError: could not convert string to float: '12,5'

prix_log.removeHandler(fichier_prix)
fichier_prix.close()
os.remove("prix.log")
"""
logger.exception() s'utilise uniquement dans un bloc except : il journalise
au niveau ERROR et ajoute automatiquement le traceback (les lignes entre la
1re et la dernière : "Traceback (most recent call last):", "File …").
"""


########################
#  Bonnes pratiques    #
########################

"""
17. Réécrivez ces lignes avec un formatage "paresseux" (les valeurs passées
    en arguments du logger). Pourquoi est-ce préférable ?

        logger.debug(f"Lecture de {nom_fichier}")
        logger.info(f"{nb} lignes lues en {duree:.2f} s")
        logger.warning("Valeur négative : " + str(valeur))
"""
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, force=True,
                    format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger("exo17")
nom_fichier, nb, duree, valeur = "meteo.csv", 365, 0.123456, -4

logger.debug("Lecture de %s", nom_fichier)
# => DEBUG:exo17:Lecture de meteo.csv
logger.info("%d lignes lues en %.2f s", nb, duree)
# => INFO:exo17:365 lignes lues en 0.12 s
logger.warning("Valeur négative : %s", valeur)
# => WARNING:exo17:Valeur négative : -4
"""
Avec une f-string ou une concaténation, le message est construit AVANT
l'appel, même s'il ne sera jamais affiché (par exemple un debug() quand le
niveau est INFO) : c'est du travail inutile, parfois coûteux. Avec des
arguments, logging ne construit le message que s'il passe le filtre de
niveau.

(%s : n'importe quelle valeur convertie en texte ; %d : un entier ; %.2f :
un float à 2 décimales. C'est l'ancienne syntaxe de formatage, cf. chap. 8.)
"""

"""
18. Qu'est-ce qui ne va pas dans chacune de ces lignes ?
        a) logger.info("Connexion de %s (mot de passe : %s)", user, mdp)
        b) logger.error("Erreur")
        c) logger.critical("Fichier chargé")
        d) (dans un except) logger.error("Échec du calcul")
        e) (dans un module importé) logging.basicConfig(level=logging.DEBUG)
"""
"""
a) On écrit un MOT DE PASSE dans le journal : c'est une faille de sécurité
   (les logs sont lus, copiés, archivés…). Ne jamais journaliser de donnée
   sensible : logger.info("Connexion de %s", user).
b) Le message n'apporte aucune information : quelle erreur ? Sur quoi ?
   Avec quelles données ? Par exemple : "Impossible d'écrire rapport.pdf :
   dossier introuvable".
c) Mauvais niveau : charger un fichier est un événement normal (INFO).
   Abuser de CRITICAL rend les vrais problèmes invisibles.
d) Dans un except, logger.exception("Échec du calcul") garde le traceback,
   indispensable pour comprendre la cause.
e) Un module ne doit pas configurer logging : c'est le rôle du programme
   principal (cf. exercice 11).
"""

"""
19. (Problème) Écrivez une fonction nettoyer_temperatures(valeurs) qui
    reçoit une liste de strings (lues dans un fichier) et renvoie la liste
    des températures valides, en float. Elle utilise un logger nommé
    "nettoyage" et journalise :
       - au niveau DEBUG, chaque valeur acceptée ;
       - au niveau WARNING, chaque valeur ignorée, avec la raison : "non
         numérique" si float() échoue, "hors limites" si la température
         n'est pas entre -50 et 60 ;
       - au niveau INFO, un bilan : "<n> valeurs gardées sur <total>".
    Configurez logging (dans le "programme principal", c'est-à-dire en bas
    du fichier) pour afficher sur stdout les messages à partir de INFO, au
    format "%(levelname)s:%(name)s:%(message)s", et testez avec :
        ["12.5", "abc", "18", "999", "-3", ""]
    Puis passez le niveau à DEBUG : que change-t-il ?
"""
# Dans un vrai projet, cette partie serait dans un module nettoyage.py, avec
# logger = logging.getLogger(__name__).
nettoyage_log = logging.getLogger("nettoyage")


def nettoyer_temperatures(valeurs):
    gardees = []
    for texte in valeurs:
        try:
            temperature = float(texte)
        except ValueError:
            nettoyage_log.warning("Valeur ignorée (%r) : non numérique", texte)
            continue
        if not -50 <= temperature <= 60:
            nettoyage_log.warning("Valeur ignorée (%r) : hors limites", texte)
            continue
        nettoyage_log.debug("Valeur acceptée : %s", temperature)
        gardees.append(temperature)
    nettoyage_log.info("%d valeurs gardées sur %d", len(gardees),
                       len(valeurs))
    return gardees


# "Programme principal" : la configuration se fait ici, et nulle part
# ailleurs.
donnees = ["12.5", "abc", "18", "999", "-3", ""]

logging.basicConfig(level=logging.INFO, stream=sys.stdout, force=True,
                    format="%(levelname)s:%(name)s:%(message)s")
print(nettoyer_temperatures(donnees))
# => WARNING:nettoyage:Valeur ignorée ('abc') : non numérique
# => WARNING:nettoyage:Valeur ignorée ('999') : hors limites
# => WARNING:nettoyage:Valeur ignorée ('') : non numérique
# => INFO:nettoyage:3 valeurs gardées sur 6
# => [12.5, 18.0, -3.0]

logging.getLogger().setLevel(logging.DEBUG)
print(nettoyer_temperatures(donnees))
# => DEBUG:nettoyage:Valeur acceptée : 12.5
# => WARNING:nettoyage:Valeur ignorée ('abc') : non numérique
# => DEBUG:nettoyage:Valeur acceptée : 18.0
# => WARNING:nettoyage:Valeur ignorée ('999') : hors limites
# => DEBUG:nettoyage:Valeur acceptée : -3.0
# => WARNING:nettoyage:Valeur ignorée ('') : non numérique
# => INFO:nettoyage:3 valeurs gardées sur 6
# => [12.5, 18.0, -3.0]

"""
Au niveau DEBUG, on voit en plus chaque valeur acceptée : utile pendant le
développement, trop bavard en production. Et on est passé de l'un à l'autre
sans toucher à la fonction : c'est tout l'intérêt de logging.

Remarques :
    - %r affiche la repr() de la valeur (cf. chap. 41) : on voit ainsi
      clairement la chaîne vide ('') qui, avec %s, serait invisible.
    - Le "continue" (cf. chap. 13) passe directement à la valeur suivante.
"""
