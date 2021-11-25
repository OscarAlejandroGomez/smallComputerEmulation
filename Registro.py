
class Registro:
    #Inicializar los 4 registros
    def __init__(self, nombre, iden):
        self.nombre = nombre
        self.palabra = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.iden = iden

    # Se obtiene el numero del registro en codigo binario
    def obtenerPalabra(self):
        word = ''
        for i in range(1, len(self.palabra)):
            word += str(self.palabra[i])
        return word

    # Se obtiene valor decimal almacenado en el registro
    def obtenerDecimal(self):
        valor = int(self.obtenerPalabra(), 2)
        if self.palabra[0] == 1:
            valor *= -1
        return valor    
        
    # Se pasa la palabra desde afuera y se guarda en el registro
    def setPalabra(self, word):
        self.palabra = word
    
    # Se pasa el numero decimal y se setea al registro convirtiendolo en decimal
    def setPalabraDecimal(self, numero):
        neg = False
        if numero < 0:
            neg = True
            numero *= -1    
        word = bin(numero).replace("0b", "")
        arrWord = list(word)
        for i in range(0,len(arrWord)):
            arrWord[i] = int(arrWord[i])
        resArr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        num = 15
        for i in reversed(arrWord):
            resArr[num] = i
            num -=1
        self.palabra = resArr
        if neg:
            self.palabra[0] = 1
        