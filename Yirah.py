import sys
import time
import os

def limpiar_pantalla():
     os.system('cls')

def escribir_tiempo_real(texto, retraso=0.05):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()  # Asegura que se imprime en pantalla inmediatamente
        time.sleep(retraso)
    print()

#Crear clase padre personaje
class Personaje:
    def __init__(self, nombre, edad, vida):
        self.nombre = nombre
        self.edad = edad
        self.vida = 100

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad
    
    def setVida(self, vida):
        self.vida = vida

    def getVida(self):
        return self.vida

    def caminar(self):
        return "Estas caminando..."

    def hablar(self):
        return "Estas hablando..."

    def escalar(self):
        return "Estas escalando..."
       
class Guerrero(Personaje):
    def __init__(self):
        super().__init__()
        self.ataque_guerrero = 25
        self.defensa_guerrero = 100

    def accion_atacar(self):
        return (f"{self.getNombre} ha hecho un ataque de {self.ataque_guerrero}")
    
    def accion_defender(self):
        return (f"Has usado una defensa de {self.defensa_guerrero} y es muy efectiva.")

class Caballero(Personaje):
    def __init__(self):
        super().__init__()
        self.ataque_caballero = 33
        self.defensa_caballero = 100
    
    def accion_atacarC(self):
        return (f"{self.getNombre} ha hecho un ataque de {self.ataque_caballero}")
    
    def accion_defenderC(self):
        return (f"Has usado una defensa de {self.defensa_caballero} y es muy efectiva.") 

class Asesino(Personaje):
    def __init__(self):
        super().__init__()
        self.ataque_asesino = 22
        self.defensa_asesino = 100
    
    def accion_atacarC(self):
        return (f"{self.getNombre} ha hecho un ataque de {self.ataque_asesino}")
    
    def accion_defenderC(self):
        return (f"Has usado una defensa de {self.defensa_asesino} y es muy efectiva.")    


lista_personajes = ["Guerrero", "Caballero", "Asesino"]

if __name__ == "__main__":

    escribir_tiempo_real("\tYIRAH\n\tBy: Smough69")
    time.sleep(3)
    escribir_tiempo_real("Bienvenido, ¿Cuál es tu nombre?")
    nombre_jugador = input("Nombre: ")
    repeticion_menu = True
    while repeticion_menu:
        print("Selecciona tu personaje")
        for personaje in lista_personajes:
            print(f"Clase: {personaje}")
        escoger = input("Escribe a que clase perteneces: ")
        if escoger != "Guerrero" and escoger != "Caballero" and escoger != "Asesino":
            limpiar_pantalla()
            print("Por favor escriba correctamente el nombre de la clase a la que pertenece")
        else:
            limpiar_pantalla()
            escribir_tiempo_real(f"Comencemos a escribir tu historia {nombre_jugador}...")
            repeticion_menu = False
