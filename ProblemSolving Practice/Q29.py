#TODO: Given a list of names, print all names starting with the  letter 'A'

names = ["Asia", "Anartica", "Mumbai", "Arnala"]

for name in names:
    if name.startswith(("A",'a')):#use tuple ()
        print(name)

