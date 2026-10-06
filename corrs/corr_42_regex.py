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
#  Chap. 42     #  Expressions régulières : corrigés                           #
#               #                                                              #
################################################################################

import re
from collections import Counter


##################################
#  Chaînes brutes et recherches  #
##################################

r"""
1. Sans exécuter, que valent len("\t") et len(r"\t") ? Pourquoi faut-il
   écrire les regex en chaîne brute ?
"""
print(len("\t"))    # => 1 : "\t" est UN caractère, la tabulation
print(len(r"\t"))   # => 2 : dans une chaîne brute, "\" et "t" sont gardés
r"""
Les regex utilisent beaucoup l'antislash (\d, \w, \b…). Sans le r, Python
interprète certains de ces antislashs AVANT de transmettre le motif au module
re : "\b" devient le caractère "retour arrière", et la regex ne trouve plus
rien, sans aucune erreur. Avec r"…", le motif arrive intact.
"""

r"""
2. Sans exécuter, que renvoient ces trois appels (un objet Match ou None) ?
"""
print(re.search(r"\d+", "Tome 3"))
# => <re.Match object; span=(5, 6), match='3'>
print(re.match(r"\d+", "Tome 3"))      # => None
print(re.fullmatch(r"\d+", "Tome 3"))  # => None
r"""
    - search trouve "3" n'importe où dans la chaîne ;
    - match exige que la chaîne COMMENCE par le motif : "T" n'est pas un
      chiffre, donc None ;
    - fullmatch exige que TOUTE la chaîne corresponde : None aussi.
"""

r"""
3. Écrivez une fonction contient_chiffre(texte) qui renvoie True si le texte
   contient au moins un chiffre, False sinon (avec re.search).
"""
def contient_chiffre(texte):
    return re.search(r"\d", texte) is not None

print(contient_chiffre("R2D2"))    # => True
print(contient_chiffre("Python"))  # => False
r"""
re.search renvoie un Match ou None : "is not None" le transforme en booléen.
On aurait aussi pu écrire bool(re.search(r"\d", texte)).
Un seul chiffre suffit : inutile d'écrire \d+.
"""

r"""
4. Avec re.search et les méthodes de l'objet Match, affichez le premier
   nombre trouvé dans "Température : 23 degrés, humidité : 60 %", puis sa
   position (début et fin).
"""
m = re.search(r"\d+", "Température : 23 degrés, humidité : 60 %")
if m:
    print(m.group())              # => 23
    print(m.start(), m.end())     # => 14 16
r"""
search s'arrête au PREMIER résultat : 60 n'est pas trouvé. Le if protège
contre le cas où il n'y aurait aucun nombre (m vaudrait None, et m.group()
lèverait une AttributeError).
"""


################################
#  Classes et quantificateurs  #
################################

r"""
5. Sans exécuter, que renvoient ces appels ?
"""
print(re.findall(r"[aeiou]", "regex"))         # => ['e', 'e']
print(re.findall(r"\d{2}", "12345"))           # => ['12', '34']
print(re.findall(r"\w+", "Bonjour, l'été !"))  # => ['Bonjour', 'l', 'été']
print(re.findall(r"[^a-z ]", "abc 123 déf"))   # => ['1', '2', '3', 'é']
r"""
    - \d{2} prend les chiffres deux par deux, sans chevauchement : "5", resté
      seul, n'est pas pris ;
    - \w+ s'arrête sur l'apostrophe (qui n'est pas un caractère de mot), mais
      reconnaît les lettres accentuées ;
    - [^a-z ] : tout ce qui n'est ni une lettre de a à z, ni un espace. "é"
      n'est pas dans l'intervalle a-z, il est donc pris.
"""

r"""
6. Écrivez une fonction est_code_postal(texte) qui renvoie True si le texte
   est EXACTEMENT un code postal français de 5 chiffres.
"""
def est_code_postal(texte):
    return re.fullmatch(r"\d{5}", texte) is not None

print(est_code_postal("75011"))   # => True
print(est_code_postal("7501"))    # => False
print(est_code_postal("75011 "))  # => False : l'espace final est refusé
r"""
Pour VALIDER un format, on utilise fullmatch : avec search, "a75011b"
serait accepté, car il CONTIENT 5 chiffres.
"""

