height = int(input('Veuillez entrer un nombre entier pour définir la longeur: '))
width = int(input('Veuillez entrer un nombre entier pour définir la largeur: '))


def draw_rectangle(width, height):
    for i in range(height):
        if (i == 0 or i == height - 1):
            print('|', '-' * width, '|')
        else:
            print('|', ' ' * width, '|')




draw_rectangle(width, height)