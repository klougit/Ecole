from action import *
from regle import *
from os import *
from tkinter import messagebox


class Renommage(Action):
    def __init__(self, regle, nom_rep):
        Action.__init__(self, regle, nom_rep)

    @staticmethod
    def retourne_liste(liste):
        liste_propre = ""
        for element in liste:
            liste_propre = liste_propre + element + "\n"
        return liste_propre

    def renommer(self, objet):
        """
        Effectue l'action de renommage selon les regles. Utilise le resultat de objet.simulation()
        :return:
        """

        original, modifie = objet.simulation()        #On recupère un tuple contenant la liste des fichier originelle et celle obtenue après modification
        result = messagebox.askokcancel("Etes-vous sûr?", "Après renommage:\n"+self.retourne_liste(modifie), icon='warning')
        if result is True:
            for element in os.listdir(self.nom_rep):     #on parcours le repertoire "nom_rep"
                for i in range(0, len(original)):               #pour chaqe fichier on parcours la liste "orig"
                    if element == original[i]:                  #comparaison d'un fichier avec son emplacement dans la liste orig
                        os.rename(self.nom_rep + "/" + element, self.nom_du_rep + "/" + modifie[i]) #rennomage du fichier
            print ("Répertoire après modification")
            for element2 in os.listdir(self.nom_rep):
                print(element2)    #Affichage du répertoire une fois le rennomage effectué
        else:
            print("Operation annulée")

# O = Regle("Regle numero 1","Lettre","A","bon","Coucou","az",None)
# toto = Renommage(O)
# toto.renommer()
