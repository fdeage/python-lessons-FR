################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.1.0        #
# ██   ██ ██                ██   ██    © Félix Déage - 2026                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 11     #  Saisie utilisateur : corrigés                               #
#               #                                                              #
################################################################################

"""
Ce fichier est interactif : il vous posera 9 questions. Pour les autres
exercices, la saisie est "simulée" (rangée directement dans une variable),
pour ne pas avoir à répondre à des dizaines de questions. La ligne avec
input() correspondante est indiquée en commentaire.
"""


#########################
#  La fonction input()  #
#########################

"""
1. input() retourne TOUJOURS une chaîne de caractères (str), même si
   l'utilisateur tape un nombre : on obtient le texte "42", et non le nombre
   42.
"""

# 2. Saluer l'utilisateur :
prenom = input("> Ton prénom ? ")
print(f"Bonjour {prenom} !")  # => Bonjour … ! (avec le prénom saisi)
"""
Pensez à l'espace à la fin de l'invite ("> Ton prénom ? "), sinon la saisie
est collée au point d'interrogation.
"""

# 3. Le nom d'une ville et sa longueur (saisie simulée) :
ville = "Toulouse"  # en vrai : ville = input("> Ta ville ? ")
print(f"{ville} s'écrit avec {len(ville)} lettres.")
# => Toulouse s'écrit avec 8 lettres.


#########################
#  Convertir la saisie  #
#########################

# 4. Une chaîne multipliée est RÉPÉTÉE ; un nombre multiplié est… multiplié :
saisie = "5"
print(saisie * 3)       # => 555
print(int(saisie) * 3)  # => 15
"""
saisie * 3 colle trois fois le texte "5" (cf. chap. 7) : on obtient "555".
Après conversion avec int(), on calcule vraiment : 5 * 3 = 15.
"""

# 5. La somme de deux entiers :
nombre1 = int(input("> Un premier nombre entier ? "))
nombre2 = int(input("> Un second nombre entier ? "))
print(f"La somme vaut {nombre1 + nombre2}.")  # => La somme vaut … (selon
#                                                 vos saisies)
"""
Sans les int(), on obtiendrait la CONCATÉNATION des deux textes : "3" + "4"
donnerait "34" au lieu de 7 !
"""

# 6. Prix total (saisies simulées) :
prix_unitaire = float("12.5")  # en vrai : float(input("> Prix unitaire ? "))
quantite = int("3")            # en vrai : int(input("> Quantité ? "))
print(f"Total : {prix_unitaire * quantite:.2f} €")  # => Total : 37.50 €
"""
Le prix est un décimal : on le convertit avec float(). La quantité est un
nombre entier d'articles : int() suffit. Le format ":.2f" affiche toujours
2 décimales (cf. chap. 8), comme il se doit pour un prix.
"""

# 7. L'âge en 2026 (saisie simulée) :
annee_naissance = int("1990")  # en vrai : int(input("> Année de naissance ? "))
print(f"En 2026, tu auras {2026 - annee_naissance} ans.")
# => En 2026, tu auras 36 ans.


########################
#  Nettoyer la saisie  #
########################

# 8. On enchaîne les méthodes : d'abord strip(), puis upper() :
ville = "  lyon  "
print(ville.strip().upper())  # => LYON

# 9. Une réponse oui/non transformée en booléen :
reponse = input("> Aimes-tu Python ? (oui/non) ")
aime_python = reponse.strip().lower() == "oui"
print(aime_python)  # => True si vous avez tapé "oui" (même "  OUI "), sinon
#                       False
"""
On nettoie la saisie (strip, lower), PUIS on la compare à "oui" : le résultat
de la comparaison est un booléen (cf. chap. 9), que l'on range dans une
variable. Pas besoin de "if" !
"""

# 10. Normaliser une adresse email :
email = "  Ada.Lovelace@Example.COM "
print(email.strip().lower())  # => ada.lovelace@example.com
"""
Les adresses email ne tiennent pas compte des majuscules : les mettre toutes
en minuscules permet de comparer deux adresses de façon fiable.
"""


