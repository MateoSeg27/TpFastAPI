# Ejercicio 1: "Fuerza de Manos"

# Descripción:
# Se modelará un sistema en el que una persona tiene dos manos, cada una con una capacidad de carga máxima. Además, la persona posee una fuerza total, que representa el peso máximo que puede levantar combinando ambas manos.

# El objetivo es determinar si una persona puede levantar un objeto de determinado peso usando una o ambas manos.

# Requisitos del programa:

# Crear una clase Mano

# Debe tener un atributo para almacenar el peso máximo que puede sostener.
# Debe contener un método para verificar si una mano puede sostener un objeto por sí sola.
# Crear una clase Persona

# Debe tener dos manos.
# Debe tener un atributo que represente su fuerza total (peso máximo que puede levantar sumando ambas manos).
# Debe incluir un método que reciba un peso y determine si la persona puede levantarlo con una sola mano o con ambas.
# Casos de prueba esperados:

# Una persona con suficiente fuerza total y con manos capaces de sostener el objeto, debe poder levantarlo.
# Si el objeto es demasiado pesado para una sola mano pero no para ambas juntas, debe levantarlo con ambas manos.
# Si el objeto excede la fuerza total de la persona, no podrá levantarlo.
# Pista:
# Usar POO para estructurar bien las clases y sus relaciones. Definir métodos que permitan tomar decisiones sobre si el objeto puede levantarse o no.

class Mano():
    def __init__(self, peso_max):
        self.peso_max=peso_max
    def puede_sostener(self,peso):
        return peso<=self.peso_max

class Persona:
    def __init__(self, mano_izq, mano_der, capacidad_total):
        self.mano_izq=mano_izq
        self.mano_der=mano_der
        self.capacidad_total=capacidad_total
    
    def puede_levantar(self,peso):
        if self.mano_izq.puede_sostener(peso) or self.mano_der.puede_sostener(peso):
            return "Puede levantarlo con una mano"
        elif peso<=self.capacidad_total:
            return "Puede levantarlo con las dos manos"
        else:
            return "No se puede levantar"

mano_izq = Mano(10)
mano_der = Mano(8)
persona = Persona(mano_izq, mano_der, 15)

print(persona.puede_levantar(7))
print(persona.puede_levantar(16))
print(persona.puede_levantar(15))


print("""--------------------------------------------------------------------------------
      Punto 2-""")

# Ejercicio 2: "Sistema de Compra y Envío de Productos"

# Descripción:
# Se requiere un sistema de compra y venta de productos, donde los usuarios puedan elegir entre diferentes métodos de entrega.

# Cada tipo de servicio de entrega tiene sus propias características, como el costo del envío y el tiempo estimado de entrega.

# Objetivo:
# Diseñar un sistema flexible donde, si en el futuro se agregan nuevos métodos de entrega, no sea necesario modificar el código existente.

# Requisitos del programa:

# Crear una clase Producto

# Debe contener atributos como nombre y precio.
# Crear una clase Pedido

# Debe permitir asociar un producto con un método de envío.
# Debe poder calcular el costo total sumando el precio del producto y el costo del envío.
# Debe poder mostrar el tiempo estimado de entrega según el tipo de envío seleccionado.
# Debe implementar un método especial (__str__) que dé formato legible al pedido para su almacenamiento.
# Persistencia de datos:

# Se debe usar un método estático para registrar los pedidos en un archivo externo.

# Puede ser un archivo .txt o .json (a elección del programador).

# El método debe recibir un pedido y guardar sus datos utilizando el __str__ o convertirlos a formato adecuado para JSON.


# Diferentes tipos de envío

# Crear al menos tres métodos de entrega distintos, por ejemplo:
# Envío estándar: Económico, pero demora más.
# Envío express: Más caro, pero entrega rápida.
# Envío personalizado: Puede tener un costo variable dependiendo de la distancia.
# Casos de prueba esperados:

# Un usuario debe poder elegir el tipo de envío.
# El sistema debe calcular el costo total correctamente.
# Si en el futuro se agregan nuevos métodos de envío, el código debe seguir funcionando sin cambios.
# Pista:
# Organizar el código usando clases y herencia para estructurar los distintos tipos de envío. Asegurar que el sistema sea escalable, 
# permitiendo agregar más opciones sin alterar las clases existentes.  

from abc import ABC, abstractmethod

# Clase Producto
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio


# Clase abstracta MetodoEnvio
class MetodoEnvio(ABC):
    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    @abstractmethod
    def tiempo_entrega(self) -> str:
        pass


# Envío estándar
class EnvioEstandar(MetodoEnvio):
    def calcular_costo(self) -> float:
        return 5.0

    def tiempo_entrega(self) -> str:
        return "5 a 7 días hábiles"


# Envío express
class EnvioExpress(MetodoEnvio):
    def calcular_costo(self) -> float:
        return 15.0

    def tiempo_entrega(self) -> str:
        return "1 a 2 días hábiles"


# Envío personalizado (según distancia)
class EnvioPersonalizado(MetodoEnvio):
    def __init__(self, distancia_km: float):
        self.distancia_km = distancia_km

    def calcular_costo(self) -> float:
        return 0.5 * self.distancia_km  # $0.5 por km

    def tiempo_entrega(self) -> str:
        return f"{1 + self.distancia_km // 50:.0f} días estimados"


# Clase Pedido
class Pedido:
    def __init__(self, producto: Producto, metodo_envio: MetodoEnvio):
        self.producto = producto
        self.metodo_envio = metodo_envio

    def calcular_total(self) -> float:
        return self.producto.precio + self.metodo_envio.calcular_costo()

    def tiempo_entrega(self) -> str:
        return self.metodo_envio.tiempo_entrega()

    def __str__(self) -> str:
        return (f"Producto: {self.producto.nombre}, "
                f"Precio: ${self.producto.precio:.2f}, "
                f"Envío: ${self.metodo_envio.calcular_costo():.2f}, "
                f"Total: ${self.calcular_total():.2f}, "
                f"Entrega estimada: {self.tiempo_entrega()}")

    @staticmethod
    def guardar_pedido_txt(pedido, archivo='pedidos.txt'):
        with open(archivo, 'a') as f:
            f.write(str(pedido) + '\n')


# CASOS DE PRUEBA

producto1 = Producto("Teclado Mecánico", 100)
envio1 = EnvioEstandar()
pedido1 = Pedido(producto1, envio1)
print(pedido1)
Pedido.guardar_pedido_txt(pedido1)

producto2 = Producto("Notebook", 1200)
envio2 = EnvioExpress()
pedido2 = Pedido(producto2, envio2)
print(pedido2)
Pedido.guardar_pedido_txt(pedido2)

producto3 = Producto("Escritorio Gamer", 300)
envio3 = EnvioPersonalizado(distancia_km=120)
pedido3 = Pedido(producto3, envio3)
print(pedido3)
Pedido.guardar_pedido_txt(pedido3)