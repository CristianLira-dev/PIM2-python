

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