import tkinter as tk
from tkinter import *
from bdd import BDD
# couleurs = https://htmlcolorcodes.com/fr/

class Facture():
    def __init__(self):

        # #menu déroulant
        self.choix_r = tk.StringVar(root)


        self.opt = tk.OptionMenu(root, self.choix_r, *BDD.get_raison())
        
        self.opt.config(width=30, font=('Helvetica', 12))
        self.opt.grid(pady=35, row=1)

        self.choix_r.trace("w", self.call)
        #affichage des dates en texte

        self.frame_produit =  tk.Frame(root, bg="#ece8d4")
        self.frame_produit.grid(row = 3, pady = 35)

    def callback(self, *args):
        index = []
        loulou = []
        loulou = BDD.get_produit(self.choix_r.get(), self.choix_d.get())
        if loulou != []:
            print("coucou")
            index = ["produit", "quantite"]

            for i in range(len(index)):
                tk.Label(self.frame_produit, text=index[i] ,borderwidth="1",relief="solid",width="12").grid(row=0, column=i+1)

            for i in range(len(loulou)):

                tk.Label(self.frame_produit, text=loulou[i].name ,borderwidth="1",relief="solid",width="12").grid(row=i+1, column=1)
                tk.Label(self.frame_produit, text=loulou[i].quantite, borderwidth="1",relief="solid",width="12").grid(row=i+1, column=2)

        else:
            print("else")
            for widget in self.frame_produit.winfo_children():
                widget.forget()


    #affichage des dates
    def call(self, *arg):
        self.choix_d = tk.StringVar(root)

        # self.callback(*[])
        if BDD.get_date(self.choix_r.get()) != []:
            self.opte = tk.OptionMenu(root, self.choix_d, *BDD.get_date(self.choix_r.get()))
        else:
            self.opte = tk.OptionMenu(root, self.choix_d, *['Aucune facture disponible'])
        
        self.opte.grid(pady=15, row = 2)
        self.opte.config(text = f"{BDD.get_date(self.choix_r.get())}", width=30, font=('Helvetica', 12))
        self.choix_d.trace("w", self.callback)
        for widget in self.frame_produit.winfo_children():
            widget.destroy()


# Fenetre
root = tk.Tk()
root.title("Ikeo")
root.geometry("310x600")
root.configure(bg="#ece8d4")

#Titre fenetre
frame_titre = tk.Frame(root)
frame_titre.grid(row= 0)
titre = tk.Label(frame_titre, text='Facture', font=("Helvetica",40), bg="#ece8d4")
titre.grid()


facture = Facture()

root.mainloop()
