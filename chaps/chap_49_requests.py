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
#  Chap. 49     #  Récupérer des données sur le Web : requests                 #
#               #                                                              #
################################################################################
#
#  - Le Web en bref : client, serveur, HTTP
#  - JSON, le format des API
#  - Un serveur de démonstration
#  - La bibliothèque standard : urllib.request
#  - Installer et importer requests
#  - Une requête GET
#  - La réponse : statut, en-têtes, contenu
#  - Paramètres d'URL
#  - Toujours un timeout
#  - Gérer les erreurs
#  - Envoyer des données : POST
#  - En-têtes et clés d'API
#  - Les sessions
#  - La pagination
#  - Respecter le serveur : limites et robots.txt
#  - Télécharger un fichier
#  - De l'API à pandas
#  - Une vraie API publique
#  - Pour aller plus loin : scraping et httpx
#  - Arrêter le serveur
#
##############################

# Le Web en bref : client, serveur, HTTP
#########################################

"""
Beaucoup de données ne sont pas dans des fichiers, mais sur le Web : météo,
cours de la bourse, données publiques (data.gouv.fr), réseaux sociaux… On les
récupère en interrogeant une API ("Application Programming Interface") : un
site Web destiné non pas à des humains, mais à des programmes.

Le vocabulaire :
    - le CLIENT envoie une REQUÊTE (votre navigateur, ou votre programme) ;
    - le SERVEUR la reçoit et renvoie une RÉPONSE ;
    - ils communiquent avec le protocole HTTP (ou HTTPS, sa version chiffrée).

Une URL se décompose ainsi :

    https://geo.api.gouv.fr/communes?nom=Lyon&fields=population
    └─┬─┘   └──────┬──────┘└───┬───┘└────────────┬────────────┘
    schéma       hôte       chemin     paramètres ("query string")

Une requête HTTP contient :
    - une MÉTHODE : GET (lire, la plus courante), POST (envoyer/créer),
      PUT/PATCH (modifier), DELETE (supprimer) ;
    - une URL ;
    - des EN-TÊTES ("headers") : des couples clé/valeur d'informations
      (langue, format accepté, clé d'API…) ;
    - parfois un CORPS ("body") : les données envoyées (avec POST).

La réponse contient un CODE DE STATUT, des en-têtes et un corps. Les codes à
connaître (IMPT) :
    200 OK                    tout va bien
    201 Created               ressource créée (après un POST)
    301/302                   redirection
    400 Bad Request           requête mal formée (votre faute)
    401 Unauthorized          authentification nécessaire ou invalide
    403 Forbidden             accès interdit
    404 Not Found             la ressource n'existe pas
    429 Too Many Requests     trop de requêtes : ralentissez !
    500 Internal Server Error le serveur a planté (sa faute)
    503 Service Unavailable   serveur indisponible (maintenance, surcharge)
En résumé : 2xx = succès, 3xx = redirection, 4xx = erreur du client,
5xx = erreur du serveur.
"""


# JSON, le format des API
##########################

"""
La plupart des API répondent en JSON ("JavaScript Object Notation"), un format
texte qui ressemble énormément aux dictionnaires et listes de Python (cf.
chap. 27 et 28). Le module json de la bibliothèque standard convertit dans les
deux sens :
    - json.loads(texte) : texte JSON -> objet Python ("load string") ;
    - json.dumps(objet) : objet Python -> texte JSON ("dump string").
"""
import json

texte = '{"ville": "Lyon", "temperatures": [12.5, 14.0], "pluie": false}'
donnees = json.loads(texte)
print(type(donnees))              # => <class 'dict'>
print(donnees["temperatures"][1])  # => 14.0
print(donnees["pluie"])           # => False (false en JSON, False en Python)
print(json.dumps({"ok": True, "valeur": None}))
# => {"ok": true, "valeur": null}

"""
Correspondances : objet {} <-> dict, tableau [] <-> list, chaîne <-> str,
nombre <-> int/float, true/false <-> True/False, null <-> None.
"""


# Un serveur de démonstration
##############################

