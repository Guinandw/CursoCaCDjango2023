""" Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
datos.
• mostrar(): Muestra los datos de la persona.
• es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. """

class Persona:
    def __init__(self, nombre = "", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre
    
   
    @property
    def edad(self):
        return  self.__edad
    
        
    @property
    def dni(self):
        return  self.__dni
    
    #se establecieron nombres diferentes a los setters
    @nombre.setter
    def editarnombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    
    @edad.setter
    def editarEdad(self, nuevaEdad):
        self.__edad = nuevaEdad
    
    @dni.setter
    def editarDni(self, nuevoDni):
        self.__dni = nuevoDni
        
    def mostrar(self):
        print(f'Nombre: {self.__nombre} - EDAD: {self.__edad} - DNI: {self.__dni}')
        
    def mayor_de_edad(self):
        if(self.__edad >= 18):
            return True
        else:
            return False
        

""" Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase: 
• Un constructor, donde los datos pueden estar vacíos. 
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero. 
• mostrar(): Muestra los datos de la cuenta. 
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada. 
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos """

class Cuenta:
    #Cuenta se compone de persona sino no existe. Se estableque que el parametro titular es de la clase persona
    def __init__(self, titular: Persona(), cantidad =0):
        self.__titular = titular
        self.__cantidad = cantidad
    
   

    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self, persona:Persona):
        self.__titular = persona
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("Ingrese una cantidad superior a 0")
    
    #ejercicio indica que la cuenta puede estar en numeros rojos. supongo que hace referencia
    #a que puede retirar mas dinero del que se tiene. No hay restricciones con los retiros 
    def retirar(self, cantidad):
            self.__cantidad -= cantidad
        
    def mostrar(self):
        self.__titular.mostrar() 
        print(f'Cantidad: {self.__cantidad}')
        


""" 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta """


class CuentaJoven(Cuenta):
    
    def __init__(self, titular:Persona(), cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
        
    def es_titular_valido(self):
        return self.titular.mayor_de_edad() and self.titular.edad < 25     
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No puede retirar, no cumple con la edad validad para retiros.")
    
    def mostrar(self):
        super().mostrar()
        print(f'Bonificacion {self.__bonificacion}%')
        


will = Persona('Willian', 43, '385489294')
marc = Persona('Marcos', 19, '544780138')
c1 = Cuenta(will, 32000)
cj1 = CuentaJoven(marc, 18000, 10)

c1.mostrar()
cj1.mostrar()

marc.editarEdad = 17

marc.mostrar()
cj1.retirar(16000)

cj1.mostrar()
c1.ingresar(-11)