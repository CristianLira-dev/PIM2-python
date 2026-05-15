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

    porte = input("Digite o porte do pet: ")

    pet = Pet(nome, idade, raca, porte)

    return pet