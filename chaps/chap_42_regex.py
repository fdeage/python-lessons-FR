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
#  Chap. 42     #  Expressions régulières                                      #
#               #                                                              #
################################################################################
#
#  - Introduction
#  - Les chaînes brutes : r"…"
#  - Chercher : search, match et fullmatch
#  - Les objets Match
#  - Les caractères spéciaux : . ^ $
#  - Les classes de caractères : [] et \d \w \s
#  - Les quantificateurs : * + ? {m,n}
#  - Gourmand ou paresseux ?
#  - Trouver toutes les occurrences : findall et finditer
#  - Les groupes
#  - Alternance et frontières de mots : | et \b
#  - Échapper les caractères spéciaux
#  - Les drapeaux : IGNORECASE, MULTILINE, VERBOSE
#  - Compiler une regex : re.compile
#  - Remplacer et découper : sub et split
#  - Bonus : lookahead et lookbehind
#  - Cas pratiques en Data Science
#  - Pièges et bonnes pratiques
#  - En bref
#
#############################################

import re


# Introduction
###############

r"""
Une "expression régulière" (en anglais "regular expression", abrégé "regex"
ou "regexp") est un MOTIF (un "pattern") qui décrit une famille de chaînes de
caractères. Par exemple :
    - "un ou plusieurs chiffres"
    - "5 chiffres à la suite" (un code postal)
    - "des lettres, un @, des lettres, un point, des lettres" (un email)

Une fois le motif écrit, on peut demander à Python :
    - est-ce que cette chaîne CONTIENT le motif ?          (re.search)
    - est-ce que cette chaîne EST EXACTEMENT le motif ?    (re.fullmatch)
    - trouve-moi TOUTES les occurrences du motif           (re.findall)
    - REMPLACE toutes les occurrences du motif par…        (re.sub)
    - DÉCOUPE la chaîne à chaque occurrence du motif       (re.split)

Les regex existent dans presque tous les langages (JavaScript, Java, SQL,
grep, éditeurs de texte…), avec une syntaxe très proche : ce que vous
apprenez ici vous servira partout.

En Python, elles sont fournies par le module "re" de la bibliothèque standard
(rien à installer, cf. chap. 22) : on l'a importé en haut du fichier.

IMPT : Avant de sortir les regex, demandez-vous si les méthodes des strings
(cf. chap. 7 et 8) ne suffisent pas. Elles sont plus simples et plus lisibles :
"""
phrase = "Le chat dort sur le canapé"
print("chat" in phrase)             # => True
print(phrase.startswith("Le"))      # => True
print(phrase.replace("chat", "chien"))  # => Le chien dort sur le canapé
print("2024".isdigit())             # => True

r"""
Les regex deviennent utiles quand on cherche une FORME plutôt qu'un texte
précis : "n'importe quel nombre", "un mot qui commence par une majuscule",
"une date au format jj/mm/aaaa"… Là, les méthodes des strings ne suffisent
plus.
"""


# Les chaînes brutes : r"…"
############################

r"""
Les regex utilisent beaucoup l'antislash "\" (par exemple "\d" veut dire "un
chiffre"). Or, dans une string normale, l'antislash sert déjà à écrire des
caractères spéciaux (cf. chap. 7) : "\n" est un saut de ligne, "\t" une
tabulation, "\b" un "retour arrière"…

Pour éviter les conflits, on écrit TOUJOURS les regex dans une "chaîne brute"
(raw string), préfixée par r : dans r"…", l'antislash est un caractère
ordinaire, que Python laisse tel quel.
"""
print(len("\n"))    # => 1 : un seul caractère, le saut de ligne
print(len(r"\n"))   # => 2 : deux caractères, "\" et "n"
print(r"\d+")       # => \d+

r"""
IMPT : prenez l'habitude d'écrire r"…" pour TOUTES vos regex, même quand ce
n'est pas indispensable. Sans le r, "\d" provoque un avertissement
(SyntaxWarning) dans les versions récentes de Python, et "\b" devient un
caractère invisible : votre regex ne trouvera rien, sans erreur !
"""


