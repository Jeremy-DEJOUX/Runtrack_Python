# def tri(tab):
#     for i in range(len(tab)):
#         min = i

#         for j in range(i+1, len(tab)):
#             if tab[min] > tab[j]:
#                 min = j
#             tmp = tab[i]
#             tab[i] = tab[min]
#             tab[min] = tmp
#     return tab

tab = []

a = input("Entrez un nombre entier :")
tab.append(a)

b = input("Entrez un nombre entier :")
tab.append(b)

c = input("Entrez un nombre entier :")
tab.append(c)

d = input("Entrez un nombre entier :")
tab.append(d)

e = input("Entrez un nombre entier :")
tab.append(e)

tab.sort() # OR tri(tab)

print("Tri du Tableau", tab)