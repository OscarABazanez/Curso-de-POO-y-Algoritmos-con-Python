class Coordenadas:


    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def distancia(self, otra_cordenada):
        x_diff = (self.x - otra_cordenada.x)**2
        y_diff = (self.y - otra_cordenada.y)**2

        return(x_diff + y_diff)**0.5


    def multiplicacion(self, otra_cordenada):
        return self.x*self.y

if __name__ == '__main__':

    coord_1 = Coordenadas(3,30)
    coord_2 = Coordenadas(4,8)
    coord_multi = Coordenadas(10,20)
    a = 1+1

    print('Esta a una distancia de: ',coord_1.distancia(coord_2))
    print('La * de la coordenadas es: ',coord_multi.multiplicacion(coord_multi))

    # Metodo isinstance (Nos ayuda a determinar)
    print('a = 1+1 Es una instancia?',isinstance(a,Coordenadas))
    print('coord_1 = Coordenadas(3,30) Es una instancia?',isinstance(coord_2,Coordenadas))