# 1. Crea una función que reciba una lista de números y la ordene de menor a
# mayor. La función debe devolver la lista ordenada (Debe usar set).
# def ordenar_nros(set):
#     lista_ordenada=sorted(set)
#     print(lista_ordenada)

# a={5,6,1,2,4,3}
# ordenar_nros(a)

print("----------------------------------------------------------------------------")

# 2. Crea un programa que permita crear un conjunto desde cero y después me
# permita eliminar un elemento de un conjunto si está presente en el conjunto.
# n=int(input("Cuantos nros quiere agregar a la lista?: "))
# list=set()
# for i in range (1,n+1):
#     m=int(input(f"Agregue el nro {i}°: "))
#     list.add(m)
# print(list)
    
# def eliminar_nro(set, nro):
#     if nro in set:
#         set.remove(nro)
#     else:
#         print("El nro no esta en la lista")

# numero=int(input("Ingrese el nro para eliminar de la lista: "))
# eliminar_nro(list, numero)
# print(f"Lista sin el nro {numero}")
# print(list)

print("----------------------------------------------------------------------------")

# 3. Dados dos conjuntos de números, escribe un programa para encontrar los
# números que faltan en el segundo conjunto en comparación con el primero y viceversa
# list1={1,2,3,4}
# list2={3,4,5,6}
# print(f"El conjunto 1 es: {list1}")
# print(f"El conjunto 2 es: {list2}")
# print(f"Los numeros que faltan en el conjunto 2 y que estan en el conjunto 1 son: {list1-list2}")
# print(f"Los numeros que faltan en el conjunto 1 y que estan en el conjunto 2 son: {list2-list1}")

print("----------------------------------------------------------------------------")

# 4. Escriba un programa en Python para eliminar todos los duplicados de una
# lista de cadenas dada y devolver una lista de cadenas únicas.

# nombres1=["Mateo","Agustina","Martina","Gaston","Mateo","Martina","Nacho"]
# print(f"Lista con duplicados: {nombres1}")

# nombres_sin_duplicados=list(set(nombres1))
# print(f"Lista sin duplicados: {nombres_sin_duplicados}")

print("----------------------------------------------------------------------------")

# 5. Crea una función llamada factorial que reciba un número entero positivo y
# devuelva su factorial. Ejemplo: factorial(4) debe devolver 24.
# def factorial(num):
#     c=1
#     for i in range(1,num+1):
#         c=c*i
#     print(f"El factorial de {num} es {c}")

# N=int(input("Ingrese un nro para descubrir su factorial: "))
# factorial(N)

print("----------------------------------------------------------------------------")

# 6. Crea una función llamada fibonacci(n) que reciba como parámetro un número
# entero n y devuelva una lista con los primeros n números de la serie de
# Fibonacci. La serie de Fibonacci es una secuencia en la que cada número se
# obtiene sumando los dos anteriores. Comienza así: Ejemplo:

# def fibonacci(n):
#     lista=[0,1]
#     if n<=0:
#         print("ERROR, el nro debe ser mayor a 0")
#     elif n==1:
#         print([0])
#     elif n==2:
#         print([0,1])
#     elif n>=3:
#         for i in range(2,n):
#             siguiente=lista[i-1]+lista[i-2]
#             lista.append(siguiente)
#     print(lista)
        
# n_fibo=int(input("Cuantos nros de la secuencia de fibonacci quiere generar: "))
# fibonacci(n_fibo)

print("----------------------------------------------------------------------------")

# 7- Crea una función recursiva llamada 
# suma_recursiva que reciba un número 
# devuelva la suma de los primeros n números naturales
# def recursiva(N):
#     c=0
#     for i in range(1,N+1):
#         c=c+i
#     print(f"La recursiva de {N} es {c}")

# auxx=int(input("Ingrese un nro: "))
# recursiva(auxx)

print("----------------------------------------------------------------------------")


# 8- Crea una clase Libro con los atributos titulo , autor y año_publicacion. Luego, crea una subclase llamada 
# LibroDigital que tenga un atributo adicional
# class Libro():
#     def __init__(self,titulo,autor,año_publicacion):
#         self.titulo=titulo
#         self.autor=autor
#         self.año_publicacion=año_publicacion

# class LibroDigital(Libro):
#     def __init__(self, titulo, autor, año_publicacion,pagina_descarga):
#         super().__init__(titulo, autor, año_publicacion)
#         self.pagina_descarga = pagina_descarga
        
print("----------------------------------------------------------------------------")    
        
#  9- Dado un texto con información estructurada, escribí un programa que 
# extraiga los datos usando slicing y los devuelva como un diccionario.
#  A partir de un texto como el siguiente, la funcion deberia retornar el siguiente 
# diccionario:

def slicing(text):
    nombre_inicio=text.find("Nombre: ")+len("Nombre: ")
    edad_inicio=text.find("Edad: ")+len("Edad: ")
    ciudad_inicio=text.find("Ciudad: ")+ len("Ciudad: ")
    
    nombre = text[nombre_inicio:text.find("|", nombre_inicio) - 1]
    edad = int(text[edad_inicio:text.find("|", edad_inicio) - 1])
    ciudad = text[ciudad_inicio:]
    
    return{
        "nombre":nombre,
        "edad":edad,
        "ciudad":ciudad  
    }
        
texto="Nombre: Mateo Segura | Edad: 19 | Ciudad: Salta"
print(slicing(texto))