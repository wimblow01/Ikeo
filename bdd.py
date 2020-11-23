from ikeoClass import Product, Client
import mysql.connector


class BDD():

    @classmethod
    def connect(cls):
        cls.link = mysql.connector.connect(**{
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port' : 8081,
            'database': 'ikeo'
            })
        cls.cursor=cls.link.cursor()
        
    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.link.close()

    @classmethod
    def getAllProducts(cls):
        cls.connect()
        productList=[]
        query="SELECT * FROM produits"
        cls.cursor.execute(query)
        liste=cls.cursor.fetchall()
        for row in liste:
            id=int(row[0])
            name=str(row[1])
            ref=str(row[2])
            description=str(row[3])
            aband=str(row[4])
            product=Product(id,name,ref,description,aband)
            productList.append(product)
        cls.close()
        return productList

    @classmethod
    def getFournisseurForProducts(cls):
        products=cls.getAllProducts()
        cls.connect()
        productWithFournisseur=[]
        
        for product in products:
            query="SELECT site_de_production.nom FROM site_de_production \
                    JOIN produit_site ON site_de_production.id_site=produit_site.id_site \
                    where produit_site.id_produit="+str(product.id)
            cls.cursor.execute(query)
            liste=cls.cursor.fetchall()
            listeFournisseur=[]
            for row in liste:
                name=str(row[0])
                listeFournisseur.append(name)
            product.fournisseur=listeFournisseur
            productWithFournisseur.append(product)

        return productWithFournisseur

    @classmethod
    def get_raison(cls):
        BDD.connect()
        liste_raison = []
        query = "select raison, ville from clients join raison_sociale on clients.id_raison =  raison_sociale.id_raison join ville on clients.id_ville = ville.id_ville"
        BDD.cursor.execute(query)
        res = BDD.cursor.fetchall()
        for row in res:
            nom_raison =str(row[0])
            ville = str(row[1])
            client = Client(nom_raison, ville)
            liste_raison.append(client)

        return liste_raison


    @classmethod
    def get_date(cls, cloclo):
        BDD.connect()
        # choix_raison = recup_raison
        liste_date = []
        raison_s = cloclo.split("-")[0]
        villes = cloclo.split("-")[1]
        query = f"select date_facture from facture \
                join clients on facture.id_client = clients.id_client \
                join raison_sociale on clients.id_raison = raison_sociale.id_raison \
                join ville on clients.id_ville = ville.id_ville \
                where raison = '{raison_s}' and ville = '{villes}'; "

        BDD.cursor.execute(query)
        res = BDD.cursor.fetchall()
        for row in res:
            liste_date.append(str(row[0]))
        return liste_date

    # @classmethod
    # def get_produit(cls, cloclo, date_facture):
    #     BDD.connect()
    #     liste_prod = []
    #     raison_s = cloclo.split("-")[0]
    #     villes = cloclo.split("-")[1]
    #     query = f"select * from factures_produit \
    #             join produits on produits.id_produit = factures_produit.id_produit \
    #             join facture on factures_produit.id_facture = facture.id_facture \
    #             join clients on facture.id_client = clients.id_client \
    #             join raison_sociale on clients.id_raison =  raison_sociale.id_raison \
    #             join ville on clients.id_ville = ville.id_ville \
    #             where raison = '{raison_s}' and ville = '{villes}' and date_facture = '{date_facture}' "
        
    #     BDD.cursor.execute(query)
    #     res = BDD.cursor.fetchall()
    #     for row in res:
    #         liste_prod.append(str(row[0:2]))
    #     return "\n".join(liste_prod)


    @classmethod
    def get_produit(cls, cloclo, date_facture):
        BDD.connect()
        liste_prod = []
        raison_s = cloclo.split("-")[0]
        villes = cloclo.split("-")[1]
        query = f"select produits.id_produit,nom_produit,ref_produit,aband_produit,desription_produit, quantite from factures_produit \
                join produits on produits.id_produit = factures_produit.id_produit \
                join facture on factures_produit.id_facture = facture.id_facture \
                join clients on facture.id_client = clients.id_client \
                join raison_sociale on clients.id_raison =  raison_sociale.id_raison \
                join ville on clients.id_ville = ville.id_ville \
                where raison = '{raison_s}' and ville = '{villes}' and date_facture = '{date_facture}' "
        
        BDD.cursor.execute(query)
        res = BDD.cursor.fetchall()
        for row in res:
            id=int(row[0])
            name=str(row[1])
            ref=str(row[2])
            description=str(row[3])
            aband=str(row[4])
            quantite = int(row[5])
            product=Product(id,name,ref,description,aband, quantite= quantite)
            liste_prod.append(product)

        return liste_prod



