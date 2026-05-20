import Cadastro
import Banco_De_Dados
import Excluir_Pet
import Editar_Dados

Banco_De_Dados.carregar_pets()

# MENU DO SISTEMA
while True:
    print("""
    ----------------------------------
     SISTEMA DE GERENCIAMENTO DE PETS
    ----------------------------------
    
    Selecione uma das opções abaixo:
    
    1 - Cadastrar Pet
    2 - Listar Pets Cadastrados
    3 - Editar Dados
    4 - Excluir Pet
    5 - Sair
          
    """)


    opcao = input("Digite a opção desejada: ")


    if opcao == "1":
        #cria o objeto com base no retorno da classe cadastro
        pet = Cadastro.cadastro()
        #armazena o pet no banco de dados
        Banco_De_Dados.armazenar_pets(pet.to_json())
        #salva o banco de dados em um arquivo JSON
        Banco_De_Dados.salvar_pets()


    elif opcao == "2":
        Banco_De_Dados.listar_pets()

    elif opcao == "3":
        Editar_Dados.editar_dados()

    elif opcao == "4":
        Excluir_Pet.excluir_pet()

    elif opcao == "5":
        break

    else:
        print("\nOpção inválida.")