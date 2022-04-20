class Personne:
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


class Livre():

    def __init__(self, titre, Auteur):
        self.titre = titre
        self.auteur = Auteur

    def Affichage(self):
        print(self.titre, self.auteur.nom)


class Auteur(Personne):
    
    oeuvres = [['Livres01', "Jean", "Michel"], ['Livres02', "Michel", "Jean"], ["Livres03", "Jean", "Michel"]]

    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        

    def listeOeuvre(self):
        for i in range(len(self.oeuvres)):
            if (self.oeuvres[i][1] == self.nom):
                print(self.oeuvres[i][0])

    def ecrirUnLivre(self):
        titre = input('Entrez un titre de Livre: ')

        newLivre = Livre(titre)
        self.oeuvres.append([newLivre.titre, self.nom])
        print(self.oeuvres)

# Auteur('Jean', 'Michel').listeOeuvre()  
# Auteur('Michel', 'Jean').listeOeuvre()
Livre('Livres01', Auteur('jean', 'Michel')).Affichage() 
