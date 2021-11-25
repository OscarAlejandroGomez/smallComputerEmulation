from Registro import Registro as re
from ALU import ALU
from Memoria import Memoria
from UnidadControl import UnidadControl
from Cargador import Cargador

class Computador:
    def __init__(self):
        regA = re('A', [0,0])
        regB = re('B', [0,1])
        regC = re('C', [1,0])
        regD = re('D', [1,1])
        self.registros = []
        self.registros.append(regA)
        self.registros.append(regB)
        self.registros.append(regC)
        self.registros.append(regD)
        self.alu = ALU()
        self.memoria = Memoria()
        self.unidadControl = None 
        self.memDatos = 100    # Valor escogido arbitrariamente para guardar varibles
        self.memProg = 0        

    # Imprimir los valores almacenados en los registros A B C D
    def impReg(self):
        for i in self.registros:
            print(i.nombre, "   ",i.palabra, "   ", i.iden)  
    
    #Carga desde un archivo en assembler dado un nombre
    def cargar(self, archivo):
        cargador = Cargador(archivo,self.memDatos)
        cargador.interpretarReloc()
        self.memProg = int(cargador.cargarMemoria(self.memoria))
        self.unidadControl = UnidadControl(self.memoria, self.registros, self.alu, self.registros, self.memDatos, self.memProg)
        
        
        

    def decimalBinario(self, numero):
        palabra = bin(numero).replace("0b", "")
        word =  list(palabra)
        for i in range(0,len(word)):    #Convierte a entero el arreglo
            word[i] = int(word[i])
        resArr = [0,0,0,0,0,0,0,0,0,0]
        num = 9
        for i in reversed(word):
            resArr[num] = i
            num -=1
        return resArr

    #Ejecutar desde la posicion de memoria especificada
    def ejecutarInstrucciones(self):
        codigoDir = self.decimalBinario(self.memProg)
        self.unidadControl.ejecutar(codigoDir)