import Banco_De_Dados
import Cadastro

def validar_banco_de_dados():
    if len(Banco_De_Dados.pets) == 0:
        print("\nAINDA NÃO EXISTEM PETS CADASTRADOS")
        resposta = input("Deseja cadastrar um pet? [S/N]").upper()

        while resposta not in ["S", "SIM", "N", "NAO"]:
            print("DIGITE APENAS S OU N")
            resposta = input("Deseja cadastrar um pet? [S/N]").upper()

        if resposta == "S" or resposta == "SIM":
            pet = Cadastro.cadastro()
            Banco_De_Dados.armazenar_pets(pet.to_json())
            Banco_De_Dados.salvar_pets()
            return
        else:
            return
def escolha_do_pet():
    contador = 1
    for pet in Banco_De_Dados.pets:
        print(f"[{contador}] Pet: {pet['nome']}")
        contador += 1

    opcao = input("\nDigite o número do pet: ")

    while True:
        if opcao.isnumeric() == False:
            print("DIGITE APENAS NÚMEROS")
            opcao = input("Digite o número do pet: ")
            continue
        else:
            break

    return int(opcao)
def escolha_dos_dados(opcao):

    if Banco_De_Dados.pets[opcao - 1]["adotado"] == "Sim":
        Banco_De_Dados.pets[opcao - 1]["adotado"] = "Sim"
    else:
        Banco_De_Dados.pets[opcao - 1]["adotado"] = "Não"

    print(f"""
            ╔══════════════════════════════╗
                    PET {opcao}
            ╠══════════════════════════════╣
              1 - Nome     : {Banco_De_Dados.pets[opcao - 1]["nome"]}
              2 - Idade    : {Banco_De_Dados.pets[opcao - 1]["idade"]}
              3 - Raça     : {Banco_De_Dados.pets[opcao - 1]["raca"]}
              4 - Porte    : {Banco_De_Dados.pets[opcao - 1]["porte"]}
              5 - Adotado  : {Banco_De_Dados.pets[opcao - 1]["adotado"]}
            ╚══════════════════════════════╝
            """)
    escolha = input("Qual campo deseja editar? (1, 2, 3, 4, 5) ")
    while not escolha.isnumeric() or int(escolha) not in (1, 2, 3, 4, 5):
        print("DIGITE APENAS NÚMEROS DE 1 A 5!")
        escolha = input("Qual campo deseja editar? (1, 2, 3, 4, 5) ")

    return int(escolha)
def editar_nomes(opcao):
    novo_nome = input("Digite o nome do pet: ")
    Banco_De_Dados.pets[opcao - 1]["nome"] = novo_nome
    print("NOME ATUALIZADO COM SUCESSO!")
def editar_idade(opcao):
    mesORano = input("O pet tem meses ou anos de vida? (M/A): ").strip().upper()

    while mesORano not in ["M", "A"]:
        print("DIGITE APENAS M OU A")
        mesORano = input("O pet tem meses ou anos de vida? (M/A): ").strip().upper()

    if mesORano == "M":
        abreviacao = "meses"
    else:
        abreviacao = "anos"

    idadeNum = input("Digite a idade do pet (Digite apenas os números): ")

    while idadeNum.isnumeric() == False:
        print("DIGITE APENAS NUMEROS")
        idadeNum = input("Digite a idade do pet: ")

    while mesORano == "M" and int(idadeNum) > 11:
        print("UM PET COM MAIS DE 11 MESES DEVE SER CADASTRADO COM ANOS")
        idadeNum = input("Digite a idade do pet (Digite apenas os números): ")

    nova_idade = f"{idadeNum} {abreviacao}"
    Banco_De_Dados.pets[opcao - 1]["idade"] = nova_idade

    print("IDADE ATUALIZADA COM SUCESSO!")
def editar_raca(opcao):
    nova_raca = input("Digite a raça do pet: ")
    Banco_De_Dados.pets[opcao - 1]["raca"] = nova_raca
    print("RAÇA ATUALIZADA COM SUCESSO!")
def editar_porte(opcao):
    print("""
                    Selecione o porte do pet:

                    [1] Pequeno
                    [2] Médio
                    [3] Grande
                    """)

    escolha = input("Digite a opção desejada: ")
    while escolha not in ["1", "2", "3"]:
        print("DIGITE APENAS 1, 2 OU 3")
        escolha = input("Digite a opção desejada: ")

    portes = {
        "1": "Pequeno",
        "2": "Médio",
        "3": "Grande"
    }

    novo_porte = portes[escolha]
    Banco_De_Dados.pets[opcao - 1]["porte"] = novo_porte
    print("PORTE ATUALIZADO COM SUCESSO!")
def editar_status_adocao(opcao):
    pet = Banco_De_Dados.pets[opcao - 1]

    while True:
        resposta = input("Deseja alterar o status do pet? [S/N] ").upper()

        if resposta in ["S", "SIM", "N", "NAO"]:
            break

        print("DIGITE APENAS S OU N")

    if resposta in ["S", "SIM"]:

        if pet["adotado"] == "Não":
            pet["adotado"] = "Sim"
            print("PET ADOTADO!")

        else:
            pet["adotado"] = "Não"
            print("ADOÇÃO REMOVIDA!")


def editar_dados():

    validar_banco_de_dados()

    interromper_Loop = False
    while True:

        print("\nSelecione o pet que deseja editar:\n")

        opcao = escolha_do_pet()

        opcao = int(opcao)
        if opcao < 1 or opcao > len(Banco_De_Dados.pets):
            print("PET NÃO ENCONTRADO")
        else:
            interromper_Loop = True

        if interromper_Loop:
            break

    resposta_do_usuario = "S"
    while resposta_do_usuario == "S" or resposta_do_usuario == "SIM":

        escolha = escolha_dos_dados(opcao)

        if escolha == 1:
            editar_nomes(opcao)
        elif escolha == 2:
            editar_idade(opcao)
        elif escolha == 3:
            editar_raca(opcao)
        elif escolha == 4:
            editar_porte(opcao)
        elif escolha == 5:
            editar_status_adocao(opcao)

        resposta_do_usuario = input("Deseja editar outro dado do pet? [S/N]").upper()
        while resposta_do_usuario not in ["S", "SIM", "N", "NAO"]:
            print("DIGITE APENAS S OU N")
            resposta_do_usuario = input("Deseja editar outro dado do pet? [S/N]").upper()

    Banco_De_Dados.salvar_pets()