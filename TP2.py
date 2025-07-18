# Ejercicio 1: Calculadora de Descuentos
# Crea una función que calcule el precio final de un producto después de aplicar un descuento.
# Requisitos:
# -La función debe recibir el precio original y el porcentaje de descuento.
# -Debe retornar el precio final después del descuento.
# -Incluye un docstring que describa la función, sus parámetros y el valor deretorno.

def calculadora_desc(precio,porcentaje_descuento):
    """
    Calcula el descuento de una compra
    
    Parametros:
    precio(int, float): el precio inicial de la compra.
    porcentaje_descuento(int): porcentaje del descuento de la compra.
    
    Retorna:
    El descuento calculado(float).
    El precio final despues del descuento(float).
    
    """
    desc=precio*porcentaje_descuento/100
    total_desc=precio-desc
    print(f"El descuento es de : {desc}")
    print(f"El precio total despues del descuento es de {total_desc}")

n=float(input("Ingrese el precio de la compra: "))
d=int(input("Ingrese el porcentaje del descuento: "))
calculadora_desc(n,d)

print("--------------------------------------------------------------")

# Ejercicio 2: Conversión de Temperaturas
# Crea una función que convierta temperaturas de Celsius a Fahrenheit o viceversa.
# Requisitos:
# -La función debe recibir la temperatura, la unidad de origen y la unidad de destino.
# -Debe retornar la temperatura convertida.
# -Incluye ejemplos de uso en el docstring.

def conversor_temp(temperatura, unidad, unidad_destino):
    """
    Convierte temperaturas de celsius a fahrenheit o al reves
    
    Parametros:
    -temperatura(int): ingresada por el usuario
    -unidad(input): celsius o fahrenheit, es la unidad en la que esta la temperatura ingresada.
    -unidad_destino(input): celsius o fahrenheit, a que unidad se va a convertir.
    
    Retorna:
    -temperatura_final(int/float): es la temperatura en la que se transforma. 
    
    """
    
    if unidad=="celsius" and unidad_destino=="fahrenheit":
        temperatura_final=(temperatura*1.8)+32
        print(f"Los {temp} grados {uni} a {uni_destino} son {temperatura_final}")
        
    elif unidad=="fahrenheit" and unidad_destino=="celsius":
        temperatura_final=(temperatura_final-32)/1.8
        print(f"Los {temp} grados {uni} a {uni_destino} son {temperatura_final}")
        
    elif(unidad=="celsius" and unidad_destino=="celsius") or (unidad=="fahrenheit" and unidad_destino=="fahrenheit"):
        print("ERROR. Las temperaturas son las mismas")
    else:
        print("ERROR. Las temperaturas estan mal escritas")

temp=int(input("Ingrese una temperatura: "))
uni=input("Ingrese una unidad a convertir(celsius/fahrenheit): ").lower()
uni_destino=input("Ingrese la unidad a la que quiere convertir(celsius/fahrenheit): ").lower()
conversor_temp(temp,uni,uni_destino)

print("--------------------------------------------------------------")

# Ejercicio 3: Verificación de Palíndromos
# Escribe una función que determine si una palabra o frase es un palíndromo.
# Requisitos:
# -La función debe recibir una cadena de texto.
# -Debe retornar True si es un palíndromo y False en caso contrario.

def palindroma(text):
    """
    Comprueba si una cadena de texto es palindroma
    
    Parametros:
    text(input): ingresa una cadena de texto
    
    Retorna:
    -True or False
    
    """
    if text==text[::-1]:
        return True
    else:
        return False

t=input("Ingrese un texto: ").lower()
print(palindroma(t))

print("--------------------------------------------------------------")

# Ejercicio 4: Análisis de Texto
# Crea una función que cuente la cantidad de palabras y caracteres en un texto.
# Requisitos:
# -La función debe recibir una cadena de texto.
# -Debe retornar un diccionario con la cantidad de palabras y caracteres.
# -Documenta claramente la estructura del diccionario en el docstring.

def analisis_txt(texto):
    """
    Cuenta la cantidad de caracteres y palabras de una cadena de texto
    
    Parametros:
    -texto(input): recibe una cadena de texto.
    
    Retorna:
    -dic(diccionario): devuelve un diccionario con las cantidad de caracteres y de palabras.
    
    """
    
    cc=len(texto)
    cp=len(texto.split())
    
    dic={}
    dic["Cantidad caracteres"]=cc
    dic["Cantidad palabras"]=cp
    return dic
    
l=input("Ingrese un texto: ")
print(analisis_txt(l))

print("--------------------------------------------------------------")

#  Ejercicio 5: Generador de Números Primos
#  Escribe una función que genere una lista de números primos hasta un número dado.
#  Requisitos:
#  -La función debe recibir un número entero positivo.
#  -Debe retornar una lista con todos los números primos hasta ese número.
#  -Incluye en el docstring una explicación sobre qué es un número primo.

