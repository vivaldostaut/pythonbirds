class Pessoa:
    def cumprimentar(self):
         return 'Olá'


if __name__ == '__main__':
    p=Pessoa()
    print(type(p))
    print(id(p))
    print(Pessoa.cumprimentar(p))
    print(id((Pessoa.cumprimentar(p))))
    print(p.cumprimentar())
    print(id(p.cumprimentar()))