# Chercher : search, match et fullmatch
########################################

r"""
Les trois fonctions de base prennent un motif et une chaîne :
    - re.search(motif, texte)    : le motif apparaît-il QUELQUE PART ?
    - re.match(motif, texte)     : le texte COMMENCE-t-il par le motif ?
    - re.fullmatch(motif, texte) : le texte ENTIER correspond-il au motif ?

Elles renvoient un objet "Match" si le motif est trouvé, et None sinon.
Comme None est "faux" (cf. chap. 21), on les utilise directement dans un if.
"""
texte = "Commande 4521 expédiée"

print(re.search(r"\d+", texte))
# => <re.Match object; span=(9, 13), match='4521'>
# texte ne commence pas par un chiffre :
print(re.match(r"\d+", texte))      # => None
print(re.fullmatch(r"\d+", texte))  # => None : texte n'est pas QUE des chiffres
print(re.fullmatch(r"\d+", "4521"))
# => <re.Match object; span=(0, 4), match='4521'>

if re.search(r"\d", texte):
    print("Le texte contient au moins un chiffre")
# => Le texte contient au moins un chiffre

r"""
Ici, r"\d+" signifie "un ou plusieurs chiffres" : on détaille cette syntaxe
dans les sections suivantes.

Quelle fonction choisir ?
    - pour TROUVER quelque chose dans un texte : search
    - pour VALIDER un format (un code postal, une date saisie…) : fullmatch
    - match est rarement utile : search avec "^" (cf. plus bas) fait pareil.
"""


# Les objets Match
###################

r"""
Quand la recherche réussit, l'objet Match renvoyé contient des informations
sur ce qui a été trouvé :
    - .group()  : le texte trouvé
    - .start()  : l'indice de début
    - .end()    : l'indice de fin (exclu, comme pour les slices, cf. chap. 31)
    - .span()   : le tuple (début, fin)
"""
m = re.search(r"\d+", "Il fait 23 degrés")
print(m.group())   # => 23
print(m.start())   # => 8
print(m.end())     # => 10
print(m.span())    # => (8, 10)
print("Il fait 23 degrés"[8:10])  # => 23 : on retrouve bien le texte

r"""
Attention : si la recherche échoue, on obtient None, qui n'a pas de méthode
.group(). C'est une erreur très fréquente :
"""
m = re.search(r"\d+", "Il fait beau")
try:
    print(m.group())
except AttributeError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

# La bonne pratique : toujours tester le résultat avant de s'en servir.
if m:
    print(m.group())
else:
    print("Aucun nombre trouvé")
# => Aucun nombre trouvé


# Les caractères spéciaux : . ^ $
##################################

r"""
Dans un motif, la plupart des caractères se représentent eux-mêmes : r"chat"
cherche exactement "chat". Mais certains ont un sens spécial :

    .   n'importe quel caractère (sauf le saut de ligne)
    ^   le DÉBUT de la chaîne
    $   la FIN de la chaîne
"""
print(re.search(r"c.t", "un cat"))
# => <re.Match object; span=(3, 6), match='cat'>
print(re.search(r"c.t", "le cut"))
# => <re.Match object; span=(3, 6), match='cut'>
print(re.search(r"c.t", "le ct"))  # => None : il faut exactement 1 caractère

print(bool(re.search(r"^Bonjour", "Bonjour à tous")))  # => True
print(bool(re.search(r"^Bonjour", "Hé, Bonjour")))     # => False
print(bool(re.search(r"\.csv$", "ventes.csv")))        # => True
print(bool(re.search(r"\.csv$", "ventes.csv.bak")))    # => False

r"""
Note : dans r"\.csv$", le point est précédé d'un antislash pour signifier "un
VRAI point" et non "n'importe quel caractère" (cf. "Échapper les caractères
spéciaux", plus bas).

Les autres caractères spéciaux sont : * + ? { } [ ] ( ) | \
On les découvre un par un dans la suite du chapitre.
"""