r"""
7. Écrivez une regex qui valide une plaque d'immatriculation française au
   format "AB-123-CD".
"""
PLAQUE = r"[A-Z]{2}-\d{3}-[A-Z]{2}"
print(bool(re.fullmatch(PLAQUE, "AB-123-CD")))    # => True
print(bool(re.fullmatch(PLAQUE, "ab-123-cd")))    # => False : minuscules
print(bool(re.fullmatch(PLAQUE, "AB-1234-CD")))   # => False : 4 chiffres
r"""
Le tiret, hors des crochets, n'a pas de sens spécial : pas besoin de
l'échapper.
"""

r"""
8. Sans exécuter, que renvoient ces deux appels ? Expliquez la différence.
"""
print(re.findall(r"\(.+\)", "f(x) + g(y)"))    # => ['(x) + g(y)']
print(re.findall(r"\(.+?\)", "f(x) + g(y)"))   # => ['(x)', '(y)']
r"""
Les parenthèses sont échappées : \( et \) sont de vraies parenthèses.
    - ".+" est GOURMAND : il va le plus loin possible, jusqu'à la DERNIÈRE
      parenthèse fermante ;
    - ".+?" est PARESSEUX : il s'arrête à la PREMIÈRE parenthèse fermante.
Une alternative claire : r"\([^)]+\)".
"""


############################
#  findall et les groupes  #
############################

r"""
9. Extrayez tous les nombres (entiers ou décimaux avec un point, éventuellement
   négatifs) de la chaîne "Solde : -12.5 €, puis +30 €, puis 7.25 €", et
   calculez leur somme.
"""
solde = "Solde : -12.5 €, puis +30 €, puis 7.25 €"
nombres = re.findall(r"[-+]?\d+(?:\.\d+)?", solde)
print(nombres)                          # => ['-12.5', '+30', '7.25']
print(sum(float(n) for n in nombres))   # => 24.75
r"""
    [-+]?        un signe, optionnel
    \d+          la partie entière
    (?:\.\d+)?   une partie décimale optionnelle. Le groupe est NON capturant
                 (?:…) : avec un groupe capturant, findall renverrait seulement
                 le contenu du groupe (".5", "", ".25") !
float() accepte le "+" : float("+30") vaut 30.0.
"""

r"""
10. Avec un seul re.findall et des groupes, transformez
        "Ada:36, Alan:41, Grace:85"
    en une liste de tuples, puis en un dictionnaire (âges en int).
"""
couples = re.findall(r"(\w+):(\d+)", "Ada:36, Alan:41, Grace:85")
print(couples)   # => [('Ada', '36'), ('Alan', '41'), ('Grace', '85')]
ages = {nom: int(age) for nom, age in couples}
print(ages)      # => {'Ada': 36, 'Alan': 41, 'Grace': 85}
r"""
Avec DEUX groupes, findall renvoie une liste de tuples (un élément par
groupe). La compréhension de dictionnaire (cf. chap. 23) déballe chaque
tuple en (nom, age).
"""

r"""
11. Avec des groupes NOMMÉS, analysez l'heure "14h05" et affichez le
    dictionnaire renvoyé par .groupdict().
"""
m = re.fullmatch(r"(?P<heures>\d{1,2})h(?P<minutes>\d{2})", "14h05")
print(m.groupdict())   # => {'heures': '14', 'minutes': '05'}
print(int(m.group("heures")) * 60 + int(m.group("minutes")))  # => 845
r"""
\d{1,2} accepte aussi "9h30". Les valeurs sont des strings : on les convertit
pour calculer (ici, le nombre de minutes depuis minuit).
"""

r"""
12. Avec re.finditer, affichez chaque mot de plus de 6 lettres de la phrase
    suivi de sa position de début.
"""
phrase = "Les expressions régulières simplifient énormément le nettoyage"
for m in re.finditer(r"\w{7,}", phrase):
    print(m.group(), m.start())
# => expressions 4
# => régulières 16
# => simplifient 27
# => énormément 39
# => nettoyage 53
r"""
"Plus de 6 lettres" = au moins 7 : \w{7,}. finditer donne des objets Match,
donc on a accès à .start(), ce que findall ne permet pas.
"""


###################################
#  Alternance, \b et échappement  #
###################################

r"""
13. Trouvez tous les mots "le", "la" ou "les" ENTIERS dans :
    "Le chat mange la salade et les croquettes de lecture".
"""
texte = "Le chat mange la salade et les croquettes de lecture"
print(re.findall(r"\b(?:le|la|les)\b", texte, flags=re.IGNORECASE))
# => ['Le', 'la', 'les']
r"""
    - \b de chaque côté impose des mots entiers : "salade" et "lecture" ne
      sont pas pris ;
    - le groupe non capturant (?:…) limite l'alternance aux trois mots (sans
      lui, le premier \b ne s'appliquerait qu'à "le" et le dernier qu'à
      "les") ;
    - re.IGNORECASE permet de trouver "Le".
Un motif équivalent et plus court : r"\bl(?:es?|a)\b".
"""

