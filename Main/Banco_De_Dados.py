import json
import os

pets = []

# Armazena os pets em um Array
def armazenar_pets(pet):
    pets.append(pet)

# Lista os pets cadastrados
def listar_pets():
    if len(pets) != 0:
        contador = 1

        for pet in pets:

            adotado = "Sim" if pet["adotado"] else "Não"

            print(f"""
╔══════════════════════════════╗
        PET {contador}
╠══════════════════════════════╣
  Nome     : {pet["nome"]}
  Idade    : {pet["idade"]}
  Raça     : {pet["raca"]}
  Porte    : {pet["porte"]}
  Adotado  : {adotado}
╚══════════════════════════════╝
""")

            contador += 1

    else:
        print("AINDA NÃO EXISTEM PETS CADASTRADOS")

# Salva Array em um arquivo JSON
def salvar_pets():
    with open("pets.json", "w") as arquivo:
        json.dump(pets, arquivo, indent=4)

def carregar_pets():
    if os.path.exists("pets.json"):
        try:
            with open("pets.json", "r") as arquivo:
                dados_temporarios = json.load(arquivo)

                pets.clear()
                pets.extend(dados_temporarios)
        except :
            pets.clear()