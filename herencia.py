
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    
    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):

    def __init__(self, lado):
        # Nuestra base y altura es igual a nuestro lado
        super().__init__(lado, lado)


def figuras_geometricas():
    rectangulo = Rectangulo(base=3,altura=4)
    print(f'Usando el padre: {rectangulo.area()}')

    cuadrado = Cuadrado(lado=5)
    print(f'Usando el hijo: {cuadrado.area()}')

        
class Estudiante:
    
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera

    
    def identificacion(self):
        return f'{self.nombre} es un estudiante de {self.carrera} y su matricula es {self.matricula}'


class NivelAcademicoSuperior(Estudiante):

    def __init__(self, nombre, matricula, carrera):
        super().__init__(nombre,matricula, carrera)


def info_estudiantes():
    estudiante = Estudiante(nombre='Oscar',matricula=321, carrera='Universidad')
    print(estudiante.identificacion())
    
    nivel_academico = NivelAcademicoSuperior(carrera='Preparatoria',nombre='Daniela',matricula=999)
    print(nivel_academico.identificacion())

if __name__ == "__main__":
    # figuras_geometricas()
    info_estudiantes()