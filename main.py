import Cadastro
from Pet import pet

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
    dicionario_de_cadastro = Cadastro.cadastro()
    pet = pet(dicionario_de_cadastro.get("nome"), dicionario_de_cadastro.get("idade"),
              dicionario_de_cadastro.get("raca"), dicionario_de_cadastro.get("porte"))
    print(pet.nome, pet.idade, pet.raca, pet.porte)

elif opcao == "2":
    listar_pets()

else:
    print("\nOpção inválida.")