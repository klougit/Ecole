
from tkinter import *
from tkinter import messagebox


class MaFenetre(Tk):
    def __init__(self, title):
        super(MaFenetre, self).__init__()
        # self.grid_columnconfigure(0, weight=2)
        # self.grid_rowconfigure(0, weight=2)
        self.resizable(width=False, height=False)
        self.title(title)
        self.menu()
        self.main_window()
        self.geom_fen(1200, 600)

    def geom_fen(self, larg, haut):
        if self.winfo_screenwidth() < 1920:
            larg *= 0.8
            haut *= 0.8
        self.geometry(
            "%dx%d%+d%+d" % (larg, haut, (self.winfo_screenwidth() - larg) // 2,
                             (self.winfo_screenheight() - haut) // 2))

    def main_window(self):
        frame = Frame(self)
        frame.pack()
        lab = Label(frame, text="test")
        lab.pack()



    def menu(self):
        main_menu = Menu(self)
        roll_menu = Menu(main_menu, tearoff=0)                              # Menu déroulant
        roll_menu.add_command(label="Lister", command=self.list_window)     # Option lister, renvoie sur une fenêtre listant les règles
        roll_menu.add_command(label="Créer", command=self.create_window)    # Option créer, renvoie sur une fenêtre de creation

        help_menu = Menu(main_menu, tearoff=0)  # Menu Fils
        help_menu.add_command(label="À propos", command=self.help)

        main_menu.add_cascade(label="Règles", menu=roll_menu)
        main_menu.add_cascade(label="?", menu=help_menu)

        self.config(menu=main_menu)

    def clear_screen(self, frame):
        for widget in frame.winfo_children():
            widget.pack_forget()

    @staticmethod
    def help():
        messagebox.showinfo("À propos", "Créé par Quentin Nicolas\nVersion 1.0")

    def list_window(self):
        # messagebox.showinfo("Liste des règles", "lister")
        fen = MaFenetre("Liste des règles")
        lab = Label(fen, text="test")
        lab.pack()

    def create_window(self):
        messagebox.showinfo("Créer une règle", "creer")


fen = MaFenetre("Renommage fichier")
fen.mainloop()