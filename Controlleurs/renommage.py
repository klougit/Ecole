from os import *
from tkinter import messagebox
from action import *
from regle import *


class Renommage(Action):
    def __init__(self, regle, nom_rep):
        Action.__init__(self, regle, nom_rep)

    @staticmethod
    def retourne_liste(liste):
        """
            Methode permettant de stringifier la liste passee en parametre
        :param liste: Entrer une liste a stringifier
        :return: liste stringifiee
        """
        liste_propre = ""
        for element in liste:
            liste_propre = liste_propre + element + "\n"
        return liste_propre

    def renommer(self, objet):
        """
            Effectue l'action de renommage selon les regles. Utilise le resultat de objet.simulation()
        """
        original, modifie = objet.simulation()
        result = messagebox.askokcancel("Etes-vous sûr?", "Après renommage:\n"+self.retourne_liste(modifie), icon='warning')
        if result is True:  #Si user clique sur OK
            for element in os.listdir(self.nom_rep):
                for i in range(0, len(original)):
                    if element == original[i]:
                        os.rename(self.nom_rep + "/" + element, self.nom_rep + "/" + modifie[i]) #rennomage du fichier
        else:
            messagebox.showinfo("Annulé", "Renommage annulé")
