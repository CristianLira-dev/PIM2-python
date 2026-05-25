class Pet:

    def __init__(
        self,
        nome,
        idade,
        raca,
        porte,
        energia,
        sociavel_criancas,
        adotado=False
    ):

        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.energia = energia
        self.sociavel_criancas = sociavel_criancas
        self.adotado = adotado

    def to_json(self):

        return {
            "nome": self.nome,
            "idade": self.idade,
            "raca": self.raca,
            "porte": self.porte,
            "energia": self.energia,
            "sociavel_criancas": self.sociavel_criancas,
            "adotado": self.adotado
        }