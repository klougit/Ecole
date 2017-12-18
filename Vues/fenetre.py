import sys
sys.path.append('.\\Controlleurs')
from regle import *
from listeregle import *
from renommage import *
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox


class MaFenetre(Tk):
    def __init__(self):
        super(MaFenetre, self).__init__()
        self.geom_fen(1050, 450)
        self.resizable(width=False, height=False)
        self.menu()
        self.main_window()
        self.mainloop()

    def geom_fen(self, larg, haut):
        """
            Permet de dimensionner la fenetre en fonction de la résolution, et de la centrer
        :param larg: Largeur de la fenetre générée
        :param haut: Hauteur de la fenetre générée
        :return:
        """
        if self.winfo_screenwidth() < 1920:
            larg *= 0.8
            haut *= 0.8
        self.geometry(
            "%dx%d%+d%+d" % (larg, haut, (self.winfo_screenwidth() - larg) // 2,
                             (self.winfo_screenheight() - haut) // 2))

    def menu(self):
        """
            Menu de la fenetre, contenant Regle>Lister>Creer et ?>A propos
        """
        main_menu = Menu(self)
        roll_menu = Menu(main_menu, tearoff=0)                               # Menu déroulant
        roll_menu.add_command(label="Lister", command=self.window_liste)     # Option lister, renvoie sur une fenêtre listant les règles
        roll_menu.add_command(label="Créer", command=self.window_creer)       # Option créer, renvoie sur une fenêtre de creation

        help_menu = Menu(main_menu, tearoff=0)
        help_menu.add_command(label="À propos", command=self.help)

        main_menu.add_cascade(label="Règles", menu=roll_menu)
        main_menu.add_cascade(label="?", menu=help_menu)

        self.config(menu=main_menu)

    def main_window(self):
        """
            Fenetre principale permettant de renommer des fichiers d'un dossier en fonction des parametre mit dans les champs
        """
        self.title("Renommage de fichier")
        ### Label ###
        title_lab = Label(self, text="Renommer en lot").grid(row=0, column=2)
        Label(self, text="Nom de répertoire").grid(row=1, column=1)
        Label(self, text="Amorce").grid(row=3, column=0, pady=10)
        Label(self, text="Prefixe").grid(row=3, column=1)
        Label(self, text="Nom du fichier").grid(row=3, column=2)
        Label(self, text="Postfixe").grid(row=3, column=3)
        Label(self, text="Extension concernée").grid(row=3, column=4)
        Label(self, text="A partir de : ").grid(row=5, column=0, pady=10)

        ### Picture ###
        picture = PhotoImage(file="./Modeles/Rename.gif")
        label1 = Label(self, image=picture)
        label1.image = picture
        label1.grid(row=1, column=5)

        ### Entry ###
        self.prefix = StringVar()
        Entry(self, textvariable=self.prefix).grid(row=4, column=1, padx=15)

        self.nom_fich = StringVar()
        Entry(self, textvariable=self.nom_fich).grid(row=4, column=2, padx=15)

        self.apartirde = StringVar()
        Entry(self, textvariable=self.apartirde).grid(row=6, column=0, padx=15)

        self.postfix = StringVar()
        Entry(self, textvariable=self.postfix).grid(row=4, column=3, padx=15)

        self.ext = StringVar()
        Entry(self, textvariable=self.ext).grid(row=4, column=4, padx=15)

        ### Combobox ###
        self.amorce_select = StringVar()
        amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
        Combobox(self, textvariable=self.amorce_select,
                               values=amorce_choice, state='readonly').grid(row=4, column=0, padx=15)
        self.amorce_select.set(amorce_choice[0])

        ### Button ###
        Button(self, text="Browse", command= self.browse).grid(row=1, column=2)
        Button(self, text="Renommer", command=self.renommer_fichiers).grid(row=6, column=4)

    def renommer_fichiers(self):
        """
            Methode permettant de renommer avec la regle passee
        """
        nomrep = self.file_path
        amorce = self.amorce_select.get()
        a_partir_de = self.apartirde.get()
        prefixe = self.prefix.get()
        nom_fichier = self.nom_fich.get()
        postfixe = self.postfix.get()
        extension = self.ext.get()
        ma_regle = Regle(" ", amorce, a_partir_de, prefixe, nom_fichier, postfixe, extension)
        rename = Renommage(ma_regle, nomrep)
        rename.renommer(rename)

    def window_creer(self):
        """
            Fenetre associee a la creation de regle
        """
        win_creer = Toplevel(self)
        win_creer.geometry(
            "%dx%d%+d%+d" % (1050, 450, (self.winfo_screenwidth() - 1050) // 2,
                             (self.winfo_screenheight() - 450) // 2))
        win_creer.title("Création nouvelle règle")
        Label(win_creer, text="Nom de règle").grid(row=1, column=1)
        Label(win_creer, text="Amorce").grid(row=3, column=0, pady=10)
        Label(win_creer, text="Prefixe").grid(row=3, column=1)
        Label(win_creer, text="Nom du fichier").grid(row=3, column=2)
        Label(win_creer, text="Postfixe").grid(row=3, column=3)
        Label(win_creer, text="Extension concernée").grid(row=3, column=4)
        Label(win_creer, text="A partir de : ").grid(row=5, column=0, pady=10)

        ## Picture ####
        # picture = PhotoImage(file="./Modeles/New-Rule.gif")
        # label1 = Label(self.frame, image=picture)
        # label1.image = picture
        # label1.grid(row=1, column=5)

        ### Entry ###
        self.nomregle = StringVar()
        Entry(win_creer, textvariable=self.nomregle).grid(row=1, column=2)
        self.prefix = StringVar()
        Entry(win_creer, textvariable=self.prefix).grid(row=4, column=1, padx=15)
        self.apartirde = StringVar()
        Entry(win_creer, textvariable=self.apartirde).grid(row=6, column=0, padx=15)
        self.postfix = StringVar()
        Entry(win_creer, textvariable=self.postfix).grid(row=4, column=3, padx=15)
        self.nom_fich = StringVar()
        Entry(win_creer, textvariable=self.nom_fich).grid(row=4, column=2, padx=15)
        self.ext = StringVar()
        Entry(win_creer, textvariable=self.ext).grid(row=4, column=4, padx=15)

        ### Combobox ###
        self.amorce_select = StringVar()
        amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
        Combobox(win_creer, textvariable=self.amorce_select,
                 values=amorce_choice, state='readonly').grid(row=4, column=0, padx=15)
        self.amorce_select.set(amorce_choice[0])

        ### Button ###
        Button(win_creer, text="Créer", command=self.creer_nouvelle_regle).grid(row=6, column=4)

    def creer_nouvelle_regle(self):
        """
            Methode créant une nouvelle regle via methode sauvegarder de ListeRegle en recuperant les données des champs de texte
        """
        nomrep = self.nomregle.get()
        amorce = self.amorce_select.get()
        apartirde = self.apartirde.get()
        prefixe = self.prefix.get()
        nomfich = self.nom_fich.get()
        postfixe = self.postfix.get()
        ext = self.ext.get()
        ma_regle = Regle(nomrep, amorce, apartirde, prefixe, nomfich, postfixe, ext)
        ma_liste = ListeRegle()
        ma_liste.sauvegarder(ma_regle)
        messagebox.showinfo("Ok","Règle " + nomrep + " créée")

    def window_liste(self):
        """
            Fenetre associee a la selection de regles existantes
        """
        win_liste = Toplevel(self)
        win_liste.geometry(
            "%dx%d%+d%+d" % (1050, 450, (self.winfo_screenwidth() - 1050) // 2,
                             (self.winfo_screenheight() - 450) // 2))
        win_liste.title("Liste des règles")
        liste_regle = ListeRegle()
        liste_regle.charger()
        regles = liste_regle.get_regle()
        noms_regles = []
        for i in regles:
            noms_regles.append(str(i).split(" ")[0])
        ### Combobox ###
        self.amorce_select = StringVar()
        Combobox(win_liste, textvariable=self.amorce_select,
                 values=noms_regles, state='readonly').grid(row=0, column=0)
        self.amorce_select.set(noms_regles[0])
        ### Button ###
        Button(win_liste, text="valider", command=self.previsu_selection).grid(row=1, column=0)

    def previsu_selection(self):
        """
            Fenetre associee à la previsualisation d'une regle selectionnee
        """
        win_liste_select = Toplevel(self)
        win_liste_select.geometry(
            "%dx%d%+d%+d" % (1050, 450, (self.winfo_screenwidth() - 1050) // 2,
                             (self.winfo_screenheight() - 450) // 2))
        am = self.amorce_select.get()
        nom_regle = am.split(" ")[0]
        amorce = am.split(" ")[1]
        apartirde = am.split(" ")[2]
        prefixe = am.split(" ")[3]
        nom_fichier = am.split(" ")[4]
        postfixe = am.split(" ")[5]
        ext = am.split(" ")[6]

        ### Label ###
        Label(win_liste_select, text="Nom de règle").grid(row=1, column=1)
        Label(win_liste_select, text="Amorce").grid(row=3, column=0, pady=10)
        Label(win_liste_select, text="Prefixe").grid(row=3, column=1)
        Label(win_liste_select, text="Nom du fichier").grid(row=3, column=2)
        Label(win_liste_select, text="Postfixe").grid(row=3, column=3)
        Label(win_liste_select, text="Extension concernée").grid(row=3, column=4)
        Label(win_liste_select, text="A partir de : ").grid(row=5, column=0, pady=10)

        ## Picture ####
        # picture = PhotoImage(file="./Modeles/New-Rule.gif")
        # label1 = Label(self.frame, image=picture)
        # label1.image = picture
        # label1.grid(row=1, column=5)

        ## Entry ###
        self.nomR = Entry(win_liste_select)
        self.nomR.grid(row=1, column=2)
        self.nomR.insert(0, nom_regle)

        self.amorce = Entry(win_liste_select)
        self.amorce.grid(row=4, column=0)
        self.amorce.insert(0, amorce)

        self.apart = Entry(win_liste_select)
        self.apart.grid(row=6, column=0, padx=15)
        self.apart.insert(0, apartirde)

        self.prefixe = Entry(win_liste_select)
        self.prefixe.grid(row=4, column=1, padx=15)
        self.prefixe.insert(0, prefixe)

        self.nomFichier = Entry(win_liste_select)
        self.nomFichier.grid(row=4, column=2, padx=15)
        self.nomFichier.insert(0, nom_fichier)

        self.postfixe = Entry(win_liste_select)
        self.postfixe.grid(row=4, column=3)
        self.postfixe.insert(0, postfixe)

        self.extens = Entry(win_liste_select)
        self.extens.grid(row=4, column=4)
        self.extens.insert(0, ext)
        Button(win_liste_select, text="choisir", command=self.regle_choisie).grid(row=6, column=4)

    def regle_choisie(self):
        """
            Fenetre associee a la regle choisie dans la liste afin de renommer en fonction de celle-ci
        """
        win_regle_choisie = Toplevel(self)
        win_regle_choisie.geometry(
            "%dx%d%+d%+d" % (1050, 450, (self.winfo_screenwidth() - 1050) // 2,
                             (self.winfo_screenheight() - 450) // 2))
        win_regle_choisie.title("Renommage de fichier")
        # Label
        Label(win_regle_choisie, text="Renommer en lot").grid(row=0, column=2)
        Label(win_regle_choisie, text="Nom de répertoire").grid(row=1, column=1)
        Label(win_regle_choisie, text="Amorce").grid(row=3, column=0, pady=10)
        Label(win_regle_choisie, text="Prefixe").grid(row=3, column=1)
        Label(win_regle_choisie, text="Nom du fichier").grid(row=3, column=2)
        Label(win_regle_choisie, text="Postfixe").grid(row=3, column=3)
        Label(win_regle_choisie, text="Extension concernée").grid(row=3, column=4)
        Label(win_regle_choisie, text="A partir de : ").grid(row=5, column=0, pady=10)

        # Picture
        picture = PhotoImage(file="./Modeles/Rename.gif")
        label1 = Label(win_regle_choisie, image=picture)
        label1.image = picture
        label1.grid(row=1, column=5)

        # Entry
        self.nom_dossier = StringVar()
        Entry(win_regle_choisie, textvariable=self.nom_dossier).grid(row=1, column=2)

        amorce = Entry(win_regle_choisie)
        amorce.grid(row=4, column=0, padx=15)
        amorce.insert(0,self.amorce.get())

        prefixe = Entry(win_regle_choisie)
        prefixe.grid(row=4, column=1, padx=15)
        prefixe.insert(0, self.prefixe.get())

        nom_fich = Entry(win_regle_choisie)
        nom_fich.grid(row=4, column=2, padx=15)
        nom_fich.insert(0, self.nomFichier.get())

        apartirde = Entry(win_regle_choisie)
        apartirde.grid(row=6, column=0, padx=15)
        apartirde.insert(0, self.apart.get())

        postfixe = Entry(win_regle_choisie)
        postfixe.grid(row=4, column=3, padx=15)
        postfixe.insert(0, self.postfixe.get())

        extension = Entry(win_regle_choisie)
        extension.grid(row=4, column=4, padx=15)
        extension.insert(0, self.extens.get())

        ### Button ###
        Button(win_regle_choisie, text="Renommer", command=self.renommer_fichers_regle_choisie).grid(row=6, column=4)

    def renommer_fichers_regle_choisie(self):
        """
            Methode permettant de renommer des fichiers après la selection d'une regle sauvegardee et selectionnee
        """
        nomrep = self.nom_dossier.get()
        amorce = self.amorce.get()
        a_partir_de = self.apart.get()
        prefixe = self.prefixe.get()
        nom_fichier = self.nomFichier.get()
        postfixe = self.postfixe.get()
        extension = self.extens.get()
        ma_regle2 = Regle(self.nomR.get(), amorce, a_partir_de, prefixe, nom_fichier, postfixe, extension)
        rename = Renommage(ma_regle2, nomrep)
        rename.renommer(rename)

    def browse(self):
        """
            Methode permettant de choisir quel dossier selectionner pour le rename
        """
        self.file_path = filedialog.askdirectory()

    @staticmethod
    def help():
        """
            Popup a propos :
        """
        messagebox.showinfo("À propos", "Créé par Quentin Nicolas\nVersion 1.0")


fen = MaFenetre()

# if __name__ == '__main__':
#     app = MyWindow("Renommage fichier")
#     app.mainloop()
#     app.quit()