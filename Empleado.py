from Persona import Personas


class Empleados(Personas):

    codigo = 0
    nivelAcademico = ""
    sueldoBase = 0

    def mostrarDatos(self):
        return super().mostrarDatos(), "codigo ", self.codigo, " nivel academico ", self.nivelAcademico, " salario base ", self.sueldoBase