def generar_primos(nro):
    """
    Genera una lista de números primos desde 2 hasta un número dado (inclusive).

    Un número primo es un número entero mayor que 1 que solo tiene dos divisores: 
    él mismo y el 1. Es decir, no puede dividirse exactamente (sin decimales) 
    por ningún otro número que no sea 1 o él mismo.

    Parámetros:
    - hasta (int): número entero positivo hasta el cual se buscarán números primos.

    Retorna:
    - lista de números primos desde 2 hasta 'hasta'.
    """
    primos = []
    for n in range(2, nro + 1):
        es_primo = True
        if n == 2:
            primos.append(n)
            continue
        if n % 2 == 0:
            continue
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
    return primos

n=int(input("Ingrese un nro: "))

print(generar_primos(n))

print("--------------------------------------------------------------")

#  Ejercicio 6: Gestión de Inventario
#  Crea una función que actualice el inventario de una tienda.
#  Requisitos:
#  -La función debe recibir un diccionario representando el inventario y una lista de productos vendidos.
#  -Debe actualizar las cantidades en el inventario y retornar el inventario actualizado.
#  -Incluye en el docstring un ejemplo de entrada y salida.

def gestion_inventario(dicc,list):
    
    """
    Actualiza un inventario dado
    
    Parámetros:
    - dicc: diccionario con productos y cantidades.
    - list: lista con productos vendidos.

    Retorna:
    - diccionario actualizado.
    
    """
    for i in list:
        if i in dicc:
            dicc[i]-=1
        else:
            print(f"El producto {i}, no esta en stock")
    return dicc


inventario={"fruta":15,"verdura":20,"golosina":30,"gaseosa":25,"agua":8}
print(inventario)
lista=[]
print("Mientras No ponga la palabra no, puede seguir ingresando productos")

m=input("Ingrese el producto a comprar: ").lower()
lista.append(m)
while m!="no":
    m=input("Ingrese el producto a comprar: ").lower()
    if m!="no":
        lista.append(m)

print(gestion_inventario(inventario,lista))

print("--------------------------------------------------------------")

#  Ejercicio 7: Validación de Contraseñas
#  Escriba un programa de  Python para convertir una lista de string en una nueva 
#  lista con listas de caracteres utilizando map.
#  Requisitos:
#  -input : ["hola","adios"]
#  -output: [["h","o","l","a"] , ["a","d","i","o","s"]]

def validacion_contra(string):
    """
    Valida la contraseña leyendo cada caracter de una lista y dividiendolos en listas
    
    Parametros:
    -string: Lista de string
    
    Retorna:
    -resultado: lista de caracteres divididos
    
    """
    resultado=list(map(list,string))
    return resultado            
    
lista_string=["hola","adios","buenas"]
print(f"La lista de contraseñas es: {lista_string}")
print(f"La validacion de contraseñas es: {validacion_contra(lista_string)}")

print("--------------------------------------------------------------")

# Ejercicio 8: Cálculo de Estadísticas
#  Crea una función que calcule la media, mediana y moda de una lista de 
# números.
#  Requisitos:
#  -La función debe recibir una lista de números.
#  -Debe retornar un diccionario con la media, mediana y moda.
#  -Incluye en el docstring una explicación de cada estadística y un ejemplo de uso

def calculo_estadisticas(lista):
    
    """
    Calcula Media,Mediana y Moda de una lista dada.
    
    - Media: es el promedio de todos los valores (suma / cantidad).
    - Mediana: es el número del medio si la lista está ordenada.
    - Moda: es el número que más veces se repite.
    
    Parametros:
    -lista(list): lista de enteros que se ordena.
    
    Retorna:
    -dic: diccionario con los resultados de Media,Mediana y Moda.
    
    ejemplo de uso:
    -lista=[1,2,2,3]
    
    -dic={"Media":2,"Mediana":2,"Moda":2}
    """
    
    dic={}
    #ordena lista
    auxlista=sorted(lista)
    c=0
    sum=0
    #Saca la suma de los numeros y los divide(Media)
    for i in (auxlista):
        c+=1
        sum+=i
    total=sum/c
    
    #Saca la (Mediana)
    longitud_lista=len(auxlista)
    if longitud_lista%2==0:
        indice_central1=longitud_lista//2-1
        indice_central2=longitud_lista//2
        indice_central=(indice_central1+indice_central2)/2
    else:
        indice_central=(longitud_lista-1)//2
    
    auxiliar=max(set(auxlista), key=auxlista.count)
    
    dic["Media"]=total
    dic["Mediana"]=indice_central
    dic["Moda"]=auxiliar
    return dic

lista_nros=[1,2,2,3,4,4,4,5,5]
print(calculo_estadisticas(lista_nros))