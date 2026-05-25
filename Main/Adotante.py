class Adotante:

    def __init__(
        self,
        nome,
        moradia,
        tempo_disponivel,
        experiencia,
        possui_criancas,
        preferencia_porte,
        preferencia_energia
    ):

        self.nome = nome
        self.moradia = moradia
        self.tempo_disponivel = tempo_disponivel
        self.experiencia = experiencia
        self.possui_criancas = possui_criancas
        self.preferencia_porte = preferencia_porte
        self.preferencia_energia = preferencia_energia

    def to_json(self):
        return {
            "nome": self.nome,
            "moradia": self.moradia,
            "tempo_disponivel": self.tempo_disponivel,
            "experiencia": self.experiencia,
            "possui_criancas": self.possui_criancas,
            "preferencia_porte": self.preferencia_porte,
            "preferencia_energia": self.preferencia_energia
        }