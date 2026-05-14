def cadastro():
    nome = input("\nDigite o nome do pet: ")
    idade = input("Digite a idade do pet: ")
    raca = input("Digite a raça do pet: ")
    porte = input("Digite o porte do pet: ")

    dicionario = {"nome": nome, "idade": idade, "raca": raca, "porte": porte}
    return dicionario