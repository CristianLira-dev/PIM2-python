#funcao responsavel por criar o cadastro de pets
def cadastro():
    from Pet import pet

    nome = input("\nDigite o nome do pet: ")

    idade = input("Digite a idade do pet: ")
    while idade.isnumeric() == False:
        print("DIGITE APENAS NUMEROS")
        idade = input("Digite a idade do pet: ")

    raca = input("Digite a raça do pet: ")

    porte = input("Digite o porte do pet: ")

    pet = pet(nome, idade, raca, porte)
    return pet