from math import factorial
#from math import bin

print("Erick Ramírez Villafuerte")
print ("Carné 200915472")
print("Actividad No. 4")

class base10:

    #atributos de clase
    datoNum=0
    fac=0
    contador=0
    variable=1
    bin=0
    cociente=0

    #métodos de clase
    def numero(self,num):
        self.numero = num
        print("El número en base 10 es: ", self.numero)
    
    def factorial(self):
        self.fac=factorial(self.numero)
        print("El factorial del numero ingresado es: ", self.fac)
    
    def prim(self):
        while self.numero<= self.contador:
            if (self.numero % self.variable ==0):
                self.contador=self.contador+1
                print(self.contador)
            self.variable=self.variable+1
            print(self.variable)
        
        if self.contador==2:
            print("El numero ", self.numero," SÏ es primo ")
        else:
            print("El número ", self.numero, " NO es primo")

    def perfecto(self):
        if((self.numero==6)or(self.numero==28)or(self.numero==496)or(self.numero==8128)):
            print("El número ingreasado es perfecto")
        else:
            print("El numero ingresado NO es perfecto")

    def decimal_binario(self):
        self.bin=bin(self.numero)
        print("El número ", self.numero, "en base 10, es equivalente a ",self.bin," En base 2")
