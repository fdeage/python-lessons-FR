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
#  Chap. 34     #  POO I : exercices                                           #
#               #                                                              #
################################################################################

"""
Écrivez votre réponse sous chaque énoncé, puis exécutez le fichier pour
vérifier. Pour les exercices "sans exécuter", déroulez le programme dans votre
tête (cf. chap. 1) en notant, pour chaque objet, la valeur de ses attributs.

Les corrigés sont dans le fichier corrs/corr_34_poo_1.py.
"""


###############################
#  En Python, tout est objet  #
###############################

"""
1. Sans exécuter, qu'affichent ces lignes ? Vérifiez ensuite.
       print(type(3.0))
       print(type(None))
       print(type(len))
       print(isinstance(True, int))

2. Les lignes suivantes appellent des méthodes. Pour chacune, dites sur quel
   objet la méthode est appelée, et si elle MODIFIE cet objet ou RETOURNE un
   nouvel objet :
       mots = ["b", "a"]
       mots.sort()
       nom = "ada"
       nom.capitalize()
"""


##########################
#  Classe et instance    #
##########################

"""
3. Dans chaque paire, dites lequel est la classe et lequel est l'instance :
       a) str  /  "bonjour"
       b) [3, 1, 2]  /  list
       c) le plan d'une voiture  /  la voiture garée devant chez vous

4. Créez une classe vide Velo. Créez deux instances v1 et v2, donnez à v1 un
   attribut couleur = "rouge". Que se passe-t-il si vous affichez v2.couleur ?
   (Protégez la ligne avec un try/except, cf. chap. 26.)
"""


################################
#  __init__, self, attributs   #
################################

"""
5. Écrivez une classe Personne dont le constructeur reçoit un prenom et un
   age, et les stocke dans des attributs du même nom. Créez deux personnes et
   affichez leur prénom et leur âge.

6. Sans exécuter, trouvez les DEUX erreurs dans cette classe, et dites quel
   message d'erreur on obtiendrait :
       class Livre:
           def __init__(titre, auteur):
               self.titre = titre
               auteur = auteur

       l = Livre("Germinal", "Zola")
       print(l.auteur)

7. Écrivez une classe Point3D avec trois attributs x, y, z, qui valent 0 par
   défaut. Créez l'origine, puis le point (1, 2, 3), puis le point dont seul
   z vaut 5 (utilisez un argument nommé).

8. Sans exécuter, qu'affiche ce programme ?
       class Boite:
           def __init__(self, contenu):
               self.contenu = contenu

       b1 = Boite("pommes")
       b2 = Boite("poires")
       b1.contenu = "cerises"
       print(b1.contenu, b2.contenu)
       print(b1.__dict__)
"""


##################
#  Les méthodes  #
##################

"""
9. Ajoutez à la classe Personne (exercice 5) :
     - une méthode se_presenter() qui RETOURNE "Bonjour, je suis <prenom>." ;
     - une méthode est_majeur() qui retourne True si l'âge est >= 18 ;
     - une méthode feter_anniversaire() qui augmente l'âge de 1.
   Testez-les.

10. Écrivez une classe Cercle, construite à partir de son rayon, avec deux
    méthodes aire() et perimetre() (prenez pi = 3.14159, ou math.pi,
    cf. chap. 22). Ajoutez une méthode agrandir(facteur) qui multiplie le
    rayon par facteur.

11. Réécrivez l'appel c.aire() sous sa forme "longue", Cercle.aire(c), et
    vérifiez que le résultat est identique. Expliquez en une phrase ce que
    Python fait de "c".

12. Écrivez une classe Compteur avec un attribut valeur (0 au départ) et trois
    méthodes : incrementer(), decrementer() (qui ne descend jamais sous 0) et
    reinitialiser(). Faites-la compter le nombre de voyelles du mot
    "anticonstitutionnellement" (une boucle et un appel à incrementer()
    par voyelle).
"""


###################################################
#  Attributs de classe et attributs d'instance    #
###################################################

"""
13. Sans exécuter, qu'affiche ce programme ? Expliquez la 3e ligne affichée.
        class Robot:
            nb_robots = 0
            def __init__(self, nom):
                self.nom = nom
                Robot.nb_robots += 1

        r1 = Robot("R2")
        r2 = Robot("C3")
        print(Robot.nb_robots)
        r1.nb_robots = 100
        print(Robot.nb_robots, r1.nb_robots, r2.nb_robots)

14. Cette classe contient un bug. Sans exécuter, qu'affiche la dernière ligne ?
    Corrigez la classe.
        class Panier:
            articles = []
            def ajouter(self, article):
                self.articles.append(article)

        p1 = Panier()
        p2 = Panier()
        p1.ajouter("pain")
        print(p2.articles)
"""


##############################
#  __str__ et __repr__       #
##############################

"""
15. Ajoutez à la classe Cercle une méthode __str__ qui retourne par exemple
    "Cercle de rayon 2", et une méthode __repr__ qui retourne "Cercle(2)".
    Affichez un cercle avec print(), puis une liste de deux cercles.

16. Sans exécuter, qu'affichent les deux print() ?
        class Mot:
            def __init__(self, texte):
                self.texte = texte
            def __repr__(self):
                return f"Mot({self.texte!r})"

        m = Mot("python")
        print(m)
        print([m, Mot("java")])
"""


####################################
#  Objets mutables et références   #
####################################

"""
17. Sans exécuter, qu'affiche ce programme ?
        class Jauge:
            def __init__(self):
                self.niveau = 0

        def remplir(j):
            j.niveau = 10

        a = Jauge()
        b = a
        remplir(b)
        c = Jauge()
        print(a.niveau, b.niveau, c.niveau)
        print(a is b, a == c)
"""


##############
#  Synthèse  #
##############

"""
18. Écrivez une classe Inventaire qui gère le stock d'un petit magasin :
      - un attribut stock : dictionnaire produit -> quantité, vide au départ ;
      - ajouter(produit, quantite) : ajoute au stock (crée le produit s'il
        n'existe pas) ;
      - retirer(produit, quantite) : lève une ValueError (cf. chap. 26) si la
        quantité disponible est insuffisante, sinon retire du stock ;
      - total() : retourne le nombre total d'articles ;
      - __str__ : une ligne par produit, triée par ordre alphabétique, par
        exemple "pommes : 12".
    Testez avec quelques produits, et un retrait impossible (dans un try).

19. Écrivez une classe Statistiques construite à partir d'une liste de
    nombres, avec les méthodes moyenne(), minimum(), maximum(), etendue()
    (= max - min) et ecart_type() (racine carrée de la moyenne des carrés des
    écarts à la moyenne). Testez-la sur les températures
    [12.5, 14.0, 9.5, 11.0, 13.0].
"""
