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
#  Chap. 49     #  Récupérer des données sur le Web : exercices                #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", essayez de prévoir le résultat
avant de lancer le programme.

Ces exercices nécessitent requests ("uv add requests", ou lancez ce fichier
avec "uv run --with requests --with pandas exos_49_requests.py").

Comme dans le chapitre, on démarre ci-dessous ("Préparation") le petit
serveur de démonstration : toutes vos requêtes se font vers l'adresse BASE
(sans Internet). Il est arrêté tout à la fin du fichier ("Nettoyage") :
écrivez vos réponses AVANT cette section. Rappel des routes :
    GET  /api/stations              liste des stations (filtre ?ville=…)
    GET  /api/releves?page=N        relevés, par pages de 3
    POST /api/releves               ajoute un relevé (renvoie 201)
    GET  /api/prive                 exige l'en-tête X-API-Key: demo-123
    GET  /api/quota                 répond toujours 429 (Retry-After: 1)
    GET  /lent                      met 1 seconde à répondre
    GET  /releves.csv               un fichier CSV
    GET  /robots.txt                les règles pour les robots

Les corrigés sont dans le fichier corrs/corr_49_requests.py.
"""


#################
#  Préparation  #
#################

# Le même serveur que dans le chapitre (inutile de le lire en détail).
import json
import os
import socket
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

STATIONS = [
    {"id": 1, "nom": "Lyon-Bron", "ville": "Lyon", "altitude": 200},
    {"id": 2, "nom": "Paris-Montsouris", "ville": "Paris", "altitude": 75},
    {"id": 3, "nom": "Lyon-St-Exupéry", "ville": "Lyon", "altitude": 235},
]
RELEVES = [
    {"date": f"2024-03-0{j}", "station": 1, "temp": t}
    for j, t in zip(range(1, 8), [8.5, 10.0, 12.5, 9.0, 7.5, 11.0, 13.5])
]
CLE_SECRETE = "demo-123"
CSV_RELEVES = "date,temp\n2024-03-01,8.5\n2024-03-02,10.0\n2024-03-03,12.5\n"


class ApiMeteo(BaseHTTPRequestHandler):
    """Le gestionnaire de requêtes de notre serveur (cf. chap. 34-35)."""

    def repondre(self, statut, contenu, type_contenu="application/json"):
        if type_contenu == "application/json":
            contenu = json.dumps(contenu, ensure_ascii=False)
        corps = contenu.encode("utf-8")
        self.send_response(statut)
        self.send_header("Content-Type", f"{type_contenu}; charset=utf-8")
        self.send_header("Content-Length", str(len(corps)))
        if statut == 429:
            self.send_header("Retry-After", "1")
        self.end_headers()
        try:
            self.wfile.write(corps)
        except (BrokenPipeError, ConnectionResetError):
            pass  # le client est parti avant la fin (timeout, cf. plus bas)

    def do_GET(self):
        url = urlparse(self.path)
        params = parse_qs(url.query)  # {"ville": ["Lyon"]}
        if url.path == "/api/stations":
            ville = params.get("ville", [None])[0]
            res = [s for s in STATIONS if ville is None or s["ville"] == ville]
            self.repondre(200, res)
        elif url.path == "/api/releves":
            page = int(params.get("page", ["1"])[0])
            debut = (page - 1) * 3
            morceau = RELEVES[debut:debut + 3]
            suivante = page + 1 if debut + 3 < len(RELEVES) else None
            self.repondre(200, {"page": page, "page_suivante": suivante,
                                "resultats": morceau})
        elif url.path == "/api/prive":
            if self.headers.get("X-API-Key") == CLE_SECRETE:
                self.repondre(200, {"message": "Bienvenue !"})
            else:
                self.repondre(401, {"erreur": "clé d'API manquante"})
        elif url.path == "/api/quota":
            self.repondre(429, {"erreur": "trop de requêtes"})
        elif url.path == "/lent":
            time.sleep(1)
            self.repondre(200, {"message": "enfin !"})
        elif url.path == "/releves.csv":
            self.repondre(200, CSV_RELEVES, "text/csv")
        elif url.path == "/robots.txt":
            self.repondre(200, "User-agent: *\nDisallow: /api/prive\n",
                          "text/plain")
        else:
            self.repondre(404, {"erreur": "introuvable"})

    def do_POST(self):
        taille = int(self.headers.get("Content-Length", 0))
        recu = json.loads(self.rfile.read(taille) or b"{}")
        recu["id"] = len(RELEVES) + 1
        self.repondre(201, recu)

    def log_message(self, *args):
        pass  # coupe l'affichage de chaque requête dans la console


# Port 0 : le système choisit un port libre (il change à chaque exécution).
serveur = ThreadingHTTPServer(("127.0.0.1", 0), ApiMeteo)
serveur.daemon_threads = True
threading.Thread(target=serveur.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{serveur.server_port}"

# Si votre ordinateur passe par un proxy, on lui demande d'ignorer localhost :
os.environ["NO_PROXY"] = "127.0.0.1,localhost"


#################################
#  Le Web en bref, URL et JSON  #
#################################

"""
1. Sans exécuter : pour chacun de ces codes de statut, dites s'il s'agit
   d'un succès, d'une erreur du client ou d'une erreur du serveur, et ce
   qu'il signifie : 200, 201, 401, 404, 429, 500, 503.
   Puis écrivez une fonction categorie(code) qui renvoie "succès",
   "redirection", "erreur client" ou "erreur serveur".

