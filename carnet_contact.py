nom = input("Entrez votre nom : ")
age = int(input("Entrez votre age : "))

fichier = open("contact.txt", "a")
fichier.write(nom + age + "\n")
fichier.close()
print("Contact enrigstrer")

fichier = open("contact.txt", "r")
contenu = fichier.read()
fichier.close()

print("---------- LISTE DES CONTACTS ----------")
print(contenu)
