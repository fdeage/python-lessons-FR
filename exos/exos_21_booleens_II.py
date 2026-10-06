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
#  Chap. 21     #  Booléens II : exercices                                     #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) avant de vérifier avec print().

Les corrigés sont dans le fichier corrs/corr_21_booleens_II.py.
"""


######################
#  Tables de vérité  #
######################

"""
1. Sans exécuter, complétez la table de vérité de "not A or B" :

      A     | B     | not A or B
     ------ | ----- | ----------
      True  | True  |
      True  | False |
      False | True  |
      False | False |

   Puis faites-la calculer par Python avec deux boucles "for".

2. Combien de lignes a la table de vérité d'une expression qui utilise
   3 variables booléennes A, B et C ? Et 5 variables ? Affichez avec trois
   boucles imbriquées la table de "A and (B or C)".

3. Écrivez une fonction xor(a, b) qui retourne True si un seul des deux
   booléens est vrai. Testez-la sur les 4 combinaisons.

4. Au restaurant, on choisit "entrée OU dessert" (mais pas les deux). Avec
   les variables entree = True et dessert = False, écrivez la condition qui
   vérifie que la commande est valide.
"""


###########################
#  Les lois de De Morgan  #
###########################

"""
5. Réécrivez ces conditions SANS "not" devant une parenthèse, en appliquant
   les lois de De Morgan (puis en simplifiant les "not" sur les
   comparaisons) :
     a) not (x > 0 and y > 0)
     b) not (age < 12 or age > 60)
     c) not (mot == "" or mot == "stop")

6. Vérifiez avec deux boucles que "not (A and B)" et "not A and not B" ne
   sont PAS équivalents : pour quelles valeurs de A et B diffèrent-ils ?

7. Un parc d'attractions refuse l'accès si "la personne mesure moins de
   1,20 m OU a moins de 8 ans". Écrivez la condition d'ACCÈS (la personne
   peut entrer) de deux façons : avec un "not", puis sans "not".
"""


##############################################
#  Calculs avec les booléens et conversions  #
##############################################

"""
8. Sans exécuter, que valent ces expressions ?
     a) True + True + True
     b) True * 10 - False
     c) (3 > 2) + (2 > 3)
     d) 1 == True
     e) 2 == True
     f) int(False) + int(True)

9. Une liste contient les réponses d'un QCM, corrigées : True si la réponse
   est juste. Calculez la note sur 20 à partir de cette liste, en utilisant
   sum().
       reponses = [True, True, False, True, False, True, True, True]
"""


############################################
#  Valeurs "vraies" et "fausses" : bool()  #
############################################

"""
10. Sans exécuter, que vaut bool() de chacune de ces valeurs ?
      0    0.0    -1    ""    " "    "0"    "False"    []    [[]]    {}
      None    (0,)    0.001

11. Sans exécuter, qu'affiche ce programme ?
        for valeur in [0, 1, "", "a", [], [0], None]:
            if valeur:
                print(valeur, "est vrai")
            else:
                print(valeur, "est faux")

12. Écrivez une fonction decrire_panier(panier) qui affiche "Panier vide" si
    la liste est vide, et "N article(s)" sinon. Utilisez "if not panier:"
    plutôt qu'une comparaison avec len().

13. Ce programme est bogué : il affiche "Stock inconnu" alors que le stock
    est connu (il vaut 0). Corrigez-le.
        stock = 0
        if stock:
            print("Stock :", stock)
        else:
            print("Stock inconnu")
"""


##############################################
#  Ce que retournent vraiment "and" et "or"  #
##############################################

"""
14. Sans exécuter, que valent ces expressions ?
      a) 0 or 7
      b) 4 or 7
      c) 0 and 7
      d) 4 and 7
      e) "" or "vide"
      f) [] or [0]
      g) None or 0 or ""
      h) "a" and "b" and "c"
      i) not "abc"

15. Écrivez une fonction saluer(nom) qui affiche "Bonjour <nom>", ou
    "Bonjour inconnu·e" si nom est une chaîne vide. Utilisez "or", sans "if".

16. Pourquoi "or" n'est-il pas une bonne idée pour donner une valeur par
    défaut à un nombre de places réservées, qui peut valoir 0 ?
        places = 0
        places_affichees = places or 2
"""


########################################
#  Égalité et identité : "==" et "is"  #
########################################

"""
17. Sans exécuter, qu'affiche ce programme ?
        a = [1, 2]
        b = [1, 2]
        c = a
        print(a == b, a is b, a is c)
        c.append(3)
        print(a, b)
        b = a
        print(a is b)

18. Corrigez les comparaisons suivantes pour respecter les bonnes pratiques
    (cf. aussi chap. 20) :
        if resultat == None: …
        if est_admin is True: …
        if nom is "Ada": …
"""


####################
#  all() et any()  #
####################

"""
19. Sans exécuter, que valent ces expressions ?
      a) all([True, True, False])
      b) any([False, False, True])
      c) all([1, 2, 3])
      d) any(["", 0, None])
      e) all([])
      f) any([])
      g) all("abc")

20. Une liste de températures est donnée. Avec all() ou any() :
      a) affichez s'il a gelé au moins une fois (température < 0) ;
      b) affichez si toutes les températures sont "raisonnables"
         (entre -50 et 60).
        temperatures = [12, 5, -2, 8, 15]

21. Écrivez une fonction mot_de_passe_valide(mdp) qui retourne True si le
    mot de passe contient au moins 8 caractères, au moins un chiffre et au
    moins une majuscule (utilisez any(), une boucle et les méthodes
    .isdigit() et .isupper(), cf. chap. 8).
"""


##############################
#  Les opérateurs bit à bit  #
##############################

"""
22. Sans exécuter, que valent ces expressions ? (Posez le calcul en binaire.)
      a) 0b1100 & 0b1010
      b) 0b1100 | 0b1010
      c) 0b1100 ^ 0b1010
      d) 5 << 2
      e) 40 >> 3
      f) ~7

23. Sans exécuter, qu'affiche ce programme ? Pourquoi ? Corrigez-le.
        x = 10
        if x > 1 & x < 5:
            print("x est entre 1 et 5")

24. Les droits d'un fichier sous Linux sont stockés sur 3 bits : lecture = 4
    (0b100), écriture = 2 (0b010), exécution = 1 (0b001).
      a) Construisez avec "|" la valeur des droits "lecture + exécution".
      b) Avec "&", testez si les droits 6 permettent l'écriture, puis
         l'exécution.
      c) Avec "^", retirez le droit d'écriture des droits 7.
"""
