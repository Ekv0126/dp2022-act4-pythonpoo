from actividad4_2 import salario

planilla=salario()

planilla.salarioBase(int(input("Ingrese el salario base del empleado: ")))
planilla.venta(int(input("Ingrese el total de ventas del empleado: ")))

planilla.comision()
planilla.obtenerIgss()
planilla.cuentaAhorro()
planilla.totalGanancias()
planilla.totalDesc()
planilla.salLiquido()


