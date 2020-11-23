
    # D'afficher tous les produits ainsi que leurs sites de production,
    # D'afficher la facture d'un client à une date choisie,
    # De saisir une facture (et de la mémoriser en base),
    # De saisir un nouveau client,
    # D'afficher tous les sites de productions,
    # De saisir un nouveau produit et de le ratacher à un site de production.

import tkinter as tk
from tkinter import *
from bdd import BDD


loulou = BDD.getFournisseurForProducts()


root = tk.Tk()
root.title("Ikeo")
root.geometry("1080x720")
root.configure(bg="#ece8d4")


frame_titre = tk.Frame(root, bg="#ece8d4")
frame_titre.pack()
titre = tk.Label(frame_titre, text='Produits', font=("Helvetica",40), bg="#ece8d4")
titre.pack()



frame_produit =  tk.Frame(root)
frame_produit.pack(pady = 50)

index = ["nom", "référence", "Produit abandonné", "description", "fournisseur"]


for i in range(len(index)):
    tk.Label(frame_produit, text=index[i],borderwidth="1",relief="solid",width="18", height = "3").grid(row=0, column=i+1)




for i in range(len(loulou)):
    tk.Label(frame_produit, text=loulou[i].name,borderwidth="1",relief="solid",width="18", height = "3").grid(row=i+1, column=1)
    tk.Label(frame_produit, text=loulou[i].ref_produit,borderwidth="1",relief="solid",width="18", height = "3").grid(row=i+1, column=2)
    tk.Label(frame_produit, text=loulou[i].aband_produit,borderwidth="1",relief="solid",width="18", height = "3").grid(row=i+1, column=3)
    tk.Label(frame_produit, text=loulou[i].description_produit,borderwidth="1",relief="solid",width="18", height = "3").grid(row=i+1, column=4)
    tk.Label(frame_produit, text=loulou[i].fournisseur,borderwidth="1",relief="solid",width="18", height = "3").grid(row=i+1, column=5)



root.mainloop()



