# import sys
# sys.path.append('.\\classes')
# from regle import *
# from listeregle import *
#
#
# from tkinter import *
# from tkinter import messagebox
# from tkinter.ttk import Combobox
#
# class FenetreCreer():
#     def __init__(self):
#         self.fenetre_creer = Tk()
#         self.fenetre_creer.resizable(width=False, height=False)
#         self.fenetre_creer.title("Créer règle")
#         self.create()
#         self.menu()
#         self.geom_fen(1050, 450)
#         # self.fenetre_creer.mainloop()
#
#     def geom_fen(self, larg, haut):
#         if self.fenetre_creer.winfo_screenwidth() < 1920:
#             larg *= 0.8
#             haut *= 0.8
#         self.fenetre_creer.geometry(
#             "%dx%d%+d%+d" % (larg, haut, (self.fenetre_creer.winfo_screenwidth() - larg) // 2,
#                              (self.fenetre_creer.winfo_screenheight() - haut) // 2))
#
#     def menu(self):
#         main_menu = Menu(fenetre_creer)
#         roll_menu = Menu(main_menu, tearoff=0)                              # Menu déroulant
#         roll_menu.add_command(label="Lister")
#         roll_menu.add_command(label="Créer")#, command=self.create_window)
#         help_menu = Menu(main_menu, tearoff=0)  # Menu Fils
#         help_menu.add_command(label="À propos")#, command=self.help)
#
#         main_menu.add_cascade(label="Règles", menu=roll_menu)
#         main_menu.add_cascade(label="?", menu=help_menu)
#
#         self.fenetre_creer.config(menu=main_menu)
#
#     def create(self):
#         ### Label ###
#         Label(self.fenetre_creer, text="Nom de règle").grid(row=1, column=1)
#         Label(self.fenetre_creer, text="Amorce").grid(row=3, column=0, pady=10)
#         Label(self.fenetre_creer, text="Prefixe").grid(row=3, column=1)
#         Label(self.fenetre_creer, text="Nom du fichier").grid(row=3, column=2)
#         Label(self.fenetre_creer, text="Postfixe").grid(row=3, column=3)
#         Label(self.fenetre_creer, text="Extension concernée").grid(row=3, column=4)
#         Label(self.fenetre_creer, text="A partir de : ").grid(row=5, column=0, pady=10)
#
#         ## Picture ####
#         # picture = PhotoImage(file="./data/New-Rule.gif")
#         # label1 = Label(self.frame, image=picture)
#         # label1.image = picture
#         # label1.grid(row=1, column=5)
#
#         ### Entry ###
#         self.nomregle = StringVar()
#         Entry(self.fenetre_creer, textvariable=self.nomregle).grid(row=1, column=2)
#
#         self.prefix = StringVar()
#         Entry(self.fenetre_creer, textvariable=self.prefix).grid(row=4, column=1, padx=15)
#
#         self.apartirde = StringVar()
#         Entry(self.fenetre_creer, textvariable=self.apartirde).grid(row=6, column=0, padx=15)
#
#         self.postfix = StringVar()
#         Entry(self.fenetre_creer, textvariable=self.postfix).grid(row=4, column=3, padx=15)
#
#         self.nom_fich = StringVar()
#         Entry(self.fenetre_creer, textvariable=self.nom_fich).grid(row=4, column=2, padx=15)
#
#         self.ext = StringVar()
#         Entry(self.fenetre_creer, textvariable=self.ext).grid(row=4, column=4, padx=15)
#
#         ### Combobox ###
#         self.amorce_select = StringVar()
#         amorce_choice = ('Aucune', 'Lettres', 'Chiffres')
#         Combobox(self.fenetre_creer, textvariable=self.amorce_select,
#                  values=amorce_choice, state='readonly').grid(row=4, column=0, padx=15)
#         self.amorce_select.set(amorce_choice[0])
#
#         ### Button ###
#         Button(self.fenetre_creer, text="Créer", command=self.creer_nouvelle_regle).grid(row=6, column=4) # , command=)
#
#     def creer_nouvelle_regle(self):
#         nomrep = self.nomregle.get()
#         amorce = self.amorce_select.get()
#         apartirde = self.apartirde.get()
#         prefixe = self.prefix.get()
#         nomfich = self.nom_fich.get()
#         postfixe = self.postfix.get()
#         ext = self.ext.get()
#         # if amorce == "Aucune":
#         #     amorce = None
#         # print(str(nomrep)+" "+str(amorce)+" "+str(apartirde)+" "+str(prefixe)+" "+str(nomfich)+" "+str(postfixe)+" "+str(ext))
#         ma_regle = Regle(nomrep, amorce, apartirde, prefixe, nomfich, postfixe, ext)
#         ma_liste = ListeRegle()
#         ma_liste.sauvegarder(ma_regle)
#         self.fenetre_creer.quit()
#
# toto = FenetreCreer()
# # toto.mainloop()