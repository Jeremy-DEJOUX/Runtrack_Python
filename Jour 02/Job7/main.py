class Board():

    Plateau = []

    def __init__(self, heigth:int, width:int):
        self.width = width
        self.height = heigth

    def createBoard(self):
        for i in range(self.height):
            self.Plateau.append(['O']*self.width)
        print(self.Plateau)

    def Play(self):
        colonne = int(input('Choisissez la colonne ou vous voulez jouer: '))
        pass

Board(5, 5).createBoard()
