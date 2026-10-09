jour = int(input("Entrez le jour : "))
heure = int(input("Entrez l'heure : "))
minute = int(input("Entrez les minutes : "))

total = (jour - 1) * 24 * 60 + heure * 60 + minute

print("Nombre de minutes écoulées depuis le début du mois :", total)