# funcao responsavel por criar o cadastro de pets
def cadastro():

    from Pet import Pet

    nome = input("\nDigite o nome do pet: ")

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

    idade = f"{idadeNum} {abreviacao}"

    raca = input("Digite a raça do pet: ")

    # SELETOR DE PORTE

    print("""
    Selecione o porte do pet:

    [1] Pequeno
    [2] Médio
    [3] Grande
    """)

    opcao = input("Digite a opção desejada: ")

    while opcao not in ["1", "2", "3"]:
        print("DIGITE APENAS 1, 2 OU 3")
        opcao = input("Digite a opção desejada: ")

    portes = {
        "1": "Pequeno",
        "2": "Médio",
        "3": "Grande"
    }

    porte = portes[opcao]

    print("\nCadastro concluído com sucesso!")

    pet = Pet(nome, idade, raca, porte)

    return pet