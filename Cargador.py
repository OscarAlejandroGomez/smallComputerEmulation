class Cargador:

    def __init__(self, archivo, memDatos):
        self.archivo = archivo
        self.memDatos = memDatos
        self.letrasPos = []                 # 0 -> Nombre,    1 -> Dirección
        self.etiquetasPos = []              # 0 -> Nombre,    1 -> Dirección
        self.matriz = []
        self.codigos = []
        self.vacio = [0,0,0,0,  0,0,0,0  ,0,0,0,0,  0,0,0,0]
        self.relocali = ['x','x','x','x','x','x','x','x','x','x']
    
    # Lee linea por linea el archivo y devuelve un arreglo con estos valores 
    def leer(self):
        file1 = open(self.archivo, 'r')
        lines = file1.readlines()
        lineas = []
        for line in lines:
            lineas.append(line.strip()) 
        lineasArr = []
        for linea in lineas:
            datos = list(linea.split(" "))
            lineasArr.append(datos)
        for i in range(len(lineasArr)):
            if len(lineasArr[i]) == 2:
                temp = ['llenar']
                lineasArr[i] = temp+lineasArr[i]
            elif len(lineasArr[i]) == 1:
                temp = ['llenar']
                lineasArr[i] = temp+lineasArr[i]
                lineasArr[i] =  lineasArr[i]+temp
        
        # Se crea el arrelgo con el tamaño correcto de posibles etiquetas
        for i in range(0,len(lineasArr)):
            self.etiquetasPos.append(['Etiqueta', 0])
        self.matriz =  lineasArr

    # Obtenemos todas las etiqueas y se asigna una posicion en memoria en la parte de programa.
    def fillEtiquetas(self):
        for i in range(0,len(self.matriz)):
            etiqueta = self.matriz[i][0] 
            encontrada = False
            if etiqueta != 'llenar':
                for j in self.etiquetasPos:
                    if j[0] == etiqueta:
                        encontrada = True
                        break
                if encontrada == False:
                    self.etiquetasPos[i][0] = etiqueta.replace(':','')
                    self.etiquetasPos[i][1] = i
    
    # Llenamos todos lo nombres que se encuentren en la memoria y se le asigna una posicion de memoria en la parte de datos
    def fillLetras(self):
        for i in range(0, len(self.matriz)):
            parametro = self.matriz[i][2]
            separados = list(parametro.split(','))
            if len(separados) == 2:
                vocal = separados[1]
                encontrado = False
                if vocal.islower():
                    for j in self.letrasPos:
                        if j[0] == vocal:
                            encontrado = True
                            break
                    if encontrado == False:
                        self.letrasPos.append([vocal, self.memDatos])
                        self.memDatos += 1
        
    # Aqui se lee toda la line y se generan listas con codigos binarios
    def acciones(self):
        for i in range(0, len(self.matriz)):
            palabra = self.matriz[i][1]
            if self.testParar(palabra):
                self.codigos.append(self.vacio)
            elif self.testCargar(palabra):
                parametro = self.matriz[i][2]
                separados = list(parametro.split(','))
                reg = self.getReg(separados[0])
                mem = self.decimalBinario(self.getVarPos(separados[1]))
                self.codigos.append(self.cargarGen(reg, mem))    # Aqui se introduce la instruccion resultante al arreglo de codigos 
            elif self.testCargarValor(palabra):
                parametro = self.matriz[i][2]
                separados = list(parametro.split(','))
                reg = self.getReg(separados[0])
                val = self.decimalBinario(int(separados[1]))
                self.codigos.append(self.cargarValorGen(reg, val))
            elif self.testAlmacenar(palabra):
                parametro = self.matriz[i][2]
                separados = list(parametro.split(','))
                reg = self.getReg(separados[0])
                mem = self.decimalBinario(self.getVarPos(separados[1]))
                self.codigos.append(self.almacenarGen(reg, mem))
            elif self.testSaltarSiCero(palabra):
                parametro = self.matriz[i][2]
                #mem = self.decimalBinario(self.getEtiquetaPos(parametro))
                mem = self.relocali
                self.codigos.append(self.satarSiCeroGen(mem))
            elif self.testSaltarSiNeg(palabra):
                parametro = self.matriz[i][2]
                #mem = self.decimalBinario(self.getEtiquetaPos(parametro))
                mem = self.relocali
                self.codigos.append(self.saltarSiNegGen(mem))
            elif self.testSaltarSiPos(palabra):
                parametro = self.matriz[i][2]
                #mem = self.decimalBinario(self.getEtiquetaPos(parametro))
                mem = self.relocali
                self.codigos.append(self.saltarSiPosGen(mem))
            elif self.testSaltarSiDes(palabra):
                parametro = self.matriz[i][2]
                #mem = self.decimalBinario(self.getEtiquetaPos(parametro))
                mem = self.relocali
                self.codigos.append(self.saltarSiDesGen(mem))
            elif self.testSaltar(palabra):
                parametro = self.matriz[i][2]
                #mem = self.decimalBinario(self.getEtiquetaPos(parametro))
                mem = self.relocali
                self.codigos.append(self.saltarGen(mem))
            elif self.testCopiar(palabra):
                parametro = self.matriz[i][2]
                separados = list(parametro.split(','))
                reg1 = self.getReg(separados[0])
                reg2 = self.getReg(separados[1])
                self.codigos.append(self.copiarGen(reg1, reg2))
            elif self.testSumar(palabra):
                parametro = self.matriz[i][2]
                separados = list(parametro.split(','))
                reg1 = self.getReg(separados[0])
                reg2 = self.getReg(separados[1])
                self.codigos.append(self.sumarGen(reg1, reg2))
            elif self.testRestar(palabra):
                parametro = self.matriz[i][2]
                separados = list(parametro.split(','))
                reg1 = self.getReg(separados[0])
                reg2 = self.getReg(separados[1])
                self.codigos.append(self.restarGen(reg1, reg2))
            elif self.testMult(palabra):
                parametro = self.matriz[i][2]
                separados = list(parametro.split(','))
                reg1 = self.getReg(separados[0])
                reg2 = self.getReg(separados[1])
                self.codigos.append(self.multGen(reg1, reg2))
            elif self.testDiv(palabra):
                parametro = self.matriz[i][2]
                separados = list(parametro.split(','))
                reg1 = self.getReg(separados[0])
                reg2 = self.getReg(separados[1])
                self.codigos.append(self.divGen(reg1, reg2))
            elif self.testSalida(palabra):
                parametro = self.matriz[i][2]
                mem = self.decimalBinario(self.getVarPos(parametro))
                self.codigos.append(self.salidaGen(mem))
            elif self.testEntrada(palabra):
                parametro = self.matriz[i][2]
                mem = self.decimalBinario(self.getVarPos(parametro))
                self.codigos.append(self.entradaGen(mem))
            elif self.testPop(palabra):
                parametro = self.matriz[i][2]
                reg = self.getReg(parametro)
                self.codigos.append(self.popGen(reg))
            elif self.testPush(palabra):
                parametro = self.matriz[i][2]
                reg = self.getReg(parametro)
                self.codigos.append(self.pushGen(reg))
            else:
                print("El codigo ensamblador introducido es incorrecto")
                exit()
            
    #Permite imprir los codigos que han generado hasta ahora en forma ordenada
    def imprimirCodigos(self):
        for i in self.codigos:
            print(i)

    #Permite obtener el codigod del registro
    def getReg(self,nombre):
        if nombre == 'A':
            return [0,0]
        elif nombre ==  'B':
            return [0,1]
        elif nombre == 'C':
            return [1,0]
        elif nombre == 'D':
            return [1,1]

    # Permite obtener la posicion de memoria de una variable (minuscuala) dado un nombre
    def getVarPos(self,letra):
        for i in range(0,len(self.letrasPos)):
            if self.letrasPos[i][0] == letra:
                return self.letrasPos[i][1]

    #Permite obtener la direccion de la etiqueta 
    def getEtiquetaPos(self, etiqueta):
        for i in range(0, len(self.etiquetasPos)):
            if self.etiquetasPos[i][0] == etiqueta:
                return self.etiquetasPos[i][1]


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

    # Permite imprimir las instrucciones generadas en codigo de maquina
    def impirmirInst(self):
        for i in self.codigos:
            print(i)

    # Filtros para saber que tipo de palabra se esta leyendo -----------------------------------
    def testParar(self, palabra):
        if palabra == "Parar":
            return True

    # --------------- Cargar un valor en registro desde memoria
    def testCargar(self, palabra):
        if palabra == "Cargar":
            return True 
    def cargarGen(self, reg, mem):
        res = []
        code = [0, 0, 0, 1]
        res = res+code
        res = res+reg
        res = res + mem
        return res
        
    # --------------- Cargar un valor
    def testCargarValor(self, palabra):
        if palabra == "CargarValor":
            return True
    def cargarValorGen(self,reg, val):
        res = []
        code = [0, 0, 1, 0]
        res = res+code+reg+val
        return res

    # --------------- Almacenar un valor
    def testAlmacenar(self, palabra):
        if palabra == "Almacenar":
            return True 
    def almacenarGen(self, reg,mem):
        res = []
        code = [0, 0, 1, 1]
        res = res+code
        res = res+reg
        res = res + mem
        return res
    
    # --------------- Saltar si 0
    def testSaltarSiCero(self, palabra):
        if palabra == "SaltarSiCero":
            return True 
    def satarSiCeroGen(self, mem):
        res = []
        code = [0, 1, 0, 0, 0, 0]
        res = res+code+mem
        return res

    # --------------- Saltar si Negativo
    def testSaltarSiNeg(self, palabra):
        if palabra == "SaltarSiNeg":
            return True 
    def saltarSiNegGen(self, mem):
        res = []
        code = [0, 1, 0, 0, 0, 1]
        res = res+code+mem
        return res

    # --------------- Saltar si Positivo
    def testSaltarSiPos(self, palabra):
        if palabra == "SaltarSiPos":
            return True
    def saltarSiPosGen(self, mem):
        res = []
        code = [0, 1, 0, 0, 1, 0]
        res = res+code+mem
        return res

    # --------------- Saltar si Desbordamiento
    def testSaltarSiDes(self, palabra):
        if palabra == "SaltarSiDes":
            return True
    def saltarSiDesGen(self, mem):
        res = []
        code = [0, 1, 0, 0, 1, 1]
        res = res+code+mem
        return res

    # --------------- Saltar sin ninguna condición
    def testSaltar(self, palabra):
        if palabra == "Saltar":
            return True
    def saltarGen(self, mem):
        res = []
        code = [0, 1, 0, 1, 0, 0]
        res = res+code+mem
        return res

    # --------------- Copiar un registro dentro de otro
    def testCopiar(self, palabra):
        if palabra == "Copiar":
            return True
    def copiarGen(self,reg1,reg2):
        res = []
        code = [0, 1, 1, 0,  0,0,0,0 ,0,0,0,0 ]
        res = code + reg1+reg2
        return res

    # --------------- Sumar un registro con otro
    def testSumar(self, palabra):
        if palabra == "Sumar":
            return True
    def sumarGen(self,reg1,reg2):
        res = []
        code = [0, 1, 1, 0,  0,0,0,0 ,0,0,0,1 ]
        res = code + reg1+reg2
        return res

    # --------------- Restar un registro con otro
    def testRestar(self, palabra):
        if palabra == "Restar":
            return True
    def restarGen(self,reg1,reg2):
        res = []
        code = [0, 1, 1, 0,  0,0,0,0 ,0,0,1,0]
        res = code + reg1+reg2
        return res

    # --------------- Multiplicar un registro con otro
    def testMult(self, palabra):
        if palabra == "Mult":
            return True
    def multGen(self,reg1,reg2):
        res = []
        code = [0, 1, 1, 0,  0,0,0,0 ,0,0,1,1]
        res = code + reg1+reg2
        return res
    
    # --------------- Dividir un registro con otro
    def testDiv(self, palabra):
        if palabra == "Div":
            return True
    def divGen(self,reg1,reg2):
        res = []
        code = [0, 1, 1, 0,  0,0,0,0 ,0,1,0,0]
        res = code + reg1+reg2
        return res

    # --------------- Estandar Output
    def testSalida(self, palabra):
        if palabra == "Salida":
            return True
    def salidaGen(self, mem):
        res = []
        code = [0, 1, 1, 1,  0,1]
        res = res + code + mem
        return res
    
    # --------------- Estandar Input
    def testEntrada(self, palabra):
        if palabra == "Entrada":
            return True
    def entradaGen(self, mem):
        res = []
        code = [0, 1, 1, 1,  1,0]
        res = res + code + mem
        return res
    
    # --------------- Pop al stack
    def testPop(self,palabra):
        if palabra == "Pop":
            return True
    def popGen(self, reg):
        codigo = [1,0,0,0, 0,0,0,0, 0,0,0,0, 0,1]
        res = codigo + reg
        return res

    # --------------- Push al stack
    def testPush(self,palabra):
        if palabra == "Push":
            return True
    def pushGen(self, reg):
        codigo = [1,0,0,0, 0,0,0,0, 0,0,0,0, 1,1]
        res = codigo + reg
        return res


    # Final de los filtros

    # Escribe en codigo maquina el codigo en assemble
    def escribir(self, nombre):
        fileNombre = self.archivo.replace(".txt", "")
        fileNombre = fileNombre + nombre+".txt"
        file = open(fileNombre, 'w')
        for i in self.codigos:
            file.write(str(i)+"\n")


    # Se encarga de convertir el codigo en assembler a un codigo binario
    # que esta incompleto pues en esta etapa el codigo es relozalizable
    def interpretarReloc(self):
        self.leer()
        self.fillEtiquetas()
        self.fillLetras()
        self.acciones()
        self.escribir('Relocalizble')
        print("\n\n\ Incio de la lectura de datos \n\n")
        print("Codigo relocalizable, ")
        print("donde la 'x' indica las posiciones que seran definidas al cargar a memoria el programa:          ")
        self.imprimirCodigos()

    # Se encarga de dado una posicion de memoria en donde cargar el programa
    # poner el codigo binario ya completo en esas posiciones de memoria
    def cargarMemoria(self, memoria):
        print("\n\nIndique la poscición de memoria en donde quiere cargar el programa,")
        print('Debe ser un número menor a 1024, en haya espacio para almacenar el programa y no se solape con')
        print("los espacios destinados a almecenar variables, (recomendado [254, 800])\n")
        memDatos = int(input("Ingrese el valor:     "))
        for i in range(0, len(self.codigos)):
            if self.codigos[i][15] == 'x':
                etiqueta = self.matriz[i][2]
                pos = 0
                for j in self.etiquetasPos:    # Hallar la posicion
                    if j[0] == etiqueta:
                        pos = j[1]
                pos += memDatos
                self.codigos[i] = self.codigos[i][0:6] + self.decimalBinario(pos)
        print("\nCodigo en memoria fija:   \n")
        self.imprimirCodMem(memDatos)
        self.escribir("BinarioFinal")
        for i in range(0,len(self.codigos)):
            memoria.memoria[i+memDatos] = self.codigos[i]
        return memDatos
        
    # imprimir con direccion de memoria
    def imprimirCodMem(self, ini):
        print("                       Valor                             Posición"  )
        for i in range(0, len(self.codigos)):
            print(self.codigos[i], "        ", i+ini)