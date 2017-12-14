import sys
sys.path.append('.\\classes')
from regle import *

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


class MyWindow(Tk):
    def __init__(self, title):
        super(MyWindow, self).__init__()
        self.resizable(width=False, height=False)
        # self.title(title)
        self.main_window()
        self.menu()
        self.geom_fen(1050, 450)

    def geom_fen(self, larg, haut):
        if self.winfo_screenwidth() < 1920:
            larg *= 0.8
            haut *= 0.8
        self.geometry(
            "%dx%d%+d%+d" % (larg, haut, (self.winfo_screenwidth() - larg) // 2,
                             (self.winfo_screenheight() - haut) // 2))




    def test(self):
        nomrep = self.nomrep.get()
        amorce = self.amorce_select.get()
        apartirde = self.apartirde.get()
        prefixe = self.prefix.get()
        nomfich = self.nom_fich.get()
        postfixe = self.postfix.get()
        ext = self.ext.get()
        # print(str(nomrep)+" "+str(amorce)+" "+str(apartirde)+" "+str(prefixe)+" "+str(nomfich)+" "+str(postfixe)+" "+str(ext))





    def main_window(self):
        # toto = MyWindow()
        self.frame = Frame(self)
        self.frame.grid()
        ### Label ###
        # title_lab = Label(self, text="Renommer en lot").grid(row=0, column=2)
        Label(self.frame, text="Nom de répertoire").grid(row=1, column=1)
        Label(self.frame, text="Amorce").grid(row=3, column=0, pady=10)
        Label(self.frame, text="Prefixe").grid(row=3, column=1)
        Label(self.frame, text="Nom du fichier").grid(row=3, column=2)
        Label(self.frame, text="Postfixe").grid(row=3, column=3)
        Label(self.frame, text="Extension concernée").grid(row=3, column=4)
        Label(self.frame, text="A partir de : ").grid(row=5, column=0, pady=10)

        ### Picture ####
        picture = PhotoImage(file="./data/Rename.gif")
        label1 = Label(self.frame, image=picture)
        label1.image = picture
        label1.grid(row=1, column=5)

        ### Entry ###
        self.nomrep = StringVar()
        Entry(self.frame, textvariable=self.nomrep).grid(row=1, column=2)

        self.prefix = StringVar()
        Entry(self.frame, textvariable=self.prefix).grid(row=4, column=1, padx=15)

        self.nom_fich = StringVar()
        Entry(self.frame, textvariable=self.nom_fich).grid(row=4, column=2, padx=15)

        self.apartirde = StringVar()
        Entry(self.frame, textvariable=self.apartirde).grid(row=6, column=0, padx=15)

        self.postfix = StringVar()
        Entry(self.frame, textvariable=self.postfix).grid(row=4, column=3, padx=15)

        self.ext = StringVar()
        Entry(self.frame, textvariable=self.ext).grid(row=4, column=4, padx=15)

        ### Combobox ###
        self.amorce_select = StringVar()
        amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
        Combobox(self.frame, textvariable=self.amorce_select,
                               values=amorce_choice, state='readonly').grid(row=4, column=0, padx=15)
        self.amorce_select.set(amorce_choice[0])

        ### Button ###
        Button(self.frame, text="Renommer", command=self.test).grid(row=6, column=4)

    def create(self):
        self.frame = Frame(self)
        self.frame.grid()
        ### Label ###
        # title_lab = Label(self, text="Renommer en lot").grid(row=0, column=2)
        Label(self.frame, text="Nom de répertoire").grid(row=1, column=1)
        Label(self.frame, text="Amorce").grid(row=3, column=0, pady=10)
        Label(self.frame, text="Prefixe").grid(row=3, column=1)
        Label(self.frame, text="Nom du fichier").grid(row=3, column=2)
        Label(self.frame, text="Postfixe").grid(row=3, column=3)
        Label(self.frame, text="Extension concernée").grid(row=3, column=4)
        Label(self.frame, text="A partir de : ").grid(row=5, column=0, pady=10)

        ## Picture ####
        # picture = PhotoImage(file="./data/New-Rule.gif")
        # label1 = Label(self.frame, image=picture)
        # label1.image = picture
        # label1.grid(row=1, column=5)

        ### Entry ###
        nomrep = StringVar()
        Entry(self.frame, textvariable=nomrep).grid(row=1, column=2)

        prefix = StringVar()
        Entry(self.frame, textvariable=prefix).grid(row=4, column=1, padx=15)

        apartirde = StringVar()
        Entry(self.frame, textvariable=apartirde).grid(row=6, column=0, padx=15)

        postfix = StringVar()
        Entry(self.frame, textvariable=postfix).grid(row=4, column=3, padx=15)

        ext = StringVar()
        Entry(self.frame, textvariable=ext).grid(row=4, column=4, padx=15)

        ### Combobox ###
        amorce_select = StringVar()
        amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
        Combobox(self.frame, textvariable=amorce_select,
                 values=amorce_choice, state='readonly').grid(row=4, column=0, padx=15)
        amorce_select.set(amorce_choice[0])

        ### Button ###
        Button(self.frame, text="Renommer").grid(row=6, column=4)  # , command=)


    def roll(self):
        self.clear_screen(self.frame)
        self.create()

    def menu(self):
        main_menu = Menu(self)
        roll_menu = Menu(main_menu, tearoff=0)                              # Menu déroulant
        roll_menu.add_command(label="Lister", command=self.roll)     # Option lister, renvoie sur une fenêtre listant les règles
        roll_menu.add_command(label="Créer", command=self.create_window)    # Option créer, renvoie sur une fenêtre de creation

        help_menu = Menu(main_menu, tearoff=0)  # Menu Fils
        help_menu.add_command(label="À propos", command=self.help)

        main_menu.add_cascade(label="Règles", menu=roll_menu)
        main_menu.add_cascade(label="?", menu=help_menu)

        self.config(menu=main_menu)

    @staticmethod
    def clear_screen(frame):
        for widget in frame.winfo_children():
            widget.grid_forget()
            widget.destroy()

    @staticmethod
    def help():
        messagebox.showinfo("À propos", "Créé par Quentin Nicolas\nVersion 1.0")

    def list_window(self):
        # messagebox.showinfo("Liste des règles", "lister")
        fen = MyWindow("Liste des règles")
        lab = Label(fen, text="test")
        lab.pack()

    def create_window(self):
        messagebox.showinfo("Créer une règle", "creer")


fen = MyWindow("Renommage fichier")
fen.mainloop()

# if __name__ == '__main__':
#     app = MyWindow("Renommage fichier")
#     app.mainloop()
#     app.quit()