import pandas as pd

def clean(datos):
    return datos.dropna() 

class Limpiador():
    
    nombre = 'Sin nombre'
    datos = None
    def __init__(self, nombre_personalizado,datos_personzalizados):
        self.nombre = nombre_personalizado
        self.datos = datos_personzalizados

    def clean(self):
        return self.datos.dropna()

if __name__ == '__main__':
    print('Es una libreria de limpieza de datos')