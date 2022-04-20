class Personne:
    def __init__(self):
        self.nom = input('Entrez votre nom: ')
        self.prenom = input('Entrez votre prenom: ')

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

Personne_02 = Personne()
Personne_02.SePresenter()

pp = Personne_02.getPrenom()

print(pp)