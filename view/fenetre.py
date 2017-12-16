import sys
sys.path.append('.\\classes')
from regle import *
from listeregle import *
from renommage import *


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox



class MyWindow(Tk):
    def __init__(self, title):
        super(MyWindow, self).__init__()
        self.resizable(width=False, height=False)
        # self.title(title)
        # self.create()
        # self.window_liste()
        self.main_window()
        self.menu()
        self.geom_fen(1050, 450)
        self.mainloop()

    def geom_fen(self, larg, haut):
        if self.winfo_screenwidth() < 1920:
            larg *= 0.8
            haut *= 0.8
        self.geometry(
            "%dx%d%+d%+d" % (larg, haut, (self.winfo_screenwidth() - larg) // 2,
                             (self.winfo_screenheight() - haut) // 2))

    def menu(self):
        main_menu = Menu(self)
        roll_menu = Menu(main_menu, tearoff=0)                              # Menu déroulant
        roll_menu.add_command(label="Lister", command=self.window_liste)     # Option lister, renvoie sur une fenêtre listant les règles
        roll_menu.add_command(label="Créer", command=self.window_creer)#, command=self.create_window)    # Option créer, renvoie sur une fenêtre de creation

        help_menu = Menu(main_menu, tearoff=0)  # Menu Fils
        help_menu.add_command(label="À propos", command=self.help)

        main_menu.add_cascade(label="Règles", menu=roll_menu)
        main_menu.add_cascade(label="?", menu=help_menu)

        self.config(menu=main_menu)

    def creer_nouvelle_regle(self):
        nomrep = self.nomregle.get()
        amorce = self.amorce_select.get()
        apartirde = self.apartirde.get()
        prefixe = self.prefix.get()
        nomfich = self.nom_fich.get()
        postfixe = self.postfix.get()
        ext = self.ext.get()
        # if amorce == "Aucune":
        #     amorce = None
        # print(str(nomrep)+" "+str(amorce)+" "+str(apartirde)+" "+str(prefixe)+" "+str(nomfich)+" "+str(postfixe)+" "+str(ext))
        ma_regle = Regle(nomrep, amorce, apartirde, prefixe, nomfich, postfixe, ext)
        ma_liste = ListeRegle()
        ma_liste.sauvegarder(ma_regle)
        messagebox.showinfo("Ok","Règle " + nomrep + " créée")

    def window_creer(self):
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
        # picture = PhotoImage(file="./data/New-Rule.gif")
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

    def regle_choisie(self):
        print(self.nomR.get()+";"+self.amorce.get()+";"+self.apart.get()+";"+self.prefixe.get()+";"+self.nomFichier.get()+";"+self.postfixe.get()+";"+self.extens.get())
        # return self.nomR.get()+";"+self.amorce.get()+";"+self.apart.get()+";"+self.prefixe.get()+";"+self.nomFichier.get()+";"+self.postfixe.get()+";"+self.extens.get()
        #todo faire un fichier de sauvegarde pour la regle choisie, dans le main_fenetre faire un if(regle_choisie non vide alors on charge, sinon

    def launch(self):
        win_liste_select = Toplevel(self)
        win_liste_select.geometry(
            "%dx%d%+d%+d" % (1050, 450, (self.winfo_screenwidth() - 1050) // 2,
                             (self.winfo_screenheight() - 450) // 2))
        toto = self.amorce_select.get()
        nom_regle = toto.split(" ")[0]
        amorce = toto.split(" ")[1]
        apartirde = toto.split(" ")[2]
        prefixe = toto.split(" ")[3]
        nom_fichier = toto.split(" ")[4]
        postfixe = toto.split(" ")[5]
        ext = (toto.split(" ")[6] + toto.split(" ")[7])[1:-1].replace("'", "")

        ### Label ###
        Label(win_liste_select, text="Nom de règle").grid(row=1, column=1)
        Label(win_liste_select, text="Amorce").grid(row=3, column=0, pady=10)
        Label(win_liste_select, text="Prefixe").grid(row=3, column=1)
        Label(win_liste_select, text="Nom du fichier").grid(row=3, column=2)
        Label(win_liste_select, text="Postfixe").grid(row=3, column=3)
        Label(win_liste_select, text="Extension concernée").grid(row=3, column=4)
        Label(win_liste_select, text="A partir de : ").grid(row=5, column=0, pady=10)

        ## Picture ####
        # picture = PhotoImage(file="./data/New-Rule.gif")
        # label1 = Label(self.frame, image=picture)
        # label1.image = picture
        # label1.grid(row=1, column=5)

        ## Entry ###
        self.nomR = Entry(win_liste_select)
        self.nomR.grid(row=1, column=2)
        self.nomR.insert(0,nom_regle)

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

    def window_liste(self):
        win_liste = Toplevel(self)
        win_liste.geometry(
            "%dx%d%+d%+d" % (1050, 450, (self.winfo_screenwidth() - 1050) // 2,
                             (self.winfo_screenheight() - 450) // 2))
        win_liste.title("Liste des règles")
        liste_regle = ListeRegle()
        liste_regle.charger()
        toto = liste_regle.get()
        # print(str(toto[0]).split(" ")[0]) #sort le nom de regle

        ### Combobox ###
        self.amorce_select = StringVar()
        Combobox(win_liste, textvariable=self.amorce_select,
                 values=toto, state='readonly').grid(row=0, column=0)
        self.amorce_select.set(toto[0])


        Button(win_liste, text="valider", command=self.launch).grid(row=1, column=0)

    @staticmethod
    def help(): #help
        messagebox.showinfo("À propos", "Créé par Quentin Nicolas\nVersion 1.0")







    def renommer_fichers(self):
        pass


    def main_window(self):
        ### Label ###
        # title_lab = Label(self, text="Renommer en lot").grid(row=0, column=2)
        Label(self, text="Nom de répertoire").grid(row=1, column=1)
        Label(self, text="Amorce").grid(row=3, column=0, pady=10)
        Label(self, text="Prefixe").grid(row=3, column=1)
        Label(self, text="Nom du fichier").grid(row=3, column=2)
        Label(self, text="Postfixe").grid(row=3, column=3)
        Label(self, text="Extension concernée").grid(row=3, column=4)
        Label(self, text="A partir de : ").grid(row=5, column=0, pady=10)

        ### Picture ####
        picture = PhotoImage(file="./data/Rename.gif")
        label1 = Label(self, image=picture)
        label1.image = picture
        label1.grid(row=1, column=5)

        ### Entry ###
        self.nomrep = StringVar()
        Entry(self, textvariable=self.nomrep).grid(row=1, column=2)

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
        Button(self, text="Renommer").grid(row=6, column=4)



    # def create(self):
    #     ### Label ###
    #     # title_lab = Label(self, text="Renommer en lot").grid(row=0, column=2)
    #     Label(self, text="Nom de règle").grid(row=1, column=1)
    #     Label(self, text="Amorce").grid(row=3, column=0, pady=10)
    #     Label(self, text="Prefixe").grid(row=3, column=1)
    #     Label(self, text="Nom du fichier").grid(row=3, column=2)
    #     Label(self, text="Postfixe").grid(row=3, column=3)
    #     Label(self, text="Extension concernée").grid(row=3, column=4)
    #     Label(self, text="A partir de : ").grid(row=5, column=0, pady=10)
    #
    #     ## Picture ####
    #     # picture = PhotoImage(file="./data/New-Rule.gif")
    #     # label1 = Label(self.frame, image=picture)
    #     # label1.image = picture
    #     # label1.grid(row=1, column=5)
    #
    #     ### Entry ###
    #     self.nomregle = StringVar()
    #     Entry(self, textvariable=self.nomregle).grid(row=1, column=2)
    #
    #     self.prefix = StringVar()
    #     Entry(self, textvariable=self.prefix).grid(row=4, column=1, padx=15)
    #
    #     self.apartirde = StringVar()
    #     Entry(self, textvariable=self.apartirde).grid(row=6, column=0, padx=15)
    #
    #     self.postfix = StringVar()
    #     Entry(self, textvariable=self.postfix).grid(row=4, column=3, padx=15)
    #
    #     self.nom_fich = StringVar()
    #     Entry(self, textvariable=self.nom_fich).grid(row=4, column=2, padx=15)
    #
    #     self.ext = StringVar()
    #     Entry(self, textvariable=self.ext).grid(row=4, column=4, padx=15)
    #
    #     ### Combobox ###
    #     self.amorce_select = StringVar()
    #     amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
    #     Combobox(self, textvariable=self.amorce_select,
    #              values=amorce_choice, state='readonly').grid(row=4, column=0, padx=15)
    #     self.amorce_select.set(amorce_choice[0])
    #
    #     ### Button ###
    #     Button(self, text="Créer", command=self.creer_nouvelle_regle).grid(row=6, column=4) # , command=)


    @staticmethod
    def clear_screen(frame):
        for widget in frame.winfo_children():
            widget.grid_forget()
            widget.destroy()



    def list_window(self):
        # messagebox.showinfo("Liste des règles", "lister")
        fen = MyWindow("Liste des règles")
        lab = Label(fen, text="test")
        lab.pack()





fen = MyWindow("Renommage fichier")

# if __name__ == '__main__':
#     app = MyWindow("Renommage fichier")
#     app.mainloop()
#     app.quit()