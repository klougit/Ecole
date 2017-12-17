from action import *
from regle import *
from os import *
from tkinter import *
from tkinter import messagebox

class Renommage(Action):        #Classe renommage hérite d'Action
    def __init__(self, regle, nom_rep):
        Action.__init__(self, regle, nom_rep)    #On récupère les attributs de la classe mere

    @staticmethod
    def retourne_liste(liste):
        liste_propre = ""
        for element in liste:
            liste_propre = liste_propre + element + "\n"
        return liste_propre

    def renommer(self, objet):
        """
        Effectue l'action de renommage selon les regles. Utilise le resultat de objet.simulate()
        :return:
        """

        t = objet.simulate()        #T recupère un tuple contenant la liste des fichier originelle et celle obtenue après modification
        modif = t[0]
        orig = t[1]             #Affectation de chaque valeur du tuple à une variable
        # check = input("Voulez vous proceder a ces renommages ? (Entree pour OUI, n'importe quelle touche pour NON): ")
        result = messagebox.askokcancel("Etes-vous sûr?", "Après renommage:\n", icon='warning')
        if result is True:
            for element in os.listdir(self.nom_du_rep):     #on parcours le repertoire "nom_du_rep"
                for i in range(0, len(orig)):               #pour chaqe fichier on parcours la liste "orig"
                    if element == orig[i]:                  #comparaison d'un fichier avec son emplacement dans la liste orig
                        os.rename(self.nom_du_rep + "/" + element, self.nom_du_rep + "/" + modif[i]) #rennomage du fichier
            print ("Répertoire après modification")
            for element2 in os.listdir(self.nom_du_rep):
                print(element2)    #Affichage du répertoire une fois le rennomage effectué
        else:
            print("Operation annulée")

# O = Regle("Regle numero 1","Lettre","A","bon","Coucou","az",None)
# toto = Renommage(O)
# toto.renommer()



