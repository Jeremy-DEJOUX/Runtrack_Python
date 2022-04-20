class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(self.nom, self.prenom)

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

class Client(Personne):

    catalog = []

    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)

class Bibliotheque():
    
    catalogue = [["Livres01", 5], ["Livres02", 2], ["Livres03", 1], ["Livres04", 7], ["Livres05", 9]]    

    def acheterLivre(self):
        pass

    def inventaire(self):
        for i in range(len(self.catalogue)):
            print(f'Titre: {self.catalogue[i][0]}  Quantitées: {self.catalogue[i][1]}')

    def louer(self, nom, Client):
        catalog = Client.catalog
        for i in range(len(self.catalogue)):
            if (self.catalogue[i][0] == nom):
                if (self.catalogue[i][1] > 0):
                    self.catalogue[i][1] = self.catalogue[i][1] - 1
                    catalog.append(self.catalogue[i][0])
                    print("Le Livre existe le voici", self.catalogue[i][0])
                else:
                    print("Le livre n'est plus en stock")
            else:
                print("Le Livre n'existe pas")
    
    def rendreLivre(self, Client):
        catalog = Client.catalog
        for i in range(len(catalog)):
            for j in range (len(self.catalogue)):
                if (catalog[i][0] in self.catalogue[j][0]):
                    self.catalogue[j][1] = self.catalogue[j][1] + 1
            catalog.pop(i)




