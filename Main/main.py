import Cadastro
import Cadastro_Adotante
import Banco_De_Dados
import Recomendacao
import Excluir_Pet
import Editar_Dados


Banco_De_Dados.carregar_pets()
Banco_De_Dados.carregar_adotantes()


while True:

    print("""

----------------------------------
 SISTEMA DE ADOÇÃO INTELIGENTE
----------------------------------

1 - Cadastrar Pet
2 - Listar Pets
3 - Editar Pet
4 - Excluir Pet
5 - Cadastrar Adotante
6 - Recomendar Pet
7 - Sair
""")


    opcao = input("Digite a opção desejada: ")


    if opcao == "1":

        pet = Cadastro.cadastro()

        Banco_De_Dados.armazenar_pets(
            pet.to_json()
        )

        Banco_De_Dados.salvar_pets()


    elif opcao == "2":

        Banco_De_Dados.listar_pets()


    elif opcao == "3":

        Editar_Dados.editar_dados()


    elif opcao == "4":

        Excluir_Pet.excluir_pet()


    elif opcao == "5":

        adotante = Cadastro_Adotante.cadastrar_adotante()

        Banco_De_Dados.armazenar_adotante(
            adotante.to_json()
        )

        Banco_De_Dados.salvar_adotantes()


    elif opcao == "6":

        Recomendacao.recomendar_pet()


    elif opcao == "7":

        print("ENCERRANDO SISTEMA...")
        break


    else:
        print("OPÇÃO INVÁLIDA")