# Les classes de caractères : [] et \d \w \s
#############################################

r"""
Les crochets [] définissent une "classe" : UN caractère parmi ceux listés.
    [aeiou]     une voyelle
    [0-9]       un chiffre (le tiret indique un intervalle)
    [a-zA-Z]    une lettre non accentuée, minuscule ou majuscule
    [^0-9]      UN caractère qui n'est PAS un chiffre (^ au début = négation)
"""
print(re.findall(r"[aeiouy]", "python"))  # => ['y', 'o']
print(re.findall(r"[0-9]", "A1B22"))      # => ['1', '2', '2']
print(re.findall(r"[^0-9]", "A1B22"))     # => ['A', 'B']

r"""
(re.findall renvoie la liste de toutes les occurrences : cf. plus bas.)

Comme certaines classes reviennent sans arrêt, elles ont un raccourci :
    \d   un chiffre ("digit")                ≈ [0-9]
    \w   un caractère de "mot" ("word") : lettre (accentuée ou non),
         chiffre ou "_"
    \s   un "blanc" ("space") : espace, tabulation, saut de ligne…

Et leurs versions en MAJUSCULE sont leur contraire :
    \D   tout sauf un chiffre
    \W   tout sauf un caractère de mot (ponctuation, espaces…)
    \S   tout sauf un blanc
"""
adresse = "12 rue de l'Été, 69007"
print(re.findall(r"\d", adresse))   # => ['1', '2', '6', '9', '0', '0', '7']
print(re.findall(r"\W", adresse))   # => [' ', ' ', ' ', "'", ',', ' ']
print(re.findall(r"\s", "a b\tc"))  # => [' ', '\t']

r"""
Note : en Python 3, \w reconnaît les lettres accentuées ("É", "é"…), ce qui
est pratique pour du texte français. Ce n'est pas le cas de [a-zA-Z] !
"""
print(re.findall(r"\w", "Été"))       # => ['É', 't', 'é']
print(re.findall(r"[a-zA-Z]", "Été"))  # => ['t']


# Les quantificateurs : * + ? {m,n}
####################################

r"""
Un quantificateur se place APRÈS un élément pour dire combien de fois il peut
se répéter :
    *       0 fois ou plus
    +       1 fois ou plus
    ?       0 ou 1 fois (l'élément est optionnel)
    {3}     exactement 3 fois
    {2,4}   entre 2 et 4 fois
    {2,}    au moins 2 fois

IMPT : le quantificateur porte sur l'élément JUSTE AVANT lui (un caractère,
une classe [], ou un groupe () vu plus bas).
"""
print(re.findall(r"\d+", "3 pommes et 12 poires"))  # => ['3', '12']
print(re.findall(r"\d", "3 pommes et 12 poires"))   # => ['3', '1', '2']

# "colou?r" : le "u" est optionnel (orthographes anglaise et américaine)
print(re.findall(r"colou?r", "color colour"))  # => ['color', 'colour']

# Un code postal français : exactement 5 chiffres
print(bool(re.fullmatch(r"\d{5}", "69007")))   # => True
print(bool(re.fullmatch(r"\d{5}", "6907")))    # => False

# Une année entre 1000 et 2999, très simplement :
print(re.findall(r"[12]\d{3}", "En 1998 puis 2024, pas 3500"))
# => ['1998', '2024']

r"""
Différence entre * et + : avec *, "zéro fois" est accepté. Un motif qui peut
correspondre à une chaîne VIDE donne parfois des résultats surprenants :
"""
print(re.findall(r"\d*", "a12"))  # => ['', '12', '']
r"""
Les '' sont des correspondances vides trouvées devant "a" et en fin de chaîne.
En pratique, on préfère presque toujours + à *.
"""


# Gourmand ou paresseux ?
##########################

