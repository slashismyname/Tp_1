nbEmploy = int(input("Veuillez saisir le nombre des employes : "))

tableau_E = []
tableau_S = []

for i in range(nbEmploy):
    nom = input("Veuillez saisir le nom de l'employe numero " + str(i + 1) + " : ")
    salaire = int(input("Veuillez saisir le salaire de l'employe numero " + str(i + 1) + " : "))

    tableau_E.append(nom)
    tableau_S.append(salaire)

print("C'est la fin du remplissage")

plus_petite_valeur = min(tableau_S)
index_plus_petite_valeur = tableau_S.index(plus_petite_valeur)

plus_grande_valeur = max(tableau_S)
index_plus_grande_valeur = tableau_S.index(plus_grande_valeur)

while True:
    print("Appuyez sur 1 pour affficher le plus petit et le plus grand salaire ou 0 pour finir")
    valeur = input()
    if valeur == "1":
        print("Le plus grand valeur saaire est de :")
        print("Nom:", tableau_E[index_plus_grande_valeur], "Salaire:", tableau_S[index_plus_grande_valeur])
        print("/n")
        print("Le plus petit salaire est de :")
        print("Nom:", tableau_E[index_plus_petite_valeur], "Salaire:", tableau_S[index_plus_petite_valeur])
        break
    elif valeur == "0":
        break