"""
Pour que ce chapitre fonctionne SANS connexion Internet, et donne toujours le
même résultat, on démarre ici notre propre petit serveur Web, sur votre
ordinateur (adresse 127.0.0.1, dite "localhost"). Il simule une API de
relevés météo.

Vous n'avez PAS besoin de comprendre ce code en détail : retenez seulement
qu'il tourne en parallèle du programme (dans un "thread"), et qu'il répond
aux URL suivantes :
    GET  /api/stations              liste des stations (filtre ?ville=…)
    GET  /api/releves?page=N        relevés, par pages de 3
    POST /api/releves               ajoute un relevé (renvoie 201)
    GET  /api/prive                 exige l'en-tête X-API-Key
    GET  /api/quota                 répond toujours 429 (trop de requêtes)
    GET  /lent                      met 1 seconde à répondre
    GET  /releves.csv               un fichier CSV
    GET  /robots.txt                les règles pour les robots
    tout le reste                   404
"""
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
print("Serveur de démonstration démarré")  # => Serveur de démonstration démarré

# Si votre ordinateur passe par un proxy, on lui demande d'ignorer localhost :
os.environ["NO_PROXY"] = "127.0.0.1,localhost"


# La bibliothèque standard : urllib.request
############################################

"""
Python sait faire des requêtes HTTP sans rien installer, avec le module
urllib.request. Mais son interface est verbeuse : il faut décoder les octets
soi-même, construire les paramètres à la main, et les erreurs HTTP sont des
exceptions qu'il faut toujours intercepter.
"""
import urllib.error
import urllib.request

with urllib.request.urlopen(BASE + "/api/stations", timeout=5) as rep:
    print(rep.status)                        # => 200
    octets = rep.read()                      # le corps, en octets (bytes)
    stations = json.loads(octets.decode("utf-8"))
print(stations[0]["nom"])                    # => Lyon-Bron

try:
    urllib.request.urlopen(BASE + "/n-existe-pas", timeout=5)
