import Recomendacao
import Banco_De_Dados

def testar_compatibilidade():
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


        score, motivos = Recomendacao.calcular_score(adotante, pet)

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
    return top3, adotante


def listar_pets_compativeis():

    top3, adotante = testar_compatibilidade()

    print(f"\n3 PETS MAIS COMPATÍVEIS PARA {adotante['nome']}\n")

    contador = 1
    for item in top3:

        pet = item["pet"]
        score = item["score"]
        motivos = item["motivos"]
        selo = Recomendacao.gerar_selo(score)


        print(f"{contador}. Nome: {pet['nome']}, Compatibilidade: {score:.2f}%, Selo: {selo} - Motivos: {', '.join(motivos)}")
        contador += 1
    return adotante, top3


def adotar_por_recomendacao():
    pet_nome = []

    adotante, top3 = listar_pets_compativeis()

    pet_escolhido = int(input("\nDIGITE O NUMERO DO PET QUE DESEJA ADOTAR (OU '-1' PARA VOLTAR): "))

    if pet_escolhido == -1:
        print("OPERAÇÃO CANCELADA.")
        return
    elif pet_escolhido < 1 or pet_escolhido > len(top3):
        print("PET INVÁLIDO. OPERAÇÃO CANCELADA.")
        return
    
    top3[pet_escolhido - 1]["pet"]["adotado"] = True
    pet_nome.append(top3[pet_escolhido - 1]["pet"]["nome"])
    adotante["pets_adotados"] = pet_nome

    print(f"\nPARABÉNS {adotante['nome']}! VOCÊ ADOTOU O PET {pet_nome} POR RECOMENDAÇÃO!")

    Banco_De_Dados.salvar_pets()
    Banco_De_Dados.salvar_adotantes()