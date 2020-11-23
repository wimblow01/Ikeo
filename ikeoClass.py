
class Product():
    
    def __init__(self,id,name,ref_produit,aband_produit,description_produit,fournisseur=[], quantite=0):
        self.id=id
        self.name=name
        self.ref_produit=ref_produit
        self.aband_produit=aband_produit
        self.description_produit=description_produit
        self.fournisseur=fournisseur
        self.quantite = quantite

    def __repr__(self):
        return self.name + "-" + str(self.quantite) + "\n"



class Client():
    def __init__(self, raison_sociale, ville):
        self.raison_sociale = raison_sociale
        self.ville = ville
    
    def __repr__(self):
        stri = self.raison_sociale + "-" + self.ville

        return stri