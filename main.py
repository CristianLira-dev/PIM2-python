import json

arquivo = "pets.json"
dados = []

class Pet:
    def __init__(self, nome, idade, raca, porte, adotado=False):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.adotado = adotado

    def to_json(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "raca": self.raca,
            "porte": self.porte,
            "adotado": self.adotado
        }
    
pet1 = Pet(
    "Thor",
    "2 anos",
    "Labrador",
    "Grande"
)
pet2 = Pet(
    "Batata",
    "2 anos",
    "Labrador",
    "Grande",
    True
)


dados.append(pet1.to_json())
dados.append(pet2.to_json())

with open(arquivo, "w", encoding="utf-8") as arq:
    json.dump(dados, arq, indent=4, ensure_ascii=False)

print("testar criação do arquivo")