r"""
Par défaut, les quantificateurs sont "gourmands" ("greedy") : ils prennent le
PLUS de caractères possible. C'est souvent un piège, par exemple avec des
balises HTML :
"""
html = "<b>gras</b> et <i>italique</i>"
print(re.findall(r"<.+>", html))   # => ['<b>gras</b> et <i>italique</i>']

r"""
On voulait chaque balise séparément, mais ".+" a avalé le plus possible :
du premier "<" jusqu'au DERNIER ">".

En ajoutant un "?" après le quantificateur, on le rend "paresseux" ("lazy") :
il prend le MOINS de caractères possible.
    *?   +?   ??   {m,n}?
"""
print(re.findall(r"<.+?>", html))
# => ['<b>', '</b>', '<i>', '</i>']

r"""
Une autre solution, souvent plus claire et plus rapide : une classe niée.
"<[^>]+>" se lit "un <, puis des caractères qui ne sont pas des >, puis >".
"""
print(re.findall(r"<[^>]+>", html))
# => ['<b>', '</b>', '<i>', '</i>']


# Trouver toutes les occurrences : findall et finditer
#######################################################

r"""
re.findall(motif, texte) renvoie la LISTE de tous les textes trouvés (une
liste vide si rien n'est trouvé). C'est la fonction la plus utilisée pour
extraire des données.
"""
releve = "Lundi : 12.5°C, mardi : 14°C, mercredi : -2.5°C"
temperatures = re.findall(r"-?\d+(?:\.\d+)?", releve)
print(temperatures)   # => ['12.5', '14', '-2.5']
# On obtient des strings : il faut les convertir pour calculer (cf. chap. 6)
valeurs = [float(t) for t in temperatures]
print(sum(valeurs) / len(valeurs))  # => 8.0

r"""
Décortiquons r"-?\d+(?:\.\d+)?" :
    -?          un signe moins, optionnel
    \d+         un ou plusieurs chiffres
    (?:\.\d+)?  un groupe (cf. section suivante) optionnel : un point suivi
                de chiffres. Le "?:" indique un groupe "non capturant" (on
                y revient plus bas).

re.finditer(motif, texte) fait la même chose, mais renvoie un ITÉRATEUR
(cf. chap. 23 et 36) d'objets Match : utile quand on a besoin des positions,
ou quand le texte est très long.
"""
for m in re.finditer(r"\d+", "a1 b22 c333"):
    print(m.group(), m.span())
# => 1 (1, 2)
# => 22 (4, 6)
# => 333 (8, 11)


# Les groupes
##############

r"""
Les parenthèses () ont deux rôles :
    1. REGROUPER des éléments, pour leur appliquer un quantificateur :
       r"(ha)+" = "ha" répété une ou plusieurs fois
    2. CAPTURER une partie du texte trouvé, pour la récupérer ensuite.
"""
print(re.fullmatch(r"(ha)+", "hahaha") is not None)  # => True

# Capturer : une date au format jj/mm/aaaa
m = re.search(r"(\d{2})/(\d{2})/(\d{4})", "Né le 14/07/1989 à Paris")
print(m.group())    # => 14/07/1989 : le texte trouvé en entier (= group(0))
print(m.group(1))   # => 14 : le 1er groupe
print(m.group(3))   # => 1989
print(m.groups())   # => ('14', '07', '1989') : tous les groupes

r"""
IMPT : avec des groupes, re.findall change de comportement : il renvoie les
GROUPES (sous forme de tuples s'il y en a plusieurs), et non le texte entier.
"""
texte = "Rendez-vous le 03/02/2024 et le 15/03/2024"
print(re.findall(r"\d{2}/\d{2}/\d{4}", texte))
# => ['03/02/2024', '15/03/2024']
print(re.findall(r"(\d{2})/(\d{2})/(\d{4})", texte))
# => [('03', '02', '2024'), ('15', '03', '2024')]

