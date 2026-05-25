from Adotante import Adotante


def cadastrar_adotante():

    nome = input("Digite o nome do adotante: ").strip()

    while nome == "":
        print("O NOME NÃO PODE FICAR VAZIO")
        nome = input("Digite o nome do adotante: ").strip()


    print("""
[1] Casa
[2] Apartamento
""")


    opcao_moradia = input("Você reside em quais dessas opções?: ")


    while opcao_moradia not in ["1", "2"]:

        print("DIGITE APENAS 1 OU 2")

        opcao_moradia = input("Você reside em quais dessas opções?: ")


    moradias = {
        "1": "Casa",
        "2": "Apartamento"
    }


    moradia = moradias[opcao_moradia]


    print("""
[1] Baixo
[2] Médio
[3] Alto
""")


    opcao_tempo = input("Digite a quantidade de tempo disponível para o seu pet: ")


    while opcao_tempo not in ["1", "2", "3"]:

        print("DIGITE APENAS 1, 2 OU 3")

        opcao_tempo = input("Digite a quantidade de tempo disponível para o seu pet: ")


    tempos = {
        "1": "Baixo",
        "2": "Médio",
        "3": "Alto"
    }


    tempo_disponivel = tempos[opcao_tempo]


    print("""
[1] Iniciante
[2] Intermediário
[3] Experiente
""")


    opcao_experiencia = input("Digite seu nível de experiências com pets: ")


    while opcao_experiencia not in ["1", "2", "3"]:

        print("DIGITE APENAS 1, 2 OU 3")

        opcao_experiencia = input("Digite seu nível de experiências com pets: ")


    experiencias = {
        "1": "Iniciante",
        "2": "Intermediário",
        "3": "Experiente"
    }


    experiencia = experiencias[opcao_experiencia]


    resposta = input(
        "Possui crianças em casa? [S/N]: "
    ).strip().upper()


    while resposta not in ["S", "SIM", "N", "NAO"]:

        print("DIGITE APENAS S OU N")

        resposta = input(
            "Possui crianças em casa? [S/N]: "
        ).strip().upper()


    possui_criancas = resposta in ["S", "SIM"]


    print("""
[1] Pequeno
[2] Médio
[3] Grande
[4] Tanto Faz
""")


    opcao_porte = input("Digite a opção de porte desejada: ")


    while opcao_porte not in ["1", "2", "3", "4"]:

        print("DIGITE APENAS 1, 2, 3 OU 4")

        opcao_porte = input("Digite a opção de porte desejada: ")


    portes = {
        "1": "Pequeno",
        "2": "Médio",
        "3": "Grande",
        "4": "Tanto Faz"
    }


    preferencia_porte = portes[opcao_porte]


    print("""
[1] Baixa
[2] Média
[3] Alta
""")


    opcao_energia = input("Digite o nível de energia que você deseja em seu pet: ")


    while opcao_energia not in ["1", "2", "3"]:

        print("DIGITE APENAS 1, 2 OU 3")

        opcao_energia = input("Digite o nível de energia que você deseja em seu pet: ")


    energias = {
        "1": "Baixa",
        "2": "Média",
        "3": "Alta"
    }


    preferencia_energia = energias[opcao_energia]


    adotante = Adotante(
        nome,
        moradia,
        tempo_disponivel,
        experiencia,
        possui_criancas,
        preferencia_porte,
        preferencia_energia
    )


    print("\nADOTANTE CADASTRADO COM SUCESSO!")

    return adotante