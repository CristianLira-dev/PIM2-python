import Banco_De_Dados
import Cadastro


def validar_banco_de_dados():

    if len(Banco_De_Dados.pets) == 0:

        print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  NENHUM PET CADASTRADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

        resposta = input(
            "Deseja cadastrar um pet agora? [S/N]: "
        ).strip().upper()


        while resposta not in ["S", "SIM", "N", "NAO"]:

            print("❌ Digite apenas S ou N.")

            resposta = input(
                "Deseja cadastrar um pet agora? [S/N]: "
            ).strip().upper()


        if resposta in ["S", "SIM"]:


            pet = Cadastro.cadastro()

            Banco_De_Dados.armazenar_pets(
                pet.to_json()
            )

            Banco_De_Dados.salvar_pets()

            return True

        return False

    return True



def escolha_do_pet():

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐶 PETS DISPONÍVEIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    contador = 1

    for pet in Banco_De_Dados.pets:

        print(f"[{contador}] {pet['nome']}")

        contador += 1


    opcao = input(
        "\n👉 Digite o número do pet que deseja editar: "
    )


    while not opcao.isnumeric():

        print("❌ Digite apenas números.")

        opcao = input(
            "👉 Digite o número do pet que deseja editar: "
        )


    return int(opcao)



def escolha_dos_dados(opcao):

    pet = Banco_De_Dados.pets[opcao - 1]

    criancas = (
        "Sim"
        if pet.get("sociavel_criancas")
        else "Não"
    )

    adotado = (
        "Sim"
        if pet.get("adotado")
        else "Não"
    )

    print(f"""
╔══════════════════════════════╗
         🐾 EDITAR PET
╠══════════════════════════════╣
 1 - Nome        : {pet.get("nome")}
 2 - Idade       : {pet.get("idade")}
 3 - Raça        : {pet.get("raca")}
 4 - Porte       : {pet.get("porte")}
 5 - Energia     : {pet.get("energia")}
 6 - Crianças    : {criancas}
 7 - Adotado     : {adotado}
╚══════════════════════════════╝
""")


    escolha = input(
        "👉 Qual informação deseja editar? (1-7) "
        "\n[8] Sair"
        "\nDigite a opção desejada:   "
    )


    while not escolha.isnumeric() or int(escolha) not in range(1, 9):

        print("❌ Escolha apenas números de 1 a 7.")

        escolha = input(
            "👉 Qual informação deseja editar? (1-7): "
        )


    return int(escolha)



def editar_nome(opcao):

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✏️  ALTERAÇÃO DE NOME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    novo_nome = input(
        "Digite o novo nome do pet: "
    ).strip()


    while novo_nome == "":

        print("❌ O nome não pode ficar vazio.")

        novo_nome = input(
            "Digite o novo nome do pet: "
        ).strip()


    Banco_De_Dados.pets[opcao - 1]["nome"] = novo_nome

    print("✅ Nome atualizado com sucesso!")



def editar_idade(opcao):

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 ALTERAÇÃO DE IDADE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    mesORano = input(
        "O pet possui meses ou anos? [M/A]: "
    ).strip().upper()


    while mesORano not in ["M", "A"]:

        print("❌ Digite apenas M ou A.")

        mesORano = input(
            "O pet possui meses ou anos? [M/A]: "
        ).strip().upper()


    abreviacao = (
        "meses"
        if mesORano == "M"
        else "anos"
    )


    idadeNum = input(
        "Digite a idade do pet: "
    )

    if mesORano == "M":

        while not idadeNum.isnumeric() or not (1 <= int(idadeNum) <= 11):

            print("❌ Digite apenas números entre 1 e 11.")

            idadeNum = input(
                "Digite a idade do pet (1-11 meses): "
            )

    else:

        while not idadeNum.isnumeric():

            print("❌ Digite apenas números.")

            idadeNum = input(
                "Digite a idade do pet: "
            )


    idade = f"{idadeNum} {abreviacao}"

    Banco_De_Dados.pets[opcao - 1]["idade"] = idade

    print("✅ Idade atualizada com sucesso!")