r"""
C'est pour cela qu'on utilise des groupes "non capturants" (?:…) quand on
veut seulement regrouper, sans capturer (cf. les températures plus haut).

Les groupes nommés : (?P<nom>…)
Quand il y a beaucoup de groupes, les numéros deviennent illisibles. On peut
donner un nom à chaque groupe, et le récupérer avec .group("nom") ou avec
.groupdict(), qui renvoie un dictionnaire (cf. chap. 18) :
"""
m = re.search(r"(?P<jour>\d{2})/(?P<mois>\d{2})/(?P<annee>\d{4})",
              "Né le 14/07/1989")
print(m.group("annee"))   # => 1989
print(m.groupdict())      # => {'jour': '14', 'mois': '07', 'annee': '1989'}


# Alternance et frontières de mots : | et \b
#############################################

r"""
La barre verticale | signifie "OU" : r"chat|chien" trouve "chat" ou "chien".
Elle a une priorité très faible : elle sépare TOUT ce qui est à sa gauche de
TOUT ce qui est à sa droite. On utilise donc souvent un groupe pour la
limiter.
"""
print(re.findall(r"chat|chien", "un chat, un chien, un poisson"))
# => ['chat', 'chien']
print(re.findall(r"(?:Mme|M\.) \w+", "M. Dupont et Mme Martin"))
# => ['M. Dupont', 'Mme Martin']

r"""
\b est une "ancre" : il ne correspond à aucun caractère, mais à une FRONTIÈRE
de mot (le passage entre un caractère de mot \w et autre chose). Il permet de
chercher des mots entiers :
"""
print(re.findall(r"art", "art, partir, artiste"))  # => ['art', 'art', 'art']
print(re.findall(r"\bart\b", "art, partir, artiste"))  # => ['art']
print(re.findall(r"\bart\w*", "art, partir, artiste"))  # => ['art', 'artiste']

r"""
(C'est ici que le r de la chaîne brute est vital : sans lui, "\b" serait le
caractère "retour arrière", et la regex ne trouverait rien.)
"""


# Échapper les caractères spéciaux
###################################

r"""
Pour chercher un caractère spécial "pour de vrai" (un point, un +, une
parenthèse…), on le précède d'un antislash : on dit qu'on l'"échappe".
    \.   un vrai point
    \+   un vrai plus
    \(   une vraie parenthèse
    \\   un vrai antislash
"""
print(re.findall(r"\d+\.\d+", "Prix : 3.50 ou 4x50"))  # => ['3.50']
print(re.findall(r"\d+.\d+", "Prix : 3.50 ou 4x50"))   # => ['3.50', '4x50']

r"""
Dans une classe [], la plupart des caractères spéciaux perdent leur sens :
[.+*] signifie "un point, un plus ou une étoile". Seuls ^ (au début), - (au
milieu) et ] gardent un sens particulier.

Quand le texte à chercher vient d'une variable (une saisie de l'utilisateur,
par exemple), on ne sait pas s'il contient des caractères spéciaux.
re.escape() les échappe tous automatiquement :
"""
recherche = "1+1"
print(re.escape(recherche))                         # => 1\+1
print(re.findall(recherche, "1+1=2, 11=11"))        # => ['11', '11']
print(re.findall(re.escape(recherche), "1+1=2, 11=11"))  # => ['1+1']

# Une regex mal formée lève une erreur re.error :
try:
    re.search(r"(\d+", "123")
except re.error as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")


# Les drapeaux : IGNORECASE, MULTILINE, VERBOSE
################################################

r"""
Les fonctions de re acceptent un argument "flags" (des "drapeaux") qui
modifie leur comportement. Les plus utiles :

    re.IGNORECASE (ou re.I) : ignore la différence majuscules/minuscules
"""
print(re.findall(r"python", "Python, PYTHON, python"))
# => ['python']
print(re.findall(r"python", "Python, PYTHON, python", flags=re.IGNORECASE))
# => ['Python', 'PYTHON', 'python']

