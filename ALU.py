
from sys import exit

class ALU:
    # Inicializador
    def __init__(self):
        self.ALUregs = []
        regc = ['C', 0]        # Resultado Cero          0
        regp = ['P', 0]        # Resultado Positivo      1
        regn = ['N', 0]        # Resultado Negativo      2
        regd = ['D', 0]        # Resultado Incontenible  3
        self.ALUregs.append(regc)
        self.ALUregs.append(regp)
        self.ALUregs.append(regn)
        self.ALUregs.append(regd)

    # Suma de dos registros, el resultado se almacena en el primer registro 
    def suma(self, regIni, regFin):
        self.actualizarRegs()
        val1 = regIni.obtenerDecimal()
        val2 = regFin.obtenerDecimal()
        res = val1+val2    
        self.verificarRegs(res)
        regIni.setPalabraDecimal(res)

    # Resta de dos registros, el resultado se almacena en el primer registro 
    def resta(self, regIni, regFin):
        self.actualizarRegs()
        val1 = regIni.obtenerDecimal()
        val2 = regFin.obtenerDecimal()
        res = val1-val2
        self.verificarRegs(res)
        regIni.setPalabraDecimal(res)       

    # Realiza la división entera, guarda el resultado en el primer registro y el residuo en el segundo
    def division(self, regIni, regFin):
        self.actualizarRegs()
        val1 = regIni.obtenerDecimal()
        val2 = regFin.obtenerDecimal()
        if val2 == 0:
            print("Division por 0, se detiene el programa")
            exit()
        res = val1 // val2
        self.verificarRegs(res)
        residuo = val1 % val2
        regIni.setPalabraDecimal(res) 
        regFin.setPalabraDecimal(residuo)

    # Multiplica y guarda el resultado en el primero de los registros
    def multi(self, regIni, regFin):
        self.actualizarRegs()
        val1 = regIni.obtenerDecimal()
        val2 = regFin.obtenerDecimal()
        res = val1 * val2
        self.verificarRegs(res)
        regIni.setPalabraDecimal(res) 

    # Limpia los resultados de los registros
    def actualizarRegs(self):
        for i in self.ALUregs:
            i[1] = 0

    #Permite imprimir los registros de la ALU
    def imprimirRegs(self):
        for i in self.ALUregs:
            print(i[0],"   ", i[1])     

    # Permite actualizar con los valores actuales a los registros
    def verificarRegs(self, valor):
        if valor > 32767 or valor < -32767:
            self.ALUregs[3][1] = 1 
        elif valor == 0:
            self.ALUregs[0][1] = 1
        elif valor > 0:
            self.ALUregs[1][1] = 1
        elif valor < 0:
            self.ALUregs[2][1] = 1    