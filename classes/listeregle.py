from regle import *


class ListeRegle:

    def __init__(self):
        regles = []
        self.regles = regles

    def get_regle(self):
        return self.regles

    def set_regles(self, valeur):
        self.regles = valeur

    def sauvegarder(self, regle):
        fichier = open("./files/regles.ini", "a")
        saved = str(regle).replace(" ", ";")
        print(saved, file=fichier)
        fichier.close()

    def charger(self):
        """
        Permet de charger les reglès extraites depuis le fichier txt regles.ini
        :return:
        """
        fichier = open("./files/regles.ini", "r")
        mon_fichier = fichier.readlines()   #On lit les lignes du fichier une a une
        for ligne in mon_fichier:           #on affecte, une par une, chaque valeur du fichier à ligne
            t = ligne.replace("\n", "").split(";")  #on créer une liste T qui prend chaque caractéristique de la regle
            self.regles.append(Regle(t[0], t[1], t[2], t[3], t[4], t[5], t[6]))
            fichier.close()

    def __str__(self):
        liste_regle = ""
        for rule in self.regles:
            liste_regle = liste_regle + str(rule) + "\n"
        return liste_regle

#(self, nom_regle, amorce, apartirde, prefixe, nom_fichier(none ou quelque chose), postfixe, extension(none ou liste):

# O = Regle("Regle_numero_1","Lettre","A","bon",None,"az",None)
# B = Regle("Regle_numero_2","Chiffre","1","bete","DEBEBOM","izi",".txt,.pdf")
# R = ListeRegle()
# R.sauvegarder(B)
# R.charger()
# print(R)


