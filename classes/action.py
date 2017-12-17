from regle import *
import re
import os


class Action:

    def __init__(self, regle, nom_rep):
        """
            Constructeur de l'objet Action
            :param regle: attends un objet Regle en entrée
            :param nom_rep: attends un chemin en entrée
        """
        self.nom_rep = nom_rep
        self.regle = regle

    def get_nom_rep(self):
        return self.nom_rep

    def set_nom_rep(self, valeur):
        self.nom_rep = valeur

    def get_regle(self):
        return self.regle

    def set_regle(self, valeur):
        self.regle = valeur

    def __str__(self):
        return self.nom_du_rep + self.regle

    def simulation(self):
        nom_original = []
        nom_modifie = []                           #Listes permettant à stocker les noms
        amm = str(self.regle.apartirde)                  #ammorce initiale
        if self.regle.extension == "":
            for fichier in os.listdir(self.nom_rep):     #Parcours du dossier
                nom_original.append(fichier)                #Stockage des noms de fichier dans la liste nom_original
                nom_complet = fichier.split(".")            #nom du fichier splité
                extension = nom_complet[1]                  #nom de l'extension dans la variable extension
                if self.regle.nom_fichier != "":
                    nom = self.regle.nom_fichier
                else:                               #permet de remplacer ou nom par nom_fichier en fonctions des options
                    nom = nom_complet[0]
                if self.regle.amorce == "Aucune":            #Instructions si il n'y a pas d'ammorce
                    nom_modifie.append(self.regle.prefixe+nom+self.regle.postfixe+"."+extension)     #population de la liste "nom_modifier"


                else:
                    if self.regle.amorce == "Chiffres":
                        self.regle.apartirde = int(self.regle.apartirde)
                        nom_modifie.append(str(self.regle.apartirde) + self.regle.prefixe + nom+self.regle.postfixe + "." + extension)
                        self.regle.apartirde += 1            #instructions si il y'a une ammorce (CHiffre ou lettre)
                    elif self.regle.amorce == "Lettres":
                        nom_modifie.append(amm + self.regle.prefixe + nom + self.regle.postfixe + "." + extension)
                        amm = incrementation_char(amm)             #appel à la fonction "incrementation_char" qui permet d'incrementer lettres
        else:
            for fichier in os.listdir(self.nom_rep):
                bool = False
                bool2 = False
                nom_original.append(fichier)
                nom_complet = fichier.split(".")
                extension = nom_complet[1]
                if self.regle.nom_fichier != "":
                    nom = self.regle.nom_fichier
                else:                               #Remplace ou non par nom_fichier en fonctions des options
                    nom = nom_complet[0]
                for i in self.regle.extension.split(","):
                    if ("."+extension) == i:
                        bool2 = True            #Previens que l'extension à bien matché avec AU MOINS une des extensions spécifiées
                        if self.regle.amorce == "Aucune":
                            nom_modifie.append(self.regle.prefixe+nom+self.regle.postfixe+"."+extension)
                        else:
                            if self.regle.amorce == "Chiffres":
                                self.regle.apartirde = int(self.regle.apartirde)
                                nom_modifie.append(str(self.regle.apartirde) + self.regle.prefixe + nom + self.regle.postfixe + "."+ extension)
                                self.regle.apartirde += 1
                            elif self.regle.amorce == "Lettres":
                                nom_modifie.append(amm + self.regle.prefixe + nom + self.regle.postfixe + "." + extension)
                                amm = incrementation_char(amm)
                    else:
                        bool = True
                if bool == True and bool2 == False:             #Vérification droit de création sinon suppresion
                    nom_original.remove(fichier)
        return nom_original, nom_modifie


def incrementation_char(text, chlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Permet l'incrémentation d'une variable de type string
    :param text: La lettre à incrémenter
    :param chlist: spécifie les caractéristique de la lettre (Majuscule ou miniscule)
    :return:
    """
    chlist = ''.join(sorted(set(str(chlist))))
    chlen = len(chlist)
    if not chlen:
        return ''
    text = str(text)
    text = re.sub('[^' + chlist + ']', '', text)
    if not len(text):
        return chlist[0]
    #Incrementation
    inc = ''
    over = False
    for i in range(1, len(text)+1):
        lchar = text[-i]
        pos = chlist.find(lchar) + 1
        if pos < chlen:
            inc = chlist[pos] + inc
            over = False
            break
        else:
            inc = chlist[0] + inc
            over = True
    if over:
        inc += chlist[0]
    result = text[0:-len(inc)] + inc
    return result