2. Avec urllib.parse.urlparse et parse_qs (bibliothèque standard), découpez
   l'URL ci-dessous et affichez son schéma, son hôte, son chemin et le
   dictionnaire de ses paramètres.

3. Sans exécuter : qu'affiche ce programme ?
       import json
       d = json.loads('{"actif": true, "valeurs": [1, null], "nom": "A"}')
       print(d["actif"], d["valeurs"], type(d["nom"]))
       print(json.dumps({"x": None, "ok": False}))
"""
URL_EXO_2 = "https://api.exemple.org/v1/releves?station=12&debut=2024-03-01"


################################
#  urllib et première requête  #
################################

"""
4. Avec urllib.request (sans requests), récupérez /api/stations et affichez
   le nom de chaque station.

5. Avec requests, récupérez /api/stations et affichez le nom des stations
   situées à plus de 100 m d'altitude.

6. Sans exécuter : pour une réponse 404, que valent .ok et .status_code ?
   requests lève-t-il une erreur ? Vérifiez avec l'URL BASE + "/rien".

7. Affichez le type de contenu (en-tête Content-Type) renvoyé par
   /releves.csv, puis les deux premières lignes de son texte.
"""


######################
#  Paramètres d'URL  #
######################

"""
8. Avec params=…, récupérez les stations de la ville de Paris. Affichez
   l'URL réellement appelée (à partir du "?") et le nombre de stations.

9. Écrivez une fonction stations_de(ville) qui renvoie la liste des NOMS
   des stations de cette ville. Testez avec "Lyon", "Paris" et "Nice".
"""


########################
#  Timeout et erreurs  #
########################

"""
10. Appelez /lent successivement avec des timeouts de 0.2, 0.5 puis
    3 secondes. Pour chacun, affichez "timeout X s : réussi" ou
    "timeout X s : trop lent".

11. Écrivez une fonction recuperer(url) qui renvoie le JSON de l'URL, ou
    None en cas d'erreur réseau OU de code d'erreur HTTP, en affichant le
    nom de l'erreur. Testez-la sur /api/stations, sur /rien et sur une
    adresse où personne n'écoute ("http://127.0.0.1:9/").

12. Sans exécuter : dans quel ordre faut-il écrire ces trois "except" ?
    Pourquoi ?
        except requests.RequestException: …
        except requests.Timeout: …
        except requests.HTTPError: …
"""


########################
#  POST et clés d'API  #
########################

"""
13. Envoyez en POST le relevé {"date": "2024-03-09", "station": 2,
    "temp": 6.5} et affichez le code de statut et l'identifiant attribué.

14. Appelez /api/prive sans clé, puis avec la clé lue dans la variable
    d'environnement METEO_API_KEY (définissez-la dans le programme avec
    os.environ.setdefault, pour l'exercice). Affichez les deux codes.
    Pourquoi ne faut-il pas écrire la clé dans le code ?
"""


############################
#  Sessions et pagination  #
############################

"""
15. Avec une Session qui envoie automatiquement la clé d'API et un
    User-Agent, appelez /api/prive puis /api/stations.

16. Récupérez TOUS les relevés de /api/releves en parcourant les pages
    (champ "page_suivante"), puis affichez leur nombre et la température
    moyenne, arrondie à 2 chiffres.

17. Réécrivez l'exercice 16 sous forme d'un générateur iter_releves(session)
    qui produit les relevés un par un (cf. chap. 36). Utilisez-le pour
    afficher la date du premier relevé à plus de 12 °C.
"""


#########################################
#  Respecter le serveur et télécharger  #
#########################################

"""
18. Écrivez une fonction avec_reessais(url, essais=3) qui fait la requête ;
    si la réponse est 429, elle attend (Retry-After secondes, mais au plus
    0.1 s pour l'exercice) puis réessaie, jusqu'à "essais" tentatives. Elle
    renvoie la réponse finale. Testez sur /api/quota (code final : 429) et
    sur /api/stations (200).

19. Lisez /robots.txt avec urllib.robotparser.RobotFileParser et dites si
    les URL /api/stations et /api/prive peuvent être visitées.

20. Téléchargez /releves.csv avec stream=True dans le fichier
    "exo49_releves.csv", affichez son nombre de lignes, puis supprimez-le.
"""


#######################
#  De l'API à pandas  #
#######################

"""
21. (pandas nécessaire) Construisez un DataFrame à partir de tous les
    relevés (exercice 16) et affichez la date la plus chaude et l'écart
    entre la température maximale et minimale.

22. (Internet nécessaire, facultatif) Avec l'API https://geo.api.gouv.fr/
    communes et les paramètres nom, fields et limit, affichez la population
    des 3 premières communes dont le nom contient "Saint-Malo". Prévoyez le
    cas où il n'y a pas de connexion (timeout court, except).
"""


###############
#  Nettoyage  #
###############

serveur.shutdown()
serveur.server_close()
