import Banco_De_Dados


def gerar_selo(score):

    if score >= 80:
        return "🟢 Alta Compatibilidade"

    elif score >= 50:
        return "🟡 Média Compatibilidade"

    else:
        return "🔴 Baixa Compatibilidade"


def calcular_score(adotante, pet):

    score = 0
    motivos = []


    if adotante["preferencia_porte"] == pet["porte"]:

        score += 30
        motivos.append("+30 Compatibilidade de porte")

    elif adotante["preferencia_porte"] == "Tanto Faz":

        score += 15
        motivos.append("+15 Sem preferência de porte")


    if adotante["preferencia_energia"] == pet["energia"]:

        score += 30
        motivos.append("+30 Compatibilidade de energia")


    if adotante["possui_criancas"]:

        if pet["sociavel_criancas"]:

            score += 20
            motivos.append("+20 Sociável com crianças")

    else:
        score += 10


    if adotante["experiencia"] == "Experiente":

        score += 20
        motivos.append("+20 Experiência com pets")


    return score, motivos


def recomendar_pet():

    if len(Banco_De_Dados.adotantes) == 0:
        print("AINDA NÃO EXISTEM ADOTANTES CADASTRADOS")
        return


    if len(Banco_De_Dados.pets) == 0:
        print("AINDA NÃO EXISTEM PETS CADASTRADOS")
        return


    print("\nSELECIONE O ADOTANTE:\n")


    contador = 1

    for adotante in Banco_De_Dados.adotantes:

        print(f"[{contador}] {adotante['nome']}")

        contador += 1


    opcao = input("\nDigite a opção desejada: ")


    while not opcao.isnumeric():

        print("DIGITE APENAS NÚMEROS")

        opcao = input("Digite a opção desejada: ")


    opcao = int(opcao)


    if opcao < 1 or opcao > len(Banco_De_Dados.adotantes):

        print("ADOTANTE NÃO ENCONTRADO")
        return


    adotante = Banco_De_Dados.adotantes[opcao - 1]

    ranking = []


    for pet in Banco_De_Dados.pets:

        if pet["adotado"]:
            continue


        score, motivos = calcular_score(adotante, pet)

        ranking.append({
            "pet": pet,
            "score": score,
            "motivos": motivos
        })


    ranking.sort(
        key=lambda item: item["score"],
        reverse=True
    )


    top3 = ranking[:3]


    print("\nTOP 3 PETS MAIS COMPATÍVEIS\n")


    for item in top3:

        pet = item["pet"]
        score = item["score"]
        motivos = item["motivos"]

        if {pet['sociavel_criancas']}:
            criancas = "Sim"
        else:
            criancas = "Não"

        selo = gerar_selo(score)

        print(f"""
══════════════════════════════
PET: {pet['nome']}
══════════════════════════════
Compatibilidade: {score}%
{selo}

Idade: {pet['idade']}
Raça: {pet['raca']}
Porte: {pet['porte']}
Energia: {pet['energia']}
Sociável c/ crianças: {criancas}


Motivos:
""")


        for motivo in motivos:
            print(motivo)
