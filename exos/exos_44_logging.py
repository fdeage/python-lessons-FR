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
#  Chap. 44     #  Journaliser avec logging : exercices                        #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier.

Pour que vos logs s'affichent au même endroit que vos print() (et dans le
bon ordre), configurez logging avec stream=sys.stdout, comme dans le cours.
Si vous appelez basicConfig() dans plusieurs exercices, ajoutez force=True
(Python 3.8+), sinon seul le premier appel sera pris en compte.

Si un exercice crée des fichiers de log, supprimez-les à la fin (en fermant
d'abord les handlers, cf. chap. 44, section "Nettoyage").

Les corrigés sont dans le fichier corrs/corr_44_logging.py.
"""


#################################
#  Pourquoi logging ? Niveaux   #
#################################

"""
1. Citez trois avantages du module logging par rapport à des print() pour
   suivre le fonctionnement d'un programme.

2. Sans exécuter, et sans aucune configuration de logging au préalable,
   qu'affiche ce programme ? Sur quelle sortie (stdout ou stderr) ?

       import logging
       logging.debug("Connexion à la base")
       logging.info("12 lignes chargées")
       logging.warning("3 lignes ignorées")
       logging.error("Rapport non généré")

3. Quel niveau (DEBUG, INFO, WARNING, ERROR, CRITICAL) choisiriez-vous pour
   chacun de ces messages ?
       a) "Valeur de la variable seuil : 0.75"
       b) "Plus d'espace disque : arrêt du programme"
       c) "Fichier ventes.csv chargé (1200 lignes)"
       d) "Colonne 'date' absente, on utilise la date du jour"
       e) "Impossible d'envoyer l'e-mail de rapport"

4. Sans exécuter : que vaut logging.WARNING ? Et
   logging.ERROR > logging.INFO ? Vérifiez ensuite en exécutant.
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

6. Écrivez une fonction charger_csv(nom) qui journalise (niveau INFO, avec
   le logger principal) le message "Chargement de <nom>". Configurez le
   format pour obtenir exactement :
       [INFO] charger_csv : Chargement de clients.csv
   (Indice : %(funcName)s.)

7. Sans exécuter, qu'affiche ce programme ? Pourquoi ? Comment le corriger ?

       import logging, sys
       logging.basicConfig(level=logging.WARNING, stream=sys.stdout)
       logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
       logging.debug("Message de débogage")

8. a) Quel format de date (paramètre datefmt) produit des dates de la forme
      2026-10-06 18:42:07 ? Pourquoi ce format est-il conseillé ?
   b) Dans le format "%(levelname)-8s %(message)s", à quoi sert le "-8" ?
"""


####################################
#  Loggers nommés et hiérarchie    #
####################################

"""
9. Sans exécuter, que valent :
       a) logging.getLogger("ventes") is logging.getLogger("ventes")
       b) logging.getLogger("app.db.requetes").parent.name, sachant que le
          logger "app.db" a déjà été créé avec logging.getLogger("app.db")
       c) logging.getLogger("solo").parent.name

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

11. Vous écrivez un module "statistiques.py", destiné à être importé par
    d'autres programmes.
    a) Comment y créer le logger ? Quel sera son nom ?
    b) Faut-il appeler basicConfig() dans ce module ? Pourquoi ?

12. La bibliothèque que vous utilisez écrit des dizaines de messages INFO
    avec un logger nommé "bavard". Écrivez la ligne qui n'affiche plus que
    ses messages WARNING et plus graves, sans toucher à vos propres
    messages. Vérifiez avec un exemple.
"""


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

14. Sans exécuter, combien de fois le message s'affiche-t-il ? Pourquoi ?
    Comment l'afficher une seule fois ?

        logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                            format="%(message)s", force=True)
        log = logging.getLogger("double")
        log.addHandler(logging.StreamHandler(sys.stdout))
        log.info("Bonjour")

15. a) Un RotatingFileHandler est créé avec maxBytes=1_000_000 et
       backupCount=3. Combien de fichiers de log, au maximum, existeront sur
       le disque ? Quelle place occuperont-ils, au maximum, environ ?
    b) Créez un tel handler (avec maxBytes=100 et backupCount=1) pour un
       logger "mesures", écrivez 20 messages, et affichez la liste des
       fichiers créés. Nettoyez ensuite.

16. Écrivez une fonction lire_prix(texte) qui renvoie float(texte). Si la
    conversion échoue (ValueError), elle doit journaliser l'erreur AVEC son
    traceback, au niveau ERROR, avec le message "Prix illisible : <texte>",
    puis renvoyer None. Écrivez le log dans un fichier, et affichez
    seulement la 1re et la dernière ligne du fichier (le traceback dépend de
    votre ordinateur). Nettoyez ensuite.
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

18. Qu'est-ce qui ne va pas dans chacune de ces lignes ?
        a) logger.info("Connexion de %s (mot de passe : %s)", user, mdp)
        b) logger.error("Erreur")
        c) logger.critical("Fichier chargé")
        d) (dans un except) logger.error("Échec du calcul")
        e) (dans un module importé) logging.basicConfig(level=logging.DEBUG)

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
