
class UnidadControl:
    def __init__(self,memoria, registros, alu, regC, memDatos, memProg):
        self. regs = []
        regCP = ["IC", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]     # Instrucción en curso     0
        regIC = ["CP", [0,0,0,0,0,0,0,0,0,0]]                 # Contador de programa     1
        self.regs.append(regCP)
        self.regs.append(regIC)
        self.memoria = memoria
        self.registros = registros
        self.alu = alu
        self.SR = [0,0,0,0,0,0,1,1,1,1]   #La pila iniciara desde la posicion 15 de la memoria
        self.regC  = regC
        self.memDatos = memDatos
        self.memProg = memProg

    # Permite imprimir los registros, su nombre y el valor almacenado
    def imprimirRegs(self):
        for i in self.regs:
            print(i[0], "    ", i[1])    

    #Obtiene la palabra en binario de un registro de memoria
    def obtenerPalabra(self, direc):
        word = ''
        for i in range(0, len(direc)):
            word += str(direc[i])   
        return word

    def obtenerPalabra16(self, direc):
        word = ''
        for i in range(1, len(direc)):
            word += str(direc[i])    
        return word

    #Obtiene el numero decimal de una palabra en binario, sirve para comunicarse con la memoria
    def binarioDecimal(self, binario):
        if len(binario) > 11:
            valor = int(self.obtenerPalabra16(binario), 2)
            if binario[0] == 1:
                valor *= -1
            return valor
        palabra = self.obtenerPalabra(binario)
        return int(palabra,2)

    #Obtiene la lista en binario, dado un numero decimal 
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

    #Aumenta el contador del programa en una unidad
    def aumentarPos(self):
        val = self.binarioDecimal(self.regs[1][1])
        val += 1
        self.regs[1][1] = self.decimalBinario(val)

    #Disminuye en una unidad el contador del programa
    def disminuirPos(self):
        val = self.binarioDecimal(self.regs[1][1])
        val -= 1
        self.regs[1][1] = self.decimalBinario(val)

    # Hace que el contador salte a la posicion especificada
    def saltar(self, direc):
        self.regs[1][1] = direc

    #Extrae la instruccion del contador del programa CP y la guarda en la instruccion en curso IC
    def extraer(self):
        direccion = self.binarioDecimal(self.regs[1][1])
        self.regs[0][1] = self.memoria.getCode(direccion)
    
    # Verifica si el codigo es de cargar
    def testCargar(self, instr):
        codigo = [0, 0, 0, 1]
        cargar = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                cargar = False
                break
        return cargar
    
    # Verifica si el codigo es el de cargar valor
    def testCargarValor(self, instr):
        codigo = [0, 0, 1, 0]
        cargarValor = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                cargarValor = False
                break
        return cargarValor

    # Verifica si el codigo es de almacenar un valor
    def testAlmacenar(self, instr):
        codigo = [0, 0, 1, 1]
        almacenar = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                almacenar = False
                break
        return almacenar

    # Verifica si el codigo es de saltar si 0
    def testSaltarSiCero(self, instr):
        codigo = [0, 1, 0, 0, 0, 0]
        saltarCero = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                saltarCero = False
                break
        return saltarCero
    
    # Verifica si el codigo es saltar si el numero es negativo 
    def testSaltarSiNeg(self, instr):
        codigo = [0, 1, 0, 0, 0, 1]
        saltarNeg = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                saltarNeg = False
                break
        return saltarNeg

    # Verifica si el codigo es de saltar si es positivo
    def testSaltarSiPos(self, instr):
        codigo = [0, 1, 0, 0, 1, 0]
        saltarPos = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                saltarPos = False
                break
        return saltarPos    

    # Verifica si el codigo es de saltar si desbordamiento
    def testSaltarSiDes(self, instr):
        codigo = [0, 1, 0, 0, 1, 1]
        saltarDes = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                saltarDes = False
                break
        return saltarDes 

    # Verifica si el codigo es de saltar sin ninguna condicion.
    def testSaltar(self, instr):
        codigo = [0, 1, 0, 1, 0, 0]
        saltar = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                saltar = False
                break
        return saltar     

    # Verifica si el codigo es de Copiar
    def testCopiar(self, instr):
        codigo = [0, 1, 1, 0,  0,0,0,0 ,0,0,0,0 ]
        copiar = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                copiar = False
                break
        return copiar

    # Verifica si el codigo es de Sumar
    def testSumar(self, instr):
        codigo = [0, 1, 1, 0,  0,0,0,0 ,0,0,0,1 ]
        sumar = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                sumar = False
                break
        return sumar

    # Verifica si el codigo es de Restar
    def testRestar(self, instr):
        codigo = [0, 1, 1, 0,  0,0,0,0 ,0,0,1,0]
        restar = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                restar = False
                break
        return restar  

    # Verifica si el codigo es de Multiplicar
    def testMultiplicar(self, instr):
        codigo = [0, 1, 1, 0,  0,0,0,0 ,0,0,1,1]
        multi = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                multi = False
                break
        return multi

    # Verifica si el codigo es de Multiplicar
    def testDividir(self, instr):
        codigo = [0, 1, 1, 0,  0,0,0,0 ,0,1,0,0]
        div = True
        for i in range(0, len(codigo)):
            if  instr[i] != codigo[i]:
                div = False
                break
        return div

    # Verifica si se trata de una standar output
    def testSalida(self, instr):
        codigo = [0, 1, 1, 1,  0,1]
        salida = True
        for i in range(0, len(codigo)):
            if instr[i] != codigo[i]:
                salida = False
                break
        return salida 
    
    # Verifica si se trata de una standar output
    def testEntrada(self, instr):
        codigo = [0, 1, 1, 1,  1,0]
        entrada = True
        for i in range(0, len(codigo)):
            if instr[i] != codigo[i]:
                entrada = False
                break
        return entrada 
    
    #Verificar si la instruccion es de Pop del Stack
    def testPop(self, instr):
        codigo = [1,0,0,0, 0,0,0,0, 0,0,0,0, 0,1]
        pop = True
        for i in range(0, len(codigo)):
            if instr[i] != codigo[i]:
                pop = False
                break
        return pop

    #Verificar si la instruccion es de push del stack
    def testPush(self, instr):
        codigo = [1,0,0,0, 0,0,0,0, 0,0,0,0, 1,1]
        push = True
        for i in range(0, len(codigo)):
            if instr[i] != codigo[i]:
                push = False
                break
        return push

    # Funcion que toma la instruccion almacena en el CP y la traduce a lo que pueda ejecutar el computador
    def decodificar(self):
        instr = self.regs[0][1]
        if self.testCargar(instr):
            self.cargarCo(instr)
        elif self.testCargarValor(instr):
            self.cargarValorCo(instr)
        elif self.testAlmacenar(instr):
            self.almacenarCo(instr)
        elif self.testSaltarSiCero(instr):
            if self.alu.ALUregs[0][1] == 1:
                self.saltarCo(instr)
        elif self.testSaltarSiNeg(instr):
            if self.alu.ALUregs[2][1] == 1:
                self.saltarCo(instr)
        elif self.testSaltarSiPos(instr):
            if self.alu.ALUregs[1][1] == 1:
                self.saltarCo(instr)
        elif self.testSaltarSiDes(instr):
            if self.alu.ALUregs[3][1] == 1:
                self.saltarCo(instr)
        elif self.testSaltar(instr):
            self.saltarCo(instr)
        elif self.testCopiar(instr):
            self.copiarCo(instr)
        elif self.testSumar(instr):
            self.sumarCo(instr)
        elif self.testRestar(instr):
            self.restaCo(instr)
        elif self.testMultiplicar(instr):
            self.multiCo(instr)
        elif self.testDividir(instr):
            self.dividirCo(instr)
        elif self.testSalida(instr):
            self.salidaCo(instr)
        elif self.testEntrada(instr):
            self.entradaCo(instr)
        elif self.testPop(instr):
            self.popCo(instr)
        elif self.testPush(instr):
            self.pushCo(instr)
        elif instr == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
            print("Ejecucion finalizada")
            exit()
        else:
            print(" es un numero") 

    #Realiza la accion de cargar en un registro el contenido de una direccion de memoria 
    def cargarCo(self, instr):
        reg = [instr[4], instr[5]]
        mem = [0,0,0,0,0,0,0,0,0,0]
        num = 6
        for i in range(0,10):  # Se guarda en mem la direccion que esta en la instruccion 
            mem[i] = instr[num]
            num += 1   
        for i in self.registros:
            if i.iden == reg:
                i.palabra = self.memoria.getCode(self.binarioDecimal(mem))

    #Realiza la accion de cargar en un registro el contenido de un v
    def cargarValorCo(self, instr):
        reg = [instr[4], instr[5]]
        valor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        num = 6   # Esto deberia comenzar desde 6
        for i in range(0,10):   # Se guarda en valor el que esta en la instruccion
            valor[num] = instr[num]
            num += 1
        for i in self.registros:
            if i.iden == reg:
                i.palabra = valor

    # Almacena el contenido del registro en la celda de memoria especificado
    def almacenarCo(self, instr):
        reg = [instr[4], instr[5]]
        mem = [0,0,0,0,0,0,0,0,0,0]
        num = 6
        for i in range(0,10):  # Se guarda en mem la direccion que esta en la instruccion 
            mem[i] = instr[num]
            num += 1
        for i in self.registros:
            if i.iden == reg:
                self.memoria.setDir(self.binarioDecimal(mem), i.palabra)

    # Si el indicador de la alu es alguno, se salta a la posicion de memoria especificada
    def saltarCo(self, instr):
        mem = [0,0,0,0,0,0,0,0,0,0]
        num = 6
        for i in range(0,10):  # Se guarda en mem la direccion que esta en la instruccion 
            mem[i] = instr[num]
            num += 1    
        self.regs[1][1] = mem
        self.disminuirPos()

    # Copia el contenio del primer registro en el segundo
    def copiarCo(self, instr):
        reg1 = [instr[12], instr[13]]
        reg2 = [instr[14], instr[15]]
        for i in self.registros:
            if i.iden == reg2:
                for j in self.registros:
                    if j.iden == reg1:
                        i.palabra = j.palabra
                        break
    
    #Suma el contenido de dos registros y el resultado  y el resultado se almacena en el primero de ellos
    def sumarCo(self, instr):
        print("esta sumando")
        reg1 = [instr[12], instr[13]]
        reg2 = [instr[14], instr[15]]
        for i in self.registros:
            if i.iden == reg1:
                for j in self.registros:
                    if j.iden == reg2:
                        self.alu.suma(i, j)
                        break
    
    #Resta el contenido de dos registros y el resultado  y el resultado se almacena en el primero de ellos
    def restaCo(self, instr):
        reg1 = [instr[12], instr[13]]
        reg2 = [instr[14], instr[15]]
        for i in self.registros:
            if i.iden == reg1:
                for j in self.registros:
                    if j.iden == reg2:
                        self.alu.resta(i, j)
                        break

    #Multiplica el contenido de dos registros y el resultado  y el resultado se almacena en el primero de ellos
    def multiCo(self, instr):
        reg1 = [instr[12], instr[13]]
        reg2 = [instr[14], instr[15]]
        for i in self.registros:
            if i.iden == reg1:
                for j in self.registros:
                    if j.iden == reg2:
                        self.alu.multi(i, j)
                        break
    
    #Divide el contenido de dos registros y el resultado  y el resultado se almacena en el primero de ellos, el residuo en el segundo
    def dividirCo(self, instr):
        reg1 = [instr[12], instr[13]]
        reg2 = [instr[14], instr[15]]
        for i in self.registros:
            if i.iden == reg1:
                for j in self.registros:
                    if j.iden == reg2:
                        self.alu.division(i, j)
                        break
    
    # Permite mostrar un contenido de memoria en la salida estandar
    def salidaCo(self, instr):
        mem = [0,0,0,0,0,0,0,0,0,0]
        num = 6
        for i in range(0,10):  # Se guarda en mem la direccion que esta en la instruccion 
            mem[i] = instr[num]
            num += 1
        memn = self.binarioDecimal(mem)
        print("Direccion de memoria:  ", mem)
        print("Resultado en binario:  ", self.memoria.getCode(memn))
        print("Resultado en decimal:  ", self.binarioDecimal(self.memoria.getCode(memn)) )

    #Permite el ingreso de numeros y guardarlos en lugares especificos de memoria
    def entradaCo(self, instr):
        mem = [0,0,0,0,0,0,0,0,0,0]
        num = 6
        for i in range(0,10):  # Se guarda en mem la direccion que esta en la instruccion 
            mem[i] = instr[num]
            num += 1
        print("Numero a guardar en al direccion:  ", mem)    
        num = int(input()) 
        memn = self.binarioDecimal(mem)
        self.memoria.setDecimal(memn, num)  

    def popCo(self,instr):
        reg = [instr[14], instr[15]]
        direccion = self.binarioDecimal(self.SR)
        for i in self.registros:
            if i.iden == reg:
                numeroArr = self.memoria.getCode(direccion)
                i.palabra = numeroArr
        direccion -= 1
        self.SR = self.decimalBinario(direccion)
    
    # Este es el codigo con el cual se hace el push
    def pushCo(self,instr):
        reg = [instr[14], instr[15]]
        direccion = self.binarioDecimal(self.SR)
        direccion += 1
        for i in self.registros:
            if i.iden == reg:
                self.memoria.setDir(direccion, i.palabra)
        self.SR = self.decimalBinario(direccion)

    #Ejecuta un programa almacenado en memoria del cual se obtiene la direccion inicial donde esta almacenado
    def ejecutar(self, dirIns):
        self.regs[1][1] = dirIns
        pasos = 1
        print("\n\n\n       En este punto inicia la ejecució del programa  \n\n\n")

        while self.binarioDecimal(self.regs[1][1]) < 1025:
            print("\n\n\nPaso computacional numero:    ", pasos)
            print("\n\nRegistros de A, B, C y D\n")
            for i in self.regC:
                print(i.nombre, "   ",i.palabra)
            print("\n\nPosiciones de memoria para el almacenaje de variables:   \n")
            self.imprimirCodMem(self.memDatos, 5)
            print("\n\nPosiciones de memoria donde se almacena el programa:   \n")
            self.imprimirCodMem(self.memProg, 15)
            print("\n\nRegistros de la ALU:      \n")
            self.alu.imprimirRegs()
            self.extraer()
            print("\n\nRegistros de la unidad de control:      \n")
            self.imprimirRegs()
            self.decodificar()
            self.aumentarPos()
            pasos+=1
            print("*****************************************************************************")
        print("El programa no tiene fin")

    
    
    # imprimir con direccion de memoria
    def imprimirCodMem(self, ini, cantidad):
        print("                       Valor                             Posición"  )
        for i in range(0, cantidad+8):
            print(self.memoria.memoria[i+ini-4], "        ", i-4+ini)