r"""
14. L'utilisateur cherche le texte "3.5" (une variable). Pourquoi
    re.findall(recherche, "3.5 ou 315") ne donne-t-il pas le bon résultat ?
    Corrigez avec re.escape.
"""
recherche = "3.5"
print(re.findall(recherche, "3.5 ou 315"))             # => ['3.5', '315']
print(re.findall(re.escape(recherche), "3.5 ou 315"))  # => ['3.5']
r"""
Dans une regex, le point signifie "n'importe quel caractère" : "3.5" trouve
donc aussi "315". re.escape("3.5") renvoie "3\.5", où le point est échappé.
Règle : dès qu'un motif est construit à partir d'un texte venu de
l'extérieur, on l'échappe.
"""

r"""
15. Que se passe-t-il avec re.search(r"[0-9", "abc") ? Interceptez l'erreur.
"""
try:
    re.search(r"[0-9", "abc")
except re.error as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")
r"""
Le crochet ouvrant n'est jamais fermé : le motif est invalide, et re lève
une exception re.error (qui précise la position du problème).
"""


#######################
#  sub, split, flags  #
#######################

r"""
16. Avec re.sub, remplacez toutes les suites d'espaces (y compris les
    tabulations) par un seul espace.
"""
print(re.sub(r"\s+", " ", "trop    d'espaces\t\tici"))   # => trop d'espaces ici
r"""
\s couvre les espaces, tabulations et sauts de ligne ; \s+ en prend une suite
entière, remplacée par UN espace.
"""

r"""
17. Avec re.sub et des références aux groupes, convertissez les dates
    "2024-03-15" en "15/03/2024" dans "Du 2024-03-15 au 2024-04-02".
"""
print(re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1",
             "Du 2024-03-15 au 2024-04-02"))
# => Du 15/03/2024 au 02/04/2024
r"""
Les trois groupes capturent l'année, le mois et le jour ; dans le
remplacement (lui aussi en chaîne brute !), \3/\2/\1 les remet dans l'ordre
français.
"""

r"""
18. Découpez la chaîne "pommes ; poires,kiwis  ;fraises" en une liste de
    fruits sans espaces, avec un seul re.split.
"""
print(re.split(r"\s*[;,]\s*", "pommes ; poires,kiwis  ;fraises"))
# => ['pommes', 'poires', 'kiwis', 'fraises']
r"""
Le séparateur est "un point-virgule ou une virgule, entouré d'éventuels
espaces" : les espaces font partie du séparateur, donc ils disparaissent.
"""

r"""
19. Avec re.MULTILINE, récupérez la liste des noms de clés de ce fichier de
    configuration. Les lignes de commentaire ne doivent pas être prises.
"""
config = "hote=localhost\nport=8080\n# commentaire\nmode=debug"
print(re.findall(r"^(\w+)=", config, flags=re.MULTILINE))
# => ['hote', 'port', 'mode']
r"""
Avec re.MULTILINE, ^ correspond au début de CHAQUE ligne. La ligne
"# commentaire" commence par "#", qui n'est pas un caractère de mot : elle
est ignorée. Sans le drapeau, on n'obtiendrait que ['hote'].
"""

r"""
20. Réécrivez la regex de l'exercice 7 avec re.VERBOSE.
"""
PLAQUE_VERBOSE = re.compile(r"""
    [A-Z]{2}    # deux lettres majuscules
    -           # un tiret
    \d{3}       # trois chiffres
    -           # un tiret
    [A-Z]{2}    # deux lettres majuscules
""", re.VERBOSE)
print(bool(PLAQUE_VERBOSE.fullmatch("AB-123-CD")))   # => True
r"""
Avec re.VERBOSE, les espaces et les sauts de ligne du motif sont ignorés, et
tout ce qui suit un # est un commentaire. (Si l'on veut un vrai espace dans
le motif, il faut alors l'écrire "\ " ou utiliser \s.)
"""


########################
#  Cas pratiques data  #
########################

r"""
21. Écrivez une fonction prix_en_float(texte) qui convertit "12,50 €",
    "1 299,99 €" et "€ 8" en floats, et renvoie None pour "gratuit".
"""
def prix_en_float(texte):
    m = re.search(r"\d[\d ]*(?:,\d+)?", texte)
    if m is None:
        return None
    nombre = m.group().replace(" ", "").replace(",", ".")
    return float(nombre)

