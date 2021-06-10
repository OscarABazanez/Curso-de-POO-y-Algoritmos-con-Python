class Helados:

    def __init__(self,nombre,sabor,clave):
        self.nombre = nombre
        self.__sabor = sabor
        self.__clave = clave

    @property
    def sabor(self):
        return self.__sabor
    
    @property
    def clave(self):
        return self.__clave

    @sabor.setter
    def sabor(self,value):
        a = self.__sabor = value
        return a

    @clave.setter
    def clave(self,value):
        self.__clave = value
    
    
helados = Helados('Raton','queso',123)

print(f'Original:',helados.sabor)
helados.sabor = 'amargo'
print(f'Modificado:',helados.sabor)
print('---------------')
print(f'Original:',helados.clave)
helados.clave = 99999
print(f'Modificado:',helados.clave)
print('+++++++++++++++++++++++++')
