
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'{self.nombre} Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre,modelo=None):
        self.modelo = modelo
        super().__init__(nombre)
    

    def avanza(self):
        print(f'Ando moviendome en mi bicicleta {self.modelo}')


def main():
    persona = Persona(nombre='Oscar')
    persona.avanza()

    ciclista = Ciclista(nombre='Pedro',modelo='BMW')
    ciclista.avanza()


if __name__ == '__main__':
    main()