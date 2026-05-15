import json

pets = []

#Armazena os pets em um Array
def armazenar_pets(pet):
    pets.append(pet)

#Lista os pets cadastrados
def listar_pets():
    if len(pets) != 0:
        contador = 1
        for pet in pets:
            print(f"{contador} - nome: {pet["nome"]} | idade: {pet["idade"]} | raca: {pet["raca"]} "
                  f"| porte: {pet["porte"]} | adotado: {pet["adotado"]}")
            contador += 1
    else:
        print("AINDA NAO EXISTEM PETS CADASTRADOS")

#Salva Array em um arquivo JSON
def salvar_pets():
    with open("pets.json", "w") as arquivo:
        json.dump(pets, arquivo, indent=4)