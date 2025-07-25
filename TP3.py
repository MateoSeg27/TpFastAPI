# Implementar un sistema de reproducción de música utilizando Programación Orientada a Objetos. Debes evitar el uso de estructuras de control 
# condicional (if, elif, else o match-case) para cambiar entre fuentes de reproducción.

# Descripción:
# Se debe modelar un reproductor de música que puede reproducir sonido desde diferentes fuentes:

# MP3 (por defecto)
# CD
# Consola
# Cada fuente debe tener su propia forma de indicar que está reproduciendo música:

# MP3: "Sonando MP3"
# CD: "Sonando CD"
# Consola: "Sonando Consola"
# El reproductor debe tener un método reproducir() que muestre el mensaje correspondiente según la fuente activa. 
# Además, debe contar con un método cambiar_fuente(nueva_fuente) que permita cambiar la fuente de reproducción sin utilizar estructuras 
# condicionales (if, elif, else, match-case).

# Requisitos Técnicos:
# Utilizar el concepto de polimorfismo para evitar el uso de condicionales.
# Crear una clase Reproductor con los métodos reproducir() y cambiar_fuente(nueva_fuente).
# Crear una clase para cada fuente de sonido (MP3, CD, Consola) con su propia implementación de reproducir().
# El programa debe iniciar con la fuente MP3 por defecto.

# Ejemplo de Uso Esperado:
# reproductor = Reproductor()  
# reproductor.reproducir()  # Salida: "Sonando MP3"

# reproductor.cambiar_fuente(CD())  
# reproductor.reproducir()  # Salida: "Sonando CD"

# reproductor.cambiar_fuente(Consola())  
# reproductor.reproducir()  # Salida: "Sonando Consola"

class MP3:
    def reproducir(self):
        return "Sonando MP3"

class CD:
    def reproducir(self):
        return "Sonando CD"
    
class Consola:
    def reproducir(self):
        return "Sonando Consola"

class Reproductor:
    def __init__(self):
        self._fuente= MP3()
    def cambiar_fuente(self,nueva_fuente):
        self._fuente=nueva_fuente
    def reproducir(self):
        print(self._fuente.reproducir())

reproductor= Reproductor()
reproductor.reproducir()

reproductor.cambiar_fuente(CD())
reproductor.reproducir()

reproductor.cambiar_fuente(Consola())
reproductor.reproducir()