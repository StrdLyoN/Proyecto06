import pandas as pd

def clean(datos):
    return datos.dropna() 

if __name__ == '__main__':
    print('Es una libreria de limpieza de datos')