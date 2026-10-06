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
#  Chap. 49     #  Récupérer des données sur le Web : corrigés                 #
#               #                                                              #
################################################################################

"""
Ce corrigé nécessite requests (et pandas pour l'exercice 21) :
?> uv run --with requests --with pandas corrs/corr_49_requests.py
Sans requests, seuls les exercices 1 à 4 (bibliothèque standard) tournent.
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
1. 200 : succès (OK).
   201 : succès, ressource créée (après un POST).
   401 : erreur du client, authentification manquante ou invalide.
   404 : erreur du client, ressource introuvable.
   429 : erreur du client, trop de requêtes (il faut ralentir).
   500 : erreur du serveur, il a planté.
   503 : erreur du serveur, indisponible (maintenance, surcharge).
   La centaine suffit à classer un code : on utilise la division entière
   (cf. chap. 4).
"""


def categorie(code):
    """Classe un code de statut HTTP selon sa centaine."""
    centaine = code // 100
    if centaine == 2:
        return "succès"
    elif centaine == 3:
        return "redirection"
    elif centaine == 4:
        return "erreur client"
    elif centaine == 5:
        return "erreur serveur"
    return "inconnu"


for code in [200, 201, 301, 401, 404, 429, 500, 503]:
    print(code, categorie(code))
# => 200 succès
#    201 succès
#    301 redirection
#    401 erreur client
#    404 erreur client
#    429 erreur client
#    500 erreur serveur
#    503 erreur serveur

# 2. urlparse découpe l'URL ; parse_qs transforme la "query string" en
#    dictionnaire de LISTES (un paramètre peut apparaître plusieurs fois).
URL_EXO_2 = "https://api.exemple.org/v1/releves?station=12&debut=2024-03-01"
morceaux = urlparse(URL_EXO_2)
print(morceaux.scheme)          # => https
print(morceaux.netloc)          # => api.exemple.org
print(morceaux.path)            # => /v1/releves
print(parse_qs(morceaux.query))
# => {'station': ['12'], 'debut': ['2024-03-01']}

"""
3. true -> True, null -> None, et une chaîne JSON devient une str ; dans
   l'autre sens, None -> null et False -> false.
"""
d = json.loads('{"actif": true, "valeurs": [1, null], "nom": "A"}')
print(d["actif"], d["valeurs"], type(d["nom"]))
# => True [1, None] <class 'str'>
print(json.dumps({"x": None, "ok": False}))  # => {"x": null, "ok": false}


################################
#  urllib et première requête  #
################################

# 4. urlopen renvoie des octets : on les décode avant json.loads.
import urllib.request

with urllib.request.urlopen(BASE + "/api/stations", timeout=5) as rep:
    stations = json.loads(rep.read().decode("utf-8"))
for s in stations:
    print(s["nom"])
# => Lyon-Bron
#    Paris-Montsouris
#    Lyon-St-Exupéry

try:
    import requests
except ImportError:
    print("requests n'est pas installé ('uv add requests') : fin du corrigé.")
    serveur.shutdown()
    serveur.server_close()
    sys.exit(0)

# 5. Une compréhension avec condition (cf. chap. 23) :
stations = requests.get(BASE + "/api/stations", timeout=5).json()
print([s["nom"] for s in stations if s["altitude"] > 100])
# => ['Lyon-Bron', 'Lyon-St-Exupéry']

"""
6. Pour une 404, .ok vaut False et .status_code vaut 404. requests ne lève
   AUCUNE erreur : le serveur a bien répondu. C'est à nous de vérifier (ou
   d'appeler .raise_for_status()).
"""
rep = requests.get(BASE + "/rien", timeout=5)
print(rep.ok, rep.status_code)  # => False 404

# 7. Les en-têtes sont dans .headers ; le corps en texte dans .text.
rep = requests.get(BASE + "/releves.csv", timeout=5)
print(rep.headers["Content-Type"])     # => text/csv; charset=utf-8
print(rep.text.splitlines()[:2])       # => ['date,temp', '2024-03-01,8.5']


