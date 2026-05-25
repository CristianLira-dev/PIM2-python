import Banco_De_Dados


def excluir_pet():

    if len(Banco_De_Dados.pets) == 0:
        print("AINDA NÃO EXISTEM PETS CADASTRADOS")
        return


    contador = 1

    for pet in Banco_De_Dados.pets:

        print(f"[{contador}] Pet: {pet['nome']}")

        contador += 1


    opcao = input("Digite o número do pet: ")


    while not opcao.isnumeric():

        print("DIGITE APENAS NÚMEROS")

        opcao = input("Digite o número do pet: ")


    opcao = int(opcao)


    if opcao < 1 or opcao > len(Banco_De_Dados.pets):

        print("PET NÃO ENCONTRADO")
        return


    pet_escolhido = Banco_De_Dados.pets[opcao - 1]


    print(f"""
Deseja realmente excluir o pet {pet_escolhido['nome']}?

[1] Cancelar
[2] Excluir Pet
""")


    confirmacao = input("Digite a opção desejada: ")


    while confirmacao not in ["1", "2"]:

        print("DIGITE APENAS 1 OU 2")

        confirmacao = input("Digite a opção desejada: ")


    if confirmacao == "2":

        Banco_De_Dados.pets.pop(opcao - 1)

        Banco_De_Dados.salvar_pets()

        print("PET EXCLUÍDO COM SUCESSO!")

    else:
        print("EXCLUSÃO CANCELADA")