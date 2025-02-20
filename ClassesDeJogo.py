class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def atacar(self):
        ataques = {
            "mago": "usou magia",
            "guerreiro": "usou espada",
            "monge": "usou artes marciais",
            "ninja": "usou shuriken"
        }
        ataque = ataques.get(self.tipo, "usou um ataque desconhecido")
        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplo de uso:
heroi1 = Heroi("Arthas", 30, "guerreiro")
heroi1.atacar()

heroi2 = Heroi("Merlin", 150, "mago")
heroi2.atacar()

heroi3 = Heroi("Shen", 25, "ninja")
heroi3.atacar()

heroi4 = Heroi("Liu Kang", 28, "monge")
heroi4.atacar()