Pets = []

def armazenar_pets(pet):
    Pets.append(pet)

def listar_pets():
    contador = 1
    for pet in Pets:
        print(f"{contador} - nome: {pet["nome"]} | idade: {pet["idade"]} | raca: {pet["raca"]} "
              f"| porte: {pet["porte"]} | adotado: {pet["adotado"]}")
        contador += 1