from Empleado import Empleados


class Ventas(Empleados):
    tipoContratacion = ""
    comisionVentas = 3
    igss=0
    sueldoLiquido=0

    def mostrarDatos(self):
        print(super().mostrarDatos())
        self.igss=super().sueldoBase*4.83/100
        self.sueldoLiquido=super().sueldoBase + self.comisionVentas-self.igss
        print("El igss es: ", self.igss)
        print("El salario liquido: ", self.sueldoLiquido)
        print("tipo de contratación ", self.tipoContratacion)
        print("Comisión sobre las ventas", self.comisionVentas)
        print("Salario liquido ", self.sueldoLiquido)