r"""
    re.MULTILINE (ou re.M) : ^ et $ correspondent au début et à la fin de
    CHAQUE LIGNE, et non plus seulement de toute la chaîne.
"""
inventaire = """pommes: 12
poires: 7
kiwis: 30"""
print(re.findall(r"^\w+", inventaire))                  # => ['pommes']
print(re.findall(r"^\w+", inventaire, flags=re.MULTILINE))
# => ['pommes', 'poires', 'kiwis']

r"""
    re.VERBOSE (ou re.X) : les espaces et les sauts de ligne du motif sont
    ignorés, et on peut y mettre des commentaires avec #. Indispensable pour
    rendre lisible une regex longue !
"""
motif_telephone = r"""
    (?:\+33\s?|0)     # indicatif : +33 (avec ou sans espace) ou 0
    [1-9]             # premier chiffre après l'indicatif (pas 0)
    (?:[\s.-]?\d{2}){4}   # 4 paires de chiffres, séparées ou non
"""
print(bool(re.fullmatch(motif_telephone, "06 12 34 56 78", flags=re.VERBOSE)))
# => True
print(bool(re.fullmatch(motif_telephone, "+33 6.12.34.56.78",
                        flags=re.VERBOSE)))
# => True

r"""
On combine plusieurs drapeaux avec l'opérateur | (le "ou" bit à bit vu au
chap. 21) : flags=re.IGNORECASE | re.MULTILINE.
"""


# Compiler une regex : re.compile
##################################

r"""
Quand on utilise plusieurs fois le même motif, on peut le "compiler" une fois
pour toutes avec re.compile(). On obtient un objet Pattern, qui possède les
mêmes méthodes que le module re (search, findall, sub…), sans avoir à repasser
le motif :
"""
CODE_POSTAL = re.compile(r"\b\d{5}\b")

adresses = ["10 rue Neuve 69002 Lyon", "Paris 75011", "BP 12"]
for adresse in adresses:
    m = CODE_POSTAL.search(adresse)
    print(m.group() if m else "pas de code postal")
# => 69002
# => 75011
# => pas de code postal

r"""
Avantages :
    - le motif est défini à un seul endroit, avec un nom parlant (une
      "constante" en majuscules, cf. chap. 20) ;
    - on peut passer les drapeaux une seule fois : re.compile(motif, re.I).
Le gain de vitesse, lui, est faible : Python garde déjà en cache les derniers
motifs utilisés.
"""


# Remplacer et découper : sub et split
#######################################

r"""
re.sub(motif, remplacement, texte) remplace TOUTES les occurrences du motif.
C'est l'équivalent de str.replace() (cf. chap. 8), mais avec un motif.
"""
# Normaliser les espaces multiples :
print(re.sub(r"\s+", " ", "trop   d'espaces \t ici"))  # => trop d'espaces ici

# Masquer des numéros de carte :
print(re.sub(r"\d{4}(?=\d{4})", "****", "1234567812345678"))
# => ************5678
# (le (?=…) est un "lookahead", cf. la section bonus)

