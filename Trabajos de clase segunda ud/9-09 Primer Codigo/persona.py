class Persona:
    nombre = ""
    edad = 0
    estatura = 0
    peso = 0
    
    
    #Metodo del constructor
    def __init__(self, nombre, edad, estatura, peso):
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
    #Primer metodo
    def mostrar_info(self):
        print("Nombre: ", self.nombre)
        print("Nombre: ", self.edad)
        print("Nombre: ", self.estatura)
        print("Nombre: ", self.peso)
        
        