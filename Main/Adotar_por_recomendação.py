import Recomendacao
import Banco_De_Dados

def testar_compatibilidade():
    
    if not Banco_De_Dados.adotantes:
        print("\n❌ AINDA NÃO EXISTEM ADOTANTES CADASTRADOS.")
        return None, None

    if not Banco_De_Dados.pets:
        print("\n❌ AINDA NÃO EXISTEM PETS CADASTRADOS.")
        return None, None

    
    print("\n" + "="*30)
    print("      SELECIONE O ADOTANTE      ")
    print("="*30)
    contador = 1
    for adotante in Banco_De_Dados.adotantes:
        print(f"{contador}. {adotante['nome']}")
        contador += 1
    print("="*30)

    
    while True:
        opcao = input("\nDigite o número do adotante desejado: ").strip()
        if opcao.isdigit():
            opcao = int(opcao)
            if 1 <= opcao <= len(Banco_De_Dados.adotantes):
                break
        print("⚠️ OPÇÃO INVÁLIDA! Por favor, escolha um número da lista.")

    adotante = Banco_De_Dados.adotantes[opcao - 1]
    ranking = []

    
    for pet in Banco_De_Dados.pets:
        if pet.get("adotado", False):
            continue

        score, motivos = Recomendacao.calcular_score(adotante, pet)
        ranking.append({
            "pet": pet,
            "score": score,
            "motivos": motivos
        })

    
    ranking.sort(key=lambda item: item["score"], reverse=True)
    
    
    return ranking[:3], adotante


def listar_pets_compativeis():
    top3, adotante = testar_compatibilidade()
    
    
    if not top3:
        return None, None

    print("\n" + "="*50)
    print(f"🐾 3 PETS MAIS COMPATÍVEIS PARA: {adotante['nome'].upper()} 🐾")
    print("="*50)

    if not top3:
        print("Nenhum pet disponível para recomendação no momento.")
        return top3, adotante

    for i, item in enumerate(top3, 1):
        pet = item["pet"]
        score = item["score"]
        motivos = item["motivos"]
        selo = Recomendacao.gerar_selo(score)

        print(f"{i}️⃣  {pet['nome']}")
        print(f"   📊 Compatibilidade: {score:.1f}% | Selo: {selo}")
        print(f"   💡 Motivos: {', '.join(motivos)}")
        print("-" * 50)
        
    return adotante, top3


def adotar_por_recomendacao():
    adotante, top3 = listar_pets_compativeis()
    
    
    if not adotante or not top3:
        return

    while True:
        try:
            entrada = input("\n👉 Digite o NÚMERO do pet para adotar (ou '-1' para VOLTAR): ").strip()
            pet_escolhido = int(entrada)
            
            if pet_escolhido == -1:
                print("\n❌ OPERAÇÃO CANCELADA PELO USUÁRIO.")
                return
                
            if 1 <= pet_escolhido <= len(top3):
                break
            
            print(f"⚠️ Número inválido. Escolha entre 1 e {len(top3)} (ou -1 para voltar).")
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números.")

    
    item_selecionado = top3[pet_escolhido - 1]
    pet = item_selecionado["pet"]

    
    pet["adotado"] = True
    pet["adotante"] = adotante["nome"]
    
    
    if "pets_adotados" not in adotante or not isinstance(adotante["pets_adotados"], list):
        adotante["pets_adotados"] = []
    adotante["pets_adotados"].append(pet["nome"])


    print(f" 🎉 PARABÉNS, {adotante['nome'].upper()}!")
    print(f" Você acabou de adotar o(a) {pet['nome']} por recomendação! ❤️")

    
    Banco_De_Dados.salvar_pets()
    Banco_De_Dados.salvar_adotantes()