for p in ["12,50 €", "1 299,99 €", "€ 8", "gratuit"]:
    print(prix_en_float(p))
# => 12.5
# => 1299.99
# => 8.0
# => None
r"""
    \d          le prix commence par un chiffre
    [\d ]*      puis des chiffres ou des espaces (séparateurs de milliers)
    (?:,\d+)?   puis éventuellement une virgule et des décimales
Ensuite, on retire les espaces et on remplace la virgule par un point, pour
que float() accepte la chaîne (cf. chap. 6).
"""

r"""
22. Masquez les adresses emails d'un texte en ne gardant que la première
    lettre et le domaine.
"""
texte = "Contact : alice.martin@exemple.fr ou bob@site.com"
print(re.sub(r"\b(\w)[\w.+-]*@([\w-]+(?:\.[\w-]+)+)", r"\1***@\2", texte))
# => Contact : a***@exemple.fr ou b***@site.com
r"""
    (\w)              groupe 1 : la première lettre
    [\w.+-]*          le reste de la partie locale, qui disparaît
    @                 l'arobase
    ([\w-]+(?:\.[\w-]+)+)   groupe 2 : le domaine (au moins un point)
Le remplacement r"\1***@\2" recolle la première lettre, des étoiles et le
domaine.
"""

r"""
23. Comptez le nombre de lignes de log par niveau (INFO, ERROR, WARNING).
"""
logs = """2024-05-02 10:00:01 INFO démarrage
2024-05-02 10:05:12 ERROR disque plein
2024-05-02 10:06:00 WARNING mémoire basse
2024-05-02 11:15:42 ERROR disque plein"""

niveaux = re.findall(r"^\S+ \S+ ([A-Z]+)", logs, flags=re.MULTILINE)
print(niveaux)            # => ['INFO', 'ERROR', 'WARNING', 'ERROR']
print(Counter(niveaux))   # => Counter({'ERROR': 2, 'INFO': 1, 'WARNING': 1})
r"""
Chaque ligne commence par la date (\S+ = des caractères non blancs), un
espace, l'heure, un espace, puis le niveau en majuscules, que l'on capture.
Counter (cf. chap. 43) compte ensuite les occurrences ; avec un dictionnaire,
on aurait écrit compte[n] = compte.get(n, 0) + 1 (cf. chap. 27).
"""

r"""
24. Écrivez une fonction est_telephone(texte) qui accepte les numéros de
    téléphone français usuels et refuse les autres. Testez-la avec des assert.
"""
TELEPHONE = re.compile(r"""
    (?:\+33\s?|0)        # indicatif international ou 0
    [1-9]                # premier chiffre (jamais 0)
    (?:[\s.]?\d{2}){4}   # 4 paires de chiffres, séparées ou non
""", re.VERBOSE)

def est_telephone(texte):
    return TELEPHONE.fullmatch(texte) is not None

assert est_telephone("0612345678")
assert est_telephone("06 12 34 56 78")
assert est_telephone("06.12.34.56.78")
assert est_telephone("+33 6 12 34 56 78")
assert not est_telephone("0012345678")    # 0 après l'indicatif
assert not est_telephone("06 12 34 56")   # trop court
print("Tests de est_telephone : OK")      # => Tests de est_telephone : OK
r"""
Les tests positifs ET négatifs sont indispensables : une regex trop
permissive passerait tous les tests positifs.
"""

r"""
25. Bonus (lookahead) : écrivez une regex qui valide un mot de passe d'au
    moins 10 caractères contenant au moins un chiffre, une minuscule et une
    majuscule.
"""
MOT_DE_PASSE = re.compile(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}")
for mdp in ["motdepasse", "MotDePasse", "MotDePasse1", "Court1"]:
    print(mdp, bool(MOT_DE_PASSE.fullmatch(mdp)))
# => motdepasse False
# => MotDePasse False
# => MotDePasse1 True
# => Court1 False
r"""
Chaque (?=.*X) vérifie, depuis le début, que "X apparaît quelque part plus
loin", SANS consommer de caractères. Les trois conditions sont donc testées
indépendamment, puis .{10,} vérifie la longueur.
Remarque : trois tests séparés (any(c.isdigit() for c in mdp)…) seraient
plus lisibles ; les lookaheads sont surtout utiles quand on ne peut fournir
qu'UNE regex (dans un formulaire HTML, une base de données…).
"""