r"""
Dans le remplacement, \1, \2… (ou \g<nom>) désignent le contenu des groupes
capturés. Pratique pour réorganiser un texte, par exemple passer des dates
du format français jj/mm/aaaa au format international aaaa-mm-jj :
"""
print(re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", "le 14/07/1989"))
# => le 1989-07-14

r"""
Le remplacement peut même être une FONCTION (cf. chap. 32) : elle reçoit
l'objet Match et renvoie le texte de remplacement.
"""
def doubler(m):
    return str(int(m.group()) * 2)

print(re.sub(r"\d+", doubler, "3 œufs et 250 g de farine"))
# => 6 œufs et 500 g de farine

r"""
re.split(motif, texte) découpe le texte à chaque occurrence du motif, comme
str.split() mais avec plusieurs séparateurs possibles :
"""
print(re.split(r"[,;]\s*", "pommes, poires;kiwis ;  fraises"))
# => ['pommes', 'poires', 'kiwis ', 'fraises']
print(re.split(r"\s*[,;]\s*", "pommes, poires;kiwis ;  fraises"))
# => ['pommes', 'poires', 'kiwis', 'fraises']


# Bonus : lookahead et lookbehind
##################################

r"""
Les "lookarounds" (regarder autour) vérifient ce qui se trouve AVANT ou APRÈS
une position, sans l'inclure dans le résultat :
    (?=…)    lookahead : suivi de…
    (?!…)    lookahead négatif : NON suivi de…
    (?<=…)   lookbehind : précédé de…
    (?<!…)   lookbehind négatif : NON précédé de…
"""
prix = "Total : 45 € (dont 7 € de port), réf. 1234"
# les nombres suivis de " €" :
print(re.findall(r"\d+(?= €)", prix))      # => ['45', '7']
print(re.findall(r"(?<=réf\. )\d+", prix))  # => ['1234']

r"""
Un usage classique : vérifier plusieurs conditions sur un mot de passe, chacune
avec un lookahead placé au début du motif.
"""
FORT = re.compile(r"(?=.*\d)(?=.*[A-Z]).{8,}")
print(bool(FORT.fullmatch("motdepasse")))   # => False : ni chiffre ni majuscule
print(bool(FORT.fullmatch("MotDePasse42")))  # => True


# Cas pratiques en Data Science
################################

r"""
En Data Science, les regex servent surtout à NETTOYER et EXTRAIRE des données
textuelles mal formatées. Quelques exemples typiques.

1. Convertir des prix écrits "à la française" en nombres :
"""
prix_bruts = ["12,50 €", "1 299,00€", "€ 8", "gratuit"]

def prix_en_float(texte):
    """Renvoie le prix contenu dans texte, ou None s'il n'y en a pas."""
    m = re.search(r"\d[\d\s]*(?:,\d+)?", texte)
    if m is None:
        return None
    nombre = re.sub(r"\s", "", m.group())   # retire les espaces des milliers
    return float(nombre.replace(",", "."))   # virgule -> point

print([prix_en_float(p) for p in prix_bruts])  # => [12.5, 1299.0, 8.0, None]

r"""
2. Extraire des emails d'un texte. Le motif ci-dessous est volontairement
simple : il couvre les cas courants, pas tous les cas autorisés par la norme
(cf. "Pièges et bonnes pratiques").
"""
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
message = "Écrivez à ada.lovelace@exemple.fr ou à support+fr@site.co.uk !"
print(EMAIL.findall(message))
# => ['ada.lovelace@exemple.fr', 'support+fr@site.co.uk']

r"""
3. Analyser des lignes de log (des journaux d'événements, cf. chap. 44) pour
en faire des données structurées, prêtes à être analysées :
"""
journal = """2024-03-01 08:15:02 INFO Connexion de alice
2024-03-01 08:17:45 ERROR Base de données injoignable
2024-03-01 09:02:11 WARNING Disque rempli à 91%
2024-03-01 09:30:00 ERROR Délai dépassé"""

LIGNE_LOG = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<heure>[\d:]{8}) "
    r"(?P<niveau>[A-Z]+) (?P<message>.*)"
)
evenements = [m.groupdict() for m in LIGNE_LOG.finditer(journal)]
print(len(evenements))   # => 4
print(evenements[1])
# => {'date': '2024-03-01', 'heure': '08:17:45', 'niveau': 'ERROR',
#      'message': 'Base de données injoignable'}
erreurs = [e["heure"] for e in evenements if e["niveau"] == "ERROR"]
print(erreurs)   # => ['08:17:45', '09:30:00']

r"""
(Note : deux chaînes brutes écrites côte à côte sont collées automatiquement
par Python : c'est pratique pour couper une regex longue sur plusieurs
lignes, cf. chap. 8.)

4. Valider des données avant de les utiliser : on garde les codes postaux
valides, et on met de côté les autres pour les vérifier à la main.
"""
codes = ["69007", "7500", "13 001", "33000", "2A004"]
valides = [c for c in codes if re.fullmatch(r"\d{5}|2[AB]\d{3}", c)]
invalides = [c for c in codes if c not in valides]
print(valides)     # => ['69007', '33000', '2A004']
print(invalides)   # => ['7500', '13 001']

