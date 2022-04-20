height = int(input(("Entrez un hauteur: ")))

def draw_triangle(height):
    for i in range(height):
        print(' ' * (height - i), '/', ' ' * i * 2,  '\\')
        if (i == height - 1):
            print('','/', '_' * (height * 2), '\\')

draw_triangle(height)