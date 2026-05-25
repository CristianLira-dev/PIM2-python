from Pet import Pet


def cadastro():

    nome = input("Digite o nome do pet: ").strip()

    while nome == "":
        print("O NOME NÃO PODE FICAR VAZIO")
        nome = input("Digite o nome do pet: ").strip()


    mesORano = input(
        "O pet tem meses ou anos de vida? (M/A): "
    ).strip().upper()

    while mesORano not in ["M", "A"]:

        print("DIGITE APENAS M OU A")

        mesORano = input(
            "O pet tem meses ou anos de vida? (M/A): "
        ).strip().upper()


    abreviacao = "meses" if mesORano == "M" else "anos"


    idadeNum = input("Digite a idade do pet: ")

    while idadeNum.isnumeric() == False:

        print("DIGITE APENAS NÚMEROS")

        idadeNum = input("Digite novamente: ")


    idade = f"{idadeNum} {abreviacao}"


    raca = input("Digite a raça do pet: ").strip()

    while raca == "":
        print("A RAÇA NÃO PODE FICAR VAZIA")
        raca = input("Digite a raça do pet: ").strip()


    print("""
[1] Pequeno
[2] Médio
[3] Grande
""")


    opcao_porte = input("Digite o porte do pet: ")


    while opcao_porte not in ["1", "2", "3"]:

        print("DIGITE APENAS 1, 2 OU 3")

        opcao_porte = input("Digite o porte do pet: ")


    portes = {
        "1": "Pequeno",
        "2": "Médio",
        "3": "Grande"
    }


    porte = portes[opcao_porte]


    print("""
[1] Baixa
[2] Média
[3] Alta
""")


    opcao_energia = input("Digite o nível de energia do seu pet: ")


    while opcao_energia not in ["1", "2", "3"]:

        print("DIGITE APENAS 1, 2 OU 3")

        opcao_energia = input("Digite o nível de energia do seu pet: ")


    energias = {
        "1": "Baixa",
        "2": "Média",
        "3": "Alta"
    }


    energia = energias[opcao_energia]


    resposta = input(
        "O pet é sociável com crianças? [S/N]: "
    ).strip().upper()


    while resposta not in ["S", "SIM", "N", "NAO"]:

        print("DIGITE APENAS S OU N")

        resposta = input(
            "O pet é sociável com crianças? [S/N]: "
        ).strip().upper()


    sociavel_criancas = resposta in ["S", "SIM"]


    pet = Pet(
        nome,
        idade,
        raca,
        porte,
        energia,
        sociavel_criancas
    )


    print("\nPET CADASTRADO COM SUCESSO!")

    return pet