def editar_raca(opcao):

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🐕 ALTERAÇÃO DE RAÇA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    nova_raca = input(
        "Digite a nova raça do pet: "
    ).strip()


    while nova_raca == "":

        print("❌ A raça não pode ficar vazia.")

        nova_raca = input(
            "Digite a nova raça do pet: "
        ).strip()


    Banco_De_Dados.pets[opcao - 1]["raca"] = nova_raca

    print("✅ Raça atualizada com sucesso!")



def editar_porte(opcao):

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📏 ALTERAÇÃO DE PORTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1] Pequeno
[2] Médio
[3] Grande
""")

    escolha = input(
        "👉 Escolha o novo porte: "
    )


    while escolha not in ["1", "2", "3"]:

        print("❌ Digite apenas 1, 2 ou 3.")

        escolha = input(
            "👉 Escolha o novo porte: "
        )


    portes = {
        "1": "Pequeno",
        "2": "Médio",
        "3": "Grande"
    }



    novo_porte = portes[escolha]

    Banco_De_Dados.pets[opcao - 1]["porte"] = novo_porte

    print("✅ Porte atualizado com sucesso!")



def editar_energia(opcao):

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ ALTERAÇÃO DE ENERGIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1] Baixa
[2] Média
[3] Alta
""")

    escolha = input(
        "👉 Escolha o novo nível de energia: "
    )


    while escolha not in ["1", "2", "3"]:

        print("❌ Digite apenas 1, 2 ou 3.")

        escolha = input(
            "👉 Escolha o novo nível de energia: "
        )


    energias = {
        "1": "Baixa",
        "2": "Média",
        "3": "Alta"
    }


    nova_energia = energias[escolha]

    Banco_De_Dados.pets[opcao - 1]["energia"] = nova_energia

    print("✅ Energia atualizada com sucesso!")



def editar_criancas(opcao):

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👶 SOCIÁVEL COM CRIANÇAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    resposta = input(
        "O pet é sociável com crianças? [S/N]: "
    ).strip().upper()


    while resposta not in ["S", "SIM", "N", "NAO"]:

        print("❌ Digite apenas S ou N.")

        resposta = input(
            "O pet é sociável com crianças? [S/N]: "
        ).strip().upper()


    sociavel = resposta in ["S", "SIM"]

    Banco_De_Dados.pets[opcao - 1][
        "sociavel_criancas"
    ] = sociavel

    print("✅ Informação atualizada com sucesso!")



def editar_status_adocao(opcao):

    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏠 STATUS DE ADOÇÃO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

    resposta = input(
        "Deseja marcar o pet como adotado? [S/N]: "
    ).strip().upper()


    while resposta not in ["S", "SIM", "N", "NAO"]:

        print("❌ Digite apenas S ou N.")

        resposta = input(
            "Deseja marcar o pet como adotado? [S/N]: "
        ).strip().upper()


    Banco_De_Dados.pets[opcao - 1][
        "adotado"
    ] = resposta in ["S", "SIM"]


    print("✅ Status de adoção atualizado!")



def editar_dados():

    continuar = validar_banco_de_dados()

    if continuar == False:
        return


    while True:

        print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠️  EDIÇÃO DE PETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

        opcao = escolha_do_pet()


        if opcao < 1 or opcao > len(Banco_De_Dados.pets):

            print("❌ Pet não encontrado.")

        else:
            break


    resposta = "S"


    while resposta in ["S", "SIM"]:

        escolha = escolha_dos_dados(opcao)


        if escolha == 1:

            editar_nome(opcao)

        elif escolha == 2:

            editar_idade(opcao)

        elif escolha == 3:

            editar_raca(opcao)

        elif escolha == 4:

            editar_porte(opcao)

        elif escolha == 5:

            editar_energia(opcao)

        elif escolha == 6:

            editar_criancas(opcao)

        elif escolha == 7:

            editar_status_adocao(opcao)

        elif escolha == 8:
            return


        Banco_De_Dados.salvar_pets()


        resposta = input(
            "\nDeseja editar outro dado deste pet? [S/N]: "
        ).strip().upper()


        while resposta not in ["S", "SIM", "N", "NAO"]:

            print("❌ Digite apenas S ou N.")

            resposta = input(
                "Deseja editar outro dado deste pet? [S/N]: "
            ).strip().upper()


    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ ALTERAÇÕES FINALIZADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")