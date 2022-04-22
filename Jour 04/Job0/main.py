f = open('Jour 04/Job0/output.txt', 'a')
f.write(input('Entrez une chaine de caractères: '))
f.close()

f = open("Jour 04/Job0/output.txt", "r")
print(f.read())