r"""
(Les codes de la Corse commencent par 2A ou 2B : d'où l'alternance.)

5. Avec pandas : les colonnes de texte ont des méthodes .str qui acceptent
des regex (cf. chap. 39 et 48) :
    df["ville"].str.contains(r"^Saint", regex=True)   # filtre
    df["date"].str.extract(r"(\d{4})")                # extrait l'année
    df["prix"].str.replace(r"[^\d,]", "", regex=True) # nettoie
C'est exactement la même syntaxe de motifs que dans ce chapitre.
"""


# Pièges et bonnes pratiques
#############################

r"""
1. Les regex deviennent vite illisibles. Comparez :
       r"^(?:(?:\+33\s?|0)[1-9](?:[\s.-]?\d{2}){4})$"
   avec la version VERBOSE commentée de la section "Les drapeaux". Pour toute
   regex de plus d'une quinzaine de caractères : re.VERBOSE et des
   commentaires, ou un découpage en petites regex nommées.

2. Une regex "parfaite" n'existe pas toujours. La regex qui valide TOUS les
   emails permis par la norme fait plusieurs centaines de caractères… et ne
   dit toujours pas si l'adresse existe ! Visez une regex SIMPLE qui couvre
   les cas réels, et vérifiez les cas limites autrement (en envoyant un email
   de confirmation, par exemple).

3. Pour les formats structurés, utilisez un vrai outil plutôt qu'une regex :
       - dates          : datetime.strptime (cf. chap. 30)
       - CSV            : le module csv ou pandas (cf. chap. 28 et 39)
       - JSON           : le module json (cf. chap. 28)
       - HTML           : une bibliothèque comme BeautifulSoup (cf. chap. 49)
   Par exemple, r"\d{2}/\d{2}/\d{4}" accepte "99/99/2024", que strptime
   rejetterait.

4. Testez vos regex ! Sur des exemples qui DOIVENT passer, et sur des
   exemples qui NE DOIVENT PAS passer (cf. chap. 29 et 37) :
"""
def est_code_postal(texte):
    return re.fullmatch(r"\d{5}", texte) is not None

assert est_code_postal("69007")
assert not est_code_postal("6900")      # trop court
assert not est_code_postal("690077")    # trop long
assert not est_code_postal("69 007")    # espace
print("Tests de est_code_postal : OK")  # => Tests de est_code_postal : OK

r"""
5. Pour mettre au point une regex, utilisez un site comme
   https://regex101.com (choisissez la saveur "Python") : il explique chaque
   morceau du motif et surligne les correspondances en direct.
"""


# En bref
##########

r"""
    import re
    r"…"                    toujours écrire les regex en chaîne brute
    re.search(m, t)         m apparaît-il dans t ? -> Match ou None
    re.fullmatch(m, t)      t correspond-il entièrement à m ? (validation)
    re.findall(m, t)        liste de toutes les occurrences (ou des groupes)
    re.finditer(m, t)       itérateur d'objets Match
    re.sub(m, r, t)         remplace (r peut contenir \1 ou être une fonction)
    re.split(m, t)          découpe t à chaque occurrence de m
    re.compile(m, flags)    motif réutilisable

    .  ^  $                 n'importe quel caractère, début, fin
    [abc] [a-z] [^0-9]      classes de caractères
    \d \w \s / \D \W \S     chiffre, caractère de mot, blanc / leurs contraires
    * + ? {m,n}             quantificateurs (gourmands) ; *? +? : paresseux
    ( ) (?: ) (?P<nom> )    groupe capturant, non capturant, nommé
    a|b    \b               alternance, frontière de mot
    \.  re.escape(t)        échapper un caractère spécial / tout un texte
    re.I  re.M  re.X        IGNORECASE, MULTILINE, VERBOSE
"""
