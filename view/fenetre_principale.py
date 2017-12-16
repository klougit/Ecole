import sys
sys.path.append('.\\classes')
from regle import *
from listeregle import *
import fenetre_creer


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

class FenetrePrincipale():
    def __init__(self):
        self.fenetre_principale = Tk()
        self.fenetre_principale.resizable(width=False, height=False)
        self.fenetre_principale.title("Renommage fichier")
        self.menu()
        self.main_window()
        self.geom_fen(1050, 450)
        self.fenetre_principale.mainloop()

    def geom_fen(self, larg, haut):
        if self.fenetre_principale.winfo_screenwidth() < 1920:
            larg *= 0.8
            haut *= 0.8
        self.fenetre_principale.geometry(
            "%dx%d%+d%+d" % (larg, haut, (self.fenetre_principale.winfo_screenwidth() - larg) // 2,
                             (self.fenetre_principale.winfo_screenheight() - haut) // 2))

    # def faireApparaitreLeToplevel():
    #     top = Toplevel(self.fenetre_principale)
    #     top.title("coucou")
    #
    #     lab = Label(top, text="Ce soir je vais manger des frites")
    #     lab.pack()

    def menu(self):
        main_menu = Menu(self.fenetre_principale)
        roll_menu = Menu(main_menu, tearoff=0)                              # Menu déroulant
        roll_menu.add_command(label="Lister")#, command=self.faireApparaitreLeToplevel)     # Option lister, renvoie sur une fenêtre listant les règles
        roll_menu.add_command(label="Créer")#, command=self.create_window)    # Option créer, renvoie sur une fenêtre de creation

        help_menu = Menu(main_menu, tearoff=0)  # Menu Fils
        help_menu.add_command(label="À propos")#, command=self.help)

        main_menu.add_cascade(label="Règles", menu=roll_menu)
        main_menu.add_cascade(label="?", menu=help_menu)

        self.fenetre_principale.config(menu=main_menu)

    # @staticmethod
    # def create_window():
    #     FenetreCreer()

    def main_window(self):
        ### Label ###
        # title_lab = Label(self, text="Renommer en lot").grid(row=0, column=2)
        Label(self.fenetre_principale, text="Nom de répertoire").grid(row=1, column=1)
        Label(self.fenetre_principale, text="Amorce").grid(row=3, column=0, pady=10)
        Label(self.fenetre_principale, text="Prefixe").grid(row=3, column=1)
        Label(self.fenetre_principale, text="Nom du fichier").grid(row=3, column=2)
        Label(self.fenetre_principale, text="Postfixe").grid(row=3, column=3)
        Label(self.fenetre_principale, text="Extension concernée").grid(row=3, column=4)
        Label(self.fenetre_principale, text="A partir de : ").grid(row=5, column=0, pady=10)

        ### Picture ####
        picture = PhotoImage(file="./data/Rename.gif")
        label1 = Label(self.fenetre_principale, image=picture)
        label1.image = picture
        label1.grid(row=1, column=5)

        ### Entry ###
        self.nomrep = StringVar()
        Entry(self.fenetre_principale, textvariable=self.nomrep).grid(row=1, column=2)

        self.prefix = StringVar()
        Entry(self.fenetre_principale, textvariable=self.prefix).grid(row=4, column=1, padx=15)

        self.nom_fich = StringVar()
        Entry(self.fenetre_principale, textvariable=self.nom_fich).grid(row=4, column=2, padx=15)

        self.apartirde = StringVar()
        Entry(self.fenetre_principale, textvariable=self.apartirde).grid(row=6, column=0, padx=15)

        self.postfix = StringVar()
        Entry(self.fenetre_principale, textvariable=self.postfix).grid(row=4, column=3, padx=15)

        self.ext = StringVar()
        Entry(self.fenetre_principale, textvariable=self.ext).grid(row=4, column=4, padx=15)

        ### Combobox ###
        self.amorce_select = StringVar()
        amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
        Combobox(self.fenetre_principale, textvariable=self.amorce_select,
                               values=amorce_choice, state='readonly').grid(row=4, column=0, padx=15)
        self.amorce_select.set(amorce_choice[0])

        ### Button ###
        Button(self.fenetre_principale, text="Renommer").grid(row=6, column=4)

fen = FenetrePrincipale()