print("Erick Ramírez Villafuerte")
print("200915472")
print("Actividad No. 4")

class salario:
    #atributos de la clase.
    salarioBase=0
    comisionVenta=0
    igss=0
    ahorro=0
    totalGanado=0
    totalDescuentos=0
    sueldoLiquido=0

    def salarioBase(self,sB):
        self.salarioBase=sB
        print("El salario ingresado es de: ", self.salarioBase)
    
    def venta(self,v):
        self.venta=v
        print("El total de ventas generadas es: ", self.venta)

    def comision(self):
        self.comisionVenta=self.venta*10/100
        print("La comisoón sobre ventas es de: ", self.comisionVenta)

    def obtenerIgss(self):
        self.igss=self.salarioBase*4.32/100
        print("El total del descuesto por servicio de IGSS es de: ", self.igss)

    def cuentaAhorro(self):
        self.ahorro=(self.salarioBase+self.venta+self.comisionVenta)*.07
        print("El total de ahorro sobre ganancias es: ", self.ahorro)
    
    def totalGanancias(self):
        self.totalGanado=self.salarioBase+self.comisionVenta+250
        print("El total de ganancias del empleado es de: ", self.totalGanado)

    def totalDesc(self):
        self.totalDescuentos=self.ahorro+self.igss
        print("El total de desucentos para el empleado es de: ", self.totalDescuentos)

    def salLiquido(self):
        self.sueldoLiquido=self.totalGanado-self.totalDescuentos
        print("El salario liquido del trabajador es de: ", self.sueldoLiquido)