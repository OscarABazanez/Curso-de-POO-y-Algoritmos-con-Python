# Problema: Descomponer un Automovil

class Automovil:

    def __init__(self, modelo, marca, color, asiento):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.asiento = asiento
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)


    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = 'en_movimiento'

        return f'Esta {self._estado}'

    
    def caracteristicas(self):
        return f'un Modelo {self.modelo}, de color {self.color} y de {self.asiento} asientos.'


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    
    def inyecta_gasolina(self, cantidad):
        pass


if __name__ == '__main__':
    carro_1 = Automovil('2013','Zowie', 'Rojo',4)
    print(carro_1.acelerar(),carro_1.caracteristicas())