
# Oscar Alejandro Gómez Suarez
# Lenguajes de Programación

from Computador import Computador

def main():
    computador = Computador()
    conti = True
    print("Para ejecutar el codigo escriba el nombre de archivo a cargar y ejecutar, para salir escriba \'salir\' ")
    archivo = input()
    if archivo == 'salir':
        conti = False
    while conti:
        computador.cargar(archivo)
        computador.ejecutarInstrucciones()
        print("Para ejecutar el codigo escriba el nombre de archivo a cargar y ejecutar, para salir escriba \'salir\' ")
        archivo = input()
        if archivo == 'salir':
            conti = False


if __name__ ==  "__main__":
    main()
    
