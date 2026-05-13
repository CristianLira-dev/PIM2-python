import json
import os

#nome do arquivo, onde serão salvas as informações
arquivo = "pets.json"

#dados do arquivo salvo em um array
pets = []

#classe do pet
class Pet:
    def __init__(self, nome, idade, raca, porte, adotado=False):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.adotado = adotado

#função que transforma o objeto em um json 
    def to_json(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "raca": self.raca,
            "porte": self.porte,
            "adotado": self.adotado
        }
    
#verifica se o arquivo já existe
if not os.path.exists(arquivo):
#abre o arquivo com o nome "pets.json" e coloca as informações que estão dentro do array pets
    with open(arquivo, "w", encoding="utf-8") as arq:
        json.dump(pets, arq, indent=4, ensure_ascii=False)

# FUNÇÃO PARA LISTAR PETS
def listar_pets():

#le o arquivo e coloca as informações no array pets
    with open(arquivo, "r", encoding="utf-8") as arq:
        pets = json.load(arq)

    print("\n<--- PETS CADASTRADOS --->")

    for pet in pets:

#verifica se esta adotado ou não
        status = "Sim" if pet["adotado"] else "Não"

        print(f"""
Nome: {pet["nome"]}
Idade: {pet["idade"]}
Raça: {pet["raca"]}
Porte: {pet["porte"]}
Adotado: {status}
""")
        
# FUNÇÃO PARA CADASTRAR PET
def cadastrar_pet():

    nome = input("\nDigite o nome do pet: ")
    idade = input("Digite a idade do pet: ")
    raca = input("Digite a raça do pet: ")
    porte = input("Digite o porte do pet: ")

#cria um objeto da classe Pet com as informações que o usuario digitou acima
    novo_pet = Pet(
        nome.capitalize(),
        idade,
        raca.capitalize(),
        porte.capitalize()
    )

#le o arquivo e salva as informações no array pets
    with open(arquivo, "r", encoding="utf-8") as arq:
        pets = json.load(arq)

#adiciona o pet do usuario ao final da lista dos pets cadastrados
    pets.append(novo_pet.to_json())

#coloca a lista dos pets cadastrados atualizada no arquivo pets.json
    with open(arquivo, "w", encoding="utf-8") as arq:
        json.dump(pets, arq, indent=4, ensure_ascii=False)

    print("\nPet cadastrado com sucesso!")

# MENU DO SISTEMA
print("""
----------------------------------
 SISTEMA DE GERENCIAMENTO DE PETS
----------------------------------

Selecione uma das opções abaixo:

1 - Cadastrar Pet
2 - Listar Pets Cadastrados
      
""")


opcao = input("Digite a opção desejada: ")


if opcao == "1":
    cadastrar_pet()

elif opcao == "2":
    listar_pets()

else:
    print("\nOpção inválida.")