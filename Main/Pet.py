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