######################
#  Paramètres d'URL  #
######################

# 8.
rep = requests.get(BASE + "/api/stations", params={"ville": "Paris"},
                   timeout=5)
print(rep.url[rep.url.index("?"):])    # => ?ville=Paris
print(len(rep.json()))                 # => 1


# 9.
def stations_de(ville):
    """Renvoie les noms des stations d'une ville."""
    rep = requests.get(BASE + "/api/stations", params={"ville": ville},
                       timeout=5)
    rep.raise_for_status()
    return [s["nom"] for s in rep.json()]


print(stations_de("Lyon"))   # => ['Lyon-Bron', 'Lyon-St-Exupéry']
print(stations_de("Paris"))  # => ['Paris-Montsouris']
print(stations_de("Nice"))   # => []


########################
#  Timeout et erreurs  #
########################

# 10. /lent met 1 s : seuls les timeouts supérieurs à 1 s réussissent.
for limite in [0.2, 0.5, 3]:
    try:
        requests.get(BASE + "/lent", timeout=limite)
        print(f"timeout {limite} s : réussi")
    except requests.Timeout:
        print(f"timeout {limite} s : trop lent")
# => timeout 0.2 s : trop lent
#    timeout 0.5 s : trop lent
#    timeout 3 s : réussi


# 11. raise_for_status() transforme les codes 4xx/5xx en HTTPError, si bien
#     qu'un seul "except RequestException" attrape TOUS les cas.
def recuperer(url):
    """Renvoie le JSON de l'URL, ou None (en affichant l'erreur)."""
    try:
        rep = requests.get(url, timeout=2)
        rep.raise_for_status()
        return rep.json()
    except requests.RequestException as err:
        print("Erreur :", type(err).__name__)
        return None


print(len(recuperer(BASE + "/api/stations")))  # => 3
print(recuperer(BASE + "/rien"))
# => Erreur : HTTPError
#    None
print(recuperer("http://127.0.0.1:9/"))
# => Erreur : ConnectionError
#    None

"""
12. Du plus PRÉCIS au plus GÉNÉRAL : Timeout et HTTPError d'abord (dans
    n'importe quel ordre entre eux), RequestException en dernier. Python
    teste les "except" dans l'ordre et s'arrête au premier qui correspond ;
    or Timeout et HTTPError sont des sous-classes de RequestException
    (cf. chap. 26 et 35) : placé en premier, RequestException attraperait
    tout, et les deux autres ne serviraient jamais.
"""
print(issubclass(requests.Timeout, requests.RequestException))    # => True
print(issubclass(requests.HTTPError, requests.RequestException))  # => True


########################
#  POST et clés d'API  #
########################

# 13. json=… convertit le dictionnaire en JSON et règle l'en-tête.
rep = requests.post(BASE + "/api/releves",
                    json={"date": "2024-03-09", "station": 2, "temp": 6.5},
                    timeout=5)
print(rep.status_code, rep.json()["id"])  # => 201 8

# 14.
print(requests.get(BASE + "/api/prive", timeout=5).status_code)  # => 401
os.environ.setdefault("METEO_API_KEY", "demo-123")  # pour l'exercice
cle = os.environ["METEO_API_KEY"]
rep = requests.get(BASE + "/api/prive", headers={"X-API-Key": cle},
                   timeout=5)
print(rep.status_code)  # => 200
"""
Une clé écrite dans le code finit dans git, puis souvent sur GitHub, où des
robots la récupèrent en quelques minutes : quelqu'un pourrait alors utiliser
(et épuiser, voire faire payer) votre compte. La variable d'environnement
reste sur VOTRE machine.
"""


############################
#  Sessions et pagination  #
############################

# 15. Les en-têtes de session.headers sont envoyés à CHAQUE requête.
with requests.Session() as session:
    session.headers.update({"X-API-Key": cle,
                            "User-Agent": "exercices-python/1.0"})
    print(session.get(BASE + "/api/prive", timeout=5).json())
    print(len(session.get(BASE + "/api/stations", timeout=5).json()))
