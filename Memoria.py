
class Memoria:
    def __init__(self):
        self.memoria = []
        for i in range(0,1025):
            dir = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.memoria.append(dir)
    
    #Permite asignar un codigo binario a la memoria dada la posición y el valor a asignar
    def setDir(self, direc, code):
        self.memoria[direc] = code
    
    #Permite obtener el codigo binario dada una dirección
    def getCode(self, direc):
        return self.memoria[direc]

    # Se pasa el numero decimal y este se guarda en una direccion especificada
    def setDecimal(self, direc, numero):
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
        self.memoria[direc] = resArr
        if neg:
            self.memoria[direc][0] = 1