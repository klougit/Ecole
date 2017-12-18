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
        """
            Methode permettant la sauvegarde d'une regle passee en parametre
        :param regle:
        :return:
        """
        fichier = open("./Modeles/regles.ini", "a")
        saved = str(regle).replace(" ", ";")
        print(saved, file=fichier)
        fichier.close()

    def charger(self):
        """
            Methode permettant de charger les regles contenues dans regles.ini
        :return:
        """
        fichier = open("./Modeles/regles.ini", "r")
        mon_fichier = fichier.readlines()
        for ligne in mon_fichier:
            t = ligne.replace("\n", "").split(";")
            self.regles.append(Regle(t[0], t[1], t[2], t[3], t[4], t[5], t[6]))
            fichier.close()

    def __str__(self):
        liste_regle = ""
        for rule in self.regles:
            liste_regle = liste_regle + str(rule) + "\n"
        return liste_regle
