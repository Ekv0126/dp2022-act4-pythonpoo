print("Erick Ramírez Villafuerte")
print("200915472")
print("Actividad No. 4")
        
class textos:
    #atributos de la clase.
    texto1=""
    texto2=""
    promedio=0
    texto3=""
    conteo=0
    num=0
    textocompleto=""
    #métodos de la clase.

    def texto1(self, t1):
        self.texto1=t1

    def texto2(self,t2):
        self.texto2=t2

    def texto3(self,t3):
        self.texto3=t3

    def promedio(self):
        self.promedio=((len(self.texto1)+len(self.texto2)+len(self.texto3))/3)
        print("El promedio de letras qu eposeen las 3 palabras ingresadas es de: ", self.promedio)

    def concatenar(self):
        self.conteo=len(self.texto1+self.texto2+self.texto3)
        if self.conteo>15:
            print("La cantidad de letras de los 3 textos SI supera los 15 caracteres: ", self.conteo)
        else:
            print("La cantidad de letras de los 3 textos NO superan los 15 caracteres. ", self.conteo)

    def mayor(self):
        if ((len(self.texto1)>len(self.texto2))and((len(self.texto1)>len(self.texto3)))):
            print("el texto No. 1 ", self.texto1, " es el mas largo de todos con un total de: ",len(self.texto1)," caracteres" )
        elif ((len(self.texto2)>len(self.texto1))and((len(self.texto2)>len(self.texto3)))):
            print("el texto No 2", self.texto2, " es el mas largo de todos con un total de: ",len(self.texto2)," caracteres" )
        elif ((len(self.texto3)>len(self.texto1))and((len(self.texto3)>len(self.texto2)))):
            print("el texto No 3", self.texto3, " es el mas largo de todos con un total de: ",len(self.texto3)," caracteres" )
        else:
            print("Al parecer los datos ingresados tienen el mismo tamaño")

    def contar(self):
        self.textocompleto=self.texto1+self.texto2+self.texto3
        print(self.textocompleto)
        for i in self.textocompleto:
          #  print(i)
          if i.isnumeric() == True:
              self.num=self.num+1
        print("La cantidad de numeros dentro del texto es de ", self.num)
        
