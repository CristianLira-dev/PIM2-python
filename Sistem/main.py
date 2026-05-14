import Cadastro
import Banco_De_Dados

# MENU DO SISTEMA
while True:
    print("""
    ----------------------------------
     SISTEMA DE GERENCIAMENTO DE PETS
    ----------------------------------
    
    Selecione uma das opções abaixo:
    
    1 - Cadastrar Pet
    2 - Listar Pets Cadastrados
    3 - Sair
          
    """)


    opcao = input("Digite a opção desejada: ")


    if opcao == "1":
        #cria o objeto com base no retorno da classe cadastro
        pet = Cadastro.cadastro()
        #armazena o pet no banco de dados
        Banco_De_Dados.armazenar_pets(pet.to_json())
        Banco_De_Dados.salvar_pets()


    elif opcao == "2":
        Banco_De_Dados.listar_pets()

    elif opcao == "3":
        break

    else:
        print("\nOpção inválida.")