#####################################
#  Gestion d'erreurs de conversion  #
#####################################

# 11. Trois conversions sur cinq échouent :
try:
    int("3.0")  # => ValueError : int() refuse le point décimal
except ValueError as err:
    print(f"1: (Sans ce try: … except …, cette ligne créerait : {err})")

try:
    float("3,0")  # => ValueError : il faut un POINT, pas une virgule
except ValueError as err:
    print(f"2: (Sans ce try: … except …, cette ligne créerait : {err})")

print(int(" 12 "))  # => 12 (les espaces autour sont tolérés)

try:
    float("douze")  # => ValueError : du texte n'est pas un nombre
except ValueError as err:
    print(f"3: (Sans ce try: … except …, cette ligne créerait : {err})")

print(int("-5"))  # => -5 (le signe moins est accepté)

# 12. On remplace la virgule par un point AVANT de convertir :
saisie = "12,75"
print(float(saisie.replace(",", ".")))  # => 12.75


###############################################
#  Vérifier une saisie avant de la convertir  #
###############################################

# 13. isdigit() ne répond True que si TOUS les caractères sont des chiffres :
print("123".isdigit())           # => True
print("12.3".isdigit())          # => False (le point n'est pas un chiffre)
print("-7".isdigit())            # => False (le "-" non plus)
print(" 7".isdigit())            # => False (l'espace non plus)
print(" 7".strip().isdigit())    # => True (après nettoyage)
print("".isdigit())              # => False (une chaîne vide)

# 14. Vérifier une saisie :
places = input("> Combien de places veux-tu réserver ? ")
print(f"Saisie valide : {places.strip().isdigit()}")  # => Saisie valide : …
#                                                        (True ou False)
"""
On nettoie d'abord la saisie avec strip(), pour que " 3 " soit accepté. Au
chap. 12, on pourra utiliser ce booléen pour décider quoi faire (convertir,
ou afficher un message d'erreur).
"""


###################################
#  Petits programmes interactifs  #
###################################

# 15. Convertisseur km → miles :
saisie = input("> Une distance en km (ex. : 42,195) ? ")
km = float(saisie.strip().replace(",", "."))
miles = km / 1.609344
print(f"{km} km = {miles:.2f} miles")  # => 42.195 km = 26.22 miles (pour
#                                          une saisie de 42,195)
"""
Les trois étapes classiques : nettoyer (strip, replace), convertir (float),
calculer. Un mile étant plus long qu'un kilomètre, on DIVISE par 1.609344.
"""

# 16. Une durée en heures et minutes (saisie simulée) :
duree = int("135")  # en vrai : duree = int(input("> Durée en minutes ? "))
print(f"{duree // 60} h {duree % 60} min")  # => 2 h 15 min
"""
135 // 60 donne le nombre d'heures complètes (2), et 135 % 60 les minutes
restantes (15), cf. chap. 4.
"""

# 17. Carte de visite (saisies simulées) :
prenom = "  ada "     # en vrai : prenom = input("> Ton prénom ? ")
nom = "lovelace"      # en vrai : nom = input("> Ton nom ? ")
print(f"{prenom.strip().capitalize()} {nom.strip().upper()}")
# => Ada LOVELACE
"""
capitalize() met la 1re lettre en majuscule et le reste en minuscules (cf.
chap. 8) ; upper() met tout en majuscules. Le strip() d'abord, sinon
capitalize() s'appliquerait à l'espace de tête, et "a" resterait minuscule !
"""

# 18. La moyenne de trois notes :
note1 = float(input("> Note 1 ? ").replace(",", "."))
note2 = float(input("> Note 2 ? ").replace(",", "."))
note3 = float(input("> Note 3 ? ").replace(",", "."))
moyenne = (note1 + note2 + note3) / 3
print(f"Moyenne : {moyenne:.1f}")  # => Moyenne : … (par exemple 13.5 pour
#                                     12, 15 et 13.5)
"""
Attention aux parenthèses : sans elles, seule note3 serait divisée par 3
(la division passe avant l'addition, cf. chap. 5).
"""
