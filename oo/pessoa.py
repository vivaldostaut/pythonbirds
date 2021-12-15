class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
         return f'Olá {self.nome}, {self.idade}'


if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro Felipe', idade=27)
    ana = Pessoa(nome='Ana Beatrice', idade=23)
    staut = Pessoa(ana,pedro, nome='Vivaldo Staut', idade=50)

    print(staut.cumprimentar())
    for filho in staut.filhos:
        print(filho.nome)