except urllib.error.HTTPError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 1: (Sans ce try: … except …, cette ligne créerait : HTTP Error 404: Not
#    Found)

"""
C'est suffisant pour un petit script sans dépendance. Pour tout le reste, on
utilise requests, de loin la bibliothèque HTTP la plus utilisée en Python.
"""


# Installer et importer requests
#################################

"""
requests n'est pas dans la bibliothèque standard. Avec uv (cf. chap. 47) :
    ?> uv add requests                       # dans un projet
    ?> uv run --with requests chap_49_requests.py   # essai ponctuel
(ou, à l'ancienne : python3 -m pip install requests)
"""
try:
    import requests
except ImportError:
    print("requests n'est pas installé : tapez 'uv add requests' ou lancez "
          "'uv run --with requests chap_49_requests.py'. Fin du chapitre.")
    serveur.shutdown()
    serveur.server_close()
    sys.exit(0)


# Une requête GET
##################

"""
Une seule ligne suffit : requests.get(url) envoie la requête, attend la
réponse et la renvoie sous forme d'un objet Response.
"""
reponse = requests.get(BASE + "/api/stations", timeout=5)
print(type(reponse))         # => <class 'requests.models.Response'>
print(reponse)               # => <Response [200]>
print(reponse.status_code)   # => 200

stations = reponse.json()    # décode directement le JSON du corps
print(type(stations))        # => <class 'list'>
print(len(stations))         # => 3
for s in stations:
    print(f"{s['nom']:18} {s['altitude']:>4} m")
# => Lyon-Bron           200 m
#    Paris-Montsouris     75 m
#    Lyon-St-Exupéry     235 m


# La réponse : statut, en-têtes, contenu
#########################################

"""
L'objet Response contient tout ce que le serveur a renvoyé :
    .status_code  le code de statut (int)
    .ok           True si le code est < 400
    .reason       le texte du statut ("OK", "Not Found"…)
    .headers      les en-têtes (un dictionnaire, insensible à la casse)
    .text         le corps, décodé en str
    .content      le corps, en octets (bytes : pour les images, les zip…)
    .json()       le corps, décodé depuis le JSON
    .url          l'URL finale (après paramètres et redirections)
    .elapsed      le temps de réponse
"""
print(reponse.ok)                          # => True
print(reponse.reason)                      # => OK
print(reponse.headers["Content-Type"])     # => application/json; charset=utf-8
print(reponse.headers["content-type"])     # => application/json; charset=utf-8
# (la casse des noms d'en-têtes n'a pas d'importance)
print(reponse.text[:28])                   # => [{"id": 1, "nom": "Lyon-Bron"

introuvable = requests.get(BASE + "/n-existe-pas", timeout=5)
print(introuvable.status_code, introuvable.ok)  # => 404 False
print(introuvable.json())                  # => {'erreur': 'introuvable'}

"""
IMPT : contrairement à urllib, requests ne lève PAS d'erreur pour un code
4xx ou 5xx : la requête a "réussi" techniquement, le serveur a répondu. C'est
à vous de vérifier le statut (cf. "Gérer les erreurs").

Attention aussi : .json() ne marche que si le corps est bien du JSON.
"""
csv_brut = requests.get(BASE + "/releves.csv", timeout=5)
try:
    csv_brut.json()
except requests.JSONDecodeError as err:  # requests 2.27+
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")
# => 2: (Sans ce try: … except …, cette ligne créerait : Expecting value:
#    line 1 column 1 (char 0))


# Paramètres d'URL
###################

"""
Pour filtrer, trier ou paginer, une API attend des paramètres dans l'URL
("?ville=Lyon&tri=nom"). Plutôt que de les coller à la main (et de gérer les
espaces, accents et caractères spéciaux), on passe un dictionnaire à params :
requests construit et encode l'URL tout seul.
"""
reponse = requests.get(BASE + "/api/stations", params={"ville": "Lyon"},
                       timeout=5)
print(reponse.url.split("/", 3)[3])         # => api/stations?ville=Lyon
print([s["nom"] for s in reponse.json()])  # => ['Lyon-Bron', 'Lyon-St-Exupéry']

# Les caractères spéciaux sont encodés automatiquement ("%20" pour l'espace) :
reponse = requests.get(BASE + "/api/stations",
                       params={"ville": "Saint Étienne"}, timeout=5)
print(reponse.url.split("?")[1])  # => ville=Saint+%C3%89tienne
print(reponse.json())             # => [] (aucune station dans cette ville)


# Toujours un timeout
######################

"""
IMPT : par défaut, requests attend une réponse INDÉFINIMENT. Si le serveur ne
répond pas, votre programme reste bloqué pour toujours. Passez TOUJOURS un
timeout (en secondes) : au-delà, requests lève une erreur Timeout.

Notre route /lent met 1 seconde à répondre :
"""
reponse = requests.get(BASE + "/lent", timeout=5)
print(reponse.json())  # => {'message': 'enfin !'}

try:
    requests.get(BASE + "/lent", timeout=0.2)
except requests.Timeout as err:
    print("3: (Sans ce try: … except …, cette ligne créerait : Timeout)")
# => 3: (Sans ce try: … except …, cette ligne créerait : Timeout)

"""
Valeurs raisonnables : 5 à 30 secondes selon l'API. On peut aussi séparer le
temps de connexion et le temps de lecture : timeout=(3, 30).
"""


# Gérer les erreurs
####################

"""
Trois familles d'erreurs, toutes filles de requests.RequestException
(cf. la hiérarchie des exceptions, chap. 26 et 35) :
    - requests.ConnectionError : impossible de joindre le serveur (pas de
      réseau, mauvaise adresse, serveur éteint) ;
    - requests.Timeout : le serveur a mis trop de temps ;
    - requests.HTTPError : le serveur a répondu avec un code 4xx/5xx, levée
      SEULEMENT si l'on appelle .raise_for_status().

Pour simuler un serveur éteint, on demande un port libre puis on le referme
aussitôt : personne n'écoute plus à cette adresse.
"""
with socket.socket() as s:
    s.bind(("127.0.0.1", 0))
    port_ferme = s.getsockname()[1]

try:
    requests.get(f"http://127.0.0.1:{port_ferme}/", timeout=5)
except requests.ConnectionError:
    print("4: (Sans ce try: … except …, cette ligne créerait : "
          "ConnectionError)")
# => 4: (Sans ce try: … except …, cette ligne créerait : ConnectionError)

# raise_for_status() transforme un code 4xx/5xx en exception :
try:
    requests.get(BASE + "/n-existe-pas", timeout=5).raise_for_status()
except requests.HTTPError as err:
    print(f"5: (Sans ce try: … except …, cette ligne créerait : "
          f"{str(err).split(' for url')[0]})")
# => 5: (Sans ce try: … except …, cette ligne créerait : 404 Client Error:
#    Not Found)

"""
Le schéma à retenir (IMPT) : une fonction qui récupère des données, vérifie
le statut, et gère toutes les erreurs réseau au même endroit.
"""


def recuperer_json(url, **kwargs):
    """Retourne le JSON de l'URL, ou None en cas de problème (cf. chap. 32
    pour **kwargs : on transmet params, headers… tels quels à requests)."""
    try:
        rep = requests.get(url, timeout=5, **kwargs)
        rep.raise_for_status()
        return rep.json()
    except requests.RequestException as err:
        print("Problème réseau :", type(err).__name__)
        return None


print(recuperer_json(BASE + "/api/stations", params={"ville": "Paris"}))
# => [{'id': 2, 'nom': 'Paris-Montsouris', 'ville': 'Paris', 'altitude': 75}]
print(recuperer_json(BASE + "/n-existe-pas"))
# => Problème réseau : HTTPError
#    None


# Envoyer des données : POST
#############################

"""
Pour ENVOYER des données (créer un relevé, poster un formulaire), on utilise
requests.post. Avec json=…, requests convertit le dictionnaire en JSON et
ajoute l'en-tête Content-Type: application/json.
(Pour un formulaire HTML classique, on utiliserait data=… à la place.)
"""
nouveau = {"date": "2024-03-08", "station": 1, "temp": 14.5}
reponse = requests.post(BASE + "/api/releves", json=nouveau, timeout=5)
print(reponse.status_code)  # => 201 (Created)
print(reponse.json())
# => {'date': '2024-03-08', 'station': 1, 'temp': 14.5, 'id': 8}
# (le serveur a renvoyé le relevé, complété de son identifiant)


# En-têtes et clés d'API
#########################

"""
Beaucoup d'API demandent une CLÉ d'API (un mot de passe propre à votre
programme), pour savoir qui les appelle et limiter les abus. Elle se passe
généralement dans un en-tête, avec headers=… (le nom exact de l'en-tête
dépend de l'API : "Authorization: Bearer …", "X-API-Key: …"…).
"""
reponse = requests.get(BASE + "/api/prive", timeout=5)
print(reponse.status_code, reponse.json())
# => 401 {'erreur': "clé d'API manquante"}

"""
IMPT : ne JAMAIS écrire une clé d'API dans le code ! Le code finit dans git,
puis sur GitHub, et la clé est volée en quelques minutes (des robots
scannent GitHub en permanence). On la range dans une VARIABLE D'ENVIRONNEMENT,
définie hors du code :
    ?> export METEO_API_KEY="…"      # Linux / macOS (ou dans un fichier .env
                                      #   jamais commité, cf. .gitignore)
et on la lit avec os.environ (cf. chap. 22) :
"""
os.environ.setdefault("METEO_API_KEY", CLE_SECRETE)  # pour la démo seulement
cle = os.environ.get("METEO_API_KEY")
reponse = requests.get(BASE + "/api/prive", headers={"X-API-Key": cle},
                       timeout=5)
print(reponse.status_code, reponse.json())  # => 200 {'message': 'Bienvenue !'}

# Un en-tête que l'on envoie souvent : User-Agent, pour se présenter poliment.
entetes = {"User-Agent": "cours-python-ds/1.0 (contact@example.org)"}


# Les sessions
###############

"""
Quand on fait beaucoup de requêtes vers la même API, on crée une Session :
    - elle garde les en-têtes communs (la clé d'API, le User-Agent) : on ne
      les répète plus à chaque appel ;
    - elle réutilise la même connexion réseau : c'est nettement plus rapide ;
    - elle conserve les cookies (pour les sites où l'on se connecte).
On l'utilise avec "with", pour qu'elle soit fermée à la fin (cf. chap. 28).
"""
with requests.Session() as session:
    session.headers.update({"X-API-Key": cle, **entetes})
    privee = session.get(BASE + "/api/prive", timeout=5)
    lyon = session.get(BASE + "/api/stations", params={"ville": "Lyon"},
                       timeout=5)
print(privee.json()["message"], len(lyon.json()))  # => Bienvenue ! 2


# La pagination
################

"""
Une API ne renvoie jamais des millions de lignes d'un coup : elle découpe les
résultats en PAGES. Il faut alors boucler, page après page, jusqu'à la
dernière. Chaque API indique la page suivante à sa manière (un numéro, une
URL "next", un "curseur"…) : lisez sa documentation.

Notre API renvoie 3 relevés par page, et un champ "page_suivante" qui vaut
None (null) sur la dernière page.
"""
premiere = requests.get(BASE + "/api/releves", timeout=5).json()
print(premiere["page"], premiere["page_suivante"], len(premiere["resultats"]))
# => 1 2 3


def tous_les_releves(session):
    """Parcourt toutes les pages et renvoie la liste complète des relevés."""
    releves = []
    page = 1
    while page is not None:  # cf. chap. 13
        rep = session.get(BASE + "/api/releves", params={"page": page},
                          timeout=5)
        rep.raise_for_status()
        contenu = rep.json()
        releves.extend(contenu["resultats"])
        page = contenu["page_suivante"]
        time.sleep(0.05)  # on laisse respirer le serveur (section suivante)
    return releves


with requests.Session() as session:
    releves = tous_les_releves(session)
print(len(releves))                     # => 7
print(releves[-1])  # => {'date': '2024-03-07', 'station': 1, 'temp': 13.5}

"""
Variante élégante : un générateur qui produit les relevés au fur et à mesure,
page par page, sans tout garder en mémoire (cf. chap. 36).
"""


# Respecter le serveur : limites et robots.txt
###############################################

"""
Une API est un service partagé. Règles de politesse (et de survie) :
    - lisez les conditions d'utilisation et les LIMITES ("rate limits") :
      par exemple 10 requêtes par seconde, ou 1 000 par jour ;
    - espacez vos requêtes avec time.sleep() dans les boucles ;
    - si le serveur répond 429 (Too Many Requests), attendez avant de
      réessayer : l'en-tête Retry-After indique souvent combien de secondes ;
    - ne retéléchargez pas mille fois la même chose : enregistrez les
      résultats dans un fichier (cf. chap. 28).
"""
reponse = requests.get(BASE + "/api/quota", timeout=5)
print(reponse.status_code)                 # => 429
attente = int(reponse.headers.get("Retry-After", "5"))
print(f"On attend {attente} s avant de réessayer")  # => On attend 1 s avant…

"""
Pour les SITES Web (pas les API), le fichier /robots.txt indique ce que les
robots ont le droit de visiter. La bibliothèque standard sait le lire :
"""
from urllib.robotparser import RobotFileParser

robots = RobotFileParser()
robots.parse(requests.get(BASE + "/robots.txt", timeout=5).text.splitlines())
print(robots.can_fetch("*", BASE + "/api/stations"))  # => True
print(robots.can_fetch("*", BASE + "/api/prive"))     # => False


# Télécharger un fichier
#########################

"""
Pour un fichier (CSV, image, zip…), on écrit .content (des octets) dans un
fichier ouvert en mode binaire "wb" (cf. chap. 28).

Pour un GROS fichier, on ajoute stream=True : requests ne charge pas tout en
mémoire, et l'on écrit le fichier morceau par morceau avec iter_content().
"""
nom_fichier = "chap49_releves.csv"
with requests.get(BASE + "/releves.csv", stream=True, timeout=5) as rep:
    rep.raise_for_status()
    with open(nom_fichier, "wb") as f:
        for morceau in rep.iter_content(chunk_size=8192):  # 8 Ko à la fois
            f.write(morceau)

with open(nom_fichier, encoding="utf-8") as f:
    print(f.readline().strip())  # => date,temp
print(os.path.getsize(nom_fichier), "octets")  # => 57 octets


# De l'API à pandas
####################

"""
Une liste de dictionnaires JSON se convertit directement en DataFrame
(cf. chap. 39) : chaque dictionnaire devient une ligne, chaque clé une
colonne. C'est le chemin classique API -> pandas -> analyse.
"""
try:
    import pandas as pd
except ImportError:
    print("(pandas n'est pas installé : 'uv add pandas'. Section sautée.)")
else:
    df = pd.DataFrame(releves)
    print(df.shape)                        # => (7, 3)
    print(df["temp"].mean())               # => 10.285714285714286
    print(df.loc[df["temp"].idxmax(), "date"])  # => 2024-03-07

    # Et le CSV téléchargé se lit directement… ou même depuis l'URL !
    df_csv = pd.read_csv(BASE + "/releves.csv")
    print(df_csv["temp"].tolist())         # => [8.5, 10.0, 12.5]

    # Pour du JSON imbriqué (dictionnaires dans des dictionnaires),
    # pd.json_normalize aplatit les niveaux en colonnes "a.b" :
    imbrique = [{"station": {"nom": "Bron", "alt": 200}, "temp": 8.5}]
    print(pd.json_normalize(imbrique).columns.tolist())
    # => ['temp', 'station.nom', 'station.alt']

os.remove(nom_fichier)  # on supprime le fichier téléchargé


# Une vraie API publique
#########################

"""
Tout ce qui précède s'applique tel quel aux vraies API. Exemple avec l'API
Géo du gouvernement français (gratuite, sans clé) :
https://geo.api.gouv.fr/decoupage-administratif/communes

Ce bloc nécessite Internet : sans connexion, il affiche simplement un
message. Les chiffres VARIENT (mise à jour des données de population).
"""
try:
    rep = requests.get("https://geo.api.gouv.fr/communes",
                       params={"nom": "Lyon", "fields": "nom,population",
                               "limit": 3},
                       headers=entetes, timeout=5)
    rep.raise_for_status()
    for commune in rep.json():
        print(f"{commune['nom']:15} {commune.get('population', '?'):>8}")
    # => Lyon              519127   (VARIE)
    #    …
except requests.RequestException as err:
    print("(pas d'accès à Internet : exemple sauté -", type(err).__name__, ")")

"""
D'autres API publiques pour s'entraîner : api.github.com (dépôts GitHub),
data.gouv.fr (des milliers de jeux de données), open-meteo.com (météo, sans
clé), api-adresse.data.gouv.fr (géocodage d'adresses).
"""


# Pour aller plus loin : scraping et httpx
###########################################

"""
Le SCRAPING consiste à extraire des données de pages Web faites pour les
humains (du HTML), quand il n'existe pas d'API. On télécharge la page avec
requests, puis on l'analyse avec BeautifulSoup ("uv add beautifulsoup4") :

    from bs4 import BeautifulSoup
    page = requests.get(url, headers=entetes, timeout=10)
    soupe = BeautifulSoup(page.text, "html.parser")
    titres = [h2.get_text() for h2 in soupe.find_all("h2")]

Le scraping doit rester ÉTHIQUE et légal :
    - préférez toujours une API ou un jeu de données officiel s'il existe ;
    - respectez robots.txt et les conditions d'utilisation du site ;
    - limitez votre rythme (time.sleep) et identifiez-vous (User-Agent) ;
    - attention aux données personnelles (RGPD) et au droit d'auteur.

httpx ("uv add httpx") est une alternative moderne à requests, avec presque
la même interface (httpx.get, httpx.Client…), qui gère en plus HTTP/2 et la
programmation asynchrone (async/await) pour lancer des centaines de requêtes
en parallèle.
"""


# Arrêter le serveur
#####################

"""
On arrête proprement notre serveur de démonstration : shutdown() stoppe la
boucle serve_forever(), server_close() libère le port.
"""
serveur.shutdown()
serveur.server_close()
print("Serveur arrêté")  # => Serveur arrêté
