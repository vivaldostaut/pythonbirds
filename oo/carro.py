
"""
Voce deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor tera a responsabilidade de controlar a velocidade. Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que devera incrementar a velocidadae de uma unidade
3) Metodo frear que devera decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção como valores ppossiveis Norte, Sul , Leste e Oeste
2) Método girar_a_direita
3) Método girar a esquerda

  N
O   L
  S
    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Tetando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

NORTE='Norte'
LESTE='Leste'
SUL='Sul'
OESTE='Oeste'


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        return

    def frear(self):
        self.velocidade -= 2
        if self.velocidade <= 0:
            self.velocidade = 0
        return

class Direcao:
    bussola_dct={1:NORTE, 2:LESTE, 3:SUL, 4:OESTE}

    def __init__(self):
        self.valor = NORTE
        self.posicao = 1

    def girar_a_direita(self):
        self.posicao += 1
        if self.posicao == 5:
            self.posicao = 1
        self.valor = self.bussola_dct[self.posicao]
        # if self.valor == NORTE:
        #     self.valor = LESTE
        # elif self.valor == LESTE:
        #     self.valor = SUL
        # elif self.valor == SUL:
        #     self.valor = OESTE
        # elif self.valor == OESTE:
        #     self.valor = NORTE
        return

    def girar_a_esquerda(self):
        self.posicao -= 1
        if self.posicao == 0:
            self.posicao = 4
        self.valor = self.bussola_dct[self.posicao]
        # if self.valor == NORTE:
        #     self.valor = OESTE
        # elif self.valor == OESTE:
        #     self.valor = SUL
        # elif self.valor == SUL:
        #     self.valor = LESTE
        # elif self.valor == LESTE:
        #     self.valor = NORTE
        return

motor = Motor()
direcao = Direcao()

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor


if __name__ == '__main__':
    print(direcao.valor)
    print(motor.velocidade)
    motor.acelerar()
    direcao.girar_a_direita()
    print(direcao.valor)
    print(motor.velocidade)

