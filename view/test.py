# import tkinter as tk
# from test2 import delete_frame
#
#
# # def delete_frame():
# #     for widget in frame.winfo_children():
# #         widget.pack_forget()
# def tutu():
#     delete_frame(frame)
#
# fenetre = tk.Tk()
#
# frame = tk.Frame(fenetre)
# frame.grid()
#
# for i in range(3):
#     btn = tk.Button(frame, text=i)
#     btn.grid()  ## J'ai utilisé .pack() ici... donc .pack_forget()
#
# bouton_delete = tk.Button(fenetre, text='Delete',
#                           command=tutu)
# bouton_delete.grid()
#
# fenetre.mainloop()


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


class MyWindow(Tk):
    def __init__(self, title):
        super(MyWindow, self).__init__()
        self.resizable(width=False, height=False)
        self.title(title)
        self.geom_fen(1200, 600)
        self.fenetre()

    def fenetre(self):
        '''
        http://lyyn.fr.nf/wp/2013/04/22/python-3-tkinter-liste-deroulante-avec-combobox-le-chemin-de-croix/
        :return:
        '''
        self.toto = Frame(self)
        self.toto.grid()
        Label(self.toto, text="1").grid()
        tutu = Button(self, text='del', command=self.tutu)
        tutu.grid()


    def fen(self):
        self.toto = Frame(self)
        self.toto.grid()
        Label(self.toto, text="2").grid()
        tutu = Button(self, text='del', command=self.tutu)
        tutu.grid()

    def tutu(self):
        self.clear_screen(self.toto)
        self.fen()

    def clear_screen(self, frame):
        for widget in frame.winfo_children():
            widget.grid_forget()

    def geom_fen(self, larg, haut):
        if self.winfo_screenwidth() < 1920:
            larg *= 0.8
            haut *= 0.8
        self.geometry(
            "%dx%d%+d%+d" % (larg, haut, (self.winfo_screenwidth() - larg) // 2, (self.winfo_screenheight()
                                                                                  - haut) // 2))

    @staticmethod
    def help(toto):
        messagebox.showinfo("À propos", "Créé par Quentin Nicolas\nVersion 1.0"+str(toto))




toto = MyWindow("titre")
toto.mainloop()