# => {'message': 'Bienvenue !'}
#    3


# 16. On boucle tant qu'il y a une page suivante (None sur la dernière).
def tous_les_releves(session):
    releves = []
    page = 1
    while page is not None:
        contenu = session.get(BASE + "/api/releves", params={"page": page},
                              timeout=5).json()
        releves.extend(contenu["resultats"])
        page = contenu["page_suivante"]
    return releves


with requests.Session() as session:
    releves = tous_les_releves(session)
temperatures = [r["temp"] for r in releves]
print(len(releves), round(sum(temperatures) / len(temperatures), 2))
# => 7 10.29


# 17. "yield from" produit un à un les relevés de chaque page (cf. chap. 36).
def iter_releves(session):
    page = 1
    while page is not None:
        contenu = session.get(BASE + "/api/releves", params={"page": page},
                              timeout=5).json()
        yield from contenu["resultats"]
        page = contenu["page_suivante"]


with requests.Session() as session:
    premier_chaud = next(r for r in iter_releves(session) if r["temp"] > 12)
print(premier_chaud["date"])  # => 2024-03-03
# Avantage : next() s'arrête au premier relevé trouvé ; les pages suivantes
# ne sont même pas téléchargées (ici, une seule page a suffi).


#########################################
#  Respecter le serveur et télécharger  #
#########################################

# 18.
def avec_reessais(url, essais=3):
    """Réessaie après un 429, en respectant (à peu près) Retry-After."""
    for tentative in range(1, essais + 1):
        rep = requests.get(url, timeout=5)
        if rep.status_code != 429:
            return rep
        attente = float(rep.headers.get("Retry-After", 1))
        print(f"tentative {tentative} : 429, on attend")
        time.sleep(min(attente, 0.1))  # plafonné à 0.1 s pour l'exercice
    return rep


print(avec_reessais(BASE + "/api/quota").status_code)
# => tentative 1 : 429, on attend
#    tentative 2 : 429, on attend
#    tentative 3 : 429, on attend
#    429
print(avec_reessais(BASE + "/api/stations").status_code)  # => 200

# 19.
from urllib.robotparser import RobotFileParser

robots = RobotFileParser()
robots.parse(requests.get(BASE + "/robots.txt", timeout=5).text.splitlines())
for chemin in ["/api/stations", "/api/prive"]:
    print(chemin, robots.can_fetch("*", BASE + chemin))
# => /api/stations True
#    /api/prive False

# 20. Mode "wb" : on écrit des octets (cf. chap. 28).
with requests.get(BASE + "/releves.csv", stream=True, timeout=5) as rep:
    rep.raise_for_status()
    with open("exo49_releves.csv", "wb") as f:
        for morceau in rep.iter_content(chunk_size=1024):
            f.write(morceau)
with open("exo49_releves.csv", encoding="utf-8") as f:
    print(len(f.readlines()))  # => 4 (l'en-tête + 3 relevés)
os.remove("exo49_releves.csv")


#######################
#  De l'API à pandas  #
#######################

# 21.
try:
    import pandas as pd
except ImportError:
    print("(pandas n'est pas installé : exercice 21 sauté)")
else:
    df = pd.DataFrame(releves)
    print(df.loc[df["temp"].idxmax(), "date"])     # => 2024-03-07
    print(df["temp"].max() - df["temp"].min())     # => 6.0

# 22. Résultat VARIABLE (données mises à jour) ; sans réseau, un message.
try:
    rep = requests.get("https://geo.api.gouv.fr/communes",
                       params={"nom": "Saint-Malo",
                               "fields": "nom,population", "limit": 3},
                       timeout=5)
    rep.raise_for_status()
    for commune in rep.json():
        print(commune["nom"], commune.get("population"))
    # => Saint-Malo 47000 (environ, VARIE)
    #    …
except requests.RequestException as err:
    print("(pas d'accès à Internet :", type(err).__name__, ")")


###############
#  Nettoyage  #
###############

serveur.shutdown()
serveur.server_close()
