from action import *
from regle import *
from os import *

class Renommage(Action):        #Classe renommage hérite d'Action
    def __init__(self, regle):
        Action.__init__(self, regle)    #On récupère les attributs de la classe mere

    def rennommer(self):
        """
        Effectue l'action de renommage selon les regles. Utilise le resultat de objet.simulate()
        :return:
        """

        t = toto.simulate()        #T recupère un tuple contenant la liste des fichier originelle et celle obtenue après modification
        print(t)
        modif = t[0]
        orig = t[1]             #Affectation de chaque valeur du tuple à une variable
        check = input("Voulez vous proceder a ces renommages ? (Entree pour OUI, n'importe quelle touche pour NON): ")
        if check is "":
            for element in os.listdir(self.nom_du_rep):     #on parcours le repertoire "nom_du_rep"
                for i in range(0, len(orig)):               #pour chaqe fichier on parcours la liste "orig"
                    if element == orig[i]:                  #comparaison d'un fichier avec son emplacement dans la liste orig
                        os.rename(self.nom_du_rep + "/" + element, self.nom_du_rep + "/" + modif[i]) #rennomage du fichier
            print ("Répertoire après modification")
            for element2 in os.listdir(self.nom_du_rep):
                print(element2)    #Affichage du répertoire une fois le rennomage effectué
        else:
            print("Operation annulée")

O = Regle("Regle numero 1","Lettre","A","bon","Coucou","az",None)
toto = Renommage(O)
toto.rennommer()



