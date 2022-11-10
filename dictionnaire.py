employé={"id01":{"prénom":"paul","nom":"Dupont","age":32},"id02":{"prénom":"Julie","nom":"Dupuit","age":25},"id03":{"prénom":"patrick","nom":"lolipop","age":38}

}
print(employé)
del employé["id03"]#supprimer patrick du dictionnaire
employé["id01"].update({"age":26})#pour modifier l'âge de julie #
employé["id01"].update({"age":32})#pour modifier l'âge de paul
print(employé)

