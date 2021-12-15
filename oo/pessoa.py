class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
         return f'Olá {self.nome}, {self.idade}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro Felipe', idade=27)
    ana = Pessoa(nome='Ana Beatrice', idade=23)
    staut = Pessoa(ana,pedro, nome='Vivaldo Staut', idade=50)
    solange = Pessoa(ana,pedro, nome='Solange Staut', idade=51)

    print()
    print(staut.cumprimentar())
    for filho in staut.filhos:
        print(f'- Filho: {filho.nome}')

    print()
    print(solange.cumprimentar())
    for filho in solange.filhos:
        print(f'- Filho: {filho.nome}')

    print()
    print(pedro.cumprimentar())
    for filho in pedro.filhos:
        print(f'- Filho: {filho.nome}')

    print()
    print(ana.cumprimentar())
    for filho in ana.filhos:
        print(f'- Filho: {filho.nome}')

    print(staut.__dict__)
    print(solange.__dict__)
    print(pedro.__dict__)
    print(ana.__dict__)
    print()
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())
