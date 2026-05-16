import Banco_De_Dados

def excluir_pet():

    # verifica se existem pets cadastrados
    if len(Banco_De_Dados.pets) == 0:
        print("\nAINDA NÃO EXISTEM PETS CADASTRADOS")
        return

    while True:

        print("\nSelecione o pet que deseja excluir:\n")

        contador = 1

        # lista os pets
        for pet in Banco_De_Dados.pets:
            print(f"[{contador}] Pet: {pet['nome']}")
            contador += 1

        opcao = input("\nDigite o número do pet: ")

        # valida se digitou apenas números
        while opcao.isnumeric() == False:
            print("DIGITE APENAS NÚMEROS")
            opcao = input("Digite o número do pet: ")

        opcao = int(opcao)

        # valida se o número existe na lista
        if opcao < 1 or opcao > len(Banco_De_Dados.pets):
            print("PET NÃO ENCONTRADO")
            continue

        # pega o pet escolhido
        pet_escolhido = Banco_De_Dados.pets[opcao - 1]

        print(f"""
Deseja realmente excluir o pet {pet_escolhido["nome"]}?
Essa ação não pode ser desfeita.

[1] Cancelar
[2] Excluir Pet
""")

        confirmacao = input("Digite a opção desejada: ")

        while confirmacao not in ["1", "2"]:
            print("DIGITE APENAS 1 OU 2")
            confirmacao = input("Digite a opção desejada: ")

        # cancelar
        if confirmacao == "1":
            continue

        # excluir pet
        elif confirmacao == "2":

            Banco_De_Dados.pets.pop(opcao - 1)

            Banco_De_Dados.salvar_pets()

            print(f'\nO pet {pet_escolhido["nome"]} foi excluído com sucesso!')

            return