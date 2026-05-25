import json
import os

pets = []
adotantes = []


def armazenar_pets(pet):
    pets.append(pet)


def armazenar_adotante(adotante):
    adotantes.append(adotante)


def listar_pets():

    if len(pets) == 0:
        print("AINDA NÃO EXISTEM PETS CADASTRADOS")
        return

    contador = 1

    for pet in pets:

        adotado = "Sim" if pet["adotado"] else "Não"
        criancas = "Sim" if pet["sociavel_criancas"] else "Não"

        print(f"""
╔══════════════════════════════╗
            PET {contador}
╠══════════════════════════════╣
 Nome        : {pet['nome']}
 Idade       : {pet['idade']}
 Raça        : {pet['raca']}
 Porte       : {pet['porte']}
 Energia     : {pet['energia']}
 Crianças    : {criancas}
 Adotado     : {adotado}
╚══════════════════════════════╝
""")

        contador += 1


def listar_adotantes():

    if len(adotantes) == 0:
        print("AINDA NÃO EXISTEM ADOTANTES CADASTRADOS")
        return

    contador = 1

    for adotante in adotantes:

        print(f"[{contador}] {adotante['nome']}")

        contador += 1


def salvar_pets():

    with open("pets.json", "w", encoding="utf-8") as arquivo:
        json.dump(pets, arquivo, indent=4, ensure_ascii=False)


def carregar_pets():

    if os.path.exists("pets.json"):

        try:

            with open("pets.json", "r", encoding="utf-8") as arquivo:

                dados = json.load(arquivo)

                pets.clear()
                pets.extend(dados)

        except:
            pets.clear()


def salvar_adotantes():

    with open("adotantes.json", "w", encoding="utf-8") as arquivo:
        json.dump(adotantes, arquivo, indent=4, ensure_ascii=False)


def carregar_adotantes():

    if os.path.exists("adotantes.json"):

        try:

            with open("adotantes.json", "r", encoding="utf-8") as arquivo:

                dados = json.load(arquivo)

                adotantes.clear()
                adotantes.extend(dados)

        except:
            adotantes.clear()